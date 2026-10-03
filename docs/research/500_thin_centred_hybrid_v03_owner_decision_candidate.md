# Research 500: THIN_CENTRED_HYBRID_V03 owner-decision candidate freeze

**Date:** 2026-10-03
**Status:** FINAL PRE-OWNER-DECISION CANDIDATE FROZEN
**Parent:** Research 478, 481, 489, 499
**Candidate ID:** THIN_CENTRED_HYBRID_V03
**Fixed evidence base:** 179d1117d48f3fe8acaa6fc840f22afaf087a948
**Scope:** Freeze the integrated successor semantic/control architecture after completion and reconciliation of D-1, D-2 and D-3, so the project owner can make the architecture-selection decision from one bounded candidate.
**Authority:** Development architecture candidate only. No production activation, physical migration, Specification 028 supersession, dependent-DRP resumption, or hidden-R2 exposure occurs by this freeze.

## 1. Architectural position

THIN_CENTRED_HYBRID_V03 is the successor candidate for the Project's governing semantic/control layer.

It is not a universal Project schema.

It is a small cross-domain kernel connecting:

    J1 GOVERNING ACCEPTANCE
        accepted owner-visible meaning
        typed machine consequences
        closed effect/accounting decisions
        exact completion authority
        exact lifecycle/lineage decisions

    -> non-authoritative control compilation

    -> J2 NATURAL-OWNER REALIZATION
        exact artifacts/procedures/migrations
        realizer ownership
        component coverage
        evidence/qualification/activation facts

    -> shared executable predicates

    -> J3 OPERATIONAL TRUTH
        requirement satisfaction
        consequence/enforcement truth
        regression/conflict truth

    -> generated orientation
        realization state
        next gap
        review ownership
        enforcement/authorization views

    -> detective safety net.

Domain-native semantics stay in their natural owners unless a demonstrated cross-domain consequence requires a shared primitive.

## 2. Governing-authority rule

There is one normative authority path.

A governing acceptance binds:

    exact source/human carrier
    exact package shown to the owner
    exact owner decision payload
    accepted semantic/effect payload
    provenance
    effective boundary / temporal authority.

Only accepted J1 meaning is normative.

Generated control, J2 realization facts, J3 outputs, orientation, detectors and model proposals are not independent governing authority.

Unaccepted model inference never becomes authority.

## 3. Accepted effect identity and granularity

Every machine-relevant accepted effect has:

    accepted_effect_id
    accepted_effect_statement
    typed consequence
    exact governing references
    semantic digest / exact accepted semantic payload.

One REQUIRE identity represents one independently acceptable governing effect.

Requirement identity is not determined by implementation grouping.

Completion criteria are outcome/acceptance shaped rather than implementation shaped.

## 4. Accepted machine-consequence grammar

The bounded cross-domain consequence grammar remains:

    REQUIRE
    PROHIBIT
    GATE
    AUTHORIZE
    DEFER
    LIFECYCLE
    SEQUENCE.

This grammar expresses cross-domain control consequences.

It does not replace domain-native contracts.

## 5. Closed accounting

Every accepted governing machine effect receives explicit accounting.

At the governing-event level:

    either accepted machine effects are enumerated
    or the acceptance explicitly states that it creates no accepted machine effects.

At the effect level:

    REALIZATION_TRACKED
    or
    NO_REALIZATION_REQUIRED

with a closed governed reason such as:

    SELF_EXECUTING_DISPOSITION
    STANDING_CONTROL_CONSEQUENCE
    PRINCIPLE_OR_HUMAN_ONLY_NO_MACHINE_REALIZATION
    REALIZED_AT_ACCEPTANCE.

No accepted machine effect may disappear into an untracked third state.

## 6. Standing consequences and authorization

Consequential PROHIBIT / GATE / SEQUENCE effects must bind:

    an exact enforcing control/predicate
    or
    explicit DETECTIVE_ONLY handling.

DETECTIVE_ONLY means the architecture acknowledges that no proactive enforcement exists.

AUTHORIZE is handled as bounded permission:

    the consuming action binds the exact accepted authorization
    and produces a governed execution receipt/fact.

Generated enforcement/authorization views are derived, not governing.

## 7. Completion authority and anti-self-certification

A consequential realization-tracked REQUIRE binds an exact completion contract.

Completion authority is:

    GOVERNING_ACCEPTANCE
    or
    exact ACCEPTED_DOMAIN_CONTRACT revision.

Silent follow-latest is forbidden unless a separately accepted follow policy exists.

A completion contract binds:

    criterion identity
    requirement identity
    authority/revision
    required completion components
    composition rule
    evidence requirement
    qualification requirement
    activation requirement.

The baseline composition rule qualified to date is:

    ALL_REQUIRED.

A realizer may declare coverage facts.

A realizer may not define or weaken its own governing completion rule.

Where the same actor/domain owns both the criterion and realization, consequential satisfaction additionally requires an independent qualification/admission boundary sufficient to prevent self-certification.

## 8. J2 natural-owner realization

J2 records natural-owner realization facts such as:

    realizer identity
    realizer owner
    exact artifact/procedure/migration reference
    exact revision/digest
    requirement identity
    covered completion components
    evidence/qualification/activation source facts.

Coverage is many-to-many.

Coverage does not itself equal completion.

No birth-time implementation grouping is required at J1.

## 9. Shared predicates and cross-plane stratification

Evidence validity/freshness has one versioned executable semantic source shared by J3 and WARRANT-F where both consume it.

The same-revision dependency order qualified by D-3 is acyclic:

    accepted J1 meaning
        -> lineage resolution
        -> current active requirements

    natural-owner facts
        -> shared evidence/freshness predicates
        -> base assurance decisions where required

    active requirements
        + shared predicates
        + required assurance decisions
        -> J3 truth

    J3
        -> generated orientation
        -> compiled control / downstream assurance on frozen J3 snapshots.

A downstream assurance result about a J3 snapshot may not feed back into that same J3 revision.

Operational feedback enters through a later immutable revision/snapshot.

## 10. J3 satisfaction and regression

Requirement satisfaction is derived mechanically from:

    accepted completion criteria
    valid component coverage
    current source revisions
    evidence validity/freshness
    qualification
    activation where required
    lineage/currentness
    governed deferral/conflict rules.

No authored global realization state overrides J3.

Changes in source revision, evidence freshness, qualification, activation, completion contract or lineage trigger re-derivation.

Previously satisfied requirements may regress when their factual basis no longer holds.

## 11. Requirement lineage

The qualified lifecycle vocabulary is:

    CARRY_FORWARD
    REPLACE
    SPLIT
    MERGE
    REPARTITION
    RETIRE
    REINSTATE.

CARRY_FORWARD preserves identity only under exact semantic continuity.

REINSTATE creates a new accepted identity linked to the retired predecessor; retirement history is not erased.

REPARTITION supports true crossing:

    N predecessors -> M successors

using an explicit semantic-portion mapping matrix.

Every scoped predecessor portion is:

    mapped
    retired
    or explicitly unaffected.

No semantic remainder silently disappears.

## 12. Effective-boundary rule

Accepted effect identity is atomic for lifecycle currentness.

If one predecessor contributes semantic portions to multiple successors, those successor boundaries must be synchronized for that predecessor.

Independent predecessor identities may transition at different boundaries.

This prevents one accepted atomic effect from being simultaneously partly current and partly superseded.

## 13. Realization succession

Semantic succession and realization succession are distinct.

For:

    REPLACE
    SPLIT
    MERGE
    REPARTITION
    REINSTATE

the default successor realization initialization is:

    OPEN_RESET.

Prior realization does not automatically carry.

Explicit governed carry may export exact predecessor realization facts for successor revalidation only when:

    exact component mapping is valid
    authority/effective boundary is valid
    source revisions remain valid
    evidence remains fresh
    required qualification is re-evaluated.

Carry never directly asserts successor SATISFIED.

Deferrals do not automatically carry to semantic successors; exact successor reacceptance is required.

## 14. V03 initialization collection amendment

Research 499 reconciles the only D-1 implementation disagreement.

The canonical integrated interface is now:

    realization_initialization = ordered array of zero or more records

where each record contains exactly:

    effect_id
    mode.

Ordering:

    lexical by effect_id.

This collection form is required because the qualified lineage architecture permits SPLIT and crossing N:M REPARTITION with multiple successor initialization records.

A singleton transition therefore still emits a one-element array.

This is the only semantic/control-interface delta from V02 caused by D-1.

## 15. Generated orientation

The bounded generated realization orientation remains:

    REVIEW_REQUIRED
    DEFERRED
    OPEN
    SATISFIED.

Generated next-gap vocabulary remains:

    REVIEW
    UNOWNED
    DEPENDENCY
    COVERAGE
    EVIDENCE
    QUALIFICATION
    ACTIVATION
    NONE.

Orientation is a versioned derived projection.

It is not authored normative state.

Governing lifecycle and realization orientation remain separate concepts.

## 16. REVIEW_REQUIRED ownership

Every review-required condition maps to a resolving owner class/reference appropriate to its source, including:

    governing owner
    domain-contract owner
    realization owner
    assurance owner
    integration/recovery owner.

Review routing may not become a generic unresolved bucket with no responsible owner.

## 17. Non-authoritative compilation

Accepted J1 semantics may compile deterministically into operational artifacts such as:

    ActionContract
    ControlObligationSet
    gate inputs
    transition requirements
    reconstruction requirements
    coverage/enforcement expectations.

Compilation:

    is versioned
    binds exact inputs
    is reproducible
    invalidates on stale/conflicting inputs
    never becomes independent semantic authority.

## 18. Owner-facing review and model assistance

The default governing review shows source meaning beside proposed structured effects.

The owner may:

    ACCEPT
    AMEND
    REJECT.

The package exposes, as applicable:

    accepted effect statements
    typed consequences
    accounting dispositions
    completion authority/criteria
    compact lifecycle change.

Owner review burden was LOW in the qualified C9 cases.

Independent second-model review may be used as an advisory detective safeguard.

It does not become authority and is not required for acceptance validity.

## 19. Detective safety net

Structured proactive control and detective mechanisms coexist.

Candidate detective functions include:

    semantic/recital leak detection
    missing-effect/accounting detection
    realization/enforcement gap detection
    policy/claim integrity checks
    repository/integrity checks.

Detective findings route review.

They do not directly mutate governing meaning or current source facts.

## 20. Legacy transition boundary

V03 does not claim completeness over unreconciled legacy knowledge.

Legacy IN_FORCE obligations retain their existing authority/control until governed reconciliation.

Hybrid completeness/orientation applies only to reconciled and activated hybrid identities.

Unreconciled legacy is surfaced explicitly, including:

    LEGACY_UNRECONCILED.

No legacy obligation is silently downgraded to DETECTIVE_ONLY merely because the hybrid architecture exists.

## 21. Evidence closure

The pre-owner-decision evidence required by Research 477 is complete.

D-3:

    D3_DEPENDENCY_PROOF_PASSES

Evidence:

    same-revision dependency graph acyclic
    8 / 8 proof obligations
    5 / 5 controls.

D-2:

    D2_LINEAGE_EXTENSION_PLAUSIBLE

Evidence:

    independently authored ChatGPT and Claude evaluators
    14 / 14 material semantic agreement
    crossing REPARTITION
    staged independent boundaries
    REINSTATE
    realization carry/reset
    deferral rebinding
    CARRY_FORWARD continuity.

D-1:

    D1_AMEND

Evidence:

    one real governing act
    visible source + proposed J1 package
    owner ACCEPT
    actual natural-owner Git/Claude J2 facts
    shared predicates
    J3 satisfaction
    generated orientation
    standing prohibition handling
    bounded authorization exercise
    REPLACE + OPEN_RESET realization succession
    independently authored ChatGPT and Claude evaluators.

Raw D-1 exact comparison:

    13 / 14 material fields exact
    one container-cardinality mismatch only
    identical effect_id + OPEN_RESET semantic payload.

The raw result remains preserved as a mismatch.

The bounded interface amendment is incorporated prospectively in V03.

## 22. Candidate invariants

    INV-01  unaccepted inference is never governing authority.
    INV-02  generated projections are never independent authority.
    INV-03  accepted effect identity binds owner-visible meaning + typed consequence + exact refs.
    INV-04  one REQUIRE identity represents one independently acceptable governing effect.
    INV-05  every accepted machine effect receives explicit accounting.
    INV-06  consequential standing constraints cannot remain silently unenforced.
    INV-07  realizer coverage cannot define or weaken its own governing completion rule.
    INV-08  completion and satisfaction derive from accepted criteria plus current source facts.
    INV-09  shared evidence/freshness semantics have one executable source.
    INV-10  semantic change is prospective; historical accepted meaning is not rewritten.
    INV-11  every scoped predecessor semantic portion is mapped, retired or explicitly unaffected.
    INV-12  semantic succession is acyclic and authority/effective-boundary bound.
    INV-13  realization does not automatically carry across semantic succession.
    INV-14  generated orientation cannot be overridden by reported state.
    INV-15  unresolved authority/semantic conflict routes to an identified review owner.
    INV-16  domain-native semantics remain domain-owned unless a demonstrated cross-domain consequence needs a shared primitive.
    INV-17  hybrid completeness claims never silently include unreconciled legacy.
    INV-18  realization initialization is a deterministic ordered 0..N collection compatible with multi-successor lineage.

## 23. What is intentionally not selected here

V03 does not select:

    a universal Project type system
    birth-time realization grouping
    authored authoritative global state
    later unaccepted semantic inference as authority
    one universal database/ledger/event-sourcing topology
    physical file/folder layout
    exact storage technology
    exact cryptographic acceptance mechanism
    exact UI
    production deployment topology.

Those remain separate implementation/physical-architecture decisions.

## 24. Evidence limits

V03 is supported as a development architecture candidate.

The evidence does not yet establish:

    production implementation correctness
    large-scale migration correctness
    untouched confirmation
    long-run maintenance economics at production scale
    performance/scalability of a concrete implementation.

Those belong to later governed stages.

## 25. Owner-decision readiness

Research 478 required D-1, D-2 and D-3 to pass or be reconciled before owner architecture decision.

That condition is now met:

    D1 = D1_AMEND, reconciled into V03
    D2 = D2_LINEAGE_EXTENSION_PLAUSIBLE
    D3 = D3_DEPENDENCY_PROOF_PASSES.

No unresolved pre-owner-decision discriminator remains from Research 477.

Therefore:

    OWNER_ARCHITECTURE_DECISION_READY=true.

This does not mean:

    production is selected
    migration is authorized
    Specification 028 is superseded
    dependent DRPs are resumed.

## 26. Current disposition

    CANDIDATE=THIN_CENTRED_HYBRID_V03
    STATUS=FINAL_PRE_OWNER_DECISION_CANDIDATE

    D1=D1_AMEND_RECONCILED
    D2=D2_LINEAGE_EXTENSION_PLAUSIBLE
    D3=D3_DEPENDENCY_PROOF_PASSES

    OWNER_ARCHITECTURE_DECISION_READY=true
    PRODUCTION_TARGET_SELECTED=false

    SPECIFICATION_028_AUTHORITY=UNCHANGED
    PHYSICAL_MIGRATION_AUTHORIZED=false
    DEPENDENT_DRPS_RESUMED=false
    HIDDEN_R2_DETAILS=SEALED

    NEXT=FREEZE_OWNER_ARCHITECTURE_DECISION_PACKAGE
