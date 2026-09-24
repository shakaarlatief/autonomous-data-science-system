# Research 297: P-D2 Attempt 002 Repaired Harness Refreeze

**Date:** 2026-09-24
**Status:** P-D2 ATTEMPT 002 HARNESS REFROZEN / EXECUTION NOT YET RUN / NO OWNER ASSURANCE DECISION
**Parent protocol:** Research 277
**Selection/label freeze:** Research 294 / `d7f65392b851c03b49c246c023b0a6684ef3c60b`
**Attempt 001 failure:** Research 296
**Repaired harness commit:** `3ee7e4f547e98f5fd8bbf38fc7a5a760c6a47ed1`
**Probe:** P-D2
**Scope:** Prospectively refreeze the P-D2 harness after the single authorized selection-fixture Git-blob hash-basis repair and before Attempt 002 execution.
**Authority:** Probe-harness freeze only.

## 1. Repair applied

Exactly one semantic source line changed from the Attempt 001 harness:

```text
EXPECTED_FIXTURE_SHA256
    be70e8c3aa5f4dea2b9f2680ebaae1b4c09b1733a6f8a22da4edeb93d3f86072
->  3946655c69bba95d5f7b606e8a25cb1a2be1119e5613dfb4e3ecf9dbf515fc43
```

The replacement value is the SHA-256 of the exact Git blob content returned from the frozen selection commit.

No selected historical case, independent label, rationale, normalized policy delta, classifier branch, criterion, negative control, digest algorithm or threshold changed.

## 2. Frozen bindings

Selection remains:

```text
commit        d7f65392b851c03b49c246c023b0a6684ef3c60b
path          experiments/r8c_assurance_probe_v01/p_d2_history_labels.json
blob SHA-256  3946655c69bba95d5f7b606e8a25cb1a2be1119e5613dfb4e3ecf9dbf515fc43
```

Repaired harness:

```text
commit        3ee7e4f547e98f5fd8bbf38fc7a5a760c6a47ed1

experiments/r8c_assurance_probe_v01/README.md
    9611225a2dc3ce7c6d14bef04303fc9459a9127d04eed52c3894f853e876bf5b

experiments/r8c_assurance_probe_v01/p_d2_ratchet_history.py
    3c7324ccc22270b68e819fe2a761d70f7d0da76d669b90dea98c84052d84c6f7
```

Hash basis is `GIT_BLOB_BYTES_AT_COMMIT`.

## 3. Pre-execution validation

Before this refreeze:

```text
Python compile                 PASS
git diff --check              PASS
repair diff                   exactly one expected-hash substitution
Attempt 002 executed          false
```

## 4. Attempt 002 discriminator

The exact Research 295 PASS discriminator remains unchanged. Attempt 002 must still satisfy all nine criteria, including the real-history independent-label comparison, material-weakening detection, non-gating lineage evolution, required-witness deletion control, exact owner-batch digest binding, material-delta digest mutation, stale binding rejection, label exclusion and patch-drift rejection.

## 5. Execution command

```text
.\.venv\Scripts\python.exe experiments\r8c_assurance_probe_v01\p_d2_ratchet_history.py ^
  --selection-commit d7f65392b851c03b49c246c023b0a6684ef3c60b ^
  --harness-commit 3ee7e4f547e98f5fd8bbf38fc7a5a760c6a47ed1 ^
  --output experiments\r8c_assurance_probe_v01\evidence\p_d2_run_002.json
```

No Attempt 002 result has been observed before this freeze.

## 6. Current state

```text
P_D2_ATTEMPT001=HARNESS_INVALID
P_D2_ATTEMPT002_HARNESS=FROZEN
P_D2_VALID_RESULT=NOT_YET_AVAILABLE
THRESHOLDS_CHANGED=false
LABELS_CHANGED=false

COMPLETED_VALID_DECISION_PROBES=5_OF_8
OWNER_ASSURANCE_DECISION=HELD
PHYSICAL_MIGRATION_AUTHORIZED=false
NEXT=EXECUTE_P_D2_ATTEMPT002
```
