# Research 268: P-R8B-01-R2 Harness Defect, Prospective Repair, and Replacement Freeze

**Date:** 2026-09-23
**Status:** FIRST CORRECTED-RUN ATTEMPT HARNESS_INVALID / PROSPECTIVE REPAIR FROZEN / EXECUTION RETRY NEXT / NO OWNER REPRESENTATION DECISION
**Parent protocol:** Research 266
**Prior freeze:** Research 267
**Prior frozen harness commit:** ceda2a257e8ff6b16bf9ffd1403d041ed07acc61
**Replacement harness commit:** a893e7e904e29ca91491108bd816d4af06dba6c1
**Probe:** P-R8B-01-R2
**Candidate:** WMR-H V0.3
**Scope:** Record the first corrected-run harness failure, classify it as a probe implementation defect, preserve unchanged architecture thresholds, and freeze the prospective repair before retry.
**Authority:** Harness-defect and replacement-freeze record only. No architecture disposition changes.

## 1. Failed execution classification

The first execution attempt against the Research 267 frozen harness terminated before any gate result was produced.

Observed exception:

    ProbeFailure: real workstream state block not found

Cause:

    the converter assumed the first fenced state block followed the
    "## Current qualified state" heading immediately

but the real carrier contains an explanatory paragraph between the heading and the fenced state block.

This is a probe implementation defect, not an architecture failure.

Therefore:

    P_R8B_01_R2_ATTEMPT_1=HARNESS_INVALID
    BLOCKING_GATE_RESULTS_PRODUCED=0
    ARCHITECTURE_DISPOSITION_CHANGED=false

Research 266 explicitly permits prospective harness repair after a demonstrated harness defect without changing thresholds.

## 2. Prospective repair

The parser was amended only to locate the first fenced text state block within the real "Current qualified state" section after intervening prose.

No gate threshold, candidate rule, schema, expected source hash, or result interpretation was changed.

The repaired file was:

    committed
    AST-parse checked
    pushed

before retry execution.

## 3. Replacement hash basis

As required by Research 266/267:

    HASH_BASIS=GIT_BLOB_BYTES_AT_COMMIT

Replacement commit:

    a893e7e904e29ca91491108bd816d4af06dba6c1

Frozen SHA-256 values:

    experiments/r8b_representation_probe_v02/README.md
        2f18eac78843435825bccefc7b5f134253909b7ccb6cab0b6d9999a3ba65c5b4

    experiments/r8b_representation_probe_v02/probe.py
        db73ab4f5a37df69337be430864d72b9d926fbea8f964e309256275d971b3dd1

    experiments/r8b_representation_probe_v02/schemas/project_meta.schema.json
        67c24d1ae68af5d6283c2c7c1f493aaea4f1db976f7d3758fa7e7cafaa0248fa

    experiments/r8b_representation_probe_v02/schemas/workstream_state.schema.json
        b07c488940ac11e5bcf3edced5b323062ed3a6f43b8e68a582efca1f37427afd

    experiments/r8b_representation_probe_v02/schemas/receipt.schema.json
        53e889a09332e35e44e5ca033d7e2f3915edeada9fd1f2125a46fcd4730b5074

    experiments/r8b_representation_probe_v02/schemas/standalone_relation.schema.json
        8a674fefe8aa13404e138ad59d6def6a48423578c484d6498ff4a89f6ef93132

Real-source fixture hashes remain unchanged:

    Source Vault
        8af6602abbc25ff7eac8d8021239841231b32d28fe0880c859b3be2a7c30ea2a

    Specification 028
        7651707b5d590efd7686a77dca20597dc731bfafa1fabc2358775bef7b9d2ffe

## 4. Retry command

    .\.venv\Scripts\python.exe experiments\r8b_representation_probe_v02\probe.py --harness-commit a893e7e904e29ca91491108bd816d4af06dba6c1 --output experiments\r8b_representation_probe_v02\evidence\run_002

## 5. Current state

    ATTEMPT_1=HARNESS_INVALID
    THRESHOLDS_CHANGED=false
    CANDIDATE_CHANGED=false
    REPLACEMENT_HARNESS_FROZEN=true
    OWNER_REPRESENTATION_DECISION=HELD
    NEXT=EXECUTE_P_R8B_01_R2_ATTEMPT_2
