# Upstream Review Log

## 2026-04-24

- Reviewed upstream baseline through OpenClaw release `v2026.4.23`
- Reviewed selected official OpenClaw advisories published on `2026-04-23` that map directly to current curriculum security surfaces
- Change category: advisory-aware security and maintenance clarification with no release drift
- Confirmed the curriculum repo baseline after adding delivery assets, templates, grading assets, and maintenance automation
- Added advisory-aware reading, security, and maintenance references to the curriculum
- Confirmed no additional release-driven curriculum changes were required beyond the existing `v2026.4.23` baseline
- Curriculum files touched: `curriculum/sources/official-reading-map.md`, `curriculum/sources/validation-register.md`, `curriculum/governance-and-security-strand.md`, `curriculum/semester-2/index.md`, `curriculum/semester-2/teaching-guide.md`, `curriculum/labs/advanced-lab-guides.md`, `curriculum/update-and-release-discipline.md`, `curriculum/templates/release-aware-note-template.md`, `curriculum/maintenance/upstream-review-playbook.md`, `curriculum/maintenance/change-control-checklist.md`, `curriculum/maintenance/upstream-state.json`
- Follow-up validation: targeted revalidation of Semester 2 security teaching and audit labs before the next formal curriculum review
- Established the automated drift-check system for future upstream review

### 2026-04-24 targeted follow-up

- Upstream release/advisory baseline unchanged from the same-day review
- Change category: targeted Semester 2 security-teaching revalidation
- Curriculum files touched: `curriculum/governance-and-security-strand.md`, `curriculum/semester-2/index.md`, `curriculum/semester-2/teaching-guide.md`, `curriculum/labs/advanced-lab-guides.md`, `curriculum/assessment/question-bank.md`, `curriculum/assessment/practical-exams.md`, `curriculum/rubrics/master-rubric.md`
- Outcome: clarified `security audit --deep` vs `--fix`, trusted-proxy failure modes, workspace dotenv ownership boundaries, and ACP child-session constraint inheritance
- Follow-up validation: include these items in the next external curriculum audit

## 2026-05-04

- Reviewed upstream baseline through OpenClaw GitHub release `v2026.5.3`
- Reviewed npm package baseline `openclaw@2026.5.3-1`, published after `v2026.5.3` as a core npm hotfix
- Reviewed official release highlights touching plugin install/update hardening, externalized official plugin behavior, file-transfer tooling, channel streaming progress drafts, `/steer`, `/side`, update/doctor behavior, invalid-config fail-closed behavior, provider/proxy handling, memory/search reliability, and Codex harness/persona forwarding
- Reviewed selected open GitHub issues as non-authoritative risk signals, including current plugin, Discord, WSL/browser, security-audit, and performance reports
- Change category: release-drift curriculum repair
- Curriculum files touched: `PROJECT_STATE.md`, `.mentor/MENTOR_STATE.md`, `curriculum/maintenance/upstream-state.json`, `curriculum/maintenance/review-log.md`, `curriculum/sources/official-reading-map.md`, `curriculum/sources/validation-register.md`, `curriculum/update-and-release-discipline.md`, `curriculum/semester-1/index.md`, `curriculum/semester-2/index.md`, `curriculum/labs/lab-catalog.md`, `curriculum/labs/core-lab-guides.md`, `curriculum/labs/advanced-lab-guides.md`, `curriculum/labs/specialization-lab-guides.md`, `curriculum/tracks/plugin-developer.md`, `curriculum/tracks/production-devops.md`, `curriculum/tracks/security-hardening.md`
- Outcome: curriculum baseline updated from `v2026.4.23` to `v2026.5.3` / `2026.5.3-1`; latest plugin/update/file-transfer/release-discipline changes mapped into teaching surfaces
- Follow-up validation: run fresh external Codex/Claude adversarial review after this patch and convert at least the highest-value labs into fully command-by-command manuals

## 2026-08-13

- Reviewed current stable GitHub/npm baseline `v2026.7.1-2` / `openclaw@2026.7.1-2`
- Reviewed package-only extended-stable baseline `openclaw@2026.6.34` and observed beta tag `openclaw@2026.8.1-beta.1` without promoting beta into the teaching baseline
- Reviewed current official install, update-channel, `openclaw attach`, release-note, security-policy, and advisory surfaces
- Reviewed all 112 official advisories published after the prior 2026-04-24 advisory cutoff; integrated representative cases by recurring failure family instead of copying the full feed into teaching material
- Change category: major release, documentation, runtime, coding-agent, update-channel, and advisory drift repair
- Curriculum files touched: `PROJECT_STATE.md`, `.mentor/MENTOR_STATE.md`, `curriculum/maintenance/upstream-state.json`, `curriculum/maintenance/review-log.md`, `curriculum/sources/official-reading-map.md`, `curriculum/sources/validation-register.md`, `curriculum/update-and-release-discipline.md`, `curriculum/governance-and-security-strand.md`, `curriculum/automation-and-detached-work.md`, `curriculum/semester-1/index.md`, `curriculum/semester-2/index.md`, `curriculum/labs/advanced-lab-guides.md`, `curriculum/tracks/security-hardening.md`, `curriculum/templates/release-aware-note-template.md`
- Outcome: refreshed the supported Node floor and flagged conflicting Node 24/26 recommendation text across official docs; taught stable, extended-stable, beta, and dev semantics; added scoped `openclaw attach` and durable coding-agent evidence; strengthened approval, plugin persistence, sandbox/SSRF, credential ownership, channel identity, and detached-authority casework
- Follow-up validation: map the advisory-family cases into assessment questions and model answers, run command-level labs on an installed stable OpenClaw environment, and obtain fresh external adversarial review

## 2026-08-15 Platform-Agnostic Migration

- Change category: curriculum architecture and product-boundary migration
- Evidence reviewed: official agent-framework/harness guidance; MCP, A2A, and OpenTelemetry materials; NIST/OWASP/SSDF; ABET/CS2023/SWEBOK; foundational agent/evaluation research; current OpenClaw, Hermes Agent, ChatGPT Work, and xAI case sources
- Curriculum change: replaced the OpenClaw-centered spine with Agent Harness Systems Engineering outcomes, semesters, labs, assessments, tracks, source policy, and comparative case method
- Product boundary: removed embedded Elite Mentor OS plugin/marketplaces after publishing its standalone repository; Mentor OS work is paused by user decision
- Simplification: removed unpopulated screenshot/classroom-manual layer and consolidated six repetitive role answer packs into one calibration pack
- Executable evidence: added a standard-library-first Python reference harness; current tests cover bounded runtime, tools, approval, context budget, persistent session/event recovery, and repeated-trial evaluation
- OpenClaw handling: preserved `upstream-state.json`, release/advisory review history, drift workflow/script, and OpenClaw as a dated source-visible case study
- Validation: Markdown links, JSON parsing, formatting, Python compilation, and current reference tests passed during implementation; external validation and clean lab reproduction remain pending
- Follow-up: finish advanced executable fixtures, run internal/external adversarial review, reproduce critical labs, calibrate assessors, and pilot with real learners before readiness claims

## 2026-08-15 Internal Migration and Source Validation

- Change category: bounded advanced-fixture implementation, source-drift repair, case-evidence hardening, and internal validation
- Executable evidence: extended the reference harness with per-attempt event identity, schema migration, bounded memory and orchestration, checked protocol/telemetry ports, policy-based repeated-trial evaluation, malformed-provider handling, and adversarial tests
- Protocol drift repaired: updated MCP teaching to the `2026-07-28` stateless per-request negotiation model, pinned A2A `1.0.0`, and moved OpenTelemetry GenAI references to the dedicated semantic-conventions repository
- Case evidence: added dated claim ledgers for Hermes Agent `v2026.8.13`, ChatGPT Work public contracts, and current xAI agent tooling, including explicit unknown-internal boundaries
- OpenClaw drift: authenticated release check remained at `v2026.7.1-2`, extended-stable remained `2026.6.34`, and the observed beta tag advanced to `2026.8.1-beta.2` without changing the stable teaching baseline; advisory metadata showed 647 published records, latest publication `2026-06-30T01:11:32Z`, latest update `2026-08-13T17:27:46Z`, and no later advisory update at review time
- Validation evidence: reference-harness tests, drift-script tests, Python compilation, JSON parsing, local Markdown links, secret-pattern checks, and repository whitespace checks were run; detailed results and unavailable-tool boundaries are recorded in the current internal validation report
- Evidence boundary: the 112 advisories published after the previous cutoff were reviewed in the 2026-08-13 pass; the 2026-08-15 metadata check did not reread the entire 647-record feed, and no authored lab was promoted to independently reproduced
- Follow-up: reproduce critical labs in clean learner environments, implement pinned protocol/provider/telemetry examples where justified, run accessibility and assessor calibration audits, then obtain independent academic, practitioner, and security review

## 2026-09-07 Targeted Release and Teaching Review

- Observed GitHub latest `v2026.9.2`, published `2026-09-05T20:00:07Z`; npm latest `2026.9.2`, beta `2026.9.1`, extended-stable `2026.6.34`. Read grouped release notes, not every contribution/PR. The intervening `v2026.8.1`, `v2026.8.2`, and `v2026.9.1` release migration reviews remain pending.
- Primary docs checked: session tools, gateway security, plugin compatibility, and release channels. Material changes were mapped to session privacy/authority controls, default concurrency, late approvals, recovery/restore regression cases, and the September 8 SDK alias retirement boundary. Sources are linked in the validation register; moving documentation is distinguished from pinned behavior.
- Paginated official advisory API: 647 metadata records, latest update still `2026-08-13T17:27:46Z`; no later updates found. No claim to reread bodies or prove absence of vulnerabilities.
- Updated the validation register, security strand, release discipline, release-aware template, maintenance state, and both continuity files. Preserve the fully reviewed release/date; separate latest-observed fields keep incomplete migration work visible to the drift checker. No user OpenClaw installation was inspected or changed.
- Also finished the interrupted lesson 1-4 teaching expansion and corrected LAB-C6 prerequisite IDs. The two exact Markdown Python examples executed successfully; these are author checks, not student outcomes.
- Verification: both example outputs matched; changing the final answer to 999 caused the intended assertion failure. All four maintenance-script tests passed. Changed JSON parsed, three local Markdown links/anchors resolved, and Git whitespace checks passed. No runtime code changed and the historical 63-test result was not presented as a new execution.
- Required follow-up: finish intermediate release/source review, isolated product regressions and independent security review; continue full teaching development and empirical learner/assessor/accessibility evidence. No readiness gate was promoted.

## Logging rule

Every future upstream review should append:

- date
- upstream release reviewed
- change category
- curriculum files touched
- whether a follow-up validation pass is required
