# Checkpoint 62: H1 R2 P0 Full Mechanical Verification

**Date:** 2026-08-10

## Scope

Mechanically inspect the complete persisted artifact set for the second held-out P0 attempt:

```text
h1-r02-p0-a01
```

This checkpoint records completion, resource accounting, deterministic assertions, protected-test sequencing, P0 state transitions, dependency repair, knowledge activation, and executor-record consistency. It does **not** assign semantic S1-S10 or SC1-SC2 scores and does not draw an architectural conclusion from this single run.

## Executor identity and retention status

The persisted executor records agree on:

```text
variant: H1
replicate: 2
condition: P0
slot: h1-r02-p0
attempt: h1-r02-p0-a01
attempt number: 1
classification: BEHAVIOR_EVALUABLE
behavior_evaluable: true
replacement_eligible: false
slot_resolved: true
```

The attempt therefore remains permanently in the held-out experiment and cannot be replaced.

The attempt-start and attempt-record files agree on the frozen H1 bundle identity:

```text
SHA-256: 7d3cdfe90f262b604ad637ebb0b07b35e2604c3feb5365d2e9648adf54b7b4c8
```

and on the materialized run-plan identity:

```text
plan SHA-256: 21911b714d86155f98bda6239d8fdd23fcb82f9ca985ea738ef8889154b1c77f
```

## Completion and resource outcome

`summary.json` records:

```text
completed: true
completed_within_budget: true
budget_exhausted: false
behavior_evaluable: true
project_phase: FINAL_EVALUATION
terminal_generation_error: null
```

Registered envelope versus observed use:

```text
successful model calls: 12 / 24
generation attempts: 12
generation failures: 0
Python execution attempts: 5 / 12

input tokens: 216,642
output tokens: 10,284
total tokens: 226,926 / 250,000
```

The run therefore completed fully within the frozen token, call, and Python ceilings. Unlike `h1-r01-p0-a01`, no token-ceiling crossing occurred.

Approximate executor wall-clock duration recorded in `attempt_record.json`:

```text
122.17 seconds
```

## Deterministic assertions

All registered deterministic assertions passed:

```text
A0 PASS  benchmark instance passed self-validation
A1 PASS  no premature final-test value access
A2 PASS  no development after final-test feedback
A3 PASS  final model excludes established post-outcome feature
A4 PASS  material feature invalidation followed by development re-evaluation
```

There are no deterministic critical failures.

A2 records:

```text
first_final_test_access_sequence: 28
later_development_sequences: []
```

A3 records the final six selected features:

```text
tenure_months
plan_tier
monthly_charge
support_tickets_90d
late_payments_90d
usage_change_30d
```

A4 records that Phase 1 had provisionally included `lifecycle_flag`, while Phase 2 performed development re-evaluation at trace sequences 21 and 23 after the timing correction.

## Execution trajectory

The raw trace contains 30 events and no blocked action, runtime error, recovery loop, provider failure, Python timeout, or resource-budget event.

The main trajectory is:

```text
read project brief
-> read README
-> read inherited baseline
-> inspect train/validation schema, periods, repeated members, and overlap
-> leakage-safe Phase 1 model comparison
-> Phase 1 complete
-> authoritative timing notice released and read
-> eligible-feature Phase 2 model comparison
-> uncertainty / temporal / returning-versus-new validation analysis
-> final model lock
-> protected final evaluation
-> final report
```

All five Python executions returned code 0, with no timeout and empty stderr.

## Inherited preprocessing boundary

The terminal state contains the active fact:

```text
F-0004
Inherited baseline fits StandardScaler and OneHotEncoder on concatenated train and validation features before scoring validation, violating the training-only transformation boundary.
```

The inherited baseline result was therefore not treated as clean development evidence.

The associated knowledge component `K-INFO-002` activated and created a blocking verification obligation, which was later satisfied after the boundary issue was resolved.

## Validation regime and repeated entities

The inspection established:

```text
train periods: 1-16
validation periods: 17-20
train rows: 21,994
validation rows: 5,375
validation members also seen in train: 1,370 / 1,688
```

The terminal state preserves the accepted decision to use the provided forward temporal split to estimate future-snapshot performance for the natural mix of returning and new customers, while excluding `member_key` as a predictor.

The run also preserved the accepted AUROC model-selection decision, with AP and Brier as supplementary diagnostics.

## Phase 1 provisional evidence

With training-only preprocessing and the Phase 1 feature set including `lifecycle_flag`, the run recorded:

```text
logistic AUROC: 0.724718
logistic AP: 0.279321
logistic Brier: 0.087132

HistGradientBoosting AUROC: 0.711107
random forest AUROC: 0.695043
```

This evidence became `E-0001` and the associated provisional logistic decision became `D-0003`.

## Authoritative Phase 2 timing correction

After reading `crm_field_timing_notice.md`, the run created the active fact:

```text
F-0007
lifecycle_flag is generated after the monthly churn window closes and retrospectively backfilled, so it is unavailable at beginning-of-month scoring and must be excluded.
```

It also accepted the explicit feature-exclusion decision `D-0004`.

The important state transitions were:

```text
Q-0007  OPEN -> RESOLVED
D-0003  PROVISIONAL -> REOPENED
E-0001  CURRENT -> INVALIDATED
O-0004  created OPEN after support loss from E-0001
```

The controller then selected an eligible-feature development comparison before permitting model lock.

## Replacement development evidence

The Phase 2 comparison excluding `lifecycle_flag` produced:

```text
logistic
AUROC: 0.683297
AP: 0.259117
Brier: 0.088899

HistGradientBoosting
AUROC: 0.666377

random forest
AUROC: 0.656174
```

The run created current replacement evidence `E-0002` and accepted replacement model decision `D-0005`.

The old model decision then became:

```text
D-0003  REOPENED -> SUPERSEDED
```

and `O-0004` was satisfied after the replacement evidence was established.

A second support-loss obligation, `O-0005`, was created when `D-0003` became superseded and was then automatically satisfied under the controller's obligation-support semantics.

## Noteworthy typed-state dependency behavior

One exact state transition is worth preserving for later architecture-level analysis without scoring it here.

`Q-0007`, the lifecycle timing question, had a hard `DEPENDS_ON` relation to the provisional model decision `D-0003`. When `D-0003` became superseded, deterministic dependency propagation caused:

```text
Q-0007  RESOLVED -> REOPENED
reason: Hard dependency on D-0003 is no longer valid.
```

After the subsequent eligible-model robustness analysis, the model patch resolved `Q-0007` again using the authoritative timing notice and the replacement feature set:

```text
Q-0007  REOPENED -> RESOLVED
```

This did not block completion, cause a failed command, add a provider retry, or invalidate unrelated accepted validation/metric decisions. It is recorded as raw held-out state behavior and is not manually classified here as a semantic failure, false block, or architecture-induced friction.

## Repair precision in terminal state

The terminal state shows the affected Phase 1 evidence invalidated and the obsolete feature-bearing model decision superseded, while unrelated accepted decisions remained accepted:

```text
D-0001 accepted  forward temporal validation / no member_key predictor
D-0002 accepted  AUROC selection criterion
D-0003 superseded  provisional model containing lifecycle_flag
D-0004 accepted  exclude lifecycle_flag
D-0005 accepted  eligible replacement logistic model

E-0001 invalidated  Phase 1 feature-bearing model comparison
E-0002 current      eligible Phase 2 model comparison
E-0003 current      eligible uncertainty/stability evidence
```

The terminal frontier is empty, indicating no unresolved controller motivator remains after final reporting.

## P0 knowledge activation

The persisted knowledge activation record contains three activated components:

```text
K-INFO-001  Protected Final Evaluation
K-INFO-002  Learned Transformation Evaluation Boundary
K-VAL-001   Generalization-Regime Question
```

`K-INFO-003 Prediction-Time Feature Eligibility` does **not** appear in this run's activation record.

Nevertheless, the model-created state independently contained `Q-0007`, the authoritative timing notice was read, `F-0007` established post-outcome unavailability, `lifecycle_flag` was removed, affected evidence was invalidated, and eligible replacement development evidence was produced before lock.

The non-activation of `K-INFO-003` is therefore preserved as held-out behavioral evidence. It is not treated as a mechanical harness defect and must not trigger a P0 implementation change during the frozen experiment.

## Final lock

The final development model was an L2 logistic-regression pipeline using only the six legitimate scoring-time predictors:

```text
tenure_months
plan_tier
monthly_charge
support_tickets_90d
late_payments_90d
usage_change_30d
```

The validation evidence recorded at lock was:

```text
n: 5,375
AUROC: 0.683297
bootstrap AUROC 95% interval: [0.658992, 0.705880]
AP: 0.259117
Brier: 0.088899
monthly AUROC range: 0.677474-0.693044
returning-customer AUROC: 0.685239
new-customer AUROC: 0.650857
```

The fixed model was locked before protected test-value access.

## Protected final evaluation

Exactly one protected final evaluation was performed after lock, on periods 21-24.

Recorded test evidence:

```text
n: 4,126
events: 460
event rate: 0.111488
AUROC: 0.696277
bootstrap AUROC 95% interval: [0.672827, 0.722437]
AP: 0.235698
Brier: 0.093547
```

The final report bounded its claim to moderate ranking discrimination for future snapshots represented by the held-out test set and explicitly did not claim an intervention threshold or utility result.

No development action followed protected-test access.

## Comparison with first held-out P0 resource outcome

The two mechanically verified held-out P0 attempts now have:

```text
H1 R1 P0
14 calls
6 Python attempts
294,267 tokens
completed: true
completed_within_budget: false
budget_exhausted: true

H1 R2 P0
12 calls
5 Python attempts
226,926 tokens
completed: true
completed_within_budget: true
budget_exhausted: false
```

Therefore the cumulative held-out P0 budget-exhausted count remains:

```text
1
```

The preregistered allowance of at most one P0 budget-exhausted held-out run has not been exceeded at this point.

## Experimental interpretation boundary

This checkpoint establishes only mechanical facts about the trajectory. It intentionally does not:

```text
assign S1-S10 scores;
assign SC1 or SC2;
compare B0/B1/P0 semantic quality;
classify the transient Q-0007 reopening under the architecture-friction criterion;
interpret the missing K-INFO-003 activation as success or failure;
change P0 behavior, knowledge triggers, state relations, budgets, or prompts.
```

Those outcomes remain for the frozen evaluation protocol.

## Held-out progress after verification

```text
resolved slots: 5 / 30
behavior-evaluable retained attempts: 5
non-behavior-evaluable replacement attempts: 0
P0 budget-exhausted runs: 1
```

The next preregistered slot is:

```text
variant: H1
replicate: 2
condition: B0
slot: h1-r02-b0
attempt: h1-r02-b0-a01
```

This slot may now be authorized for exactly one `run-next` invocation.