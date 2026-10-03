# Research 478: integrated thin-centred hybrid successor candidate V0.2

**Date:** 2026-10-03
**Status:** AMENDED DEVELOPMENT CANDIDATE FROZEN / D1-D3 REQUIRED BEFORE OWNER DECISION / NO PRODUCTION SELECTION
**Parent:** Research 476-477
**Fixed evidence base:** 91d896b067181a0e59b031271c4dfca8c2eada42
**Candidate ID:** THIN_CENTRED_HYBRID_V02
**Scope:** Freeze the amended integrated Project semantic/control architecture after final Claude critique reconciliation.
**Authority:** Development candidate only. No production selection, Specification 028 replacement, migration, dependent-DRP resumption, or hidden-R2 exposure.

## 1. Architectural position

THIN_CENTRED_HYBRID_V02 is a small cross-domain semantic/control kernel plus bounded natural-owner contracts.

It contains:

    J1 governing acceptance
        human-governing source meaning
        owner-visible accepted effect statements
        typed accepted machine consequences
        exact accepted domain-contract references
        closed effect/accounting dispositions
        completion criteria where consequential
        governed lifecycle and requirement lineage

    non-authoritative control compilation
        ActionContract
        ControlObligationSet
        gate / transition / reconstruction inputs

    J2 natural-owner realization
        realizer declarations
        many-to-many component coverage
        source-owned artifact/procedure/migration facts

    J3 operational truth
        shared evidence/freshness predicates
        assurance decisions where required
        deterministic coverage/satisfaction
        activation / deferral / conflict facts

    generated orientation
        realization state + next gap + regression/enforcement views

    detective safety net
        semantic leak detection
        missing-accounting audit
        realization-gap audit
        policy/claim/integrity checks.

It is not a universal Project ontology, a universal ObligationUnit store, an authored global state database, or an inference engine that turns model confidence into authority.

## 2. One governing authority path

A governing acceptance binds one accepted meaning boundary:

    exact source/human carrier
    + owner-visible accepted effect statements
    + typed machine consequences
    + exact accepted domain-contract revisions
    + applicable completion/accounting/lifecycle metadata.

Only accepted J1 meaning is normative.

Generated control, J2 facts, J3 predicates and orientation are subordinate facts/projections.

A model may draft or critique the package.

It cannot make an unaccepted draft governing.

An accepted record must bind:

    exact package digest/revision shown to the owner
    exact owner decision payload
    accepted semantic payload
    drafter/reviewer provenance
    effective boundary / temporal authority.

The production authentication mechanism is intentionally open pending later realization qualification.

## 3. Accepted effect identity

Every accepted machine effect has:

    accepted_effect_id
    accepted_effect_statement
    typed consequence
    exact governing references
    semantic_digest.

The statement is the compact owner-visible canonical rendering of the effect.

The semantic digest covers the accepted statement, typed consequence and governing references, not incidental file formatting or location unless location itself is governing meaning.

For REQUIRE:

    one independently acceptable governing effect
        -> one stable requirement identity.

Evidence, qualification and activation facts are not separate requirement identities merely because they are separately checked.

SEQUENCE remains a separate accepted effect when ordering itself is normative.

## 4. Accepted machine-consequence grammar

The shared forms remain:

    REQUIRE
    PROHIBIT
    GATE
    AUTHORIZE
    DEFER
    LIFECYCLE
    SEQUENCE.

Detailed domain semantics remain in their natural owners.

The cross-domain form exists only where a machine-relevant governing consequence needs stable identity and exact control references.

## 5. Closed event/effect accounting

Every governing event must deterministically account for every accepted machine effect it creates or changes.

A governing event may instead declare:

    CREATES_NO_ACCEPTED_MACHINE_EFFECTS

when true.

Each accepted effect carries an accounting disposition appropriate to its kind.

For realization-requiring REQUIRE effects:

    REALIZATION_TRACKED
    NO_REALIZATION_REQUIRED.

NO_REALIZATION_REQUIRED uses a bounded accepted reason class, initially:

    SELF_EXECUTING_DISPOSITION
    STANDING_CONTROL_CONSEQUENCE
    PRINCIPLE_OR_HUMAN_ONLY_NO_MACHINE_REALIZATION
    REALIZED_AT_ACCEPTANCE.

No accepted effect may silently disappear merely because no consumer or realizer has yet been created.

The reason taxonomy is architecture-governed and extensible through prospective amendment.

## 6. Standing-consequence enforcement accounting

Realization tracking is not the only persistent-control concern.

For consequential:

    PROHIBIT
    GATE
    SEQUENCE

the accepted effect must bind either:

    exact enforcing control/predicate reference

or:

    DETECTIVE_ONLY

with explicit acknowledgement that no proactive enforcement exists.

An otherwise consequential unbound standing constraint derives review.

AUTHORIZE is handled differently because unused permission need not be actively enforced.

When consequential permission is exercised:

    the consuming action must bind the exact authorization decision/predicate
    and produce a governed execution receipt/fact.

A sibling generated enforcement view may expose:

    ENFORCED
    DETECTIVE_ONLY
    UNBOUND_REVIEW_REQUIRED.

## 7. Domain-contract revision binding

A governing reference to a domain contract is pinned to an exact accepted revision by default.

A later revision does not silently alter prior governing meaning or its done-definition.

Following a newer revision requires:

    governed re-binding
    OR
    a separately accepted bounded follow policy.

No generic follow-latest behavior exists by default.

If one actor/domain both owns a completion criterion and realizes the corresponding requirement, consequential satisfaction additionally requires an independent qualification/admission fact or a separately governed acceptance boundary sufficient to prevent self-certification.

## 8. Completion contract

A realization-tracked requirement that can be consequentially treated as complete binds an effective:

    completion_contract_ref.

The completion contract is owned by:

    GOVERNING_ACCEPTANCE
    OR
    exact ACCEPTED_DOMAIN_CONTRACT.

It defines:

    criterion identity
    requirement identity
    exact authority/reference/revision
    required completion components
    composition rule
    evidence requirement
    qualification requirement
    activation requirement.

Currently qualified composition:

    ALL_REQUIRED.

Other composition semantics require governed extension and separate qualification.

Completion components are acceptance-shaped outcomes/criteria.

They must not be invented merely to predict future implementation partition.

Artifact/path/module references remain valid when the governing requirement itself is explicitly artifact-specific.

## 9. J2 natural-owner realization

A realizer declaration is a bounded factual claim about implementation coverage.

It binds:

    realizer identity
    realizer owner
    exact artifact/procedure/migration reference
    exact relevant revision/digest
    requirement identity
    covered completion components.

The model is many-to-many.

One realizer may cover multiple requirements.

Multiple realizers may contribute to one requirement.

A realizer self-report such as FULL is advisory only.

It never changes the governing completion criterion or directly sets requirement satisfaction.

## 10. Shared evidence/freshness predicates and cross-plane stratification

Evidence validity and freshness must have one executable semantic source, not separate J3 and WARRANT-F implementations.

Candidate dependency order:

    current governing/lineage resolution
        -> natural-owner source facts
        -> shared evidence/freshness predicate library
        -> WARRANT-F decisions where assurance is required
        -> J3 requirement satisfaction
        -> generated orientation
        -> compiled/consuming control.

A WARRANT-F claim about a J3-derived fact binds an immutable J3 snapshot/revision.

That assurance result may not feed back into the same J3 derivation revision.

D-3 must prove the exact dependency graph acyclic before owner decision.

## 11. J3 coverage and satisfaction

For ALL_REQUIRED:

    valid_component_coverage
        = union(valid, current realizer component claims)
          restricted to accepted required components.

Duplicate claims add no coverage.

Unknown components, stale contract revisions or invalid authority route to review.

Then:

    coverage_complete
        = all required components covered under the current valid completion contract.

Coverage is not satisfaction.

For an active current requirement:

    requirement_satisfied
        = completion_contract_valid
          AND coverage_complete
          AND evidence_valid where required
          AND qualification_complete where required
          AND activation_effective where required
          AND NOT conflict_present.

Satisfaction is bound to exact current revisions/freshness.

Changes in artifact revision, evidence freshness, qualification, activation, completion contract or lineage trigger re-derivation.

Add:

    regressed

as a derived flag when a previously SATISFIED current requirement becomes unsatisfied.

conflict_present is generated from bounded unresolved conflicts such as:

    incompatible active accepted consequences
    inconsistent authoritative source facts
    invalid concurrent lineage/control decisions.

Component-level deferral is not supported in V0.2.

## 12. Requirement lineage

Historical accepted meaning is immutable.

Relation classes:

    CARRY_FORWARD
    REPLACE
    SPLIT
    MERGE
    REPARTITION
    RETIRE
    REINSTATE.

CARRY_FORWARD:

    preserves the same identity only under exact semantic continuity.

REPLACE:

    1 predecessor -> 1 distinct successor.

SPLIT:

    1 predecessor -> N successors.

MERGE:

    N predecessors -> 1 successor.

REPARTITION:

    N predecessors -> M successors using an explicit predecessor-to-successor mapping matrix and explicit retirement of any unmapped semantic remainder.

RETIRE:

    closes a predecessor with no successor under accepted authority/evidence.

REINSTATE:

    creates a new accepted identity linked to the retired predecessor; retirement history is not erased.

Successor effects may have per-target effective boundaries.

The semantic-succession graph remains acyclic.

Every scoped live predecessor is:

    mapped
    retired
    or explicitly unaffected.

No competing same-boundary outgoing succession records may silently choose precedence.

D-2 must qualify REPARTITION, per-target boundaries, REINSTATE and realization succession before owner decision.

## 13. Realization succession across lineage

No realization fact automatically carries across semantic change.

For:

    REPLACE
    SPLIT
    MERGE
    REPARTITION
    REINSTATE

successors start:

    OPEN

by default.

A governed realization-carry mapping may preserve/reuse predecessor realization only if:

    predecessor coverage is mapped to exact successor completion components
    relevant source revisions remain valid
    evidence remains fresh
    required qualification is re-evaluated
    the carry mapping is authority/effective-boundary bound.

For CARRY_FORWARD, compatible realization may continue because accepted meaning identity is unchanged, subject to ordinary revision/freshness validity.

Deferrals do not automatically carry across semantic succession unless explicitly reaccepted for the successor.

## 14. Generated realization orientation

For current active requirements, top-level generated states remain:

    REVIEW_REQUIRED
    DEFERRED
    OPEN
    SATISFIED.

next_gap values:

    REVIEW
    UNOWNED
    DEPENDENCY
    COVERAGE
    EVIDENCE
    QUALIFICATION
    ACTIVATION
    NONE.

Precedence:

    invalid source/conflict/invalid deferral
        -> REVIEW_REQUIRED / REVIEW

    valid governed deferral
        -> DEFERRED / NONE

    satisfied
        -> SATISFIED / NONE

    otherwise OPEN, with the first action-relevant unresolved gap.

UNOWNED means no responsible realizer/operational owner exists.

DEPENDENCY means an accepted SEQUENCE/prerequisite blocks progress.

REGRESSED is orthogonal and derived.

Reported/authored realization-state labels have no authority.

Governing lifecycle remains separate from realization orientation.

## 15. REVIEW_REQUIRED routing

Every review item derives a resolving owner class/reference from the predicate that created it.

Examples:

    governing owner
    domain-contract owner
    realization owner
    assurance owner
    integration/recovery owner.

Routing does not create normative authority.

It identifies who must resolve the underlying source-of-truth problem.

## 16. Non-authoritative control compilation

Accepted semantics and authoritative current facts may compile into disposable artifacts such as:

    ActionContract
    ControlObligationSet
    gate inputs
    transition requirements
    reconstruction requirements
    coverage/enforcement expectations.

Generated control:

    is versioned
    binds exact inputs
    is reproducible
    is invalidated by stale/conflicting inputs
    never becomes independent semantic authority.

## 17. Domain ownership and whole-system boundaries

AO remains owner of activation/orchestration and pre-dispatch control.

WARRANT-F remains owner of claims/evidence/warrant/admission.

Git/integration remains owner of repository/integration facts.

Continuity/recovery remains owner of reconstruction and recovery facts.

WMR-H/Project Knowledge preserves accepted history, rationale, authority transitions and temporal truth.

Delivery/realizers own implementation facts.

The semantic kernel references those contracts.

It does not duplicate their detailed policy.

Architecture evolution remains governed by AO-4 and owner normative decision authority.

## 18. Acceptance review and advisory model support

The default owner-facing acceptance review exposes:

    governing source meaning
    proposed accepted effect statements
    typed consequences
    accounting dispositions
    completion criteria/authority where relevant
    compact lineage change where relevant.

Schema/runtime internals remain drill-down.

Observed development burden:

    thin semantic review       LOW
    incremental hybrid review LOW

in the tested packages.

An independent second-model faithfulness check may be used as an advisory detective safeguard.

It:

    reports discrepancies beside the owner review
    has no authority
    is not required for acceptance validity
    does not prove owner-review efficacy.

Owner acceptance remains a normative responsibility boundary, not a claim of infallibility.

## 19. Detective safety net

Structured proactive control and detective controls coexist.

Candidate detective functions:

    recital/semantic leak detection
    missing-effect/accounting detection
    realization/enforcement gap detection
    policy/claim integrity checks
    repository integrity checks.

Detector output is advisory/review-triggering.

It never creates accepted governing meaning.

## 20. Legacy transition boundary

V0.2 does not claim completeness over unreconciled legacy knowledge.

Legacy IN_FORCE obligations:

    retain their current governing authority and existing control mechanisms.

Hybrid completeness/orientation applies only to:

    reconciled and activated hybrid identities.

Unreconciled legacy is surfaced explicitly as:

    LEGACY_UNRECONCILED

or equivalent transition scope.

Later governed reconciliation/migration determines successor mapping.

No legacy obligation is silently downgraded to DETECTIVE_ONLY merely because the hybrid exists.

## 21. Evidence classes

Current evidence must be described accurately.

Mechanism plausibility:

    C4-C8 probes
    SP-4 detector probe.

Development evidence:

    SP-2 three-case owner faithfulness
    C9 three-card owner burden
    corrected thin/rich CQ analyses.

Not yet present:

    end-to-end integrated execution evidence
    production-readiness evidence
    untouched confirmation evidence.

The same-author/isolated-fixture limitation of C4-C8 remains explicit.

## 22. Candidate invariants

    INV-01 unaccepted inference is never governing authority.
    INV-02 generated projections are never independent authority.
    INV-03 accepted effect identity binds owner-visible statement + typed consequence + exact refs.
    INV-04 one REQUIRE identity represents one independently acceptable governing effect.
    INV-05 every accepted machine effect receives explicit event/effect accounting.
    INV-06 consequential standing constraints cannot remain silently unenforced.
    INV-07 realizer coverage cannot define or weaken its own governing completion rule.
    INV-08 completion and satisfaction derive from accepted criteria plus current source facts.
    INV-09 shared evidence/freshness semantics have one executable source.
    INV-10 semantic change is prospective; historical accepted meaning is not rewritten.
    INV-11 every scoped predecessor is mapped, retired or explicitly unaffected.
    INV-12 semantic succession is acyclic and authority/effective-boundary bound.
    INV-13 realization does not automatically carry across semantic succession.
    INV-14 generated orientation cannot be overridden by reported state.
    INV-15 unresolved authority/semantic conflict routes to review.
    INV-16 domain-native semantics remain domain-owned unless a demonstrated cross-domain consequence requires a shared primitive.
    INV-17 hybrid completeness claims are scoped and never silently include unreconciled legacy.

## 23. Remaining pre-owner-decision work

V0.2 is not owner-decision-ready until:

    D-1 integrated real-event micro-replay passes or is reconciled;
    D-2 lineage extension probe passes or is reconciled;
    D-3 cross-plane dependency proof passes or is reconciled.

D-1 must use independently authored evaluator implementations from different models.

D-1 owner review is ordinary source-plus-proposal ACCEPT / AMEND / REJECT, not a hidden-error efficacy test.

## 24. Current disposition

    CANDIDATE=THIN_CENTRED_HYBRID_V02
    STATUS=AMENDED_DEVELOPMENT_CANDIDATE

    D1=REQUIRED
    D2=REQUIRED
    D3=REQUIRED

    OWNER_ARCHITECTURE_DECISION_READY=false
    PRODUCTION_TARGET_SELECTED=false

    SPECIFICATION_028_AUTHORITY=UNCHANGED
    PHYSICAL_MIGRATION_AUTHORIZED=false
    DEPENDENT_DRPS_RESUMED=false

    HIDDEN_R2_DETAILS=SEALED

    NEXT=FREEZE_D3_CROSS_PLANE_DEPENDENCY_PROOF
