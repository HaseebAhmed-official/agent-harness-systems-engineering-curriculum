# Internal Migration Audit - 2026-08-15

## Decision Record

- Candidate audited: commit `eb8d423`
- Scope: platform-agnostic Agent Harness Systems Engineering curriculum, reference harness, source controls, and OpenClaw maintenance automation
- Excluded product: Elite Mentor OS, which is separately versioned and frozen by user decision
- Reviewer: repository-authoring Codex session; this is internal evidence, not independent validation
- Review date: 2026-08-15, Asia/Karachi

## Verdict

| Claim level | Verdict | Reason |
| --- | --- | --- |
| Strong self-study draft | `conditional` | The program spine, labs, assessments, sources, and bounded executable fixtures are coherent; advanced labs still need clean reproduction and some require external systems. |
| Supervised pilot | `conditional` | Run critical labs in clean learner environments first, freeze expected evidence, and brief assessors on current fixture limits. |
| Standalone ready-to-teach program | `reject` | Complete lecture delivery, accessibility review, timing evidence, and independently reproduced labs do not yet exist. |
| Institution-ready curriculum | `reject` | There is no real cohort, assessor-reliability result, delayed transfer study, independent academic review, or adoption evidence. |
| Enterprise-ready program | `reject` | There is no organizational security/privacy/legal review, production workload evidence, support model, or enterprise pilot. |
| World-class or optimum claim | `reject` | Internal artifacts and tests cannot establish comparative excellence or learning effectiveness. |

## Executed Checks

| Check | Observed result | Boundary |
| --- | --- | --- |
| Reference harness | 20 of 20 `unittest` cases passed | Standard-library teaching fixtures only; not a production runtime. |
| OpenClaw drift script | 4 of 4 `unittest` cases passed | Tests request construction and issue-body behavior, not GitHub Actions execution. |
| Python compilation | 15 files compiled from source | Syntax/import-independent compilation is not type, lint, or security analysis. |
| JSON parsing | 1 repository JSON file parsed | Schema semantics were reviewed manually; no separate JSON Schema exists. |
| Curriculum structure | 25 unique labs each have one guide; 90 sequential questions; 54 sequential oral prompts; both semesters contain weeks 1-16 | Structural completeness is not pedagogical validity. |
| Outcome traceability | PLO-1 through PLO-10 each map to direct evidence, teaching locations, required labs, and high-stakes assessment | Mapping is internally coherent but has not been empirically validated with learners or assessors. |
| Local Markdown links | Targets validated across 75 Markdown files | Anchor fragments and external semantics were not certified by this check. |
| Duplicate-content check | No exact duplicate curriculum files | Near-duplicate prose still requires editorial judgment. |
| Source crawl | 128 unique HTTPS URLs checked | Ten legitimate sources rejected or timed out in the generic crawler but were independently resolved through current browser/search or Crossref; two deliberate invalid fixtures and two code-span parser artifacts were excluded. |
| Secret checks | No high-confidence secret signature or likely hard-coded credential assignment found | This is a pattern scan, not full history or specialized secret scanning. |
| Git whitespace | `git diff --check` passed before candidate commit | Does not replace formatters or linters. |
| Optional analyzers | `ruff`, `mypy`, `bandit`, `gitleaks`, and `actionlint` unavailable | No result is claimed for these tools. |

## Current Source Findings

- MCP teaching now targets the `2026-07-28` stateless, per-request negotiation model instead of initialization-era assumptions.
- A2A teaching is pinned to released specification `1.0.0`.
- OpenTelemetry GenAI teaching points to the dedicated semantic-conventions repository and remains a protocol/telemetry lab requirement rather than a reference-harness claim.
- Hermes Agent evidence is pinned to `v2026.8.13`; ChatGPT Work and xAI claims are dated public-contract claims with private internals marked `unknown`.
- OpenClaw stable remains `v2026.7.1-2`, npm extended-stable remains `2026.6.34`, and beta was observed at `2026.8.1-beta.2`. Stable release drift was false at review time.
- OpenClaw advisory metadata showed 647 published records, latest publication `2026-06-30T01:11:32Z`, and latest update `2026-08-13T17:27:46Z`. The earlier review covered the 112 advisories published after the prior cutoff; this audit did not reread all 647 records.

## Findings Repaired In Candidate

1. Replaced stale MCP/A2A/OpenTelemetry assumptions with current pinned source boundaries.
2. Added dated claim ledgers for Hermes Agent, ChatGPT Work, and xAI agent tooling without inferring managed internals.
3. Added bounded memory, orchestration, integration/export, per-attempt persistence, and policy-based evaluation fixtures.
4. Rejected reused provider call identities, invalid memory-policy outputs, invalid worker outputs, malformed adapter shapes, and contaminated export event streams.
5. Clarified advisory publication versus update timestamps and recorded stable, extended-stable, and beta channels separately.
6. Pinned the GitHub checkout action and prevented drift-check authentication tokens from entering request URLs.

## Residual Blockers

- A bounded pinned MCP `2.0.0` in-process proof and A2A SDK `1.1.2` JSON-RPC/ASGI proof are now instructor-executed, but neither proves external network transport, TLS/OAuth, disconnect/timeout/retry, cancellation, side-effect approval, streaming, duplicate handling, or cross-implementation compatibility.
- A bounded OpenTelemetry SDK `1.44.0` in-memory span proof is instructor-executed against a commit-pinned development GenAI schema, but no OTLP backend, metrics/logs, SLO/alert path, production redaction audit, network model provider, or real provider compatibility fixture is reproduced.
- A bounded single-host SQLite durability fixture is now instructor-executed. It covers persisted state transitions, idempotency conflicts, bounded retries, lease recovery and fencing, cooperative cancellation, ambiguous-outcome quarantine, and manual resolution; it does not prove real process killing, enforced handler deadlines, queue/worker heartbeats, distributed state, external-service reconciliation, or exactly-once effects. Process isolation, egress control, production redaction, hostile concurrency, and hostile multi-tenant fixtures remain absent.
- Authored labs have not been independently run in clean WSL/Linux, container, VPS, and constrained-budget lanes with retained evidence.
- No representative maintained evaluation corpus, validated graders, uncertainty analysis, leakage study, or cost/latency baseline exists.
- No accessibility audit, learner timing study, measured assessor calibration, delayed unaided changed-task transfer result, or cohort pilot exists.
- No independent academic, practitioner, security, privacy/legal, or enterprise-governance review has evaluated the migrated scope.
- Ruff, MyPy with untyped-body checking, and Bandit now pass for the reference harness. Specialized secret-history and workflow-linter evidence remains absent.

## Maturity Snapshot

At the 2026-08-15 audit, planning estimates were approximately **74% artifact implementation**, **25% hands-on reproducibility evidence**, and **30% institution/enterprise proof**. They are historical prioritization aids only; the addendum below supersedes them. The completion-gate ledger in `PROJECT_STATE.md` overrides every percentage.

## Next Gate

### 2026-09-06 Authorization Fixture Addendum

This remains author-session evidence. `security.py` adds opt-in host-scoped resources and destinations with exact expiring/revocable single-use approval; the minimal foundations `Policy` retains its original reusable-grant behavior. Fourteen security methods exercise forced malicious provider calls and a deliberately vulnerable synthetic positive control, benign success, cross-resource/session denial, destination variants, changed arguments, replay, expiry/revocation, concurrent grant consumption, tool-binding drift, and denial after partial-effect failure or policy recreation. No real network request is made.

The current Windows Python 3.13.1 exact-dependency environment passed all 48 tests in 4.521 seconds. Ruff, MyPy with `--check-untyped-defs` over 19 source/test files, Bandit on `src`, four drift-script tests, and `git diff --check` passed. Three existing upstream A2A protobuf deprecation warnings remain. A type error in the deliberate schema-mutation test was repaired with an explicit type narrowing. This is worktree execution; fresh archive/WSL evidence will be recorded separately.

LAB-C6's existing guide now includes runnable commands, trust assumptions, exploit/control/end-state predictions, benign controls, detection/recovery evidence, required unseen variants, and oral-defense criteria. The fixture has trusted host identities/handlers and no real model, network/OS enforcement, persistent approvals, malicious-handler containment, or independent audit. Its single-grant lock is not full runtime concurrency safety. LAB-C6 remains `authored`, and the readiness verdicts above remain unchanged. Only two new files were needed; all teaching/state/source changes reuse canonical files.

### Continuing Gate

2026-09-07 clean corpus follow-up: fresh Git archive `9706d44` passed all 63 tests in 6.995 seconds and its separate CLI passed all 20 contracts in WSL Python 3.13.9 with offline exact locked dependencies. Corpus hash matched Windows. The directory was `/tmp/harness-9706d44.A9dGoQ`; the full synthetic report was read back from `corpus-report.json`. Three known A2A warnings remained. This upgrades the new starting fixture from worktree-only to clean archive execution, not independent reproduction or a representative model benchmark.

2026-09-07 corpus addendum: `evaluation-corpus.json` and `corpus.py` supply 20 versioned original synthetic contracts, six families, public development/challenge splits, strict schema and duplicate/split checks, fixture-state/trace predicates, per-task timing, corpus hash, and full failed rows. Mutation tests demonstrate detection of unauthorized writes, plausible final text with wrong state, changed private inventory, and mismatched event identity. Duplicate call-ID renaming/default settings and misspelled zero-count event assertions are rejected. Wilson interval tests verify known values, extremes, and invalid input; the deterministic corpus report deliberately has no confidence interval or model cost estimate. Windows Python 3.13.1 passed 63 tests in 9.081 seconds; the CLI passed 20/20. Ruff, MyPy (20 files), Bandit on source, and whitespace checks passed. This is internally executed contract evidence; general workload representativeness, adversarial in-process candidate containment, semantic contamination detection, independent grader calibration, and teaching validity remain unproved. No maturity verdict is raised.

Final commit-bound evaluator evidence, 2026-09-06: a fresh archive of `1423d88` passed all 50 tests in 12.421 seconds in WSL Python 3.13.9 using the committed lock and offline cached dependencies. Directory: `/tmp/harness-1423d88.7iofeT`. Command: `uv run --offline --python 3.13 --extra interop --locked python -m unittest discover -s tests -v`. Three known A2A protobuf warnings remained. The LAB-C7 starting fixture is internally `executed`; the complete lab remains `authored`. This does not supply independent reviewer or learner evidence.

2026-09-06 follow-up: security implementation `b2a0221` passed all 48 tests from a clean Git archive in fresh WSL at `/tmp/harness-b2a0221.tyzzwz`, Python 3.13.9, Linux 6.18.33.2 x86-64, using `uv run --python 3.13 --extra interop --locked python -m unittest discover -s tests -v`. Test time was 6.949 seconds excluding environment setup. Three known upstream A2A warnings remained. This is instructor execution, not independent reproduction.

A separate evaluator defect was reproduced: with zero pass-rate thresholds, a factory exception could approve a release. The repair records infrastructure failures explicitly and vetoes approval regardless of scoring thresholds. Ordinary negative grades remain task outcomes; available runs survive grader failure. Five evaluator methods now include factory exceptions, grader exceptions, malformed grade, critical-task veto, and valid negative-grade behavior. All 50 worktree tests passed in the Windows exact-dependency environment in 2.952 seconds; Ruff, MyPy with untyped-body checking, Bandit on source, and Git whitespace checks passed. LAB-C7's new exercise explains the measurement boundary and requires a maintained corpus and calibrated graders before stronger evaluation claims. No readiness percentage or verdict is raised by this repair.

Reproduce the critical lab path in a clean learner environment and retain commands, inputs, outputs, failures, environment fingerprints, timing, and assessor decisions. Do not promote readiness claims until that evidence is reviewed and the residual blockers are materially reduced.

## 2026-08-16 Interoperability Addendum

This addendum is still author-session evidence, not independent review. The reference harness gained one optional exact-version lane: MCP Python SDK `2.0.0`, A2A Python SDK `1.1.2`, and OpenTelemetry SDK `1.44.0`. The default standard-library lane remains dependency-free.

The full 24-test suite passed on Windows Python 3.11.9 and from a Git archive of implementation commit `25d06ae` extracted into a fresh WSL `/tmp` directory. The commit-bound run used CPython 3.14.2, Linux 6.18.33.2 x86-64, glibc 2.35, and an offline Linux wheelhouse; tests took 3.182 seconds. It observed MCP `2026-07-28` discovery and schema rejection, an authenticated A2A JSON-RPC task/artifact exchange plus `401` denial, and linked in-memory agent/tool spans that omitted supplied sensitive values. A2A emitted three upstream protobuf `label()` deprecation warnings.

The fixture is `executed`; LAB-C4, LAB-C5, and LAB-C8 remain `authored`. No second person reproduced the work. Updated planning estimates are approximately **76% artifact implementation**, **28% hands-on reproducibility evidence**, and **30% institution/enterprise proof**. The strong readiness verdicts remain rejected.

## 2026-09-08 Protocol and Security Teaching Checkpoint

Semester 2 lessons 5-8 gained worked protocol traces, three executable examples, threat modeling, scoped-approval controls, remediation, and changed-task assessment. The exact Markdown MCP/A2A/scoped-policy examples passed on Windows Python 3.13.1; the 14 existing security tests passed in 0.022 seconds. Sixteen ordered week headings and eight ordered lesson headings were verified. A2A additionally emitted a dispatch-loop cancellation-without-EventQueue.close warning. Cleanup remains unverified; the successful assertions do not establish warning-free lifecycle behavior. No runtime source changed, full runtime suite or WSL lane was rerun, or independent reviewer/learner participated. The bounded samples do not complete LAB-C4/C5/C6.

Permission transitions interrupted the authored work. The sandbox helper failed before command/file-edit startup; approved escalated shell execution and the apply_patch utility were used to complete validation and continuity. A temporary command typo in the virtualenv path was corrected. No status or percentage is promoted. Next investigate the A2A lifecycle warning, then expand lessons 9-16; retain all external teaching/adoption gates.

## 2026-09-07 Teaching and Drift Addendum

Semester 2 structural checks: 16 ordered week headings, four ordered expanded lesson headings, all 10 local Markdown links/anchors across the eight changed files, and Git whitespace validation passed. No new files were added. This checks navigation and sample execution, not completeness of the remaining instruction.

Semester 2 follow-up: lessons 1-4 now have worked explanations, prediction keys, failure/control pairs, independent lab tasks, remediation, and changed-condition assessment. All four exact Markdown Python blocks passed in the current worktree on Windows Python 3.13.1 and WSL Ubuntu Python 3.13.9. The process exercise starts a real child that exits with code 23 after committing a lease and writing one local synthetic receipt; reopening and retrying yields two effects without reconciliation and one with the limited single-task receipt check. Both tasks report local success. This improves process-exit teaching evidence, not transactional external-service guarantees. The deletion generation-check example is a sequential schedule only. No runtime source changed, full runtime suite was not rerun, no independent person reproduced it, and LAB-C1/C2/C3 remain authored. Primary SRE, Anthropic, and AWS sources are linked with bounded claims in the source register. Ubuntu's default Python 3.10 was not used or changed; its already-cached Python 3.13.9 meets the project requirement. Remaining weeks, complete lab evidence, assessment/accessibility calibration, and external learner/adoption gates stay open.

Latest teaching follow-up: lessons 1-16 are expanded; all 10 exact Python examples passed on Windows Python 3.13.1. The guide has 16 ordered week headings and matching lesson headings after duplicate-heading repair. Lessons 11-16 cover reusable approval scope, memory trust/expiry/deletion, diagnostic privacy, evaluator failure/empty-evidence veto, integration review, and changed-task assessment. A fake-marker variation observed raw exception text in both failure event data and stored tool messages. A second variation demonstrated a text-only success predicate accepting duplicate synthetic effects while state inspection accepted the single-effect control and rejected the duplicate. The inspection helper initially used nonexistent RunResult.messages; reading Harness.store.messages corrected it and the checks passed. No runtime code changed or independent learner evidence was generated. Strong readiness verdicts remain rejected.

These checks use the current teaching fixture and disposable in-memory state; the full 63-test runtime suite and clean-WSL corpus were not rerun for this documentation-only change. All three local Markdown links/anchors across the five changed files and Git whitespace checks passed. The dated source register records targeted primary OWASP authorization and OpenTelemetry sensitive-data guidance. Full lab execution, unseen exam seeding, calibrated scoring, accessibility usability, and learner transfer remain unproved; Semester 2 still needs comparable instruction. No new files or maturity-percentage increase were needed.

Earlier lessons 7-10 follow-up: Lesson 8 supplies a formative fault matrix and assessment procedure, not an executed unseen exam. Context, attempt correlation, and SQLite reopen examples have explicit capability limits. The source-register entry records SQLite 3.47.1 with fresh stores in delete mode; concurrent-WAL risk is not applicable to those observed modes, while other environments remain unchecked. A temporary inspection connection-cleanup error was corrected with explicit closing and rerun successfully.

This remains author-session review. Semester 1 lessons 1-4 gained worked instruction, public keys, prediction tasks, guided/independent practice, remediation, and evidence limits. Both exact Markdown Python blocks ran on the existing Windows Python 3.13.1 environment: `final 5 [5]` and `no_progress cancelled provider_error`. Final-response checking is distinct from independently observed handler state. LAB-C6 prerequisite labels now correctly refer to B3 typed tools, B6 policy, and B5 sessions/events.

The current implemented baseline is `9706d44`: 63 bounded tests and 20 synthetic corpus contracts passed on Windows and clean WSL, as recorded in the project checkpoint. This supersedes historical lower test totals, not the incomplete-readiness verdict.

A targeted OpenClaw September review found material session-access and migration teaching impact. The validation register and maintenance review log record primary sources, the unchanged advisory metadata cutoff, and the unresolved intermediate-release/product-test scope. Latest observed is not fully reviewed. Expanded instruction and passing examples do not prove student learning, full delivery readiness, accessibility, assessor consistency, or enterprise safety. G7 and external-adoption gates remain incomplete.

Follow-up on 2026-09-07: lessons 5-6 now expose the teaching validator's unsupported `minimum` constraint and demonstrate partial effects before a tool exception. All four exact guide examples passed; approved replay produced the expected duplicate synthetic effect, and wrong-session approval prevented dispatch. These observations do not repair schema completeness, add a production executor, or prove classroom effectiveness. Intermediate OpenClaw releases were triaged and selected claims were checked against version-pinned documentation; detailed implementation/regression review remains open. LAB-C3 deletion and migration-cleanup extensions are authored, not executed product proof.

## 2026-08-16 Durable Execution Addendum

This addendum is also author-session evidence, not independent review. Implementation commit `a78f42a` added a standard-library SQLite durable-work starting fixture with an explicit state/version contract, atomic claims, per-claim lease-token fencing, bounded retry policy, idempotency-intent checks, cancellation, expired-lease recovery, quarantine, compensation/manual resolution, and an append-only application transition ledger.

The exact-dependency 34-test suite passed on Windows. A Git archive of implementation head `ac25d63` then passed all 34 tests after fresh extraction under WSL using CPython 3.14.2, Linux 6.18.33.2 x86-64, glibc 2.35, and the offline exact-version wheelhouse; the test runner reported 3.150 seconds and the measured command elapsed time was 3.843 seconds. Ruff, exact-environment MyPy with `--check-untyped-defs`, Bandit, `uv lock --check`, compilation, drift tests, local-link checks, and Git whitespace checks also passed. The three A2A protobuf `label()` deprecation warnings remain upstream warnings in the optional integration lane.

The durability fixture is `executed`; LAB-C2 remains `authored`. There was no independent learner, real process kill, enforced call timeout, distributed worker system, or external side-effect service. Updated planning estimates are approximately **78% artifact implementation**, **30% hands-on reproducibility evidence**, and **30% institution/enterprise proof**. The strong readiness verdicts remain rejected.
