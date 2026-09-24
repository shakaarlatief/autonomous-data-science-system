# Research 287: P-D3 Third Repair Refreeze for Attempt 004

**Date:** 2026-09-24
**Status:** P-D3 THIRD REPAIR FROZEN / ATTEMPT 004 NOT YET RUN / NO ARCHITECTURE RESULT YET
**Parent protocol:** Research 277
**Invalid attempts:** Research 282, Research 284, Research 286
**Probe:** P-D3
**Frozen repaired harness commit:** 542018f1290864bc7735c896a64f5aed5de48a76
**Frozen source commit:** 721545c46b94e0a87c87a572fb357ff314f6913f
**Hash basis:** GIT_BLOB_BYTES_AT_COMMIT
**Scope:** Freeze the prospectively repaired P-D3 harness after the narrowly authorized child-interpreter site-isolation change and before Attempt 004.
**Authority:** Repaired-fixture freeze only.

## 1. Repair applied

Research 286 authorized exactly:

    child execution
        from:
            python -I -c ...

        to:
            python -I -S -c ...

This removes ambient site-packages from the isolated child process so Product/JW1 absence tests are controlled only by the temporary fixture path plus the standard library.

No architecture criterion, source commit, representative behavior, static scan, forbidden import, result class or threshold changed.

## 2. Frozen harness binding

    experiments/r8c_assurance_probe_v01/README.md
        614967937244531c8b1cb8e4154f7e42f91b88f58bcd32120f31918ba1090fa4

    experiments/r8c_assurance_probe_v01/p_d3_boundary_independence.py
        7babd8dcaf7b61527c95ab6419383137375f0a62ac17f2191495a60f73531341

    HARNESS_COMMIT
        542018f1290864bc7735c896a64f5aed5de48a76

    SOURCE_COMMIT
        721545c46b94e0a87c87a572fb357ff314f6913f

## 3. Attempt history

    Attempt 001 = HARNESS_INVALID
    Attempt 002 = HARNESS_INVALID
    Attempt 003 = HARNESS_INVALID

All remain preserved.

## 4. Attempt 004 command

    .\.venv\Scripts\python.exe experiments\r8c_assurance_probe_v01\p_d3_boundary_independence.py ^
      --harness-commit 542018f1290864bc7735c896a64f5aed5de48a76 ^
      --source-commit 721545c46b94e0a87c87a572fb357ff314f6913f ^
      --output experiments\r8c_assurance_probe_v01\evidence\p_d3_run_004.json

No Attempt 004 result has been observed at this freeze point.

## 5. Current state

    P_D3_ATTEMPT_004=NOT_RUN
    P_D3_THIRD_REPAIRED_HARNESS=FROZEN
    COMPLETED_VALID_DECISION_PROBES=2_OF_8
    OWNER_ASSURANCE_DECISION=HELD
    PHYSICAL_MIGRATION_AUTHORIZED=false
    NEXT=EXECUTE_P_D3_ATTEMPT004
