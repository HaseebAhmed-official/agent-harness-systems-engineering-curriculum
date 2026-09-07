# Reference Harness

This is the curriculum's minimal executable model of a single-agent harness. It exists so learners can trace stable contracts before using a framework.

It includes:

- a provider protocol and deterministic scripted provider
- bounded turns, tool-call budgets, cancellation, and explicit stop reasons
- typed tool registration with a small JSON-Schema subset
- exact-argument approval binding for side-effecting tools
- an opt-in LAB-C6 policy with host-issued per-session resource/destination capabilities and expiring, revocable, single-use approvals
- append-only session messages plus session- and attempt-correlated lifecycle events
- explicit context selection/budget evidence and fail-closed budget errors
- SQLite-backed single-process session/event persistence for reset-recovery labs
- a SQLite durable-task fixture with atomic claims, fenced leases, retry classification, idempotency-intent checks, cooperative cancellation, state-version quarantine, and manual compensation evidence
- repeated-call no-progress detection
- a bounded memory fixture with write policy, provenance, namespace isolation, expiry, retrieval, and deletion
- deterministic routing and sequential fan-out fixtures with budgets and visible partial failure
- pinned capability-adapter and event-exporter ports for protocol/telemetry contract tests
- an optional, exact-version interoperability lane with real MCP discovery/tool validation, A2A JSON-RPC task/artifact exchange plus an authentication boundary, and in-memory OpenTelemetry spans with sensitive content omitted
- repeated-trial evaluation with per-task thresholds and critical-failure release gates
- explicit evaluation-infrastructure failures that veto release even under permissive score thresholds, while retaining available runs for diagnosis
- a versioned 20-task synthetic contract corpus with final-state/trace grading, duplicate and split checks, per-task timing, and a separate Wilson interval math exercise

It intentionally does **not** claim production readiness. It does not provide process isolation, handler timeouts, preemptive cancellation during a call, network egress control, cryptographic identity, full event/log redaction, full JSON Schema, or a network model client. The durable-task fixture is a single-host SQLite teaching model: it has no queue service, worker heartbeat, distributed consensus/lease guarantee, real process-kill harness, or exactly-once external-effect guarantee. Memory is in-process lexical retrieval and fan-out is sequential. The optional interoperability proofs use in-process MCP, in-process ASGI for A2A, and an in-memory OpenTelemetry exporter. They do not prove external network transport, TLS/OAuth, resilient protocol retries, an OTLP backend, SLO operation, protocol certification, or stable GenAI-convention compliance.

The basic `Policy` retains reusable exact approvals for the foundations exercise. Select `ScopedPolicy` from `agent_harness.security` explicitly for the LAB-C6 single-use approval exercise. Its host-only `approve` method must never be exposed as a model tool. Its lock protects grant consumption within one process, not concurrent access to the complete harness. Host session identity, handlers, clock, and unchanged arguments between authorization and dispatch are trusted. Tool-object binding detects replacement and schema/metadata drift; it does not attest installed code or prevent a handler from changing behavior internally. Destination strings are opaque exact allowlisted values; there is no DNS, redirect, socket, filesystem, or tenant isolation enforcement. Grants disappear on restart and are spent before dispatch even if the handler fails after a partial effect. Recovery requires reconciliation and a new host decision.

Run the tests without installing dependencies:

```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests -v
```

Run the exact optional interoperability lane in WSL/Linux:

```bash
uv run --extra interop --locked python -m unittest discover -s tests -v
```

Without the optional extra, four interoperability tests skip explicitly while the dependency-free base suite still runs. `uv.lock` freezes the optional lane's transitive resolution. A release-sensitive teaching run must preserve the Python version, lockfile, test output, and current source pins.

Learners should first pass the complete current suite, then add a changed requirement while preserving contract, policy, state, event, and evaluation evidence. Use the minimal runtime for Semester 1 and the bounded extension fixtures as starting points for LAB-C1 through LAB-C8; passing these fixture tests is not the same as passing those labs.

Run the isolated security starting exercise from this directory with `PYTHONPATH=src` (or the PowerShell equivalent above):

```bash
PYTHONPATH=src python -m unittest discover -s tests -p test_security.py -v
```

The tests use synthetic documents, in-memory effects, and `.invalid` destination strings without network requests. A scripted provider deliberately emits malicious calls: this measures authorization behavior after assumed model compromise, not actual model susceptibility or an attack-success rate. Follow [LAB-C6](../curriculum/labs/advanced-lab-guides.md#lab-c6-agentic-attack-and-mitigation) for the exploit/control comparison, learner extensions, and assessment gate.

Run the LAB-C7 corpus from this directory with `PYTHONPATH=src` set:

```bash
python -m agent_harness.corpus evaluation-corpus.json --candidate-revision YOUR_GIT_COMMIT
```

Replace the revision label with the actual commit and retain any dirty diff. The command prints a JSON evidence report and exits nonzero for failed contracts. It does not write files unless the caller redirects stdout. The report retains corpus hash, Python/platform, per-family results, elapsed fixture/setup/run/grade time, messages, correlated events, final inventory, and read/write journals. It contains synthetic data only. `run_corpus(..., candidate=...)` accepts a compatible harness factory for learner implementations; expected answers are not passed to that factory. In-process candidates remain trusted Python code, so this is not tamper-resistant assessment of hostile code.

The 10 development and 10 public challenge tasks cover six declared families. Validation rejects duplicate IDs, normalized prompts, executable scenarios (including renamed call IDs and explicit defaults), cross-split declared families, unknown fields/events, and malformed expected results. It does not detect arbitrary semantic paraphrases, source overlap, training contamination, or exposure of public challenge answers. Grading is exact for these contracts and can penalize valid alternative wording/behavior outside their scope. An assessor must supply fresh tasks for independent assessment. Timing is local execution cost evidence, not provider latency; provider cost and confidence interval are deliberately `null`. See [LAB-C7](../curriculum/labs/advanced-lab-guides.md#lab-c7-evaluation-corpus-and-regression-gate) for generalization limits and learner extensions.
