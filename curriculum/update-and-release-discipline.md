# Update and Release Discipline

## Purpose

Keep the stable curriculum, reference harness, framework adapters, protocols, product cases, labs, and claims correct as their change rates differ.

## Layered Change Model

| Layer | Examples | Default handling |
| --- | --- | --- |
| Stable foundations | testing, idempotency, least privilege, experimental design | periodic evidence review |
| Harness contracts | loop, tools, state, policy, observability, eval | design review plus regression tests |
| Standards/protocols | MCP, A2A, OpenTelemetry, NIST/OWASP | pin version; compatibility/security review |
| Framework adapters | SDK APIs, defaults, persistence, tracing | verify before every lab run |
| Product cases | OpenClaw, Hermes, ChatGPT Work, xAI | date claims; review releases/docs/advisories |

## Required Release Record

Every material update records:

- component and old/new version or date
- source and retrieval date
- changed behavior, default, security boundary, or deprecation
- affected outcomes, lessons, labs, assessments, fixtures, and claims
- migration and compatibility impact
- test/evidence plan
- rollback or retirement decision
- owner and next review trigger

## Curriculum Change Gates

1. Triage: editorial, instructional, behavioral, security, protocol, or breaking.
2. Verify with primary evidence and identify contradictions.
3. Separate stable-core impact from adapter/case-study impact.
4. Update all aligned surfaces together.
5. Run links, tests, lab reproduction, and source spot checks appropriate to risk.
6. Seek independent review for security, standards, or high-stakes changes.
7. Record decision and release notes.
8. Retire stale assets rather than leaving conflicting paths.

## Cohort Reproducibility

- Freeze the reference-harness commit and lab dependency versions for graded work.
- Record framework/provider/protocol/product versions used by each cohort.
- Do not change a graded environment mid-cohort without migration support and fairness review.
- Preserve expected evidence and known deviations.
- Teach learners to identify drift rather than memorize one version.

## Security Response

Critical advisories or observed vulnerabilities can override normal cadence. Triage exposure, affected labs/deployments, compensating controls, update/rollback, learner notification, and regression coverage. Do not publish exploit detail that increases harm before coordinated handling.

## Release Channels and Previews

Stable, beta, preview, nightly, source-build, and package-only channels are case-specific. Label them and state why a non-stable surface is included. Preview material cannot silently become a required baseline.

## Teaching Rule

### OpenClaw Migration Exercise (2026-09-07)

Use the dated [validation entry](sources/validation-register.md#targeted-drift-review-2026-09-07), not an assumed current default. Compare the reviewed `v2026.7.1-2` baseline with observed `v2026.9.2`. List intermediate versions still awaiting review. Draft a change decision covering session access, concurrent delegation, restore integrity, and expiring approval ownership. For each, specify one invariant, failure injection, expected evidence, rollback boundary, and owner.

Worked answer fragment: a late approval must not authorize already closed work. Test an allowed on-time approval and a delayed response after cancellation; inspect dispatched effects, not just UI status. A backup command's success is insufficient: restore a synthetic record with unusual bytes and verify exact contents, while a deliberately corrupt archive must fail visibly. These are proposed assessment cases, not product test results.

Assess the learner on finding hidden authority/data changes and proposing discriminating tests. Do not award credit for copying release highlights. Freeze existing graded environments until migration and fairness evidence is accepted; an old pin is reproducible, not automatically secure.

Assess the learner's ability to verify, migrate, test, and communicate change. Do not assess current defaults as timeless facts.

### Irreversible Cleanup Gate

The [intermediate-release ledger](sources/validation-register.md#intermediate-release-triage-2026-09-07) includes a product cleanup path that removes retained migration originals. Treat this as a separate change decision, not the final line of a routine upgrade script.

In a disposable synthetic migration exercise, preserve an old schema snapshot, migrate a copy, change data in the new system, and rehearse restore into a fresh target. Record which new writes rollback would lose and how reconciliation would work. Refuse cleanup until the retained-artifact inventory, tested restore, retention decision, and loss boundary have an accountable owner. Never overwrite the sole original to test the backup.

The instructor presents a conflicting active configuration and older last-known-good copy. Passing work preserves both, diagnoses the conflict, and justifies a merge or refusal instead of silently replacing newer user choices. A dry-run result must be refreshed when relevant state changes; it is not an immutable authorization.
