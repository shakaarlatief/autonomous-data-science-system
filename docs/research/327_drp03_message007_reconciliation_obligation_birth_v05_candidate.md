# Research 327: DRP-03 Message 007 Reconciliation and Obligation-Birth V0.5 Candidate

**Date:** 2026-09-25
**Status:** MESSAGE 007 RECONCILED / RESEARCH 326 AMENDED / DRP-03 AMEND RETAINED / V0.5 CANDIDATE / R2 PREREGISTRATION NEXT / NO R2 HARNESS FROZEN
**Parent:** Research 326 / MC-0029 Message 007
**Accepted architecture base:** R5-R8C through Research 311
**Frozen DRP-03 result:** Research 326
**Claude critique:** docs/model_collaboration/threads/MC-0029/messages/007_claude_drp03_amendment_critique.md
**Evidence binding:** docs/research/project_knowledge_activation_orchestration/ao10/evidence/drp03_run001_binding.json
**Scope:** Reconcile every material Message 007 amendment into the obligation-birth candidate, correct the empirical interpretation of DRP-03 R1 without rewriting the frozen result, and define the design contract that a later DRP-03 R2 preregistration must test.
**Authority:** Research candidate only. This record does not accept V0.5, amend Specification 028, freeze an R2 harness, authorize AO-10 production implementation, authorize physical migration, retire current oracles, or switch authority.

## 1. Reconciliation disposition

Message 007's final disposition is accepted:

    Research 326
        -> AMEND

The eleven required changes R2-REQ-1 through R2-REQ-11 are incorporated below.

The core Research 326 diagnosis remains:

    DRP03=AMEND

    free-form retrospective reconstruction
        is not reproducible enough
        to define authoritative obligation boundaries

    obligation birth
        belongs at the governing acceptance boundary

    legacy extraction
        remains candidate-only until governed reconciliation

    RealizationState
        remains derived rather than authored

Message 007 materially strengthens all four statements.

## 2. DRP-03 R1 remains a valid AMEND

The frozen R1 comparison remains immutable evidence:

    reviewer A propositions        157
    reviewer B propositions        136
    observed matches                73

    proposition-set F1              0.49829351535836175
    frozen threshold                0.85

    grouping F1                     0.6753246753246753
    frozen threshold                0.70

The AMEND is not an artefact of the paraphrase matcher.

At each exact shared anchor, the maximum possible one-to-one match count is the smaller proposition count.

Across the corpus:

    reviewer A anchors              67
    reviewer B anchors              51
    shared anchors                  51
    A-only anchors                  16
    B-only anchors                   0
    propositions at A-only anchors  34

    maximum possible matches        99
    maximum possible proposition F1 0.6757679180887372

Even a perfect paraphrase matcher cannot reach the frozen 0.85 criterion.

The failure therefore contains genuine semantic disagreement in:

    normative-item selection
    proposition granularity
    realization-boundary granularity

not merely wording variance.

## 3. R1 evidence scope is corrected

Research 326 correctly rejected the reviewer-A false-gap value as decision evidence, but Message 007 identifies two additional limitations.

The corrected interpretation is:

    reviewer-A false-gap metric
        NOT_DECISION_USABLE
        because the hidden evaluator coupled expected wording/granularity
        to gate identity

    reviewer-B false-gap metric
        NOT_BLIND
        because ChatGPT authored and knew the evaluator key before
        authoring reviewer B

    witness-tag sensitivity
        INSTRUCTED_NOT_DETECTED
        because the reviewer packet named all three witness tags and
        required reviewers to attach them

Therefore the following R1 observations remain useful:

    both reviewers mapped material witness concepts when named
    both reviewers created zero units for the two negative-control sources
    the pure state-derivation function passed all seven frozen fixtures

but R1 does not establish blind witness sensitivity or blind false-gap specificity.

The R1 attempt remains a valid AMEND because the proposition-selection and grouping failures independently determine AMEND, and the discovered measurement defects do not create the failing result.

## 4. Result-evidence digest correction

Research 326 recorded:

    a5a7a51e25f635d3536a1a4c5a64fa02c76fe8539fbef6503a0ca7978a74c609

That is the SHA-256 of the Windows working-tree serialization of the JSON with CRLF line endings.

The tracked Git blob is normalized to LF.

For durable repository evidence, the canonical binding is:

    evidence path
        docs/research/project_knowledge_activation_orchestration/ao10/evidence/drp03_run001_result.json

    first tracked commit
        7eb98abcda10e0fc7417c32da493239fea78b807

    Git blob OID
        bd26cd313fcdaf8163fa0b605a3fcfacb23f471b

    hash basis
        GIT_BLOB_BYTES_AT_COMMIT

    SHA-256
        f2e7b9071320079d5b239ef38b1d1d9f252a6af36d3a574e16df081dd09b8966

Research 326 is preserved historically and is not edited.

The new machine-readable binding records both digests and marks the checkout-specific CRLF digest non-canonical.

## 5. The R1 disagreement exposes two undefined concepts

### 5.1 Which accepted statements create realization obligations

The R1 packet did not define a sufficient normativity taxonomy.

Reviewer A treated many accepted clarifications, retention statements, sequencing rules, and dispositions as obligations.

Reviewer B selected a narrower set.

Both were permitted by the frozen instructions.

V0.5 therefore introduces a closed normative-kind taxonomy for accepted delta items:

    OBLIGATION
        requires a future discrete realization act or effect

    CONSTRAINT
        establishes a standing invariant or admissibility condition whose
        enforcement/verification must remain traceable while the constraint is in force

    DISPOSITION
        changes governing/lifecycle state by the authority event itself,
        such as accepting, superseding, retiring, or reopening a subject

    SEQUENCING
        establishes an ordering, prerequisite, hold, or transition-gating rule

    PRINCIPLE
        supplies governing interpretation or design direction but does not,
        by itself, specify a separately realizable act

The taxonomy is about the accepted normative delta, not prose style.

A single acceptance event may contain multiple kinds.

Consequences:

    OBLIGATION
        births or revises an ObligationUnit

    CONSTRAINT
        must have a standing realization/enforcement binding;
        if that binding does not already exist, an ObligationUnit is born
        to establish it

    DISPOSITION
        is realized by the authority event itself;
        any follow-on work must be separately declared

    SEQUENCING
        binds a governed dependency/gate rule;
        if an implementation/control surface is required and absent,
        a corresponding ObligationUnit is born

    PRINCIPLE
        does not silently become an implementation obligation;
        concrete consequences must appear separately as OBLIGATION,
        CONSTRAINT, or SEQUENCING items

This prevents both under-tracing and the creation of permanent open obligations for every accepted statement.

### 5.2 What constitutes one realization boundary

The V0.3/V0.4 phrase one realization boundary and one evidence path was not operational enough.

V0.5 defines the grouping test:

Two accepted realization-requiring items belong in the same ObligationUnit only when all of the following hold:

    1. the same realization act or effect would satisfy both;

    2. the same evidence event/path is sufficient to demonstrate both;

    3. the same qualification/admission decision closes both;

    4. failure of either item would constitute the same realization failure,
       rather than an independently remediable failure.

If any condition is false, split the unit.

This is stronger than section-level grouping and weaker than one-unit-per-sentence.

Cross-heading grouping is allowed when the four conditions hold.

Heading location is not an obligation boundary.

## 6. AcceptanceDeclarationSet and obligation birth

V0.5 distinguishes the accepted semantic delta from the realization-tracking subset.

Every governed acceptance event carries an:

    AcceptanceDeclarationSet

containing:

    exact acceptance identity
    exact accepted subject/revision
    exact accepted normative delta item IDs
    normative kind for each delta item
    resulting ObligationUnits where required
    standing constraint/sequencing bindings where applicable
    explicit CREATES_NO_REALIZATION_UNITS when appropriate

The prior name ObligationDeclarationSet remains usable as the realization-requiring projection, but it is not the full accepted normative delta.

This avoids forcing DISPOSITION and PRINCIPLE items into ObligationUnits while still preserving the complete accepted normative interpretation.

## 7. Declaration drafting moves before the decision

DRP-05b established:

    MEDIATED       0
    COOPERATIVE   53
    UNMEDIATED    12
    MEDIATED share 0.00

Therefore a target mechanism that relies on mediated post-acceptance interception would operate almost entirely in its fallback path today.

V0.5 moves declaration drafting into proposal authoring.

For a normal governed change:

    candidate governing change
        ->
    exact change package / proposal
        ->
    mechanically addressable normative-delta candidates
        ->
    candidate AcceptanceDeclarationSet
        ->
    ambiguity review where materially consequential
        ->
    owner/governance decision
        ->
    accepted source text + accepted declaration set are bound together
        ->
    acceptance postflight validates persistence/binding
        ->
    realization evidence accumulates from natural owners

The declaration set is part of what the authority reviews, rather than an interpretation invented after the decision.

This does not require AO to sit technically on the mutation path.

For COOPERATIVE execution, proposal completeness is a governed procedural precondition and AO can detect missing closure.

For UNMEDIATED authority events:

    the valid authority event remains valid

but:

    missing declaration
        -> CONTROL_OBSERVATION / REVIEW_REQUIRED
        -> affected downstream scope may be held
        -> owner may explicitly waive the hold

If a proposal existed, postflight recovers the already-authored candidate declaration rather than re-deriving it from accepted prose.

If no proposal/declaration existed, postflight extraction is candidate-only until reconciled.

## 8. Closed governed acceptance-event kinds

The V0.5 birth rule applies only to explicit governing transitions of these kinds:

    OWNER_DECISION_ACCEPTANCE
    AO4_NORMATIVE_DISPOSITION
    SPECIFICATION_ACCEPTANCE_OR_AMENDMENT
    REQUIREMENT_ACCEPTANCE_OR_AMENDMENT
    POLICY_OR_PROFILE_ACCEPTANCE_OR_AMENDMENT
    AUTHORITY_OR_CUTOVER_DECISION

A research document containing the word ACCEPTED is not automatically an acceptance event.

It qualifies only when it is the authoritative carrier of one of the event kinds above or records an explicitly identified authority event.

This prevents status-line vocabulary from defining the birth scope.

The list itself remains challengeable through governed architecture evolution, but implementation may not silently widen it.

## 9. Natural-owner fact direction

The accepted declaration is not a mutable requirements checklist.

After birth, realization facts originate at their natural owner.

Examples:

    implementation / migration artifact
        REALIZES <obligation-id>

    assurance claim / verifier / decision evidence
        EVIDENCES or QUALIFIES <obligation-id>

    activation / cutover receipt
        ACTIVATES <obligation-id>

    governed deferral record
        DEFERS <obligation-id or deterministic scoped selector>

The accepted semantic payload of an ObligationUnit is immutable after birth.

Later normative rescoping, addition, removal, split, merge, or replacement creates a governed successor relation rather than silently editing history.

Current state is derived by reverse lookup over valid source-owned facts.

This preserves the natural-owner rule and avoids a hand-maintained requirements database.

## 10. Deferral validity and REVIEW_REQUIRED

R1 exposed a critical attribution disagreement:

    matched propositions                 73
    same derived state                   33
    agreement rate                       0.4520547945205479

    A DEFERRED / B UNLINKED             30

    reviewer-A deferred units           54 / 97
    reviewer-B deferred units           12 / 60

A generic program hold is not automatically a governed deferral.

A valid DeferralRecord must bind:

    exact obligation IDs
        OR
    a deterministic scope selector whose resolved obligation set is recorded

and must include:

    governing authority
    blocking reason
    reactivation/closure condition
    future evidence path
    temporal/revision binding
    provenance

State derivation first validates the facts.

Candidate order:

    invalid / stale / contradictory required facts
        -> REVIEW_REQUIRED

    valid governed deferral
        -> DEFERRED

    no valid realization relation and no valid deferral
        -> UNLINKED

    realization relation but required evidence absent
        -> LINKED

    evidence present but qualification incomplete
        -> EVIDENCED

    qualification complete but required activation/effect absent
        -> QUALIFIED

    valid realization + evidence + qualification + activation
        -> OPERATIONAL

REVIEW_REQUIRED is not a manually authored lifecycle state.

It is the deterministic consequence of source-fact invalidity or contradiction.

The realization lifecycle remains separate from governing lifecycle such as supersession or retirement.

## 11. Temporal-authority rules

V0.5 adopts Message 007 T-1 through T-3.

T-1:

    The accepted source text remains authoritative.

    The AcceptanceDeclarationSet is the accepted structured interpretation
    bound to that text.

    A conflict between accepted text and declaration yields REVIEW_REQUIRED.
    Neither silently overrides the other.

T-2:

    declaration correction
        CLERICAL
            locator, formatting, transcription, or non-semantic metadata repair
            with no change to accepted meaning

        NORMATIVE
            adds, removes, splits, merges, rescopes, reclassifies, or changes
            the realization consequence of accepted meaning

    NORMATIVE correction requires the same level of governing authority
    required for the original semantic change.

T-3:

    A downstream hold caused by missing/invalid declaration state is
    owner-overridable through an explicit recorded waiver.

Bookkeeping never acquires authority above the owner.

A waiver is evidence and does not pretend the declaration defect disappeared.

## 12. Legacy accepted history

Retrospective extraction is not obligation birth.

For legacy material:

    frozen accepted source/revision
        ->
    deterministic candidate segmentation
        ->
    candidate normative-kind classification
        ->
    candidate realization-unit grouping
        ->
    candidate fact attribution
        ->
    governed reconciliation
        ->
    accepted legacy declaration set

Until that reconciliation:

    legacy extracted units
        = CANDIDATE

They may:

    raise REVIEW
    raise ControlObservation
    support migration analysis

They may not:

    satisfy an admission gate
    fail an admission gate as if authoritative
    silently reinterpret the earlier owner/governance decision

Legacy reconciliation is required only when at least one of these holds:

    contract remains IN_FORCE
    obligation must survive into a successor
    lineage is required for oracle retirement / migration safety
    unresolved historical meaning is needed by a consequential current decision

A contract already scheduled for complete supersession does not require a full redundant legacy ledger when DRP-07 successor lineage can preserve its live obligations directly.

## 13. DRP-03 R2 is split by question

Research 326's first R2 sketch mixed the target birth mechanism with legacy extraction.

V0.5 requires three separately scored components.

### R2-BIRTH

Question:

    Can the acceptance-time declaration mechanism capture the accepted
    normative delta with high completeness/precision, bounded ambiguity,
    and bounded authoring burden?

Replay real acceptance events using the information available before the decision:

    proposal / candidate text
    accepting change package
    exact pre-decision context allowed by the fixture

A declaration author drafts the candidate AcceptanceDeclarationSet before seeing any hidden evaluator key.

An independent auditor evaluates:

    normative-item completeness
    precision
    normative-kind classification
    unit-boundary correctness
    ambiguity / REVIEW_REQUIRED rate
    authoring effort

### R2-LEGACY

Question:

    Can legacy candidate extraction support bounded migration/reconciliation
    without silently becoming authority?

Use mechanically segmented frozen legacy sources.

Reviewers independently classify item IDs and group realization-requiring item IDs.

This component tests migration tooling, not the authority-birth mechanism.

### R2-STATE

Question:

    Given frozen accepted units and source-owned realization facts,
    can reviewers or deterministic rules attribute valid facts and derive
    state reproducibly?

Include fact-validity fixtures for:

    generic program hold
    deferral missing reactivation condition
    deferral missing future evidence path
    stale fact
    contradictory fact
    evidence bound to the wrong subject/revision
    valid deferral
    valid operational realization

The component scores state agreement in addition to deterministic function correctness.

## 14. R2 anti-leakage and reviewer independence

The R2 source-item segmentation must be mechanical.

The segmentation rule is frozen before any hidden key is authored.

It may split mechanically by:

    sentence
    list item
    code-block line / structured row where semantically addressable

It must not perform judgment-based merging.

Items receive stable IDs.

Reviewers classify and group IDs.

Units may span headings.

Hidden witnesses are not named in reviewer packets.

Specificity and witness keys bind stable item/event IDs, not expected reviewer wording.

Because both current MC-0029 reviewers have now seen the R1 witnesses and candidate design, at least one R2 decision reviewer must be a fresh interaction with no MC-0029 result/witness exposure.

If a harness/key author also annotates, a third fresh blind reviewer is mandatory and the key-author annotation cannot be the sole blind specificity evidence.

The current Claude-04 interaction is no longer eligible as the blind witness reviewer.

The current ChatGPT interaction is no longer eligible as the blind evaluator-key reviewer.

## 15. R2 metrics and threshold discipline

The original 0.85 proposition F1 cannot simply be relabeled as an item-ID threshold.

R2 uses a different measurement problem.

The preregistration stage must therefore freeze and justify thresholds before held-out scoring.

Required metrics include at least:

    normative selection
        precision
        recall / F1
        Cohen's kappa over normative vs non-normative item classification

    normative kind
        multiclass agreement / kappa

    unit grouping
        pairwise same-unit F1 or another fully frozen item-pair metric

    state attribution
        exact derived-state agreement
        material DEFERRED vs UNLINKED disagreement rate

    birth audit
        material omission count/rate
        false obligation count/rate
        REVIEW_REQUIRED rate

    adoption
        authoring effort per acceptance event
        owner-intervention count/rate

Threshold selection may use a disjoint development/calibration corpus only when:

    development and held-out corpora are frozen first
    decision thresholds are frozen before held-out labels/results are observed
    the calibration rationale is recorded
    held-out witnesses remain concealed

No R1 threshold may be weakened retroactively.

R1 remains failed under its original protocol.

## 16. Falsifiers added

V0.5 adopts F-O1 through F-O5.

F-O1 STATE ATTRIBUTION DISAGREEMENT

    If derived-state agreement remains below the preregistered R2 threshold
    after DeferralRecord validity is applied, the KA-R52 fact/deferral model
    must change.

F-O2 ACCEPTANCE-BIRTH OMISSION

    If independent birth audit finds material accepted normative items omitted
    above threshold, acceptance-time birth does not close the upstream blind
    spot and must be redesigned.

F-O3 DECLARATION AUTHORING BURDEN

    If proposal-time declaration cost exceeds the DRP-08 budget, simplify the
    declaration model before acceptance.

F-O4 NORMATIVE-KIND SUBJECTIVITY

    If blind normative-kind agreement remains below threshold, the taxonomy
    must change before adoption.

F-O5 AMBIGUITY BURDEN

    If REVIEW_REQUIRED frequency requires excessive owner intervention, the
    ambiguity model is an adoption failure and must be simplified.

## 17. Downstream dependency changes

WARRANT-F:

    the no-untracked-third-state claim must rely on detected, not named,
    witnesses and valid DeferralRecord semantics.

AO-3:

    proposal-time declaration closure becomes a governing-change preflight
    obligation.

    Under COOPERATIVE / UNMEDIATED execution it remains detective/procedural,
    not falsely described as technical prevention.

DRP-04:

    may proceed only for KA-R51 detectors that do not consume disputed
    obligation-state semantics.

DRP-06:

    bounded-orientation fixtures must not treat obligation state as qualified
    until R2-STATE passes.

DRP-07:

    remains held until R2 defines qualified normative-item and unit semantics.

    It must use the normative-kind taxonomy for Specification 028 lineage.

DRP-08:

    must explicitly measure proposal-time declaration authoring,
    DeferralRecord authoring, REVIEW_REQUIRED burden, and owner intervention.

## 18. R2-REQ-1 through R2-REQ-11 disposition

    R2-REQ-1   ACCEPTED
    R2-REQ-2   ACCEPTED_AND_REFINED
    R2-REQ-3   ACCEPTED
    R2-REQ-4   ACCEPTED
    R2-REQ-5   ACCEPTED
    R2-REQ-6   ACCEPTED_AND_STRENGTHENED_TO_PROPOSAL_TIME
    R2-REQ-7   ACCEPTED
    R2-REQ-8   ACCEPTED
    R2-REQ-9   ACCEPTED_AND_SPLIT_BY_R2_COMPONENT
    R2-REQ-10  ACCEPTED_AS_R2_BIRTH
    R2-REQ-11  ACCEPTED

No required Message 007 amendment remains intentionally omitted.

## 19. Current boundary

    DRP09=PASS
    DRP05A=PASS
    DRP05B=PASS_DETECTIVE_FIRST
    DRP01=PASS
    DRP03_R1=AMEND

    RESEARCH326=AMENDED_BY_RESEARCH327
    MESSAGE007=RECONCILED

    R1_PROPOSITION_F1=0.49829351535836175
    R1_MAX_POSSIBLE_PARAPHRASE_F1=0.6757679180887372
    R1_GROUPING_F1=0.6753246753246753
    R1_STATE_AGREEMENT=0.4520547945205479

    R1_REVIEWER_A_FALSE_GAP=NOT_DECISION_USABLE
    R1_REVIEWER_B_FALSE_GAP=NOT_BLIND
    R1_WITNESS_SENSITIVITY=INSTRUCTED_NOT_DETECTED

    DRP03_EVIDENCE_HASH_BASIS=GIT_BLOB_BYTES_AT_COMMIT
    DRP03_EVIDENCE_SHA256=f2e7b9071320079d5b239ef38b1d1d9f252a6af36d3a574e16df081dd09b8966

    OBLIGATION_BIRTH=PROPOSAL_AUTHORED_ACCEPTANCE_BOUND_V05_CANDIDATE
    NORMATIVE_KIND_TAXONOMY=V05_CANDIDATE
    REALIZATION_BOUNDARY=V05_OPERATIONAL_RULE
    REALIZATION_FACT_DIRECTION=NATURAL_OWNER_REVERSE_REFERENCES
    REALIZATION_STATE=FULLY_DERIVED_WITH_REVIEW_REQUIRED_CANDIDATE
    LEGACY_EXTRACTION=CANDIDATE_ONLY

    DRP03_R2=NOT_YET_FROZEN
    DRP03_R2_COMPONENTS=R2_BIRTH_R2_LEGACY_R2_STATE
    FRESH_BLIND_REVIEWER_REQUIRED=true

    OWNER_DECISION=NOT_READY
    AO10_PRODUCTION_IMPLEMENTATION_AUTHORIZED=false
    AO10_SHADOW_ACTIVATION_AUTHORIZED=false
    PHYSICAL_MIGRATION_AUTHORIZED=false
    CURRENT_ORACLE_RETIREMENT_AUTHORIZED=false
    AUTHORITY_SWITCH_ALLOWED=false

    NEXT=DRP03_R2_EXACT_PREREGISTRATION_AND_HARNESS_DESIGN
