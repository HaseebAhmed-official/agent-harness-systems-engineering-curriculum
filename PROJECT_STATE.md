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

Implementation `9706d44` passed 63 exact-dependency tests on Windows Python 3.13.1 and from a clean WSL archive on Python 3.13.9 (6.995 seconds). The separate corpus CLI passed 20/20 deterministic contracts with SHA256 `8b3bba3c763daa36b77091d89ef855e8c518e6116331e753d283e10b26074e32` on both systems. Ruff, MyPy (20 source/test files), and Bandit passed at that milestone. Three known upstream A2A warnings remain. The temporary WSL report `/tmp/harness-9706d44.A9dGoQ/corpus-report.json` is regenerable from that commit, not a permanent evidence location.

The implementation includes optional host-scoped authorization and single-use approval controls (`b2a0221`), unconditional evaluator infrastructure-failure veto (`1423d88`), and the maintained synthetic corpus (`9706d44`). LAB-C6/C7 contain executable starting exercises and explicit remaining evidence contracts. Earlier evidence remains in Git and the lab ledger; completed clean WSL runs must not be restarted as unfinished work.

2026-09-08 teaching milestone: Semester 1 lessons 1-16 and Semester 2 lessons 1-8 have expanded guidance. Four opening Semester 2 examples passed on Windows/WSL at `87a701a`. The three new MCP/A2A/scoped-policy examples passed on Windows Python 3.13.1; all 14 existing security tests passed in 0.022 seconds. A2A emitted a queue-cleanup warning despite successful assertions; investigate its lifecycle before claiming graceful shutdown. The protocol examples are in-process, not external transport or production-auth evidence. Weeks 9-16 still need expansion, and full lab/exam execution, accessibility, assessor reliability, independent reproduction, and learner outcomes remain incomplete.

2026-09-07 product-source milestone: targeted OpenClaw `v2026.9.2` release/docs review integrates broader session access, privacy regression cases, recovery/approval migration tests, and an upcoming plugin alias retirement. npm tags and all 647 advisory metadata records were checked. No advisory update postdates the saved August 13 cutoff. Intermediate release headings and selected high-risk summaries have now been triaged, with pinned session-default documentation checked for 8.2 and 9.2. Detailed implementation and installed-product regressions remain pending, so `upstream-state.json` separates observations from the unchanged fully reviewed `v2026.7.1-2` baseline. LAB-C3 now includes a deletion-lineage/stale-publication exercise and release discipline includes an irreversible-cleanup gate.

The [internal migration audit](Validations/internal-migration-audit-2026-08-15.md) conditionally accepts a strong self-study draft and supervised-pilot candidate, but rejects standalone ready-to-teach, institution-ready, enterprise-ready, and world-class claims at the current evidence level.

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
- The bounded SQLite fixture teaches idempotency-intent checks, retry classification, lease recovery/fencing, cooperative cancellation, ambiguous-outcome repair, and state-version quarantine. Semester 2 lesson 3 now executes one actual process-exit boundary with a synthetic local file effect and controlled lease clock on Windows/WSL. LAB-C2 still requires a broader crash matrix, enforced handler timeouts, queue/worker heartbeat behavior, transactional external-service reconciliation, and independent reproduction; distributed workflow-engine comparison also remains. Single-task receipt inspection does not prove concurrent idempotency or power-loss safety.
- Evaluation now includes a maintained deterministic corpus, trace/state graders, duplicate/split guards, measured local execution time, and a separate tested Wilson exercise. Representative workloads, independent grader calibration, semantic leakage review, live-provider cost/latency, and justified sampling remain missing.
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
2. Follow the compact checkpoint's next-action ordering: expand Semester 2's teaching guide, then continue focused product implementation/regression review and technical evidence work; the full goal and evidence gates remain unchanged.
3. Reproduce the critical lab path independently and preserve environment, command, output, failure, timing, and assessor evidence.
4. Add realistic task/provider evaluation, manually reviewed grader/leakage evidence, and actual memory/persistence and process/network security boundaries. Clean validation of the 20-task deterministic contract corpus is complete; it remains a starting fixture, not a production benchmark.
5. Run accessibility and assessor-calibration audits, then repair findings.
6. Seek independent review and pilot evidence only after the internal blockers are materially reduced.

## State-Preservation Protocol

Current continuation note (2026-09-08): pending lessons 5-8 were verified after permission changes interrupted work. Approved escalated execution worked around the sandbox helper startup failure; no validation process remains. Investigate A2A queue cleanup next, then develop Semester 2 lessons 9-16. Protocol/security primary sources were checked on September 8. The latest examples passed on Windows only this pass, not clean WSL or independent reproduction. Preserve the SQLite WAL preflight and product reviewed-versus-observed distinctions. Do not restart broad release discovery or repeat completed corpus work. Mentor OS stays frozen; maturity estimates are unchanged.
