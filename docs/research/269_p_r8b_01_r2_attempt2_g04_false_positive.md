# Research 269: P-R8B-01-R2 Attempt 2 Result, G04 False Positive, and Harness-Invalid Classification

**Date:** 2026-09-23
**Status:** ATTEMPT 2 HARNESS_INVALID / 17 OF 18 BLOCKING GATES PASS / 2 OF 2 AMENDMENT GATES PASS / G04 FALSE POSITIVE / NO OWNER REPRESENTATION DECISION
**Parent protocol:** Research 266
**Replacement freeze:** Research 268
**Frozen harness commit:** a893e7e904e29ca91491108bd816d4af06dba6c1
**Probe:** P-R8B-01-R2
**Candidate:** WMR-H V0.3
**Scope:** Preserve the second corrected-run evidence, classify the sole reported blocking failure, and distinguish a harness false positive from an architecture-relevant failure without weakening the original Research 263 threshold.
**Authority:** Empirical result classification only. No architecture acceptance, Specification 028 amendment, AO-10 authorization, or physical migration.

## 1. Observed result

Attempt 2 completed the full harness and produced:

    blocking gates       17 / 18 PASS
    amendment gates       2 / 2 PASS
    reported overall      AMEND_REQUIRED

The sole reported blocking failure was:

    G04
        ProbeFailure: transition-owned current fact leaked into definition: 'PAUSED'

All other corrected blocking gates passed, including the seven gates Claude had classified INVALID in the original harness after their corrected implementations were introduced.

Durable evidence:

    experiments/r8b_representation_probe_v02/evidence/run_002/

## 2. Frozen-input integrity

The result binds itself to:

    HASH_BASIS=GIT_BLOB_BYTES_AT_COMMIT
    HARNESS_COMMIT=a893e7e904e29ca91491108bd816d4af06dba6c1

and records the exact Research 268 Git-blob SHA-256 values.

The real-source hashes also match Research 268 exactly.

No threshold or candidate was modified before the run.

## 3. Why G04 is a harness false positive

Research 263 G04 requires the six **current transition-owned facts** to be absent from the human definition and present in machine state.

The candidate human definition contains:

    A PAUSED state is routing and does not by itself mean completion or supersession.

This is a durable statement about the semantics of the PAUSED state class.

It is not the current factual assertion:

    current workstream state = PAUSED

The G04 implementation searched for the raw value string PAUSED anywhere in the definition. Therefore it conflated:

    state vocabulary / durable semantic explanation

with:

    current transition-owned state assertion

The implementation is stricter than, and semantically different from, the preregistered criterion.

A human definition must be allowed to explain what a PAUSED state means without thereby becoming the owner of the current state.

Therefore the reported G04 failure is not evidence against the definition/state split.

## 4. Threshold remains unchanged

The blocking threshold is not weakened.

It remains:

    current workstream state
    current pause reason
    current return condition
    current resume target
    SOURCE-VAULT:INGESTION milestone state
    COURSE:2 milestone state

must not be canonically asserted as current truth in the human definition.

The corrected detector must test **current assertions**, not ban the vocabulary tokens themselves.

## 5. Required prospective correction

The repaired G04 implementation must:

    inspect governed metadata for forbidden transition-state ownership

    detect current-state assertions such as:
        workstream state = PAUSED
        current state = PAUSED
        **Status:** PAUSED
        equivalent explicit current-state forms

    detect exact current pause_reason text

    detect exact current return_condition text

    detect exact current resume_target text

    detect the current milestone assertions:
        source ingestion = NOT_STARTED
        Course 2 = BLOCKED

    permit durable generic semantics such as:
        "A PAUSED state is routing..."

A negative-control candidate must inject all six current assertions and the detector must find all six.

The real converted definition must produce:

    detected current transition-owned assertions = 0

This preserves the original six-fact threshold while making the gate semantic rather than token-based.

## 6. Evidence from all other corrected gates

Attempt 2 materially strengthens the architecture evidence:

    G05
        real file transition
        Git-measured definition diff = zero
        co-located negative control produces nonzero definition diff

    G08
        revision-only/decrement/same/skipped revisions rejected
        invalid merge revision rejected
        no-op validator controls detected
        valid committed merge history accepted
        corrupted committed history rejected

    G10
        file-backed capture/review/promotion
        capture and receipt bytes unchanged

    G13
        rule-based real Specification 028 conversion
        lifecycle frozen
        all declared references/provenance accounted for
        non-metadata content preserved

    G16
        derivatives materialized then deleted
        anchor-only recovery succeeds
        generated-only negative locator fails visibly

    G17
        actual framework files replaced
        compatible instance validates
        incompatible instance returns migration_required
        instance bytes unchanged

    G18
        Git-computed review shapes pass

The strengthened weak gates G02/G09/G15 also pass.

AM1-G1 and AM2-G1 both pass.

## 7. Classification

Because the only blocking failure is caused by a demonstrated mismatch between the gate implementation and its preregistered semantic criterion:

    P_R8B_01_R2_ATTEMPT_2=HARNESS_INVALID

rather than:

    ARCHITECTURE_AMEND_REQUIRED

The run remains durable evidence for every gate it validly exercised.

A prospective G04 repair and new freeze are required before a final confirmatory result.

## 8. Current state

    ATTEMPT_2_REPORTED_OVERALL=AMEND_REQUIRED
    ATTEMPT_2_CLASSIFIED=HARNESS_INVALID
    BLOCKING_GATES_PASS=17_OF_18
    AMENDMENT_GATES_PASS=2_OF_2
    SOLE_FAILURE=G04_FALSE_POSITIVE

    THRESHOLDS_CHANGED=false
    CANDIDATE_CHANGED=false
    OWNER_REPRESENTATION_DECISION=HELD

    SPECIFICATION028=UNCHANGED
    AO10=HELD
    FILE_LEVEL_MIGRATION=HELD
    PHYSICAL_MIGRATION_AUTHORIZED=false
    NEXT=PROSPECTIVE_G04_REPAIR_AND_REFREEZE
