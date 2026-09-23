# Research 267: P-R8B-01-R2 Corrected Harness Freeze on Git-Blob Hash Basis

**Date:** 2026-09-23
**Status:** CORRECTED HARNESS FROZEN / EXECUTION NOT YET RUN / HASH BASIS CROSS-PLATFORM / NO OWNER REPRESENTATION DECISION / NO PHYSICAL MIGRATION
**Parent correction protocol:** Research 266
**Original protocol:** Research 263
**Corrected harness commit:** ceda2a257e8ff6b16bf9ffd1403d041ed07acc61
**Probe:** P-R8B-01-R2
**Candidate:** WMR-H V0.3
**Scope:** Freeze the corrected successor harness and exact real-source inputs before any corrected-run result is observed.
**Authority:** Empirical fixture freeze only. This harness is temporary research/qualification machinery, not future assurance architecture.

## 1. Freeze order

The corrected harness was:

    implemented
    AST-parsed successfully
    repository-integrity checked
    committed
    pushed

before this freeze record was authored.

It has not yet been executed.

## 2. Hash basis

Unlike Research 264, every harness hash in this record uses exactly:

    HASH_BASIS=GIT_BLOB_BYTES_AT_COMMIT

Commit:

    ceda2a257e8ff6b16bf9ffd1403d041ed07acc61

The byte sequence is obtained from:

    git show <commit>:<path>

and hashed with SHA-256.

This definition is invariant across Windows working-tree line-ending conversion, Linux checkouts and repository API reads.

## 3. Frozen harness Git-blob SHA-256

    experiments/r8b_representation_probe_v02/README.md
        2f18eac78843435825bccefc7b5f134253909b7ccb6cab0b6d9999a3ba65c5b4

    experiments/r8b_representation_probe_v02/probe.py
        2819d243a16ffd2c219a00a68805dca8429f4140658b633cf48c43e8480c9cd7

    experiments/r8b_representation_probe_v02/schemas/project_meta.schema.json
        67c24d1ae68af5d6283c2c7c1f493aaea4f1db976f7d3758fa7e7cafaa0248fa

    experiments/r8b_representation_probe_v02/schemas/workstream_state.schema.json
        b07c488940ac11e5bcf3edced5b323062ed3a6f43b8e68a582efca1f37427afd

    experiments/r8b_representation_probe_v02/schemas/receipt.schema.json
        53e889a09332e35e44e5ca033d7e2f3915edeada9fd1f2125a46fcd4730b5074

    experiments/r8b_representation_probe_v02/schemas/standalone_relation.schema.json
        8a674fefe8aa13404e138ad59d6def6a48423578c484d6498ff4a89f6ef93132

## 4. Frozen real-source fixture Git-blob SHA-256

At the same commit:

    docs/source_universe/SOURCE_VAULT_BOOTSTRAP_WORKSTREAM.md
        8af6602abbc25ff7eac8d8021239841231b32d28fe0880c859b3be2a7c30ea2a

    docs/specifications/028_v1_project_knowledge_architecture_implementation_and_migration_contract.md
        7651707b5d590efd7686a77dca20597dc731bfafa1fabc2358775bef7b9d2ffe

These equal the prior real-source fixture hashes.

## 5. Corrected implementation coverage

The successor harness retains all 18 original blocking labels G01-G18.

Material corrections include:

    G05
        real file transition + Git-measured human-definition diff
        + co-located negative control

    G08
        non-swallowing negative checks
        + no-op-validator controls
        + committed-history validation
        + merge history
        + corrupted-history negative control

    G10
        file-backed receipt/capture/review/promotion procedures

    G13
        rule-based real Specification 028 conversion
        + full non-metadata preservation comparison
        + explicit lifecycle/reference/provenance/authority accounting

    G16
        on-disk project anchor
        + generated derivatives created then deleted
        + recovery from anchor only
        + generated-only locator negative control

    G17
        actual framework file replacement
        + validation under refreshed schema/parser contract
        + instance-byte non-overwrite

    G18
        Git-computed transition, metadata, receipt and specification review shapes

The previously weak gates are also strengthened:

    G02
        JSON-compatible TOML check isolated from schema rejection

    G04
        loss/disposition manifest + computed pairing resolution

    G09
        discovery output drives bound admission
        + malformed declared relation fails visibly

    G15
        disk-driven canonical reread -> SQLite build -> delete -> reread/rebuild

Additional diagnostics:

    G07 control arm without revision bump
    revisionless definition hash freshness in current.json
    narrowed receipt evidence claim

New WMR-H V0.3 amendment gates:

    AM1-G1
        fail-visible governance recognition cases

    AM2-G1
        committed revision-history enforcement

## 6. Result binding requirement

The corrected result JSON MUST include:

    probe = P-R8B-01-R2
    protocol = Research 266
    original_threshold_basis = Research 263
    candidate = WMR-H V0.3

and a harness binding containing:

    hash_basis = GIT_BLOB_BYTES_AT_COMMIT
    commit = ceda2a257e8ff6b16bf9ffd1403d041ed07acc61
    all six frozen harness Git-blob SHA-256 values

It must also record the two real-source fixture hashes.

A semantic mismatch between working-tree harness text and the named frozen Git blob aborts execution.

## 7. Execution command

From repository root:

    .\.venv\Scripts\python.exe experiments\r8b_representation_probe_v02\probe.py --harness-commit ceda2a257e8ff6b16bf9ffd1403d041ed07acc61 --output experiments\r8b_representation_probe_v02\evidence\run_001

The durable evidence path is intentionally not under the repository's ignored results/ convention.

## 8. Outcome rule

PASS requires:

    original blocking gates G01-G18 = 18 / 18 PASS
    AM1-G1 = PASS
    AM2-G1 = PASS

The original Research 263 thresholds remain unchanged.

A harness defect produces HARNESS_INVALID only after the defect is demonstrated; success criteria are not reinterpreted.

## 9. Current state

    P_R8B_01_R2_PROTOCOL=FROZEN_RESEARCH266
    P_R8B_01_R2_HARNESS_COMMIT=ceda2a257e8ff6b16bf9ffd1403d041ed07acc61
    HASH_BASIS=GIT_BLOB_BYTES_AT_COMMIT
    P_R8B_01_R2_EXECUTED=false

    WMR_H_V0_3=CORRECTION_CANDIDATE
    OWNER_REPRESENTATION_DECISION=HELD

    SPECIFICATION028=UNCHANGED
    AO10=HELD
    FILE_LEVEL_MIGRATION=HELD
    PHYSICAL_MIGRATION_AUTHORIZED=false
    NEXT=EXECUTE_P_R8B_01_R2
