# Research 295: P-D2 Ratchet-History Harness Freeze

**Date:** 2026-09-24
**Status:** P-D2 HARNESS FROZEN / EXECUTION NOT YET RUN / NO OWNER ASSURANCE DECISION
**Parent protocol:** Research 277
**Selection/label freeze:** Research 294
**Candidate:** WARRANT-F V0.2
**Probe:** P-D2
**Frozen selection commit:** `d7f65392b851c03b49c246c023b0a6684ef3c60b`
**Frozen harness commit:** `c83313e150b8fbc0676e045c77137b69b322d790`
**Hash basis:** GIT_BLOB_BYTES_AT_COMMIT
**Scope:** Freeze the concrete label-blind P-D2 ratchet classifier, Git-history verification, negative controls and exact policy-diff binding before any P-D2 execution result is observed.
**Authority:** Probe-harness freeze only.

## 1. Independence boundary retained

Research 294 froze the real history sample and semantic labels at `d7f65392...` before any classifier existed.

The harness reads that exact committed fixture through Git object identity. The classifier receives only a sanitized input containing case ID, parent/head commits, selected patch digest and normalized policy delta. `independent_label` and `label_rationale` are excluded from classifier input, and the harness statically rejects a classifier implementation that references either field.

## 2. Ratchet classifier

The frozen classifier implements the Research 276 weakening dimensions directly:

```text
removed required claim          -> WEAKEN
lower consequence/threshold     -> WEAKEN
weaker trust                    -> WEAKEN
narrower/removed verifier       -> WEAKEN
weaker required witness         -> WEAKEN
wider waiver authority          -> WEAKEN
narrower governed input scope   -> REVIEW
```

Only after those weakening checks does lineage handling run.

For rename/move, split, merge, retirement/replacement and refactor operations, valid base-witness carry-forward permits `NEUTRAL`. Missing carry-forward forces `REVIEW`. Non-lineage additions/broadenings/stronger trust or witnesses become `STRENGTHEN`; otherwise the result is `NEUTRAL`.

This ordering is deliberate: a carrier move cannot hide a real policy weakening.

## 3. Real-history binding

For all ten frozen cases the harness independently recomputes:

```text
single parent identity
selected non-empty binary diff
selected patch SHA-256
selected patch byte count
added/removed evidence markers
```

A negative control corrupts one frozen patch digest and must be rejected.

## 4. Required-base-witness self-removal control

The preregistered self-weakening condition is exercised by cloning the lineage-neutral PD2-H03 rename/move policy delta and removing `base_witness_carry_forward`.

The mutated candidate must classify `WEAKEN` or `REVIEW`; it may not remain neutral/strengthening.

## 5. Exact policy-diff digest

The harness canonicalizes, in deterministic JSON order, each case's:

```text
case_id
parent_commit
head_commit
selected_patch_sha256
policy_delta
```

and SHA-256 hashes the complete batch.

One owner-batch binding is then created against exactly that digest. A material threshold mutation is applied after binding; the digest must change and the original binding must reject the mutated policy set.

This tests the Research 277 requirement that one owner decision can bind one exact policy-diff digest without making the Git carrier itself semantic authority.

## 6. Frozen files

```text
experiments/r8c_assurance_probe_v01/README.md
    9611225a2dc3ce7c6d14bef04303fc9459a9127d04eed52c3894f853e876bf5b

experiments/r8c_assurance_probe_v01/p_d2_ratchet_history.py
    bb8019eb60bb0fac9786f900727973b865574b859c51f873a9a13b13665505e4

selection fixture at d7f65392...
    experiments/r8c_assurance_probe_v01/p_d2_history_labels.json
    be70e8c3aa5f4dea2b9f2680ebaae1b4c09b1733a6f8a22da4edeb93d3f86072
```

The harness source compiled successfully and `git diff --check` passed before this freeze. The probe itself was not executed.

## 7. Frozen PASS discriminator

P-D2 returns `PASS` only if all frozen criteria hold:

1. every real-history label satisfies the Research 277 compatibility criterion;
2. every independently labelled material weakening is detected as `WEAKEN` or `REVIEW`;
3. lineage-preserving changes with carried witnesses are not owner-gated as weakening/review;
4. deliberate required-base-witness removal is blocked;
5. one exact owner-batch policy-diff digest accepts the original batch;
6. a material policy mutation changes that digest;
7. the stale original binding rejects the mutated batch;
8. classifier inputs structurally exclude frozen labels/rationales;
9. historical patch-digest drift is rejected.

No threshold may be changed after execution.

## 8. Execution command

```text
.\.venv\Scripts\python.exe experiments\r8c_assurance_probe_v01\p_d2_ratchet_history.py ^
  --selection-commit d7f65392b851c03b49c246c023b0a6684ef3c60b ^
  --harness-commit c83313e150b8fbc0676e045c77137b69b322d790 ^
  --output experiments\r8c_assurance_probe_v01\evidence\p_d2_run_001.json
```

No P-D2 execution result has been observed before this freeze.

## 9. Current state

```text
P_D2_SAMPLE=FROZEN_RESEARCH294
P_D2_HARNESS=FROZEN
P_D2_EXECUTED=false

COMPLETED_VALID_DECISION_PROBES=5_OF_8
OWNER_ASSURANCE_DECISION=HELD
SPECIFICATION028=UNCHANGED
AO10=HELD
PHYSICAL_MIGRATION_AUTHORIZED=false

NEXT=EXECUTE_P_D2
```
