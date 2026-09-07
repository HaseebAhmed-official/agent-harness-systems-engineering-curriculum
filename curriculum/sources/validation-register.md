# Validation Register

## Purpose

Track the evidence class and claim boundary for curriculum-wide claims. Product- and release-specific facts belong in dated case-study or maintenance records, not in the stable core.

## Claim Status

- `verified-primary`: directly supported by current S0 evidence
- `supported-research`: supported by applicable S1 evidence
- `triangulated`: supported by multiple independent relevant sources with an explicit inference
- `case-specific`: valid only for the dated implementation or product
- `contested`: credible sources or definitions disagree
- `pending`: evidence is incomplete
- `retired`: no longer taught as current

## Core Claim Register

| ID | Claim | Status | Evidence and boundary | Revalidation trigger |
| --- | --- | --- | --- | --- |
| VR-001 | Agent systems should distinguish model reasoning from harness-controlled tools, instructions/context, execution, state, and governance. | triangulated | OpenAI agent guide; Anthropic effective agents/harness posts; curriculum uses an explicit working definition. | Major field-definition or architecture review |
| VR-002 | Deterministic code or workflows should be preferred when they satisfy the requirement; autonomy adds uncertainty, cost, and attack surface. | triangulated | Anthropic effective agents; OpenAI practical guide; engineering inference. Not a ban on agents. | New comparative evidence |
| VR-003 | Single- and multi-agent patterns include routing, parallelization, manager/orchestrator, handoffs, and evaluator-optimizer variants. | verified-primary | OpenAI guide/SDK and Anthropic effective agents. Names and semantics vary by framework. | Framework docs materially change |
| VR-004 | Context quality depends on selection, provenance, freshness, budget, and separation of instructions from untrusted data. | triangulated | Anthropic context/tool guidance; MCP architecture; security guidance. | New context-engineering evidence |
| VR-005 | Long-running work needs explicit state, handoff, recovery, and verification artifacts across context boundaries. | triangulated | Anthropic long-running harness guidance; LangGraph/PydanticAI durable execution. Exact mechanism is architecture-specific. | Durable-runtime changes or new evidence |
| VR-006 | Reliability requires explicit timeout, retry classification, idempotency, cancellation, compensation/recovery, and audit behavior. | triangulated plus executed fixture | Temporal retry/error guidance, LangGraph persistence/interrupt semantics, and AWS idempotent-API guidance; the bounded SQLite fixture executes duplicate-intent checks, classified retry, lease recovery/fencing, cooperative cancellation, incompatible-state quarantine, and manual compensation. It does not prove a workflow engine, distributed lease, actual call timeout, or exactly-once external effect. | Durable-runtime contract, source, or fixture change |
| VR-007 | MCP `2026-07-28` uses host/client/server roles, stateless requests, per-request protocol/capability metadata, and optional up-front `server/discover`; protocol support alone does not prove safe authorization or correct behavior. | verified-primary plus executed fixture | MCP `2026-07-28` architecture/base protocol and Python SDK `2.0.0`; bounded in-process proof observed discovery, version, typed success, malformed-input rejection, and local denial. External transport/auth/resilience remain unproved. | MCP specification or SDK protocol-era release |
| VR-008 | A2A `1.0.0` represents agent discovery plus task/message/artifact exchange across versioned bindings; compatibility and trust require binding/auth tests. | verified-primary plus executed fixture | A2A specification `1.0.0` and Python SDK `1.1.2`; bounded ASGI proof observed AgentCard-driven JSON-RPC task/artifact exchange and missing-credential denial. Streaming, duplicate, cancellation, and remote compatibility remain unproved. | A2A specification or SDK release |
| VR-009 | Shared observability semantics improve portability, but GenAI conventions must be version-pinned and now come from the dedicated OpenTelemetry GenAI repository rather than the core repository. | verified-primary plus executed fixture | OpenTelemetry SDK `1.44.0`; dedicated GenAI repository pinned at `a685613a207a580163353b8e48a7ad88967e7b42`; bounded in-memory proof emitted linked agent/tool spans without supplied content. The conventions are development status; no OTLP/SLO claim follows. | Convention migration, stability, schema, or SDK version change |
| VR-010 | Agent evaluation needs defined tasks, trials, transcripts/outcomes, graders, repeated trials, and suitable capability/regression suites. | triangulated | Anthropic eval guidance; benchmark papers; statistics foundations. Exact sample sizes depend on decision risk and variance. | Evaluation-method review |
| VR-011 | Trace-only or output-only grading can miss material failures; use both when actions and state matter. | triangulated | Anthropic eval guidance and benchmark methods; applicability depends on task. | New evaluation evidence |
| VR-012 | Benchmark success does not establish universal production reliability. | supported-research | AgentBench, tau-bench, OSWorld scopes/limitations; general external-validity principle. | Benchmark or methodology change |
| VR-013 | Prompt injection, excessive agency, confused deputy, exfiltration, persistence, and supply-chain compromise are material agent-system threats. | verified-primary | OWASP agentic materials, NIST AI RMF/GenAI profile, current advisories/case studies. | OWASP/NIST revision or major incident evidence |
| VR-014 | Policy, approvals, sandboxing, network controls, identity, secrets, audit, and recovery are complementary layers; none alone proves security. | triangulated plus executed bounded fixture | [OWASP AI Agent Security](https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html), reviewed 2026-09-06; NIST, Anthropic sandboxing, product advisories. Local `security.py` and 14 tests demonstrate host-issued capability checks and expiring/revocable one-use approvals under scripted malicious proposals. No actual model-injection resistance, network egress, process isolation, durable grants, or independent security audit is established. See LAB-C6 for scope, controls, and transfer requirements. | Security architecture, authorization implementation, threat model, or guidance change |
| VR-015 | Single-user or trusted-operator designs must not be represented as hostile multi-tenant isolation without evidence. | triangulated | Product security boundaries plus least-privilege/isolation principles. | Product/architecture changes |
| VR-016 | AI risk management and secure development require ongoing governance, mapping, measurement, management, and lifecycle evidence. | verified-primary | NIST AI RMF, GenAI Profile, and SSDF. | NIST revision |
| VR-017 | ABET, CS2023, and SWEBOK can inform outcome and content alignment but do not confer accreditation or endorsement. | verified-primary | Official criteria/body-of-knowledge scope. | Criteria revision |
| VR-018 | Delayed, unaided, explicitly changed-task performance is stronger mastery evidence than immediate repetition or polished artifacts. | supported-research | IES retrieval/spacing guidance; Roediger/Karpicke; Cepeda et al.; Barnett/Ceci transfer taxonomy; ICAP and active-learning evidence. The exact delay/change and inference strength remain domain- and task-dependent. | Pedagogy evidence review |
| VR-019 | OpenClaw, Hermes Agent, ChatGPT Work, and xAI agent tooling illustrate different harness/product boundaries; no case proves a universal architecture. | case-specific | Current official docs/source/product pages. Internal architecture cannot be inferred where not public. | Every case-study delivery |
| VR-020 | A learner can build a transferable harness only if implementation, tests, security, evaluation, operations, and defense are directly assessed. | pending | Constructive-alignment rationale is strong; effectiveness still requires pilot learner evidence. | Pilot and external review |
| VR-021 | Practice, active engagement, and feedback can support learning, but no single method or practice quantity establishes expertise or program effectiveness. | supported-research | How People Learn II; ICAP; Freeman et al.; Macnamara et al.; latter explicitly limits overclaims about deliberate practice. | Pedagogy meta-analysis or pilot evidence |
| VR-022 | Assessment decisions require evidence for the intended interpretation/use, consistency, fairness, administration, scoring, and consequences rather than assuming a detailed rubric is valid. | verified-primary | AERA/APA/NCME testing standards; this curriculum's local validity remains pending pilot evidence. | Testing-standards revision or assessment redesign |

## Product Baselines

### LAB-C7 Corpus and Statistics Evidence (2026-09-06)

The original synthetic `harness-contracts-2026-09-06` corpus contains 20 fixed harness-contract tasks, not a population sample or model benchmark. [Anthropic evaluation guidance](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), opened 2026-09-06, supports distinguishing tasks/trials/graders, traces, and final outcomes. [NIST proportion interval guidance](https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm) and its [Wilson formula](https://www.itl.nist.gov/div898/software/dataplot/refman1/auxillar/propconf.htm) support the separate statistical calculation exercise. The automatic corpus report withholds confidence intervals because the tasks are fixed deterministic cases. Known-value and boundary tests check the calculation; no interval proves independence, representative sampling, model quality, or classroom effectiveness. Revalidate when corpus population, sampling design, grader semantics, or statistical method changes. See LAB-C7 for primary-source scope, manual leakage review, and missing evidence.

### OpenClaw

The existing release/advisory baseline is preserved in:

- `../maintenance/upstream-state.json`
- `../maintenance/review-log.md`
- `../maintenance/upstream-review-playbook.md`

OpenClaw facts in legacy files remain case-specific until migrated. Verify them before delivery.

### Other Cases

Hermes Agent, ChatGPT Work, and xAI case-study claims currently have source-map entries but no complete local evidence ledger. They are `pending` for classroom delivery until dated claim tables and exercises are implemented.

## Validation Workflow

1. Identify the exact claim and whether it is stable theory, protocol/framework behavior, product behavior, research finding, or inference.
2. Open the best current primary source; do not rely on this register's summary.
3. Record version/date, supporting passage or code location, contradictions, and scope.
4. Downgrade or split claims that exceed the evidence.
5. Update the affected outcome, lab, assessment, and case study together.
6. Run an independent spot check for security-, standards-, or release-sensitive changes.
7. Record unresolved uncertainty and the next revalidation trigger.

## Freshness Targets

| Claim class | Default review cadence |
| --- | --- |
| Active security advisories and critical product changes | before each delivery and on alert |
| Product/framework releases and APIs | before each lab run |
| Protocol specifications and semantic conventions | each term and before compatibility claims |
| Security/governance standards | each term and on revision |
| Foundational research and pedagogy | annually or when material evidence emerges |

Cadence is a maximum interval, not a guarantee of freshness.
