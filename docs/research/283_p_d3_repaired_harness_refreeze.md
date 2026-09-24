# Research 283: P-D3 Repaired Harness Refreeze

**Date:** 2026-09-24
**Status:** P-D3 REPAIRED HARNESS FROZEN / ATTEMPT 002 NOT YET RUN / NO ARCHITECTURE RESULT YET
**Parent protocol:** Research 277
**Invalid attempt:** Research 282
**Probe:** P-D3
**Frozen repaired harness commit:** 1841fb62b5f41556381535263b567f43c97d8d2d
**Frozen source commit:** 721545c46b94e0a87c87a572fb357ff314f6913f
**Hash basis:** GIT_BLOB_BYTES_AT_COMMIT
**Scope:** Freeze the prospectively repaired P-D3 harness after the single authorized fixture-bootstrap change and before Attempt 002.
**Authority:** Repaired-fixture freeze only.

## 1. Repair applied

Research 282 authorized exactly one harness correction:

    stop reading nonexistent tracked:
        tools/__init__.py

    instead create inside the temporary isolated current-shaped fixture:
        tools/__init__.py
        with empty content

The committed diff performs only that change.

No change was made to:

    P-D3 question
    result classes
    thresholds
    frozen source commit
    static import scan
    representative Product behavior
    representative JW1 behavior
    target-shaped paths
    forbidden-dependency injections
    interpretation rules

## 2. Repaired harness binding

    experiments/r8c_assurance_probe_v01/README.md
        614967937244531c8b1cb8e4154f7e42f91b88f58bcd32120f31918ba1090fa4

    experiments/r8c_assurance_probe_v01/p_d3_boundary_independence.py
        47a7ea55278f716f90e065b156b706cb8bc1af6fa17fd2990a9facd5c6912fd1

    HARNESS_COMMIT
        1841fb62b5f41556381535263b567f43c97d8d2d

    SOURCE_COMMIT
        721545c46b94e0a87c87a572fb357ff314f6913f

    HASH_BASIS
        GIT_BLOB_BYTES_AT_COMMIT

## 3. Attempt 001 remains preserved

The invalid first attempt remains durable:

    experiments/r8c_assurance_probe_v01/evidence/
        p_d3_run_001_harness_invalid.json

Its failure is not overwritten or reclassified.

Attempt 002 is a new prospective execution against the repaired frozen harness.

## 4. Attempt 002 command

    .\.venv\Scripts\python.exe experiments\r8c_assurance_probe_v01\p_d3_boundary_independence.py ^
      --harness-commit 1841fb62b5f41556381535263b567f43c97d8d2d ^
      --source-commit 721545c46b94e0a87c87a572fb357ff314f6913f ^
      --output experiments\r8c_assurance_probe_v01\evidence\p_d3_run_002.json

No Attempt 002 result has been observed at this freeze point.

## 5. Current state

    P_D3_ATTEMPT_001=HARNESS_INVALID
    P_D3_REPAIRED_HARNESS=FROZEN
    P_D3_ATTEMPT_002=NOT_RUN

    COMPLETED_VALID_DECISION_PROBES=2_OF_8
    OWNER_ASSURANCE_DECISION=HELD
    PHYSICAL_MIGRATION_AUTHORIZED=false
    NEXT=EXECUTE_P_D3_ATTEMPT_002
