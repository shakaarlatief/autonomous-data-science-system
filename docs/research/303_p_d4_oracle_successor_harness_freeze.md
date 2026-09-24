# Research 303: P-D4 Oracle-Successor Harness Freeze

**Date:** 2026-09-24
**Status:** P-D4 SUCCESSOR HARNESS FROZEN / EXECUTION NOT YET RUN / NO P-D4 RESULT
**Parent protocol:** Research 277
**Corpus freeze:** Research 299 / `d1f9418b4315010b0b4e77cc5943921a5b0e76d0`
**Old-oracle baseline:** Research 300 / PASS 11 OF 11
**Successor contract:** Research 302 / V0.2 / `58ff6b2f39169e2f8470ba020848472b8b196724`
**Harness commit:** `7f0f035f38118d0f9671050ac6fb5fc3b938cc37`
**Probe:** P-D4
**Scope:** Freeze the concrete old-oracle replay, legacy compatibility translation, representation-independent successor classifier, translated-representation discriminator and pre-registered successor controls before any P-D4 successor execution result is observed.
**Authority:** Probe-harness freeze only. It does not retire the current oracle, select a provider/workflow topology, or authorize physical migration.

## 1. Frozen architecture of the probe

The harness deliberately separates three roles:

```text
frozen old oracle
    exact migration oracle / baseline replay only

legacy compatibility translator
    converts the frozen current-routing carriers into ROUTING_ASSURANCE_SUBJECT_V1

successor semantic classifier
    consumes only ROUTING_ASSURANCE_SUBJECT_V1
    returns structured successor claim IDs
```

The successor classifier does not read repository files, inspect Git, execute the old checker, or parse the legacy JSON/Markdown carriers.

## 2. Exact frozen inputs

Corpus:

```text
commit  d1f9418b4315010b0b4e77cc5943921a5b0e76d0
path    experiments/r8c_assurance_probe_v01/p_d4_oracle_corpus.json
SHA256  4baacd66facc321c2ada84eff57acbd71fd3c9e326d8ab93a6b7adc752a24877
```

Successor contract V0.2:

```text
commit  58ff6b2f39169e2f8470ba020848472b8b196724
path    experiments/r8c_assurance_probe_v01/p_d4_successor_contract_v02.json
SHA256  36abb09beb186f8bdd0b3014ce8acfaa606036ab9f66955c96d0fd4f043b04aa
```

Concrete harness:

```text
commit  7f0f035f38118d0f9671050ac6fb5fc3b938cc37

experiments/r8c_assurance_probe_v01/README.md
    496aa994ff036895bd3201b8064bb495fb7693ea46b6f21b81b76b02e93a0b70

experiments/r8c_assurance_probe_v01/p_d4_oracle_successor.py
    b327ce4ada3861e5ef3f6d0946f1655a9fe22de63f0b3123d39534232a1196bf
```

All load-bearing hashes use `GIT_BLOB_BYTES_AT_COMMIT`.

## 3. Frozen old-oracle replay

The harness re-materializes all eleven frozen corpus cases and runs the exact current checker blob frozen by Research 299.

This is not successor logic. It is a replay guard requiring the already-observed Research 300 baseline to remain:

```text
11 / 11 semantic dispositions matched
```

If that baseline changes, P-D4 cannot pass.

## 4. Compatibility translation

The translator is allowed to understand the legacy representation because migration necessarily needs one representation boundary.

It:

```text
parses the legacy routing JSON when parseable
extracts overlapping CURRENT_STATE orientation facts
provides explicit available-checkpoint identities
classifies the legacy boundary as SEMANTIC or VOLATILE
constructs ROUTING_ASSURANCE_SUBJECT_V1
```

Malformed legacy JSON fails translation under `PD4-SR1` rather than being repaired or guessed.

The translator is separate from the successor semantic classifier, so legacy syntax does not become successor authority.

## 5. Successor classifier

`classify_successor()` evaluates only the eight Research 302 successor claims:

```text
PD4-SR1  structured subject well-formed / translatable
PD4-SR2  routed checkpoint exists
PD4-SR3  branch-scoped active-line freshness
PD4-SR4  independent orientation semantic parity
PD4-SR5  stable semantic boundary
PD4-SR6  complete integration revision identity
PD4-SR7  work-line and PR identity
PD4-SR8  specification/outcome well-formedness
```

A static independence check rejects direct classifier references to:

```text
check_current_routing
current_routing.json
CURRENT_STATE.md
git_bytes
subprocess
```

## 6. Translated-representation and completeness controls

The harness includes a direct successor subject representing PD4-C02 semantics without any legacy carrier access. It must pass.

A paired direct stale subject changes active checkpoint 269 to 268 while the active/checked line remains the same and available checkpoints remain `[268, 269]`. It must fail `PD4-SR3`.

The four Research 302 controls must also fail their pre-registered claims:

```text
PD4-X1 active_pr = 0                         -> PD4-SR7
PD4-X2 invalid work-line identity             -> PD4-SR7
PD4-X3 latest_specification = '28'            -> PD4-SR8
PD4-X4 empty latest_experiment_outcome        -> PD4-SR8
```

## 7. Frozen PASS discriminator

P-D4 returns `PASS` only when all seven harness criteria are true:

```text
1. frozen old-oracle replay remains 11/11
2. successor matches all 11 frozen GOOD/BAD dispositions
3. direct translated good subject passes without legacy carrier access
4. direct stale translated subject fails PD4-SR3
5. all four successor-only completeness controls fail their expected claims
6. successor classifier remains legacy-mechanism independent
7. no unique frozen requirement depends on retaining the legacy carrier/output shape
```

No corpus label, claim, threshold or control may be changed after execution.

## 8. Pre-execution validation

Before this freeze:

```text
Python compile       PASS
git diff --check    PASS
P-D4 execution      NOT RUN
```

The harness was committed and pushed before this research record was authored.

## 9. Execution command

```text
.\.venv\Scripts\python.exe experiments\r8c_assurance_probe_v01\p_d4_oracle_successor.py ^
  --harness-commit 7f0f035f38118d0f9671050ac6fb5fc3b938cc37 ^
  --output experiments\r8c_assurance_probe_v01\evidence\p_d4_run_001.json
```

No P-D4 successor execution result has been observed before this freeze.

## 10. Current state

```text
P_D4_CORPUS=FROZEN
P_D4_OLD_ORACLE_REPLAY=PASS_11_OF_11
P_D4_SUCCESSOR_CONTRACT=V0_2_FROZEN
P_D4_HARNESS=FROZEN
P_D4_EXECUTED=false

COMPLETED_VALID_SCOPED_PROBES=6_OF_8
OWNER_ASSURANCE_DECISION=HELD
SPECIFICATION028=UNCHANGED
AO10=HELD
PHYSICAL_MIGRATION_AUTHORIZED=false

NEXT=EXECUTE_P_D4
```
