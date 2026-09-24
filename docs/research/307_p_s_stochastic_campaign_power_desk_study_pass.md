# Research 307: P-S Stochastic Campaign Power Desk-Study PASS

**Date:** 2026-09-24
**Status:** P-S PASS / FUTURE DECISION-GRADE CAMPAIGN DESIGNABLE / CURRENT TWO-ITEM EVIDENCE REMAINS OBSERVE-ONLY / ALL EIGHT PROBES RECONCILED
**Parent protocol:** Research 277
**Plan freeze:** Research 305 / `b693ca84722149e91e5a6e67b5d2b292491097ac`
**Harness freeze:** Research 306 / `ae66a929b023d9fec805eb11a3a2c9b1155d74d8`
**Probe:** P-S
**Evidence:** `experiments/r8c_assurance_probe_v01/evidence/p_s_run_001.json`
**Evidence SHA-256:** `51250bf76f110473e5093bb147e60dece8c698893ae79b0b92177203c8a5c3c5`
**Scope:** Reconcile the exact frozen P-S desk-study result against the preregistered stochastic-campaign discriminator.
**Authority:** Empirical probe result only. It does not itself authorize a stochastic BLOCK claim, physical migration, or the final owner architecture decision.

## 1. Result

The exact Research 306 harness returns:

```text
P_S=PASS
criteria=8/8 PASS
pooled within-item variance sigma^2 = 0.008
pooled within-item SD sigma         = 0.0894427191
```

No MDE, power target, heterogeneity sensitivity, repeat grid, feasibility ceiling or decision criterion changed after observation.

## 2. Preserved evidence structure

The source evidence contains only two independent benchmark-item clusters:

```text
H1 paired P0-B1 differences
    +0.10, 0.00, 0.00, 0.00, +0.20
    mean = 0.06

H2 paired P0-B1 differences
     0.00, +0.20, 0.00, 0.00, 0.00
    mean = 0.04

grand mean of item effects = 0.05
```

Each item contributes five repeated stochastic paired observations. The ten repeats are not treated as ten independent benchmark items.

## 3. Variance evidence

Both item clusters have paired sample variance `0.008`, giving:

```text
pooled within-item sigma^2 = 0.008
sigma                       = 0.0894427191
```

The sample variance of the two item means is `0.0002`.

The truncated method-of-moments between-item variance estimate is zero, but the harness explicitly refuses to interpret this as evidence that population heterogeneity is zero because `J=2` is insufficient to identify between-item variability reliably.

Therefore sample-size planning uses the frozen `tau/sigma` sensitivity grid rather than the descriptive `tau_hat` as truth.

## 4. Pseudo-independence negative control

Naively treating all ten paired repeats as independent gives:

```text
naive n  = 10
naive SE = 0.0268741925
```

Under the conservative frozen item-heterogeneity sensitivity `tau = 2*sigma`, the cluster-aware standard error for the actual current design is:

```text
J = 2
R = 5
cluster-aware SE = 0.1296148140
```

The cluster-aware value is much larger than the naive value.

Thus the probe visibly rejects pseudo-replication and the naive run-level standard error is forbidden from driving a decision-grade recommendation.

## 5. Conservative MDE 0.10 feasibility result

Under:

```text
alpha = 0.05
power = 0.80
MDE = 0.10
tau = 2*sigma
```

the frozen candidate designs are:

| Repeats per item | Required independent items | Candidate+baseline treatment executions |
|---:|---:|---:|
| 2 | 29 | 116 |
| 3 | 28 | 168 |
| 5 | 27 | 270 |

The preregistered feasibility rule required at least one `R in {2,3,5}` design at no more than 200 total treatment executions.

`R=2`, `J=29` satisfies that discriminator at 116 total candidate+baseline executions.

This is a desk-study planning result, not a permanent production campaign recommendation.

## 6. Broader frozen sensitivity grid

Finite required independent-item counts were produced for every frozen combination of:

```text
MDE        0.30 / 0.20 / 0.10
R          1 / 2 / 3 / 5
tau/sigma  0 / 0.5 / 1 / 2
```

The pre-existing material effect `0.30` remains distinct from the `0.20` and `0.10` planning-sensitivity calculations.

The historical observed `+0.05` mean is not converted into a post-hoc acceptance target.

## 7. Decision-grade campaign shape supported

The evidence supports a future campaign discipline with:

```text
paired candidate/baseline evaluation within item
independent benchmark items as the sample-size axis
item-clustered treatment of repeated stochastic samples
one decisive metric per claim
preregistered MDE / power / sample size
no retry-to-green
item-level public-development/private-held-out separation
all repeats of one item kept in one partition
```

This satisfies the Research 277 P-S architecture criterion that at least one realistic campaign shape supports preregistered power/MDE reasoning and paired/item-clustered analysis.

## 8. Current evidence remains OBSERVE_ONLY

P-S does not upgrade the existing Prototype V0 result into a decision-grade generalization claim.

Only two independent benchmark items were observed. They are adequate to estimate within-item stochastic variability for this desk study, but not to establish robust population-level item heterogeneity or a general stochastic BLOCK claim.

Accordingly:

```text
CURRENT_PROTOTYPE_V0_DECISION_GRADE_GENERALIZATION=false
CURRENT_PROTOTYPE_V0_BLOCK_STATUS=OBSERVE_ONLY
FUTURE_DECISION_GRADE_CAMPAIGN_DESIGNABLE=true
```

## 9. Architecture interpretation

The frozen result supports WARRANT-F V0.2's stochastic decision model:

```text
preregistered effect/MDE
justified item sample size
paired candidate/baseline evaluation
item-clustered repeated-sample analysis
public-development/private-held-out distinction
no retry-to-green
```

No different stochastic-decision architecture is required by P-S.

Therefore:

```text
P_S=PASS
WARRANT_F_V0_2_AMENDMENT_REQUIRED_BY_P_S=false
```

## 10. Eight-probe program state

P-S is the eighth and final decision-relevant probe.

```text
P_H=INCONCLUSIVE / explicitly scoped current-host capability evidence
P_D6=PASS
P_D3=PASS
P_D5=PASS
P_D1=PASS
P_D2=PASS
P_D4=PASS
P_S=PASS

COMPLETED_VALID_OR_SCOPED_PROBES=8_OF_8
UNRESOLVED_AMEND_RESULTS=0
ACTIVE_HARNESS_INVALID_RESULTS=0

OWNER_ASSURANCE_DECISION=READY_FOR_TOTAL_RECONCILIATION
SPECIFICATION028=UNCHANGED
AO10=HELD
FILE_LEVEL_MIGRATION=HELD
PHYSICAL_MIGRATION_AUTHORIZED=false
AUTHORITY_SWITCH_ALLOWED=false

NEXT=R8C_TOTAL_PROBE_RECONCILIATION_AND_OWNER_DECISION_READINESS
```
