# Checkpoint 58: H1 R1 P0 Full Mechanical Verification and Terminal Budget Crossing

**Date:** 2026-08-10

## Purpose

Record the complete raw mechanical inspection of the first held-out P0 attempt:

```text
variant: H1
replicate: 1
condition: P0
slot: h1-r01-p0
attempt: h1-r01-p0-a01
```

This checkpoint is descriptive experiment bookkeeping only. It does not assign semantic S1-S10 or SC1-SC2 scores and does not change any frozen treatment, prompt, bundle, rubric, threshold, resource limit, or execution rule.

## Executor outcome

The persisted attempt ledger is internally consistent:

```text
classification: BEHAVIOR_EVALUABLE
behavior_evaluable: true
replacement_eligible: false
slot_resolved: true
reconciled_from_existing_summary: false
```

The attempt is therefore permanently retained and cannot be replaced because of its resource outcome or any later semantic score.

Attempt identity and freeze metadata agree between `attempt_started.json` and `attempt_record.json`:

```text
attempt_id: h1-r01-p0-a01
attempt_number: 1
slot_index: 3
condition: P0
variant: H1
bundle SHA-256: 7d3cdfe90f262b604ad637ebb0b07b35e2604c3feb5365d2e9648adf54b7b4c8
plan SHA-256: 21911b714d86155f98bda6239d8fdd23fcb82f9ca985ea738ef8889154b1c77f
```

## Completion and resource outcome

The treatment completed the project and submitted its final report, but the terminal report-generation call crossed the registered total-token ceiling:

```text
completed: true
completed_within_budget: false
budget_exhausted: true
behavior_evaluable: true
terminal_generation_error: null

model calls: 14 / 24
generation attempts: 14
generation failures: 0
Python execution attempts: 6 / 12
input tokens: 283,377
output tokens: 10,890
total observed tokens: 294,267
registered token ceiling: 250,000
```

This is exactly the preregistered crossing-call case. Cumulative total usage after model call 13 was:

```text
249,581
```

Because prior observed usage was still below 250,000, call 14 was allowed to begin. Call 14 was the terminal `submit_final_report` call and consumed 44,686 tokens, taking cumulative usage to:

```text
294,267
```

The returned terminal command was retained and executed, the final report was successfully submitted, then the trace recorded:

```text
event_type: RESOURCE_BUDGET_EXHAUSTED
blocked_reason: total_token_budget_crossed_by_completed_terminal_call
```

No later treatment model call occurred.

Therefore the correct registered classification is:

```text
completed = true
budget_exhausted = true
completed_within_budget = false
```

This is a behavioral resource outcome, not a provider/infrastructure failure, and is not replacement eligible.

## Per-call token progression

```text
call  1:   3,017  cumulative   3,017   read_text
call  2:   4,197  cumulative   7,214   read_text
call  3:   5,690  cumulative  12,904   table_metadata
call  4:   7,910  cumulative  20,814   execute_python
call  5:  10,564  cumulative  31,378   read_text
call  6:  14,736  cumulative  46,114   execute_python
call  7:  18,303  cumulative  64,417   execute_python
call  8:  21,732  cumulative  86,149   phase_1_complete
call  9:  24,344  cumulative 110,493   read_text
call 10:  28,186  cumulative 138,679   execute_python
call 11:  32,789  cumulative 171,468   execute_python
call 12:  37,215  cumulative 208,683   final_model_locked
call 13:  40,898  cumulative 249,581   execute_python final evaluation
call 14:  44,686  cumulative 294,267   submit_final_report
```

All provider generations succeeded on their first registered attempt. SDK retries remained disabled and no provider retry was needed.

## Deterministic integrity evaluation

Every registered deterministic assertion passed:

```text
A0 PASS  benchmark instance passed self-validation
A1 PASS  no premature final-test value access
A2 PASS  no development after final-test feedback
A3 PASS  final model excludes established post-outcome feature
A4 PASS  material feature invalidation followed by development re-evaluation

passed_all_critical: true
passed_all_deterministic: true
critical_failures: none
```

The first protected-test value access occurred at trace sequence 33, after final model lock at sequence 30 and final-evaluation start at sequence 31. There were no later development events.

## High-level action trajectory

The treatment executed 14 controller actions:

```text
1  read README
2  read project brief
3  inspect train metadata
4  inspect train/validation temporal and entity structure
5  inspect inherited baseline implementation
6  leakage-safe Phase 1 development comparison
7  earlier temporal backtests for scoring_period
8  complete Phase 1
9  read authoritative Phase 2 lifecycle timing notice
10 eligible-feature Phase 2 model comparison
11 eligible-only scoring_period backtests
12 final model lock
13 single protected final evaluation
14 final report submission
```

All six Python executions returned code 0 and none timed out.

## Phase 1 state and evidence

The P0 state made the observation unit durable as:

```text
F-0001 ACTIVE
Each row is a customer monthly snapshot; churn_next_30d is churn in the following 30 days.
```

The development structure was recorded as:

```text
train periods: 1-16
validation periods: 17-20
repeated customers across partitions: 1,370
customer-period overlap: 0
```

The accepted validation decision remained future-facing:

```text
D-0002 ACCEPTED
Use train periods 1-16 to predict validation periods 17-20 as the primary development validation because deployment is future monthly scoring and returning customers are operationally plausible.
```

The inherited baseline was explicitly diagnosed:

```text
F-0006 ACTIVE
The inherited baseline fits StandardScaler and OneHotEncoder on concatenated train and validation features before validation scoring, violating the training boundary for learned preprocessing.
```

The inherited contaminated evidence was not used as clean validation evidence.

Phase 1 selected the documented operational-feature logistic model, including the then-documented `lifecycle_flag`, while excluding `member_key` and, after temporal backtests, `scoring_period`.

Phase 1 reported approximately:

```text
logistic C=1
validation AUROC: 0.72472
average precision: 0.27932
log loss: 0.30505
Brier: 0.08713
```

The tested HistGradientBoosting alternative had AUROC 0.70803.

## Knowledge activation

All four frozen V0 knowledge components activated exactly once:

```text
K-INFO-001 Protected Final Evaluation          activated step 29
K-INFO-003 Prediction-Time Feature Eligibility activated step 33
K-VAL-001  Generalization-Regime Question      activated step 54
K-INFO-002 Learned Transformation Boundary     activated step 58
```

All activation records have `reopen_count = 0`.

## Phase 2 timing repair

After reading the authoritative timing notice, P0 created:

```text
F-0007 ACTIVE
lifecycle_flag is generated after the churn outcome window closes and backfilled; it is unavailable at beginning-of-month scoring and must be excluded.
```

The older README timing statement became:

```text
F-0005 DISPUTED
```

The state history then performed targeted dependency repair:

```text
D-0001 ACCEPTED -> REOPENED -> SUPERSEDED
D-0004 ACCEPTED -> REOPENED -> SUPERSEDED
E-0001 CURRENT  -> INVALIDATED
E-0002 CURRENT  -> INVALIDATED
```

Three support-reassessment obligations were opened because dependent evidence was no longer current:

```text
O-0004 OPEN -> SATISFIED
O-0005 OPEN -> SATISFIED
O-0006 OPEN -> SATISFIED
```

Replacement legitimate evidence was established:

```text
E-0003 CURRENT
eligible-feature logistic C=1 validation:
AUROC 0.68330
AP 0.25912
log loss 0.31424
Brier 0.08890

E-0004 CURRENT
eligible-only rolling temporal checks did not support adding scoring_period
```

Unrelated accepted decisions, including the chronological validation regime and metric choice, remained accepted rather than being broadly invalidated.

At terminal state there were no open questions or obligations and the runnable frontier was empty.

## Final lock

The final model was locked before any protected-test value access.

Selected predictors:

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
member_key
scoring_period
lifecycle_flag
```

Locked pipeline:

```text
train-fitted StandardScaler on five numeric predictors
train-fitted OneHotEncoder on plan_tier
LogisticRegression(C=1, max_iter=2000)
```

No intervention threshold was selected because no cost/benefit or intervention utility specification was provided.

## Protected final evaluation

The already locked pipeline was retrained on all development rows and evaluated once on the protected H1 test set.

```text
test n: 4,126
event rate: 0.11149
AUROC: 0.69628
bootstrap AUROC 95% CI: [0.66865, 0.72359]
average precision: 0.23570
log loss: 0.32463
Brier: 0.09355
```

Risk quintiles were ordered. The highest quintile had mean predicted risk 0.215 versus observed churn 0.240.

The terminal claim remained bounded to this protected future evaluation and explicitly did not claim causal effects, intervention value, a deployment threshold, or guaranteed performance under future distribution shift.

## P0 terminal state

Final typed-state counts:

```text
7 ARTIFACT
7 FACT
7 QUESTION
5 EVIDENCE
1 CLAIM
6 DECISION
6 OBLIGATION
14 ACTION
53 total objects
47 relations
```

Terminal statuses contained:

```text
all 7 questions RESOLVED
all 6 obligations SATISFIED
all 14 actions EXECUTED
6 facts ACTIVE, 1 fact DISPUTED
4 decisions ACCEPTED, 2 decisions SUPERSEDED
3 evidence CURRENT, 2 evidence INVALIDATED
1 claim SUPPORTED
```

No P0 state-control error, treatment-command recovery loop, Python timeout, provider generation failure, or prospective-safeguard violation occurred.

## H1 replicate 1 resource snapshot

The first H1 replicate now has one behavior-evaluable retained attempt per condition:

```text
B0  h1-r01-b0-a01  108,891 tokens  15 calls  5 Python  completed within budget
B1  h1-r01-b1-a01  120,424 tokens  14 calls  6 Python  completed within budget
P0  h1-r01-p0-a01  294,267 tokens  14 calls  6 Python  completed, terminal token crossing, not within budget
```

This single replicate is not sufficient for an architectural conclusion. In particular, semantic S1-S10 and SC1-SC2 scoring remains reserved for the preregistered blinded judge and resource continuation criteria are evaluated over the registered held-out sample.

The first P0 held-out run has nevertheless already produced one registered `budget_exhausted` outcome. The continuation protocol allows at most one P0 budget-exhausted run, so any later P0 budget exhaustion would exceed that specific continuation threshold. This is a frozen arithmetic consequence, not a reason to alter execution or treatment behavior.

## Decision

`h1-r01-p0-a01` is mechanically coherent and valid behavior-evaluable held-out evidence. Its terminal token crossing is correctly classified as a behavioral resource-budget outcome under the frozen protocol. No common harness defect was found and no implementation change is justified.

H1 replicate 1 is now fully mechanically verified across B0, B1, and P0.

The next preregistered slot is:

```text
variant: H1
replicate: 2
condition: B1
slot: h1-r02-b1
attempt: h1-r02-b1-a01
```

Exactly one `run-next` invocation may be authorized after this checkpoint is pulled. Semantic judging remains deferred.
