# Research 264: P-R8B-01 Probe Harness Freeze

**Date:** 2026-09-23
**Status:** PROBE HARNESS FROZEN / EXECUTION NOT YET RUN / NO OWNER REPRESENTATION DECISION / NO PHYSICAL MIGRATION
**Parent:** Research 263
**Probe:** P-R8B-01
**Protocol authority:** Research 263
**Repository base before harness freeze:** b8e173630f1023ccc734cb9cf12e3e81b6e98dfe
**Scope:** Freeze the concrete temporary harness used to execute the preregistered P-R8B-01 gates before any result is observed.
**Authority:** Probe implementation freeze only. The harness is not future assurance architecture.

## 1. Why this freeze exists

Research 263 preregistered the architecture claims, fixtures and blocking thresholds.

This record freezes the concrete implementation that will execute those gates before it is run, preserving the distinction:

    protocol
        Research 263

    implementation
        Research 264

    result
        future Research 265 or successor

No pass/fail threshold may be weakened because of observed results without creating a successor protocol and invalidating the confirmatory interpretation of the original run.

## 2. Harness location

Temporary current-repository research surface:

    experiments/r8b_representation_probe_v01/

This location does not grant the current experiments/ root target-architecture status.

The harness is explicitly temporary JC3 research/qualification machinery.

## 3. Frozen implementation files

    experiments/r8b_representation_probe_v01/README.md
    experiments/r8b_representation_probe_v01/probe.py
    experiments/r8b_representation_probe_v01/schemas/project_meta.schema.json
    experiments/r8b_representation_probe_v01/schemas/workstream_state.schema.json
    experiments/r8b_representation_probe_v01/schemas/receipt.schema.json
    experiments/r8b_representation_probe_v01/schemas/standalone_relation.schema.json

Frozen SHA-256:

    probe.py
        7264d7e329c5564cc366a275232f4644472add735ec00528d8d83c3a54d99711

    project_meta.schema.json
        3df8669cc1ee1e045c2ba91075e17cf7fde01b42c9c57e3df63c0aae64f4eac4

    workstream_state.schema.json
        f0cd9714531752446d875e14a956a3a68802b7539f44e66a46f23580d745cf0d

    receipt.schema.json
        f7446874fe02f2f3c185a0be24e5c8e7f39fbea25b0dbf62b4229145372aad87

    standalone_relation.schema.json
        27943ee623641d55b77f3c07691a9972f13d5bae6190a6b946648e03a4a33880

## 4. Real-source fixture freeze

The harness asserts exact source hashes before execution.

    docs/source_universe/SOURCE_VAULT_BOOTSTRAP_WORKSTREAM.md
        8af6602abbc25ff7eac8d8021239841231b32d28fe0880c859b3be2a7c30ea2a

    docs/specifications/028_v1_project_knowledge_architecture_implementation_and_migration_contract.md
        7651707b5d590efd7686a77dca20597dc731bfafa1fabc2358775bef7b9d2ffe

Source drift aborts the probe rather than silently changing the empirical fixture.

The canonical files themselves are never modified by the probe.

## 5. Implementation strategy

The temporary harness uses:

    Python standard library
        pathlib
        json
        tomllib
        hashlib
        tempfile
        sqlite3
        subprocess / Git

    current repository jsonschema dependency
        Draft 2020-12 structural validation

This tool choice is implementation convenience only.

It does not select Python, pytest, GitHub Actions, JSON Schema tooling implementation, or any other test/CI mechanism for the future assurance architecture.

## 6. Gate realization

The script implements G01-G18 from Research 263, including:

    strict metadata-position parser
    JSON-compatible TOML value rejection
    plain-Markdown negative control
    real Source Vault definition/state split
    zero-human-diff routine state transition
    exact stale-write rejection
    cross-branch revision-line conflict
    monotonic revision semantics
    repository-wide natural-owner relation discovery/bound
    capture/receipt separation
    content-addressed individual JSON receipts
    public/private fail-closed receipt checks
    real Specification 028 metadata conversion
    current.json freshness
    SQLite/FTS rebuild
    derivative-free break-glass recovery
    PSMF framework/instance refresh separation
    narrow objective Git-review shape checks

The harness writes result evidence only under its requested output directory.

## 7. Pre-execution validation

Python AST parsing:

    PASS

The probe itself has NOT been executed at this freeze boundary.

## 8. Execution command

From repository root:

    .\.venv\Scripts\python.exe experiments\r8b_representation_probe_v01\probe.py --output experiments\r8b_representation_probe_v01\results\run_001

Expected interpretation:

    exit 0
        only if all 18 blocking gates PASS

    nonzero
        one or more blocking gates failed or the harness/source precondition failed

The detailed result is written to:

    experiments/r8b_representation_probe_v01/results/run_001/result.json

## 9. Current state

    P_R8B_01_PROTOCOL=FROZEN_RESEARCH263
    P_R8B_01_HARNESS=FROZEN_RESEARCH264
    P_R8B_01_EXECUTED=false

    WMR_H_V0_2=PROBE_CANDIDATE
    REPRESENTATION_OWNER_DECISION=PENDING_PROBE

    SPECIFICATION028=UNCHANGED
    AO10=HELD
    FILE_LEVEL_MIGRATION=HELD
    PHYSICAL_MIGRATION_AUTHORIZED=false
    NEXT=EXECUTE_P_R8B_01
