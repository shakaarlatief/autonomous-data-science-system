# Research 279: P-D6 Executor Capability Probe Harness Freeze

**Date:** 2026-09-24
**Status:** P-D6 HARNESS FROZEN / EXECUTION NOT YET RUN / NO OWNER ASSURANCE DECISION
**Parent protocol:** Research 277
**Candidate:** WARRANT-F V0.2
**Probe:** P-D6
**Frozen harness commit:** a84e111e6dd60d1b56380a8aeb78fd842b1cf4f9
**Hash basis:** GIT_BLOB_BYTES_AT_COMMIT
**Scope:** Freeze the concrete P-D6 harness before any execution result is observed.

## 1. Purpose

P-D6 tests the owner clarification encoded in WF-A34 through WF-A36:

    assurance semantics are executor-neutral
    execution planning is capability-aware
    execution surface does not imply trust
    provider/model names do not own semantics

The probe is intentionally narrow.

It does not select an executor, model, Git provider, CI provider, or local/remote workflow.

## 2. Frozen files

    experiments/r8c_assurance_probe_v01/README.md
        aa57781bb751135f3132e0d656e46b2ebcef26eb60144a42d826823acd577e4d

    experiments/r8c_assurance_probe_v01/p_d6_executor_capability.py
        a7cd0ffcdb3e18e26018f234353b006e2b1c5f406ed5eadf25ebe6a2e5ae835d

## 3. Harness design

The harness defines one immutable assurance request containing:

    exact subject
    verifier ID
    required capabilities
    required trust properties

It then evaluates executor records whose dimensions are separated:

    actor label
    execution-surface label
    capability set
    trust-property set

The fixtures include:

    two different model labels with identical local capability/trust records

    one hosted executor with isolation + producer authenticity

    one hosted executor with isolation but no producer authenticity

    one Git-API-only executor lacking process execution

    one local executor lacking subject binding

## 4. Required assertions

The frozen harness must fail if:

    actor/model label changes eligibility or trust semantics

    a missing capability does not block eligibility

    a missing required trust property does not block eligibility

    hosted surface label alone produces T2

    evaluating one executor mutates the assurance request

The harness includes a deliberate negative-control trust function that assigns T2 from the word "hosted".

The probe is discriminating only if that bad function produces a different result from property-based trust classification for the isolated-only hosted executor.

## 5. Execution binding

The harness requires:

    --harness-commit a84e111e6dd60d1b56380a8aeb78fd842b1cf4f9

and records the Git-blob hashes for the frozen files in its result.

Execution command:

    .\.venv\Scripts\python.exe experiments\r8c_assurance_probe_v01\p_d6_executor_capability.py --harness-commit a84e111e6dd60d1b56380a8aeb78fd842b1cf4f9 --output experiments\r8c_assurance_probe_v01\evidence\p_d6_run_001.json

## 6. Interpretation remains preregistered

PASS requires all Research 277 P-D6 criteria.

A PASS supports semantic capability/trust separation only.

It does not show that current ChatGPT, Claude, Codex, Claude Code, GitHub, local runtime or hosted CI have any particular target role.

## 7. Current state

    P_D6_HARNESS=FROZEN
    P_D6_EXECUTED=false
    HARNESS_COMMIT=a84e111e6dd60d1b56380a8aeb78fd842b1cf4f9
    HASH_BASIS=GIT_BLOB_BYTES_AT_COMMIT

    COMPLETED_DECISION_PROBES=1_OF_8
    NEXT=EXECUTE_P_D6
