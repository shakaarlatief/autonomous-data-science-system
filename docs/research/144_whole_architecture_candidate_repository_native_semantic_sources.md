# Research 144: Whole-Architecture Candidate - Repository-Native Semantic Sources with Selective Identity, Derived Views, and Action-Gated Authority

**Date:** 2026-09-14
**Status:** SERIOUS WHOLE-ARCHITECTURE CANDIDATE SYNTHESIZED / DESIGN-COVERAGE QUALIFICATION NEXT / TARGET ARCHITECTURE NOT SELECTED
**Candidate label:** `PKA-CANDIDATE-01`
**Scope:** Synthesize one serious successor architecture from the complete Research 124 evidence field after the H1/H2 mechanism probes, real-corpus independent review, MC-0014/MC-0015 corrections, D1-D8 external evidence and owner-provided ICM evaluation. Define enough logical structure, authority semantics, typed source responsibilities, derived-view behavior, activation, lifecycle, validation, scaling and migration behavior to qualify the candidate systematically against Requirements V0.2.
**Authority:** Candidate architecture research only. Requirements V0.2 remain the frozen acceptance authority. This record does not select the target architecture, migrate current authority, or authorize implementation as the production continuity system.
**Declared references:** `research:124`, `research:125`, `research:126`, `research:127`, `research:128`, `research:129`, `research:130`, `research:131`, `research:132`, `research:133`, `research:134`, `research:136`, `research:138`, `research:139`, `research:143`, `path:docs/research/PROJECT_KNOWLEDGE_ARCHITECTURE_REQUIREMENTS_V02.md`, `checkpoint:488`

## 1. Candidate statement

The candidate is:

> **A repository-native architecture in which rich human-readable semantic sources remain the primary authority; durable semantic identity is assigned selectively where continuity matters; authoritative facts normally have one canonical semantic source; genuinely joint authority is represented only as an explicit exception; global current-state, routing, search, dependency, identity and authority-closure surfaces are generated/rebuildable views; and consequential actions pass through action-shaped authority resolution plus contract activation before guidance or mutation is finalized.**

This is deliberately not a global semantic registry, not a pure-document architecture, not an object-primary knowledge graph, and not retrieval-first memory.

```text
stable bootstrap / constitutional core
        |
        v
 task/reconstruction planner
     /               \
broad continuation   narrow governed task
     |                    |
     v                    v
generated views      authority resolver
     |                    |
     +---------+----------+
               |
               v
     repository-native semantic sources
       /       |       |       \
   knowledge workstreams procedures evidence
       \       |       |       /
        +-------+-------+------+
                |
       selective identity + typed relations
                |
       explicit promotion boundary
                |
       generated/rebuildable secondary views
```

## 2. Why this is no longer H1 versus H2

Research 136 showed that ordinary cross-object relations do not require a separate spine. Research 138/MC-0014 showed that the strongest H1 sidecar and H2 both reified the difficult relation, so their difference partly collapsed into ownership/addressing. Research 143 then showed that semantic first-classness and authority home are independent axes.

The candidate therefore uses the corrected model:

```text
STEP 0
    identify one singular semantic unit / proposition

AXIS I: SEMANTIC CONTINUITY / IDENTITY
    DURABLE_IDENTITY
    NO_SEPARATE_IDENTITY
    UNRESOLVED

AXIS A: AUTHORITY MODE / HOME
    SINGLE_SOURCE
    JOINT_AUTHORITY
    DERIVED_ONLY
    UNRESOLVED
```

For example:

```text
Cockpit workstream
    identity    DURABLE_IDENTITY
    authority   SINGLE_SOURCE

aggregate active / paused / next projection
    identity    NO_SEPARATE_IDENTITY
    authority   DERIVED_ONLY
```

The architecture is built around those distinctions rather than around whether information is physically in documents or in a spine.

## 3. Constitutional boundary

The candidate preserves the existing project constitution unless and until an explicit qualified switch occurs:

```text
project-development authority
    public ADS repository

transient model/chat memory
    never authority

private companion continuity
    delegated only where explicitly allowed;
    never silently overrides public state

current architecture
    remains operational authority throughout candidate implementation,
    shadow qualification and migration
```

The successor can use multiple canonical semantic sources inside the repository without creating multiple project authorities. One project authority means one governed authority domain, not one physical file or universal table.

## 4. Responsibility decomposition

The candidate has nine logical responsibilities. They need not become nine services or directories.

### 4.1 Stable bootstrap and constitutional core

A very small authored bootstrap surface contains only project identity/authority boundary, how to inspect current route and freshness, broad-versus-narrow reconstruction rules, authority-resolution procedure, fail/escalate behavior, and pointers to derived-view generation/validation contracts. It must not accumulate project history, active-workstream lists, large catalogs or ordinary knowledge payload.

The current `CONTINUITY.md` is the natural compatibility point for this role during migration.

### 4.2 Canonical semantic-source layer

Rich project knowledge remains primarily in repository-native, human-readable sources such as decisions, requirements, research syntheses, governing procedures, workstream sources and evidence records.

A canonical semantic source contains rich explanatory content plus only the structured declarations needed for machine-safe identity, authority, relation, lifecycle or reconstruction semantics. The candidate rejects a universal giant metadata block on every file.

### 4.3 Selective identity and relationship semantics

Durable semantic IDs are introduced only where continuity matters, for example workstreams, governed procedures, durable decisions/knowledge units or relations whose own lifecycle genuinely matters. Ordinary files, paragraphs, headings, search clusters and generated navigation nodes do not automatically receive semantic IDs.

Directional relations are authored once by the natural semantic owner wherever possible. Reverse edges and closures are generated.

### 4.4 Capture, candidate consolidation and promotion

Conversation-born or tool-born reasoning can enter a low-friction non-authoritative capture surface. It may later be consolidated into a candidate synthesis. Unique accepted understanding becomes authority only through explicit promotion onto a canonical semantic source.

### 4.5 Derived-view generation

Current routing, broad current-state views, identity indexes, authority closure, subject indexes, dependency graphs, search indexes and task packets are derived from canonical sources wherever practical. They are read surfaces, not ordinary mutation surfaces.

### 4.6 Reconstruction and retrieval planning

A small planner chooses the minimum safe path:

```text
generic continuation
    broad orientation -> active route -> relevant domain -> detail

narrow governed task
    minimal safe orientation -> authority resolution -> exact governing sources

exploratory research
    semantic/lexical retrieval -> evidence drill-down -> explicit uncertainty
```

Positive and negative context contracts may state both what must be loaded and what should remain latent.

### 4.7 Authority resolution and action-contract activation

A project-controlled resolver computes the governing source or source set for consequential work from explicit applicability, scope, lifecycle and supersession semantics. Probabilistic retrieval can nominate candidates but cannot silently make the final governing decision when explicit semantics exist.

Where a procedure contains mandatory ordered constraints, preconditions or prohibitions, those constraints are activated as an action contract and checked against proposed guidance/action before dispatch.

### 4.8 Validation, consolidation and maintenance control

Local schema/relation checks, impact-aware validation, freshness checks, periodic qualification and recurring active-surface consolidation keep maintenance bounded while preserving history.

### 4.9 Migration and degraded-mode control

The candidate is built and qualified in shadow mode. Current authority remains live. Public/private degraded behavior, rollback, generated-view loss and migration parity are explicit before any switch.

## 5. Canonical source profiles

The candidate uses **profiles**, not one universal ontology. A source adopts only the structured fields required by its responsibility.

### 5.1 Common governed-source envelope

A source participating in machine-resolved semantics may declare the equivalent of:

```text
kind
    responsibility profile

authority_class
    canonical / candidate / historical / derived / evidence as applicable

semantic_id
    only when durable identity is required

lifecycle_or_epistemic_state
    only where current/candidate/historical/superseded/rejected/etc. matters

scope
    only where applicability cannot be inferred safely

relations
    only directional relations this source naturally owns

provenance/evidence references
    when traceability is materially required

temporal qualifiers
    only where recording/applicability/authority times can diverge materially
```

Empty irrelevant fields are not required. The logical model does not yet freeze YAML versus another repository-native syntax. The selected encoding must keep structured semantics adjacent to the rich source, machine-parseable and human-inspectable without creating a second authoritative sidecar by default.

## 6. Profile: workstream/activity

A resumable workstream is a strong `DURABLE_IDENTITY + SINGLE_SOURCE` case. Its canonical source declares the equivalent of:

```text
semantic_id              required
state                    active / paused / blocked / completed / superseded
parent                   optional
requires / depends_on    zero or more
pause_reason             required when deliberately paused
return_condition         required when expected to resume
resume_target            required when expected to resume
current_anchor           optional exact branch/ref/checkpoint/task anchor
```

The prose owns objective, rationale and explanatory context. The structured declaration owns only the control semantics needed for deterministic continuation. Global active/paused/next routing is generated from these sources.

## 7. Profile: governing procedure / action contract

A consequential governing procedure normally has durable identity because paths may change while the procedure remains conceptually continuous. It may declare identity, status/applicability, scope/action classes governed, authority transitions and selective effective time.

For exact-fidelity procedures, the same governed source also carries a structured action contract representing machine-checkable material constraints:

```text
preconditions
ordered mandatory constraints / steps
prohibitions
required postconditions / verification
fail-closed conditions
```

The prose remains rich and authoritative. The structured contract is an authoritative projection within the same source, not an LLM-generated shadow copy.

## 8. Profile: decision / requirement / accepted knowledge unit

Durable decisions and accepted syntheses may reuse stable identifiers such as `D-033` or `research:124` where continuity matters. Typical structured semantics are deliberately small: identity, current epistemic/authority state, scope if material, source/evidence basis when synthesized, selective supersession/update relation and selective temporal applicability.

Most explanatory content stays in prose. The architecture does not atomize every sentence into a claim object.

## 9. Profile: evidence/source

Evidence artifacts need enough identity/provenance for drill-down but do not automatically become governing knowledge. A source may expose artifact/source identity, evidence class, exact revision/external citation and links from promoted knowledge. Reverse citation views are generated where possible.

## 10. Selective identity lifecycle

A semantic ID is project-owned and independent of the current path/filename. The candidate distinguishes:

```text
rename / move               same identity, new carrier
representation replacement same intended identity, changed carrier/form
merge                       two prior identities become one; old refs remain resolvable
split                       one prior identity becomes several successors
supersession                old identity remains historical but loses current authority
retirement                  identity remains resolvable but inactive
```

Ordinarily the canonical source carries the stable ID and a generated identity index maps ID to current carrier. Merge/split/redirect creates a small authoritative identity-transition record or tombstone because the transition itself has historical/provenance meaning. This is selective, not a hand-maintained global registry.

## 11. Relationship ownership rule

For every material relation:

```text
1. Can one semantic source honestly own the directional fact?
       yes -> author it once there

2. Is the queried relationship only a deterministic closure/view over source-owned facts?
       yes -> DERIVED_ONLY

3. Does the relation itself need durable identity/lifecycle/provenance distinct from participants?
       yes -> give the relation one canonical semantic source

4. Does the authoritative content genuinely require multiple sources together?
       yes -> JOINT_AUTHORITY exception

5. If ownership remains ambiguous
       -> UNRESOLVED; do not duplicate the fact to hide ambiguity
```

## 12. Joint-authority exception

Requirements V0.2 must support governing source sets even though Corpus V0.1 did not produce a clean real hard case. A **joint-authority declaration** may therefore exist only when no single source can honestly own the complete governing content.

It owns only combination semantics:

```text
optional durable identity for the authority-set relationship
member governing sources
scope / action class
combination rule such as all-required, precedence, base-plus-supplement
selective effective time
conflict / unresolved status
```

It does not copy substantive member content. This is not a global spine. It is a repository-native semantic source created only for a demonstrated joint-authority case; a generated authority index discovers such declarations alongside source-local authority relations.


## 13. Supersession and temporal semantics

The default historical mechanism remains Git plus durable source status and explicit relation semantics. No universal event ledger is introduced.

Where current authority depends on the distinction, a source may declare a minimal authority-transition mode:

```text
REPLACE
    successor fully replaces predecessor for declared scope

SUPPLEMENT
    predecessor remains governing and successor must be consumed with it

SPECIALIZE
    successor governs a narrower declared scope

CORRECT
    predecessor's prior statement is erroneous for declared scope
```

Temporal fields are selective:

```text
recorded_at / Git revision
    normally available from repository history

effective_from / effective_to
    only where applicability differs materially from recording

authority_from
    only where acceptance/promotion time differs materially
```

Generated current-authority views resolve these semantics, not merely latest-commit recency.

## 14. Capture and promotion lifecycle

The candidate uses four semantic roles without requiring four permanent artifact families:

```text
CAPTURE
    low-friction, incomplete, non-authoritative intake

CONSOLIDATED_CANDIDATE
    source-linked synthesis suitable for review

PROMOTED_DURABLE_KNOWLEDGE
    explicitly accepted canonical source or canonical-source update

DERIVED_CONSUMPTION_VIEW
    task-shaped read representation over durable sources
```

A capture record requires only enough structure to preserve origin: capture ID, recorded time, source/provenance pointer, candidate status and an optional rough subject/workstream link.

Promotion records what was accepted, the source/candidate basis and which canonical source now owns the understanding. Temporary capture state may later be archived/removed when the promoted source preserves sufficient provenance and rejected rationale.

## 15. Derived-view contract

The candidate treats these as generated/rebuildable by default:

```text
current routing
broad current-state orientation
Knowledge Map / subject-artifact navigation
identity lookup index
authority candidate/closure index
workstream graph and active route projection
provenance reverse index
search / lexical / semantic indexes
change-impact indexes
context packets
```

Every persistent derived view exposes or has an adjacent manifest with the equivalent of:

```text
view identity / purpose
authority_class = derived
source boundary / revisions or digest
generator identity + version
rebuildability class
creation/refreshed boundary
freshness/staleness state
failure/rebuild procedure
```

Structural views should normally be deterministic/reproducible. Probabilistic semantic summaries may be regenerable rather than byte-identical, but cannot silently contain unique accepted truth.

## 16. Compatibility treatment of current global surfaces

The candidate preserves stable compatibility entry paths during migration while changing their eventual authority role.

### `CONTINUITY.md`

Remains authored and small. It becomes the stable bootstrap/constitutional protocol rather than a growing state packet.

### `current_routing.json`

Becomes a committed deterministic derived projection over active workstream/current-route declarations. It remains useful at cold start but no longer duplicates hand-authored route truth.

### `CURRENT_STATE.md`

Becomes a human-readable current-orientation view generated or consolidated from canonical active sources. Any unique accepted insight discovered during generation must be promoted into a canonical source before the view can rely on it as project truth.

### `KNOWLEDGE_MAP.md`

Becomes a generated navigation/subject index over source-local declarations and artifact inventory, avoiding indefinite hand-maintained path enumeration.

These role changes are candidate behavior only. The files' current authority remains unchanged until migration qualification and explicit switch.

## 17. Reconstruction planner

The planner consumes the small bootstrap plus task intent and produces a bounded reconstruction contract containing, as needed:

```text
task class / intended action
minimum safe orientation sources/views
must-load governing sources
supporting/evidence sources
negative-context / do-not-load guidance
freshness requirements
expected receipt fields
fail/escalate conditions
```

### Generic continuation

```text
bootstrap
-> current routing/current-state view
-> active workstream source(s)
-> relevant unresolved risks/authority
-> drill down only as needed
```

### Narrow governed task

```text
bootstrap protocol
-> task/action classification
-> authority resolver
-> exact governing source set + action contract
-> minimal supporting evidence
-> action/guidance conformance check
```

Full broad orientation is not mandatory for the narrow path.

## 18. Retrieval stack

The candidate uses several subordinate access paths:

```text
exact semantic-id lookup
exact path/artifact lookup
structured relation/authority/workstream indexes
lexical search
optional semantic/vector retrieval
optional hierarchical/global summaries
```

No retriever is itself authority. Search results expose source role/authority class where known. Optional retrieval failure may degrade discovery but cannot silently bypass deterministic governing-source resolution.

## 19. Authority resolver

The resolver is a project-controlled deterministic/hybrid component whose **decision contract** is deterministic even if a model assists task classification.

Input semantics include:

```text
intended action / requested operation
target / scope
current workstream/environment
actor/role when material
consequence profile
time query when material
```

It resolves:

```text
applicable canonical governing sources
required supplements / joint-authority declarations
supersession / precedence / effective-time closure
conflicts or missing required authority
material action-contract constraints
```

Its receipt includes:

```text
resolution status
source IDs + exact revisions
why they apply
combination semantics
activated constraint IDs
freshness/availability result
unresolved conflict or missing-evidence state
```

If explicit semantics do not resolve a high-consequence ambiguity, the resolver fails visibly rather than asking a language model to blend plausible sources.

## 20. Action-contract conformance

BL-001 proved that source activation is insufficient if mandatory procedure constraints disappear or reorder in final guidance.

For procedures with structured action contracts, candidate qualification must demonstrate:

```text
all mandatory constraints survive into guidance/action
ordered constraints remain ordered
prohibitions are not omitted or contradicted
preconditions are checked before mutation/advice
postconditions/verification are preserved
missing/contradictory constraints fail visibly
```

Free-form semantic conformance may require model-assisted verification, but critical constraint IDs and ordering provide a deterministic backbone. One model pass is not accepted as sole proof for high-consequence promotion/execution.

## 21. Workstream continuation model

Workstreams are first-class semantic units when continuity matters, but their state remains single-source whenever possible.

The workstream graph supports:

```text
parent / child
multiple dependencies
active / paused / blocked / completed / superseded
pause reason
return condition
resume target
current anchor
```

The global active route is a generated projection. Interruption recovery reads durable workstream sources and completed project evidence; it does not replay a previous chat plan as completed work.

Concurrent updates use expected source revision / Git-head semantics. Stale writes fail before authoritative mutation.

## 22. Public/private boundary

The public repository remains project-development authority.

A public source/view may declare an abstract private dependency without leaking private paths or details, for example:

```text
private_dependency: required-for-task-X
verification_status: unavailable / verified / stale
```

Public reconstruction remains usable without private detail for ordinary public work. If a consequential task genuinely requires delegated private state and that state cannot be verified, the task fails/escalates visibly instead of inferring missing content from memory.

Generated public views receive non-leakage validation before publication.

## 23. Validation architecture

Validation is layered by cost and dependency radius.

### Local deterministic checks

```text
profile/schema validity
semantic ID format/uniqueness within affected scope
relation target existence
workstream state-field consistency
procedure contract syntax/order uniqueness
private/public field restrictions
```

### Impact-aware checks

```text
identity redirect/merge/split closure
workstream dependency/resume consistency
authority closure / replacement-supplement semantics
derived-view affected dependency set
reverse inbound references for move/migration
```

### Behavioral checks

```text
cold continuation walk
narrow governed-task authority resolution
action-contract fidelity
missing/conflicting authority failure
interruption/resume
optional retrieval outage
public/private degraded mode
derived-store deletion/rebuild
```

### Periodic / milestone full qualification

```text
full generated-view rebuild
whole-repository referential integrity
5x/10x scaling simulation
consolidation fidelity audit
migration parity / rollback test
provider/model switch reconstruction
```

## 24. Maintenance and dependency economics

Global views are generated from local canonical declarations. An ordinary local change should therefore touch one or a few canonical sources plus the affected generated dependency neighborhood, rather than a growing list of global maps.

Persistent views are limited to those that materially reduce reconstruction/activation cost. Ephemeral task packets need not be committed.

The candidate tracks at least:

```text
manual touch fan-out
generated refresh fan-out
active view bytes/tokens
cold-start reads/calls
authority resolution reads/calls
stale-view detection latency
consolidation frequency/review cost
schema/identity migration impact
```


## 25. Recurring consolidation

Consolidation is not a one-time migration cleanup. Possible triggers include routing-payload growth, active-view token/byte pressure, high route fan-out, repeated downstream correction, excess historical detail on the active path, stale/conflicting summaries and workstream closure.

The process is:

```text
identify pressure
-> generate/source-link candidate synthesis
-> verify must-preserve view contract
-> explicitly promote accepted synthesis where unique understanding is created
-> mark detailed sources historical/latent as appropriate
-> rebuild active views
-> preserve drill-down/provenance
```

High-consequence consolidation receives proportionate independent verification or reconciliation.

## 26. Why this candidate should scale better than the current architecture

The current architecture often copies growing state into manually maintained global surfaces. Candidate 01 changes the scaling relation:

```text
history grows
    -> canonical source/history grows
    -> active/global views remain bounded by current semantic state and view contract

local source changes
    -> affected declarations change
    -> dependent views regenerate
    -> unrelated global files do not require manual edits
```

The candidate does not promise constant cost. A genuinely more complex active project can require a larger active view. It promises that passive historical accumulation does not structurally force proportional active-context or manual-routing growth.

## 27. Migration strategy

Migration is staged and **single-authority throughout**.

### M0 - shadow tooling

Build parsers/validators/generators over existing sources without changing current authority.

### M1 - active/high-consequence declarations

Add structured declarations only to active workstreams, current governing procedures and other high-value sources needed for qualification. Do not mass-convert history.

### M2 - generated compatibility views

Generate shadow versions of current routing, current-state and Knowledge Map surfaces. Compare against current manually governed outputs and investigate differences.

### M3 - identity and authority shadow resolution

Build identity index and authority closure. Exercise merge/split, update/supplement and missing/conflict cases without changing production routing.

### M4 - capture/promotion path

Exercise low-friction capture, candidate consolidation and explicit promotion on bounded real work.

### M5 - scaling and degraded-mode qualification

Run 5x/10x synthetic history growth, derived deletion/rebuild, provider switch, private-unavailable and concurrent-update tests.

### M6 - migration reconciliation

Map current canonical/active knowledge to successor source profiles. Preserve stable identities, historical rationale and current authority. Use forward/reverse reference walks plus copy -> verify -> remove discipline where carriers move.

### M7 - explicit authority switch

Only after full Requirements V0.2 qualification, owner acceptance, rollback proof and repository integrity may the project make an explicit authority transition. Until then, the current continuity architecture remains authoritative.

## 28. How the candidate differs from earlier architecture families

### Versus Distributed Document Contracts / original H1

It retains source-local ownership but adds selective semantic identity, typed workstream/procedure contracts, exceptional joint-authority objects, capture/promotion and project-controlled authority activation.

### Versus Bounded Semantic/Control Spine / original H2

It does not create a default central cross-object control store. First-class identity and structured semantics normally remain with one canonical semantic source; joint-authority objects are exceptions.

### Versus Object-Primary / H3

Rich repository sources remain the normal authoritative representation. Only selected semantic units receive structured identity/lifecycle. The project is not decomposed into a universal object graph.

### Versus Retrieval-First Minimal Formalism / H0

Retrieval remains subordinate. Governing authority, workstream continuation, promotion, identity transitions and critical action contracts have explicit deterministic semantics.

### Versus event sourcing

Git plus current sources and selective temporal/transition declarations remain sufficient unless later qualification demonstrates a recurring historical-replay need that cannot be served safely otherwise.

## 29. Deliberately rejected design moves

Candidate 01 rejects:

```text
one giant hand-maintained semantic registry
one giant metadata schema on every file
semantic IDs for every paragraph/sentence
centralizing every cross-object relation
persisting every conceivable derived view
making embeddings/vector search authoritative
making generated current-state summaries write authorities
universal event sourcing
universal bitemporal fields
manual global route updates for every knowledge addition
using long context as the primary scaling strategy
forcing human review after every low-risk transformation
```

## 30. Concrete open implementation choices

The candidate is concrete at the semantic/contract level but intentionally leaves several physical choices for qualification:

```text
structured declaration syntax
    YAML front matter, constrained Markdown block or another repository-native encoding

exact directory layout
    existing artifact families may remain; semantic identity must not depend on path

identity format
    reuse stable existing IDs where possible; define new project-owned IDs only when needed

view generator implementation
    Python/static generation is a likely prototype; architecture does not depend on it

semantic search implementation
    optional and subordinate

consequence-policy calibration
    exact profiles/thresholds need behavioral qualification

free-form action-contract conformance checker
    deterministic constraint backbone is specified; semantic checker remains to prove
```

These are implementation degrees of freedom that Requirements V0.2 deliberately leaves open.

## 31. Candidate falsification conditions

Candidate 01 should be weakened or rejected if implementation shows any of the following:

```text
source-local declarations require routine edits to many unrelated files

derived global views cannot be rebuilt without unique hidden truth

stable identity merge/split becomes a growing manual global registry

joint-authority exceptions proliferate so widely that the exception becomes a de facto spine

workstream/current-state generation loses important rationale or creates ambiguous resume state

authority closure cannot reliably distinguish replace/supplement/specialize/correct

action-contract checking remains too weak to prevent BL-001-style fidelity failures

capture is too burdensome and important reasoning remains trapped in conversations

consolidation omits governing constraints/uncertainty or requires globally expensive review

public/private degraded mode leaks private metadata or makes ordinary public reconstruction unusable

5x/10x passive history growth materially expands mandatory active context or ordinary manual maintenance

migration requires a big-bang authority switch or loses semantic identity/provenance
```

## 32. Synthesis disposition

Candidate 01 is the first post-MC-0015 **whole-architecture candidate** that incorporates the entire evidence program without reverting to the old H1/H2 split.

It is strong enough for systematic Requirements V0.2 design-coverage review and targeted implementation qualification.

It is **not yet selected** because the most consequential mechanisms remain unimplemented as one integrated system, especially authority/action-contract fidelity, identity transitions, exceptional joint authority, generated-current-view parity, capture/promotion ergonomics, consolidation fidelity, public/private degraded mode and 5x/10x maintenance behavior.

```text
CANDIDATE=PKA-CANDIDATE-01
WHOLE_ARCHITECTURE_SYNTHESIS=COMPLETE
RICH_REPOSITORY_NATIVE_SOURCES=PRIMARY
SELECTIVE_DURABLE_IDENTITY=YES
DEFAULT_AUTHORITY_MODE=SINGLE_SOURCE
JOINT_AUTHORITY=BOUNDED_EXCEPTION
GLOBAL_CURRENT_NAVIGATION_STATE=DERIVED_BY_DEFAULT
ACTION_GATED_AUTHORITY=CORE
CAPTURE_DOES_NOT_IMPLY_AUTHORITY=CORE
MECHANIZED_REIFICATION_CLASSIFIER=NOT_REQUIRED_FOR_V01
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=SYSTEMATIC_REQUIREMENTS_V02_DESIGN_COVERAGE_AND_QUALIFICATION_PLAN
```
