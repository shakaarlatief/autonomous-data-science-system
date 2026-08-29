# Development Method

**Status:** Current canonical project-development method  
**Current version:** 0.6  
**Last reviewed:** 2026-08-29

## Purpose

This document defines how the Autonomous Data Science System itself is designed, implemented, tested, reviewed, preserved, and evolved.

ADS evolves at two levels:

```text
Level 1  target ADS product/system
Level 2  method used to build, preserve, verify and evolve ADS
```

Both levels should be evidence-driven. The development method must preserve authority, maturity, provenance, reversibility and proportionality of effort.

Deep historical rationale remains in foundations, research, specifications, checkpoints, collaboration records, ledgers and Git history. This document is the operational method.

## Core loop

```text
explore / discuss
-> identify a meaningful question or failure
-> investigate or implement at the smallest justified scope
-> verify proportionately to risk
-> obtain human/model review where required
-> preserve a checkpoint when the boundary materially changes
-> perform promotion audit
-> update canonical knowledge/routing where warranted
-> continue
```

The preservation and verification process must not become so expensive that it interferes with substantive work.

## Checkpoint granularity

The active AI collaborator is responsible for detecting natural checkpoints. A checkpoint is normally warranted when a concept or decision stabilizes, a substantial implementation/experiment milestone is reached, a human-review question materially changes, acceptance/rejection/promotion status changes, the project changes direction, a reusable lesson is discovered, continuity becomes fragile, or preservation is explicitly requested.

A checkpoint is **not** warranted merely because another commit or small visual adjustment occurred.

### Micro-iteration rule

Within one open review/implementation boundary, Git history and the active research/review record should absorb ordinary micro-iterations such as:

```text
pixel-level tuning
small geometry/copy refinements
small implementation defects inside the same hypothesis
test corrections preserving the same contract
exact-target refreshes within the same review question
```

Several small refinements may be preserved together when that review boundary closes or materially changes.

Closed historical checkpoints are not rewritten to make later events appear contemporaneous. An explicitly open review checkpoint may receive a bounded update while the exact same question remains open, provided chronology remains clear in Git.

Checkpoint metadata is governed by `docs/checkpoints/README.md` and mechanically validated.

## Promotion audit

Every substantive checkpoint asks whether stabilized material belongs in a stronger/current layer, including:

```text
VISION.md
PRINCIPLES.md
DECISIONS.md
OPEN_QUESTIONS.md
DEVELOPMENT_METHOD.md
CONTINUITY.md
foundation / research / specification
KNOWLEDGE_MAP.md
experiment/status ledger
MAJOR_CHANGES.md
```

No promotion is a valid outcome. Recentness, prominence or multi-model agreement does not itself confer authority.

## Knowledge layers and authority

Repository roles remain intentionally separate:

```text
canonical docs                 current operational truth
foundations                    deep durable rationale
research                       bounded evidence/candidates
specifications                 explicit scoped contracts
checkpoints                    historical/continuity state
experiment/status ledgers      detailed operational evidence
model-collaboration records    coordination/review provenance
Git history                    exact implementation/document evolution
```

Practical authority order:

1. accepted/frozen current specifications/contracts within scope;
2. explicit current decisions/canonical specifications;
3. current principles, vision, development method, continuity and current state;
4. foundations for rationale;
5. research for bounded evidence;
6. checkpoints/collaboration records for provenance;
7. raw history.

Unresolvable conflicts become explicit open questions rather than guesses.

## Knowledge routing and discoverability

`docs/KNOWLEDGE_MAP.md` is the primary global navigation layer and has two durable responsibilities:

```text
CURRENT CONTINUATION ROUTE
    what is active now and what to read next

EVERGREEN TOPIC LIBRARY
    major topic -> canonical sources + deep rationale + evidence/history
    + specialized indexes/ledgers
```

Current-stage work must not crowd out or replace the evergreen library.

The map routes to sources rather than duplicating their contents. At meaningful stage boundaries, reconcile topic coverage so important new foundations/specifications/research remain discoverable and specialized indexes remain linked.

Structural protection:

```text
scripts/check_knowledge_map.py
.github/workflows/knowledge-map-integrity.yml
```

The validator protects topic presence and route/path integrity. It does not infer semantic authority automatically.

## Risk-scaled verification

Development Method v0.6 separates **development verification** from **acceptance verification**.

```text
V0  documentation / provenance
    relevant structural, routing or metadata validators only

V1  targeted
    exact regression for an isolated change plus adjacent invariant(s)

V2  subsystem
    relevant regressions for one coherent subsystem

V3  full integrated
    complete source-faithful/integrated suite for shared, cross-cutting,
    mixed or uncertain blast radius

V4  promotion / release
    V3 plus relevant provenance, routing, metadata, build and promotion gates
```

Rules:

```text
unknown blast radius -> escalate upward
shared/core mechanism -> V3
pull request/manual full review boundary -> V3 or V4 as appropriate
explicit [full-cockpit] commit marker -> force full Cockpit V3
V1/V2 must never be reported as a complete integrated pass
unexpected dependency/failure -> reclassify and broaden verification
```

### Human visual review ordering

For a low-risk visual refinement:

```text
implement
-> V1/V2 deterministic check
-> human visual review
-> iterate with narrow checks if needed
-> one broader/full gate when the meaningful acceptance boundary closes
```

This avoids repeatedly paying full integration cost for designs the human may immediately reject.

Cross-cutting changes may still require V3 before human review.

### Cockpit selector

Cockpit verification selection is implemented by:

```text
scripts/select_cockpit_verification.py
.github/workflows/cockpit-reintegration-fidelity.yml
```

Only high-confidence local path families may narrow the suite. Mixed/shared/unknown changes fall back conservatively to V3.

Same-branch obsolete CI runs should be cancelled when a newer push supersedes them.

## Coherent repository writes

When several routing/canonical files represent one logical transition, prefer one coherent multi-file commit/tree update where practical. This reduces transient contradictions, redundant CI starts and noisy history.

Do not batch unrelated changes merely for convenience.

## Real-project and system-gap extraction

ADS should be tested on heterogeneous real/realistic projects. When work exposes a weakness, analyze:

```text
observed failure
-> why did the current system/method miss it?
-> project-specific or general?
-> if general, what reusable capability should change?
-> what future test prevents regression?
```

Important Level-2 precedents:

```text
Checkpoint 22 / v0.3   promotion/discoverability architecture
Checkpoint 100 / v0.4  checkpoint metadata contract
MC-0001..0003 / v0.5   governed multi-model collaboration
Research 064           checkpoint hygiene during rapid iteration
Research 103 / v0.6    evergreen topic routing + risk-scaled verification
```

## Governed multi-model development

Canonical collaboration protocol:

```text
docs/model_collaboration/README.md
docs/model_collaboration/INTERACTION_PROVENANCE_AND_NAMING.md
docs/model_collaboration/DEFERRED_REVIEW_AND_CATCHUP.md
```

SOLO remains the default for routine work. Use collaboration when independent review, counter-design, cross-model research or audit value justifies the coordination cost.

One collaborator owns target-state writes unless secondary write surfaces are explicitly declared. Independent-first review requires a frozen immutable base and explicit exposure status. Review of ancestor X does not automatically review descendant Y.

`docs/model_collaboration/REVIEW_INBOX.md` is a convenience route; per-thread state and exact repository artifacts are authoritative.

## Interaction provenance

Visible conversations use `NN - Main Topic / Stage` with provider-local IDs such as `chatgpt-10` or `claude-01`. Provider/model identity is provenance, not authority.

## Knowledge reconciliation

Perform broader reconciliation at meaningful stage boundaries, major method revisions, observed routing drift, major experiment/specification closure, prototype generation changes, or contradiction/staleness events.

Ask:

```text
Are durable insights promoted correctly?
Are VISION/PRINCIPLES/DECISIONS/OPEN_QUESTIONS current?
Does KNOWLEDGE_MAP retain both current routing and evergreen topic coverage?
Are foundations/specifications/research discoverable by topic?
Is CURRENT_STATE concise and present-tense?
Are detailed runs in the right ledgers?
Are checkpoint/session/collaboration metadata coherent?
Are pending reviews discoverable?
Does MAJOR_CHANGES capture significant structural evolution?
```

Reconciliation is periodic, not per-commit.

## Continuity

Canonical cross-session reconstruction is defined in `docs/CONTINUITY.md`.

Substantive preservation failure and routing drift are different problems. If durable source artifacts exist, repair routing conservatively rather than recreating knowledge from memory.

## Deferred infrastructure

The current preservation foundation remains:

```text
Git
Markdown
explicit repository structure
small deterministic validators where earned
AI-assisted curation under normal governance
```

Semantic/vector repository retrieval, generated semantic catalogs, contradiction engines, generalized dependency graphs and heavier orchestration remain deferred until observed need justifies them.

Development Method v0.6 does **not** introduce a knowledge database because the diagnosed failure was routing discipline, not missing storage.

## Version history

### Version 0.6

**Introduced:** Checkpoint 265, 2026-08-29

- V0-V4 risk-scaled verification and escalation rules;
- development verification separated from acceptance verification;
- targeted/subsystem checks before human review for small visual work;
- full integrated/promotion gates retained at meaningful boundaries;
- conservative Cockpit test selection with unknown-path fallback to full;
- `[full-cockpit]` explicit full-gate request;
- CI concurrency cancellation for obsolete iterative runs;
- coherent multi-file batching where appropriate;
- stronger micro-iteration checkpoint aggregation;
- `KNOWLEDGE_MAP.md` restored as current route + evergreen topic library;
- lightweight knowledge-map structural validator.

Evidence:

```text
docs/research/103_repository_knowledge_discoverability_and_risk_scaled_verification_audit.md
docs/checkpoints/265_development_method_v06_knowledge_routing_and_verification_reconciliation.md
```

### Version 0.5

Checkpoint 204, 2026-08-26: governed provider-neutral multi-model development, explicit write ownership, independent-first review, deferred review/catch-up and Specification 024 collaboration-state guard.

### Version 0.4

Checkpoint 100/103, 2026-08-19/20: explicit checkpoint metadata contract and mechanical validation.

### Version 0.3

Checkpoint 76, 2026-08-18: promotion audits, `KNOWLEDGE_MAP.md`, periodic reconciliation, lightweight authority/provenance metadata, `MAJOR_CHANGES.md`.

Deep rationale: `docs/foundations/014_knowledge_preservation_architecture_and_evolution.md`.

### Version 0.2

Checkpoint 2, 2026-08-08: proactive checkpoint detection, conceptual rather than message-count timing, proactive conversation rotation.

### Version 0.1

Checkpoint 0, 2026-08-07: initial fluid discussion, layered preservation, checkpoints, maturity distinctions and method evolution.
