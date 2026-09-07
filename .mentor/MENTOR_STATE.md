# Curriculum Mentor State

## Workspace Role

This is the source repository for the platform-agnostic **Agent Harness Systems Engineering Curriculum**. OpenClaw is becoming one versioned case study, not the program spine. Elite Mentor OS is a separate sibling product in `../elite-mentor-os`.

## Active Goal

Build a university-presentable, enterprise-relevant curriculum through which a serious learner can design, implement, test, secure, operate, evaluate, and evolve agent harness systems comparable in class to OpenClaw, Hermes Agent, ChatGPT Work, xAI agent tooling, and future systems.

## Non-Negotiable Decisions

- English output by default; Roman Urdu only when explicitly requested.
- Teach first principles and stable contracts before frameworks or products.
- Require humans to trace, explain, verify, debug, and own final trust decisions.
- Treat OpenClaw, Hermes, ChatGPT Work, and xAI products as dated case studies.
- Keep the curriculum and Elite Mentor OS in separate repositories and release cycles.
- Avoid duplicate trees and file clutter; reuse or rewrite canonical files.
- State continuity is mandatory after every material milestone.
- Do not claim mastery or readiness from generated artifacts or static validation alone.

## Verified Baseline

- Checkpoint date: 2026-09-07. Use Git for current publication state; last entering pushed checkpoint was `97dbcf3`.
- Implementation `9706d44` passed 63 exact-dependency tests on Windows Python 3.13.1 and from a clean WSL archive on Python 3.13.9 (6.995 seconds). The separate corpus CLI passed 20/20 deterministic contracts with SHA256 `8b3bba3c763daa36b77091d89ef855e8c518e6116331e753d283e10b26074e32` on both systems. Ruff, MyPy (20 source/test files), and Bandit passed at that milestone. Three known upstream A2A warnings remain. The temporary WSL report `/tmp/harness-9706d44.A9dGoQ/corpus-report.json` is regenerable from that commit, not a permanent evidence location.
- Runtime fixtures cover basic contracts, context, state, memory, orchestration, optional in-process MCP/A2A/telemetry, single-host SQLite durable work, scoped authorization, and evaluator integrity. They are teaching starting points, not production infrastructure or complete labs.
- The corpus has 20 synthetic fixed tasks, six families, and 10 development/10 public challenge tasks. Its hashes, trace/state grading, leakage guards, and separate Wilson exercise do not establish representative live-model performance.
- Internal readiness verdict remains self-study draft / supervised-pilot candidate; standalone, institutional, enterprise, and world-class readiness are unproven.
- Elite Mentor OS is separate and frozen.

## Honest Progress

| Scope | Estimate | Critical remaining evidence |
| --- | ---: | --- |
| Expanded agent-harness curriculum artifacts | 78% | production adapters/security/distributed durability, lab reproduction, complete delivery evidence, independent audits |
| Hands-on reproducibility evidence | 30% | independent lab runs, learner reproduction, and calibration |
| Expanded curriculum institution/enterprise proof | 30% | cohort, measured calibration, accessibility audit, external adoption evidence |

These are planning estimates. Completion gates in `PROJECT_STATE.md` control claims.

## Current Milestone

Semester 1 lessons 1-16 now have instructional guidance, worked reasoning, practice, assessment anchors, remediation, and evidence boundaries. All 10 exact Python blocks passed on Windows Python 3.13.1; the 16 week/lesson headings are ordered without duplicates. New lessons address reusable approval scope, memory relevance versus authority, diagnostic privacy, evaluator validity, integration defense, and delayed changed-task assessment. A fake-marker variation verified raw exception disclosure in failure events and stored tool messages; another variation showed a success-looking response hiding duplicate synthetic effects, rejected by independent state inspection. These are negative teaching controls, not runtime repairs. The temporary inspection code was corrected to read messages from Harness.store rather than RunResult. No real credentials, external effects, or learner outcomes were involved. Semester 2 remains outline-level; complete lab/exam execution and learner validation remain pending for both semesters.

Access recovered after three sandbox ACL-failure turns. Corrected a temporary inspection script to close SQLite connections explicitly; cleanup then passed. Windows linked SQLite is 3.47.1, source ID b95d11e958643b969c47a8e5857f3793b9e69700b8f1469371386369a26e577e. Fresh SQLiteSessionStore and DurableTaskStore databases both observed journal mode delete. Their source does not enable WAL, so the specific WAL-reset race does not apply to these observed fresh configurations. Existing/imported databases and WSL were not inspected for this issue. Before concurrent WAL labs, verify a patched SQLite runtime and actual mode; no blanket safety claim follows. See the dated validation register for sources.

OpenClaw intermediate releases `v2026.8.1`, `v2026.8.2`, and `v2026.9.1` were triaged by grouped-entry headings with selected breaking/security/state summaries read in detail. Pinned docs confirm the `agent` default in 8.2 versus `all` in 9.2. The source ledger maps memory/learning defaults, rollback cleanup, principal-scoped skills/approvals, and migration failures into stable teaching requirements. LAB-C3 now has a lineage/deletion/stale-index-worker exercise; release discipline has an irreversible-cleanup gate. These exercises are authored, not product executions.

Latest observed remains `v2026.9.2`; fully reviewed baseline remains `v2026.7.1-2`. Discovery is complete for the intervening releases, but detailed high-risk implementation/installed-product regressions and optional dependency reachability remain pending. Do not repeat broad release scraping or unchanged advisory polling as a substitute for those checks.

The prior status-only reply made no implementation progress; this continuation completed and verified the pending lessons 11-16. Targeted OWASP authorization and OpenTelemetry sensitive-data sources were checked and linked in the guide and validation register. No new files or runtime changes were needed. No live process is pending. Older session-log Next cells are historical.

## Next Actions

1. Expand Semester 2's existing teaching guide, starting with production requirements, orchestration comparison, durable execution, and memory. Inspect the relevant lab guides and reference code first; build worked examples, failure/control pairs, assessment anchors, and remediation rather than another outline. All Semester 1 printed examples are executed, not independently learner-validated; its complete labs and seeded exams remain open.
2. Deepen actual executor isolation/timeouts, persistence/crash recovery, and external protocol/provider evaluation. Preserve the difference between a bounded fixture and a complete independently reproduced lab.
3. For OpenClaw, conduct focused implementation/regression checks for session visibility, approval lifetime, migration conflicts, and optional memory-plugin dependency reachability. No installed user environment changes; use source analysis or disposable evidence lanes. Keep reviewed versus observed version fields distinct.
4. Obtain accessibility evidence, measured assessor calibration, and independent learner lab reproduction; prepare qualified reviews/pilots after internal blockers are reduced. No claim of institutional effectiveness before real evidence.
5. Keep Mentor OS frozen and separately versioned. Save material decisions and evidence here and in PROJECT_STATE; do not raise percentages from test counts.

## Required Curriculum Layers

1. Foundations: CS, software engineering, security, statistics, LLMs, human factors.
2. Harness contracts: loop, providers, context, tools, policy, execution, state, memory, orchestration, observability, evaluation, governance.
3. Standards/adapters: MCP, A2A, OpenTelemetry, durable execution, selected frameworks.
4. Product case studies: OpenClaw, Hermes Agent, ChatGPT Work, xAI agent tooling, future systems.

## Evidence Rules

- Mastery requires delayed, unaided, changed-task transfer.
- Current claims require dated primary sources.
- Labs require executable or inspectable evidence and explicit failure modes.
- Assessments must test reasoning, tracing, debugging, tradeoffs, and oral defense.
- Security tests must include prompt injection, confused deputy, privilege, exfiltration, supply chain, persistence, and recovery.
- Final maturity requires independent review and real learner/assessor evidence.

## Session Log

| Date | Decision/evidence | Next |
| --- | --- | --- |
| 2026-09-06 | Added optional host-scoped tool/resource/destination policy and expiring/revocable single-use approvals, 14 adversarial test methods, and LAB-C6 teaching/assessment instructions. All 48 tests passed in the existing exact-dependency Windows environment; source/static checks passed. Sandbox command failures were temporarily handled with the available Node runtime for repository-local reads/tests; normal command/patch access has now resumed. State is saved here after the earlier failed checkpoint attempt. | Commit and cleanly validate in WSL; preserve pending durability evidence and drift-script repair. Then address LAB-C7 and current source drift. |
| 2026-08-15 | Pushed clean OpenClaw baseline `94aa38d` and plugin snapshot `50f6439`; researched primary architecture, protocol, security, accreditation, and evaluation sources. | Finish standalone Mentor OS extraction. |
| 2026-08-15 | Expanded target from OpenClaw mastery to platform-agnostic Agent Harness Systems Engineering; measured 55/81 curriculum files as OpenClaw-referenced. | Migrate canonical outcomes and semester spine after product separation. |
| 2026-08-15 | Published standalone Mentor OS v0.3 at `HaseebAhmed-official/elite-mentor-os`; static validators and isolated Codex/Claude remote installs passed. User then paused all Mentor OS work. | Focus only on curriculum until explicitly resumed. |
| 2026-08-15 | Migrated canonical curriculum, semesters, teaching guides, labs, assessments, tracks, sources, governance, and case method; removed embedded plugin and redundant screenshot manuals; added tested minimal Python reference harness. | Consolidate remaining support assets and extend advanced executable evidence. |
| 2026-08-15 | Consolidated model answers; migrated examples, templates, decks, environment lanes, maintenance, calibration, and validation prompt; added explicit PLO alignment plus context-budget and SQLite reset-recovery tests. | Extend advanced contracts and run internal adversarial validation. |
| 2026-08-15 | Added per-attempt event identity, bounded memory/orchestration, checked protocol/telemetry ports, policy-based evaluation gates, schema migration coverage, and adversarial tests. Mentor OS remains frozen. | Complete internal curriculum audit and repair findings. |
| 2026-08-15 | Fixed candidate `eb8d423`: 20 harness tests and 4 drift tests pass; current MCP/A2A/OpenTelemetry sources and non-OpenClaw case ledgers were repaired; internal audit conditionally accepts self-study/supervised-pilot use and rejects stronger readiness claims. | Reproduce the critical lab path cleanly; then add justified real adapters and run accessibility/calibration review. |
| 2026-08-16 | Added exact optional MCP `2.0.0`, A2A SDK `1.1.2`, and OpenTelemetry SDK `1.44.0` proofs at `25d06ae`. All 24 tests passed on Windows and from that commit's Git archive in fresh offline WSL using Python 3.14.2; the WSL test run took 3.182 seconds. Only the shared fixture is `executed`; advanced labs remain `authored`, and Mentor OS remains frozen. | Implement the highest-value remaining production fixture and pursue independent lab reproduction without promoting unearned readiness claims. |
| 2026-08-16 | Added bounded SQLite durable work at `a78f42a` and hardened exact-SDK telemetry typing at `ac25d63`: idempotency-intent checks, bounded retries, atomic claims, lease fencing/recovery, cancellation, ambiguous-outcome repair, and state-version quarantine. All 34 exact-dependency tests passed on Windows and from a clean `ac25d63` Git archive in fresh WSL; the WSL test runner took 3.150 seconds. LAB-C2 remains `authored`, and Mentor OS remains frozen. | Build the highest-value platform-independent security or evaluation fixture and pursue independent lab reproduction without promoting unearned readiness claims. |

## Resume Protocol

Read `PROJECT_STATE.md`, this file, Git status/log, and current source baseline. Continue from `Next Actions`; do not reconstruct the plan from old README percentages or chat history.
