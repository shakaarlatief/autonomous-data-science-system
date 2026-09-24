# Research 296: P-D2 Attempt 001 Harness Invalid and Prospective Hash-Basis Repair

**Date:** 2026-09-24
**Status:** P-D2 ATTEMPT 001 HARNESS_INVALID / NO ARCHITECTURE INFERENCE / NARROW HASH-BASIS REPAIR AUTHORIZED / NO OWNER ASSURANCE DECISION
**Parent protocol:** Research 277
**Selection/label freeze:** Research 294 / `d7f65392b851c03b49c246c023b0a6684ef3c60b`
**Harness freeze:** Research 295 / `c83313e150b8fbc0676e045c77137b69b322d790`
**Probe:** P-D2
**Attempt:** 001
**Scope:** Preserve the first P-D2 execution failure, classify it under the preregistered harness-failure semantics, and authorize only the prospective binding repair required to reach the discriminator.
**Authority:** Empirical failure record and narrow repair authorization only. No assurance-architecture conclusion is authorized from this attempt.

## 1. Frozen execution attempted

The exact Research 295 command was executed after the selection and harness commits had both been committed, pushed and frozen:

```text
selection commit  d7f65392b851c03b49c246c023b0a6684ef3c60b
harness commit    c83313e150b8fbc0676e045c77137b69b322d790
output            experiments/r8c_assurance_probe_v01/evidence/p_d2_run_001.json
```

Execution stopped before any historical case was classified.

## 2. Observed defect

The harness retrieves the selection fixture using:

```text
git show d7f65392...:experiments/r8c_assurance_probe_v01/p_d2_history_labels.json
```

and therefore hashes Git blob content bytes.

Research 294 had recorded the fixture SHA-256 from the Windows working-tree materialization:

```text
be70e8c3aa5f4dea2b9f2680ebaae1b4c09b1733a6f8a22da4edeb93d3f86072
```

The actual committed Git blob content at the frozen selection commit is:

```text
Git blob object             257fa5fa7fcf2d1438f28b24f277ad70c17779d8
Git blob content bytes      18491
Git blob content SHA-256    3946655c69bba95d5f7b606e8a25cb1a2be1119e5613dfb4e3ecf9dbf515fc43
```

The mismatch is consistent with the already-known cross-platform working-tree versus Git-blob byte issue that earlier corrected R8-B qualification by moving load-bearing hashes to `GIT_BLOB_BYTES_AT_COMMIT`.

The failure occurred at fixture binding, before:

```text
classifier execution
real-history label comparison
required-witness removal control
policy-diff digest control
architecture interpretation
```

A durable attempt record is preserved at:

`experiments/r8c_assurance_probe_v01/evidence/p_d2_run_001_harness_invalid.json`.

## 3. Classification

Under Research 277:

```text
P_D2_ATTEMPT_001=HARNESS_INVALID
TARGET_ARCHITECTURE_INFERENCE=NONE
```

This is not `AMEND`: no ratchet discriminator was reached.

This is not `PASS`: no P-D2 criterion was evaluated.

This is not evidence against the frozen independent history labels. Their exact committed object remains unchanged.

## 4. Allowed prospective repair

The only authorized repair is to bind the selection fixture using the committed Git blob content SHA-256:

```text
EXPECTED_FIXTURE_SHA256
    be70e8c... -> 3946655c...
```

The repaired harness may additionally rename/comment that constant to make the Git-blob byte basis unambiguous, but it must not change:

```text
the ten selected historical cases
their independent labels or rationales
any policy_delta
classifier rules
PASS/AMEND criteria
label-visibility boundary
negative controls
canonical policy-diff digest algorithm
selection commit
historical patch bindings
```

## 5. Methodological effect

The repair changes only how the already-frozen fixture identity is verified. It cannot make any historical case easier or harder for the ratchet classifier.

Therefore:

```text
THRESHOLDS_CHANGED=false
LABELS_CHANGED=false
CLASSIFIER_CHANGED=false
ARCHITECTURE_CANDIDATE_CHANGED=false
```

## 6. Required next sequence

```text
preserve Attempt 001 HARNESS_INVALID
-> repair the frozen-fixture expected hash only
-> syntax/integrity validation without executing P-D2
-> commit and push repaired harness
-> compute Git-blob harness hashes
-> prospectively refreeze Attempt 002
-> execute Attempt 002
```

## 7. Current state

```text
P_D2_ATTEMPT_001=HARNESS_INVALID
P_D2_VALID_RESULT=NOT_YET_AVAILABLE
REPAIR_SCOPE=SELECTION_FIXTURE_GIT_BLOB_HASH_ONLY
REPAIR_EXECUTED=false

COMPLETED_VALID_DECISION_PROBES=5_OF_8
OWNER_ASSURANCE_DECISION=HELD
SPECIFICATION028=UNCHANGED
AO10=HELD
PHYSICAL_MIGRATION_AUTHORIZED=false

NEXT=REPAIR_AND_REFREEZE_P_D2_ATTEMPT002
```
