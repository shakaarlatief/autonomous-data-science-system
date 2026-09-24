# Research 289: P-D5 Adapter Fidelity Harness Freeze

**Date:** 2026-09-24
**Status:** P-D5 HARNESS FROZEN / EXECUTION NOT YET RUN / NO OWNER ASSURANCE DECISION
**Parent protocol:** Research 277
**Candidate:** WARRANT-F V0.2
**Probe:** P-D5
**Frozen harness commit:** 669134254f370802698dad8c299a02613bf4a8bb
**Frozen source commit:** 721545c46b94e0a87c87a572fb357ff314f6913f
**Hash basis:** GIT_BLOB_BYTES_AT_COMMIT
**Scope:** Freeze the concrete consumer-side adapter-fidelity harness before any P-D5 execution result is observed.
**Authority:** Probe-harness freeze only.

## 1. Architecture discriminator

P-D5 tests whether Engineering can adapt owner-native Product/JW1 results into a neutral assurance evidence model without Product or JW1 importing Engineering assurance contracts.

Required mappings remain exactly those preregistered in Research 277:

    native pass            -> PASS
    native fail            -> FAIL
    crash / collection     -> HARNESS_INVALID
    zero collected         -> INCOMPLETE
    skipped only           -> INCOMPLETE
    truncated/unparseable  -> HARNESS_INVALID
    zero claim matches     -> UNVERIFIED

## 2. Native paths

Product path:

    pytest JUnit XML

The harness materializes bounded temporary pytest fixtures for pass, fail, skipped-only, collection-error and zero-test cases.

JW1 path:

    project-knowledge CLI JSON contract

The frozen source commit is bound through tools/project_knowledge/cli.py. The probe uses the CLI's native ok/error JSON contract shape without requiring JW1 to import the neutral assurance model.

## 3. Negative controls

The harness contains two deliberately faulty consumer adapters:

    Product faulty adapter
        treats any parseable JUnit XML as PASS

    JW1 faulty adapter
        treats any parseable JSON as PASS

The fail witnesses must distinguish both faulty adapters from the correct adapters.

## 4. Frozen files

    experiments/r8c_assurance_probe_v01/README.md
        a4753b505745a7653eeb14e92579128e17ac325056afb6603fde017f2f33c0dd

    experiments/r8c_assurance_probe_v01/p_d5_adapter_fidelity.py
        d84bad07adf6ecff8309420d6e8b9f66647a447e6252e5280e30ef4757cc8b79

    HARNESS_COMMIT
        669134254f370802698dad8c299a02613bf4a8bb

    SOURCE_COMMIT
        721545c46b94e0a87c87a572fb357ff314f6913f

## 5. Execution command

    .\.venv\Scripts\python.exe experiments\r8c_assurance_probe_v01\p_d5_adapter_fidelity.py ^
      --harness-commit 669134254f370802698dad8c299a02613bf4a8bb ^
      --source-commit 721545c46b94e0a87c87a572fb357ff314f6913f ^
      --output experiments\r8c_assurance_probe_v01\evidence\p_d5_run_001.json

No P-D5 result has been observed before this freeze.

## 6. Current state

    P_D5_HARNESS=FROZEN
    P_D5_EXECUTED=false
    COMPLETED_VALID_DECISION_PROBES=3_OF_8
    OWNER_ASSURANCE_DECISION=HELD
    NEXT=EXECUTE_P_D5
