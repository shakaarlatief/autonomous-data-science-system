# Research 306: P-S Stochastic Power Harness Freeze

**Date:** 2026-09-24
**Status:** P-S POWER HARNESS FROZEN / CALCULATION NOT YET RUN / FINAL PROBE RESULT NOT AVAILABLE
**Parent protocol:** Research 277
**Plan freeze:** Research 305 / `b693ca84722149e91e5a6e67b5d2b292491097ac`
**Harness commit:** `ae66a929b023d9fec805eb11a3a2c9b1155d74d8`
**Probe:** P-S
**Scope:** Freeze the deterministic stochastic-power desk-study calculator before any P-S calculation result is observed.
**Authority:** Probe-harness freeze only. It does not create decision-grade stochastic BLOCK evidence or authorize physical migration.

## 1. Frozen harness

The concrete P-S harness is:

```text
experiments/r8c_assurance_probe_v01/p_s_stochastic_power.py
```

with documentation in:

```text
experiments/r8c_assurance_probe_v01/README.md
```

Both are frozen at commit:

```text
ae66a929b023d9fec805eb11a3a2c9b1155d74d8
```

Git-blob content SHA-256 values:

```text
README.md
    5f689582cf2be51c619c3be842f1cca8dc38ca3ba22a4673cd4117e597e297bf

p_s_stochastic_power.py
    4e5b39e30e6219c7b414eb7d34f6542c85489a9fd885747d516bfaf725cc2aba
```

## 2. Frozen input binding

The harness loads the P-S plan only from the already-committed plan freeze:

```text
commit  b693ca84722149e91e5a6e67b5d2b292491097ac
path    experiments/r8c_assurance_probe_v01/p_s_power_study_plan.json
SHA256  a0894f9fcfa49311571de80fc6a91afdc19a5eb48d9104fd142591089d59f8d7
```

The plan in turn binds the three tracked Prototype V0 evidence/protocol artifacts at the pre-P-S source commit.

## 3. Calculation semantics

The calculator derives:

```text
per-item paired means
per-item paired sample variances
pooled within-item stochastic variance sigma^2
descriptive item-mean variance
descriptive truncated method-of-moments tau^2
naive pseudo-independent standard error
cluster-aware sensitivity standard error
required independent item counts across frozen MDE/R/tau grid
total candidate+baseline treatment execution counts
```

The sample-size axis is always independent benchmark items `J`, never raw repeated runs.

## 4. Frozen power approximation

The harness implements exactly the Research 305 planning approximation:

```text
J_required = ceil(
    (z_(1-alpha/2) + z_power)^2
    * (tau^2 + sigma^2/R)
    / delta^2
)
```

with:

```text
alpha = 0.05
power = 0.80
MDE = 0.30 / 0.20 / 0.10
R = 1 / 2 / 3 / 5
tau/sigma = 0 / 0.5 / 1 / 2
```

No post-result threshold selection is possible without changing the frozen plan/harness lineage.

## 5. Pseudo-independence negative control

The harness explicitly computes the misleading standard error obtained by treating all ten repeated paired runs as independent.

It then computes the current-design cluster-sensitive standard error under:

```text
tau = 2 * sigma
J = 2 independent benchmark items
R = 5 repeats per item
```

P-S requires the cluster-sensitive value to exceed the naive value and forbids the naive value from driving recommendations.

## 6. Decision-grade campaign contract

The emitted evidence preserves:

```text
paired candidate/baseline evaluation by item
item-clustered handling of repeated stochastic samples
one decisive metric
item-level public/private partitioning
all repeats for one item in one partition
no retry-to-green
current two-item Prototype V0 evidence = OBSERVE_ONLY for decision-grade BLOCK
```

The desk study therefore cannot accidentally upgrade the historical two-item corpus into generalizable blocking evidence.

## 7. Frozen result criteria

The harness contains eight result criteria:

```text
positive within-item stochastic variance
independent items distinguished from repeats
finite sample-size calculations across all frozen scenarios
conservative MDE 0.10 design within the 200-execution feasibility ceiling
pseudo-independence negative control
paired item-clustered future campaign model
item-level public/private split for blocking
no promotion of current two-item evidence to decision-grade generalization
```

All must pass for `P_S=PASS`.

## 8. Pre-execution validation

Before this freeze:

```text
Python compilation   PASS
git diff --check     PASS
P-S calculation      NOT RUN
```

No P-S result has been observed before the harness was committed and pushed.

## 9. Execution command

```text
.\.venv\Scripts\python.exe experiments\r8c_assurance_probe_v01\p_s_stochastic_power.py ^
  --harness-commit ae66a929b023d9fec805eb11a3a2c9b1155d74d8 ^
  --output experiments\r8c_assurance_probe_v01\evidence\p_s_run_001.json
```

## 10. Current state

```text
P_S_PLAN=FROZEN
P_S_HARNESS=FROZEN
P_S_EXECUTED=false
P_S_RESULT=NOT_AVAILABLE

COMPLETED_VALID_SCOPED_PROBES=7_OF_8
OWNER_ASSURANCE_DECISION=HELD
SPECIFICATION028=UNCHANGED
AO10=HELD
PHYSICAL_MIGRATION_AUTHORIZED=false

NEXT=EXECUTE_P_S
```
