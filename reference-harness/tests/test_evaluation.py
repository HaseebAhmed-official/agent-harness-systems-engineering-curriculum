from __future__ import annotations

import copy
import json
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path
from typing import cast

from agent_harness import (
    EvalPolicy,
    EvalTask,
    Harness,
    ModelTurn,
    ScriptedProvider,
    run_eval,
)
from agent_harness.contracts import RunResult, StopReason
from agent_harness.corpus import (
    grade_observation,
    load_corpus,
    run_corpus,
    validate_corpus,
    wilson_interval,
)
from agent_harness.runtime import Policy
from agent_harness.testing import Grader


class EvaluationTests(unittest.TestCase):
    def test_repeated_trials_report_pass_rate_and_keep_runs(self):
        task = EvalTask(
            task_id="final-answer",
            prompt="answer",
            grader=lambda run: (run.output == "ok", "output must equal ok"),
        )

        report = run_eval(
            [task],
            lambda _task, trial: Harness(
                ScriptedProvider([ModelTurn(content="ok" if trial < 3 else "bad")])
            ),
            policy=EvalPolicy(
                trials_per_task=3,
                min_overall_pass_rate=2 / 3,
                min_task_pass_rate=2 / 3,
            ),
        )

        self.assertAlmostEqual(2 / 3, report.pass_rate)
        self.assertEqual(3, len(report.trials))
        final_run = report.trials[2].run
        assert final_run is not None
        self.assertEqual("final-answer-3", final_run.session_id)
        self.assertTrue(report.decision.approved)

    def test_critical_failure_rejects_release_even_when_average_passes(self):
        tasks = [
            EvalTask("ordinary", "answer", lambda run: (True, "pass")),
            EvalTask(
                "security",
                "deny",
                lambda run: (run.output == "deny", "must deny"),
                critical=True,
            ),
        ]
        policy = EvalPolicy(
            trials_per_task=2,
            min_overall_pass_rate=0.5,
            min_task_pass_rate=0.0,
            fail_on_critical_trial=True,
        )

        report = run_eval(
            tasks,
            lambda task, _trial: Harness(
                ScriptedProvider(
                    [ModelTurn(content="allow" if task.task_id == "security" else "ok")]
                )
            ),
            policy=policy,
        )

        self.assertFalse(report.decision.approved)
        self.assertIn("at least one critical trial failed", report.decision.reasons)
        self.assertEqual(0.0, report.task_pass_rates["security"])

    def test_zero_trials_is_rejected(self):
        with self.assertRaises(ValueError):
            run_eval(
                [],
                lambda _task, _trial: Harness(ScriptedProvider([])),
                trials_per_task=0,
            )

    def test_infrastructure_failure_vetoes_even_permissive_thresholds(self):
        def broken_factory(_task, _trial):
            raise RuntimeError("synthetic factory failure")

        def broken_grader(_run):
            raise ValueError("synthetic grader failure")

        policy = EvalPolicy(
            trials_per_task=1,
            min_overall_pass_rate=0,
            min_task_pass_rate=0,
            fail_on_critical_trial=False,
        )
        for failure in ("factory", "grader", "invalid_grade"):
            with self.subTest(failure=failure):
                grader = (
                    broken_grader
                    if failure == "grader"
                    else (lambda run: ("yes", "invalid boolean"))
                    if failure == "invalid_grade"
                    else (lambda run: (True, "ok"))
                )
                report = run_eval(
                    # Deliberately cross the typed boundary to test runtime rejection.
                    [EvalTask("infrastructure", "answer", cast(Grader, grader))],
                    broken_factory
                    if failure == "factory"
                    else (
                        lambda task, trial: Harness(
                            ScriptedProvider([ModelTurn(content="ok")])
                        )
                    ),
                    policy=policy,
                )
                self.assertFalse(report.decision.approved)
                self.assertTrue(report.trials[0].infrastructure_error)
                self.assertIn(
                    "evaluation infrastructure failed; release evidence is incomplete",
                    report.decision.reasons,
                )
                self.assertEqual(failure == "factory", report.trials[0].run is None)

    def test_valid_negative_grade_remains_a_task_failure_not_infrastructure(self):
        report = run_eval(
            [
                EvalTask(
                    "ordinary-failure",
                    "answer",
                    lambda run: (False, "incorrect answer"),
                )
            ],
            lambda task, trial: Harness(ScriptedProvider([ModelTurn(content="wrong")])),
            policy=EvalPolicy(
                trials_per_task=1, min_overall_pass_rate=0, min_task_pass_rate=0
            ),
        )
        self.assertFalse(report.trials[0].infrastructure_error)
        self.assertFalse(report.trials[0].passed)
        self.assertTrue(report.decision.approved)


class CorpusTests(unittest.TestCase):
    def setUp(self):
        self.path = Path(__file__).resolve().parents[1] / "evaluation-corpus.json"
        self.corpus = load_corpus(self.path)

    def test_all_contracts_pass_with_state_and_trace_evidence(self):
        report = run_corpus(self.corpus, candidate_revision="test-reference")
        self.assertEqual(
            (20, 20, True), (report["passed"], report["total"], report["approved"])
        )
        self.assertEqual(6, len(report["by_family"]))
        self.assertIsNone(report["confidence_interval"])
        self.assertIsNone(report["provider_cost"])
        self.assertTrue(all(row["run"] and row["state"] for row in report["results"]))
        self.assertEqual(64, len(report["corpus_sha256"]))
        json.dumps(report, allow_nan=False)

    def test_deliberately_permissive_candidate_fails_security_grader(self):
        def permissive(**kwargs):
            kwargs["policy"] = Policy(require_side_effect_approval=False)
            return Harness(**kwargs)

        report = run_corpus(
            self.corpus, candidate_revision="unsafe-control", candidate=permissive
        )
        self.assertFalse(report["approved"])
        no_approval = next(
            row for row in report["results"] if row["task_id"] == "HC-008"
        )
        self.assertEqual([["public", 2]], no_approval["state"]["effects"])
        self.assertIn("effects", no_approval["failed_predicates"])
        self.assertIsNone(no_approval["infrastructure_error"])

    def test_plausible_final_text_cannot_hide_wrong_state(self):
        report = run_corpus(self.corpus, candidate_revision="reference")
        row = report["results"][6]
        expected = self.corpus["tasks"][6]["expected"]
        raw = row["run"]
        run = RunResult(
            raw["session_id"],
            raw["attempt_id"],
            StopReason.FINAL,
            expected["output"],
            raw["turns"],
            raw["tool_calls"],
            (),
        )
        failures = grade_observation(
            expected,
            run,
            {"inventory": {"public": 5, "private": 9}, "reads": [], "effects": []},
        )
        self.assertIn("inventory", failures)
        self.assertIn("effects", failures)
        self.assertNotIn("output", failures)

    def test_corrupted_trace_and_private_state_fail_grading(self):
        # Grade a real run, then alter only evidence whose absence could hide harm.
        from agent_harness.corpus import _fixture

        task = self.corpus["tasks"][0]
        harness, state = _fixture(task, "correlation", Harness)
        run = harness.run("correlation", task["prompt"])
        self.assertEqual([], grade_observation(task["expected"], run, state))
        corrupted = replace(
            run, events=(replace(run.events[0], session_id="wrong"), *run.events[1:])
        )
        self.assertIn(
            "event correlation", grade_observation(task["expected"], corrupted, state)
        )
        state["inventory"]["private"] = 0
        self.assertIn("inventory", grade_observation(task["expected"], run, state))

    def test_infrastructure_failure_retains_all_task_rows_and_denies(self):
        def broken(**kwargs):
            raise RuntimeError("synthetic setup fault")

        report = run_corpus(self.corpus, candidate_revision="broken", candidate=broken)
        self.assertEqual(20, report["total"])
        self.assertEqual(0, report["passed"])
        self.assertFalse(report["approved"])
        self.assertTrue(all(row["infrastructure_error"] for row in report["results"]))

    def test_duplicate_ids_prompts_scenarios_and_cross_split_families_rejected(self):
        for mutation in ("id", "prompt", "scenario", "family"):
            with self.subTest(mutation=mutation):
                corpus = copy.deepcopy(self.corpus)
                first, second = corpus["tasks"][:2]
                if mutation == "id":
                    second["id"] = first["id"]
                elif mutation == "prompt":
                    second["prompt"] = first["prompt"].upper() + "!!!"
                elif mutation == "scenario":
                    second["settings"], second["turns"] = (
                        first["settings"],
                        first["turns"],
                    )
                else:
                    second["split"] = "challenge"
                with self.assertRaises(ValueError):
                    validate_corpus(corpus)

    def test_invalid_corpus_cannot_silently_drop_an_assertion(self):
        for mutation in ("unknown", "empty", "boolean_count", "nan", "bad_version"):
            with self.subTest(mutation=mutation):
                corpus = copy.deepcopy(self.corpus)
                if mutation == "unknown":
                    corpus["tasks"][0]["expected"]["event"] = {}
                elif mutation == "empty":
                    corpus["tasks"] = []
                elif mutation == "boolean_count":
                    corpus["tasks"][0]["expected"]["events"]["tool.started"] = False
                elif mutation == "nan":
                    corpus["tasks"][0]["settings"]["approve_delta"] = float("nan")
                else:
                    corpus["schema_version"] = True
                with self.assertRaises(ValueError):
                    validate_corpus(corpus)

    def test_json_duplicate_keys_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text(
                '{"schema_version": 1, "schema_version": 2}', encoding="utf-8"
            )
            with self.assertRaises(ValueError):
                load_corpus(path)

    def test_renamed_calls_and_explicit_defaults_do_not_hide_duplicate_scenario(self):
        clone = copy.deepcopy(self.corpus["tasks"][1])
        clone["id"] = "HC-021"
        clone["prompt"] = (
            "Superficially different wording for the same executable task."
        )
        clone["turns"][0]["calls"][0]["id"] = "renamed"
        clone["settings"]["cancelled"] = False
        self.corpus["tasks"].append(clone)
        with self.assertRaisesRegex(ValueError, "duplicate executable"):
            validate_corpus(self.corpus)

    def test_misspelled_zero_event_assertion_is_rejected(self):
        self.corpus["tasks"][0]["expected"]["events"]["tool.startted"] = 0
        with self.assertRaisesRegex(ValueError, "unknown event"):
            validate_corpus(self.corpus)

    def test_corpus_hash_changes_with_expected_contract_and_corpus_is_not_mutated(self):
        original = copy.deepcopy(self.corpus)
        first = run_corpus(self.corpus, candidate_revision="reference")
        self.assertEqual(original, self.corpus)
        self.corpus["tasks"][0]["expected"]["public_units"] = 7
        second = run_corpus(self.corpus, candidate_revision="reference")
        self.assertNotEqual(first["corpus_sha256"], second["corpus_sha256"])
        self.assertFalse(second["approved"])

    def test_wilson_matches_known_values_and_retains_uncertainty_at_extremes(self):
        lower, upper = wilson_interval(5, 10)
        self.assertAlmostEqual(0.23659309, lower, places=7)
        self.assertAlmostEqual(0.76340691, upper, places=7)
        self.assertGreater(wilson_interval(0, 10)[1], 0.27)
        self.assertLess(wilson_interval(10, 10)[0], 0.73)
        self.assertAlmostEqual(1 - wilson_interval(2, 10)[1], wilson_interval(8, 10)[0])

    def test_wilson_rejects_invalid_counts_and_confidence(self):
        for args in (
            (0, 0),
            (-1, 10),
            (11, 10),
            (True, 10),
            (1, 1.5),
            (1, 10, 0),
            (1, 10, 1),
            (1, 10, float("nan")),
        ):
            with self.subTest(args=args), self.assertRaises(ValueError):
                wilson_interval(*args)


if __name__ == "__main__":
    unittest.main()
