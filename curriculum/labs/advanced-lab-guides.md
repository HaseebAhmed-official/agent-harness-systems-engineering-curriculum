# Advanced Lab Guides

## Common Production Evidence

Every advanced lab preserves requirements, architecture, source/version baseline, failure injection, trace and end state, security/privacy review, rollback or recovery, measured result, and residual risk. Use bounded disposable environments for attack labs.

The reference harness supplies bounded starting fixtures, not completed advanced labs:

| Labs | Starting code | Learner must still add and prove |
| --- | --- | --- |
| LAB-C1 | `reference-harness/src/agent_harness/orchestration.py` | a second real pattern, timing/cost evidence, concurrency where claimed, authority propagation, and comparative ablation |
| LAB-C2 | `reference-harness/src/agent_harness/durability.py` | real process termination, actual timeout/cancellation boundary, queue/worker contention and heartbeat, external-service reconciliation, migration/backup/restore, chosen delivery semantics, and comparison with an approved durable engine |
| LAB-C3 | `reference-harness/src/agent_harness/memory.py` | durable/indexed retrieval, contamination corpus, privacy/deletion propagation, quality metrics, and unavailable-store behavior |
| LAB-C4 | `reference-harness/src/agent_harness/integration.py` plus the optional MCP proof in `protocol_proofs.py` | external transport, controlled side effect plus harness approval, returned-content injection, disconnect/timeout/retry, legacy compatibility if claimed, and safe protocol traces |
| LAB-C5 | `reference-harness/src/agent_harness/integration.py` plus the optional A2A JSON-RPC/ASGI proof in `protocol_proofs.py` | asynchronous or streaming transition, capability/authorization mismatch, duplicate handling, cancellation/timeout, malformed artifact, remote implementation swap, and safe protocol traces |
| LAB-C6 | `reference-harness/src/agent_harness/security.py` and `reference-harness/tests/test_security.py` | independently authored attack variants, real trust-boundary enforcement where claimed, memory/supply-chain path, detection and recovery evidence, and independent reproduction |
| LAB-C7 | `reference-harness/src/agent_harness/testing.py` | representative corpus, valid graders, repeated nondeterministic trials, uncertainty, leakage controls, latency/cost, and release rationale |
| LAB-C8 | attempt-correlated runtime events, `integration.py`, and the optional in-memory OpenTelemetry proof in `protocol_proofs.py` | production exporter/backend, metrics/logs, correlation contract, redaction verification, SLOs, alerts, injected degradation, and incident reconstruction |

Passing reference tests proves only the local contract examples. It cannot be submitted as advanced-lab evidence without the required extensions and measurements.

## LAB-C1: Orchestration Pattern Comparison

### Objective

Choose the simplest pattern that meets a measurable requirement.

### Task

Implement a deterministic baseline plus two patterns selected from routing, parallelization, manager/orchestrator, handoff, or evaluator-optimizer. Hold task corpus and acceptance criteria constant.

### Required Tests

- route ambiguity and misclassification
- partial parallel failure and slow worker
- delegated authority mismatch
- duplicated or conflicting result
- orchestrator/evaluator loop budget

### Evidence and Gate

Compare success, variance, latency, model/tool calls, cost proxy, failure propagation, trace complexity, and human intervention. Pass only if the selected pattern's added complexity is justified by evidence. Transfer: remove one agent and determine whether quality materially changes.

## LAB-C2: Durable Crash, Retry, and Recovery

### Objective

Preserve correct, auditable state across failures and retries.

### Task

Back the session/event contract with a durable store or approved workflow engine. Model transitions explicitly and inject crash before/after external side effects.

### Required Tests

- retryable provider timeout
- non-retryable validation failure
- duplicate task delivery
- process loss during work
- cancellation during pending work
- partial external side effect
- incompatible state/schema version

### Evidence and Gate

Pass with an idempotency strategy, transition log, checkpoint/recovery result, compensation or manual-repair path, and stated delivery semantics. “Exactly once” requires proof across the external boundary; otherwise reject the claim.

## LAB-C3: Memory Contamination and Deletion

### Objective

Measure whether memory improves tasks without violating isolation, freshness, privacy, or deletion requirements.

### Task

Implement a memory interface with write policy, provenance, retrieval, retention, and deletion. Build a corpus with useful, stale, irrelevant, malicious, and cross-user records.

### Required Tests

- retrieval precision and task effect
- stale contradiction
- injected instruction inside memory
- namespace/tenant isolation
- deletion and downstream cache/index cleanup
- unavailable memory store

### Evidence and Gate

Report benefit, contamination rate, privacy boundary, deletion evidence, failure behavior, and residual risk. Pass only if the system treats retrieved text as untrusted data and does not silently cross isolation boundaries.

## LAB-C4: MCP Integration and Contract Test

### Objective

Integrate an MCP capability while preserving harness policy and observability.

### Task

Pin a current MCP specification/SDK version. Build or use a minimal server and connect it through the harness adapter. Expose one read capability and one controlled side effect.

### Required Tests

- modern per-request version/capability declarations and `server/discover`; if legacy support is claimed, test its initialization-era path separately
- unsupported capability/version behavior
- invalid arguments and server error
- authorization denial
- disconnect, timeout, and retry boundary
- prompt injection in returned content
- side effect still requiring harness approval

### Evidence and Gate

Preserve protocol messages or safe traces, contract tests, policy decisions, and end state. Pass when MCP discovery never bypasses local authority and version assumptions are explicit.

## LAB-C5: A2A Task and Artifact Exchange

### Objective

Exchange delegated work across an agent boundary with explicit identity, lifecycle, and artifacts.

### Task

Pin a current A2A specification/SDK version. Publish or consume an AgentCard, send a task/message, return an artifact, and handle one asynchronous or streaming transition.

### Required Tests

- capability mismatch
- identity/authentication failure
- authorization failure
- duplicate task/message
- cancellation and timeout
- malformed artifact
- untrusted content returned by remote agent

### Evidence and Gate

Pass with a task state diagram, protocol trace, artifact validation, duplicate handling, trust analysis, and local-policy enforcement. Transfer: replace the remote agent with a different implementation while preserving contract tests.

## LAB-C6: Agentic Attack and Mitigation

### Objective

Demonstrate exploitable authority paths and verify layered mitigation.

### Task

Select at least four scenarios spanning prompt injection, confused deputy, exfiltration, excessive agency, persistence/memory, supply chain, identity, or approval mismatch.

### Procedure

1. Declare authorization, data, and containment boundaries.
2. Write exploit success criteria before testing.
3. Capture preconditions, execution path, trace, end state, and blast radius.
4. Implement preventive and detective controls plus recovery.
5. Retest the original exploit and at least one variant.

### Starting Exercise: Compromised Model, Bounded Authority

Prerequisites: LAB-B2 tool validation, LAB-B5 policy, LAB-B6 event reconstruction, and a passing reference-harness base suite. Read `security.py` and `test_security.py` alongside the runtime's authorization-before-dispatch path. No paid model or external service is required. Use a disposable checkout, synthetic documents, and in-memory effects only.

Run from `reference-harness` in WSL/Linux:

```bash
PYTHONPATH=src python -m unittest discover -s tests -p test_security.py -v
```

On PowerShell, set `$env:PYTHONPATH = "src"` before the same `python -m unittest` command. The starting fixture contains 14 test methods; individual methods also exercise variants. Record the actual command, Python version, commit plus any dirty diff, elapsed time, pass/skip counts, and observed effects. Do not infer full lab completion from this count.

Threat model: an attacker controls a retrieved inbox document; assume the model follows its malicious instruction and emits an export call. The host owns session identity, capability scope, registry bindings, clock, and approvals. Handlers and the Python process remain trusted. The private canary is synthetic, and destinations are strings in a local list, never real network endpoints.

1. Before running the tests, predict the allowed operation, stolen resource, effect count, and terminal reason for both policies. Draw `retrieved text -> provider proposal -> schema -> capability -> approval -> handler -> evidence`.
2. Inspect `test_compromised_model_positive_control_and_resource_denial`. The deliberately permissive policy records one unauthorized synthetic export. Repeating the same proposed calls under `ScopedPolicy` must produce zero export effects, `policy_denied`, and no `tool.started` event for the denied call. Explain why a permissive positive control is necessary to show the attack path was reachable.
3. Trace the cross-resource read, unknown host session, changed destination, and model-supplied `approved` flag cases. A tool's read-only classification does not authorize every resource. Schema validity and human-looking text do not grant permission.
4. Trace the approved benign export. It must succeed once. Replay under a new call ID or run attempt, change arguments within an otherwise allowed scope, expire or revoke the grant, and check that authority is not reused. At the exact expiry instant the grant is invalid. The 32 competing authorization attempts must consume only one grant; this does not prove a thread-safe complete runtime.
5. Inspect the partial-effect failure test. The synthetic handler records an effect and then raises. The retry must not produce a second effect. Reconcile the local sink and event record before making a new approval decision; never interpret a failed handler response as proof that no effect occurred.
6. Inspect replacement-tool and schema-change denial. Explain why object/metadata binding can detect these changes but cannot establish package provenance, stop a compromised handler, or enforce OS isolation.

### Required Extensions and Assessment

Submit at least four attack families from the task above. The provided examples can supply a baseline, but at least one family must exercise a separately implemented memory/persistence, supply-chain, or identity path, and each family needs an unseen variant of your own.

| Evidence | Pass condition | Automatic failure |
| --- | --- | --- |
| Threat model and exploit | Controlled preconditions, reachable positive control, explicit attacker and trusted-host powers | Claims a model resisted injection when the provider was scripted |
| Preventive control and benign task | Original and variant denied before their forbidden effects; authorized task still succeeds | Relies only on refusal text or a prompt blacklist; prevents all useful tasks |
| Detection | Correlated attempt/call IDs, policy decisions, expected effect count, and a reproducible detection rule checked against benign traffic | Treats absence of an alert as absence of compromise |
| Recovery | Partial effect inspected, outstanding grants revoked, a fresh policy/restart tested, and new authority issued only after reconciliation | Automatically restores spent approvals or blindly retries ambiguous effects |
| Boundary and transfer | Student explains actual enforcement layer and implements a changed task while preserving evidence | Calls an argument allowlist a network firewall or treats session labels as authentication |

For a network-control claim, add a disposable local service/proxy and prove connection-level denial, redirects, DNS/IP handling, and permitted traffic separately. For a persistence claim, exercise the actual durable store and deletion/recovery path. Do not submit those properties as proven by this in-memory fixture.

Instructor sequence: demonstrate one positive control, ask for predictions before revealing the denial trace, let learners implement a different attack variant unaided, then conduct an oral defense. Record actual learner duration and assistance instead of assuming a timing budget. Oral prompts: Why can read-only tools leak data? What changes if session identity is attacker-controlled? What happens after the effect succeeds but its response is lost? Where must enforcement live if the tool handler itself is malicious?

Source rationale reviewed 2026-09-06: [OWASP AI Agent Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html) supports scoped tools, authorization, untrusted-content handling, approval integrity, and adversarial testing. [MCP security best practices](https://modelcontextprotocol.io/docs/draft/tutorials/security/security_best_practices) supplies a separate confused-deputy/authorization reference; it is a moving draft, not a protocol conformance claim. This fixture's design and results are local engineering evidence and require their own tests. Source sampling is sufficient for these bounded teaching claims; broad model-security effectiveness remains unmeasured.

### Evidence and Gate

Pass when critical paths are blocked or explicitly accepted by an authorized owner, detection evidence is reliable, recovery is rehearsed, and residual risk is not hidden. Do not use real credentials, targets, or third-party data.

## LAB-C7: Evaluation Corpus and Regression Gate

### Objective

Build an evaluation system that can support a release decision.

### Task

Create 20-50 realistic initial tasks or justify a smaller high-cost corpus. Separate capability, regression, security, and reliability subsets. Run repeated trials where behavior is nondeterministic.

### Starting Exercise: Validate the Evaluator

Before interpreting a score, check whether the evaluation produced valid evidence. From `reference-harness`, run `PYTHONPATH=src python -m unittest discover -s tests -p test_evaluation.py -v` in WSL/Linux. On PowerShell, set `$env:PYTHONPATH = "src"` first, then run the same Python command.

The example distinguishes an ordinary failing task from an evaluation infrastructure failure. In `testing.py`, an exception escaping the harness factory, harness run, or grader, or an invalid grader return, sets `TrialResult.infrastructure_error=True` and vetoes release approval regardless of pass-rate thresholds. A valid `(False, reason)` grade is an observed task failure, governed by the declared task/overall thresholds and critical gate. The raw pass rate includes infrastructure failures as failed trials; it must not be presented as a valid model capability estimate when the infrastructure veto is present. Provider/tool errors already captured inside a valid `RunResult` remain observable candidate behavior for a task-specific grader to assess.

1. Predict the decision for a failing ordinary task, a failed critical task, and a grader that raises an exception. Set both rate thresholds to zero only for the fault-injection exercise; even under this permissive policy, broken infrastructure must reject release.
2. Inject a factory exception, a grader exception, and a malformed grade such as `("yes", "reason")`. Assert the infrastructure flag, decision reason, and retained run. A factory failure has no run; a grader failure retains the run that it could not grade. Repair the evaluator and rerun the same corpus. Never count deleting failed trials as repair.
3. Replace a grader that checks only the final text with one that also verifies stop reason, policy events, and independently observed final state. Include a plausible successful answer paired with an unauthorized effect. Record disagreements and adjudicate them against the written task requirements.
4. Add a learner-authored evaluator failure variant, such as a malformed reference answer or an unavailable evidence reader. Prove that it cannot silently become a passing or omitted trial. Explain which failures originate in the candidate and which originate in the measuring system.

The existing five evaluator test methods are regression examples, not a representative task corpus or evidence of grader validity. LAB-C7 still requires the corpus, calibrated graders, uncertainty, leakage analysis, and cost/latency measurements below.

### Maintained Contract Corpus

The repository supplies `reference-harness/evaluation-corpus.json` and its runner `src/agent_harness/corpus.py`. These are original synthetic teaching cases, versioned as `harness-contracts-2026-09-06`. The initial state is public inventory 5, private inventory 9, and empty read/effect journals. Tools read inventory, increment it, or raise a controlled exception. No model subscription, real data, network service, or installation of OpenClaw is required.

| IDs | Family | Split | Contract coverage |
| --- | --- | --- | --- |
| HC-001 to HC-002 | Basic | Development | final answer without actions; legitimate read |
| HC-003 to HC-006 | Validation | Development | missing tool, missing argument repair, boolean/integer confusion, forged approval flag |
| HC-007 to HC-010 | Approval | Development | approved write, missing approval, changed arguments, spent-grant replay |
| HC-011 to HC-012 | Resource | Public challenge | private read denial, exact resource identifiers |
| HC-013 to HC-016 | Budget | Public challenge | repeated-call stop, batched tool budget, turn budget, cancellation |
| HC-017 to HC-020 | Failure | Public challenge | provider exhaustion, duplicate call identities, context overflow, tool error recovery |

After setting `PYTHONPATH=src` from `reference-harness`, run:

```bash
python -m agent_harness.corpus evaluation-corpus.json --candidate-revision YOUR_GIT_COMMIT
```

The revision is caller-supplied provenance, not a verified attestation. Record the real commit and dirty diff. The runner prints JSON and exits 0 only when every declared contract passes. Redirect output to the learner evidence location if required. Retain failed rows; exceptions are infrastructure failures, never omitted trials. The report uses the corpus content hash, every task's expected-versus-observed predicate failures, separate inventory/read/effect state, full synthetic trace, elapsed time, and family denominators. Elapsed time includes fixture setup and grading and excludes environment installation.

First reproduce 20/20 with the reference candidate. Next pass a learner factory through `run_corpus(..., candidate=...)`. It receives provider, registry, policy, and context-builder interfaces, not expected answers. Introduce one deliberately permissive policy and observe security failures; restore policy, then introduce a candidate that returns a convincing answer without performing the required state change. Both must fail the grader. The included tests also alter private state and event correlation to check grader sensitivity. These mutation checks establish only those observed failure detections, not exhaustive grader correctness.

The validator checks duplicate task IDs, normalized identical prompts, equivalent executable scripts after normalizing call IDs/defaults, declared family overlap between splits, duplicate JSON keys, and malformed or unknown assertion fields. Keep duplicate identity patterns when normalizing scripts because repeated IDs are themselves a failure scenario. Invent a changed-ID duplicate and a zero-count misspelled event assertion and confirm validation rejects both before execution. Manually review paraphrases, shared source/templates, and contamination that these checks cannot discover. The challenge split is public and is not a secret or unexposed holdout.

### Uncertainty Exercise

The runner does **not** attach a confidence interval to 20 deterministic contracts. Running the same script 100 times does not create 100 independent observations of model capability. The separate `wilson_interval(successes, trials, confidence=0.95)` function demonstrates the binomial Wilson calculation: 5 successes in 10 trials gives approximately `[0.2366, 0.7634]`; 10 in 10 still has a lower bound below 1. This interval requires a justified sampling model and does not cover distribution shift, grader error, task leakage, or dependence.

Learner task: explain why a pooled interval is inappropriate for this fixed heterogeneous corpus. Then design a small separate nondeterministic experiment with a declared population, independent sampling unit, failure taxonomy, repetition policy, and family reporting. Identify what would invalidate the independence assumption and how you would change the analysis. Actual model use must preserve provider/model configuration and measured usage; local scripted runtime cannot provide those measurements. No universal sample size or quality guarantee is implied.

Research checked 2026-09-06: [Anthropic's agent evaluation guidance](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) distinguishes tasks, trials, graders, traces, and outcomes. [NIST's proportion confidence-interval guidance](https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm) and [Wilson formula reference](https://www.itl.nist.gov/div898/software/dataplot/refman1/auxillar/propconf.htm) support the statistical exercise. The corpus design is an original local implementation; these sources do not validate its representativeness. Research stopped after the scoped claims had primary support and executable checks; model-level effectiveness, grader calibration, and learner transfer remain separate evidence gaps.

### Corpus and Evidence Contract

Keep the initial corpus in one versioned learner artifact with stable task IDs, task family, source/provenance, prompt, starting-state fixture, expected final-state predicates, allowed/forbidden actions, criticality, grading rule, and split. Record corpus hash, harness revision, model/provider configuration when applicable, trial identifiers, and the policy selected before examining held-out results.

Separate development tasks from held-out variants by scenario family and source, not just by prompt spelling. Record exact duplicates, shared templates, near-duplicate judgments, and any overlap with examples supplied to the agent or grader. A public repository cannot promise private holdout secrecy; have the assessor supply a new changed task at assessment time. Keep raw trial outcomes, including errors, and publish exclusions with reasons and denominators.

For nondeterministic trials, state the sampled population and dependence assumptions before reporting intervals. Repeated identical scripted-provider runs do not measure model uncertainty. Report per-family counts and failures beside aggregate rates; correlated retries of one task must not be treated as independent new tasks. Record measured end-to-end latency and actual provider/tool usage where available; label proxies and missing cost information explicitly. Do not tune thresholds on the same held-out outcomes later presented as final validation.

### Required Analysis

- task coverage and representativeness
- contamination/leakage risk
- code/model/human grader validity
- trace versus end-state disagreements
- variance and confidence limits
- severity-weighted failure taxonomy
- latency, cost, tool failure, retry, and human override
- threshold selected before final release verdict

### Evidence and Gate

Pass when another reviewer can reproduce the report and the decision follows predeclared criteria. Averages cannot hide critical safety failures.

## LAB-C8: Observability, SLO, and Incident Simulation

### Objective

Operate the system through degradation and produce actionable learning.

### Task

Define availability, success, latency, recovery, cost, and human-override objectives. Inject provider latency/failure, tool degradation, queue pressure, or state inconsistency.

### Evidence and Gate

Preserve alerts, correlated timeline, diagnosis, mitigation, recovery, user impact, evidence gaps, and corrective actions. Pass when the learner identifies the actual failure layer, restores service within the exercise objective, and adds a regression/control test.

## LAB-C9: Deployment, Tenancy, and Rollback

### Objective

Defend a deployable architecture and its trust claims.

### Task

Deploy the harness in a bounded local, container, VM, or approved managed environment. Define configuration/secrets, network, filesystem, identity, storage, backup, migration, update, and rollback ownership.

### Required Tests

- missing or invalid configuration fails safely
- secret is absent from logs/artifacts
- migration success and failure
- rollback to a compatible version
- backup restore or declared alternative
- cross-session and, if claimed, cross-tenant isolation
- unavailable dependency behavior

### Evidence and Gate

Pass with deployment diagram, runbook, test evidence, rollback result, data lifecycle, and accurate single-user/team/multi-tenant boundary. Do not claim enterprise readiness from containerization alone.
