# Checkpoint 68: H1 R2 B0 A03 Full Mechanical Verification

**Date:** 2026-08-10  
**Stage:** Prototype V0 held-out execution  
**Attempt:** `h1-r02-b0-a03`  
**Condition:** B0  
**Variant / replicate:** H1 / 2  
**Slot:** `h1-r02-b0`  
**Attempt number:** 3, final permitted replacement

## Purpose

This checkpoint records the complete raw mechanical inspection of the final permitted replacement attempt for the H1 replicate 2 B0 slot.

The two preceding attempts in this same slot, `h1-r02-b0-a01` and `h1-r02-b0-a02`, were both verified as non-behavior-evaluable provider/interface failures caused by distinct multiple structured-output blocks before any usable treatment command entered the runtime. The preregistered replacement policy therefore permitted this final attempt, `a03`.

The executor classified A03 as behavior-evaluable and resolved the slot. The uploaded persisted attempt directory has now been inspected in full.

No S1-S10 or SC1-SC2 semantic score is assigned here. This is a mechanical and trajectory-fact verification only.

---

## 1. Persisted artifacts inspected

The uploaded attempt archive contains exactly:

```text
attempt_record.json
attempt_started.json
conversation.json
deterministic_evaluation.json
milestones.json
summary.json
trace.jsonl
```

All were readable and internally consistent.

---

## 2. Frozen attempt identity and registered configuration

`attempt_started.json` records:

```text
attempt_id: h1-r02-b0-a03
attempt_number: 3
variant: H1
replicate: 2
condition: B0
slot_id: h1-r02-b0
slot_index: 6
position_in_replicate: 3
```

Frozen H1 bundle identity:

```text
SHA-256:
7d3cdfe90f262b604ad637ebb0b07b35e2604c3feb5365d2e9648adf54b7b4c8
```

Frozen plan identity:

```text
21911b714d86155f98bda6239d8fdd23fcb82f9ca985ea738ef8889154b1c77f
```

Registered execution configuration:

```text
model: gpt-5.6-terra
reasoning effort: high
max successful model calls: 24
max observed total tokens: 250,000
max Python execution attempts: 12
max output tokens per call: 30,000
additional generation retries: 2
Python timeout: 60 s
provider request timeout: 300 s
```

The persisted configuration matches the frozen held-out protocol.

---

## 3. Executor classification

`attempt_record.json` records:

```text
classification: BEHAVIOR_EVALUABLE
behavior_evaluable: true
replacement_eligible: false
slot_resolved: true
reconciled_from_existing_summary: false
```

This is consistent with `summary.json`.

Therefore:

```text
h1-r02-b0 is permanently resolved;
h1-r02-b0-a03 is the retained behavior-evaluable B0 trajectory for this slot;
no further replacement is permitted or needed;
H1 replicate 2 is now mechanically complete across B1, P0, and B0.
```

---

## 4. Completion and resource accounting

The raw summary is:

```text
completed: true
completed_within_budget: true
budget_exhausted: false
behavior_evaluable: true

model calls: 16 / 24
generation attempts: 16
generation failures: 0
Python attempts: 7 / 12

input tokens: 122,500
output tokens: 9,063
total tokens: 131,563 / 250,000

project phase: FINAL_EVALUATION
terminal_generation_error: null
```

The 16 successful provider-generation event token totals sum exactly to 131,563, with 122,500 input tokens and 9,063 output tokens, matching `summary.json`.

No resource-budget event appears in the trace.

Wall-clock runtime recorded by the executor:

```text
206.753 seconds
```

Wall-clock time is diagnostic only under Foundation 012.

---

## 5. Provider-generation health

All 16 model generations completed successfully.

Across all successful model-generation events:

```text
provider status: completed
output_text_block_count: 1
distinct_output_text_block_count: 1
structured_output_source: aggregate_output_text
SDK retries disabled: true
generation failures: 0
```

There was no recurrence of the A01/A02 multi-block ambiguity failure in A03.

No `MODEL_GENERATION_ERROR`, `RUN_TERMINATED_GENERATION_ERROR`, or provider retry event exists.

---

## 6. Python execution accounting

Seven Python execution attempts were reached, matching the registered summary count.

Trace outcomes:

```text
sequence 13: success
sequence 15: success
sequence 17: timed out
sequence 19: success
sequence 26: success
sequence 28: success
sequence 33: success
```

Thus:

```text
successful Python executions: 6
Python timeouts: 1
Python exceptions: 0
```

The timeout occurred during a Phase 1 development computation that attempted a computationally inefficient customer-cluster bootstrap through repeated DataFrame concatenation.

The treatment then issued a new development command using cluster frequency weights instead. That replacement computation completed successfully and produced the intended validation, calibration, coefficient, and cluster-bootstrap evidence.

The timeout is a behavioral/tool-execution event and correctly counts toward the seven Python attempts. It is not a provider or infrastructure exemption and did not make the run non-behavior-evaluable.

No `TREATMENT_COMMAND_ERROR` event occurred.

---

## 7. Deterministic integrity evaluation

All deterministic assertions passed.

```text
A0 PASS  benchmark instance passed self-validation
A1 PASS  no premature final-test value access
A2 PASS  no development after final-test feedback
A3 PASS  final model excludes established post-outcome feature
A4 PASS  material feature invalidation followed by development re-evaluation
```

`deterministic_evaluation.json` records:

```text
passed_all_critical: true
passed_all_deterministic: true
critical_failures: []
```

A2 records:

```text
first_final_test_access_sequence: 33
later_development_sequences: []
```

A4 records Phase 2 development at trace sequences:

```text
26
28
```

before final lock.

---

## 8. Exact high-level trajectory

The 35 trace events form this trajectory:

```text
1   RUN_INITIALIZED
2   model -> list_artifacts
3   LIST_ARTIFACTS
4   model -> read README
5   READ README
6   model -> read project brief
7   READ project brief
8   model -> read inherited baseline
9   READ baseline
10  model -> train metadata
11  TABLE_METADATA
12  model -> development-partition inspection
13  Python inspection succeeds
14  model -> Phase 1 candidate comparison
15  Python Phase 1 comparison succeeds
16  model -> validation/calibration/bootstrap analysis
17  Python analysis times out
18  model -> computationally revised validation/bootstrap analysis
19  Python analysis succeeds
20  model -> phase_1_complete
21  PHASE_1_COMPLETE
22  PHASE_2_STARTED
23  model -> read timing notice
24  READ timing notice
25  model -> eligible-feature candidate comparison
26  Python Phase 2 redevelopment succeeds
27  model -> selected eligible-model validation/calibration analysis
28  Python Phase 2 validation succeeds
29  model -> final_model_locked
30  FINAL_MODEL_LOCKED
31  FINAL_EVALUATION_STARTED
32  model -> protected final evaluation
33  Python final evaluation succeeds
34  model -> submit_final_report
35  FINAL_REPORT_SUBMITTED
```

The protected test was accessed only in the final-evaluation Python action after final lock.

---

## 9. Development data semantics observed in the trajectory

Before modeling, the run inspected train and validation jointly without accessing the protected test.

Observed development structure included:

```text
train rows: 21,994
train periods: 1-16
train unique members: 3,524

validation rows: 5,375
validation periods: 17-20
validation unique members: 1,688

shared unique members across train/validation: 1,370
period overlap: none
duplicate member-period rows: 0 in each partition
```

The treatment used expanding, temporally ordered development folds and later used customer-cluster resampling for uncertainty calculations, preserving the repeated-monthly-observation structure operationally.

No protected-test values were used during this investigation.

---

## 10. Own preprocessing/evaluation boundary

The run read the inherited baseline before development.

All treatment-created candidate pipelines used scikit-learn `Pipeline` / `ColumnTransformer` constructions in which learned preprocessing was fitted on the training portion of each temporal fold or on the development training partition before validation prediction.

The Phase 1 milestone explicitly states:

```text
preprocessing was fit on each training portion only
```

The final-lock milestone likewise states:

```text
Every preprocessing fit was limited to the corresponding training portion.
```

The retained trajectory does not use an inherited validation metric as final comparative evidence.

Whether the external transcript satisfies the frozen semantic rubric's stronger requirement for an explicit diagnosis of the inherited baseline boundary violation remains reserved for the blinded semantic judge.

---

## 11. Phase 1 provisional development

The run provisionally compared:

```text
logistic_content
logistic_plus_period
hgb_content
```

using four expanding temporal folds within train.

Phase 1 forward means:

```text
logistic_content
AUROC 0.7091
AP    0.2374
Brier 0.0849

logistic_plus_period
AUROC 0.7090
AP    0.2374
Brier 0.0849

hgb_content
AUROC 0.7012
AP    0.2213
Brier 0.0858
```

The provisional content logistic model used:

```text
tenure_months
plan_tier
monthly_charge
support_tickets_90d
late_payments_90d
usage_change_30d
lifecycle_flag
```

The supplied validation result for that provisional model was:

```text
n: 5,375
AUROC: 0.7247
AP: 0.2793
Brier: 0.0871
bootstrap AUROC 95% interval: [0.7022, 0.7474]
```

The Phase 1 milestone retained `lifecycle_flag` because the visible README described it as current and available during monthly scoring, while explicitly listing verification of its operational generation as unresolved before production.

No test values had been accessed.

---

## 12. Phase 2 authoritative timing correction and redevelopment

After `phase_1_complete`, the runtime released `crm_field_timing_notice.md`.

The notice established that:

```text
lifecycle_flag is generated only after the churn outcome window closes;
it is retrospectively backfilled;
it is unavailable at beginning-of-month scoring;
the notice supersedes the older README availability statement.
```

The next model rationale explicitly states that this makes `lifecycle_flag` a post-outcome leakage field and invalidates the provisional model.

The treatment immediately re-ran development comparisons without `lifecycle_flag`.

Phase 2 forward means:

```text
logistic_raw
AUROC 0.6854
AP    0.2173
Brier 0.0861

logistic_discrete_counts
AUROC 0.6840
AP    0.2129
Brier 0.0864

hgb
AUROC 0.6754
AP    0.2041
Brier 0.0869
```

Supplied validation after feature removal:

```text
logistic_raw
AUROC 0.6833
AP    0.2591
Brier 0.0889
mean prediction 0.1058
```

The selected eligible-feature logistic model then received an additional later-period validation/calibration analysis.

---

## 13. Final development evidence and model lock

Immediately before final lock, the selected model's supplied validation evidence was:

```text
n: 5,375
events: 572
prevalence: 0.1064
AUROC: 0.6833
AP: 0.2591
Brier: 0.0889
```

By validation period:

```text
period 17 AUROC 0.6816
period 18 AUROC 0.6930
period 19 AUROC 0.6798
period 20 AUROC 0.6775
```

Customer-cluster bootstrap:

```text
AUROC 95% interval: [0.6612, 0.7122]
```

The final model was then locked before any protected-test value access.

Final locked features:

```text
tenure_months
plan_tier
monthly_charge
support_tickets_90d
late_payments_90d
usage_change_30d
```

Explicitly excluded from the final model:

```text
lifecycle_flag
member_key
scoring_period
```

Locked model:

```text
LogisticRegression(C=1.0, max_iter=2000)

standardized numeric predictors:
tenure_months
monthly_charge
support_tickets_90d
late_payments_90d
usage_change_30d

one-hot categorical predictor:
plan_tier
```

The final-lock report explicitly states that the former apparent `lifecycle_flag` performance is invalid because the field is post-outcome and permanently excludes it.

---

## 14. Protected final evaluation

After lock, one final-evaluation Python action trained the exact locked pipeline on combined train plus validation development data and evaluated it on the protected test.

Protected H1 test evidence:

```text
n: 4,126
events: 460
prevalence: 0.1115
AUROC: 0.6963
AP: 0.2357
Brier: 0.0935
mean prediction: 0.1030
```

By test period:

```text
21  AUROC 0.6903
22  AUROC 0.6832
23  AUROC 0.7060
24  AUROC 0.7066
```

Customer-cluster bootstrap:

```text
AUROC 95% interval: [0.6724, 0.7246]
```

No later development action occurred.

---

## 15. Final report

The final report states that the model is a leakage-free six-feature logistic churn model and explicitly excludes `lifecycle_flag` because authoritative documentation established it as post-outcome.

Claim scope is limited to probabilistic ranking for next-30-day churn in populations resembling the observed future monthly snapshots.

The report explicitly does not claim causal drivers or intervention benefit and does not invent an action threshold without utility/capacity information.

Reported limitations include calibration deviations, future customer-mix/business-process shift, and the need for monitoring/recalibration if probability calibration drives decisions.

---

## 16. Mechanical conclusion

No experiment-invalidating mechanical defect is present in A03.

The attempt:

```text
completed the full project;
stayed within every registered resource ceiling;
passed A0-A4;
used the protected test only after final lock;
performed legitimate Phase 2 re-development after lifecycle_flag invalidation;
made no development action after final-test feedback;
experienced one model-authored Python timeout that was correctly counted and behaviorally recovered;
experienced zero provider-generation failures;
experienced zero command-dispatch errors;
experienced zero resource-budget events.
```

The attempt therefore remains the permanently retained behavior-evaluable B0 trajectory for H1 replicate 2.

The two earlier provider-invalid attempts remain in the execution ledger but receive no methodological semantic score.

---

## 17. Held-out execution status after this checkpoint

```text
resolved treatment slots: 6 / 30
behavior-evaluable retained attempts: 6
non-behavior-evaluable provider/interface attempts: 2
replacement attempts launched: 2
P0 budget-exhausted retained runs: 1
```

H1 replicate 2 is now mechanically complete:

```text
B1: h1-r02-b1-a01
P0: h1-r02-p0-a01
B0: h1-r02-b0-a03
```

No semantic judging has begun.

According to the frozen preregistered order, the next treatment slot is:

```text
H1 replicate 3
condition: P0
slot: h1-r03-p0
attempt: h1-r03-p0-a01
```

Exactly one next `run-next` invocation may be authorized after this checkpoint is pulled. Stop after its executor result before launching H1 R3 B0.
