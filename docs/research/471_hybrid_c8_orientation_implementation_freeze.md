# Research 471: HYBRID C8 orientation implementation freeze

**Date:** 2026-10-03
**Status:** IMPLEMENTATION FROZEN / SINGLE EXECUTION NEXT
**Protocol:** Research 470
**Protocol commit:** 80b80fed246f58dec389747d83b2b545e67a3fe8
**Implementation root:** experiments/ao10_hybrid_c8_orientation_v01
**Manifest SHA-256:** 7137a3bacc9449dc73e6b158c43fd787614c44da17690e15eae0c974307027c8
**Scope:** Freeze the exact C8 orientation harness before business-rule execution.
**Authority:** Development implementation freeze only. This record does not select production architecture, amend Specification 028, expose hidden R2 material, resume dependent DRPs, migrate repository state, or switch authority.

## 1. Frozen implementation

The pre-result implementation contains:

    definitions.json
    fixtures.json
    evaluator_a.py
    evaluator_b.py
    run_comparison.py
    static_validate.py
    manifest.json

The manifest binds the six pre-result business/fixture files by exact SHA-256 and byte count.

The manifest itself hashes to:

    7137a3bacc9449dc73e6b158c43fd787614c44da17690e15eae0c974307027c8

No result.json exists at freeze time.

## 2. Frozen fixture count

    orientation fixtures      11
    evaluators                 2

Expected per-fixture and aggregate outputs are embedded in fixtures.json and may not change after execution.

## 3. Evaluator separation

Evaluator A implements the frozen ordered decision tree directly.

Evaluator B constructs normalized predicates and selects state/gap through independent priority tables.

They share fixture parsing only and do not call one another's business-rule functions.

This is code-path independence, not independent-author confirmation.

## 4. Static-only preflight

Observed before freeze:

    HYBRID_C8_STATIC_VALIDATION=PASS

The static validator checked:

    probe identity
    exact top-level vocabulary
    exact fixture count
    fixture-ID uniqueness
    Python syntax for both evaluators and the runner
    absence of result.json

It did not import or execute either evaluator.

## 5. Frozen projection

The top-level generated realization state is exactly:

    REVIEW_REQUIRED
    DEFERRED
    OPEN
    SATISFIED

The orthogonal next-gap values are exactly:

    REVIEW
    COVERAGE
    EVIDENCE
    QUALIFICATION
    ACTIVATION
    NONE

No reported/authored realization-state field is consumed by the derivation.

Governing lifecycle remains separate.

## 6. Execution rule

Exactly one normal business-rule execution is authorized against these frozen files.

If execution exposes a defect:

    preserve the observed result;
    do not change fixtures or evaluators and silently rerun;
    classify under Research 470 outcome rules.

## 7. Current boundary

    IMPLEMENTATION=FROZEN
    MANIFEST_SHA256=7137a3bacc9449dc73e6b158c43fd787614c44da17690e15eae0c974307027c8
    RESULT_EXISTS=false
    HIDDEN_R2_DETAILS=SEALED
    OWNER_PARTICIPATION_REQUIRED=false

    NEXT=EXECUTE_HYBRID_C8_ORIENTATION_V01_ONCE
