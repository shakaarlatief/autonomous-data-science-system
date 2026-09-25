# Research 326: DRP-03 AMEND and Obligation-Birth V0.4 Amendment Candidate

**Date:** 2026-09-25
**Status:** DRP-03 AMEND / RETROSPECTIVE FREE-FORM DELIMITATION NOT REPRODUCIBLE / ACCEPTANCE-BIRTH MECHANISM MUST STRENGTHEN / DERIVED REALIZATION STATE RETAINED / ONE FALSE-GAP SUBMETRIC NOT DECISION-USABLE / V0.4 CANDIDATE / CLAUDE CRITIQUE NEXT / REQUALIFICATION REQUIRED
**Parent protocol:** Research 316 / AO10-DRP-V01
**Harness freeze:** Research 324
**Reviewer freeze:** Research 325
**Claude reviewer A:** b9fba658e422279d8f8b8193b8c1bda88302dcda
**ChatGPT reviewer B:** sha256:39410f682818ee558defe3fb1fd8d582d14835d2f22d76733d101bb0e4813737
**Durable result evidence:** docs/research/project_knowledge_activation_orchestration/ao10/evidence/drp03_run001_result.json
**Result SHA-256:** a5a7a51e25f635d3536a1a4c5a64fa02c76fe8539fbef6503a0ca7978a74c609
**Scope:** Reconcile the frozen DRP-03 run without weakening its preregistered thresholds, distinguish target evidence from a discovered evaluator-specificity defect, and derive a prospective V0.4 obligation-birth amendment for independent critique before requalification.
**Authority:** Research candidate only. This record does not accept V0.4, amend Specification 028, authorize production AO-10, authorize migration, or change current authority.

## 1. Frozen result

The exact frozen comparison executed after both reviewer artifacts were committed.

Observed:

    reviewer A propositions        157
    reviewer B propositions        136
    matched propositions            73

    proposition-set F1              0.49829351535836175
    required                        >= 0.85
    result                          FAIL

    unit-grouping agreement F1      0.6753246753246753
    required                        >= 0.70
    result                          FAIL

    known sensitivity witnesses     3 / 3 reviewer A
                                    3 / 3 reviewer B
    result                          PASS

    negative-control units          0 reviewer A
                                    0 reviewer B
    result                          PASS

    realization-state fixtures      7 / 7
    result                          PASS

The frozen harness therefore returns:

    DRP03=AMEND

No threshold is weakened and no failed criterion is retrospectively waived.

## 2. The AMEND is decision-relevant even without the false-gap submetric

DRP-03 asked whether acceptance-postflight ObligationDeclarationSet generation can close KA-R52's upstream blind spot **without arbitrary or noisy decomposition**.

The answer for free-form retrospective reconstruction from accepted prose is no.

Two independently authored reviews differed substantially:

    reviewer A units                97
    reviewer B units                60

    proposition-set F1              0.4983
    grouping F1                     0.6753

The proposition disagreement is broad rather than localized.

Per-source proposition F1:

    Research 272                    0.718
    Research 256                    0.583
    Research 235                    0.400
    Research 225                    0.333
    Research 217                    0.432
    Specification 028              0.469
    Research 259                    0.095
    Research 311                    0.684

Therefore the target architecture must not depend on a future agent reconstructing the authoritative ObligationDeclarationSet later from free prose.

This is exactly the kind of upstream blind spot KA-R52 is intended to remove.

## 3. What did work

The failed reproducibility result does not invalidate every V0.3 obligation concept.

Both reviewers independently surfaced all three preregistered material witnesses:

    W_SPEC028_SECTION3_NAMED_RESPONSIBILITY_GAP
    W_AO6_BRANCH_ROTATION_ATTACH_GAP
    W_R311_ENGINEERING_NO_MUST

Both reviewers also produced zero obligation units from the two negative-control research artifacts.

This supports two important conclusions:

    semantic obligation detection must not be reduced to uppercase MUST scanning

and:

    a research artifact that discusses a candidate requirement must not
    automatically become an accepted obligation source

The fully derived realization-state model also remains supported.

All seven frozen state fixtures derive the expected state:

    UNLINKED
    LINKED
    EVIDENCED
    QUALIFIED
    OPERATIONAL
    DEFERRED
    DEFERRED with deferral precedence

Therefore:

    REALIZATION_STATE_FULLY_DERIVED=RETAIN

No hand-maintained EVIDENCED / QUALIFIED / OPERATIONAL status is reintroduced.

## 4. False-gap specificity submetric defect

The result file reports:

    Claude reviewer A false-gap rate    0.70
    ChatGPT reviewer B false-gap rate   0.00

The 0.70 value must **not** be interpreted as evidence that Claude actually classified seven already-realized W0/W1 obligations as unrealized.

The hidden evaluator key attempted to locate ten false-gap controls by matching reviewer-written proposition text.

Claude represented the W0 gate set semantically as:

    W0 is accepted only when PKA-G001 through PKA-G017 all pass.

and W1 similarly as:

    PKA-G101 through PKA-G109 must pass.

Those units were correctly derived OPERATIONAL.

However, the hidden key searched for seven individual gate descriptions such as G006, G007 and G106.

Because Claude grouped the accepted gate family instead of restating each gate in the expected wording, FG01-FG07 returned:

    derived_state = null

The evaluator then counted each null textual match as a false gap.

FG08-FG10, whose W2-W4 propositions were represented individually, all resolved OPERATIONAL.

Therefore:

    DRP03_FALSE_GAP_TEXT_MATCHER_FOR_REVIEWER_A
        = NOT_DECISION_USABLE

This is a probe-methodology defect: specificity controls were accidentally coupled to reviewer wording/granularity instead of stable semantic gate identity.

It does not turn the entire attempt into HARNESS_INVALID because the AMEND result is independently determined by two other frozen primary criteria:

    proposition F1 0.4983 < 0.85
    grouping F1    0.6753 < 0.70

Removing the defective specificity submetric cannot change the run from AMEND to PASS.

The original result remains immutable evidence.

## 5. Architecture diagnosis

V0.3 was directionally correct that obligations should be born at acceptance.

DRP-03 shows that the mechanism was still underspecified.

The weak interpretation would be:

    acceptance happens
        ->
    later model scans accepted carrier
        ->
    model invents proposition boundaries
        ->
    model invents unit grouping
        ->
    resulting units become authoritative

DRP-03 falsifies that as a sufficiently deterministic professional mechanism.

The stronger model is:

    proposal/change package
        ->
    bounded normative delta is identified while the change is being authored
        ->
    materially ambiguous boundaries are resolved as part of the governing act
        ->
    owner/governance acceptance
        ->
    acceptance postflight validates and persists the exact accepted delta
        ->
    realization references/evidence accumulate
        ->
    RealizationState is derived

In other words:

    obligation birth
        must be attached to the acceptance event

not:

    obligation authority
        reconstructed later from prose

## 6. V0.4 candidate: AcceptanceDelta + ObligationDeclarationSet

The V0.4 candidate retains the V0.3 ObligationDeclarationSet name but strengthens its provenance and birth semantics.

Every governed acceptance event must resolve exactly one of:

    ObligationDeclarationSet
        one or more accepted ObligationUnits

or:

    CREATES_NO_OBLIGATION_UNITS

The declaration set is bound to:

    governing acceptance identity
    exact accepted subject
    exact accepted source/revision
    exact accepted normative delta
    declaration-set revision

Each ObligationUnit has at least:

    stable obligation identity
    exact accepted proposition reference(s)
    responsible semantic owner
    one realization boundary
    one expected evidence path
    activation/effective boundary
    relation to predecessor/successor obligation where applicable

The authoritative proposition reference should point to the accepted normative delta or stable accepted clause identity.

Free-form paraphrase is explanatory metadata, not the identity of the obligation.

## 7. Normative delta is generated during the change, not rediscovered after history

The control plane should exploit information naturally available at the acceptance boundary.

For mediated governing changes:

    candidate governing change
        ->
    exact semantic/content delta
        ->
    NormativeDeltaCandidate
        ->
    obligation-unit proposal
        ->
    ambiguity review where consequential
        ->
    governing acceptance
        ->
    acceptance postflight validates/persists ObligationDeclarationSet
        ->
    dependent advancement

The owner should not manually maintain a requirements database.

The system drafts the delta and units from the actual change package.

The owner or responsible authority is involved only when the unit boundary changes normative meaning or realization consequences.

For a MEDIATED path, downstream consequential advancement may be held until the declaration set is valid.

For a COOPERATIVE or UNMEDIATED acceptance event:

    valid authority event remains valid
        ->
    immediate postflight recovery of the normative delta
        ->
    declaration candidate
        ->
    REVIEW_REQUIRED when material unit boundaries are ambiguous
        ->
    KA-R51 observation if declaration was absent at acceptance

Missing bookkeeping still does not retroactively erase a valid owner/governance decision.

## 8. Legacy accepted history has different semantics

Historical carriers predate the proposed acceptance-birth mechanism.

DRP-03 demonstrates that retrospective extraction is not equivalent to authoritative birth.

Therefore legacy migration must use:

    frozen accepted source/revision
        ->
    deterministic candidate clause segmentation
        ->
    candidate normative selection
        ->
    candidate unit grouping
        ->
    governed reconciliation
        ->
    accepted legacy ObligationDeclarationSet

Until reconciled:

    RETROSPECTIVE_EXTRACTED_UNIT
        = CANDIDATE

not:

    RETROSPECTIVE_EXTRACTED_UNIT
        = AUTHORITATIVE_OBLIGATION

Material reviewer disagreement becomes REVIEW_REQUIRED evidence.

This prevents migration machinery from silently rewriting what earlier owner decisions meant.

## 9. Derived realization semantics remain unchanged

Once an obligation identity exists, realization state remains computed from source-owned facts.

Candidate derivation remains:

    explicit governed deferral
        -> DEFERRED

    no valid realization relation and no valid deferral
        -> UNLINKED

    realization relation but no qualifying evidence
        -> LINKED

    required evidence present but qualification incomplete
        -> EVIDENCED

    qualification complete but required activation/effect absent
        -> QUALIFIED

    valid realization + evidence + qualification + activation
        -> OPERATIONAL

No domain author writes RealizationState directly.

Disagreement or stale/contradictory source facts should yield REVIEW_REQUIRED rather than fabricated certainty.

## 10. Secondary normative scan remains a detector, not authority

V0.3's secondary normative-language scan is retained and clarified.

It may detect:

    accepted normative source item not represented in the declaration set
    accepted change with missing declaration set
    suspicious mismatch between declaration and source delta

Its output is:

    REVIEW
    or
    CONTROL_OBSERVATION

It must not silently mint authoritative obligations from language patterns.

This remains important because Research 311's accepted Engineering constraints demonstrate that normative obligations can exist without uppercase MUST.

## 11. DRP-03 R2 measurement amendment

The original DRP-03 evidence and thresholds are not rewritten.

A requalification attempt is required after the V0.4 amendment is challenged.

R2 should preserve the intent of the original thresholds while correcting the discovered measurement coupling.

The candidate R2 method is:

1. freeze exact source revisions before reviewer work;

2. freeze deterministic **source-item identifiers** for candidate normative clauses/items without labeling them as obligations;

3. reviewers independently decide which source items are normative and independently group selected item IDs into ObligationUnits;

4. proposition-selection agreement is scored over source-item IDs rather than reviewer paraphrase similarity;

5. grouping agreement is scored over the same matched source-item IDs;

6. already-realized specificity controls bind to stable gate/item IDs such as PKA-G006 rather than expected reviewer wording;

7. the same three material sensitivity witnesses remain required;

8. the same negative-control behavior remains required;

9. fully derived state fixtures remain required;

10. the original strict thresholds are retained unless a new preregistration independently justifies a stronger threshold.

This tests semantic selection and grouping rather than prose style.

It also better approximates the proposed future mechanism, where accepted propositions have stable references.

## 12. Why V0.4 is not a universal requirements database

The amendment does not select:

    one central requirements file
    one SQL requirements database
    broad event sourcing
    universal IDs for every sentence
    one obligation unit per MUST
    one obligation unit per bullet
    manual owner bookkeeping

The declaration set is an acceptance-boundary semantic artifact.

Its persistent representation remains a later representation decision subject to WMR-H, DRP-08 adoption economics and the no-preservation-right principle.

## 13. Consequence for downstream probes

DRP-07 depends on DRP-03 obligation semantics.

Therefore DRP-07 must not treat the failed free-form retrospective unit boundaries as the final canonical unit map.

The Specification 028 lineage program may continue only after DRP-03's amendment is reconciled sufficiently to freeze the lineage-unit identification method.

DRP-04 may still study KA-R51 detector behavior independently where its fixture does not depend on disputed ObligationUnit boundaries.

DRP-08 must include the authoring/maintenance cost of the strengthened acceptance-delta mechanism.

## 14. Current disposition

    DRP09=PASS
    DRP05A=PASS
    DRP05B=PASS_DETECTIVE_FIRST
    DRP01=PASS
    DRP03=AMEND

    DRP03_PROPOSITION_F1=0.49829351535836175
    DRP03_GROUPING_F1=0.6753246753246753

    DRP03_WITNESS_SENSITIVITY=PASS
    DRP03_NEGATIVE_CONTROLS=PASS
    DRP03_DERIVED_STATE_FIXTURES=PASS

    DRP03_REVIEWER_A_FALSE_GAP_TEXT_SUBMETRIC=NOT_DECISION_USABLE
    DRP03_PRIMARY_AMEND_REMAINS_VALID=true

    OBLIGATION_BIRTH=ACCEPTANCE_BOUNDARY_STRENGTHENED_CANDIDATE
    RETROSPECTIVE_FREE_FORM_EXTRACTION=NOT_AUTHORITY
    REALIZATION_STATE=FULLY_DERIVED_RETAINED

    V04=PROSPECTIVE_CANDIDATE
    OWNER_DECISION=NOT_READY
    DRP03_R2=REQUIRED_AFTER_RECONCILIATION

    AO10_PRODUCTION_IMPLEMENTATION_AUTHORIZED=false
    AO10_SHADOW_ACTIVATION_AUTHORIZED=false
    PHYSICAL_MIGRATION_AUTHORIZED=false
    CURRENT_ORACLE_RETIREMENT_AUTHORIZED=false
    AUTHORITY_SWITCH_ALLOWED=false

    NEXT=CLAUDE_ADVERSARIAL_CRITIQUE_OF_DRP03_AMENDMENT_AND_R2_METHOD
