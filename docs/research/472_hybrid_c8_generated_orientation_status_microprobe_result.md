# Research 472: HYBRID C8 generated orientation/status micro-probe result

**Date:** 2026-10-03
**Status:** C8_ORIENTATION_MECHANISM_PLAUSIBLE / C9 OWNER-BURDEN PROBE NEXT
**Protocol:** Research 470
**Implementation freeze:** Research 471
**Frozen implementation commit:** e162d931172b004b3ece7cf2a025c482400d72d6
**Result artifact:** experiments/ao10_hybrid_c8_orientation_v01/result.json
**Result SHA-256:** 3b25657885fbe27e40414e4e1fa31c66fe7041af79f9078edab08dc92e49b03e
**Scope:** Record the single frozen HYBRID_C8_ORIENTATION_V01 execution and update the thin-centred hybrid successor hypothesis.
**Authority:** Development evidence only. This result does not select production architecture, amend Specification 028, expose hidden R2 material, resume dependent DRPs, migrate repository state, or switch authority.

## 1. Frozen execution result

The single authorized execution returned:

    fixture_total                 11
    all_match                     true
    evaluators_agree_all          true
    aggregate_matches             true
    reported_state_ignored        true
    outcome                       C8_ORIENTATION_MECHANISM_PLAUSIBLE

Both separately encoded evaluators matched every frozen expected output exactly.

No fixture, expected output or implementation rule was changed after execution.

## 2. Compact shared projection

The probe supports a generated realization-orientation projection with only four top-level states:

    REVIEW_REQUIRED
    DEFERRED
    OPEN
    SATISFIED

and one orthogonal next-gap field:

    REVIEW
    COVERAGE
    EVIDENCE
    QUALIFICATION
    ACTIVATION
    NONE

This preserves the action-relevant distinctions tested by the fixtures without turning evidence, qualification and activation milestones into independently authored global lifecycle truth.

## 3. Open requirements stay one state

The following old V0.5-like distinctions are represented as one OPEN state plus a source-derived next gap:

    no/partial coverage
        -> OPEN / COVERAGE

    coverage complete, evidence missing
        -> OPEN / EVIDENCE

    evidence valid, qualification incomplete
        -> OPEN / QUALIFICATION

    qualification complete, activation missing
        -> OPEN / ACTIVATION

This is materially smaller than maintaining separate authoritative UNLINKED / LINKED / EVIDENCED / QUALIFIED labels.

The underlying evidence, qualification and activation facts remain owned by their natural domains.

## 4. REVIEW_REQUIRED precedence

Invalid source facts, contradictions and invalid deferral facts deterministically produce:

    REVIEW_REQUIRED / REVIEW

before any progress-state rule can apply.

The aggregate attention list is generated directly from this projection.

Observed aggregate:

    state_counts
        DEFERRED            1
        OPEN                6
        REVIEW_REQUIRED     3
        SATISFIED           1

    open_gap_counts
        COVERAGE            3
        EVIDENCE            1
        QUALIFICATION       1
        ACTIVATION          1

    attention_required_ids
        R-O10
        R-O8
        R-O9

## 5. Deferral remains governed

A valid governed deferral produces:

    DEFERRED / NONE

An invalid deferral produces:

    REVIEW_REQUIRED / REVIEW

The projection does not infer deferral from a generic hold.

This preserves the earlier distinction between a governed deferral and an incidental program/workstream hold.

## 6. Reported state has no authority

O11 supplied:

    reported_state=OPERATIONAL

while source facts still had incomplete coverage.

Both evaluators returned:

    OPEN / COVERAGE

Therefore:

    reported/authored realization state
        != governing operational truth.

The source facts and deterministic rule own the generated projection.

## 7. Governing lifecycle remains separate

C8 deliberately does not fold:

    superseded
    retired
    historical
    candidate
    blocked
    paused
    migration phase

into realization orientation.

C7/governing-lifecycle resolution determines which requirement identities are current and active.

C8 then projects realization progress for that current active set.

## 8. Relation to historical DRP-06

This is not a DRP-06 PASS.

It qualifies only the realization-status subprojection that a later bounded orientation fixture may consume.

The historical DRP-06 questions about:

    fresh-session current-state correctness
    whole-payload size
    repository reads/tool actions
    authority/current-boundary fidelity

still require later confirmation after the successor semantic architecture is stable.

## 9. Current successor mechanism after C4-C8

The leading thin-centred hybrid now has mechanism-level support for:

    C4  one stable REQUIRE identity per independently acceptable governing effect
    C5  completion criteria owned by governing acceptance or accepted domain contract
    C6  deterministic bounded multi-artifact completion
    C7  governed N:M requirement lineage and explicit retirement
    C8  compact generated realization orientation

The remaining explicit comparison item from Research 463 is:

    C9  owner burden for the surviving richer acceptance metadata.

C9 must not ask the owner to judge implementation internals.

It should test only whether the additional acceptance-time information now required by the hybrid can be reviewed as part of the same governing meaning review without disproportionate burden.

## 10. Current disposition

    C4=MECHANISM_PLAUSIBLE
    C5=MECHANISM_PLAUSIBLE
    C6=MECHANISM_PLAUSIBLE
    C7=LINEAGE_MECHANISM_PLAUSIBLE
    C8=ORIENTATION_MECHANISM_PLAUSIBLE

    LEADING_CANDIDATE=THIN_CENTRED_HYBRID
    PRODUCTION_TARGET_SELECTED=false

    HIDDEN_R2_DETAILS=SEALED

    NEXT=FREEZE_HYBRID_C9_OWNER_BURDEN_PROTOCOL
