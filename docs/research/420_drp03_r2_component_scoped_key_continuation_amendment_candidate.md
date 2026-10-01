# Research 420: DRP-03 R2 Component-Scoped Key Continuation Amendment Candidate

**Date:** 2026-10-01
**Status:** AMENDMENT CANDIDATE / OWNER DECISION REQUIRED / NO EXECUTION AUTHORIZED
**Parent:** Research 419
**Scope:** Define the narrowest prospective continuation rule that preserves the failed Key Author A LEGACY result while allowing independently valid BIRTH and STATE work to continue without semantic retry-to-green.
**Authority:** Candidate protocol amendment only. This record does not authorize P6C, semantic reruns, canonical full-key assembly, any commitment, Key Author B execution, construct comparison, reviewer scoring, successor implementation, migration, oracle retirement, or authority switching.

## 1. Problem to solve

Research 419 establishes a genuine interaction between accepted rules:

    Research 330
        BIRTH, STATE, LEGACY independently classified
        LEGACY does not gate BIRTH/STATE owner-decision readiness

    Research 332
        monolithic Key A commitment precedes Key B

    Research 410
        failed LEGACY evidence qualification stops before Key A commitment

The observed Key A P6B result is:

    material-gap witness floor = PASS
    already-realized false-gap floor = PASS
    negative-control source check = FAIL
    P6B finalization = EVIDENCE_INSUFFICIENT

No semantic retry or repair is allowed.

A literal whole-sequence stop would therefore make a failed candidate-only LEGACY component prevent BIRTH/STATE dual-key construct validation, contradicting the intended component consequence separation.

## 2. Amendment objective

The amendment must do only one thing:

    prevent failed LEGACY key construction from becoming an accidental procedural gate
    on otherwise independent BIRTH and STATE qualification

It must not:

    convert LEGACY to PASS
    change any Key A label
    complete Key A LEGACY grouping after the stop
    rerun any P5/P6 semantic work
    change a negative-control source
    change a threshold
    widen the historical corpus
    expose Key A output to Key B
    weaken reviewer concealment

## 3. Frozen disposition of Key Author A LEGACY

If this amendment is accepted, the current historical Key A LEGACY branch is terminal:

    KEY_A_LEGACY_KEY_CONSTRUCTION = INCONCLUSIVE
    reason = FROZEN_NEGATIVE_CONTROL_CHECK_FAILURE

The exact private P5/P6A/P6B artifacts remain preserved.

P6C remains:

    NOT_RUN

No future same-corpus continuation may fill in the missing P6C grouping and then claim the original Key A LEGACY component completed normally.

The LEGACY consequence remains:

    no qualified obligation-unit lineage
    no legacy migration/reconciliation authority
    no oracle-retirement use that depends on qualified LEGACY units

This preserves the unfavorable result rather than repairing it.

## 4. Component-scoped commitment model

The current all-components commitment sequence is amended only for a component that has already reached a terminal non-qualifying outcome.

A key-author commitment may bind a canonical component bundle rather than requiring every R2 component to be complete.

For the present run, the allowed Key A bundle is:

    STATE
    BIRTH classification
    BIRTH grouping

Excluded from the qualifying bundle:

    LEGACY

The component-scoped commitment must bind:

    protocol ID
    public-freeze digest
    key-author identity/provenance
    exact included component set
    exact canonical bytes for those components
    canonical serialization identifier
    exact byte length
    SHA-256
    within-rater quality results applicable to included components
    explicit excluded-component status
        LEGACY = INCONCLUSIVE / NEGATIVE_CONTROL_CHECK_FAILURE

The commitment is cryptographic immutability evidence, not a claim that the excluded component passed.

## 5. Key Author B scope and blindness

After a valid Key A component-scoped commitment is frozen, a fresh Key Author B may be authorized for the same qualifying component set:

    STATE
    BIRTH

Key B must remain blind to:

    Key A labels
    Key A groupings
    Key A outputs
    Key A transcripts
    Key A commitment contents beyond the public non-secret existence needed by orchestration
    the private reason or item identities underlying the Key A LEGACY failure

Key B does not receive the Key A workspace.

Key B need not perform historical LEGACY authoring in this attempt because the historical LEGACY component is already terminal and non-qualifying under this amendment.

This avoids generating post-result semantic work solely to complete a component that cannot become qualifying in the same historical attempt.

## 6. Construct-validity comparison after the amendment

Construct-validity comparison proceeds only over components for which both key authors have frozen qualifying commitments:

    STATE
    BIRTH

The existing preregistered agreement gates remain unchanged.

No LEGACY agreement statistic is silently treated as passing, missing-at-random, or equivalent to zero disagreement.

Instead:

    HISTORICAL_R2_LEGACY_CONSTRUCT_VALIDITY = NOT_ESTABLISHED
    HISTORICAL_R2_LEGACY_COMPONENT = INCONCLUSIVE

This result remains visible in final R2 reporting.

## 7. Historical attempt accounting

This amendment does not create a second semantic attempt.

The already-observed Key A semantic outputs remain Attempt 1 evidence.

No held-out label, P5 label, candidate-gap label, evidence result, or grouping result is changed or regenerated.

Research 330's rule remains:

    same-corpus second attempt only for HARNESS_INVALID

The present result is not HARNESS_INVALID.

A future attempt to qualify LEGACY must therefore be a new prospective experiment or new protocol version with independently frozen conditions, not an extension or retry of the current historical R2 attempt.

## 8. Why this is narrower than whole-sequence termination

Whole-sequence termination is mechanically simple but would add a consequence that Research 330 explicitly rejected:

    LEGACY failure -> BIRTH/STATE owner-decision readiness blocked

The component-scoped amendment preserves the stronger existing consequence model:

    BIRTH and STATE decide architecture owner-decision readiness
    LEGACY independently gates legacy lineage/migration uses

It also preserves the failed LEGACY evidence rather than discarding it.

## 9. Why this is not retry-to-green

The amendment cannot improve the failed metric.

After acceptance:

    negative-control source check remains FAIL
    Key A LEGACY remains INCONCLUSIVE
    P6C remains NOT_RUN
    LEGACY migration authority remains blocked

Only unrelated components continue.

Therefore the amendment changes orchestration and commitment granularity, not observed semantic truth.

## 10. Required implementation work after owner acceptance

If accepted, implementation must occur prospectively and be qualified before Key B starts.

Required work:

    define canonical component-bundle serialization
    implement private component-scoped Key A assembly
    implement public-safe commitment emission
    mechanically verify included/excluded component sets
    preserve all existing private artifacts byte-for-byte
    verify Key B environment cannot read Key A storage
    instantiate the reusable BIRTH/STATE runner against the clean B root
    add regressions proving LEGACY exclusion cannot be misread as PASS
    add regressions proving a failed component cannot contaminate included-component bytes
    retain Research 348 Runtime-Bridge-only public repository operations

No Key B semantic session starts until these controls pass.

## 11. Owner decision

Recommended disposition:

    ACCEPT

Reason:

The amendment preserves every unfavorable observed fact, prohibits same-corpus semantic repair, maintains the frozen component consequence model, and prevents a candidate-only LEGACY failure from acquiring an unintended veto over BIRTH/STATE construct validity.

Alternative:

    REJECT

would retain whole-sequence termination, in which case historical R2 stops before Key B and BIRTH/STATE construct validity remains unevaluated despite their otherwise completed Key A work.

## 12. Boundary before owner decision

    RESEARCH420 = CANDIDATE
    OWNER_DECISION = REQUIRED

    KEY_A_LEGACY = EVIDENCE_INSUFFICIENT / FROZEN
    KEY_A_P6C = NOT_STARTED

    COMPONENT_SCOPED_KEY_COMMITMENT = NOT_AUTHORIZED
    KEY_AUTHOR_B = NOT_AUTHORIZED
    CONSTRUCT_COMPARISON = NOT_AUTHORIZED
    REVIEWER_SCORING = NOT_AUTHORIZED

    NEXT = OWNER_ACCEPT_OR_REJECT_COMPONENT_SCOPED_CONTINUATION
