# Checkpoint 70: H1 R3 P0 full mechanical verification and second P0 budget exhaustion

**Date:** 2026-08-18  
**Status:** Historical experiment record  
**Checkpoint class:** EXPERIMENT_EXECUTION  
**Project stage:** Prototype V0 held-out execution and evaluation  
**Scope:** Raw mechanical verification only. No S1-S10 or SC1-SC2 semantic scoring is performed here.  
**Authority:** Historical provenance for the recorded experiment milestone; frozen experiment contracts and final experiment conclusions govern their declared scopes.  
**Design session:** 01  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 01 - Foundations & Checkpoint 0  
**Attempt:** `h1-r03-p0-a01`  
**Condition:** P0  
**Variant / replicate:** H1 / 3

## Outcome

The executor classification is confirmed by the persisted attempt artifacts.

```text
behavior_evaluable: true
completed: false
completed_within_budget: false
budget_exhausted: true
replacement_eligible: false
slot_resolved: true
project_phase: FINAL_EVALUATION
terminal_generation_error: null
```

The attempt is therefore the permanently retained P0 trajectory for the H1 replicate-3 slot. It is not replacement eligible.

## Frozen identity and configuration

The attempt records the expected frozen identities:

```text
attempt_id: h1-r03-p0-a01
slot_id: h1-r03-p0
slot_index: 7
condition: P0
bundle SHA-256: 7d3cdfe90f262b604ad637ebb0b07b35e2604c3feb5365d2e9648adf54b7b4c8
plan SHA-256: 21911b714d86155f98bda6239d8fdd23fcb82f9ca985ea738ef8889154b1c77f
```

Registered execution configuration is unchanged:

```text
model: gpt-5.6-terra
reasoning effort: high
max successful model calls: 24
max observed total tokens: 250,000
max Python attempts: 12
max output tokens/call: 30,000
max additional generation retries: 2
Python timeout: 60 s
provider request timeout: 300 s
```

No treatment, prompt, controller, benchmark, budget, retry, or provider-normalization change is justified by this run.

## Resource accounting

Persisted summary:

```text
model calls: 13
generation attempts: 13
generation failures: 0
Python attempts: 6
input tokens: 247,734
output tokens: 10,751
total tokens: 258,485
wall clock: 154.56 s
```

Every provider generation completed successfully. There were no provider retries, generation errors, ambiguous structured-output failures, treatment-command errors, or Python timeouts.

All six Python executions returned code 0 with empty stderr.

### Exact token crossing

Cumulative observed treatment usage by successful model call was:

```text
call 1:   3,024
call 2:   7,231
call 3:  13,015
call 4:  21,720
call 5:  34,075
call 6:  50,311
call 7:  70,156
call 8:  93,041
call 9: 118,482
call 10: 147,711
call 11: 180,848
call 12: 217,919
call 13: 258,485
```

Call 13 was therefore legitimately admitted because prior cumulative usage was 217,919, below the 250,000 ceiling. The completed call contributed 40,566 tokens and moved cumulative usage to 258,485. The crossing call remains in the trajectory and no later treatment-model call occurred, exactly matching the preregistered crossing-call rule.

Unlike H1 R1 P0, where the budget crossing occurred on a terminal final-report call after protected evaluation, this run crossed the ceiling on the protected final-evaluation generation itself. The final evaluation executed successfully, but the resource gate then stopped the trajectory before a `submit_final_report` generation could occur.

## Deterministic integrity

All deterministic assertions passed:

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
first final-test value access sequence: 32
later development sequences: []
```

The protected final evaluation therefore occurred only after final lock and no development followed test feedback.

## Mechanical trajectory

The trace contains 33 events and follows the expected project progression:

```text
read project documentation
-> inspect train metadata
-> inspect temporal/entity structure
-> audit inherited baseline
-> clean Phase 1 model comparison
-> temporal/scoring-period robustness analysis
-> phase_1_complete
-> Phase 2 timing notice
-> eligible-feature model re-evaluation
-> eligible scoring-period robustness analysis
-> final_model_locked
-> FINAL_EVALUATION_STARTED
-> one protected final evaluation
-> RESOURCE_BUDGET_EXHAUSTED
```

There is no final-report submission event because the token ceiling was crossed immediately after the protected final-evaluation call.

## Development mechanics

The development inspection established:

```text
train periods: 1-16
validation periods: 17-20
train rows: 21,994
validation rows: 5,375
validation customers: 1,688
validation customers overlapping train: 1,370
validation overlap share: 81.2%
train customers with repeated periods: 3,021
```

The inherited baseline was explicitly represented in P0 state as fitting `StandardScaler` and `OneHotEncoder` on concatenated train and validation features before validation, so its reported validation performance was not treated as clean comparative evidence.

Phase 1 clean logistic performance was approximately:

```text
AUROC: 0.7247
AP: 0.2793
log loss: 0.3050
Brier: 0.0871
```

Phase 1 provisionally included `lifecycle_flag` because then-visible documentation described it as scoring-time information.

## Phase 2 repair

The authoritative timing notice established:

```text
lifecycle_flag is generated after the churn outcome window closes
and retrospectively backfilled;
it is unavailable at beginning-of-month scoring.
```

The typed-state history records targeted repair:

```text
F-0003 ACTIVE -> DISPUTED
D-0003 PROVISIONAL -> REOPENED -> SUPERSEDED
E-0001 CURRENT -> INVALIDATED
E-0002 CURRENT -> INVALIDATED
O-0004 OPEN -> SATISFIED
O-0005 OPEN -> SATISFIED
O-0006 OPEN -> SATISFIED
O-0007 OPEN -> SATISFIED
```

Replacement eligible-feature evidence was then created before final lock:

```text
E-0003 CURRENT
E-0004 CURRENT
D-0004 ACCEPTED
```

The previously accepted temporal-validation decision `D-0001` remained accepted. The AUROC model-selection decision `D-0002` also remained accepted; its transient support-loss obligation was explicitly satisfied because the metric decision was independently supported by task purpose rather than the invalidated model evidence.

As in H1 R2 P0, `Q-0007` was resolved from the authoritative timing notice, transiently reopened when its hard dependency on superseded `D-0003` became invalid, and later resolved again after the final eligible pipeline was established:

```text
Q-0007 OPEN -> RESOLVED -> REOPENED -> RESOLVED
```

This is retained as an architecture diagnostic for later analysis. It is not manually assigned an S-score, critical semantic failure, or architecture-friction classification here.

## Knowledge activation

All four frozen knowledge components activated in this trajectory:

```text
K-INFO-001 Protected Final Evaluation
K-INFO-002 Learned Transformation Evaluation Boundary
K-INFO-003 Prediction-Time Feature Eligibility
K-VAL-001 Generalization-Regime Question
```

This differs from H1 R2 P0, where K-INFO-003 did not activate. The difference is retained as held-out behavioral evidence and does not justify treatment modification.

## Final locked model

The final lock selected logistic regression with training-fitted preprocessing and these six predictors:

```text
tenure_months
plan_tier
monthly_charge
support_tickets_90d
late_payments_90d
usage_change_30d
```

Excluded fields include:

```text
member_key
scoring_period
lifecycle_flag
churn_next_30d
```

Phase 2 validation evidence for the eligible logistic model was:

```text
n: 5,375
AUROC: 0.683297
AP: 0.259117
log loss: 0.314238
Brier: 0.088899
```

Adding `scoring_period` changed main validation AUROC from 0.683297 to 0.684647 but slightly reduced the earlier temporal AUROC from 0.686299 to 0.686150, so it was not retained.

## Protected final evaluation

The single protected H1 test evaluation completed successfully before the budget gate terminated later treatment reasoning:

```text
n: 4,126
events: 460
prevalence: 0.111488
AUROC: 0.696277
AP: 0.235698
log loss: 0.324630
Brier: 0.093547
mean prediction: 0.103040
AUROC bootstrap 95% interval: [0.669924, 0.721935]
```

The model had already been locked before this access. There was no later development.

## Final-report incompleteness

`milestones.json` contains:

```text
phase_1_report: present
final_lock_report: present
final_report: null
```

The final state frontier still contains the top-level project-deliverable obligation `O-0001` as required/open. This is mechanically consistent with `completed: false`: the analysis and protected evaluation finished, but no final report could be generated because the crossing final-evaluation call exhausted the token budget.

This incompleteness is behavioral and must remain in the retained trajectory. It is not replacement eligible.

## Preregistered resource consequence

This is the second retained P0 held-out run with `budget_exhausted: true`:

```text
H1 R1 P0: budget exhausted
H1 R2 P0: within budget
H1 R3 P0: budget exhausted
```

The preregistered continuation rule requires no more than one P0 budget-exhausted run. Because the observed count is now two, that specific continuation requirement can no longer be satisfied regardless of later held-out runs.

This is an objective resource-envelope result, not a semantic or overall architectural verdict. The remaining frozen held-out experiment must still be executed as preregistered so that reliability, semantic quality, completion, repair precision, false blocking, and relative resource distributions can be evaluated without selective stopping.

No P0 simplification, prompt change, controller modification, or budget increase is made during the experiment.

## Updated held-out count

```text
resolved slots: 7 / 30
behavior-evaluable retained attempts: 7
non-behavior-evaluable provider/interface attempts: 2
replacement attempts launched: 2
P0 budget-exhausted retained runs: 2
```

## Next frozen slot

After this full mechanical verification, the next preregistered slot is:

```text
variant: H1
replicate: 3
condition: B0
slot: h1-r03-b0
attempt: h1-r03-b0-a01
```

Exactly one next `run-next` invocation may be launched. Stop immediately after its executor result before H1 R3 B1.
