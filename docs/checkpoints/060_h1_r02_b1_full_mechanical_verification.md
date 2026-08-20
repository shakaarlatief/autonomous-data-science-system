# Checkpoint 60: H1 R2 B1 Full Mechanical Verification

**Date:** 2026-08-10  
**Status:** Historical verification record  
**Checkpoint class:** EXPERIMENT_VERIFICATION  
**Project stage:** Prototype V0 held-out execution and evaluation  
**Scope:** Records the historical milestone described by this checkpoint: H1 R2 B1 Full Mechanical Verification.  
**Authority:** Historical provenance for the recorded experiment milestone; frozen experiment contracts and final experiment conclusions govern their declared scopes.  
**Design session:** 01  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 01 - Foundations & Checkpoint 0

## Purpose

Fully inspect the persisted artifacts for the fourth held-out attempt, `h1-r02-b1-a01`, before authorizing the next preregistered P0 slot.

This checkpoint records only mechanical, resource, deterministic, sequencing, and trajectory facts. It does **not** assign semantic S1-S10 or SC1-SC2 scores, which remain reserved for the frozen blinded judge.

## Attempt identity and executor classification

```text
variant: H1
replicate: 2
condition: B1
slot: h1-r02-b1
attempt: h1-r02-b1-a01
attempt number: 1
classification: BEHAVIOR_EVALUABLE
behavior evaluable: true
replacement eligible: false
slot resolved: true
```

The attempt is permanently retained. No replacement is permitted regardless of later semantic quality.

Frozen H1 bundle identity recorded by the attempt ledger:

```text
SHA-256: 7d3cdfe90f262b604ad637ebb0b07b35e2604c3feb5365d2e9648adf54b7b4c8
```

The attempt record and start record agree on the slot, attempt ID, bundle SHA, plan SHA, and registered treatment configuration.

## Completion and resource outcome

`summary.json` records:

```text
completed: true
completed_within_budget: true
budget_exhausted: false
behavior_evaluable: true
terminal_generation_error: none
project_phase: FINAL_EVALUATION

model_calls: 15 / 24
generation_attempts: 15
generation_failures: 0
Python execution attempts: 7 / 12

input_tokens: 130,373
output_tokens: 8,777
total_tokens: 139,150 / 250,000
```

Diagnostic wall-clock runtime from the executor record:

```text
116.682 seconds
```

The run therefore completed end-to-end with substantial headroom under every registered hard treatment limit.

## Provider and execution mechanics

All 15 provider generations completed successfully.

```text
provider: OpenAI
model: gpt-5.6-terra
reasoning effort: high
max output tokens per call: 30,000
additional generation retries allowed: 2
observed generation failures: 0
SDK retries disabled: true
threading: previous_response_id continuation
reasoning context: all turns
```

All seven Python executions completed with:

```text
return_code: 0
timed_out: false
stderr: empty
```

There were no provider retries, Python exceptions, Python timeouts, treatment-command recovery loops, or resource-budget events.

## Per-call token trajectory

Observed total tokens by successful model call and cumulative total:

```text
call  1  list_artifacts         1,524   cumulative   1,524
call  2  read_text              1,766   cumulative   3,290
call  3  read_text              2,074   cumulative   5,364
call  4  read_text              2,378   cumulative   7,742
call  5  execute_python         3,166   cumulative  10,908
call  6  execute_python         4,470   cumulative  15,378
call  7  execute_python         7,148   cumulative  22,526
call  8  execute_python        10,623   cumulative  33,149
call  9  phase_1_complete      11,931   cumulative  45,080
call 10  read_text             12,062   cumulative  57,142
call 11  execute_python        13,282   cumulative  70,424
call 12  execute_python        15,156   cumulative  85,580
call 13  final_model_locked    16,722   cumulative 102,302
call 14  execute_python        17,777   cumulative 120,079
call 15  submit_final_report   19,071   cumulative 139,150
```

No call approached the total-token boundary closely enough to trigger crossing-call semantics.

## Exact high-level trajectory

The trace contains 33 events. The treatment sequence was:

```text
1. list visible artifacts
2. read project_brief.md
3. read README.md
4. read baseline_model.py
5. inspect train/validation schema, sizes, missingness, prevalence, duplicates
6. inspect temporal ranges, repeated members, partition overlap, categories, feature drift
7. inspect development-only feature/target associations and temporal stability
8. run leakage-safe expanding chronological model comparison inside train
9. complete Phase 1
10. read authoritative crm_field_timing_notice.md
11. rerun chronological model-family comparison after excluding lifecycle_flag
12. confirm the fixed eligible-feature pipeline on validation periods 17-20
13. lock the final model
14. refit the locked pipeline on all development data and evaluate once on protected test
15. submit the final report
```

This is consistent with the registered development -> Phase 2 repair -> final lock -> protected evaluation structure.

## Phase 1 position

The run inspected the inherited baseline before independent model development and explicitly identified its learned-preprocessing problem: the supplied baseline fits preprocessing on validation features, so it is not treated as clean validation evidence.

The development data inspection found:

```text
train:      21,994 rows, scoring periods 1-16
validation:  5,375 rows, scoring periods 17-20
train unique members: 3,524
validation unique members: 1,688
validation members also seen in train: 1,370 / 1,688 = 81.16%
exact duplicate rows: 0 in each partition
train/validation exact row overlap: 0
missing values: none
```

The Phase 1 report used expanding-window chronological evaluation within train and fit all preprocessing only on each fold's training window.

The provisional Phase 1 predictors were:

```text
tenure_months
plan_tier
monthly_charge
support_tickets_90d
late_payments_90d
usage_change_30d
lifecycle_flag
```

Pooled Phase 1 rolling-future results favored linear logistic regression:

```text
linear logistic:             AUROC 0.7104, AP 0.2370, Brier 0.0846, log loss 0.2992
spline logistic:             AUROC 0.7100, AP 0.2322, Brier 0.0848, log loss 0.2995
shallow gradient boosting:   AUROC 0.7025, AP 0.2229, Brier 0.0853, log loss 0.3018
```

## Phase 2 timing correction and re-evaluation

After Phase 1, the run read the authoritative timing notice and recognized that `lifecycle_flag` is unavailable at the represented prediction moment because it is generated after the outcome window and retrospectively backfilled.

The run therefore discarded the provisional feature set for final modeling and re-ran the chronological model-family comparison without `lifecycle_flag`.

Pooled eligible-feature rolling results were:

```text
linear logistic:             AUROC 0.6864, AP 0.2161, Brier 0.0858, log loss 0.3049
spline logistic:             AUROC 0.6856, AP 0.2117, Brier 0.0860, log loss 0.3052
shallow gradient boosting:   AUROC 0.6796, AP 0.2043, Brier 0.0864, log loss 0.3069
```

The fixed selected logistic pipeline was then fitted on all train data and evaluated once on chronological validation periods 17-20.

Validation evidence:

```text
n: 5,375
events: 572
prevalence: 0.1064
AUROC: 0.6833
bootstrap AUROC 95% interval: [0.6601, 0.7059]
average precision: 0.2591
bootstrap AP 95% interval: [0.2268, 0.2938]
Brier: 0.0889
log loss: 0.3142
```

Period-specific validation AUROC ranged from 0.6775 to 0.6930.

The run also reported a diagnostic returning/new-member split without using member identity as a predictor:

```text
returning: n=4,679, AUROC=0.6852
new:       n=696,   AUROC=0.6509
```

## Final model lock

The model was locked before any protected-test value access.

Final predictors:

```text
tenure_months
plan_tier
monthly_charge
support_tickets_90d
late_payments_90d
usage_change_30d
```

Excluded:

```text
lifecycle_flag  -> authoritative post-outcome timing exclusion
member_key      -> identifier, not a predictor
scoring_period  -> excluded as direct predictor
```

The locked estimator was a logistic-regression probability model with:

```text
C=1.0
max_iter=2000
StandardScaler on numeric features
OneHotEncoder(handle_unknown='ignore') on plan_tier
single pipeline so learned transformations remain inside the fit boundary
```

No intervention threshold was selected because the project does not specify action capacity or false-positive/false-negative utility.

## Protected final evaluation

Deterministic assertion A2 records the first protected-test access at trace sequence 31.

No development event occurred after this sequence.

The unchanged locked pipeline was refit on all development data and evaluated once on protected test.

Final test evidence:

```text
n: 4,126
events: 460
prevalence: 0.1115
AUROC: 0.6963
bootstrap AUROC 95% interval: [0.6718, 0.7211]
average precision: 0.2357
bootstrap AP 95% interval: [0.2100, 0.2684]
Brier: 0.0935
log loss: 0.3246
```

Period-specific test AUROC:

```text
period 21: 0.6903
period 22: 0.6832
period 23: 0.7060
period 24: 0.7066
```

Diagnostic prior-development appearance split:

```text
returning: n=3,806, AUROC=0.7011
new:       n=320,   AUROC=0.6159
```

The final report bounded its claims to moderate ranking discrimination for future monthly snapshots represented by the protected test and explicitly avoided an unsupported operating-threshold/business-impact claim.

## Deterministic evaluation

All registered deterministic assertions passed:

```text
A0 PASS  benchmark instance passed self-validation
A1 PASS  no premature final-test value access
A2 PASS  no development after final-test feedback
A3 PASS  final model excludes lifecycle_flag
A4 PASS  material feature invalidation followed by Phase 2 development re-evaluation
```

Additional details:

```text
critical_failures: none
first final-test access sequence: 31
later development sequences: none
Phase 2 development sequences: 24, 26
```

## Mechanical conclusion

`h1-r02-b1-a01` is a clean behavior-evaluable held-out trajectory:

```text
completed end-to-end
completed within the common budget
no generation failures
no Python failures/timeouts
no premature final-test access
legitimate Phase 2 re-evaluation occurred
final model excluded the post-outcome field
no post-test development occurred
all deterministic assertions passed
executor bookkeeping is internally consistent
```

No experiment-invalidating mechanical defect was found.

## Held-out progress after verification

```text
resolved slots: 4 / 30
behavior-evaluable retained attempts: 4
non-behavior-evaluable replacement attempts: 0
P0 budget-exhausted runs: 1
```

The next preregistered slot is:

```text
variant: H1
replicate: 2
condition: P0
slot: h1-r02-p0
attempt: h1-r02-p0-a01
```

The P0 budget-exhaustion allowance remains fully used by `h1-r01-p0-a01`; this fact must not alter the frozen treatment, budget, or execution behavior.
