# Development Method

**Status:** Current canonical project-development method  
**Current version:** 0.7  
**Last reviewed:** 2026-08-29

## Purpose

This document defines how the Autonomous Data Science System itself is designed, implemented, tested, reviewed, preserved and evolved.

ADS evolves at two levels:

```text
Level 1  target ADS product/system
Level 2  method used to build, preserve, verify and evolve ADS
```

Both levels should be evidence-driven. The development method must preserve authority, maturity, provenance, reversibility, discoverability and proportionality of effort.

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

The preservation and verification process must be strong enough for a large long-lived project without becoming so expensive that it interferes with substantive work.

## Repository information architecture

Development Method v0.7 gives each global navigation/state surface one primary responsibility:

```text
README.md
    stable repository landing page

docs/README.md
    structural repository/documentation guide
    artifact family -> role / authority / lifecycle

docs/CURRENT_STATE.md
    sole human-readable live project state
    current boundary / verification / exact next step

docs/current_routing.json
    sole compact machine-readable live routing pointer

docs/KNOWLEDGE_MAP.md
    evergreen semantic subject library
    subject -> relevant durable knowledge

docs/CONTINUITY.md
    reconstruction / rotation / recovery procedure

docs/DEVELOPMENT_METHOD.md
    method used to build, verify, preserve and evolve ADS

docs/MAJOR_CHANGES.md
    selective structural history
```

Cross-linking is expected. Volatile checkpoint/branch/test state should not be copied into stable navigation files merely for convenience.

### Why the separation matters

As the repository grows, three different retrieval questions must not collapse into one document:

```text
Where am I now?               -> CURRENT_STATE / current_routing
What kind of artifact is this? -> docs/README
What do we know about X?       -> KNOWLEDGE_MAP
```

A document that tries to answer all three will become noisy, stale and difficult to maintain.

## Knowledge layers and authority

Repository roles remain intentionally separate:

```text
canonical docs                 current operational/cross-project truth
foundations                    deep durable rationale
research                       bounded evidence/candidates/investigations
specifications                 explicit scoped contracts
checkpoints                    historical/continuity state
specialized indexes/ledgers    domain-specific navigation/provenance
model-collaboration records    coordination/review provenance
code/tests                     exact executable mechanisms and regressions
Git history                    exact implementation/document evolution
```

The detailed structural guide is `docs/README.md`.

Practical authority order within the relevant scope:

1. accepted/frozen current specifications/contracts;
2. explicit current decisions/canonical documents;
3. current principles, vision, development method and continuity;
4. foundations for rationale;
5. research for bounded evidence;
6. checkpoints/collaboration records for provenance;
7. raw history.

`CURRENT_STATE.md` is authoritative for **what boundary is active now**, but should route to stronger evidence for the underlying product/scientific claim.

Unresolvable conflicts become explicit open questions rather than guesses.

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

Metadata-only repair is permitted when it restores the checkpoint metadata contract without altering substantive historical claims.

Checkpoint metadata and role are governed by `docs/checkpoints/README.md` and mechanically validated.

## Promotion audit

Every substantive checkpoint asks whether stabilized material belongs in a stronger/current layer, including:

```text
VISION.md
PRINCIPLES.md
DECISIONS.md
OPEN_QUESTIONS.md
DEVELOPMENT_METHOD.md
CONTINUITY.md
docs/README.md
foundation / research / specification
KNOWLEDGE_MAP.md
experiment/status ledger
MAJOR_CHANGES.md
```

No promotion is a valid outcome. Recentness, prominence or multi-model agreement does not itself confer authority.

## Knowledge routing and discoverability

`docs/KNOWLEDGE_MAP.md` is the global **semantic** navigation layer. It has one durable responsibility:

```text
EVERGREEN SUBJECT LIBRARY
    subject -> canonical sources + deep rationale + bounded evidence/history
    + specialized indexes/ledgers
```

It does not carry live current checkpoint, branch, CI or next-step state. Those belong to `CURRENT_STATE.md` and `current_routing.json`.

### Exhaustive durable-family routing

The Knowledge Map must explicitly route every numbered artifact in:

```text
docs/foundations/
docs/specifications/
docs/research/
```

A source may be routed to multiple subjects. Multiple membership is a feature when it improves retrieval.

Numbered checkpoints are assigned through compact semantic range records so every historical checkpoint belongs to one or more topics without reproducing the entire checkpoint directory as visible prose. Important checkpoints may additionally be linked directly.

Specialized indexes remain first-class retrieval surfaces and should be linked rather than copied into the global map.

Structural protection:

```text
scripts/check_knowledge_map.py
.github/workflows/knowledge-map-integrity.yml
```

The validator protects:

```text
topic identity and non-empty routing
human-readable Subject-index alignment with KM-TOPIC subject headings
path integrity
exhaustive Foundation / Specification / Research coverage
checkpoint-range coverage
specialized-index reachability
absence of live-state sections in the Knowledge Map
```

A green Knowledge Map validator establishes **structural coverage and integrity**, not semantic-routing correctness. It does not infer semantic authority automatically and cannot prove that every artifact was assigned to the best subject. Periodic reconciliation therefore includes a lightweight routing-quality spot-check in addition to mechanical coverage validation.

## Risk-scaled verification

Development Method v0.7 retains the v0.6 separation between **development verification** and **acceptance verification**.

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

### Verification-command integrity

The verification tier is determined by **what tests actually executed**, not by the workflow label or intended selector output.

A full-suite command must be constructed so patterns are expanded/interpreted by the test runner correctly. If quoting, interpolation or shell behavior accidentally narrows a requested V3 run, that run is not accepted as V3 evidence even if the workflow is green.

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
Research 103 / v0.6    evergreen routing recovery + risk-scaled verification
Research 104 / v0.7    single-responsibility information architecture + exhaustive routing
MC-0005                 adversarial v0.7 architecture review + narrow routing hardening
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

Ask the questions separately:

```text
Is CURRENT_STATE concise, present-tense and accurate?
Does current_routing agree with CURRENT_STATE?
Does docs/README describe the repository roles that actually exist?
Does KNOWLEDGE_MAP exhaustively route durable numbered knowledge by subject?
Does a lightweight sample confirm routing quality, not merely route coverage?
Are specialized indexes still globally reachable?
Are VISION/PRINCIPLES/DECISIONS/OPEN_QUESTIONS current?
Are foundations/specifications/research discoverable by subject?
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

Development Method v0.7 does **not** introduce a vector/semantic knowledge database because the diagnosed failure remains information architecture and routing discipline, not inability to store or retrieve repository artifacts with the current scale and tooling.

If the central Knowledge Map later becomes a demonstrated reconstruction-read-cost or maintenance bottleneck, or repeated semantic-routing drift survives the current guards, distributed per-artifact topic metadata with a generated semantic view is the leading lightweight successor architecture to evaluate before introducing a heavier semantic repository database.

## Version history

### Version 0.7

**Introduced:** Checkpoint 266, 2026-08-29

- separated stable landing, structural guide, live state, machine routing, semantic subject library and continuity procedure;
- added `docs/README.md` as the repository/documentation artifact-role map;
- made `CURRENT_STATE.md` the sole human-readable owner of volatile current state;
- made `current_routing.json` the sole compact machine-readable current pointer;
- made `KNOWLEDGE_MAP.md` evergreen subject routing only;
- required exhaustive topic routing for every numbered Foundation, Specification and Research record;
- added validated semantic checkpoint-range coverage for all numbered checkpoints;
- preserved multiple topic membership where useful;
- strengthened Knowledge Map CI to detect unassigned durable knowledge and live-state leakage;
- retained v0.6 checkpoint aggregation and V0-V4 risk-scaled verification;
- added verification-command integrity after the first v0.6 forced-full workflow executed only a narrowed subset because of quoting;
- after MC-0005, added Subject-index/`KM-TOPIC` alignment validation and made the structural-coverage-versus-semantic-correctness boundary explicit without changing the v0.7 architecture.

Evidence:

```text
docs/research/104_repository_information_architecture_and_exhaustive_knowledge_routing_refinement.md
docs/checkpoints/266_repository_information_architecture_and_exhaustive_knowledge_routing.md
docs/model_collaboration/threads/MC-0005/RESOLUTION.md
```

### Version 0.6

Checkpoint 265, 2026-08-29: restored broad topic routing after discoverability drift; introduced V0-V4 risk-scaled verification, Cockpit selector/concurrency cancellation and stronger micro-checkpoint aggregation. Its two-layer Knowledge Map was an intermediate repair and is refined by v0.7.

### Version 0.5

Checkpoint 204, 2026-08-26: governed provider-neutral multi-model development, explicit write ownership, independent-first review, deferred review/catch-up and Specification 024 collaboration-state guard.

### Version 0.4

Checkpoint 100/103, 2026-08-19/20: explicit checkpoint metadata contract and mechanical validation.

### Version 0.3

Checkpoint 76, 2026-08-18: promotion audits, `KNOWLEDGE_MAP.md`, periodic reconciliation, lightweight authority/provenance metadata and `MAJOR_CHANGES.md`.

Deep rationale: `docs/foundations/014_knowledge_preservation_architecture_and_evolution.md`.

### Version 0.2

Checkpoint 2, 2026-08-08: proactive checkpoint detection, conceptual rather than message-count timing, proactive conversation rotation.

### Version 0.1

Checkpoint 0, 2026-08-07: initial fluid discussion, layered preservation, checkpoints, maturity distinctions and method evolution.
