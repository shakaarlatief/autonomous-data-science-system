# Project-Development Knowledge Architecture Requirements V0.2

**Date frozen:** 2026-09-13
**Status:** OWNER-ACCEPTED / FROZEN V0.2 BASELINE WITH PROSPECTIVE AO-9 P7-D02 AMENDMENT
**Owner acceptance:** explicit approval in `chatgpt-23` after Research 130 reconciliation
**Scope:** Architecture-neutral acceptance requirements and invariants for the successor project-development knowledge architecture supporting development of ADS. This is not the architecture of the ADS product itself.
**Supersedes for candidate-design purposes:** the original Phase-B KA-R01..KA-R45 and KA-I01..KA-I15 wording embedded in Research 124. The original wording remains durable historical provenance.
**Evidence basis:** Research 124; historical failure corpus; BL-001, BL-002-B, BL-002U, BL-003 and BL-004; Research 126-129 D1-D8; Research 130 reconciliation; owner whole-architecture freedom clarification.
**Authority:** Frozen Research 124 requirements boundary. It constrains candidate comparison and later target selection but does not itself select a target architecture, storage technology, ontology, database, retrieval system, policy engine or migration plan.

## 1. Normative vocabulary

```text
MUST
    A candidate cannot be selected without satisfying the property.

CONDITIONAL MUST
    Mandatory when the stated task, consequence class or semantic condition applies.

SHOULD
    Strong preference. A candidate may diverge only with an explicit evidence-backed
    trade-off and compensating mechanism.

QUALIFICATION MUST
    Mandatory property of candidate evaluation/qualification rather than a runtime
    architecture feature.

DISCRIMINATOR
    Must be measured or compared, but no preferred direction is frozen in advance.
```

The requirements intentionally describe required **behavior and semantics**, not an implementation family.

## 2. Reconstruction and continuity requirements

### KA-R01: persistent project understanding
**Strength:** MUST

The architecture must preserve and make reusable the project's accumulated understanding, not merely retain document bytes. Material semantic identity, rationale, epistemic state, authority status and provenance must survive conversation loss, model changes, human-memory loss and ordinary environment restarts where they are needed for correct reconstruction.

### KA-R02: stable project-controlled bootstrap
**Strength:** MUST

One stable project-controlled entry mechanism must be sufficient to initiate reconstruction. Normal continuation must not require a human-maintained prompt containing a growing list of files, checkpoint numbers or hidden chat context. The entry mechanism is not required to be a Markdown file or file-only construct.

### KA-R03: conversation and model independence
**Strength:** MUST

No material current project fact, accepted rationale, active route, unresolved obligation, authority state or migration-critical knowledge may exist only in one conversation, one model's memory or one provider-specific hidden memory surface.

### KA-R04: task-shaped safe orientation
**Strength:** CONDITIONAL MUST

Generic continuation and cold-start reconstruction must establish broad project orientation before substantive continuation. A narrow governed task may instead use a smaller task-shaped orientation when that smaller context is sufficient to establish current state, affected scope, applicable authority, important constraints and unresolved uncertainty safely.

Full project-wide Tier-A reconstruction is therefore not automatically mandatory before every narrow consequential task.

### KA-R05: progressive disclosure
**Strength:** MUST

The architecture must support progressively deeper traversal from project orientation to domain, workstream/subdomain, governing source and exact evidence without requiring whole-corpus reading. Traversal depth and must-preserve detail are shaped by the current task/view contract.

### KA-R06: active route reconstruction
**Strength:** MUST

Where a live project route exists, the complete active continuation chain must be reconstructable, including the current workstream, parent objective, why the route exists, dependencies or blocks, and what higher-level work resumes after the route closes.

### KA-R07: relevant discovery with safety-calibrated recall
**Strength:** MUST for governing/risk-bearing discovery; SHOULD for adjacent exploratory discovery

A collaborator must be able to discover governing and risk-bearing knowledge relevant to a task without already knowing exact filenames, artifact numbers or prior-chat search terms. High recall for merely adjacent exploratory knowledge remains desirable but is not itself a deterministic safety guarantee.

### KA-R08: reconstruction and authority-resolution receipts
**Strength:** CONDITIONAL MUST

Consequential authority resolution, migration, qualification and other governed transitions must be observable enough to report what relevant surfaces were traversed, which governing sources were activated, which areas remained latent or unavailable, and which uncertainty remains unresolved. Ordinary exploratory work may use a lighter receipt.

A receipt is evidence of traversal and decision state, not proof that a model semantically understood every source.

### KA-R09: consequential-action authority activation and contract fidelity
**Strength:** MUST

Before consequential guidance or action, the architecture must resolve the applicable governing authority, make required source consumption observable, extract/bind the task-relevant governing contract strongly enough to preserve material constraints, and prevent final guidance/action from silently violating that contract.

If required authority cannot be resolved, consumed or reconciled, or if material conformance cannot be established where required, the system must fail visibly according to consequence policy rather than proceed from memory or plausible inference.

### KA-R10: known-risk and evolution-trigger activation
**Strength:** CONDITIONAL MUST

Known limitations, deferred upgrades, reopen triggers and previously observed failure conditions must be activatable when the current task or observed condition intersects them. The architecture must not depend on a human remembering that such a warning exists.

### KA-R11: uncertainty visibility
**Strength:** MUST

Missing required authority, unresolved conflict, unavailable required evidence/private state, uncertain reconstruction or unresolved material relationships must remain explicit. The system must not convert missing resolution into confident inference.

## 3. Authority, epistemic and relationship requirements

### KA-R12: explicit epistemic role
**Strength:** MUST

The architecture must distinguish material epistemic/authority states such as current accepted knowledge, candidate/provisional knowledge, historical or formerly applicable knowledge, superseded knowledge, rejected or known-wrong knowledge, raw evidence, open questions and known limitations when those distinctions affect reasoning.

The architecture is not required to impose one universal artifact taxonomy over all knowledge.

### KA-R13: action-shaped authority resolution
**Strength:** MUST

Authority must be resolved from the concrete intended action, affected scope/target, relevant role/status, environment/current state, applicable temporal semantics and supersession/precedence relations. Current authority may be one source or a governed source set.

Recency alone, directory position alone, semantic similarity alone or model confidence alone may not determine current truth.

### KA-R14: supersession, supplementation and conflict visibility
**Strength:** MUST

Declared authority relationships must be resolvable enough to distinguish materially different semantics such as replacement/obsolescence, update/supplementation, refinement/specialization and correction where the distinction changes current authority.

If apparently governing sources remain incompatible after normal authority rules, the conflict must surface as unresolved rather than being silently blended.

### KA-R15: relationship semantics
**Strength:** MUST

Relationships that materially affect understanding, authority, provenance or continuation must be explicitly representable and queryable without relying solely on heuristic prose scraping. Relation types and metadata must remain demand-driven.

Where the relationship itself carries material state, time, certainty, provenance or authority semantics, the architecture must be capable of representing those semantics. Not every prose mention or edge requires first-class relation identity.

### KA-R16: current state, history and selective temporal semantics
**Strength:** MUST

The architecture must preserve historical depth without forcing current-state surfaces to grow monotonically with all history. Current state, historical chronology and deep evidence must remain distinguishable.

Where authority, correction or historical reconstruction requires it, the architecture must also be capable of separating domain/applicability time, repository knowledge/recording time and authority-transition time. Universal bitemporal/tritemporal metadata is not required when those dimensions cannot diverge materially.

### KA-R17: view-contract consolidation fidelity
**Strength:** MUST

Compression or consolidation may omit detail from an active representation only when omitted detail remains durably recoverable and the representation preserves every semantic property required by its declared use.

Depending on the view, fidelity may require source support, coverage, uncertainty/disagreement, authority status, relationships, temporal meaning, negative/minority evidence and provenance. Material omission is a first-class fidelity failure.

### KA-R18: synthesis provenance and auditability
**Strength:** MUST

Material claims in promoted or consequential synthesis must retain a traversable route to their source basis and, where material, the transformation that produced them. Provenance granularity must be sufficient to audit important claims without requiring whole-corpus rereading.

Universal sentence-level provenance is not required.

## 4. Authority substrate and derived-state requirements

### KA-R19: one explicit project-development authority
**Strength:** MUST

ADS must retain one explicit project-development authority. At this boundary that authority remains the public ADS repository. Any future authority switch must be explicit, qualified and separately accepted. A database, graph, index, cache or other store may not become accidental competing authority merely because it is convenient.

### KA-R20: explicit authority class for stores and views
**Strength:** MUST

Every persistent knowledge store or view introduced by a candidate must have an explicit authority role/class. Captured/candidate surfaces, generated indexes, embeddings, caches, graph projections, search databases and reconstruction plans do not acquire authority automatically through storage or repeated use.

### KA-R21: rebuildability appropriate to representation
**Strength:** MUST

Derived state materially used by reconstruction must declare and satisfy an appropriate rebuildability contract. Structural projections should normally be reproducible deterministically from authoritative inputs and versioned generation logic/configuration. Probabilistic semantic synthesis may instead be regenerable/auditable with source/transformation provenance and semantic review rather than byte-identical.

Loss of genuinely derived state must not destroy unique accepted project truth.

### KA-R22: explicit promotion of unique accepted synthesis
**Strength:** MUST

If human/model synthesis produces unique understanding the project accepts as durable truth, that understanding must cross an explicit, source-traceable promotion boundary onto the authoritative substrate. It may not remain unique only inside a cache, search index, vector store, generated view or model response.

### KA-R23: freshness, source and authority-closure binding
**Strength:** MUST

A derived representation materially used for reconstruction must expose enough source revision, transformation/generator and freshness information to detect stale material relative to its declared contract. Where “current” depends on temporal or supersession semantics, freshness must include correct authority closure rather than merely latest repository revision.

### KA-R24: probabilistic retrieval is not sole governing authority
**Strength:** MUST

Semantic/vector/model-based retrieval may nominate candidate sources and improve recall, but it may not silently resolve high-consequence governing authority when explicit applicability/precedence semantics are available. Required authority needs a deterministic or otherwise verifiable resolution path, or a fail-visible unresolved result.
## 5. Workstream and continuation requirements

### KA-R25: explicit workstream identity and state
**Strength:** MUST

Active, paused, blocked, completed and superseded workstreams must be distinguishable without reconstructing control flow from chronological prose. A workstream/activity may have its own continuity independent of the current file used to document it.

### KA-R26: explicit pause and return semantics
**Strength:** MUST

Every deliberately paused route expected to resume must be able to express why it paused, what condition/dependency permits return, what exact or typed target resumes, and what parent objective it belongs to. A bare `PAUSED` label is insufficient for long-lived nested work.

### KA-R27: multiple dependencies
**Strength:** MUST capability

The continuation model must support multiple dependency edges where project work requires them. The design must not force a strict tree when the underlying work is naturally DAG-like.

### KA-R28: interruption recovery
**Strength:** MUST

After abnormal interruption during a multi-step transition, the architecture must support reconstruction of intended versus durably completed versus still-pending work from durable project/action evidence. It must not require blind replay of a previous conversation plan.

### KA-R29: concurrent collaborator safety
**Strength:** MUST

When several humans, models or tools operate on related knowledge, stale or conflicting updates to live state, authority relationships or generated routing must be detectable. Silent last-writer-wins corruption of project understanding is not acceptable.

## 6. Scale, economics and maintainability requirements

### KA-R30: bounded qualification budgets
**Strength:** QUALIFICATION MUST

Candidate qualification must use predeclared task-class-appropriate read/context/tool budgets for core reconstruction scenarios. Candidates may not obtain apparently superior recall merely by consuming an unbounded fraction of the repository. Budgets must be calibrated against useful current performance and scenario consequence.

### KA-R31: non-linear-history reconstruction cost
**Strength:** MUST

Required cold-start/reconstruction cost must not be structurally proportional to total accumulated project history. At 5x and 10x scale, historical growth must not force proportional growth in the mandatory orientation/context burden, although legitimate growth in currently active project complexity may change exact budgets.

### KA-R32: bounded mandatory active core
**Strength:** MUST

No mandatory bootstrap artifact/set or permanently active routing surface may be designed to accumulate all project history linearly. Historical growth must move behind progressive drill-down, task-shaped retrieval and recurring consolidation while remaining durably recoverable.

### KA-R33: dependency-local marginal maintenance
**Strength:** MUST

Adding or modifying ordinary project knowledge should require manual and generated maintenance proportional to the affected semantic/dependency neighborhood rather than the total project corpus or number of historical artifacts. Automated periodic global rebuild/qualification may still be legitimate.

### KA-R34: saturation and active-surface observability
**Strength:** MUST

The architecture must expose measurable signals for routing/view saturation and knowledge-maintenance pressure, including candidate-appropriate measures such as fan-out, ambiguity, stale derived state, retrieval/authority misses, active-context pressure, reconstruction cost and consolidation pressure, before degradation becomes catastrophic.

### KA-R35: human and model inspectability
**Strength:** MUST

Core authority, state and navigation semantics must remain inspectable by humans as well as machine-consumable. Internal generated indexes may use machine-oriented formats, but their authority class, source basis, transformation contract and relevant state must remain inspectable without dependence on one opaque service.

### KA-R36: provider and tool portability
**Strength:** MUST

Core continuity must not depend on proprietary hidden memory belonging to one model/provider/tool. Different capable collaborators must be able to reconstruct the project from project-controlled durable state through supported access mechanisms. Equal performance across all providers is not required.

## 7. Public/private requirements

### KA-R37: explicit public/private authority boundary
**Strength:** MUST / OWNER POLICY

The private companion may be authoritative only for explicitly delegated private continuity facts and may not silently redefine public ADS development state. Publicly resolved-private conclusions remain resolved when private access is temporarily unavailable; access then becomes not verified rather than invented contradiction.

### KA-R38: private-data non-leakage
**Strength:** MUST / OWNER POLICY

Generated public indexes, graph projections, summaries, search stores, context packets and receipts must not expose private paths, credentials, source locations or other private-only material outside its delegated boundary merely because private continuity participates in reconstruction.

### KA-R39: bounded private dependency
**Strength:** MUST / OWNER POLICY

If a task genuinely requires delegated private state, reconstruction must say so and verify relevant private continuity status when accessible. If it does not require private state, public reconstruction must remain usable without loading private details.

## 8. Qualification, observability and migration requirements

### KA-R40: structural and behavioral qualification
**Strength:** QUALIFICATION MUST

Candidate success must be tested both structurally and behaviorally. Structural tests include source/metadata/reference/freshness/generated-view consistency. Behavioral tests include orientation, governing-source activation, action-contract fidelity, risk activation, route reconstruction, uncertainty, context efficiency, consolidation fidelity and maintenance economics in realistic scenarios.

Structural validity alone is not evidence that the knowledge architecture works.

### KA-R41: multidimensional reconstruction qualification
**Strength:** QUALIFICATION MUST

Candidate evaluation must use explicit dimensions rather than one aggregate “seems informed” score. At minimum, relevant scenario classes must evaluate project/current-state orientation, route/parent objective, governing-source discovery and resolution, risk/open-obligation activation, supersession/conflict handling, action/task fidelity, uncertainty, important omission, context/read/tool cost and relevant active-surface/maintenance burden.

No single aggregate score is required or preferred.

### KA-R42: consequence-sensitive degraded mode
**Strength:** MUST

Failure of optional semantic/vector/graph/generated-view services must not create false confidence. The system must provide a safe fallback or explicit degraded state. Missing required authority for high-consequence work fails visibly; missing optional capability for low-risk exploratory work may degrade with calibrated uncertainty.

### KA-R43: migration preservation and identity reconciliation
**Strength:** MUST

Migration may change files, families, identifiers, schemas or storage mechanisms, but it must preserve the meaning, intended semantic identity continuity, authority, provenance, temporal/supersession meaning and discoverability of unique durable knowledge, or explicitly classify intentional retirement.

Rename, move, merge, split and representation-replacement semantics must be reconciled where they affect identity/authority. Silent semantic loss is unacceptable.

### KA-R44: old authority remains until successor qualification
**Strength:** MUST / TRANSITION INVARIANT

The current architecture remains authoritative during design and migration. The authority switch may occur only after the successor passes the frozen qualification scenarios, migration reconciliation and rollback/recovery criteria appropriate to the selected design.

### KA-R45: self-hosting evolution
**Strength:** MUST

The knowledge architecture must be capable of preserving and coordinating a major redesign of itself across conversations, interruptions and migration phases, including capture of redesign reasoning, authority transition and interruption recovery. If its own evolution cannot be reconstructed safely using its continuity model, it fails a core use case.

## 9. New evidence-derived requirements

### KA-R46: representation-independent continuity of identity
**Strength:** MUST

Where the project deliberately regards a subject, governed knowledge unit, workstream/activity, evidence object or other durable thing as continuous across a rename, path move, representation replacement or carrier change, the architecture must be able to preserve that continuity without assuming the human-readable label/path is the identity.

This does not require semantic IDs for every paragraph, file or relation. Identity granularity must be justified by persistence, cross-context reference, independent lifecycle, provenance or ambiguity-reduction value.

### KA-R47: multi-axis organization without truth duplication
**Strength:** MUST

The same durable knowledge must be able to participate in multiple relevant organizational views or contextual groupings, such as semantic subject, authority state, workstream, provenance, temporal state, artifact/evidence depth and reconstruction task, without copying unique project truth into independently maintained competing structures.

A deterministic preferred/default route may exist for ordinary continuation without becoming the object's only semantic parent.

### KA-R48: capture, consolidation and promotion boundary
**Strength:** MUST for semantic separation; SHOULD for low-friction capture ergonomics

The architecture must distinguish potentially valuable captured reasoning from consolidated candidate understanding and explicitly promoted durable authority when those roles differ.

Conversation-born insight must have a sufficiently low-friction intake path that important reasoning need not be lost merely because it does not yet fit a heavyweight canonical artifact. Captured/candidate material must not acquire authority automatically. Promotion of unique accepted understanding is explicit and source-traceable. Retention of unpromoted material is selective rather than an obligation to store every token or intermediate result forever.

### KA-R49: selective temporal and supersession semantics
**Strength:** CONDITIONAL MUST

Where authority, audit, historical reconstruction or correction depends on time, the architecture must be able to distinguish domain/applicability time, repository knowledge/recording time and authority-transition time as needed. It must also preserve materially different replacement, update/supplement, correction and former-validity semantics.

Universal bitemporal/tritemporal structure is not required for knowledge where these dimensions cannot diverge materially.

### KA-R50: recurring active-surface consolidation lifecycle
**Strength:** MUST capability

The architecture must provide a recurring mechanism for reducing active-routing/context pressure as knowledge accumulates while preserving durable history, provenance and drill-down. Consolidation should be triggered by measurable lifecycle/saturation pressure or explicit transition rather than arbitrary file-count aesthetics, and high-consequence consolidation must satisfy the relevant fidelity/view contract before detail becomes latent.

### KA-R51: control-miss and owner-reminder observability
**Strength:** MUST capability / QUALIFICATION MUST

Material control-behavior misses must be observable enough to become qualification and architecture-evolution evidence without depending solely on the project owner to notice, remember or preserve the failure. This includes, where materially applicable, activation misses, architecture-evolution trigger misses and cases where the owner must remind the system of a governing mechanism, deferred obligation, known risk/reopen trigger or required project process that should already have activated.

The requirement is for bounded, inspectable observability of material control failures, not exhaustive logging of every interaction, model intermediate or control decision. A detected miss is evidence only: it does not automatically change architecture, grant authority, or imply that every candidate miss is valid. Production/shadow qualification must demonstrate mechanical surfacing of representative misses without owner path naming or reminder while preserving low-consequence precision.

**Prospective amendment provenance:** accepted by the project owner at AO-9 P7-D02 on 2026-09-22 from the evidence reconciled in Research 227 and Research 228-234. Acceptance creates the requirement; it does not claim executable satisfaction. AO-10 must qualify the realization.

## 10. Frozen architecture invariants V0.2

```text
KA-I01  Durable project authority outranks transient chat/model memory.

KA-I02  The system has one explicit project-development authority; derived/convenience
        stores do not silently become competing truth.

KA-I03  Derived state contains no unique accepted project truth unless that truth is
        explicitly promoted through the authority boundary.

KA-I04  Current accepted, historically/formerly valid, superseded, rejected/known-wrong
        and unresolved knowledge remain distinguishable where material.

KA-I05  Consequential exact guidance/action requires applicable governing authority to be
        resolved and observably consumed and material action-contract constraints to be
        preserved, or the action fails according to consequence policy.

KA-I06  Unresolved governing-authority conflict or missing required evidence is surfaced
        rather than guessed or blended away.

KA-I07  Provenance and every must-preserve semantic property required by the target view
        survive synthesis, compression and migration; deeper evidence remains recoverable.

KA-I08  The old continuity system remains operational until the successor earns an explicit
        qualified authority switch.

KA-I09  Paused work expected to resume has explicit reason, return condition, parent
        relationship and resume target.

KA-I10  Public/private authority separation is preserved and private-only material is not
        leaked through public derived representations.

KA-I11  Fresh-collaborator continuation cannot depend on a previous conversation being
        available.

KA-I12  Required cold-start/reconstruction cost is not structurally proportional to
        accumulated project history, while legitimately increased active complexity may
        alter exact task budgets.

KA-I13  Routine local knowledge change does not require unbounded manual/global maintenance;
        cost normally follows the affected semantic/dependency neighborhood.

KA-I14  Optional probabilistic retrieval failure cannot silently bypass governing-authority
        safety or produce false reconstruction success.

KA-I15  From durable project state, the architecture can state its live route, authority,
        reconstruction and qualification status plus enough derived-view freshness/health
        to avoid false currentness.

KA-I16  Capture does not imply authority. Stored, summarized, indexed or repeatedly retrieved
        candidate knowledge becomes accepted authority only through explicit promotion.

KA-I17  When semantic continuity is intentionally declared, it is not forced to equal
        filename/path/carrier continuity.
```

## 11. Explicitly non-required mechanisms

This requirements boundary does not require:

```text
RDF / SKOS / OWL
a graph database
SQL / SQLite
event sourcing
semantic IDs for every sentence or claim
permanent storage of every conversation message
a vector database
GraphRAG / RAPTOR / one named retrieval architecture
one policy language / rule engine
universal bitemporal tables
every derived view to be persistently materialized
two-model review for every synthesis
a fixed number of lifecycle states
```

A candidate may still use any of these if it earns the associated complexity under the frozen requirements and qualification evidence.

## 12. Qualification and evidence discipline

The existing Research 124 stress-test family remains part of the candidate-evaluation program, subject to later fixture/threshold refinement that does not make scenarios easier for one candidate family.

Candidate comparison must also incorporate the D8 lifecycle-economics measures, including manual-touch fan-out, generated-view fan-out, incremental/full rebuild cost, validator footprint, semantic-review burden, active-surface/context size, reconstruction cost, authority-resolution cost, consolidation cost, stale-view repair latency and schema-migration impact where applicable.

The requirements boundary is intentionally broad enough that radically different successor architecture families remain eligible.

## 13. Authority transition note

Research 130 records the evidence reconciliation that produced this boundary. The project owner explicitly accepted the proposed calibration and additions in `chatgpt-23` on 2026-09-13.

From this freeze onward:

```text
PROJECT_KNOWLEDGE_ARCHITECTURE_REQUIREMENTS_V02.md
    = current frozen Research 124 candidate-acceptance requirements boundary

Research 124 original Phase-B KA-R01..KA-R45 / KA-I01..KA-I15
    = historical predecessor requirements boundary retained as provenance
```

The original V0.2 freeze did not authorize implementation or target selection. The later AO-9 P7-D02 amendment adds only KA-R51 prospectively; it does not itself authorize implementation, claim executable satisfaction, or change project authority.

```text
REQUIREMENTS_V02=FROZEN_BASELINE_WITH_PROSPECTIVE_AMENDMENT
REQUIREMENTS_COUNT=51
INVARIANTS_COUNT=17
AO9_P7_D02=ACCEPT_REQUIREMENT
KA_R51=ACCEPTED_NOT_EXECUTABLY_QUALIFIED
TARGET_ARCHITECTURE_ORIGINAL_FREEZE_STATE=NOT_SELECTED
CURRENT_SELECTED_SUCCESSOR=PKA-CANDIDATE-01
NEXT=AO9_P7_D03_OWNER_DECISION
```