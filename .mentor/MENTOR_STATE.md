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

- Date: 2026-09-07, Asia/Karachi; clean WSL implementation baseline is commit `9706d44` (security, evaluator repair, and 20-task contract corpus).
- Platform-agnostic curriculum migration, advanced interoperability hardening, and bounded durable execution are fixed through implementation head `ac25d63`.
- Current tree has 68 curriculum files; 15 OpenClaw references remain in intentional case/source/maintenance/comparative contexts.
- The reference harness has a minimal runtime, bounded memory/orchestration/persistence/evaluation fixtures, a single-host SQLite durable-work fixture, and an optional exact-version MCP/A2A/OpenTelemetry lane; 34 tests pass on Windows and from a clean WSL extraction of Git archive `ac25d63`.
- The current worktree adds opt-in `ScopedPolicy` and 14 security tests; all 48 exact-dependency tests passed on Windows Python 3.13.1 in 4.521 seconds. Ruff, MyPy with untyped-body checking (19 files), Bandit on source, four drift tests, and Git whitespace checks passed. No independent reproduction or complete LAB-C6 claim follows.
- The 2026-08-15 internal migration audit rejects standalone, institution, enterprise, and world-class readiness claims pending real evidence.
- Elite Mentor OS is separate and frozen; do not work on it until the user explicitly resumes it.

## Honest Progress

| Scope | Estimate | Critical remaining evidence |
| --- | ---: | --- |
| Expanded agent-harness curriculum artifacts | 78% | production adapters/security/distributed durability, lab reproduction, complete delivery evidence, independent audits |
| Hands-on reproducibility evidence | 30% | independent lab runs, learner reproduction, and calibration |
| Expanded curriculum institution/enterprise proof | 30% | cohort, measured calibration, accessibility audit, external adoption evidence |

These are planning estimates. Completion gates in `PROJECT_STATE.md` control claims.

## Current Milestone

Completed clean corpus validation: archive `9706d44`, WSL `/tmp/harness-9706d44.A9dGoQ`, Python 3.13.9, offline locked exact dependencies. All 63 tests passed in 6.995 seconds; the CLI separately passed 20/20, matching Windows corpus hash `8b3bba3c763daa36b77091d89ef855e8c518e6116331e753d283e10b26074e32`. Full synthetic CLI evidence is `/tmp/harness-9706d44.A9dGoQ/corpus-report.json` (temporary, may not persist); rerun from the commit to regenerate it. Three known A2A warnings remain. This supersedes pending-validation language in the checkpoint below. Next: realistic provider/task evaluation with grader calibration and manual semantic-leakage review, then stale product-source refresh and remaining delivery/learner gates. Do not repeat the completed WSL runs. Verify Git for publication status.

2026-09-07 corpus checkpoint: `evaluation-corpus.json` adds 20 original synthetic contracts in six families (10 development, 10 public challenge). `corpus.py` validates schema/duplicate JSON keys, normalized prompts, equivalent scripts including call-ID/default normalization, and declared family split overlap; grades final inventory/read/effect journals plus trace; reports hashes, timings, failures, and explicit uncertainty/cost limits. It is a deterministic contract corpus, not a representative model/workload benchmark. Thirteen additional test methods check positive/negative controls, misleading output, private-state and trace changes, infrastructure failure, metadata/leakage errors, and Wilson interval boundaries. All 63 exact-dependency tests passed on Windows Python 3.13.1 in 9.081 seconds; the corpus CLI passed 20/20 with hash `8b3bba3c763daa36b77091d89ef855e8c518e6116331e753d283e10b26074e32`. Ruff, MyPy (20 source/test files), Bandit on source, and whitespace checks passed. Clean commit-bound WSL validation of this new milestone is still pending. LAB-C7 instructions and source rationale reuse existing files. Only the corpus JSON and its runner are new files.

User alignment clarification: explain progress in plain English. Historical 78% artifact / 30% reproduction / 30% institutional-evidence estimates remain planning aids, not measurements; do not turn new test counts into higher percentages. Practical relevance must be evidenced through building, diagnosing, securing, recovering, evaluating, and transferring systems. Decade-long usefulness is an aim supported by stable fundamentals and source refresh, not a guarantee. Next after clean validation: realistic task/provider evaluation and manual semantic-leakage/grader review, current product-source refresh, then remaining delivery/accessibility and independent learner gates. Mentor OS remains frozen.

LAB-C6 security milestone `b2a0221` passed all 48 exact-dependency tests from a clean Git archive in WSL in 6.949 seconds on Python 3.13.9, Linux 6.18.33.2 x86-64. Archive directory: `/tmp/harness-b2a0221.tyzzwz`. Command: `uv run --python 3.13 --extra interop --locked python -m unittest discover -s tests -v`. Three known A2A protobuf warnings remain. This author-executed fixture evidence does not complete LAB-C6 or count as independent reproduction.

LAB-C7 evaluator repair `1423d88`: a factory exception previously yielded `approved=True` when both pass-rate thresholds were zero. `testing.py` now adds an explicit infrastructure-error flag and unconditional release veto. Five evaluation test methods cover ordinary versus critical failures, factory/grader exceptions, malformed grades, and retained evidence. All 50 exact-dependency tests passed on Windows Python 3.13.1 in 2.952 seconds; Ruff, MyPy (19 source/test files), Bandit on source, and Git whitespace checks passed. A fresh Git archive of `1423d88` then passed all 50 tests in WSL Python 3.13.9 in 12.421 seconds at `/tmp/harness-1423d88.7iofeT`, using `uv run --offline --python 3.13 --extra interop --locked python -m unittest discover -s tests -v`. Setup used the cached exact dependencies; three known A2A warnings remained. Both WSL jobs are complete; do not resume or restart them as pending work. The lab guide includes the evaluator-failure exercise and corpus/evidence contract. Next: build LAB-C7's maintained corpus and uncertainty/leakage checks, then refresh stale product sources. Verify Git for publication status; no external-readiness claim follows from author-run tests.

## Next Actions

1. Do not work on `../elite-mentor-os` until the user explicitly resumes it.
2. Keep interoperability, durability, and authorization starting fixtures distinct from lab completion; do not promote LAB-C2/C4/C5/C6/C8 without their full evidence contracts and independent reproduction.
3. Add a maintained evaluation corpus with meaningful grader/uncertainty/leakage checks for LAB-C7; pursue actual memory/persistence and process/network security evidence next. OpenClaw upstream review is stale at 2026-08-15 and still needs a current source refresh.
4. Run accessibility and measured assessor-calibration audits.
5. Request independent reviews and pilots only after internal blockers are materially reduced.

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
