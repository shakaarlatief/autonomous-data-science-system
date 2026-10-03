# Research 465: HYBRID C4-C6 implementation freeze

**Date:** 2026-10-03
**Status:** IMPLEMENTATION FROZEN / SINGLE EXECUTION NEXT
**Protocol:** Research 464
**Protocol commit:** 6cc806fb69c2d6e35edffaf8aaef3cc5df540e5b
**Implementation root:** experiments/ao10_hybrid_c4_c6_v01
**Manifest SHA-256:** a40352df2216127fcbd18e3589115bb3fac2a56c68e633a68e8b8971ee3cbef4
**Scope:** Freeze the exact C4-C6 development harness before business-rule execution.
**Authority:** Development implementation freeze only. This record does not select production architecture, amend Specification 028, expose hidden R2 material, resume dependent DRPs, migrate repository state, or switch authority.

## 1. Frozen implementation

The implementation contains seven pre-result files plus the manifest:

    definitions.json
    granularity_fixtures.json
    completion_fixtures.json
    evaluator_a.py
    evaluator_b.py
    run_comparison.py
    static_validate.py
    manifest.json

The manifest binds each pre-result file by exact SHA-256 and byte count.

The manifest itself hashes to:

    a40352df2216127fcbd18e3589115bb3fac2a56c68e633a68e8b8971ee3cbef4

No result.json exists at freeze time.

## 2. Frozen fixture counts

    granularity fixtures      4
    completion fixtures      10
    evaluators                2

The expected outputs are already embedded in the frozen fixture files.

They may not be changed after business-rule execution.

## 3. Evaluator separation

Evaluator A uses straightforward procedural validation and set accumulation.

Evaluator B uses separately encoded normalized set/relation logic.

They share only the frozen structured fixture files.

They do not call one another's business-rule functions.

This is code-path separation, not independent-author confirmation.

## 4. Static-only preflight

Before freeze, only static validation was executed.

Observed:

    HYBRID_C4_C6_STATIC_VALIDATION=PASS

The static validator checked:

    probe identity
    fixture counts
    fixture-ID uniqueness
    Python syntax for both evaluators and the comparison runner
    absence of result.json

It did not import either evaluator and did not execute the business rules.

## 5. Frozen anti-self-certification behavior

The implementation does not consume realizer self_assessment when computing:

    completion_contract_valid
    coverage_complete
    requirement_satisfied

The frozen P4 case therefore tests that a realizer reporting FULL while covering only component A cannot satisfy an A+B criterion.

The frozen P5 case separately tests attempted realizer replacement of the completion criterion itself.

## 6. Frozen completion semantics

For this probe only:

    accepted completion-contract authority
        = GOVERNING_ACCEPTANCE
          OR ACCEPTED_DOMAIN_CONTRACT

    composition
        = ALL_REQUIRED

    coverage closure
        = union of valid declared component coverage
          exactly covers every required component
          with no unknown component

    completion
        additionally requires valid evidence,
        required qualification,
        required activation,
        active requirement,
        and no conflict.

No free-text field is consumed by either evaluator.

## 7. Execution rule

Exactly one normal business-rule execution is authorized against these frozen files.

If that execution exposes an implementation defect:

    do not repair and silently rerun;
    record the observed result;
    classify under the Research 464 outcome rules.

## 8. Current boundary

    IMPLEMENTATION=FROZEN
    MANIFEST_SHA256=a40352df2216127fcbd18e3589115bb3fac2a56c68e633a68e8b8971ee3cbef4
    RESULT_EXISTS=false
    HIDDEN_R2_DETAILS=SEALED
    OWNER_PARTICIPATION_REQUIRED=false

    NEXT=EXECUTE_HYBRID_C4_C6_V01_ONCE
