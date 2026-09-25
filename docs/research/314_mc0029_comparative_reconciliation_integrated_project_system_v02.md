# Research 314: MC-0029 Comparative Reconciliation and Integrated Project-System Architecture Candidate V0.2

**Date:** 2026-09-25
**Status:** COMPARATIVE RECONCILIATION FROZEN / RESEARCH 312 AMENDED / KEYSTONE AMENDED / CLAUDE COMPARATIVE CRITIQUE REQUIRED / OWNER DECISION NOT READY / NO PRODUCTION IMPLEMENTATION
**Parent program:** Research 219 and Research 240
**Compared candidates:** Research 312 and MC-0029 Message 001 / KEYSTONE
**Accepted architecture base:** Research 256, 259, 272, 276, 309, 310, 311
**Scope:** Reconcile the two independent Specification 028 / AO-10 designs into one whole-system candidate without granting preservation rights to existing semantic or physical mechanisms.
**Authority:** Research candidate only. Specification 028 remains current transition authority. No production implementation, shadow activation, physical migration, oracle retirement, provider selection or authority switch is authorized.

## 1. Comparative disposition

The independent designs converge on the main boundary:

    Specification 028 -> prospective supersession, not mixed-era amendment
    JW1 -> project/system
    Project Engineering -> independently resolved project/engineering
    AO and WARRANT-F -> distinct systems joined by explicit contracts
    WMR-H -> retained representation architecture
    KA-R51 -> mechanically observable control misses
    KA-R52 -> deterministic accepted-obligation realization traceability
    current mechanisms -> migration oracles until qualified successor release
    semantic qualification -> before physical migration
    SHADOW -> before ACTIVE_SUBORDINATE
    authority switch -> explicit owner decision after qualification
    provider/workflow mechanisms -> adapters, not semantic authority

No R5-R8C reopen is indicated.

    RESEARCH312=AMEND
    KEYSTONE=AMEND
    SPECIFICATION028_WHOLE_DISPOSITION=SUPERSEDE_CANDIDATE_RETAINED
    OWNER_DECISION=NOT_READY

The reconciled candidate is an integrated Project system with a minimal shared semantic substrate, bounded domain models, obligation units, a hosting-neutral AO protocol, bounded generated live orientation and semantic-shadow-before-physical-migration discipline.

## 2. Verified evidence

Claude Message 001 is frozen at:

    74023a779998200a6317df07dc7cd4979ff84e47

Its MC-0029 independence boundary is preserved.

Repeated checks establish:

    Specification 028 uppercase MUST occurrences at frozen base = 104
    lines containing uppercase MUST at frozen base = 94

Specification 028 section 3 names reconstruction.py, migration.py, validation.py and git.py responsibilities. The current tools/project_knowledge package has no modules with those names. This supports KA-R52's accepted-but-unrealized problem, while successor traceability must track semantic responsibility rather than filename existence.

At the current coordination head, CURRENT_STATE.md is 436,264 bytes. Size itself is not an architectural rule, but continuing growth supports replacing append-only live narrative with bounded generated orientation plus source-owned history.

## 3. Research 312 retained strengths

Retain from Research 312:

    whole-Specification reconciliation before implementation
    JW1 / Engineering separation
    AssuranceRequest / AssuranceDecisionEnvelope seam
    integrated AO control cycle
    WMR-H mapping
    ControlExpectation / ControlTrace / ControlObservation
    natural-owner KA-R52 direction without a universal ledger
    AO-6 lifecycle revalidation rather than blind ROTATE
    explicit migration-oracle retirement discipline
    provider/workflow neutrality
    staged shadow -> bridge -> migration -> owner cutover

## 4. KEYSTONE amendments incorporated

### 4.1 Minimal shared semantic substrate

KEYSTONE correctly identifies duplicated cross-system semantics. Identity, lifecycle, scope/time, provenance binding, governed relations and obligation references should not be independently reinvented by knowledge, AO, assurance and migration.

Research 312 did not make this integration explicit.

Candidate:

    MINIMAL_SHARED_SEMANTIC_SUBSTRATE=REQUIRED

Do not collapse AO, WARRANT-F, workstreams, collaboration and migration/evolution into one universal object model. They retain genuine domain semantics.

Target shape:

    minimal shared semantic substrate
        +
    bounded domain models composing with it

Shared meaning is centralized only where it is genuinely the same.

### 4.2 Information role and governing lifecycle status

KEYSTONE's authority_class critique is materially correct. The current values mix information role with governing lifecycle.

Candidate axes:

    INFORMATION_ROLE
        GOVERNING
        EVIDENCE
        CONTROL
        DERIVED
        CAPTURE

    GOVERNING_STATUS
        PROPOSED
        IN_FORCE
        HELD
        SUPERSEDED
        RETIRED
        REJECTED

GOVERNING_STATUS applies only where a governing lifecycle exists.

This is an AO-4 AMEND candidate, not CLARIFY. Exact enums remain falsifiable under P1.

WARRANT-F accepted-state semantics remain a separate semantic exact-subject transition role.

### 4.3 Governed relations

KEYSTONE's governing / support / realization / dependency / trigger families are a strong candidate, but their exact closed vocabulary is not selected before testing.

V0.2 requires:

    finite governed relation types
    no arbitrary free-text relation type
    natural-owner edge declaration
    derived reverse/closure projections
    governed extension

P1 tests whether relation semantics belong in the shared substrate or bounded domain models.

### 4.4 Obligation units

Research 312's ObligationRealization was underspecified in granularity.

Leading KA-R52 abstraction:

    ObligationUnit =
        smallest group of accepted normative obligations sharing
        one realization boundary and one evidence path

This is semantic, not one record per document and not one record per literal MUST token. Accepted decisions, policies and procedures can create obligations without the token MUST.

Candidate states:

    UNLINKED | LINKED | EVIDENCED | QUALIFIED | OPERATIONAL | DEFERRED

UNLINKED is an observable failure after the enforcement boundary, not a legitimate terminal third state. Exact metadata placement, unit boundaries and state vocabulary remain under P3.

### 4.5 AO protocol and hosting neutrality

KEYSTONE's begin / preflight / postflight decomposition is useful.

Candidate principle:

    AO has a deterministic core protocol and versioned result contract
    correctness and recovery do not require an always-on daemon
    any qualified executor may host the protocol
    an optional service/daemon adapter remains possible if future evidence warrants it

Logical operations:

    begin
        event -> baseline -> obligation screen -> reconstruction need -> route

    preflight
        authority -> ActionContract -> ActionShape -> assurance requirement

    postflight
        result -> receipts -> observations -> continuation
        -> preservation/promotion -> evolution feedback

Exact CLI names remain realization details.

### 4.6 Typed ActionShape

Provider-specific tool/API events should be normalized by adapters into provider-neutral ActionShape records and classified deterministically where possible.

Only genuinely unstructured prose should require model-assisted action-shape recognition. Model assistance may propose a classification but cannot grant authority.

P5 measures deterministic coverage.

### 4.7 Live-surface successors

Leading direction:

    current_routing.json
        current oracle
        -> typed control state + compatibility projection

    CURRENT_STATE.md
        current human-readable state authority
        -> bounded generated orientation + source-owned history

    KNOWLEDGE_MAP.md
        current navigation oracle
        -> generated navigation after semantic-navigation qualification

    REVIEW_INBOX.md
        current convenience index
        -> generated collaboration projection

    CONTINUITY.md
        small human-readable governing bootstrap/recovery procedure

    checkpoints
        current durable boundary evidence
        -> future family/status remains open; no preservation right

No current surface retires merely because a target successor is described.

### 4.8 Semantic shadow before physical migration

Do not combine semantic-authority change and physical carrier migration in one transition unit when they can be separated.

Run the semantic successor in SHADOW against the current layout and current oracles first. Physical migration follows only after semantic parity/falsification pressure is understood.

## 5. Successor contract strata

Research 312's one integrated successor role mixes lifetimes. KEYSTONE's three-way separation is stronger, but exact document count and numbering should remain open.

Research 309 also defers general framework extraction, so no contract is currently owned by an already-extracted PSMF/framework project.

Required semantic strata:

    C1 STABLE SEMANTIC CONTRACT
       shared semantic/control invariants:
       identity, role/status, authority-resolution, relations,
       obligations, reconstruction/capture basics

    C2 ADS REALIZATION CONTRACT
       ADS JW1/Engineering realization, WMR-H bindings,
       AO interfaces, control state, generated views,
       assurance interface and provider-neutral adapters

    C3 TRANSITION / CUTOVER CONTRACT
       migration, compatibility projections, oracle retirement,
       rollback, bridge qualification, cutover and authority switch

These may become three specifications or another equally clear physical arrangement. The requirement is lifetime/authority separation, not a fixed file count.

## 6. Semantic organization and Research 217

KEYSTONE proposes:

    logical ownership/responsibility position
        +
    relations
        +
    selective cross-cutting concerns
        +
    search/navigation

This is a strong candidate, not an accepted target.

POSITION means logical semantic ownership/responsibility position, not current filesystem path. Path remains non-authoritative.

The owner's clarification removed preservation rights from the Research 217 vocabulary and from the Research 217 pattern itself. Therefore source-owned membership, polyhierarchy, preferred routes and calibration are evidence, not automatic target rules.

    RESEARCH217_TARGET_PRESERVATION_RIGHT=false
    EXACT_18_SUBJECT_VOCABULARY=NOT_FINAL
    SUBJECT_PATTERN=NOT_FINAL
    LEADING_SUCCESSOR_CANDIDATE=LOGICAL_POSITION_RELATIONS_CONCERNS_SEARCH
    FINAL_DISPOSITION=PENDING_P2

P2 must compare multiple viable architectures against Research 217's historical bar plus new cold-start, cross-plane, AO-activation and impact-analysis tasks. Research 217 must remain eligible to win on merit.

## 7. Integrated system boundary

    durable Project knowledge
        owns human-governed meaning

    minimal shared semantic substrate
        owns common identity/lifecycle/scope/relation/provenance primitives

    bounded domain models
        AO control
        workstreams
        collaboration
        assurance
        migration/evolution

    JW1
        reconstruction
        activation/orchestration
        authority/action-contract resolution
        continuity/recovery
        evolution routing
        workstream/Git policy
        obligation realization state
        generated orientation/navigation
        bridge/transition control

    Project Engineering
        WARRANT-F kernel
        verifier execution
        repository engineering
        host/provider adapters
        Git mechanics
        delivery/release
        migration execution
        evidence publication
        recovery qualification

    Product
        independently resolved
        no Project runtime dependency

Integration must not become a universal Project database, graph, event log or god object model.

## 8. KA-R51 V0.2

Retain:

    ControlExpectation
    ControlTrace
    ControlObservation

Candidate detector producers:

    D1 owner-reminder / prior-applicability
    D2 late activation
    D3 downstream catch
    D4 trigger-replay audit

D4 is a maintenance operation, not a daemon requirement.

Owner reminders are evidence, not automatic defect labels.

Each detector requires exact prior-cycle binding where applicable, sensitivity witnesses, specificity witnesses, consequence-aware persistence and bounded false-positive burden.

## 9. KA-R52 V0.2

    Governing source
        -> ObligationUnit(s)

    ObligationUnit
        stable identity
        source/revision/section anchors
        responsible semantic owner
        realization boundary
        expected evidence path
        activation/effective boundary

    realization
        implementation + claim
        procedure + evidence expectation
        owner decision
        AO activation/control rule
        migration/cutover action
        other explicitly typed realization

    OR governed deferral
        reason
        dependency/blocker
        reactivation condition
        future evidence path
        owner/decision reference

A derived coverage view is permitted; unique accepted truth remains at natural owners.

WARRANT-F may enforce the invariant that every in-scope active obligation has a valid realization path or governed deferral. The enforcement rule itself requires warrant sensitivity/specificity and effective-boundary semantics.

## 10. AO / WARRANT-F / Engineering seam

Research 312's interface remains.

AO request:

    exact subject/revision
    intended consequence
    applicable profile
    activated claims
    capability/trust requirements
    ActionContract/cycle reference

WARRANT-F result:

    exact subject
    effective policy
    evaluated claims
    warrant/evidence refs
    freshness/provenance/trust
    ADMIT | REFUSE | REVIEW_REQUIRED
    unresolved conditions

The shared substrate provides common identifiers and lifecycle/provenance primitives. It does not make AO an assurance subsystem or WARRANT-F an orchestration subsystem.

## 11. Bridge, recovery and authority

Leading order:

    design/contract acceptance
    -> semantic substrate + obligation trace realization
    -> AO SHADOW on current layout
    -> generated control/projection SHADOW
    -> assurance/admission shadow
    -> bridge SHADOW qualification
    -> explicit owner enable of ACTIVE_SUBORDINATE
    -> physical migration
    -> cutover/recovery qualification
    -> explicit owner authority switch

ACTIVE_SUBORDINATE may fail-safe to SUSPENDED under deterministic accepted policy. It may not self-enable or self-promote.

Break-glass remains derivative-independent.

Rollback capability is required. KEYSTONE's exact reverse-projection scope is not frozen; later evidence may justify reverse projection, immutable snapshot restoration or another qualified mechanism.

## 12. Comparative probe program

Decision-relevant before owner architecture disposition:

    P1 SHARED SEMANTIC SUFFICIENCY
       test role/status, relation placement and anti-over-unification
       on real carriers; include negative controls

    P2 SEMANTIC NAVIGATION ARCHITECTURES
       compare Research 217 against:
       A logical position + relations + search
       B logical position + relations + selective concerns + search
       plus another requirements-derived arm if warranted
       using old and new whole-system tasks; blind where practical

    P3 OBLIGATION UNIT GRANULARITY
       delimit units across Spec 028, AO-9 P7 and WARRANT-F;
       independent second delimiter; measure agreement and effort;
       surface known gaps without false gaps

    P4 KA-R51 DETECTOR PRECISION
       historical positive witnesses + ordinary-session negative controls

    P5 ACTIONSHAPE COVERAGE
       measure consequential actions covered by typed provider-neutral
       classification versus prose/model-assisted path

    P6 BOUNDED ORIENTATION
       fresh-collaborator continuation using target orientation/control
       versus current path; measure parity, read/tool cost and size

    P7 SPEC 028 LINEAGE + CONTRACT PARTITION
       audit all 46 sections and all 104 uppercase MUST occurrences
       across 94 lines; every normative obligation gets a successor,
       retirement or historical disposition; test C1/C2/C3 coupling

Realization-stage after architecture disposition:

    P8 bridge SHADOW replay
    CLI/result determinism
    control-record concurrency
    projection equality
    oracle sensitivity/specificity
    rollback/recovery drills
    provider/host P-H successor qualification

This prevents implementation-dependent bridge work from becoming a prerequisite for deciding the semantic architecture.

## 13. Corrections to KEYSTONE

    one universal kernel
        -> minimal shared substrate + bounded domain models

    ROLE includes PROPOSAL
        -> candidate uses CAPTURE role and GOVERNING + PROPOSED status

    exact five-family relation set
        -> governed finite registry; exact set pending P1

    Research 217 vocabulary SUPERSEDE now
        -> no preservation right; final disposition pending P2

    Research 217 rules RETAIN now
        -> evidence/baseline only; no automatic target preservation

    SC-1 framework-owned now
        -> reusable-core candidate only; extraction remains deferred

    AO is not a daemon
        -> AO correctness must not require a daemon; optional hosting remains open

    authority_class split is CLARIFY
        -> AO-4 AMEND candidate

    Research 217 change is CLARIFY
        -> if selected, prospective semantic AMEND/SUPERSEDE

    exact reverse projection rollback
        -> rollback capability required; exact mechanism open

## 14. Corrections to Research 312

Research 312 gains:

    first-principles semantic architecture as AO-10 dependency
    minimal shared semantic substrate
    role/status separation candidate
    governed relation registry
    semantic-navigation qualification
    obligation-unit granularity
    concrete KA-R51 detectors
    begin/preflight/postflight AO shape
    typed ActionShape
    bounded generated CURRENT_STATE successor
    generated REVIEW_INBOX successor
    semantic-shadow-before-physical-migration invariant
    three contract strata
    decision-relevant architecture probes before owner acceptance

Research 312's V0.1 section matrix remains evidence, not final V0.2 lineage. P7 must reconcile it with KEYSTONE's independent 46-section lineage.

## 15. Current boundary

    MC0029_MESSAGE001=COMPLETE
    MC0029_MESSAGE002=COMPARATIVE_RECONCILIATION
    RESEARCH312=AMEND
    KEYSTONE=AMEND

    INTEGRATED_PROJECT_SYSTEM_V02=FROZEN_COMPARATIVE_CANDIDATE
    MINIMAL_SHARED_SEMANTIC_SUBSTRATE=REQUIRED_CANDIDATE
    UNIVERSAL_GOD_KERNEL=REJECTED_IN_V02_CANDIDATE
    ROLE_STATUS_SPLIT=AO4_AMEND_CANDIDATE
    RELATION_REGISTRY_EXACT_SET=PENDING_P1

    RESEARCH217_PRESERVATION_RIGHT=false
    RESEARCH217_FINAL_TARGET_DISPOSITION=PENDING_P2
    LEADING_NAVIGATION_CANDIDATE=LOGICAL_POSITION_RELATIONS_CONCERNS_SEARCH

    OBLIGATION_UNITS=LEADING_KAR52_CANDIDATE
    AO_PROTOCOL=DETERMINISTIC_CORE_HOSTING_NEUTRAL
    TYPED_ACTION_SHAPE=LEADING_P7D01_REALIZATION

    SPECIFICATION028_WHOLE_DISPOSITION_CANDIDATE=SUPERSEDE
    SUCCESSOR_CONTRACT_STRATA=C1_SEMANTIC_C2_ADS_REALIZATION_C3_TRANSITION
    SUCCESSOR_PHYSICAL_DOCUMENT_COUNT=NOT_SELECTED

    DECISION_PROBES=P1_TO_P7_REQUIRED
    REALIZATION_PROBES=P8_PLUS_DOWNSTREAM

    CLAUDE_COMPARATIVE_CRITIQUE=REQUIRED
    OWNER_DECISION=NOT_READY

    AO10_PRODUCTION_IMPLEMENTATION_AUTHORIZED=false
    AO10_SHADOW_ACTIVATION_AUTHORIZED=false
    PHYSICAL_MIGRATION_AUTHORIZED=false
    CURRENT_ORACLE_RETIREMENT_AUTHORIZED=false
    AUTHORITY_SWITCH_ALLOWED=false

    NEXT=MC0029_CLAUDE_COMPARATIVE_CRITIQUE
