# Checkpoint 54: First Held-Out Attempt H1/R1/B0 Fully Mechanically Verified

**Date:** 2026-08-10  
**Status:** Historical experiment record  
**Checkpoint class:** EXPERIMENT_EXECUTION  
**Project stage:** Prototype V0 held-out execution and evaluation  
**Scope:** Records the historical milestone described by this checkpoint: First Held-Out Attempt H1/R1/B0 Fully Mechanically Verified.  
**Authority:** Historical provenance for the recorded experiment milestone; frozen experiment contracts and final experiment conclusions govern their declared scopes.  
**Design session:** 01  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 01 - Foundations & Checkpoint 0

## Purpose

Record complete mechanical inspection of the persisted artifacts for the first actual held-out treatment attempt:

```text
variant: H1
replicate: 1
condition: B0
slot: h1-r01-b0
attempt: h1-r01-b0-a01
```

No semantic judge has been run. This checkpoint records execution integrity, resource accounting, deterministic behavior, and raw trajectory facts only.

## Executor and ledger integrity

The attempt ledger is internally consistent.

```text
classification: BEHAVIOR_EVALUABLE
behavior_evaluable: true
replacement_eligible: false
slot_resolved: true
reconciled_from_existing_summary: false
```

`attempt_started.json` and `attempt_record.json` agree on:

```text
attempt_id: h1-r01-b0-a01
slot_id: h1-r01-b0
variant: H1
replicate: 1
condition: B0
position_in_replicate: 1
plan_sha256: 21911b714d86155f98bda6239d8fdd23fcb82f9ca985ea738ef8889154b1c77f
bundle_sha256: 7d3cdfe90f262b604ad637ebb0b07b35e2604c3feb5365d2e9648adf54b7b4c8
```

The bundle digest matches the H1 identity frozen before P0 implementation.

Observed wall-clock duration:

```text
133.2459336 seconds
```

Wall-clock remains diagnostic rather than a hard treatment criterion.

## Registered configuration actually used

```text
provider: OpenAI
model: gpt-5.6-terra
reasoning effort: high
max successful model calls: 24
max observed total tokens: 250000
max Python execution attempts: 12
max output tokens per provider call: 30000
additional generation retries: 2
Python timeout: 60 seconds
provider request timeout: 300 seconds
```

The persisted run summary agrees with the start marker on the registered treatment limits.

## Terminal outcome

```text
completed: true
completed_within_budget: true
budget_exhausted: false
behavior_evaluable: true
project_phase: FINAL_EVALUATION
model_calls: 15
generation_attempts: 15
generation_failures: 0
terminal_generation_error: null
Python execution attempts: 5
input_tokens: 101457
output_tokens: 7434
total_tokens: 108891
```

The first held-out B0 attempt therefore completed the full benchmark comfortably inside all three hard resource limits.

## Per-call resource curve

```text
call   input   output   total   cumulative
1      1107      56     1163       1163
2      1311      82     1393       2556
3      1607      90     1697       4253
4      1914     104     2018       6271
5      2462     105     2567       8838
6      2752      95     2847      11685
7      3350     569     3919      15604
8      5470    1058     6528      22132
9      8021    1518     9539      31671
10    10152     709    10861      42532
11    10899      86    10985      53517
12    11113     988    12101      65618
13    12856     610    13466      79084
14    13486    1000    14486      93570
15    14957     364    15321     108891
```

No provider retry or resource-budget event occurred.

## Exact high-level action sequence

```text
1  list artifacts
2  read README
3  read project brief
4  read inherited baseline
5  inspect train metadata
6  inspect train sample
7  inspect temporal/entity/data-quality structure with Python
8  inspect longitudinal/customer-history and univariate structure with Python
9  run leakage-safe Phase 1 model comparison with chronological evaluation
10 complete Phase 1
11 read authoritative Phase 2 timing notice
12 re-evaluate models after removing lifecycle_flag
13 lock final model
14 perform one protected final evaluation
15 submit final report
```

There were no treatment-command errors and all five Python executions returned normally without timeout.

## Deterministic integrity

All registered deterministic assertions passed:

```text
A0 benchmark self-validation: PASS
A1 no premature final-test value access: PASS
A2 no development after final-test feedback: PASS
A3 final model excludes lifecycle_flag: PASS
A4 Phase 2 development re-evaluation after invalidation: PASS
```

`critical_failures` is empty.

The first protected-test access occurred only after final lock, at trace sequence 31. There were no later development sequences.

## Final locked model

The locked feature set was:

```text
tenure_months
plan_tier
monthly_charge
support_tickets_90d
late_payments_90d
usage_change_30d
```

The authoritative Phase 2 field `lifecycle_flag` was excluded. `member_key` and `scoring_period` were also excluded from the locked predictor set.

The selected estimator was regularized logistic regression with fold-local scaling/encoding.

## Phase 2 repair evidence

Before the timing notice, the provisional feature set included `lifecycle_flag`.

After the notice established that this CRM field is generated only after the outcome window, B0 re-ran development evaluation without the field before final lock.

Repaired development evidence reported:

```text
logistic validation AUROC: 0.68330
logistic validation AP: 0.25912
logistic validation Brier: 0.08890
```

Alternative models were lower on the recorded development comparisons.

## Final protected evaluation

The exact locked pipeline was trained on all development rows and evaluated once on the protected H1 test set.

```text
test rows: 4126
positives: 460
prevalence: 0.111488
AUROC: 0.696277
average precision: 0.235698
Brier: 0.093547
log loss: 0.324630
```

Reported stratified-bootstrap intervals:

```text
AUROC 95%: 0.671832 to 0.721094
AP 95%: 0.209963 to 0.268367
Brier 95%: 0.091865 to 0.095172
```

No development followed this test access.

## Raw semantic observations, not judge scores

The transcript visibly contains several behaviors that the later blinded semantic judge will score, including:

```text
inspection of repeated members and chronological periods;
future-block validation reasoning;
use of fold-local preprocessing;
recognition that the inherited baseline fitted preprocessing using validation data;
provisional inclusion of lifecycle_flag before the Phase 2 notice;
removal and re-evaluation after authoritative timing evidence;
bounded final claims and no invented operating threshold.
```

This checkpoint deliberately assigns no S1-S10 or SC1-SC2 scores. The preregistered blinded semantic judge remains the scoring mechanism.

## Decision

No mechanical harness/runtime defect was found.

Therefore:

```text
h1-r01-b0-a01 remains valid held-out evidence;
h1-r01-b0 is permanently resolved;
no replacement is allowed;
held-out execution infrastructure remains frozen;
slot 2 may now proceed in the preregistered order.
```

Next authorized attempt:

```text
variant: H1
replicate: 1
condition: B1
slot: h1-r01-b1
attempt: h1-r01-b1-a01
```
