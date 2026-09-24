# Research 281: P-D3 Boundary-Independence Probe Harness Freeze

**Date:** 2026-09-24
**Status:** P-D3 HARNESS FROZEN / EXECUTION NOT YET RUN / NO OWNER ASSURANCE DECISION
**Parent protocol:** Research 277
**Candidate:** WARRANT-F V0.2
**Probe:** P-D3
**Frozen harness commit:** 5ba5ae40567bcc55da2ba031ef10a98f0df3a46e
**Frozen source commit:** 721545c46b94e0a87c87a572fb357ff314f6913f
**Hash basis:** GIT_BLOB_BYTES_AT_COMMIT
**Scope:** Freeze the concrete two-layer Product/JW1 boundary-independence harness before any P-D3 execution result is observed.
**Authority:** Probe-fixture freeze only. No architecture acceptance, migration, workspace move, dependency rewrite, or assurance cutover is authorized.

## 1. Preregistered architecture question

Research 277 asks:

> Are the accepted Product/JW1/Engineering dependency boundaries realizable without hidden runtime dependence?

The accepted high-level constraints under test are:

    Product runtime
        must not require Project-plane machinery for runtime correctness

    JW1 / project-system
        must not depend on Project Engineering

    Project Engineering
        may inspect/invoke Product and JW1 for qualification

The probe tests realizability rather than full migration completeness.

## 2. Two-layer design

### Layer A: current-state observation

Against frozen source commit:

    721545c46b94e0a87c87a572fb357ff314f6913f

the harness:

    statically scans all current Product Python files under:
        src/ads_system/

    statically scans all current JW1 Python files under:
        tools/project_knowledge/

    observes explicit absolute-import violations against the relevant forbidden
    dependency directions

    executes one representative Product semantic behavior with Project tooling
    physically absent from the isolated fixture

    executes one representative JW1 semantic behavior with Engineering
    physically absent from the isolated fixture

A current-layout defect can produce:

    CURRENT_DEBT_ONLY

without falsifying the target.

### Layer B: target-shaped isolation fixture

The harness reconstructs bounded temporary target-shaped layouts:

    product/runtime/src/ads_system/

    project/system/src/ads_project_system/

Only the files required for the selected representative semantic behaviors are materialized from the frozen source commit.

Product behavior:

    provider-neutral ReasoningRequest construction
    deterministic semantic digest

JW1 behavior:

    identity-index construction
    identity resolution

The two execute in separate isolated Python processes.

## 3. Negative controls

The harness deliberately injects:

    import ads_project_system
        into target-shaped Product reasoning

    import ads_system
        into target-shaped JW1 identity logic

Each injected fixture MUST fail because the forbidden dependency is unavailable in that isolated environment.

If either injected forbidden dependency is not detected:

    P-D3=HARNESS_INVALID

This directly tests that the absence fixture is real rather than nominal.

## 4. Static-scan limits

The static source scan covers:

    explicit absolute Python imports

It does not by itself prove absence of:

    dynamic string-based imports
    subprocess coupling
    filesystem path coupling
    environment-variable coupling
    network/service coupling

The isolated runtime fixture adds independent runtime evidence for the selected representative paths.

P-D3 therefore tests boundary realizability, not exhaustive full-system production readiness.

## 5. Frozen harness

    experiments/r8c_assurance_probe_v01/README.md
        614967937244531c8b1cb8e4154f7e42f91b88f58bcd32120f31918ba1090fa4

    experiments/r8c_assurance_probe_v01/p_d3_boundary_independence.py
        81b9de078b87608817b359bd6b5e3b41242937fdd41c47eb4612521d0a92058f

Hash basis:

    GIT_BLOB_BYTES_AT_COMMIT

Frozen harness commit:

    5ba5ae40567bcc55da2ba031ef10a98f0df3a46e

Frozen source commit:

    721545c46b94e0a87c87a572fb357ff314f6913f

## 6. Execution command

    .\.venv\Scripts\python.exe experiments\r8c_assurance_probe_v01\p_d3_boundary_independence.py ^
      --harness-commit 5ba5ae40567bcc55da2ba031ef10a98f0df3a46e ^
      --source-commit 721545c46b94e0a87c87a572fb357ff314f6913f ^
      --output experiments\r8c_assurance_probe_v01\evidence\p_d3_run_001.json

No result has been observed at this freeze point.

## 7. Result interpretation remains frozen

    target-shaped fixture succeeds
    AND negative controls discriminate
    AND current explicit-import scan is clean
        -> PASS

    target-shaped fixture succeeds
    AND negative controls discriminate
    BUT current explicit-import scan identifies current forbidden coupling
        -> CURRENT_DEBT_ONLY

    representative required behavior cannot be expressed without a forbidden
    target dependency
        -> AMEND

    target fixture or negative control fails to discriminate
        -> HARNESS_INVALID

No current-path fact may be upgraded into target architecture merely because it is observed.

## 8. Current state

    P_D3_HARNESS=FROZEN
    P_D3_EXECUTED=false

    HARNESS_COMMIT=5ba5ae40567bcc55da2ba031ef10a98f0df3a46e
    SOURCE_COMMIT=721545c46b94e0a87c87a572fb357ff314f6913f
    HASH_BASIS=GIT_BLOB_BYTES_AT_COMMIT

    COMPLETED_DECISION_PROBES=2_OF_8
    OWNER_ASSURANCE_DECISION=HELD
    PHYSICAL_MIGRATION_AUTHORIZED=false
    NEXT=EXECUTE_P_D3
