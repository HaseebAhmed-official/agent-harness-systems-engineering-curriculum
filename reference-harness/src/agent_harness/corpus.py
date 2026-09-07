"""Versioned synthetic contract corpus for LAB-C7; not a model benchmark."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import re
from collections import Counter
from collections.abc import Callable
from dataclasses import asdict
from pathlib import Path
from statistics import NormalDist
from time import perf_counter
from typing import Any

from .context import RecentContextBuilder
from .contracts import ModelTurn, RunLimits, RunResult, StopReason, ToolCall, ToolSpec
from .runtime import Harness, ToolRegistry
from .security import Capability, ScopedPolicy
from .testing import ScriptedProvider

EVENT_KINDS = frozenset(
    {
        "run.started",
        "run.finished",
        "run.no_progress",
        "context.built",
        "context.failed",
        "model.requested",
        "model.completed",
        "model.failed",
        "policy.decided",
        "tool.started",
        "tool.completed",
        "tool.failed",
        "tool.rejected",
    }
)


def _canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def _keys(value: Any, required: set[str], optional: set[str] | None = None) -> None:
    if not isinstance(value, dict) or not required <= value.keys():
        raise ValueError(f"object must contain {sorted(required)}")
    if value.keys() - required - (optional or set()):
        raise ValueError("unknown fields in corpus object")


def _text(value: Any) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError("nonempty text is required")


def _integer(value: Any, minimum: int | None = None) -> None:
    if type(value) is not int or (minimum is not None and value < minimum):
        raise ValueError("invalid integer in corpus")


def _pairs(value: Any) -> None:
    if not isinstance(value, list):
        raise TypeError("expected a list of observed resource/value pairs")
    for item in value:
        if not isinstance(item, list) or len(item) != 2:
            raise ValueError("invalid observed resource/value pair")
        _text(item[0])
        _integer(item[1])


def _scenario(settings: dict[str, Any], turns: list[dict[str, Any]]) -> str:
    # Normalize labels/defaults, but retain repeated-ID equivalence classes.
    identities: dict[str, int] = {}
    normalized_turns = []
    for turn in turns:
        calls = []
        for call in turn.get("calls", []):
            identity = identities.setdefault(call["id"], len(identities))
            calls.append([identity, call["tool"], call["arguments"]])
        normalized_turns.append([turn.get("content", ""), calls])
    defaults = {"cancelled": False, **asdict(RunLimits())}
    return _canonical([{**defaults, **settings}, normalized_turns])


def validate_corpus(corpus: dict[str, Any]) -> None:
    """Reject malformed fixtures and known split leakage before any execution."""
    _keys(corpus, {"schema_version", "corpus_id", "provenance", "sampling", "tasks"})
    if type(corpus["schema_version"]) is not int or corpus["schema_version"] != 1:
        raise ValueError("unsupported corpus schema")
    if corpus["sampling"] != "deterministic_contracts":
        raise ValueError("runner supports deterministic contract sampling only")
    _text(corpus["corpus_id"])
    _text(corpus["provenance"])
    if not isinstance(corpus["tasks"], list) or not corpus["tasks"]:
        raise ValueError("nonempty task list required")
    ids: set[str] = set()
    prompts: set[str] = set()
    scenarios: set[str] = set()
    families: dict[str, str] = {}
    for task in corpus["tasks"]:
        _keys(
            task,
            {
                "id",
                "family",
                "split",
                "critical",
                "prompt",
                "rationale",
                "settings",
                "turns",
                "expected",
            },
        )
        for key in ("id", "family", "split", "prompt", "rationale"):
            _text(task[key])
        if (
            task["split"] not in {"development", "challenge"}
            or type(task["critical"]) is not bool
        ):
            raise ValueError("invalid task split or criticality")
        if task["id"] in ids:
            raise ValueError("duplicate task ID")
        ids.add(task["id"])
        prompt = " ".join(re.findall(r"\w+", task["prompt"].casefold()))
        if prompt in prompts:
            raise ValueError("duplicate normalized prompt")
        prompts.add(prompt)
        family = task["family"].strip().casefold()
        if family in families and families[family] != task["split"]:
            raise ValueError("scenario family crosses development/challenge split")
        families[family] = task["split"]
        settings = task["settings"]
        _keys(
            settings,
            set(),
            {
                "approve_delta",
                "cancelled",
                "max_turns",
                "max_tool_calls",
                "max_repeated_call",
                "context_characters",
            },
        )
        for key, value in settings.items():
            if key == "cancelled":
                if type(value) is not bool:
                    raise ValueError("cancelled must be boolean")
            else:
                _integer(value, None if key == "approve_delta" else 1)
        if not isinstance(task["turns"], list):
            raise TypeError("turns must be a list")
        for turn in task["turns"]:
            _keys(turn, set(), {"content", "calls"})
            if not isinstance(turn.get("content", ""), str) or not isinstance(
                turn.get("calls", []), list
            ):
                raise TypeError("invalid scripted turn")
            for call in turn.get("calls", []):
                _keys(call, {"id", "tool", "arguments"})
                _text(call["id"])
                _text(call["tool"])
                if not isinstance(call["arguments"], dict):
                    raise TypeError("scripted arguments must be an object")
        scenario = _scenario(settings, task["turns"])
        if scenario in scenarios:
            raise ValueError("duplicate executable scenario")
        scenarios.add(scenario)
        expected = task["expected"]
        _keys(
            expected, {"stop", "output", "public_units", "reads", "effects", "events"}
        )
        StopReason(expected["stop"])
        if not isinstance(expected["output"], str):
            raise TypeError("expected output must be text")
        _integer(expected["public_units"])
        _pairs(expected["reads"])
        _pairs(expected["effects"])
        if not isinstance(expected["events"], dict):
            raise TypeError("event assertions must be an object")
        for name, count in expected["events"].items():
            _text(name)
            if name not in EVENT_KINDS:
                raise ValueError("unknown event assertion")
            _integer(count, 0)
    _canonical(corpus)


def _unique_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_corpus(path: Path) -> dict[str, Any]:
    corpus = json.loads(
        path.read_text(encoding="utf-8"), object_pairs_hook=_unique_keys
    )
    validate_corpus(corpus)
    return corpus


def wilson_interval(
    successes: int, trials: int, confidence: float = 0.95
) -> tuple[float, float]:
    """Binomial Wilson math exercise; caller must justify independent sampling.

    Never attach this interval to pooled deterministic corpus results. Sources
    and applicability constraints are documented in LAB-C7.
    """
    _integer(trials, 1)
    _integer(successes, 0)
    if successes > trials or isinstance(confidence, bool) or not 0 < confidence < 1:
        raise ValueError("invalid binomial interval inputs")
    quantile = 0.5 + confidence / 2
    if quantile >= 1:
        raise ValueError("confidence rounds to an infinite normal quantile")
    z = NormalDist().inv_cdf(quantile)
    p = successes / trials
    denominator = 1 + z * z / trials
    center = (p + z * z / (2 * trials)) / denominator
    radius = (
        z
        * math.sqrt(p * (1 - p) / trials + z * z / (4 * trials * trials))
        / denominator
    )
    return max(0.0, center - radius), min(1.0, center + radius)


def grade_observation(
    expected: dict[str, Any], run: RunResult, state: dict[str, Any]
) -> list[str]:
    """Use independently held fixture state in addition to candidate traces."""
    failures = []
    for name, actual, target in (
        ("stop", run.stop_reason.value, expected["stop"]),
        ("output", run.output, expected["output"]),
        (
            "inventory",
            state["inventory"],
            {"public": expected["public_units"], "private": 9},
        ),
        ("reads", state["reads"], expected["reads"]),
        ("effects", state["effects"], expected["effects"]),
    ):
        if actual != target:
            failures.append(name)
    counts = Counter(event.kind for event in run.events)
    for kind, count in expected["events"].items():
        if counts[kind] != count:
            failures.append(f"event:{kind}")
    if not run.events or run.events[-1].kind != "run.finished":
        failures.append("missing terminal event")
    if any(
        event.session_id != run.session_id or event.attempt_id != run.attempt_id
        for event in run.events
    ):
        failures.append("event correlation")
    return failures


def _fixture(
    task: dict[str, Any], session_id: str, candidate: Callable[..., Harness]
) -> tuple[Harness, dict[str, Any]]:
    state: dict[str, Any] = {
        "inventory": {"public": 5, "private": 9},
        "reads": [],
        "effects": [],
    }

    def read_units(arguments: Any) -> int:
        key = arguments["resource_id"]
        value: int = state["inventory"][key]
        state["reads"].append([key, value])
        return value

    def add_units(arguments: Any) -> int:
        key, delta = arguments["resource_id"], arguments["delta"]
        state["inventory"][key] += delta
        state["effects"].append([key, delta])
        return int(state["inventory"][key])

    def fail_tool(arguments: Any) -> None:
        raise RuntimeError("synthetic tool unavailable")

    read = ToolSpec(
        "read_units",
        "Read synthetic inventory",
        {
            "type": "object",
            "properties": {"resource_id": {"type": "string"}},
            "required": ["resource_id"],
            "additionalProperties": False,
        },
        read_units,
    )
    write = ToolSpec(
        "add_units",
        "Change synthetic inventory",
        {
            "type": "object",
            "properties": {
                "resource_id": {"type": "string"},
                "delta": {"type": "integer"},
            },
            "required": ["resource_id", "delta"],
            "additionalProperties": False,
        },
        add_units,
        side_effect=True,
    )
    fail = ToolSpec(
        "fail_tool",
        "Always raises for recovery testing",
        {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
        },
        fail_tool,
    )
    registry = ToolRegistry()
    for spec in (read, write, fail):
        registry.register(spec)
    policy = ScopedPolicy(
        {
            session_id: (
                Capability(read, {"resource_id": frozenset({"public"})}),
                Capability(write, {"resource_id": frozenset({"public"})}),
                Capability(fail, {}),
            )
        }
    )
    if "approve_delta" in task["settings"]:
        policy.approve(
            session_id,
            ToolCall(
                "host-grant",
                "add_units",
                {
                    "resource_id": "public",
                    "delta": task["settings"]["approve_delta"],
                },
            ),
            3600,
        )
    turns = [
        ModelTurn(
            turn.get("content", ""),
            tuple(
                ToolCall(
                    call["id"], call["tool"], json.loads(_canonical(call["arguments"]))
                )
                for call in turn.get("calls", [])
            ),
        )
        for turn in task["turns"]
    ]
    context = (
        RecentContextBuilder(task["settings"]["context_characters"])
        if "context_characters" in task["settings"]
        else None
    )
    return candidate(
        provider=ScriptedProvider(turns),
        registry=registry,
        policy=policy,
        context_builder=context,
    ), state


def run_corpus(
    corpus: dict[str, Any],
    *,
    candidate_revision: str,
    candidate: Callable[..., Harness] = Harness,
) -> dict[str, Any]:
    validate_corpus(corpus)
    _text(candidate_revision)
    # A candidate receives no expected answers or mutable corpus metadata.
    corpus = json.loads(_canonical(corpus))
    results = []
    for task in corpus["tasks"]:
        started = perf_counter()
        run = None
        state = None
        infrastructure_error = None
        failures = []
        try:
            session_id = f"corpus-{task['id']}"
            harness, state = _fixture(task, session_id, candidate)
            limits = RunLimits(
                **{
                    key: task["settings"][key]
                    for key in ("max_turns", "max_tool_calls", "max_repeated_call")
                    if key in task["settings"]
                }
            )
            def cancelled(value: bool = task["settings"].get("cancelled", False)) -> bool:
                return value

            run = harness.run(
                session_id,
                task["prompt"],
                limits,
                cancelled,
            )
            failures = grade_observation(task["expected"], run, state)
            messages = [
                asdict(message) for message in harness.store.messages(session_id)
            ]
        except Exception as exc:  # noqa: BLE001 - retain failed measurements.
            infrastructure_error = f"{type(exc).__name__}: {exc}"
            messages = []
        results.append(
            {
                "task_id": task["id"],
                "family": task["family"],
                "split": task["split"],
                "critical": task["critical"],
                "passed": not failures and infrastructure_error is None,
                "failed_predicates": failures,
                "infrastructure_error": infrastructure_error,
                "elapsed_seconds": perf_counter() - started,
                "state": state,
                "run": asdict(run) if run is not None else None,
                "messages": messages,
            }
        )
    passed = sum(row["passed"] for row in results)
    return {
        "corpus_id": corpus["corpus_id"],
        "corpus_sha256": hashlib.sha256(_canonical(corpus).encode()).hexdigest(),
        "candidate_revision": candidate_revision,
        "python": platform.python_version(),
        "platform": platform.platform(),
        "sampling": corpus["sampling"],
        "policy": "all declared contract predicates must pass; any infrastructure failure vetoes",
        "approved": passed == len(results),
        "passed": passed,
        "total": len(results),
        "by_family": {
            family: {
                "passed": sum(
                    row["passed"] for row in results if row["family"] == family
                ),
                "total": sum(row["family"] == family for row in results),
            }
            for family in sorted({row["family"] for row in results})
        },
        "confidence_interval": None,
        "uncertainty_note": "Fixed deterministic public contracts; no independent random sample or model capability estimate.",
        "provider_cost": None,
        "cost_note": "No external model calls; compute cost is not measured.",
        "results": results,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("corpus", type=Path)
    parser.add_argument(
        "--candidate-revision",
        required=True,
        help="Record Git commit and any dirty diff separately",
    )
    args = parser.parse_args()
    report = run_corpus(
        load_corpus(args.corpus), candidate_revision=args.candidate_revision
    )
    print(json.dumps(report, indent=2, allow_nan=False))
    return 0 if report["approved"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
