# Development Method

**Status:** Current canonical project-development method  
**Current version:** 0.8  
**Last reviewed:** 2026-09-01

## Purpose

This document defines how the Autonomous Data Science System itself is designed, implemented, tested, reviewed, preserved and evolved.

ADS evolves at two levels:

```text
Level 1  target ADS product/system
Level 2  method used to build, preserve, verify and evolve ADS
```

Both levels should be evidence-driven. The development method must preserve authority, maturity, provenance, reversibility, discoverability, integrity and proportionality of effort.

Deep historical rationale remains in foundations, research, specifications, checkpoints, collaboration records, ledgers and Git history. This document is the operational method.

## Core loop

```text
explore / discuss
-> identify a meaningful question or failure
-> investigate or implement at the smallest justified scope
-> verify proportionately to risk
-> obtain human/model review where required
-> reconcile canonical state when the boundary changes
-> preserve a checkpoint when a meaningful verified boundary is earned
-> perform promotion audit
-> continue
```

The preservation and verification process must be strong enough for a large long-lived project without becoming so expensive that it interferes with substantive work.

## Repository information architecture

Development Method v0.8 preserves the v0.7 single-responsibility information architecture and adds a bounded integrity layer around it:

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

As the repository grows, different retrieval questions must not collapse into one document:

```text
Where am I now?                -> CURRENT_STATE / current_routing
What kind of artifact is this? -> docs/README
What do we know about X?       -> KNOWLEDGE_MAP
How do I reconstruct safely?   -> CONTINUITY
How do we build/verify ADS?    -> DEVELOPMENT_METHOD
```

A document that tries to answer all of them will become noisy, stale and difficult to maintain.

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

`CURRENT_STATE.md` is authoritative for **what boundary is active now**, but routes to stronger evidence for the underlying product/scientific claim.

Unresolvable conflicts become explicit open questions rather than guesses.

## Family-aware repository integrity

ADS does not impose one universal Markdown schema on its history. Repository integrity is family-aware and prospective.

The governed classes are:

```text
live canonical state
numbered durable knowledge
checkpoints
validation/evidence
model collaboration
specialized ledgers/indexes
global prose/code/Git history
```

The public integrity implementation follows Research 106 and Specifications 025/026:

```text
numbered identity
    unique inside each governed family
    same number across different families remains valid

prospective metadata
    Foundation >= 025 requires Date / Status / Scope
    Specification >= 025 requires Date / Status / Scope
    Research >= 106 requires Date / Status / Scope
    checkpoint metadata remains governed by the existing checkpoint contract

validation/evidence
    exact pre-cutover paths are preserved by one immutable compatibility snapshot
    new paths require Date, a result field and a governed anchor

declared references
    new generic references use the strict typed Declared references field
    unambiguous existing explicit relationship fields remain compatibility-checked
    mixed narrative prose is never mined heuristically

identity agreement
    if an H1 explicitly declares governed family + number, it must agree with the filename
```

The compatibility snapshot is a migration boundary, not a hand-maintained artifact registry. Normal development must not extend it to bypass prospective validation.

## Live-state integrity

`docs/CURRENT_STATE.md` and `docs/current_routing.json` own overlapping live facts and must agree.

Agreement alone is insufficient when both are stale. On the active development branch:

```text
current_checkpoint == maximum numbered checkpoint present in that checked branch tree
```

The rule is branch-scoped. An unrelated branch with a different historical checkpoint population does not make the active branch stale.

`current_boundary` is a semantic routing label, not a second checkpoint title. It must satisfy the stable bounded contract:

```text
lowercase words separated by hyphens only
no digits
no underscores
maximum length 64
```

Exact historical identity belongs in dedicated checkpoint/research/specification fields and artifacts.

## Checkpoint granularity

The active AI collaborator is responsible for detecting natural checkpoints. A checkpoint is normally warranted when a concept or decision stabilizes, a substantial implementation/experiment milestone is reached, a human-review question materially changes, acceptance/rejection/promotion status changes, the project changes direction, a reusable lesson is discovered, continuity becomes fragile, or preservation is explicitly requested.

A checkpoint is **not** warranted merely because another commit, specification or small adjustment occurred.

### Micro-iteration rule

Within one open review/implementation boundary, Git history and the active research/review record should absorb ordinary micro-iterations such as:

```text
pixel-level tuning
small geometry/copy refinements
small implementation defects inside the same hypothesis
test corrections preserving the same contract
exact-target refreshes within the same review question
canonical reconciliation edits belonging to one already-frozen transition
```

Several small refinements may be preserved together when that review boundary closes or materially changes.

Closed historical checkpoints are not rewritten to make later events appear contemporaneous. Metadata/provenance-only repair is permitted when it restores the checkpoint contract or corrects provenance without rewriting substantive historical knowledge.

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

The validator protects topic identity/non-empty routing, Subject-index alignment, path integrity, exhaustive durable-family coverage, checkpoint-range coverage, specialized-index reachability and absence of live-state leakage.

A green Knowledge Map validator establishes **structural coverage and integrity**, not semantic-routing correctness. Periodic reconciliation therefore includes a lightweight routing-quality spot-check.

## Risk-scaled verification

Development Method v0.8 retains the V0-V4 risk-scaled verification model:

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

Same-branch obsolete CI runs should be cancelled when a newer push supersedes them where the workflow supports that behavior.

## Public repository integrity gate

When the repository-integrity architecture is in scope, the deterministic aggregate must report exactly one public result:

```text
PUBLIC_REPOSITORY_INTEGRITY=PASS
PUBLIC_REPOSITORY_INTEGRITY=FAIL
```

The aggregate reuses the accepted focused validators rather than creating parallel truth systems. It covers at least:

```text
family-aware identity and prospective metadata
validation/evidence compatibility/prospective contract
typed and compatible explicit references
Knowledge Map integrity
CURRENT_STATE/current_routing synchronization
active-branch checkpoint freshness
stable current_boundary
checkpoint metadata
model-collaboration state
```

A failure is not repaired by weakening the validator. Diagnose the exact contract and classify whether the repository or the implementation is wrong.

The active development branch may be unprotected. A passing GitHub Actions workflow is useful evidence, but it must not be described as enforced branch protection. Before a governed integrity transition is accepted, run the relevant deterministic gate on the actual target through a controlled execution surface or equivalently authoritative path and preserve what actually ran.

## Private continuity and transition preflight

Public repository integrity and private continuity are orthogonal claims:

```text
PUBLIC_REPOSITORY_INTEGRITY
    PASS | FAIL

PRIVATE_CONTINUITY_INTEGRITY
    PASS | FAIL | NOT_VERIFIED

CHAT_ROTATION_PREFLIGHT
    PASS | HOLD | FAIL
```

Rules:

```text
private inaccessible
    -> NOT_VERIFIED, not fabricated PASS and not public FAIL

public PASS + required private NOT_VERIFIED
    -> rotation HOLD

public PASS + accessible required private mismatch
    -> rotation FAIL

public PASS + required private PASS + no open transition obligations
    -> rotation may PASS
```

The private companion's public-safe synchronization anchor is stored in its existing `CURRENT_PRIVATE_STATE.md` as the public continuity checkpoint and exact public commit last reconciled against.

## Coherent repository writes

When several routing/canonical files represent one logical transition, prefer one coherent multi-file commit/tree update where practical. This reduces transient contradictions, redundant CI starts and noisy history.

Do not batch unrelated changes merely for convenience.

Before the final branch ref is advanced for a multi-file mutation, re-read the branch HEAD. If it moved since the operation was prepared, do not force the write; reconstruct against the new target.

## Abnormal execution interruption recovery

A tool-backed task can terminate after some durable writes complete but before later writes, verification, reconciliation or the final report. The correct recovery behavior is repository-first reconstruction, not trust in the interrupted conversation and not blind replay of the plan.

After an outage, tool failure, unexplained termination or user interruption during a multi-step repository mutation:

```text
1. inspect current branch HEAD before further mutation
2. identify the last independently trusted durable boundary
3. enumerate commits/files/actions that actually completed after it
4. compare completed work with the intended staged plan
5. classify apparent inconsistencies as:
       EXPECTED / DEFERRED
       KNOWN DEFECT / PLANNED REPAIR
       INTERRUPTION RESIDUE
       NEW UNPLANNED DEFECT
6. repair only findings appropriate to the current stage
7. rerun required verification rather than inheriting interrupted completion claims
8. preserve a recovery record when the interruption materially affects continuity
```

A user interruption is allowed and does not itself imply Git corruption. Completed Git operations remain durable. The protocol prevents a partially completed logical workflow from being mistaken for a completed transition.

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
MC-0008 / v0.8         family-aware integrity + continuity/preflight hardening
Research 107           abnormal-interruption recovery audit and classification method
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

Visible conversations use `NN - Main Topic / Stage` with provider-local IDs such as `chatgpt-13` or `claude-01`. Provider/model identity is provenance, not authority.

Every newly opened persistent interaction receives a fresh identity. Disposable diagnostic/plugin test interactions are not automatically promoted into the persistent ADS session sequence.

## Knowledge reconciliation

Perform broader reconciliation at meaningful stage boundaries, major method revisions, observed routing drift, major experiment/specification closure, prototype generation changes, contradiction/staleness events, or after a staged integrity implementation explicitly reaches its canonical-reconciliation phase.

Ask the questions separately:

```text
Is CURRENT_STATE concise, present-tense and accurate?
Does current_routing agree with CURRENT_STATE?
Is the active-branch checkpoint fresh?
Is current_boundary stable and semantic?
Does docs/README describe the repository roles that actually exist?
Does KNOWLEDGE_MAP exhaustively route durable numbered knowledge by subject?
Does a lightweight sample confirm routing quality, not merely route coverage?
Are specialized indexes still globally reachable?
Are VISION/PRINCIPLES/DECISIONS/OPEN_QUESTIONS current?
Are foundations/specifications/research discoverable by subject?
Are detailed runs in the right ledgers?
Are checkpoint/session/collaboration metadata coherent?
Are pending reviews discoverable?
Does the relevant public integrity aggregate pass on the actual target?
Is private continuity evaluated separately when required?
Does MAJOR_CHANGES capture significant structural evolution?
```

Reconciliation is periodic, not per-commit.

## Continuity

Canonical cross-session reconstruction is defined in `docs/CONTINUITY.md`.

Bootstrap-critical reconstruction must directly read `docs/CONTINUITY.md` as the third mandatory first-read after `README.md` and `docs/README.md`; it must not depend on an indirect routing hop.

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

Development Method v0.8 still does **not** introduce a vector/semantic knowledge database. The integrity layer is deliberately small, typed and attached to existing authority surfaces rather than becoming a second truth system.

If the central Knowledge Map later becomes a demonstrated reconstruction-read-cost or maintenance bottleneck, or repeated semantic-routing drift survives the current guards, distributed per-artifact topic metadata with a generated semantic view remains the leading lightweight successor architecture to evaluate before introducing a heavier semantic repository database.

## Version history

### Version 0.8

**Introduced:** repository-integrity canonical reconciliation, 2026-09-01. A checkpoint is intentionally deferred until the wider transition earns a meaningful verified boundary.

- retained the v0.7 single-responsibility repository information architecture;
- added family-aware prospective repository-integrity contracts rather than a universal historical schema;
- added branch-scoped current-checkpoint freshness and stable semantic `current_boundary` rules;
- added the aggregate `PUBLIC_REPOSITORY_INTEGRITY` gate without replacing focused validators;
- separated public integrity, private continuity and chat-rotation preflight claims;
- added the private-side public continuity anchor contract;
- made `docs/CONTINUITY.md` an explicit mandatory bootstrap read;
- added abnormal-execution interruption recovery and four-way finding classification;
- made coherent multi-file canonical reconciliation and branch-HEAD revalidation explicit;
- preserved Source Vault and product-specific authority boundaries while strengthening Level-2 governance.

Evidence:

```text
docs/research/106_governed_repository_integrity_and_continuity_bootstrap_hardening.md
docs/research/107_post_outage_repository_integrity_recovery_audit.md
docs/specifications/025_v1_governed_repository_integrity_and_continuity_hardening.md
docs/specifications/026_v1_repository_integrity_recovery_amendment.md
```

### Version 0.7

Checkpoint 266, 2026-08-29: separated stable landing, structural guide, live state, machine routing, semantic subject library and continuity procedure; required exhaustive durable-family routing; added checkpoint-range coverage and verification-command integrity; retained v0.6 risk-scaled verification and checkpoint aggregation.

### Version 0.6

Checkpoint 265, 2026-08-29: restored broad topic routing after discoverability drift; introduced V0-V4 risk-scaled verification, Cockpit selector/concurrency cancellation and stronger micro-checkpoint aggregation. Its two-layer Knowledge Map was an intermediate repair and was refined by v0.7.

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
