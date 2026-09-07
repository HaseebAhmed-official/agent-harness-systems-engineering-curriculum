# Semester 2 Teaching Guide

## Instructor Goal

Teach production judgment under uncertainty and failure. Feature count, autonomy, benchmark scores, and framework vocabulary are not substitutes for secure behavior, recovery, evaluation validity, or operational ownership.

## Delivery Pattern

Each week uses a production case:

1. State requirements, constraints, risk, and decision owner.
2. Predict failure modes before implementation.
3. Compare the simplest valid architectures.
4. Implement or operate one bounded slice.
5. Inject a failure or attack.
6. Inspect traces and end state.
7. Repair and rerun the evidence gate.
8. Defend tradeoffs and residual risk.

## Week-by-Week Guide

### Week 1: Production Requirements

- Teach SLOs, threat/data models, failure domains, capacity, cost, tenancy, and ownership as design inputs.
- Require measurable acceptance and rollback criteria.
- Reject “production-ready” when workload, operator, data, or trust assumptions are unstated.

#### Lesson 1: Turn a Promise Into an Acceptance Contract

Entry: defend the Semester 1 integration packet and distinguish a correct final answer from a verified action. Define the customer, task, eligible population, observation window, data boundary, operator, and consequence of failure before selecting infrastructure.

Worked case: a synthetic internal assistant drafts inventory requests; only a separately authorized operation can reserve an item. A fast HTTP response is not a successful reservation. The release owner wants an illustrative 99% of eligible requests completed correctly within 10 seconds during a fixed observation window. These numbers are invented for arithmetic, not industry requirements or measured user needs.

Separate the service-level indicator (what is measured), objective (the target), and policy (what the team does when evidence misses the target). An SLA adds an agreement and consequences; do not call a classroom target a customer contract. [Google's SLO workbook](https://sre.google/workbook/implementing-slos/), checked 2026-09-07, explains user-oriented indicators, measurement coverage, and error-budget decisions. Its examples do not prescribe this curriculum's thresholds.

Predict the release decision before running this standard-library example:

```python
from fractions import Fraction

eligible, good, unknown = 1000, 985, 5
target = Fraction(99, 100)
assert 0 <= good + unknown <= eligible
allowed_bad = eligible * (1 - target)
observed_not_good = eligible - good  # Includes unknown outcomes.
remaining = allowed_bad - observed_not_good
assert allowed_bad == 10 and remaining == -5
assert Fraction(good, eligible) < target
# A different candidate can meet its SLO and still fail a critical safety gate.
slo_met = Fraction(995, eligible) >= target
unauthorized_effects = 1
release = slo_met and unauthorized_effects == 0
assert slo_met and not release
print("Budget: 10; not-good: 15; remaining: -5; safety veto survives a passing SLO")
```

Instructor key: five unknown outcomes are not successes and must not disappear from the denominator. Report the 985 known-good, 10 known-bad, and 5 unknown cases separately. The negative remaining budget means the invented target was exceeded by five requests; it does not estimate future reliability. Zero eligible traffic means undefined evidence, not 100% success. A security/privacy critical gate is not a spendable error allowance.

Guided specification: draw the request path and list which failures each measurement point misses. A backend log cannot count requests that never reached it without additional ingress/client evidence. Choose units for queue age, deadline, recovery time, throughput, model calls, and cost. Keep estimated cost, token usage, and billed cost separate; record provider/version assumptions rather than inventing prices. Define overload behavior and who may stop execution.

Independent task: use the existing capstone proposal to specify normal, degraded, and forbidden behavior, then implement one measurement with successful, failed, unknown, and no-traffic controls. Predeclare acceptance, stop, rollback, and exception ownership. Report request-level and user/task-family results so an aggregate cannot hide systematic exclusion. No private user data or paid API is required for the baseline.

Pass requires a reproducible numerator/denominator, a decision that follows the declared policy, and an explicit unmeasured boundary. Reject retroactive exclusions made to pass. Remediation: trace one request from arrival through external outcome and identify the first missing observation. Later transfer changes traffic mix and measurement loss; the learner must revise the evidence argument rather than reuse the percentage.

### Week 2: Orchestration Patterns

- Compare deterministic workflows, routing, parallelization, manager, handoff, and evaluator-optimizer.
- Measure added quality against latency, cost, coordination failure, and observability burden.
- Require a simpler baseline and an explicit reason for every agent boundary.

#### Lesson 2: Does Another Worker Improve the Result?

Entry: separate task decomposition, routing, parallel execution, aggregation, and delegation of authority. A manager assigning work is not an authorization server. A handoff transfers specified work/state, not unlimited credentials. An evaluator-optimizer loop requires a stop budget and an evaluator independent enough to detect the candidate's failures.

Run Python examples from `reference-harness` using the documented environment with `PYTHONPATH=src`. No real model or network is used here. Read `orchestration.py` and predict call order, failure reporting, and whether an invalid plan executes any worker.

```python
from agent_harness.orchestration import run_routed, run_fan_out_sequential

calls = []
def stock(task):
    calls.append("stock")
    return "available"
def policy(task):
    calls.append("policy")
    raise RuntimeError("synthetic policy service unavailable")

workers = {"stock": stock, "policy": policy}
routed = run_routed("reserve", "stock", workers)
assert routed.failed_workers == () and calls == ["stock"]
calls.clear()
report = run_fan_out_sequential("reserve", ["stock", "policy"], workers,
                                 max_workers=2)
assert calls == ["stock", "policy"]
assert report.failed_workers == ("policy",)
assert not all(result.ok for result in report.results)
calls.clear()
try:
    run_fan_out_sequential("reserve", ["stock", "missing"], workers, max_workers=2)
except ValueError:
    pass
else:
    raise AssertionError("Unknown worker should reject the whole plan")
assert calls == []
print("Routing ran one worker; sequential fan-out retained failure; invalid plan ran none")
```

Instructor key: the routed call succeeded at obtaining stock text; it did not establish policy approval. The second report retains both results, but supplies no business decision or automatic fail-closed aggregation. The caller must enforce the task's required checks. This fan-out is sequential, not parallel, and synchronous worker calls have no enforced execution timeout. Worker-count bounds do not bound a hanging worker's duration.

Source check, 2026-09-07: [Anthropic's effective-agent guidance](https://www.anthropic.com/engineering/building-effective-agents) distinguishes predefined workflows from model-directed agents and recommends starting with simpler solutions. Treat pattern names as design options, not proof of quality or independent reasoning by multiple models.

Guided comparison: hold an inventory task and its acceptance tests constant across a direct deterministic function, routing, and two-check fan-out. Define which checks are mandatory before execution. Test an ambiguous route, slow/unavailable worker, conflicting outputs, duplicate work, and claimed authority in worker text. A failed optional recommendation may be omitted with disclosure; a failed required authorization check must not be treated as permission.

Independent [LAB-C1 task](../labs/advanced-lab-guides.md#lab-c1-orchestration-pattern-comparison): add the required two patterns beyond the deterministic baseline. If claiming concurrency, capture overlapping start/end intervals and test cancellation and partial failure under actual concurrent execution. Count work and measure end-to-end latency separately; sequential fan-out does not demonstrate speedup. For quality comparisons, use the same held-out tasks, disclosed assistance, and outcome grader; shared model errors can invalidate naive voting assumptions.

Pass requires an allowed positive case, discriminating failure cases, and a justified choice that may be the simpler baseline. Remediation: remove the aggregator's prose and implement its acceptance predicate explicitly. Changed-task transfer removes a worker or replaces it with an untrusted remote service; the learner must restate authority, deadline, and evidence boundaries.

### Week 3: Durable Execution

- Inject crash, duplicate delivery, timeout, partial side effect, and cancellation.
- Distinguish retryable, terminal, compensatable, and human-recovery states.
- Challenge exactly-once claims and require idempotency evidence.

#### Lesson 3: A Dead Worker Does Not Mean No Effect

Entry: explain Semester 1's history recovery and partial-effect examples. Read `DurableTaskStore.claim`, `recover_expired_leases`, and `run_once`. A lease is time-bounded local ownership; fencing rejects stale local completion. Neither stops a previously dispatched external action. Submission deduplication is distinct from effect deduplication.

The following trusted child program commits a task/lease, writes a harmless local receipt, and exits abruptly without completing the task. Only the spawned child calls `os._exit`; do not move that call into the parent or an interactive session. All files live in an automatically cleaned temporary directory. The timeout bounds this known child, not arbitrary descendants or hostile code. The clock is controlled for reproducibility; this is actual process exit, not power-loss, filesystem-failure, or distributed-clock testing.

```python
import os
import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory
from agent_harness.durability import DurableTaskStore, RetryPolicy, TaskState

child = r'''
import os, sys
from pathlib import Path
from agent_harness.durability import DurableTaskStore, RetryPolicy
root = Path(sys.argv[1])
store = DurableTaskStore(root / "work.db", clock=lambda: 100.0)
store.submit("request-1", {"item": "book"}, retry_policy=RetryPolicy(initial_delay=0))
assert store.claim("worker-before-exit", lease_seconds=5) is not None
(root / "effects.txt").write_text("receipt-1\n", encoding="utf-8")
os._exit(23)
'''

for reconcile in (False, True):
    with TemporaryDirectory() as directory:
        root = Path(directory)
        env = dict(os.environ, PYTHONPATH=str(Path("src").resolve()))
        exited = subprocess.run([sys.executable, "-c", child, str(root)],
                                env=env, capture_output=True, text=True, timeout=10)
        assert exited.returncode == 23, (exited.returncode, exited.stderr)
        effects = root / "effects.txt"
        assert effects.read_text(encoding="utf-8").splitlines() == ["receipt-1"]
        with DurableTaskStore(root / "work.db", clock=lambda: 106.0) as store:
            task = store.submit("request-1", {"item": "book"},
                                retry_policy=RetryPolicy(initial_delay=0))
            assert task.state == TaskState.RUNNING and task.result is None
            recovered = store.recover_expired_leases()
            assert len(recovered) == 1 and recovered[0].state == TaskState.WAITING_RETRY
            def activity(work):
                receipts = effects.read_text(encoding="utf-8").splitlines()
                if reconcile and receipts == ["receipt-1"]:
                    return {"receipt": "receipt-1", "reconciled": True}
                with effects.open("a", encoding="utf-8") as output:
                    output.write("receipt-2\n")
                return {"receipt": "receipt-2", "reconciled": False}
            result = store.run_once("worker-after-exit", activity)
            assert result is not None and result.state == TaskState.SUCCEEDED
            assert result.attempt == 2
            count = len(effects.read_text(encoding="utf-8").splitlines())
            assert count == (1 if reconcile else 2)
            print(f"Reconcile={reconcile}: local success, {count} synthetic effect(s)")
```

Instructor key: the task was still running even though the file effect existed. Both recovered runs report local success, but only the reconciled single-task case preserves one effect. Local retry machinery cannot classify the unrecorded effect after abrupt exit. The simple receipt lookup is intentionally limited to one known task/file; it is not a concurrent idempotency service, authenticated receipt, or general reconciliation algorithm. A read-then-write check can race.

Source check, 2026-09-07: [AWS's idempotent-API guidance](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) discusses caller-scoped request identity, changed-intent rejection, atomic recording with mutations, and late requests. Apply those requirements at the effect-owning boundary. A queue's unique key alone cannot make a separate service transactional.

Guided failure matrix: move child exit before dispatch, after the effect, and after local completion. Predict stored state and evidence needed before retry. Change intent under the same key and confirm rejection; do not silently recycle expired keys while delayed requests remain possible. For an unknowable outcome, stop/reconcile or use the fixture's explicit `AmbiguousEffectFailure`/`needs_repair` path rather than issuing another irreversible action. `resolve_manual` records a decision; it does not perform compensation.

Independent [LAB-C2 task](../labs/advanced-lab-guides.md#lab-c2-durable-crash-retry-and-recovery): replace the receipt file with an authorized disposable local service that atomically binds principal, operation key, intent, effect, and receipt. Add concurrent duplicate requests, lost acknowledgments, unavailable reconciliation, stale completion, cancellation, migration, backup/restore, and enforced timeouts. Compare one approved durable engine under the same contract. Use the SQLite mode/patch preflight from Semester 1 before any concurrent WAL exercise.

Pass requires actual process-exit evidence, independent effect counts, a non-duplicating positive control, and explicit ambiguity handling. Reject claims of power-loss resilience, exactly-once external effects, or hostile isolation from this sample. Remediation: identify who owns the atomic effect/receipt transaction and test one crash on each side. Transfer changes the service's retention or idempotency support; a previously safe retry may no longer be safe.

### Week 4: Memory Systems

- Teach indexing, retrieval, reranking, retention, deletion, provenance, isolation, and contamination.
- Measure both benefit and harm; do not grade only retrieval recall.
- Include malicious and stale memories.

#### Lesson 4: Can Deleted Knowledge Reappear?

Entry: separate retrieval visibility from erasure using Semester 1 lesson 12. Draw source -> admitted record -> derived fact -> index -> cache -> export. Provenance identifies dependencies; it is not proof that a source is true. A retention rule applies to named stores and data classes, not an undefined promise to forget everything.

Worked race: an indexing worker reads an old record, deletion removes the currently published index entry, then the worker republishes its stale snapshot. Checking only queries or the state before the worker resumes misses resurrection. This sequential schedule models the race; it is not concurrent or durable storage evidence.

```python
def deletion_schedule(check_generation):
    source = {"S1": "old private fact", "S2": "retained public fact"}
    index = dict(source)
    generation = {"S1": 0, "S2": 0}
    captured_generation, captured_text = generation["S1"], source["S1"]
    del source["S1"]
    generation["S1"] += 1
    index.pop("S1", None)
    assert "S1" not in index
    # In a real store, checking and publishing must share an atomic boundary.
    if not check_generation or captured_generation == generation["S1"]:
        index["S1"] = captured_text
    assert index["S2"] == "retained public fact"
    return index

assert "S1" in deletion_schedule(False)
assert "S1" not in deletion_schedule(True)
print("Stale publication resurrects deletion; generation check blocks this schedule")
```

Instructor key: the positive control retains S2, so an empty/broken index cannot masquerade as successful deletion. The protected schedule assumes a single atomic check/publication step; independent processes need a real transactional or compare-and-set boundary. Deleting/recreating S1 must not reset its generation and admit a stale job. Tombstone retention, worker lifetime, cache rebuild, backups, mixed-source facts, and authorized exports need explicit policies and tests.

Guided comparison: score a fixed task set with no memory, current memory, stale memory, and a malicious instruction embedded in memory. Measure task correctness, relevant retrieval, unauthorized influence, and privacy failures separately. A high recall score cannot cancel a cross-user disclosure. A missing store must trigger the declared safe fallback or visible failure, not fabricated recall.

Independent [LAB-C3 task](../labs/advanced-lab-guides.md#worked-deletion-boundary-exercise): implement the source-to-derived lineage and deletion contract in a durable store. Pause a separate indexing worker after read, delete and commit, then resume publication. Inject restart and partial cleanup, test mixed-origin recomputation, and retain an allowed retrieval control. Use synthetic data and declare which transcripts/exports/backups remain outside the contract. Do not claim physical erasure from one query returning no hits.

Pass requires benefit and harm measurements, durable stale-publication rejection, and an honest per-store deletion report. The printed schedule is only preparation for that gate. Remediation: trace one fact into every derived representation and identify the smallest missing deletion boundary. Later transfer adds a cache or changes the corpus language; learners must reassess guarantees rather than inherit a prior score.

#### Delivery Evidence for Lessons 1-4

These lessons supply worked instruction, explicit prediction keys, failure/control pairs, independent extensions, remediation, and changed-task assessment. The examples are bounded demonstrations, not completed LAB-C1 through LAB-C3. Weeks 5-16 still need comparable instructional development. Full lab execution, independent reproduction, workload calibration, accessibility usability, and measured learner transfer remain required before delivery-readiness claims.

### Week 5: MCP

- Trace host/client/server responsibilities, modern per-request version/capability metadata, discovery, transport, authorization, and legacy-era compatibility boundaries.
- Test error and version behavior.
- Prevent learners from equating discovery with trust.

### Week 6: A2A

- Trace AgentCard, message, task, artifact, parts, streaming, asynchronous state, and bindings.
- Test identity, authorization, duplicate delivery, and task cancellation.
- Compare A2A's system boundary with MCP rather than treating them as interchangeable.

### Week 7: Agentic Threat Modeling

- Start from assets and authority, then model prompt injection, confused deputy, exfiltration, excessive agency, persistence, identity, and supply chain.
- Require exploit preconditions and blast radius, not threat-name lists.

### Week 8: Defense in Depth

- Combine policy, approval, sandbox, filesystem/network controls, secrets, identity, audit, and recovery.
- Test bypasses and stale assumptions.
- Grade residual-risk accuracy and repair evidence.

### Week 9: Evaluation Engineering

- Separate capability, regression, safety, reliability, and production monitoring suites.
- Require repeated trials, grader rationale, disagreement analysis, leakage controls, and thresholds tied to a decision.
- Include trace and end-state grading for side-effecting tasks.

### Week 10: Reliability and Observability

- Define SLOs and error budgets before instrumentation.
- Inject queue pressure, provider degradation, tool failure, and state inconsistency.
- Require timeline reconstruction, mitigation, recovery, and corrective action.

### Week 11: Deployment and Tenancy

- Compare local, container, VM, managed, and distributed boundaries only against stated needs.
- Teach secret/config ownership, migrations, rollback, backups, isolation, and data lifecycle.
- Challenge hostile multi-tenant claims with concrete evidence requirements.

### Week 12: Governance, Privacy, and Accessibility

- Map risk to control, owner, evidence, review cadence, and exception process.
- Address user notice/control, retention/deletion, protected data, incident escalation, accessibility, and human override.
- State when legal or domain-professional review is required.

### Week 13: Framework Adapters

- Hold behavioral requirements constant while changing adapter/framework.
- Identify defaults, hidden state, policy differences, trace semantics, and portability gaps.
- Require contract tests before migration claims.

### Week 14: Product Case Studies

- Use dated primary sources and observable behavior.
- Map product capabilities to stable harness contracts and unknowns.
- Do not infer private architecture or treat marketing pages as security proof.

### Week 15: Capstone Operation and Red Team

- Freeze a release candidate.
- Run the evaluation suite, performance/cost tests, threat scenarios, incident drill, rollback, and evidence audit.
- Block defense if critical findings remain unresolved or falsely downgraded.

### Week 16: Defense and Transfer

- Use a multi-role board: engineering, security, operations, product/governance.
- Ask each learner to trace a withheld failure and adapt one capability under a changed provider, protocol, policy, or tenancy condition.
- Schedule a delayed individual retest for the highest-risk competency.

## Case-Study Selection

Select cases for contrasting architecture, trust, distribution, or operating models. At least one source-visible system should permit code tracing. At least one product case should teach the boundary between public behavior and unknown internal implementation.

OpenClaw remains a useful source-visible operator/platform case. Hermes Agent can support skills/memory/provider and trust-boundary analysis. ChatGPT Work and xAI agent tooling can support product-capability and managed-system analysis. Verify every current claim before delivery.

## Capstone Review Cadence

- proposal: problem, deterministic baseline, agentic justification
- architecture gate: contracts, data, authority, failure, evidence plan
- alpha gate: core path and deterministic tests
- security/evaluation gate: attacks, corpus, graders, thresholds
- release-candidate gate: deployment, SLO, incident, rollback, privacy
- final board: live evidence, oral defense, changed task

## Instructor Readiness Gate

The instructor team must include or consult implementation, security, operations, and assessment expertise; execute all critical labs; calibrate anchor submissions; verify current standards/product sources; and rehearse the capstone incident and red-team scenarios.
