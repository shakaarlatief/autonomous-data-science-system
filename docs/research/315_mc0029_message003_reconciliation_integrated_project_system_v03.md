# Research 315: MC-0029 Message 003 Reconciliation and Integrated Project-System Candidate V0.3

**Date:** 2026-09-25
**Status:** MESSAGE 003 RECONCILED / RESEARCH 314 AMENDED / INTEGRATED PROJECT-SYSTEM V0.3 FROZEN / DECISION-PROBE PREREGISTRATION NEXT / OWNER DECISION NOT READY / NO PRODUCTION IMPLEMENTATION
**Parent:** Research 314 / MC-0029 Message 003
**Accepted architecture base:** R5-R8C including Research 258 AM-7, Research 272 WMR-H V0.3, Research 276 WARRANT-F V0.2, Research 311 owner acceptance
**Scope:** Reconcile Claude's eleven amendments, probe revisions and falsifiers into the strongest pre-decision AO-10 / Specification 028 successor candidate while preserving temporal authority, owner authority, provider/workflow freedom and the owner's no-preservation-right doctrine.
**Authority:** Research candidate only. Specification 028 remains current transition authority. This record does not accept the V0.3 target, authorize AO-10 production implementation, authorize shadow activation, authorize current-surface compaction, authorize physical migration, retire current oracles, select providers/workflows, or switch authority.

## 1. Reconciliation result

Claude Message 003 returns AMEND on Research 314 and identifies eleven material changes.

The overall result is:

    RESEARCH314=AMEND
    MESSAGE003_AMENDMENTS=ACCEPTED_WITH_REFINEMENTS
    UPSTREAM_R5_TO_R8C=NO_REOPEN
    SPECIFICATION028_WHOLE_DISPOSITION=SUPERSEDE_CANDIDATE_RETAINED
    INTEGRATED_PROJECT_SYSTEM_V03=FROZEN_PRE_DECISION_CANDIDATE
    OWNER_DECISION=NOT_READY

No disagreement requires another comparative design round before empirical work.

The eleven amendments are dispositioned as follows:

    AMEND-1   ACCEPT
    AMEND-2   ACCEPT_WITH_GRANULARITY_REFINEMENT
    AMEND-3   ACCEPT_AS_P2_ARM_REALIZATION_NOT_TARGET_SELECTION
    AMEND-4   ACCEPT_WITH_TEMPORAL_AUTHORITY_REFINEMENT
    AMEND-5   ACCEPT_AND_STRENGTHEN_TO_FULLY_DERIVED_STATE
    AMEND-6   ACCEPT
    AMEND-7   ACCEPT_WITH_PROFILE_AUTHORITY_REFINEMENT
    AMEND-8   ACCEPT
    AMEND-9   ACCEPT
    AMEND-10  ACCEPT_WITH_PROJECT_FACT_SCOPE
    AMEND-11  ACCEPT_AS_SEPARATE_AO4_CASE_CANDIDATE_NO_EXECUTION

Research 314 remains valuable comparative evidence but is superseded as the current candidate by this V0.3 reconciliation.

## 2. Evidence checks relevant to Message 003

The following claims were independently rechecked at repository head / accepted sources:

    Research 311 uppercase MUST occurrences = 0

    Research 276 section 21 explicitly adopts WF-A31 and WF-A32.
    Profiles are invocation shorthands and do not own:
        consequence
        thresholds
        freshness
        trust requirements

    Research 258 AM-7 explicitly accepts permanent transition management.
    Reusable mechanism includes:
        compatibility/shadow transitions
        transition validation
        cutover/rollback mechanism
        transition receipts/evidence
        authority-preserving successor bridges
        repeated architecture-successor transitions

    one-time R8 migration plans / manifests / execution state /
    temporary scaffolds remain instance-specific transition material

These checks materially support AMEND-7 and AMEND-8.

## 3. AMEND-1: substrate admission becomes executable

Research 314's statement that common meaning enters the shared substrate only when "genuinely the same" is too subjective.

V0.3 adopts a declared seam inventory.

A candidate primitive may enter the minimal shared semantic substrate only when it is required for semantic agreement across consequential bounded-domain seams and its shared ownership avoids independent reinterpretation of the same contract.

Leading admission rule for DRP-01:

    each shared primitive cites the domain seams that require it
    target evidence should show use at two or more meaningful domain seams
    no primitive enters merely for convenience or generic reuse
    domain-internal concepts remain in their natural domain model
    a primitive with no justified seam citation is removed or demoted

Candidate examples:

    likely shared
        semantic identity
        exact subject/revision binding
        governing lifecycle reference
        provenance descriptor
        obligation reference

    likely domain-owned
        workstream states
        bridge-mode implementation state
        claim/warrant internals
        stochastic campaign statistics

The exact admission threshold is decision-relevant and remains falsifiable in DRP-01. The architecture requirement is the existence of a governed, testable admission rule and seam inventory, not uncontrolled semantic centralization.

## 4. AMEND-2: role is unit-scoped, not carrier-assumed

Real ADS carriers are frequently semantically mixed.

V0.3 therefore changes the candidate from per-carrier role assignment to semantic-unit role assignment.

A homogeneous carrier may itself be the semantic unit.

A mixed carrier may contain units such as:

    DecisionUnit
    ObligationUnit
    EvidenceUnit
    ControlUnit

Role/status semantics attach at the smallest stable unit required by consequential use.

Carrier-level "primary role" may exist only as a convenience projection when it is unambiguous. It is not unique accepted truth when contained units differ.

V0.3 does not yet freeze whether role is always single-valued at the atomic unit or may be a bounded set for irreducibly multi-function units. DRP-01 must measure the real mixed-role rate and test whether further decomposition remains practical.

The temporary governing-status concept remains required, but neither the token HELD nor SUSPENDED is accepted as the final machine label because both collide conceptually with existing hold/suspension semantics. DRP-01 will settle the exact vocabulary.

## 5. AMEND-3: logical position is a P2 arm, not a selected target

Claude's governed path-to-responsibility mapping is a useful way to operationalize the position-based navigation candidate.

It is not accepted as the target before DRP-02.

For the position arm:

    accepted target responsibility areas
        -> governed instance mapping
        -> default logical responsibility position

    per-carrier override
        only where primary responsibility genuinely diverges from default placement

The mapping is instance policy.

Path is an input to a default mapping, not semantic authority.

Therefore:

    path != identity
    path != authority
    physical parent != exclusive semantic parent
    logical position != current filesystem location

Because the current layout predates the R7/R8 target, DRP-02 must freeze a bounded responsibility mapping for its corpus before scoring any navigation arm. The mapping cannot be tuned after observing comparative results.

## 6. AMEND-4: obligations are born at acceptance without invalidating owner decisions

Claude correctly identifies the upstream blind spot: an obligation cannot be checked for realization if nobody ever delimits it.

V0.3 therefore requires every governed acceptance event to produce an ObligationDeclarationSet:

    zero or more ObligationUnits
    OR
    explicit CREATES_NO_OBLIGATION_UNITS

This applies to:

    owner decisions
    AO-4 dispositions
    specification acceptance
    assurance/policy acceptance
    other accepted governing changes

However, one refinement is necessary for temporal authority.

A valid owner normative decision does not become historically invalid merely because Project-system bookkeeping failed.

Therefore:

    normative acceptance time
        remains the time of the valid authority event

    acceptance postflight
        must emit / validate the obligation declaration set

    missing declaration set
        is a control/realization defect
        may cause affected-scope hold for dependent downstream action
        must be surfaced through KA-R51 / KA-R52
        does not erase or rewrite the owner decision

For a MEDIATED acceptance path, the system can require obligation-declaration completion before admitting dependent operational advancement.

For a COOPERATIVE or UNMEDIATED authority event, postflight reconciliation must recover the declaration immediately and record the miss if it did not occur.

The system should draft/delimit units mechanically or model-assistively where safe; the owner should only need to resolve materially ambiguous normative meaning, not manually maintain bookkeeping.

A secondary normative-language sensitivity scan remains useful for accepted governing carriers. It raises REVIEW on uncovered normative language but is not the ontology and cannot replace acceptance-event declaration.

## 7. AMEND-5: realization state is fully derived

Message 003 correctly rejects hand-maintained EVIDENCED / QUALIFIED / OPERATIONAL statuses.

V0.3 strengthens the rule further:

    authors do not directly set RealizationState

Authors create source-owned facts:

    realization relation
    governed deferral record
    evidence record / warrant reference
    qualification decision
    AO activation record

The system derives:

    UNLINKED
        no valid realization relation and no valid deferral

    LINKED
        realization relation exists but qualifying evidence is absent

    EVIDENCED
        required evidence is present but qualification is not complete

    QUALIFIED
        effective WARRANT-F decision satisfies the realization requirement

    OPERATIONAL
        qualified realization has the required operational activation record

    DEFERRED
        a valid governed deferral is active

Conflicting or stale source facts produce REVIEW_REQUIRED rather than a hand-selected state.

This removes another manually maintained projection and directly supports WMR-H.

## 8. AMEND-6: AO guarantees are mediation-class-specific

P7-D01 pre-dispatch prevention is possible only when the consequential action traverses a surface that can actually intercept it.

V0.3 therefore classifies action paths, not actors in the abstract:

    MEDIATED
        an ADS-controlled preflight can prevent effect

    COOPERATIVE
        executor follows/simulates the protocol voluntarily;
        AO cannot technically prevent bypass

    UNMEDIATED
        effect can occur without an ADS preflight opportunity

The classification is scoped to:

    executor surface
    action class
    intended consequence

One collaborator or provider may therefore use different mediation classes for different operations.

Guarantees become explicit:

    MEDIATED
        preventive AO preflight may be claimed after qualification

    COOPERATIVE
        protocol participation is advisory/cooperative;
        binding protection is detective plus any independent
        accepted-state admission gate

    UNMEDIATED
        AO is detective for the raw effect;
        accepted-state admission may still be preventive when
        WARRANT-F / host controls can enforce it

Mediation class is not trust level.

Execution surface is not identity.

This aligns AO-10 with WF-A35 rather than reopening WARRANT-F.

DRP-05b measures real interceptability instead of assuming it.

## 9. AMEND-7: AO cannot select away assurance claims

Research 312 / 314 allowed "activated claims" inside AssuranceRequest. That is too permissive.

V0.3 removes claim-set authority from AO.

AO supplies:

    exact subject/revision
    base revision where required
    intended consequence
    ActionContract / control-cycle reference
    capability/trust context
    optional profile hint / invocation shorthand
    optional supplemental context

WARRANT-F resolves:

    effective policy
    required claim set
    thresholds
    freshness
    trust requirements
    policy ratchet
    resulting decision

An AO-supplied profile is a shorthand/hint only and cannot weaken policy-derived requirements.

AO may request supplemental checking through a governed extension, but per-request data cannot remove, replace or suppress policy-required claims.

This preserves WF-A31 and the accepted AO / assurance separation.

DRP-09 must prove omission resistance and profile non-bypass.

## 10. AMEND-8: permanent transition semantics leave the one-time contract

Research 258 AM-7 already established permanent transition management.

V0.3 therefore refines the three strata:

    C1 VERSIONED CORE SEMANTIC CONTRACT
        reusable semantic invariants
        including authority-preserving successor-transition semantics,
        bridge modes/membrane invariants and rollback semantics

    C2 ADS PROJECT-SYSTEM REALIZATION CONTRACT
        reusable ADS realization of JW1 / Engineering / WMR-H / AO /
        transition management / assurance seams / adapters

    C3 R8 TRANSITION AND CUTOVER INSTANCE CONTRACT
        this transition's exact migration units, compatibility projections,
        thresholds, schedules, oracle retirement, cutover evidence and
        authority-switch plan

C1 is versioned and governed through AO-4.

"Core" does not mean immutable or extracted-framework-owned.

General framework extraction remains deferred.

Exact physical document count remains open.

## 11. AMEND-9: adoption economics becomes a first-class architecture criterion

The strongest architecture is not successful if normal project work routinely bypasses it because authoring and maintenance cost is too high.

V0.3 therefore adds the design rule:

Every target metadata/control element must satisfy at least one of:

    GENERATED
        derivable from already-authored authoritative facts

    NATURAL_EVENT
        authored at a moment the responsible author is already present,
        such as acceptance-time obligation declaration

    CONSEQUENTIAL_JUSTIFICATION
        it enables a named consequential decision that cannot be
        supported reliably without the element

Otherwise the element is presumptively removed.

DRP-08 will replay real recent project activity into the target representation and measure:

    authoring time / tool effort / token burden
    validation failure rate
    correction rate
    generated-versus-authored fraction
    metadata volume per consequential change
    failure modes under the actual collaborator workflow

Budgets and thresholds must be preregistered before execution.

Adoption economics is a whole-system falsifier, not a later usability optimization.

## 12. AMEND-10: rollback has a loss boundary

V0.3 accepts a declared rollback window around authority switch.

Within that window:

    zero loss of Project-governed authoritative facts,
    control facts and transition receipts created after switch

must be possible through a qualified mechanism.

Possible mechanisms remain open:

    reverse compatibility projection
    bounded dual write
    replayable receipts/state
    immutable snapshot plus forward replay
    another qualified design

This zero-loss requirement does not claim that arbitrary external-world side effects can be undone. External irreversible effects require their own action/compensation semantics.

The rollback window closes only through an explicit owner decision after qualification evidence.

After closure, returning to the predecessor is a new governed transition rather than "rollback".

## 13. AMEND-11: early CURRENT_STATE relief is a separate AO-4 candidate

The daily cost of unbounded CURRENT_STATE growth is real.

However, CURRENT_STATE is still a current authority/oracle surface and cannot be compacted merely because the successor design prefers a bounded generated view.

V0.3 therefore accepts only the governance obligation:

    EARLY_ORIENTATION_RELIEF=SEPARATE_AO4_CASE_REQUIRED_BEFORE_EXECUTION

A future bounded case may relocate settled history while retaining the current authoritative/oracle contract.

Before any such mutation:

    exact current baseline must remain reproducible from Git
    history-retention semantics must be explicit
    current routing/state invariants must remain satisfied
    reference integrity must be checked
    rollback must exist
    comparison fixtures needed by DRP-06 must be frozen

No CURRENT_STATE compaction is authorized by this record.

## 14. Revised decision-relevant probe namespace

To prevent collision between architecture-decision probes and later realization qualification, V0.3 replaces the overloaded P-numbering with two namespaces.

Decision-relevant probes:

    DRP-01  SHARED SEMANTIC SUBSTRATE SUFFICIENCY
            seam inventory
            admission / rejection
            role granularity
            temporary-status vocabulary
            anti-over-unification negative controls

    DRP-02  SEMANTIC NAVIGATION ARCHITECTURES
            Research 217 versus position/relations/search alternatives
            scenario corpus frozen before arms
            equalized/reported authoring effort
            maintenance/drift leg
            preregistered current-layout responsibility mapping

    DRP-03  OBLIGATION-UNIT GRANULARITY AND BIRTH
            acceptance-event retrospective replay
            independent delimitation
            known-gap sensitivity
            false-gap specificity
            fully derived realization-state computation

    DRP-04  KA-R51 DETECTOR PRECISION
            D1-D4
            positive historical witnesses
            ordinary-session negative controls

    DRP-05a ACTIONSHAPE CLASSIFIABILITY
            typed provider-neutral classification coverage

    DRP-05b ACTION INTERCEPTABILITY / MEDIATION
            MEDIATED / COOPERATIVE / UNMEDIATED share
            preventive-versus-detective control boundary

    DRP-06  BOUNDED ORIENTATION
            fresh-collaborator reconstruction / continuation parity
            read/tool cost
            size budget
            exact frozen current comparator

    DRP-07  SPECIFICATION 028 LINEAGE AND CONTRACT PARTITION
            all 46 sections
            all 104 uppercase MUST occurrences across 94 lines
            semantic normative obligations beyond MUST-token search
            C1/C2/C3 disposition
            cross-contract coupling

    DRP-08  ADOPTION ECONOMICS
            real recent project replay
            authoring/validation/correction burden
            generated-versus-authored fraction
            preregistered budget and falsifier

    DRP-09  ASSURANCE-REQUEST CLAIM INTEGRITY
            policy-required claims survive omission
            profile/context cannot suppress policy claims
            supplemental context cannot weaken effective gate policy

Realization qualification uses a separate namespace:

    RQP-01  BRIDGE SHADOW REPLAY
    RQP-02  CLI / RESULT DETERMINISM
    RQP-03  CONTROL-RECORD CONCURRENCY
    RQP-04  PROJECTION EQUALITY
    RQP-05  ORACLE SENSITIVITY / SPECIFICITY
    RQP-06  ROLLBACK / RECOVERY DRILLS
    RQP-07  PROVIDER / HOST P-H SUCCESSOR QUALIFICATION

RQP execution remains downstream of semantic architecture disposition unless a bounded fixture is explicitly needed to answer a decision-relevant question.

## 15. Falsifiers carried into V0.3

Message 003's falsifiers are accepted and generalized:

    F-A ADOPTION BURDEN
        DRP-08 exceeds preregistered cost / failure budget
        -> simplify architecture before owner acceptance

    F-B UNDELIMITED OBLIGATIONS
        acceptance replay misses material accepted obligations
        -> obligation-birth mechanism insufficient

    F-C ROLE GRANULARITY FAILURE
        mixed-role units remain dominant after practical decomposition
        -> role model must change

    F-D LOW MEDIATED SHARE
        preventive preflight covers too little consequential activity
        -> AO guarantees must become detective-first for those classes

    F-E SUBSTRATE CREEP
        primitives without valid seam justification accumulate
        -> shared substrate boundary insufficient

    F-F STATE DRIFT
        derived realization state disagrees with source-owned facts /
        hand-maintained expectations
        -> hand-maintained projection is invalid, or derivation semantics
           are incomplete and require amendment

Additional standing falsifier:

    F-G CONTRACT STRATA COUPLING
        DRP-07 shows C1/C2/C3 require frequent circular authority or
        mixed-lifetime edits
        -> contract partition must be redesigned before acceptance

## 16. P2 anti-home-field controls

DRP-02 must not reproduce Research 217's prior home-field advantage.

Before any competing arm is built:

    task scenarios are frozen
    scoring rules are frozen
    assignment/authoring effort accounting is frozen
    maintenance additions are frozen or generated from a frozen rule
    current-layout logical-position mapping is frozen
    any blind/held-out split is fixed

Where practical, the scenario author should not be the designer of a compared arm.

If that cannot be achieved cleanly with available collaborators, use real historical project events selected by a frozen mechanical rule rather than designer-authored scenarios.

Research 217 remains eligible to win.

## 17. Current architecture candidate

The V0.3 whole-system candidate is now:

    durable Project knowledge
        human-governed meaning and normative sources

    minimal shared semantic substrate
        only seam-justified shared primitives
        no universal domain model

    bounded domain models
        AO
        workstreams
        collaboration
        assurance
        transition/evolution
        compose through explicit seams

    JW1 / project/system
        reconstruction
        activation/orchestration
        authority/action contracts
        continuity/recovery
        architecture evolution
        workstream/Git policy
        obligation declaration/realization orchestration
        generated orientation/navigation
        permanent transition management

    Project Engineering / project/engineering
        WARRANT-F kernel
        verifier execution
        repository engineering
        provider/host adapters
        Git mechanics
        delivery/release
        migration execution
        evidence publication
        recovery qualification

    Product
        independently resolved
        no Project runtime dependency

    representation
        WMR-H writer/semantics/lifecycle architecture

    assurance
        policy-derived effective claims
        AO cannot suppress required assurance

    control
        mediation-aware preventive/detective guarantees

    transition
        semantic shadow before physical migration
        permanent bridge semantics
        instance-specific R8 transition plan
        zero-loss Project-fact rollback window around authority switch

    adoption
        first-class qualification dimension

## 18. What remains deliberately unselected

V0.3 still does not select:

    exact role/status enum
    exact shared primitive set
    exact relation registry
    final semantic-navigation architecture
    final obligation-unit granularity
    exact persistent representation of obligation units
    exact control-record schema
    exact provider/host implementation
    exact Git branch / PR / merge workflow
    exact CI/CD provider
    exact daemon/service hosting model
    exact rollback mechanism
    exact successor specification file count
    framework extraction
    current-oracle retirement
    authority switch

These are not omissions by accident. They are either decision-probe questions, realization questions or later owner decisions.

## 19. Next governed stage

MC-0029 comparative architecture design is complete enough to leave the design-dialogue phase and enter decision-relevant empirical preregistration.

The next task is not implementation.

It is to freeze a coherent preregistration for DRP-01 through DRP-09, including:

    fixtures / corpora
    independence and blinding where useful
    metrics
    thresholds
    negative controls
    falsifiers
    attempt integrity
    result classification
    cross-probe dependencies
    execution order

No probe result should be observed before its decision rule is frozen.

After all decision-relevant probes are reconciled, the owner can receive an explicit KEEP / AMEND / REOPEN / acceptance decision package.

## 20. Current boundary

    MC0029_MESSAGE001=COMPLETE
    MC0029_MESSAGE002=COMPLETE
    MC0029_MESSAGE003=COMPLETE
    MC0029_MESSAGE004=CHATGPT_RECONCILIATION

    RESEARCH314=AMENDED_BY_RESEARCH315
    INTEGRATED_PROJECT_SYSTEM_V03=FROZEN_PRE_DECISION_CANDIDATE

    UPSTREAM_R5_TO_R8C_REOPEN=false
    SPECIFICATION028_WHOLE_DISPOSITION_CANDIDATE=SUPERSEDE

    SUBSTRATE_ADMISSION=SEAM_JUSTIFIED_PENDING_DRP01
    ROLE_GRANULARITY=SEMANTIC_UNIT_PENDING_DRP01
    LOGICAL_POSITION=DRP02_ARM_NOT_SELECTED_TARGET

    OBLIGATION_BIRTH=ACCEPTANCE_POSTFLIGHT_CANDIDATE
    OWNER_DECISION_TEMPORAL_VALIDITY=NOT_CONTINGENT_ON_BOOKKEEPING
    REALIZATION_STATE=FULLY_DERIVED_CANDIDATE

    AO_MEDIATION_CLASSES=MEDIATED_COOPERATIVE_UNMEDIATED
    AO_PREVENTION_CLAIMS=MEDIATION_SCOPED
    WARRANT_EFFECTIVE_CLAIMS=POLICY_DERIVED
    AO_CANNOT_SUPPRESS_REQUIRED_CLAIMS=true

    TRANSITION_MANAGEMENT=PERMANENT_C1_C2
    R8_INSTANCE_TRANSITION=C3
    ROLLBACK_WINDOW=ZERO_LOSS_PROJECT_FACTS_CANDIDATE

    ADOPTION_ECONOMICS=FIRST_CLASS_DECISION_CRITERION
    EARLY_ORIENTATION_RELIEF=SEPARATE_AO4_CASE_REQUIRED_BEFORE_EXECUTION

    DECISION_PROBES=DRP01_TO_DRP09
    REALIZATION_PROBES=RQP01_TO_RQP07

    OWNER_DECISION=NOT_READY
    AO10_PRODUCTION_IMPLEMENTATION_AUTHORIZED=false
    AO10_SHADOW_ACTIVATION_AUTHORIZED=false
    CURRENT_STATE_COMPACTION_AUTHORIZED=false
    PHYSICAL_MIGRATION_AUTHORIZED=false
    CURRENT_ORACLE_RETIREMENT_AUTHORIZED=false
    AUTHORITY_SWITCH_ALLOWED=false

    NEXT=DRP01_TO_DRP09_PREREGISTRATION
