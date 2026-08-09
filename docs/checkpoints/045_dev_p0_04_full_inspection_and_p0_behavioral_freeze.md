# Checkpoint 45: `dev-p0-04` Full Inspection and P0 Behavioral Freeze

**Date:** 2026-08-09

## Purpose

Record the complete inspection of the fourth and final planned P0 development-calibration trajectory and freeze ordinary P0 behavioral/controller logic for held-out execution.

`dev-p0-04` was designated in advance as the final planned behavioral development run. No held-out H1/H2 treatment run has occurred.

---

## 1. Terminal outcome

`dev-p0-04` used the unchanged registered treatment envelope:

```text
24 successful model calls
250,000 observed treatment tokens
12 Python execution attempts
30,000 max output tokens per provider call
2 additional generation retries
```

Terminal result:

```text
Completed: True
Completed within budget: True
Budget exhausted: False
Successful model calls: 12
Generation attempts: 12
Generation failures: 0
Input tokens: 218,948
Output tokens: 9,116
Total observed tokens: 228,064
Python execution attempts: 4
Behavioral evaluation eligible: True
Critical deterministic assertions passed: True
All deterministic assertions passed: True
```

This is the first P0 development trajectory to complete end-to-end inside the independently fixed resource envelope.

---

## 2. Exact action sequence

The run completed without any state-control rejection, command-recovery loop, provider-generation failure, or budget event.

```text
1. read project brief
2. read README
3. inspect train metadata
4. inspect train/validation temporal and repeated-entity structure with Python
5. inspect inherited baseline code
6. run leakage-safe Phase 1 development model comparison
7. complete Phase 1
8. read authoritative Phase 2 timing notice
9. re-evaluate eligible-feature models without account_state_code
10. lock final model
11. perform the single protected final evaluation
12. submit final report
```

Trace event counts confirm:

```text
MODEL_GENERATION: 12
READ_TEXT: 4
TABLE_METADATA: 1
EXECUTE_PYTHON: 4
P0_KNOWLEDGE_ACTIVATED: 4
PHASE_1_COMPLETE: 1
PHASE_2_STARTED: 1
FINAL_MODEL_LOCKED: 1
FINAL_EVALUATION_STARTED: 1
FINAL_REPORT_SUBMITTED: 1
P0_STATE_CONTROL_ERROR: 0
MODEL_GENERATION_ERROR: 0
RESOURCE_BUDGET_EXHAUSTED: 0
```

---

## 3. Deterministic integrity

All current deterministic checks passed:

```text
A0 benchmark self-validation: PASS
A1 no premature final-test value access: PASS
A2 no development after final-test feedback: PASS
A3 final model excludes established post-outcome feature: PASS
A4 material feature invalidation followed by legitimate re-evaluation: PASS
```

Final lock selected exactly these six eligible predictors:

```text
tenure_months
plan_tier
monthly_charge
support_tickets_90d
late_payments_90d
usage_change_30d
```

`account_state_code`, `customer_id`, and `snapshot_month` were excluded from the locked pipeline.

The first protected test-value access occurred only after final model lock, and no development action followed protected test feedback.

---

## 4. Phase 1 semantics and inherited-evaluation diagnosis

The run established the future monthly churn objective and protected-test role before modeling.

The development audit found:

```text
train months: 1-16
validation months: 17-20
train rows: 21,840
validation rows: 5,296
train unique customers: 3,513
validation unique customers: 1,686
train/validation customer overlap: 1,352
```

The state and Phase 1 report explicitly represented repeated customer snapshots and chose chronological later-month validation because the intended use is future monthly scoring, while noting that validation is dominated by continuing customers and contains a smaller validation-only cohort.

The inherited baseline was explicitly diagnosed as invalid validation evidence because it fits `StandardScaler` and `OneHotEncoder` on concatenated train and validation predictors before scoring validation.

The run then generated replacement leakage-safe development evidence with all learned preprocessing fit only on training rows.

Phase 1 selected logistic regression with the seven provisionally documented operational predictors including `account_state_code` and did not access protected test values.

Two limitations remain visible behavior rather than implementation defects:

```text
the stale README sentence "Each row represents one customer" was not turned into a separate explicit durable contradiction-correction object, although the run operationally represented repeated monthly customer snapshots;
pre-Phase-2 account_state_code eligibility was accepted from visible documentation rather than being strongly qualified as an unresolved timing assumption.
```

These points must remain available to the blinded semantic evaluation. They are not reasons to reopen P0 development tuning.

---

## 5. All four knowledge components activated

The run activated exactly the four registered P0 components:

```text
K-INFO-001 Protected Final Evaluation
K-INFO-002 Learned Transformation Evaluation Boundary
K-INFO-003 Prediction-Time Feature Eligibility
K-VAL-001 Generalization-Regime Question
```

Activation instances ended resolved or satisfied before final reporting.

No additional privileged methodological component was introduced.

---

## 6. Phase 2 repair behavior

The authoritative timing notice established:

```text
account_state_code is generated only after the monthly churn outcome window closes,
is retrospectively backfilled,
and is unavailable at beginning-of-month scoring.
```

The P0 state response then performed targeted repair:

```text
marked the older README timing fact disputed;
reopened the seven-feature provisional model decision;
invalidated Phase 1 model-comparison evidence that used account_state_code;
invalidated the dependent Phase 1 deployable-performance claim;
created repair/reassessment obligations for the invalidated evidence paths;
kept the established future chronological validation-regime decision current;
created the authoritative feature-ineligibility fact;
ran a fresh development comparison using only eligible predictors;
satisfied the affected repair obligations;
locked a replacement six-feature logistic model.
```

The unrelated validation-regime decision remained accepted. This is the intended targeted-repair behavior rather than a project-wide reset.

The state store also created and automatically satisfied generic support-loss reassessment obligations whose target was the broad deliverable obligation, consistent with the generic type-semantics correction made after `dev-p0-03`.

---

## 7. Final development evidence and lock

After excluding `account_state_code`, the replacement development comparison produced:

```text
logistic eligible operational:
    AUROC 0.68836
    AP 0.22658
    Brier 0.09173

logistic eligible plus snapshot_month:
    AUROC 0.68772

histogram-gradient eligible operational:
    AUROC 0.67833

histogram-gradient eligible plus snapshot_month:
    AUROC 0.67934
```

The final locked specification was logistic regression with train-only preprocessing during development and the six eligible predictors listed above.

The final lock report retained limitations around continuing-versus-new-customer evidence, lack of an operating-threshold utility specification, and future temporal uncertainty.

---

## 8. Protected final evaluation

The single final-evaluation action trained the already locked pipeline on combined train + validation development data and evaluated it once on the protected test set.

Observed final evidence:

```text
n_test: 4,084
positives: 445
prevalence: 0.10896
AUROC: 0.66004
average precision: 0.21232
Brier score: 0.09304
```

Monthly AUROC:

```text
month 21: 0.63736
month 22: 0.66915
month 23: 0.65331
month 24: 0.69014
```

Cohorts:

```text
seen in development:
    n = 3,775
    AUROC = 0.65468

new to development:
    n = 309
    AUROC = 0.72621
```

No model redesign occurred after these values were observed.

The final report correctly stated that final AUROC was below the eligible-feature development validation AUROC and bounded claims to moderate ranking performance for similar future monthly snapshots.

It did not recommend an operating threshold because no intervention capacity or utility function was provided.

---

## 9. Resource trajectory

Per-call observed total tokens:

```text
call  1:  3,036
call  2:  4,290
call  3:  6,038
call  4:  8,199
call  5: 13,218
call  6: 17,145
call  7: 20,555
call  8: 23,079
call  9: 27,005
call 10: 31,408
call 11: 35,014
call 12: 39,077
```

Cumulative total:

```text
3,036
7,326
13,364
21,563
34,781
51,926
72,481
95,560
122,565
153,973
188,987
228,064
```

The model-facing state views remained roughly 2.0k-10.0k characters rather than returning to the original full-audit-state growth pattern.

The run therefore demonstrates resource feasibility, but not resource parity with simpler conditions.

Development comparison remains materially unfavorable in absolute token use:

```text
B1 development mean: 124,434 tokens
P0 dev-p0-04:        228,064 tokens
ratio:                ~1.83x
```

The held-out preregistered resource comparison, not development calibration, will determine whether any reliability gain offsets that overhead.

---

## 10. Final state quality

The final state contained:

```text
51 total objects
50 relations
0 active runnable-frontier motivators
```

The final project deliverable obligation was satisfied, all repair obligations were closed, final evidence and claim objects were current/supported, obsolete Phase 1 evidence/claims were invalidated, and the obsolete seven-feature decision was superseded.

A previously questionable hard relation from the Phase 2 timing question to the provisional model was explicitly removed before protected final evaluation. No controller-specific error was required to recover from it in this run.

---

## 11. Behavioral freeze decision

No experiment-invalidating mechanical defect was found in `dev-p0-04`.

The run contains behavioral imperfections that the evaluation should be allowed to score, especially the strength of the explicit row-unit contradiction correction and the pre-notice epistemic status of `account_state_code`. Those are not grounds for more development tuning.

Therefore ordinary P0 behavioral/controller logic is now **frozen for held-out H1/H2 execution**.

From this checkpoint forward, do not change P0 merely to improve:

```text
semantic rubric scores;
resource usage on this benchmark;
state-relation quality observed in ordinary model behavior;
row-unit explicitness;
pre-Phase-2 feature-timing caution;
model-selection trajectory;
final-report wording.
```

Only a purely mechanical common protocol/runtime defect that would invalidate fair execution may justify a condition-neutral correction, with affected held-out slots handled according to the preregistered defect policy.

---

## 12. Development record remains intact

All P0 development trajectories remain part of the record:

```text
dev-p0-01: incomplete, 10 calls, 250,279 tokens
dev-p0-02: incomplete, 12 calls, 291,350 tokens
dev-p0-03: incomplete, 14 calls, 260,234 tokens
dev-p0-04: complete within budget, 12 calls, 228,064 tokens
```

The earlier failed runs are not discarded or reclassified.

---

## 13. Next stage

P0 behavioral development is closed.

Before any H1/H2 treatment run, complete only common experiment-control infrastructure:

```text
B0/B1 enforcement of the same 24-call / 250k-token / 12-Python envelope;
held-out run scheduler with preregistered order;
batch blinded semantic judging;
manual-adjudication handling;
resource/outcome aggregation and continuation/falsification comparison.
```

The next implementation task is common B0/B1 resource-envelope enforcement and its deterministic tests.
