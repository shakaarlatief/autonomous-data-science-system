# Research 298: P-D2 Ratchet-History Attempt 002 PASS

**Date:** 2026-09-24
**Status:** P-D2 PASS / VALID RESULT / NO TARGET AMENDMENT REQUIRED / OWNER ASSURANCE DECISION STILL HELD
**Parent protocol:** Research 277
**Selection/label freeze:** Research 294 / `d7f65392b851c03b49c246c023b0a6684ef3c60b`
**Attempt 001:** Research 296 / `HARNESS_INVALID`
**Attempt 002 harness freeze:** Research 297 / `3ee7e4f547e98f5fd8bbf38fc7a5a760c6a47ed1`
**Probe:** P-D2
**Result evidence:** `experiments/r8c_assurance_probe_v01/evidence/p_d2_run_002.json`
**Evidence SHA-256:** `bdcfaa9c2dc89875b8500f2b1d9816313d16b6d490412b51c4d0d1c5a36c35a7`
**Scope:** Reconcile the valid Attempt 002 result against the preregistered P-D2 discriminator.
**Authority:** Empirical probe result only. It does not yet select the total assurance architecture or authorize physical migration.

## 1. Result

Attempt 002 returns:

```text
P_D2=PASS
history cases      10 / 10 classified
criteria           9 / 9 PASS
policy diff digest c1b1b03023da5e2ef5a153a6d6d92ff358d51a2785e37b76edd7645ade486f75
```

The repaired harness reached the actual discriminator after Attempt 001's hash-basis-only harness failure. No threshold, label, classifier semantic, policy delta, negative control or selection fixture changed between the invalid and valid attempts.

## 2. Independent historical labels

Every frozen semantic label satisfied its preregistered criterion:

| Case | Frozen label | Ratchet classification |
|---|---|---|
| PD2-H01 | STRENGTHEN | STRENGTHEN |
| PD2-H02 | WEAKEN | WEAKEN |
| PD2-H03 | NEUTRAL_LINEAGE | NEUTRAL |
| PD2-H04 | NEUTRAL_LINEAGE | NEUTRAL |
| PD2-H05 | NEUTRAL_LINEAGE | NEUTRAL |
| PD2-H06 | REVIEW | REVIEW |
| PD2-H07 | STRENGTHEN | STRENGTHEN |
| PD2-H08 | NEUTRAL | NEUTRAL |
| PD2-H09 | STRENGTHEN | STRENGTHEN |
| PD2-H10 | STRENGTHEN | STRENGTHEN |

Most importantly, the explicit trust weakening in PD2-H02 is not admitted as neutral/strengthening, while all three lineage-preserving carrier/lifecycle changes remain non-owner-gated when their base witness is carried.

## 3. Self-weakening negative control

The harness removes `base_witness_carry_forward` from the lineage-neutral PD2-H03 policy delta.

Observed:

```text
classification = REVIEW
blocked        = true
```

A candidate therefore cannot remove the required base witness from this lineage-preserving change and remain neutral/pass.

## 4. Exact policy-diff binding

The original ten-case batch produces:

```text
c1b1b03023da5e2ef5a153a6d6d92ff358d51a2785e37b76edd7645ade486f75
```

A material threshold mutation produces:

```text
8de644d6125c04232f87bda3659d6b14538e242a2e7218f1a4ff1385ff920ebb
```

The digests differ and the original owner-batch binding rejects the mutated policy set.

This demonstrates the intended exact decision-binding semantics without making the Git carrier itself the semantic authority.

## 5. History-integrity and label-blindness controls

All ten exact historical patch bindings revalidated. A deliberately corrupted patch digest is rejected.

The classifier input structurally excludes the frozen `independent_label` and `label_rationale` fields, and the classifier implementation is checked for direct reference to either field.

Therefore the PASS is not obtained by feeding the expected answer into the classifier.

## 6. Preregistered criteria reconciliation

Research 277 P-D2 required:

```text
material weakening -> WEAKEN or REVIEW
lineage-preserving refactor with carried witness -> not unexplained weakening
self-removal of required base witness -> cannot become PASS
batched owner decision -> exact policy-diff digest binding
```

All four are satisfied, with additional negative controls for patch drift, stale batch binding and material-delta digest mutation.

Therefore:

```text
P_D2=PASS
WARRANT_F_V0_2_AMENDMENT_REQUIRED_BY_P_D2=false
```

## 7. Limits

This is bounded empirical evidence, not universal proof that every future policy edit will be semantically classified correctly. The probe establishes that the proposed ratchet semantics can distinguish the preregistered representative historical classes, including a real material weakening, without systematically owner-gating valid lineage-preserving evolution.

It also does not select GitHub, Git branches, the current workflow topology, pytest, or any current carrier as target architecture.

## 8. Program state

P-D2 becomes the sixth decision-relevant probe with a valid/scoped result.

```text
P_H=INCONCLUSIVE / scoped provider evidence
P_D6=PASS
P_D3=PASS
P_D5=PASS
P_D1=PASS
P_D2=PASS

COMPLETED_VALID_SCOPED_PROBES=6_OF_8
REMAINING=P_D4,P_S

OWNER_ASSURANCE_DECISION=HELD
SPECIFICATION028=UNCHANGED
AO10=HELD
FILE_LEVEL_MIGRATION=HELD
PHYSICAL_MIGRATION_AUTHORIZED=false
AUTHORITY_SWITCH_ALLOWED=false

NEXT=P_D4_CURRENT_ORACLE_SUCCESSOR_FEASIBILITY
```
