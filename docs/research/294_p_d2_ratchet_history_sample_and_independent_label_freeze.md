# Research 294: P-D2 Ratchet-History Sample and Independent Label Freeze

**Date:** 2026-09-24
**Status:** P-D2 HISTORY SAMPLE + INDEPENDENT SEMANTIC LABELS FROZEN / CLASSIFIER NOT YET AUTHORED / NO P-D2 RESULT
**Parent protocol:** Research 277
**Candidate:** WARRANT-F V0.2
**Probe:** P-D2
**Fixture:** `experiments/r8c_assurance_probe_v01/p_d2_history_labels.json`
**Fixture SHA-256:** `be70e8c3aa5f4dea2b9f2680ebaae1b4c09b1733a6f8a22da4edeb93d3f86072`
**Authoring base:** `0ea3f7c1fb3c19d96ba69073e34670e83beea8ab`
**Scope:** Freeze the real-history sample, exact Git evidence bindings, mechanism-neutral policy deltas and independent semantic labels before any P-D2 ratchet classifier exists.
**Authority:** Empirical-fixture freeze only. It does not select or accept the assurance architecture and does not authorize physical migration.

## 1. Why this boundary exists

Research 277 requires P-D2 labels to exist independently before the ratchet classifier is run. The classifier must therefore be unable to define its own ground truth.

This boundary freezes the real historical changes selected for the probe, each exact parent/head Git pair, the exact selected paths and raw binary-diff SHA-256, the semantic assurance-policy delta projected from the historical change, the independent expected disposition, and the rationale for that disposition.

No P-D2 classifier or result exists at this checkpoint.

## 2. Frozen sample

Ten real historical changes are included.

| Case | Historical change | Required role in sample | Independent label |
|---|---|---|---|
| PD2-H01 | governed repository-integrity aggregate introduced | tightening / checks / workflow / tests | `STRENGTHEN` |
| PD2-H02 | architecture workflow `contents` authority expands read -> write | material weakening / trust | `WEAKEN` |
| PD2-H03 | LangGraph candidate package rename with workflow path carry-forward | rename/move | `NEUTRAL_LINEAGE` |
| PD2-H04 | temporary visual-baseline workflow retired while visual gate moves into enduring frontend CI | merge / lineage | `NEUTRAL_LINEAGE` |
| PD2-H05 | fixed-live-workflow test deleted and replaced by retirement-plus-provenance test | test deletion / lifecycle lineage | `NEUTRAL_LINEAGE` |
| PD2-H06 | Spec021 observer invocation changes from issue-opened surface to exact main-path push trigger | input-scope narrowing/change | `REVIEW` |
| PD2-H07 | frontend CI moves from `npm install` to locked `npm ci` | dependency/lock change / tightening | `STRENGTHEN` |
| PD2-H08 | async pytest marker replaced by `asyncio.run` with same integration assertions | neutral refactor | `NEUTRAL` |
| PD2-H09 | historical-intermediate checkpoint integrity added to validators/tests | validator/check tightening | `STRENGTHEN` |
| PD2-H10 | G014 repair expands schema and persistent-view qualification to complete W0 set | schema/validator/test tightening | `STRENGTHEN` |

The sample therefore covers every category preregistered by Research 277: tightening, weakening, rename/move, split/merge, test deletion, input-scope narrowing, dependency/lock change, and neutral formatting/refactor. It also spans tests, check scripts, workflows and schema/validator contracts.

## 3. Independent labels are semantic, not textual

The labels intentionally do not reduce to line-count or file-operation heuristics.

- PD2-H02 is `WEAKEN` even though the commit adds useful self-reporting behavior, because expanding `contents: read` to `contents: write` weakens a material least-privilege trust property.
- PD2-H05 is not labelled weakening merely because a test function disappears. The old lifecycle assertion is replaced by a new witness that requires the one-shot workflow to be gone while exact frozen provenance remains.
- PD2-H03 and PD2-H04 are lineage-neutral because required witness meaning carries across a move/merge of carriers.
- PD2-H06 is `REVIEW`, not automatically `WEAKEN`, because the invocation surface materially changes and narrows, but whether the narrower input domain is acceptable is a governed semantic question rather than a raw-diff fact.
- PD2-H08 remains neutral because the test execution mechanism changes while the asserted behavior is retained.

This is the discriminator P-D2 is intended to test.

## 4. Mechanism-neutral policy projection

Each case freezes a normalized `policy_delta` over the dimensions already established by Research 276:

```text
claim requirement
consequence floor
threshold
trust floor
input scope
verifier coverage
witness strength
waiver authority
lineage operation
base-witness carry-forward
```

The future classifier may consume this semantic delta and exact Git evidence binding. It may not consume `independent_label` or `label_rationale` while classifying.

That boundary prevents direct answer leakage while avoiding the opposite mistake of pretending a semantic assurance ratchet can be inferred reliably from unstructured Git text alone.

## 5. Exact Git evidence binding

Every case records its head commit, single parent commit, selected paths, `git diff --binary --find-renames=50%` patch SHA-256, patch byte count, historical commit subject and evidence markers.

The fixture was mechanically re-read after creation. All ten parent/head pairs resolve, every selected patch is non-empty, every patch digest and byte count recomputes exactly, every declared evidence marker occurs on the correct added/removed side, and all preregistered coverage categories are present.

```text
P-D2 label fixture validation PASS
cases 10
classifier_authored false
fixture_sha256 be70e8c3aa5f4dea2b9f2680ebaae1b4c09b1733a6f8a22da4edeb93d3f86072
```

## 6. Required classifier properties frozen before implementation

The next P-D2 harness must classify from the policy delta without label access and must satisfy at least these properties:

1. Weaker trust, lowered consequence/threshold/trust, narrowed governed inputs, removed required claim/verifier coverage, weakened required witnesses or widened waiver authority can never silently become `NEUTRAL` or `STRENGTHEN`.
2. Rename/move, split, merge or lifecycle replacement with valid witness carry-forward must be able to remain non-reviewing when assurance semantics are preserved.
3. A test/carrier deletion alone is not proof of weakening; disposition follows retained semantic coverage.
4. A candidate that removes its own required base witness must become `WEAKEN` or `REVIEW`, never neutral/pass.
5. The owner-batch decision representation must bind one exact canonical policy-diff digest, and any material policy-delta mutation must change that digest.
6. The frozen label and rationale fields must be structurally excluded from classifier input.

At least one deliberate negative control must remove a required carried witness from a lineage-neutral case, and one digest mutation control must prove that a material policy change changes the exact decision digest.

## 7. No result yet

This freeze establishes no evidence about whether WARRANT-F V0.2 passes P-D2.

```text
P_D2_SAMPLE=FROZEN
P_D2_LABELS=FROZEN_INDEPENDENTLY
P_D2_CLASSIFIER=NOT_AUTHORED
P_D2_RESULT=NOT_RUN

COMPLETED_VALID_PROBES=5_OF_8
OWNER_ASSURANCE_DECISION=HELD
SPECIFICATION028=UNCHANGED
AO10=HELD
PHYSICAL_MIGRATION_AUTHORIZED=false

NEXT=AUTHOR_AND_FREEZE_P_D2_RATCHET_HARNESS
```
