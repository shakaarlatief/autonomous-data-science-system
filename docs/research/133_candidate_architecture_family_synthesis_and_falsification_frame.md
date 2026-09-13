# Research 133: Candidate Architecture Family Synthesis and Falsification Frame

**Date:** 2026-09-13
**Status:** FIRST ARCHITECTURE-FAMILY SYNTHESIS COMPLETE / CLAUDE INDEPENDENT COUNTER-DESIGN VALID / COMPARATIVE REVIEW ACTIVE / TARGET ARCHITECTURE NOT SELECTED
**Scope:** Begin serious target-architecture synthesis for the ADS project-development knowledge architecture from the complete Research 124 evidence field and frozen Requirements V0.2. Construct materially different coherent architecture families, derive cross-family constraints, identify falsification questions and expose the strongest current integration hypothesis without selecting a target.
**Authority:** Supporting architecture-design research under Research 124. Requirements V0.2 remain the acceptance authority. This record does not authorize implementation, migration or authority switch.
**Declared references:** `research:124`, `research:126`, `research:127`, `research:128`, `research:129`, `research:130`, `research:131`, `research:132`, `checkpoint:474`, `path:docs/research/PROJECT_KNOWLEDGE_ARCHITECTURE_REQUIREMENTS_V02.md`

## 1. Synthesis method

This is the first architecture-design pass after the empirical, external-evidence and anti-anchoring program closed. It deliberately does **not** turn candidate architecture into a numerical tournament. The alternatives below are reasoning instruments. Their purpose is to make hidden assumptions visible, reveal incompatible trade-offs, identify mechanisms that appear necessary across otherwise different designs, and create falsifiable claims before one coherent successor is selected.

The design boundary is fixed by Requirements V0.2, not by the current repository structure and not by ICM. The current architecture remains operational authority and a migration constraint, but any artifact family, knowledge-unit boundary, routing/index mechanism, authority model, history/current representation, workstream model or storage/retrieval mechanism remains redesignable.

A candidate is therefore not judged by resemblance to the current repository. It is judged by whether it can explain, coherently and economically, how the 50 KA-R requirements and 17 KA-I invariants are satisfied and later qualified under the common stress scenarios.

## 2. What every serious candidate must explain

Before comparing implementation families, the evidence implies a set of architectural responsibilities. These are semantic responsibilities, not a frozen list of physical services or files. One component may satisfy several; several components may cooperate on one.

```text
BOOTSTRAP / ORIENTATION
    one stable project-controlled entry
    broad generic continuation, smaller safe task-shaped paths where justified

AUTHORITATIVE KNOWLEDGE SUBSTRATE
    durable accepted project knowledge, rationale and evidence
    one explicit project-development authority

IDENTITY + RELATIONSHIPS
    selective durable identity across representation changes
    explicit material authority, provenance, dependency and workstream relations

WORKSTREAM / CONTINUATION STATE
    active, paused, blocked, completed and superseded work
    dependencies, parent objective, return condition and resume target

CAPTURE / CONSOLIDATION / PROMOTION
    low-friction intake without automatic authority
    source-traceable promotion and recurring active-surface consolidation

CURRENT / HISTORY / TEMPORAL SEMANTICS
    current authority separated from historical provenance
    replacement, supplementation, correction and selective time semantics

DERIVED RECONSTRUCTION VIEWS
    bounded task/domain/current-state/search views
    source, transformation, freshness and rebuildability contracts

AUTHORITY RESOLUTION + ACTION GATING
    relevance retrieval separated from governing-source resolution
    action-shaped source-set resolution, fail-visible ambiguity and contract fidelity

ACTIVE-SURFACE CONTROL
    current routing/context pressure measured and consolidated
    deep evidence stays durable without remaining globally salient

PUBLIC / PRIVATE GOVERNANCE
    explicit delegated private boundary and non-leaking public projections

OBSERVABILITY / QUALIFICATION
    receipts, freshness/health, saturation metrics, reconstruction behavior and migration safety
```

The first design question is therefore not where these responsibilities live. It is which responsibilities need explicit deterministic structure, which can remain in rich human-readable source material, and which may safely be derived probabilistically.

## 3. Cross-family deductions already forced or strongly constrained by V0.2

Several conclusions now survive almost every plausible implementation family. They narrow the design space without selecting a technology.

### 3.1 Pure prose is insufficient for every control-semantic role

V0.2 does not require a graph or database, but KA-R06, R13-R15, R25-R29, R43 and R46 require important continuation, authority, relationship and identity semantics to be explicitly resolvable or queryable without relying solely on heuristic prose scraping. A candidate can keep rich prose as the primary human knowledge expression, but at least the semantics that govern action, continuation and declared identity need a machine-resolvable representation somewhere.

### 3.2 Pure probabilistic retrieval cannot own governing authority

KA-R09, R13 and R24 make this non-negotiable. Lexical, semantic, vector or model retrieval may nominate relevant material and improve recall. Consequential authority must still resolve through explicit applicability/precedence semantics or fail visibly.

### 3.3 Pure current-state snapshots are insufficient

Interruption recovery, migration, selective temporal reconstruction, rejected/superseded rationale and self-hosting redesign require historical lineage. A current projection can be the default interface, but cannot be the only durable representation.

### 3.4 Pure event history is also insufficient as the normal interface

The inverse fails the reconstruction and active-surface requirements. Even an event-oriented authority needs bounded current projections or consolidated knowledge so a fresh collaborator does not replay project history to understand the present.

### 3.5 A globally hand-maintained registry cannot grow linearly with history

Whether the registry is Markdown, JSON, SQL or a graph does not matter. If ordinary local knowledge changes require manual updates across growing global catalogs, the design violates the maintenance economics in KA-R31-R34 and KA-I13. Global views must therefore be generated, dependency-local, bounded, consolidated, or some combination.

### 3.6 Universal semantic atomization is not justified

Research 126 and 129 strongly constrain the opposite extreme. Stable identity should be selective. A concept, governed knowledge unit, workstream, evidence object or important relation may warrant identity; arbitrary sentences, UI groupings, cache rows and transient context packets normally do not.

### 3.7 Source/write authority and reconstruction/read views must be distinguishable

KA-R19-R24, R47 and R50 nearly force this semantic separation even if source and views are stored in the same repository. Query optimization, context assembly and semantic retrieval should not silently become write authority. New accepted insight found through a view must cross an explicit promotion boundary.

### 3.8 Active state should be derived where possible rather than copied into another manual truth surface

The evidence behind active-surface saturation argues against maintaining a second global `active=true` catalog by hand. Current salience should, where practical, follow workstream state, authority status, unresolved obligations, governing procedures, dependencies and explicit lifecycle transitions. Manual override may still exist, but active membership should not become another independently curated ontology.

### 3.9 Workstream continuity and consequential authority are the strongest cases for structured deterministic semantics

These are the domains where failure has direct control consequences and where prose reconstruction is least satisfactory. By contrast, exploratory semantic subject discovery can tolerate more derived/probabilistic assistance because the consequence of one missed adjacent item is different from losing a resume target or using the wrong governing procedure.

## 4. Design axes that distinguish real architecture families

The candidate families below differ along several independent axes. Treating those axes explicitly prevents superficial variants of the same design from masquerading as diversity.

```text
PRIMARY AUTHORITY GRANULARITY
    documents/artifacts | selected semantic objects | normalized registry | event/transition records

SEMANTIC IDENTITY OWNERSHIP
    carrier-local declarations | central bounded spine | object-primary | registry keys | mostly derived

RELATIONSHIP OWNERSHIP
    distributed declarations | central graph/spine | object links | relational rows | event-derived | mostly inferred

CURRENT/HISTORY MODEL
    versioned documents | state + lineage | object versions | event log + projection | relational current + history

ACTIVE-SURFACE MODEL
    generated catalogs | semantic/control projection | object query | materialized projection | dynamic retrieval

DERIVED-STATE ROLE
    static/generated indexes | multi-axis projections | document renderings | materialized views | search/vector/model views

AUTHORITY RESOLUTION
    local declared rules + generated closure | explicit semantic/control closure | object relationships | query/rule engine | event projection | minimal deterministic gate + retrieval

CAPTURE/PROMOTION MODEL
    artifact-local candidate records | spine-linked candidate intake | object lifecycle | event transition | normalized workflow | document intake + explicit promotion
```

A later coherent target may combine mechanisms from several families, but combinations should be justified by responsibility rather than accumulating every attractive feature.

## 5. Candidate Family A: Distributed Document Contracts

### 5.1 Core idea

Human-readable Git artifacts remain the primary authoritative knowledge units. Selected governing/current artifacts carry local machine-readable declarations, either embedded metadata or tightly bound sidecars, for stable identity where needed, scope, epistemic/authority role, material relations, task triggers, workstream links and source lineage. Global navigation, active views and dispatch indexes are generated from those distributed declarations.

This family is closest to an evolved document architecture and can borrow ICM-like recursive catalogs and task contracts without making folder/path identity authoritative.

```text
rich authoritative documents
    + local bounded declarations
        -> generated project/domain/current/task views
        -> generated dispatch/relationship closure
        -> optional lexical/semantic/vector acceleration
```

### 5.2 Strengths

It preserves excellent Git diffability, human inspectability, low migration discontinuity and rich narrative rationale. Authorship stays near the material being governed, reducing a separate global-registry update step. Local declarations can support dependency-local regeneration and make routing views disposable.

### 5.3 Main tension

Distributed declarations can become inconsistent or incomplete exactly where cross-source authority matters. Source-set closure, semantic identity merge/split, multi-hop workstream state and global relation consistency may require increasingly elaborate generation and validation. At some point the distributed metadata may amount to a fragmented database encoded in files.

### 5.4 Falsification question

Reject or materially redesign this family if realistic authority/workstream cases require repeated whole-repository scans or human reconciliation because local declarations cannot reliably produce one coherent identity/authority closure. Also reject it if the metadata burden on ordinary documents becomes large enough that capture friction and schema evolution dominate the simplicity benefit.

## 6. Candidate Family B: Bounded Semantic and Control Spine

### 6.1 Core idea

Keep rich Git artifacts and exact evidence as authoritative source material, but introduce a deliberately small Git-authoritative structured spine for only the project things whose independent identity or control semantics earn it. Likely spine objects include selected subjects/knowledge identities, workstreams/activities, governing procedure/contract identities, accepted knowledge units when they need independent lifecycle, and material authority/provenance/dependency/supersession relations.

The spine is not a copy of all prose. It points to and governs relationships among source artifacts. Search databases, graphs, context packets and semantic indexes are rebuildable projections over the authoritative documents plus spine.

```text
rich authoritative sources/evidence
             +
small authoritative semantic/control spine
             |
             +--> bounded bootstrap/current/workstream views
             +--> authority-resolution closure
             +--> semantic/subject/provenance projections
             +--> lexical/vector/search indexes
```

### 6.2 Strengths

This directly separates narrative/evidence richness from the small set of semantics that must be deterministic. Stable identities survive file moves without forcing every paragraph into an object model. Multi-axis organization can be generated over one identity layer. Workstream and authority closure can be explicit while ordinary research prose remains inexpensive to author.

### 6.3 Main tension

The spine can become a manually curated central registry and recreate the current Knowledge Map problem in a more formal format. Deciding which things deserve identity is itself governance. Every new relation/status adds lifecycle, validation and migration cost. If source documents and spine both restate the same semantic facts, competing truth appears.

### 6.4 Falsification question

Reject or narrow this family if the spine cannot remain small and dependency-local under realistic growth, if ordinary project changes routinely require several manual spine edits, or if humans/models cannot tell which facts belong in source documents versus the spine. Identity merge/split exercises are a critical stress test.


## 7. Candidate Family C: Knowledge-Object-Primary Repository

### 7.1 Core idea

Project knowledge is authored primarily as explicitly identified semantic objects rather than documents being the primary unit. Objects can represent selected concepts, governed knowledge units, workstreams, evidence/source references and material relations. Human-facing documents, domain guides and current-state pages become composed or generated representations of those objects.

```text
semantic knowledge/workstream/source objects
    -> human-readable composed views
    -> current/domain/task projections
    -> graph/search/vector acceleration
    -> exact evidence carriers linked underneath
```

This is not universal sentence atomization. The family still uses the Research 126 identity test, but it moves much farther than Family B by making governed semantic objects the normal durable authoring unit.

### 7.2 Strengths

Stable identity, multi-axis views, relation queries, authority state and representation independence are native rather than retrofitted. A concept can evolve without being bound to one file. Current synthesis, history, workstream context and evidence can become different projections of the same underlying identity graph.

### 7.3 Main tension

Knowledge that is naturally narrative can fragment into many objects whose coherence is harder for humans to author and review. Object boundaries become a permanent design burden. The architecture can shift cost from reconstruction to capture, entity resolution, relationship maintenance, semantic migrations and merge/split adjudication. Generated documents may become the only pleasant reading surface even though they are not themselves authoritative.

### 7.4 Falsification question

Reject or materially constrain this family if representative ADS reasoning requires excessive object splitting, if authors repeatedly need to reconstruct narrative context from many object records, or if `C_capture + C_rel + C_validate + C_migrate` dominates the reconstruction value. A realistic Foundation/Research/Specification conversion exercise should test whether object-primary authoring preserves rationale better or merely atomizes it.

## 8. Candidate Family D: Transition Journal plus Materialized Current Knowledge

### 8.1 Core idea

Authority-significant project changes are preserved as append-oriented transitions or events. Current knowledge, workstream state, authority closure and active views are materialized projections over that durable transition history plus large immutable evidence artifacts. Corrections add new transitions rather than silently overwriting the past.

```text
authority-significant transitions / events
    + immutable or versioned evidence
        -> current semantic projection
        -> workstream projection
        -> authority projection
        -> reconstruction views
```

Only consequential lifecycle changes would become first-class transitions. Ordinary reads, searches and every chat message would not.

### 8.2 Strengths

This family is unusually strong for interruption recovery, auditability, historical reconstruction, authority-transition time, workstream state changes and migration provenance. It naturally preserves how current state came to exist and can rebuild multiple present-day views from one lineage.

### 8.3 Main tension

Event semantics are difficult to design and evolve. Corrections, late-discovered facts, merges/splits and schema evolution can make replay complicated. Current-state usability depends on projection correctness and freshness. If every meaningful knowledge edit becomes an event, capture cost and historical noise explode. If too few events are recorded, the claimed reconstruction advantages disappear.

### 8.4 Falsification question

Reject this family if ordinary current understanding requires expensive replay or projection repair, if event schemas prove harder to evolve safely than state-oriented sources, or if representing semantic corrections requires compensating-event machinery that obscures rather than clarifies project truth. Test abnormal interruption, retroactive correction and schema evolution before treating event lineage as an advantage.

## 9. Candidate Family E: Relational Canonical Registry plus Attached Artifacts

### 9.1 Core idea

A repository-owned structured relational registry becomes authoritative for selected project state: durable IDs, epistemic/authority status, workstreams, dependencies, supersession, source links, lifecycle transitions and perhaps promoted knowledge units. Large prose, code, validation records and evidence remain normal Git artifacts referenced by the registry. Human-readable current/domain views are generated from the relational source plus attached artifacts.

The physical implementation could be a Git-versioned textual relational representation, a SQLite-like store with canonical exports, or another normalized substrate. The family is about the normalized authority model, not one database product.

### 9.2 Strengths

Constraints, joins, uniqueness, relationship closure, workstream queries and explicit migrations are mature capabilities. Authority and continuation semantics can be queried directly rather than generated from dispersed metadata. A relational model can remain smaller and more disciplined than a fully object/graph-primary knowledge representation.

### 9.3 Main tension

Human inspectability, Git diff/review quality, merge behavior and provider/tool portability can degrade depending on physical representation. If human-readable exports are maintained separately they risk becoming a second truth; if generated only on demand, ordinary browsing may depend on tooling. Schema migrations are consequential and centralization increases the blast radius of corruption or bad migrations.

### 9.4 Falsification question

Reject or redesign this family if a clean Git-native review/mutation path cannot be maintained, if concurrent branch changes merge poorly, if inspectability requires opaque specialist tooling, or if generated text views become de facto authority because humans cannot comfortably inspect the registry itself.

## 10. Candidate Family F: Retrieval-First Minimal Formalism

### 10.1 Core idea

Retain rich documents and current artifact families with very little new semantic modeling. Add only deterministic declarations for the control semantics that V0.2 clearly requires, such as governing task classes, authority/supersession, live workstream state, known-risk triggers and stable identities where absolutely necessary. Everything else, especially broad subject organization and adjacent discovery, is assembled dynamically through lexical search, repository search, semantic/vector retrieval and model-generated task contexts.

```text
rich authoritative documents
    + minimal deterministic authority/workstream declarations
    + dynamic lexical/semantic/model retrieval
        -> ephemeral task-shaped context
```

This family deliberately tests the anti-overengineering hypothesis: perhaps a durable semantic spine beyond the control-critical minimum is unnecessary.

### 10.2 Strengths

Capture and schema costs are low. Existing human-readable authority stays direct. Retrieval technology can improve without migrating core truth. Most semantic organization becomes disposable and can be regenerated as models/search improve.

### 10.3 Main tension

The design may save authoring effort by repeatedly paying reconstruction and ambiguity costs. Representation-independent identity, multi-axis organization, provenance traversal and durable concept continuity may remain weak if they are mostly inferred. Dynamic retrieval can also make behavioral qualification less reproducible, and the deterministic minimum may gradually expand until it becomes Family B in practice.

### 10.4 Falsification question

Reject this family if repeated fresh-session tests show that semantic identity, source closure or adjacent risk discovery remains too stochastic under bounded budgets, or if the deterministic exceptions required to satisfy V0.2 grow into an undeclared central semantic/control layer.

## 11. What the six families reveal

The alternatives expose a real architectural continuum rather than six unrelated products.

```text
LESS EXPLICIT SEMANTIC STATE
    Retrieval-First Minimal Formalism
        -> Distributed Document Contracts
            -> Bounded Semantic/Control Spine
                -> Relational Canonical Registry
                    -> Knowledge-Object-Primary

ORTHOGONAL HISTORY AXIS
    Transition Journal can underlie or complement several of the above,
    but becomes a distinct family when transitions are the primary authority model.
```

The important trade is not `files versus database`. It is where the project pays its semantic cost.

```text
less structure now
    -> lower capture/schema cost
    -> higher repeated reconstruction/inference/ambiguity cost

more explicit structure now
    -> stronger deterministic identity/query/authority behavior
    -> higher capture/relation/migration/governance cost
```

Research 129's lifecycle economics therefore becomes central. A candidate cannot be preferred merely because it makes one cold-start demo elegant.

## 12. Mechanisms that appear reusable across multiple families

Several mechanisms are not architecture families and should remain composable options:

```text
small stable bootstrap/router with payload behind routes
recursive project -> domain -> task progressive disclosure
positive + negative context contracts
one-home-per-fact / link rather than copied truth
explicit source-set authority resolution with fail-visible outcomes
pre-action contract binding for consequential work
read-oriented rebuildable generated views
lexical + semantic/vector retrieval subordinate to authority resolution
verified/stale freshness state on material derived views
active-surface pressure metrics and recurring consolidation
forward + reverse dependency/reference walks
source-map-like provenance for selected high-consequence synthesis
repeated correction -> governed source-improvement proposal
copy -> verify -> remove move safety and collision checks
```

The later target should select only the subset whose combined lifecycle value exceeds its maintenance cost.

## 13. First integrated hypothesis to challenge, not a target selection

The evidence currently makes one hybrid shape especially worth challenging:

> **Rich Git-authoritative source artifacts plus a bounded authoritative semantic/control spine plus rebuildable multi-axis/query views.**

This is not selected. It is a working synthesis hypothesis because it appears capable of assigning each kind of complexity to the place where the evidence says it earns its cost:

```text
RICH SOURCE ARTIFACTS
    preserve rationale, exact evidence, specifications, procedures and human inspectability

BOUNDED SEMANTIC/CONTROL SPINE
    owns only selected stable identities, authority/supersession relations, workstream state,
    consequential task/procedure applicability and other semantics that must be deterministic

REBUILDABLE VIEWS
    own broad subject routing, current/domain navigation, search, graph projections,
    semantic/vector acceleration and task-shaped context assembly

CAPTURE/PROMOTION LIFECYCLE
    allows cheap candidate intake while unique accepted insight moves explicitly into authority

ACTION GATE
    resolves the governing source set from action/scope/state/time and binds the required
    contract before consequential guidance or mutation
```

The hypothesis deliberately does **not** decide whether the spine is Markdown/JSON, a set of small typed files, relational data, a static graph, or another repository-owned representation. Physical storage should follow only after the semantic boundary proves coherent.

### 13.1 Why this hypothesis might be wrong

It may be an attractive compromise that inherits the costs of both worlds. It can create two authoring surfaces, difficult object-boundary decisions and schema governance while still depending on rich documents. A disciplined Distributed Document Contracts family might achieve the same behavior with less central machinery. Conversely, an object-primary or relational design might be cleaner because the bounded spine otherwise keeps expanding until it becomes a database badly disguised as metadata.

The independent counter-design phase should therefore be asked to attack this hypothesis rather than merely improve it.

## 14. High-value falsification probes before target narrowing

The next design work should not implement six full systems. It should use the families to choose probes that discriminate architecture assumptions cheaply.

### 14.1 Identity merge/split probe

Take a real durable concept with several historical/canonical representations, then model rename, merge, mistaken merge reversal and split. Compare how Families A, B, C and E preserve provenance and current routing. This directly tests the open KA-R46 governance risk.

### 14.2 Joint-authority closure probe

Model one base procedure plus a mandatory update, one obsolete source and one conflicting candidate. Ask each family to produce the smallest governing source set and a fail-visible ambiguity state without semantic search deciding authority.

### 14.3 Nested workstream interruption probe

Represent a parent route with two dependencies, an interrupted child transition and a deterministic resume target. This tests whether document-local declarations are enough or a central workstream/control substrate is justified.

### 14.4 Active-surface derivation probe

At synthetic 5x/10x history, derive the current project/domain routing surface from live state without manually enumerating historical artifacts. Measure active-route size, generation fan-out and stale-view behavior.

### 14.5 Local-change economics probe

Add one ordinary Research-like artifact, change one governing procedure and split one semantic identity. Measure `C_capture`, `C_rel`, `C_propagate`, `C_validate` and affected artifact count for each serious family.

### 14.6 Derived-store deletion probe

Delete every search/graph/current-view cache and reconstruct the minimum safe project state. This tests whether a candidate has accidentally hidden accepted truth in derived state.

### 14.7 Contract-fidelity probe

Use an ordered operational contract similar to BL-001. The architecture must do more than retrieve it: it must preserve the material ordered constraints into final guidance. This is likely to discriminate control-plane designs more than storage formats.

## 15. Independent counter-design boundary

The first ChatGPT synthesis should now be frozen **before** Claude sees it. The next high-value multi-model move is an `INDEPENDENT_THEN_COMPARATIVE` counter-design from the exact pre-candidate architecture boundary:

```text
233eb932062a24473fcc4f4fe93160c952eea426
```

Claude should receive the frozen V0.2 requirements and the evidence field available at that boundary, but not this Research 133 candidate synthesis during its first architecture-design pass. Its task should be to derive materially different coherent architecture families, identify mechanisms it considers forced versus optional, and state what it would falsify first.

Only after Claude's independent architecture proposal is frozen should it see Research 133 for comparative critique.

This protects against converting the cross-model step into agreement-seeking around the first ChatGPT design.

## 16. Current disposition

No family is selected. No physical storage technology is selected. The bounded semantic/control spine is a **hypothesis to challenge**, not the target architecture.

The substantive progress is that the design space is now structured around real semantic responsibilities and falsifiable trade-offs rather than a list of technologies. The next boundary is independent counter-design, followed by comparative reconciliation and only then targeted mechanism probes or deeper synthesis where disagreement remains.

```text
RESEARCH133=FIRST_ARCHITECTURE_FAMILY_SYNTHESIS_COMPLETE
CANDIDATE_FAMILIES=6
WORKING_INTEGRATED_HYPOTHESIS=BOUNDED_SEMANTIC_CONTROL_SPINE_HYBRID
WORKING_HYPOTHESIS_STATUS=CHALLENGE_NOT_SELECTION
REQUIREMENTS_V02=UNCHANGED_FROZEN
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=INDEPENDENT_CLAUDE_COUNTER_DESIGN
```

## 17. Claude independent counter-design received; comparative question sharpened

MC-0013 Message 001 is a valid candidate-design-independent Claude contribution. Claude stayed on the exact pre-candidate substantive base and did not read this Research 133 record before freezing its design.

The independent pass strongly converges with Research 133 on the architecture-level distinctions: selected control semantics need deterministic project-controlled representation; rationale and nuanced knowledge should remain rich/human-readable; semantic/vector/model retrieval is a subordinate nomination/discovery aid rather than governing authority; distributed document metadata is a serious family; explicit object/graph structure is a serious family with real schema cost; and event orientation is more plausibly selective than universally primary.

The most valuable divergence is now precise. Claude currently prefers a distributed source-local declaration architecture, with generated routing/dispatch closure and a narrow authority-transition ledger. Research 133's strongest ChatGPT hypothesis instead gives selected cross-artifact identity/control semantics their own bounded authoritative spine. The unresolved question is therefore where authoritative deterministic semantics that span several artifacts should live.

ChatGPT's Message 002 also corrects several requirement overstatements before comparative review: V0.2 does not force a pointer-only constitutional core, one project authority does not mean one physical store or one authoritative object per fact, workstream requirements do not force a literal state-machine implementation, KA-R35 requires human inspectability rather than a prose-only source layer, public/private safety is a behavioral requirement rather than a prescribed implementation, and KA-R48 means ordinary canonical commits alone do not fully answer low-friction conversation-born capture. The existing `claude-03` session also cannot repair the historical ChatGPT-only blind-baseline limitation because it is already evaluator-exposed.

The comparison introduces a third hypothesis worth attacking rather than accepting automatically: partition semantic ownership between source-local facts and cross-object/control-state facts. Source-local declarations could own artifact-specific role/scope/evidence metadata, while a bounded cross-object substrate owns identity merge/split mappings, workstream state, relations with independent lifecycle, joint authority closure and selected transition semantics. Global navigation and retrieval remain derived. This may reduce duplicate truth, or it may merely create two authoring systems and a harder boundary problem.

The next Claude turn is intentionally comparative. It will see Research 133 and ChatGPT Message 002 and should decide whether the bounded spine is genuinely distinct, whether partitioned ownership is coherent, and which common-fixture probes best discriminate the remaining serious hypotheses without giving one family an implementation-first advantage.

```text
CLAUDE_INDEPENDENT_DESIGN=VALID_FROZEN
MAIN_ARCHITECTURE_DISAGREEMENT=DISTRIBUTED_DECLARATIONS_VS_BOUNDED_CROSS_OBJECT_SPINE
PARTITIONED_SEMANTIC_OWNERSHIP=HYPOTHESIS_NOT_SELECTION
COMPARATIVE_REVIEW=ACTIVE
REQUIREMENTS_V02=UNCHANGED_FROZEN
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=CLAUDE_MC0013_MESSAGE_003
```
