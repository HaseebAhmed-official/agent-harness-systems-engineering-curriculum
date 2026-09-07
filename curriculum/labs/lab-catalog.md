# Lab Catalog

## Lab Contract

Every lab states prerequisites, environment, risk boundary, source/version baseline, objective, procedure or task contract, required evidence, failure injections, cleanup/rollback, grading criteria, and transfer variation. A lab guide that has not been executed in a clean target environment is `authored`, not `verified`.

## Phase A: Foundation Labs

### LAB-A1: Reproducible Python and Git Environment

Build a typed Python project with tests and a deterministic entry point. Demonstrate a scoped Git change and reproduce it from a clean clone.

### LAB-A2: API, Process, and Failure Tracing

Trace a request through client, process, network, serialization, and state boundaries. Diagnose seeded timeout, authentication, and malformed-response failures.

### LAB-A3: Test-Driven Defect Repair

Reproduce a defect, create a failing regression test, repair the correct layer, and explain why the test rejects an incomplete fix.

### LAB-A4: Baseline Threat Model

Identify assets, actors, trust boundaries, data flows, abuse cases, controls, evidence, and residual risk for a small tool-using application.

## Phase B: Minimal Harness Labs

### LAB-B1: Deterministic Provider Adapter

Define provider request/response contracts and implement a scripted model test double. Verify timeout, malformed output, refusal, and provider-error handling.

### LAB-B2: Bounded Agent Loop

Implement iteration, action/result flow, budgets, cancellation, stop reasons, and no-progress detection. Prove every path terminates or transfers control explicitly.

### LAB-B3: Typed Tool Registry

Implement discovery, input/output schemas, validation, structured errors, side-effect classification, and idempotency metadata. Reject unknown and malformed calls.

### LAB-B4: Context Assembly and Budget

Build instruction/data separation, provenance, relevance/freshness selection, token budgeting, and truncation behavior. Run ablations that reveal context dependence.

### LAB-B5: Session, Event Log, Checkpoint, and Replay

Record append-only lifecycle events, reconstruct session state, checkpoint progress, simulate a crash, resume, and explain deterministic versus nondeterministic replay limits.

### LAB-B6: Policy, Approval, and Execution Boundary

Bind capabilities to policy and approvals, enforce deny-by-default behavior, isolate execution, and test stale approval, argument substitution, and confused-deputy scenarios.

### LAB-B7: Observability and Evaluation Baseline

Emit correlated traces, metrics, logs, events, and artifact references. Define a small task corpus, repeat trials, and grade trace plus end state.

## Phase C: Production Harness Labs

### LAB-C1: Orchestration Pattern Comparison

Implement at least two of routing, parallelization, manager, handoff, or evaluator-optimizer. Compare quality, latency, cost, failure propagation, and human control against a deterministic baseline.

### LAB-C2: Durable Crash, Retry, and Recovery

Inject process loss, timeout, duplicate delivery, partial side effect, and cancellation. Demonstrate idempotency, retry classification, compensation or manual recovery, and auditable state transitions.

### LAB-C3: Memory Contamination and Deletion

Test retrieval quality, stale or malicious memory, cross-session isolation, retention, deletion, and provenance. Measure both task benefit and contamination harm.

### LAB-C4: MCP Integration and Contract Test

Connect a minimal host/client/server path, negotiate capabilities, expose a bounded tool or resource, validate errors and authorization, and test protocol-version assumptions.

### LAB-C5: A2A Task and Artifact Exchange

Publish or consume an AgentCard, exchange messages and tasks, return artifacts, handle async or streaming state, and test identity/auth failure behavior.

### LAB-C6: Agentic Attack and Mitigation

Execute authorized prompt-injection, confused-deputy, exfiltration, excessive-agency, persistence, or supply-chain scenarios. Capture exploit preconditions, blast radius, controls, bypasses, repair, and retest.

### LAB-C7: Evaluation Corpus and Regression Gate

Create realistic tasks, repeated trials, graders, thresholds, leakage controls, and failure taxonomy. Compare capability and regression suites and explain grader disagreement.

### LAB-C8: Observability, SLO, and Incident Simulation

Define service objectives, inject a production-like failure, reconstruct the timeline, mitigate, recover, and write an incident report with corrective actions.

### LAB-C9: Deployment, Tenancy, and Rollback

Deploy in a bounded environment, manage secrets/configuration, test migration and rollback, and defend single-user, team, or multi-tenant trust claims with evidence.

## Phase D: Transfer and Specialization Labs

### LAB-D1: Cross-Framework Portability

Implement one harness contract through two selected SDKs/frameworks. Preserve behavior tests, identify semantic gaps, and avoid framework-specific claims in core architecture.

### LAB-D2: Versioned Product Case Study

Audit one current system such as OpenClaw, Hermes Agent, ChatGPT Work, or xAI agent tooling against the stable contract model. Date product facts and distinguish observed, documented, inferred, and unknown behavior.

### LAB-D3: Tool or Protocol Extension

Build a production-quality tool, plugin, MCP server/client, or A2A adapter with schemas, errors, least authority, tests, release policy, and security review.

### LAB-D4: Local-Model Serving and Routing

Measure model serving, hardware fit, throughput, latency, quality, privacy, failure, and routing tradeoffs. Avoid universal model recommendations.

### LAB-D5: Core Runtime Contribution

Trace an unfamiliar harness/framework code path, reproduce an issue, propose or implement a scoped change, run upstream tests, and document compatibility and maintenance impact.

## Minimum Sets

### One-Semester Foundations Course

LAB-A1 through LAB-A4 and LAB-B1 through LAB-B7, ending with the minimal-harness practical.

### Two-Semester Engineering Program

All Phase A-C labs, LAB-D1, LAB-D2, and one additional specialization lab.

### Enterprise Capability Program

Diagnostic Phase A evidence, LAB-B2 through LAB-B7, LAB-C2, LAB-C6 through LAB-C9, and a role-specific Phase D lab. Use production controls and incident simulations instead of academic-only exercises.

## Verification States

- `authored`: task and evidence contract exist
- `dry-reviewed`: an independent reviewer checked clarity and safety
- `executed`: instructor completed it in the declared environment
- `reproduced`: a second person completed it from clean instructions
- `calibrated`: learner timing, common failures, and grading anchors are evidenced

Only `reproduced` or `calibrated` labs may support a standalone ready-to-teach claim.

## Reference Fixture Verification Ledger

This ledger applies to shared starting fixtures, not to learner completion of the labs they support.

Clean corpus evidence, 2026-09-07: Git archive `9706d44`, fresh WSL `/tmp/harness-9706d44.A9dGoQ`, Python 3.13.9; `uv run --offline --python 3.13 --extra interop --locked python -m unittest discover -s tests` passed 63 tests in 6.995 seconds. The separate `python -m agent_harness.corpus evaluation-corpus.json --candidate-revision 9706d44` invocation through the same uv environment passed 20/20 and reproduced the Windows corpus hash. Three known A2A warnings remained. The starting fixture is `executed`; LAB-C7 remains `authored` pending its representative-workload and independent-evidence requirements. The temporary full report is `/tmp/harness-9706d44.A9dGoQ/corpus-report.json`, regenerable from the commit.

Contract corpus checkpoint, 2026-09-07: Windows Python 3.13.1 passed all 63 exact-dependency tests in 9.081 seconds. The corpus CLI independently ran its 20 fixed contracts and reported 20/20, with canonical hash `8b3bba3c763daa36b77091d89ef855e8c518e6116331e753d283e10b26074e32`. Thirteen new test methods cover corpus validation, duplicate/split errors, intentionally unsafe candidate, misleading output/final state, trace/private-state mutation, infrastructure failure retention, and Wilson interval reference/boundary checks. This is author-executed worktree evidence pending clean archive validation. LAB-C7 remains `authored`: representative real workloads, model sampling, external grading, semantic leakage review, and independent learner reproduction remain required.

Clean evaluator evidence, 2026-09-06: Git archive `1423d88` at `/tmp/harness-1423d88.7iofeT` passed all 50 tests in WSL Python 3.13.9 in 12.421 seconds using `uv run --offline --python 3.13 --extra interop --locked python -m unittest discover -s tests -v`. The existing lockfile and cached dependencies created a fresh environment; three known A2A protobuf warnings remained. This extends `b2a0221` with infrastructure-failure release veto and two regression methods (including multiple failure variants). It is an `executed` starting fixture. LAB-C7 remains `authored`; representative corpus, validated graders, uncertainty/leakage evidence, cost/latency measurement, and independent reproduction are not established by these tests.

Clean security evidence, 2026-09-06: Git archive `b2a0221`, extracted into fresh WSL directory `/tmp/harness-b2a0221.tyzzwz`, passed all 48 tests in 6.949 seconds. Command: `uv run --python 3.13 --extra interop --locked python -m unittest discover -s tests -v`, using CPython 3.13.9 and the committed lockfile on Linux 6.18.33.2 x86-64. Environment creation downloaded Python and installed 47 packages; the reported test duration excludes that setup. Three known upstream A2A protobuf warnings remained. The security starting fixture is `executed`, not `reproduced`; the full LAB-C6 remains `authored`. This supersedes the worktree-only checkpoint below for that commit.

2026-09-06 authorization fixture checkpoint: the existing Windows Python 3.13.1 exact-dependency environment passed all 48 tests in 4.521 seconds, including 14 security methods. The new methods cover vulnerable/protected synthetic export, read-resource and session scope, destination variants, exact single-use approval, expiry/revocation, concurrent consumption, partial-effect retry denial, tool-binding drift, and restart denial. This is an author-executed worktree fixture, not a clean archive or independent reproduction. LAB-C6 remains `authored`; its complete detection/recovery, independently authored variants, memory/supply-chain/identity extension, and practical transfer gate are required by the advanced guide.

| Date | Fixture and environment | State | Observed evidence | Claim boundary |
| --- | --- | --- | --- | --- |
| 2026-08-16 | Git archive of `25d06ae`; fresh WSL `/tmp` extraction; Linux 6.18.33.2 on x86-64; glibc 2.35; CPython 3.14.2; offline wheelhouse; `mcp==2.0.0`, `a2a-sdk==1.1.2`, `opentelemetry-sdk==1.44.0` | `executed` | 24 of 24 tests passed in 3.182 seconds. MCP negotiated `2026-07-28`; A2A completed one JSON-RPC task/artifact exchange and rejected a missing bearer credential; two linked in-memory spans excluded supplied sensitive values. A2A emitted three upstream protobuf `label()` deprecation warnings. | Instructor/self-execution of a bounded fixture only. No independent learner reproduced it. It does not complete or promote LAB-C4, LAB-C5, or LAB-C8, and it does not prove external transport, production auth, resilience, OTLP operation, or protocol certification. |
| 2026-08-16 | Git archive of `ac25d63`; fresh WSL `/tmp` extraction; Linux 6.18.33.2 on x86-64; glibc 2.35; CPython 3.14.2; offline wheelhouse with the exact optional dependency lane | `executed` | 34 of 34 tests passed. The test runner reported 3.150 seconds and the measured command elapsed time was 3.843 seconds. Ten durability cases covered same-intent deduplication and changed-intent rejection, retry classification and exhaustion, close/reopen lease recovery with stale-work fencing, competing claims, idempotent-effect recovery, ambiguous-effect repair, cancellation, and incompatible-state quarantine. | Instructor/self-execution of a bounded single-host SQLite fixture only; LAB-C2 remains `authored`. It does not prove real process killing, enforced handler deadlines, a queue/worker heartbeat, distributed leases or consensus, external-service reconciliation, exactly-once effects, or independent learner reproduction. |
