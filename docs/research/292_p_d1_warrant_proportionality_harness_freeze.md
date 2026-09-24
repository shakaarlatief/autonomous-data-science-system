# Research 292: P-D1 Warrant-Proportionality Harness Freeze

**Date:** 2026-09-24
**Status:** P-D1 HARNESS FROZEN / EXECUTION NOT YET RUN / NO OWNER ASSURANCE DECISION
**Parent protocol:** Research 277
**Claim-set freeze:** Research 291
**Candidate:** WARRANT-F V0.2
**Probe:** P-D1
**Frozen harness commit:** 733e55796beed3cd07f4017e4f3718e3a2e2f943
**Frozen source commit:** 1a095044282622f2ce9e2bd38b90d77b8be8a4a2
**Hash basis:** GIT_BLOB_BYTES_AT_COMMIT
**Scope:** Freeze the concrete P-D1 warrant catalog and executable proportionality harness after claim selection and before any P-D1 execution result is observed.
**Authority:** Probe-harness freeze only.

## 1. Claim selection remains prior and independent

Research 291 froze exactly:

    4 invariant claims
    4 suite claims
    4 cross-boundary claims

before warrant text or witness implementation was authored.

This harness does not change that selection.

## 2. Warrant model exercised

For each selected claim the catalog records:

    claim ID
    grain
    declared scope
    verifier/evidence sources
    warrant basis
    limitations
    warrant status
    witness provenance
    bounded re-witness triggers

Invariant claims additionally bind:

    executable sensitivity witness
    executable specificity witness

Suite and cross-boundary claims may remain:

    PARTIALLY_WARRANTED

where the probe does not directly establish the full declared scope.

This is intentional coverage honesty, not a failure.

## 3. One-claim-per-test discriminator

The harness reads the frozen source commit and counts the real test functions covered by each suite claim.

PASS requires:

    exactly 12 first-class claims
    exactly 4 claims in each preregistered grain
    every suite claim covers at least 2 real test functions
    no one-claim-per-test expansion

The architecture is therefore tested for selective assurance claims rather than universal per-test metadata.

## 4. Invariant sensitivity and specificity

The four invariant claims execute frozen-source pytest witnesses:

    I1 noncanonical authority exclusion
    I2 duplicate current identity ownership rejection
    I3 stale capture-promotion target rejection
    I4 public/private rendered-value nonleakage

Each also executes a valid near-miss/specificity witness.

PASS requires all eight witness executions to pass.

## 5. Sampled suite mutation adequacy

The Product reasoning suite is the preregistered sampled suite.

Baseline:

    tests/unit/test_reasoning.py

must pass at the frozen source commit.

Four mutations are fixed before execution:

    M1 remove expected nonce field name
    M2 disable duplicate output-list guard
    M3 disable unsupported methodological-basis guard
    M4 disable duplicate knowledge-key guard

Each mutant is evaluated against the unchanged full Product reasoning suite.

PASS requires:

    4 / 4 sampled mutations killed

The mutation sample is deliberately small.

It tests whether a suite warrant can carry executable sensitivity evidence without claiming universal mutation completeness.

## 6. Re-witness proportionality

The catalog allows re-witness triggers such as:

    verifier semantic change
    declared-input change
    witness-corpus change
    claim-scope change
    material suite redesign
    suite health trigger

PASS forbids a requirement to re-witness merely because an unrelated test changed.

No wall-clock threshold is used because current authoring speed is not a target-architecture constraint.

## 7. Frozen files

    experiments/r8c_assurance_probe_v01/README.md
        edd20b05a5afbe1854b5b8324c20fa3cb6ef38902d46ac3b2e913ef3ceba8512

    experiments/r8c_assurance_probe_v01/p_d1_claims.json
        c4d9360968fd4fce41cd37572f74a4e34e041b06e8c297a2b9ff8bdf157c0810

    experiments/r8c_assurance_probe_v01/p_d1_warrant_proportionality.py
        3cf7d198e7017d871dd2fd6cc07a5fdae57e69fec1b24bbd728b843172704baf

## 8. Execution command

    .\.venv\Scripts\python.exe experiments\r8c_assurance_probe_v01\p_d1_warrant_proportionality.py ^
      --harness-commit 733e55796beed3cd07f4017e4f3718e3a2e2f943 ^
      --source-commit 1a095044282622f2ce9e2bd38b90d77b8be8a4a2 ^
      --output experiments\r8c_assurance_probe_v01\evidence\p_d1_run_001.json

No P-D1 execution result has been observed before this freeze.

## 9. Current state

    P_D1_CLAIM_SET=FROZEN
    P_D1_HARNESS=FROZEN
    P_D1_EXECUTED=false

    COMPLETED_VALID_DECISION_PROBES=4_OF_8
    OWNER_ASSURANCE_DECISION=HELD
    NEXT=EXECUTE_P_D1
