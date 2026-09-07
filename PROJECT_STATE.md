# Agent Harness Systems Engineering Curriculum - Project State

## Purpose

This is the canonical long-form source of truth for continuing the curriculum after context reset, compaction, or agent handoff. Read it before changing scope or claiming progress. Use `.mentor/MENTOR_STATE.md` for the compact operational checkpoint.

## Vision

Create a platform-agnostic, evidence-driven Agent Harness / Agent Systems Engineering curriculum that can be presented to universities, used by independent learners, and adapted by engineering organizations. A graduate must be able to reason about, build, test, secure, operate, and evolve systems in the class of OpenClaw, Hermes Agent, ChatGPT Work, xAI agent tooling, and future agent products.

This is not a vendor tutorial, a reading list, or a collection of generated documents. The final program must join:

- computer science and software-engineering prerequisites
- agent-loop and harness architecture from first principles
- typed tools, context, memory, sessions, policy, and execution
- durable workflows, multi-agent patterns, MCP, and A2A
- security, safety, privacy, governance, and human approval
- observability, evaluation, reliability, cost, and operations
- implementation labs with executable evidence
- calibrated assessments, oral defense, transfer, and capstones
- current product case studies without making any product the curriculum spine
- source provenance and a maintainable change-control system

The quality target is defensible university and enterprise adoption, not a literal claim of perfection. Maturity claims require observed evidence, not file count, static scores, or self-review.

## Two-Product Boundary

There are exactly two separately versioned products:

1. **Agent Harness Systems Engineering Curriculum**: this repository. It owns the academic program, labs, assessments, reference harness, case studies, sources, and course maintenance.
2. **Elite Mentor OS**: a subject-agnostic Claude Code and Codex mentor plugin in sibling repository `../elite-mentor-os`. It owns generic diagnosis, mentoring, roadmap, review, learning-state, and validation behavior.

Rules:

- The curriculum may integrate with Mentor OS, but must remain teachable without it.
- Mentor OS must not own OpenClaw or any other subject-specific content.
- Product releases, issue tracking, evidence, and roadmaps must remain separate.
- The legacy embedded Mentor OS plugin and marketplace files were removed after the standalone repository was validated and published. The curriculum links to the separate product but does not own its runtime.
- Do not create a third product or duplicate the complete curriculum across old and new trees.

## Current Repositories

Curriculum:

- local: `C:\Users\Administrator\Documents\Codex\2026-04-22-openclaw-search-deeply-on-internet-github\openclaw-mastery`
- branch: `main`
- remote: `https://github.com/HaseebAhmed-official/agent-harness-systems-engineering-curriculum.git`
- latest pushed curriculum migration milestones entering this work: `ed3c956` and `c136a86`; use Git rather than this file for the current head

Paused external product:

- local: `C:\Users\Administrator\Documents\Codex\2026-04-22-openclaw-search-deeply-on-internet-github\elite-mentor-os`
- remote: `https://github.com/HaseebAhmed-official/elite-mentor-os`
- status: separate and frozen by user decision on 2026-08-15; do not inspect, modify, validate, release, or include it in curriculum progress until explicitly resumed

User study environment:

- Windows path: `E:\Study\Openclaw mastery`
- WSL path: `/mnt/e/Study/Openclaw mastery`
- OpenClaw is already installed in the user's WSL Ubuntu environment. Do not divert curriculum work into Windows-side installation checks unless explicitly requested.

## Current Baseline

Latest verified implementation: `9706d44` passed all 63 tests from a clean WSL archive on Python 3.13.9 in 6.995 seconds, using offline locked exact dependencies. Its separate CLI run passed all 20 contracts with the same hash as Windows. This completes the corpus clean-validation step referenced below; next work is representative task/provider evaluation, manually reviewed graders/leakage, source freshness, and delivery/independent learner evidence. Three existing upstream A2A warnings remain. The full temporary report is `/tmp/harness-9706d44.A9dGoQ/corpus-report.json`; regenerate from the commit if unavailable. This is instructor execution, not independent learner reproduction.

2026-09-07 maintained corpus milestone: the reference harness now includes a versioned 20-task deterministic contract corpus across six families, 10 development/10 public challenge tasks, a strict runner with trace plus independent fixture-state grading, corpus hashing, duplicate/split checks, measured local execution times, and a separately tested Wilson interval exercise. All 63 exact-dependency tests passed on Windows Python 3.13.1 in 9.081 seconds, and the CLI passed 20/20 contracts. Ruff, MyPy (20 source/test files), Bandit on source, and whitespace checks passed. LAB-C7 now includes runnable instructions, attack/mutation controls, leakage limits, uncertainty assumptions, source rationale, and required real-workload extensions. This closes the absence of a maintained bounded contract corpus, but does not establish representative model evaluation, independent grader calibration, general leakage detection, or learning effectiveness. Clean WSL validation of this milestone remains pending; prior 50-test clean evidence below remains historical.

Clean security validation recorded 2026-09-06: commit `b2a0221` passed all 48 tests from a fresh WSL Git archive, with CPython 3.13.9 and the committed optional-dependency lock. Test time was 6.949 seconds, excluding downloads/setup; three known A2A protobuf warnings remain. This supersedes the worktree-only security checkpoint below. It is author-executed evidence, not independent lab reproduction.

Evaluator repair `1423d88` validated on Windows and WSL: a pre-fix reproducer returned `approved=True` after a factory exception when both rate thresholds were zero. `testing.py` now distinguishes infrastructure failure and applies an unconditional veto, preserving runs when a grader fails. LAB-C7 now teaches this distinction and specifies corpus provenance, final-state grading, held-out families, dependence assumptions, exclusions, and measured latency/cost evidence. All 50 exact-dependency tests passed on Windows in 2.952 seconds; Ruff, MyPy (19 source/test files), Bandit on source, and Git whitespace checks passed. A fresh Git archive of `1423d88` passed all 50 tests in WSL Python 3.13.9 in 12.421 seconds using `uv run --offline --python 3.13 --extra interop --locked python -m unittest discover -s tests -v`. The temporary directory was `/tmp/harness-1423d88.7iofeT`; three known upstream A2A warnings remained. A maintained representative corpus and validated graders remain unfinished.

2026-09-06 security milestone: the worktree adds an opt-in `ScopedPolicy` fixture and 14 adversarial test methods supporting LAB-C6. Host-issued per-session tool/resource/destination constraints, exact expiring/revocable one-use approvals, atomic in-process grant consumption, changed-tool binding rejection, and partial-effect retry denial are implemented. The advanced lab guide now supplies a runnable starting exercise, vulnerable positive control, benign control, required attack variants, detection/recovery evidence, and oral-defense criteria. All 48 tests passed in the existing Windows Python 3.13.1 exact-dependency environment; Ruff, MyPy (`--check-untyped-defs`, 19 source/test files), Bandit on `src`, four drift-script tests, and Git whitespace checks passed. This is author-run worktree evidence, not independent lab reproduction. The earlier baseline below retains the last clean WSL evidence until a new commit-bound run is recorded.

The platform-agnostic architecture, support-asset migration, advanced interoperability fixture, and bounded durable-execution fixture are fixed through implementation head `ac25d63`. The current tree has 68 curriculum files; 15 reference OpenClaw only in intentional case-study, source, maintenance, comparative, or historical contexts. The embedded Mentor plugin and empty screenshot/manual layer are gone.

The reference harness now covers the minimal runtime plus bounded Semester 2 starting fixtures for memory, orchestration, protocol/telemetry ports, per-attempt events, persistence, policy-based evaluation, and single-host SQLite durable work. The durability fixture includes explicit state/version handling, atomic claims, lease-token fencing, retry and idempotency policy, cancellation, recovery, quarantine, and manual resolution. An optional exact-version lane adds real in-process MCP `2.0.0`, A2A SDK `1.1.2` JSON-RPC/ASGI, and OpenTelemetry SDK `1.44.0` in-memory proofs. All 34 tests passed on Windows and from a clean WSL extraction of Git archive `ac25d63` on 2026-08-16. These fixtures support learning; they do not replace complete labs, independent reproduction, external transports, distributed durability, or production infrastructure.

The consolidated [internal migration audit](Validations/internal-migration-audit-2026-08-15.md) conditionally accepts a strong self-study draft and supervised-pilot candidate, but rejects standalone ready-to-teach, institution-ready, enterprise-ready, and world-class claims at the current evidence level.

### Honest Progress Snapshot

| Scope | Evidence-based completion | Interpretation |
| --- | ---: | --- |
| Platform-agnostic curriculum artifact implementation | about 78% | Canonical/support migration, dated case ledgers, bounded protocol/telemetry and durable-work proofs, and an internal audit exist; provider/security/distributed-systems depth, lab reproduction, and complete delivery evidence remain. |
| Hands-on reproducibility evidence | about 30% | The interoperability and durability starting fixtures were instructor-executed from clean Git archives in fresh WSL, but authored labs have not been independently reproduced or calibrated. |
| Expanded curriculum institution/enterprise proof | about 30% | Alignment and delivery contracts are strong, but no real cohort, measured assessor reliability, full lab reproduction, accessibility audit, or independent adoption evidence exists. |

Percentages are planning estimates, not quality claims. The gate ledger below is authoritative.

## Preserved Strengths

- two-semester instructional structure
- prerequisite bridge and competency framework
- labs, rubrics, practical exams, oral defenses, calibration, and feedback assets
- production, security, operations, extension, and contributor tracks
- release-aware maintenance and source-validation mechanisms
- OpenClaw security/advisory baseline through the August 2026 review
- historical Codex and Claude validation reports

These assets should be migrated and improved, not discarded merely to make the repository look new.

## Material Gaps

### Curriculum Architecture

- The platform-agnostic spine, stable/adapters/case layers, build progression, portability, and alignment matrix are implemented.
- Remaining risk is consistency in less-central historical/maintenance artifacts and absence of independent curriculum architecture review after migration.

### Technical Depth

- The executable reference harness proves deterministic provider behavior, bounded loop, typed tools, exact approval, context budgeting, per-attempt event identity, session/event persistence, bounded memory/orchestration, single-host durable task transitions, checked adapter ports, event export, policy-based repeated-trial evaluation, and bounded real MCP/A2A/OpenTelemetry SDK behavior. It still lacks process isolation, full JSON Schema, distributed durability, external protocol transports, production telemetry infrastructure, and production provider adapters.
- MCP and A2A are taught as independent interoperability contracts and now have pinned executable starting proofs. Their labs still lack full failure/transport/security scope and independent reproduction evidence.
- The bounded SQLite fixture teaches idempotency-intent checks, retry classification, lease recovery/fencing, cooperative cancellation, ambiguous-outcome repair, and state-version quarantine. LAB-C2 still requires real process loss, enforced handler timeouts, queue/worker heartbeat behavior, external-effect reconciliation, and independent reproduction; distributed workflow-engine comparison also remains.
- Evaluation fixtures now implement repeated trials, per-task thresholds, critical gates, and retained runs, but the curriculum still lacks a maintained representative corpus, validated graders, uncertainty analysis, leakage checks, cost, and latency evidence.
- LAB-C6 now has a runnable platform-independent authorization fixture and vulnerable/protected comparisons. Actual model susceptibility, network/process isolation, memory/supply-chain attack execution, external-effect reconciliation, and independent lab reproduction remain unproved. Its trusted-host model must not be represented as hostile multi-tenant security.

### Delivery Evidence

- Many labs are authored guidance rather than executed, frozen proof bundles.
- No real cohort timing or completion data exists.
- No inter-rater reliability evidence exists for assessors.
- No delayed, unaided, changed-task transfer study exists.
- Accessibility, localization, and learning-analytics evidence are incomplete.
- Presentation outlines are not a substitute for complete lecture delivery materials.

### Validation

- Historical reviews predate the expanded vision.
- Independent reviewers have not evaluated the migrated curriculum.
- Product claims have not passed legal/licensing, privacy, accessibility, or enterprise adoption review.
- No pilot institution or enterprise has supplied adoption evidence.

## Target Curriculum Architecture

Teach four layers explicitly:

1. **Stable foundations**: programming, operating systems, networking, distributed systems, databases, software engineering, security, statistics, LLM fundamentals, and human factors.
2. **Harness contracts**: agent loop, model/provider adapter, context assembly, typed tools, policy/approval, execution environments, sessions/event log, memory, orchestration, observability, evaluation, and release governance.
3. **Standards and adapters**: MCP, A2A, OpenTelemetry, durable execution engines, and selected framework adapters such as OpenAI Agents SDK, Google ADK, Microsoft Agent Framework, LangGraph, and PydanticAI.
4. **Versioned case studies**: OpenClaw, Hermes Agent, ChatGPT Work, xAI agent tooling, and future systems. Product facts must be dated and sourced.

Canonical implementation language: Python for the reference harness, with TypeScript literacy and at least one cross-language adapter exercise. Prefer standard-library-first foundations before framework convenience.

## Proposed Program Spine

### Prerequisite Bridge

- command line, Git, Python, TypeScript/JSON literacy
- testing, debugging, APIs, HTTP, authentication, databases
- processes, containers, networking, concurrency, queues
- probability/statistics, experimental design, basic ML/LLM concepts
- threat modeling, least privilege, secrets, and secure development

### Semester 1: Harness Foundations

- define agents, workflows, harnesses, and trust boundaries
- build a deterministic model-adapter test double
- implement a bounded agent loop and stop conditions
- implement schemas, typed tool registry, validation, errors, and idempotency
- build context assembly and budget management
- implement session state, event log, checkpoints, and replay
- add policy, approval, sandbox boundaries, and audit records
- add structured traces, metrics, logs, and a basic eval harness
- complete a minimal-harness practical and oral defense

### Semester 2: Production Agent Systems

- planning, routing, parallelization, manager/handoff patterns
- memory architecture and retrieval quality
- durable execution, retries, compensation, cancellation, recovery
- MCP and A2A interoperability
- prompt injection, confused deputy, supply chain, data exfiltration, and tool abuse
- reliability, SLOs, capacity, cost, latency, and incident response
- evaluation corpora, repeated trials, graders, regression gates, red teaming
- deployment, tenancy, governance, privacy, accessibility, and change control
- comparative product/framework case studies
- capstone: build, defend, attack, evaluate, operate, and port a working harness

## Source Standard

Primary anchors already researched for the migration:

- OpenAI practical agent guide and Agents SDK documentation
- Anthropic effective agents, context engineering, tool design, long-running harness, sandboxing, and agent-evaluation guidance
- Google Agent Development Kit documentation and source
- Microsoft Agent Framework documentation
- LangGraph persistence and human-in-the-loop documentation
- PydanticAI durable-execution documentation
- MCP and A2A specifications
- OpenTelemetry semantic conventions
- NIST AI RMF and Generative AI Profile
- NIST Secure Software Development Framework
- OWASP Agentic AI threats and Agent Security Cheat Sheet
- ABET 2026-2027 computing accreditation criteria
- ACM/IEEE-CS CS2023 and SWEBOK v4
- ReAct, Toolformer, Reflexion, MemGPT, AgentBench, tau-bench, OSWorld, and METR time-horizon research

Official standards, specifications, source repositories, current docs, releases, and advisories are authoritative for current behavior. Peer-reviewed research supports durable theory. Maintainer engineering posts support rationale. Blogs, issues, forums, Reddit, and product commentary are discovery signals that require verification.

## Completion Gates

The project is complete only when every applicable gate has evidence:

| Gate | Required evidence | Current state |
| --- | --- | --- |
| G0 Scope and boundary | Stable outcomes, product separation, claim limits | Implemented; internal audit complete, independent audit pending |
| G1 Source integrity | Claim-source map, versions/dates, independent spot checks | Improved but partial; current protocol and case claims rechecked internally |
| G2 Curriculum alignment | Outcome-to-module-to-lab-to-assessment traceability | Implemented; internal structural audit passed, assessor calibration pending |
| G3 Reference implementation | Runnable harness, tests, fixtures, documented failure modes | Partial; 63 bounded tests and 20 corpus contracts pass on Windows and clean WSL including optional SDK, durability, authorization, and evaluator/corpus integrity; production adapters and distributed infrastructure are absent |
| G4 Hands-on reproducibility | Labs executed in clean environments with expected evidence | Early; interoperability and durability starting fixtures are instructor-executed in fresh WSL, but LAB-C2/C4/C5/C8 and other labs lack independent reproduction |
| G5 Assessment validity | Authentic tasks, oral defense, transfer, anti-outsourcing controls | Strong authored system; empirical validity pending |
| G6 Security and governance | Threat labs, controls, privacy, change management, audits | Authored system plus an internally executed LAB-C6 authorization starting fixture; complete threat labs, operational isolation, and independent audit pending |
| G7 Teaching readiness | Instructor notes, pacing, accessibility, calibration | Partial |
| G8 Learner evidence | Pilot data and delayed changed-task transfer | Missing |
| G9 External validation | Independent academic, practitioner, security reviews repaired | Missing for new scope |
| G10 Release readiness | Clean repo, licensing, versioning, release notes, support boundary | In progress; repository/license exist, release package does not |

No completion percentage overrides a failed gate.

## Implementation Sequence

1. Execute every critical lab in clean learner environments and record reproduction status without promoting authored guidance to reproduced evidence.
2. Extend protocol/provider/telemetry examples only where they materially improve a remaining lab gate and can be maintained.
3. Run accessibility review and measured assessor calibration against the practical, oral-defense, and transfer gates.
4. Run independent adversarial academic, enterprise, security, and practitioner reviews; repair findings.
5. Pilot with real learners and assessors before institution-ready or enterprise-ready claims.

## Immediate Next Actions

1. Keep `../elite-mentor-os` frozen until the user explicitly resumes that product.
2. Reproduce the critical lab path independently and preserve environment, command, output, failure, timing, and assessor evidence.
3. Add realistic task/provider evaluation, manually reviewed grader/leakage evidence, and actual memory/persistence and process/network security boundaries. Clean validation of the 20-task deterministic contract corpus is complete; it remains a starting fixture, not a production benchmark.
4. Run accessibility and assessor-calibration audits, then repair findings.
5. Seek independent review and pilot evidence only after the internal blockers are materially reduced.

## State-Preservation Protocol

Current continuation note (2026-09-06): previous sandbox failures prevented saving the security checkpoint; command and patch access have now resumed. The security fixture adds only two files; teaching, sources, audit, and continuity updates reuse existing files. Retain the earlier uncommitted durability evidence and drift-script `writelines` repair when committing this milestone. The OpenClaw upstream review remains dated 2026-08-15: later release observations in chat are not a completed review and must be refreshed against current primary sources. The user requested an English explanation of the goal after a long pause; the platform-agnostic curriculum vision and frozen sibling-product decision remain in force. No maturity percentage is being raised from these test results.

At every meaningful milestone:

1. Read `PROJECT_STATE.md`, `.mentor/MENTOR_STATE.md`, `git status -sb`, and the latest commit.
2. Verify current sources for release-sensitive claims.
3. Change the smallest coherent scope and run matching checks.
4. Update both state files with decisions, evidence, blockers, and next action.
5. Commit and push separate product or milestone scopes only after validation.

Do not store chat transcripts, credentials, secrets, or speculative claims in state. Do not mark completion from document count. Do not ask the user to repeat decisions already recorded here.
