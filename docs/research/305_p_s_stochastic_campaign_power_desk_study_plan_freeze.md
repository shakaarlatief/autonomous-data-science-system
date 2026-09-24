# Research 305: P-S Stochastic Campaign Power Desk-Study Plan Freeze

**Date:** 2026-09-24
**Status:** P-S ANALYSIS PLAN FROZEN / POWER CALCULATION NOT YET RUN / NO OWNER ASSURANCE DECISION
**Parent protocol:** Research 277
**Candidate:** WARRANT-F V0.2
**Probe:** P-S
**Frozen plan commit:** `b693ca84722149e91e5a6e67b5d2b292491097ac`
**Plan:** `experiments/r8c_assurance_probe_v01/p_s_power_study_plan.json`
**Plan Git-blob content SHA-256:** `a0894f9fcfa49311571de80fc6a91afdc19a5eb48d9104fd142591089d59f8d7`
**Source evidence commit:** `a6ab12426df1bc06676b6631ca2a6305cf3b64f4`
**Scope:** Freeze the source-bound stochastic power-study model, MDE grid, clustering semantics, negative control, public/private release rule and P-S discriminator before any power calculation is executed.
**Authority:** Desk-study plan freeze only. No stochastic BLOCK claim or total assurance-architecture decision is authorized.

## 1. Preserved evidence selected

P-S uses only already-preserved Prototype V0 held-out evidence. No new live model call is permitted.

Three tracked source artifacts are bound at the pre-P-S source commit:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
    ce508bcfff678a812ea49ddb3745adc90347281035b7930dc0c1ed8aa81280ae

docs/foundations/012_preregistered_held_out_evaluation_protocol.md
    d9f226ee72ec71e1fd4108ca57e31ac911bca55d3270c944a22c277c9cce11f3

prototype_v0/configs/held_out_protocol_v0_1.json
    086447b3a227bb7713db95faffa42abfb7649496f2829f88278b7251ea33cc32
```

A local ignored decoded-results file exists, but it is deliberately not load-bearing for this desk study. The tracked final result already preserves the exact paired score differences and summary facts required.

## 2. Independence unit is frozen before calculation

The preserved experiment contains:

```text
independent benchmark items:  H1, H2
paired stochastic repeats:    5 per item
paired run differences:       10 total
```

The paired P0 minus B1 targeted-architecture-score differences are:

```text
H1: +0.10, 0.00, 0.00, 0.00, +0.20
H2:  0.00, +0.20, 0.00, 0.00,  0.00
```

The crucial preregistered rule is:

> Ten repeated paired runs are not ten independent benchmark items.

The desk study must treat repeats as stochastic observations nested within the two benchmark-item clusters.

## 3. Primary metric and paired model

The sole decisive metric for this desk study is the already-defined:

`targeted_architecture_score` on the 0-2 scale.

The primary comparison remains P0 versus B1 because Foundation 012 used B1 as the matched static-knowledge baseline.

The frozen planning model is:

```text
d_ir = mu + u_i + e_ir

u_i  item-level effect heterogeneity, Var = tau^2
e_ir within-item stochastic paired residual, Var = sigma^2

Var(item mean) = tau^2 + sigma^2 / R
Var(grand mean) = (tau^2 + sigma^2 / R) / J
```

where `J` is the number of independent benchmark items and `R` the paired stochastic repetitions per item.

## 4. Within-item variance and between-item uncertainty

The within-item stochastic variance is estimated by pooling the ordinary sample variances of the repeated paired differences within H1 and H2.

Between-item heterogeneity cannot be estimated reliably from only two items. The study may report a method-of-moments value descriptively, but it may not treat a zero estimate as evidence that true item heterogeneity is zero.

Instead, sample-size planning is frozen over:

```text
tau / sigma = 0.0, 0.5, 1.0, 2.0
```

This makes item heterogeneity an explicit sensitivity dimension rather than hidden optimism.

## 5. Power and MDE contract

The desk study uses a two-sided large-sample normal planning approximation:

```text
alpha = 0.05
target power = 0.80

J_required = ceil(
    (z_(1-alpha/2) + z_power)^2
    * (tau^2 + sigma^2 / R)
    / delta^2
)
```

The MDE grid is frozen as:

```text
0.30  primary pre-existing material effect
0.20  planning sensitivity only
0.10  planning sensitivity only
```

`0.30` is not invented for this probe. It was preregistered in Foundation 012 as the targeted-score material-reliability alternative.

The smaller effects are sensitivity calculations, not new acceptance thresholds. The observed historical `+0.05` difference is descriptive only and may not be promoted into a post-hoc target.

Repeat counts are evaluated at:

```text
R = 1, 2, 3, 5
```

## 6. Pre-frozen feasibility discriminator

P-S can PASS only if all frozen requirements hold.

In particular, under the conservative sensitivity:

```text
tau = 2 * sigma
MDE <= 0.10
alpha = 0.05
power = 0.80
R in {2,3,5}
```

there must exist a design requiring no more than:

```text
200 total candidate + baseline treatment executions
```

The 200-run bound is a probe-specific engineering-feasibility ceiling, not a permanent production campaign budget. It prevents the architecture from passing merely because an arbitrarily huge theoretical sample is finite.

## 7. Pseudo-independence negative control

The study must calculate the naive standard error produced by pretending the ten repeated pairs are ten independent items.

It must then compare that value with a cluster-aware current-study sensitivity standard error under `tau = 2*sigma`.

Required behavior:

```text
cluster-aware sensitivity SE > naive pseudo-independent SE
```

The naive value may never drive the sample-size recommendation.

This directly tests the Research 277 rule not to invent independence where item clustering exists.

## 8. Public/private confirmatory split

Decision-grade stochastic BLOCK evidence requires an item-level separation:

```text
PUBLIC / DEVELOPMENT
    variance estimation
    harness/judge calibration
    MDE and analysis preregistration

PRIVATE / HELD-OUT
    untouched confirmatory items
    final candidate-baseline campaign
    release/BLOCK evidence
```

All stochastic repeats for one benchmark item must stay in the same partition. Splitting repeats of the same item across public and private sets would leak item identity and manufacture pseudo-holdout evidence.

This is stricter than merely hiding condition labels and aligns with WARRANT-F V0.2's explicit public-development/private-held-out requirement.

## 9. Interpretation boundary

Even if P-S passes, the existing Prototype V0 experiment does not become decision-grade evidence for a general AI-quality BLOCK claim.

It has only two independent benchmark items.

A PASS would mean that preserved ADS evidence is sufficient to design a statistically coherent future campaign with:

```text
preregistered effect/MDE
justified item sample size
paired candidate/baseline evaluation
item-clustered treatment of repeats
public/private item separation
one decisive metric
no retry-to-green
```

not that the old 10 repeated pairs already satisfy those requirements.

## 10. Frozen next sequence

```text
plan committed/pushed
-> implement deterministic desk-study calculator
-> validate without executing the P-S result
-> commit/push calculator
-> Git-blob freeze harness
-> execute exact frozen calculator
-> reconcile PASS / AMEND / INCONCLUSIVE
```

## 11. Current state

```text
P_S_PLAN=FROZEN
P_S_POWER_CALCULATION=NOT_RUN
P_S_RESULT=NOT_AVAILABLE

COMPLETED_VALID_SCOPED_PROBES=7_OF_8
OWNER_ASSURANCE_DECISION=HELD
SPECIFICATION028=UNCHANGED
AO10=HELD
PHYSICAL_MIGRATION_AUTHORIZED=false

NEXT=IMPLEMENT_AND_FREEZE_P_S_POWER_HARNESS
```
