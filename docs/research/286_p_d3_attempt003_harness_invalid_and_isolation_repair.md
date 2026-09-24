# Research 286: P-D3 Attempt 003 Harness Invalid and Isolation Repair

**Date:** 2026-09-24
**Status:** P-D3 ATTEMPT 003 HARNESS_INVALID / NO ARCHITECTURE INFERENCE / NARROW CHILD-INTERPRETER ISOLATION REPAIR REQUIRED
**Parent protocol:** Research 277
**Prior harness history:** Research 281 through Research 285
**Probe:** P-D3
**Attempt:** 003
**Scope:** Preserve the third invalid P-D3 execution, identify the child-interpreter isolation defect, and authorize only the repair needed to make absence execution actually remove ambient repository packages.
**Authority:** Harness-failure record and narrow prospective repair authorization only.

## 1. Attempt 003 binding

    HARNESS_COMMIT
        374c64ee069cb690c1d5b7108ffbf2cfd83c9c5d

    SOURCE_COMMIT
        721545c46b94e0a87c87a572fb357ff314f6913f

The harness was frozen in Research 285 before execution.

## 2. Observed failure

Attempt 003 progressed beyond both prior harness defects.

The Product forbidden-dependency control behaved as intended.

The JW1 forbidden-dependency control did not.

The target-shaped JW1 fixture had:

    import ads_system

appended to the copied JW1 module.

The child process was launched with the repository virtual-environment Python using:

    -I

but not:

    -S

Therefore the interpreter still admitted virtual-environment site-packages.

The installed/editable ADS Product package made:

    import ads_system

succeed even though the target-shaped fixture itself contained no Product package.

The negative control therefore did not establish the intended absence condition.

## 3. Classification

    P_D3_ATTEMPT_003=HARNESS_INVALID

This is an isolation defect in the probe environment.

No Product/JW1 architecture inference is permitted.

    TARGET_ARCHITECTURE_INFERENCE=NONE
    WARRANT_F_V0_2_AMENDMENT_REQUIRED=false
    THRESHOLDS_CHANGED=false

Durable evidence:

    experiments/r8c_assurance_probe_v01/evidence/
        p_d3_run_003_harness_invalid.json

## 4. Narrow prospective repair

The authorized repair is only:

    child interpreter
        PREVIOUS:
            python -I -c ...

        REPAIRED:
            python -I -S -c ...

The purpose of:

    -S

is to suppress site initialization/site-packages so the child sees only:

    standard library
    explicitly inserted temporary fixture path

This changes the harness environment, not the architecture criterion.

No change is authorized to:

    source commit
    representative Product behavior
    representative JW1 behavior
    target-shaped layout
    static scan
    forbidden imports
    result thresholds
    result-class semantics
    architecture interpretation

## 5. Required next sequence

    repair run_child() only
    validate syntax/integrity without executing P-D3
    commit and push
    compute Git-blob hashes
    refreeze
    execute Attempt 004

Attempts 001 through 003 remain preserved as HARNESS_INVALID.

## 6. Current state

    P_D3_ATTEMPT_001=HARNESS_INVALID
    P_D3_ATTEMPT_002=HARNESS_INVALID
    P_D3_ATTEMPT_003=HARNESS_INVALID
    VALID_P_D3_RESULT=NONE

    REPAIR_SCOPE=ADD_-S_CHILD_ISOLATION_ONLY
    COMPLETED_VALID_DECISION_PROBES=2_OF_8
    OWNER_ASSURANCE_DECISION=HELD
    PHYSICAL_MIGRATION_AUTHORIZED=false
    NEXT=REPAIR_REFREEZE_P_D3_ATTEMPT004
