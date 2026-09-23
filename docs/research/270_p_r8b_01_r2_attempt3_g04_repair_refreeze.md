# Research 270: P-R8B-01-R2 Attempt 2 G04 Repair and Third Harness Freeze

**Date:** 2026-09-23
**Status:** G04 FALSE-POSITIVE REPAIRED / THIRD HARNESS FROZEN / ATTEMPT 3 NOT YET RUN / NO OWNER REPRESENTATION DECISION
**Parent protocol:** Research 266
**Attempt-2 classification:** Research 269
**Prior replacement harness:** a893e7e904e29ca91491108bd816d4af06dba6c1
**Third frozen harness commit:** 17c48ac8d7810b5d938532e65367e8aa550e101c
**Probe:** P-R8B-01-R2
**Candidate:** WMR-H V0.3
**Scope:** Prospectively repair the demonstrated G04 false-positive detector, freeze the resulting harness on the established Git-blob hash basis, and authorize only the third corrected execution attempt.
**Authority:** Harness-repair and empirical-fixture freeze only. No representation acceptance, Specification 028 amendment, AO-10 implementation, or physical migration.

## 1. Attempt-2 defect carried forward

Attempt 2 reported only:

    G04 FAIL
        raw token PAUSED occurred inside the durable semantic sentence:
        "A PAUSED state is routing..."

Research 269 established that this violates the harness implementation, not the Research 263 criterion.

The unchanged criterion is:

    the human definition must not canonically assert the six current
    transition-owned facts

not:

    the human definition must never use the vocabulary tokens that name
    state classes or milestone values.

Therefore:

    THRESHOLDS_CHANGED=false
    CANDIDATE_CHANGED=false
    ATTEMPT_2_CLASSIFICATION=HARNESS_INVALID

## 2. Prospective G04 repair

The repaired detector now distinguishes:

    durable semantics
        "A PAUSED state is routing..."
        permitted

from explicit current ownership such as:

    workstream state = PAUSED
    current state = PAUSED
    **Status:** PAUSED
    exact current pause_reason assertion
    exact current return_condition assertion
    exact current resume_target assertion
    source ingestion = NOT_STARTED
    Course 2 = BLOCKED

The detector checks:

    governed metadata keys that would claim current transition state
    explicit current-state body assertion forms
    exact current pause/return/resume text
    current milestone assertion forms

G04 also adds a negative-control definition containing all six current facts.

Pass requires:

    real converted definition:
        detected current transition-owned assertions = 0

    negative control:
        detected current transition-owned assertions = 6

The existing computed pairing, loss-accounting, provenance/reference, and expected-to-resume checks remain unchanged.

## 3. Freeze order

The repaired harness was:

    edited prospectively
    AST-parsed successfully
    repository-integrity checked
    committed
    pushed

before this freeze record.

Attempt 3 has not yet been executed.

## 4. Hash basis

The established cross-platform basis remains:

    HASH_BASIS=GIT_BLOB_BYTES_AT_COMMIT

Third frozen commit:

    17c48ac8d7810b5d938532e65367e8aa550e101c

Frozen Git-blob SHA-256:

    experiments/r8b_representation_probe_v02/README.md
        2f18eac78843435825bccefc7b5f134253909b7ccb6cab0b6d9999a3ba65c5b4

    experiments/r8b_representation_probe_v02/probe.py
        ac144f0719da7a736ca932990107c8a61f7f21cbcfd2f98d0261558bc0257835

    experiments/r8b_representation_probe_v02/schemas/project_meta.schema.json
        67c24d1ae68af5d6283c2c7c1f493aaea4f1db976f7d3758fa7e7cafaa0248fa

    experiments/r8b_representation_probe_v02/schemas/workstream_state.schema.json
        b07c488940ac11e5bcf3edced5b323062ed3a6f43b8e68a582efca1f37427afd

    experiments/r8b_representation_probe_v02/schemas/receipt.schema.json
        53e889a09332e35e44e5ca033d7e2f3915edeada9fd1f2125a46fcd4730b5074

    experiments/r8b_representation_probe_v02/schemas/standalone_relation.schema.json
        8a674fefe8aa13404e138ad59d6def6a48423578c484d6498ff4a89f6ef93132

Real-source fixture Git-blob SHA-256 remains:

    Source Vault workstream
        8af6602abbc25ff7eac8d8021239841231b32d28fe0880c859b3be2a7c30ea2a

    Specification 028
        7651707b5d590efd7686a77dca20597dc731bfafa1fabc2358775bef7b9d2ffe

## 5. Attempt-3 command

From repository root:

    .\.venv\Scripts\python.exe experiments\r8b_representation_probe_v02\probe.py --harness-commit 17c48ac8d7810b5d938532e65367e8aa550e101c --output experiments\r8b_representation_probe_v02\evidence\run_003

## 6. Outcome rule remains unchanged

PASS requires:

    original blocking gates G01-G18 = 18 / 18 PASS
    AM1-G1 = PASS
    AM2-G1 = PASS

No result may be upgraded by interpretation if a blocking gate validly fails.

A newly demonstrated harness defect remains HARNESS_INVALID and must be repaired prospectively.

## 7. Current state

    P_R8B_01_R2_ATTEMPT_1=HARNESS_INVALID
    P_R8B_01_R2_ATTEMPT_2=HARNESS_INVALID

    THIRD_HARNESS_COMMIT=17c48ac8d7810b5d938532e65367e8aa550e101c
    HASH_BASIS=GIT_BLOB_BYTES_AT_COMMIT
    ATTEMPT_3_EXECUTED=false

    WMR_H_V0_3=CORRECTION_CANDIDATE
    OWNER_REPRESENTATION_DECISION=HELD

    SPECIFICATION028=UNCHANGED
    AO10=HELD
    FILE_LEVEL_MIGRATION=HELD
    PHYSICAL_MIGRATION_AUTHORIZED=false
    NEXT=EXECUTE_P_R8B_01_R2_ATTEMPT_3
