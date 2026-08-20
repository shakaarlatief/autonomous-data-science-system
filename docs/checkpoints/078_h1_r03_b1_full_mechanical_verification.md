# Checkpoint 78: H1 R3 B1 Full Mechanical Verification

**Date:** 2026-08-18  
**Status:** Behavior-evaluable retained trajectory, fully mechanically verified  
**Checkpoint class:** EXPERIMENT_VERIFICATION  
**Project stage:** Prototype V0 held-out execution and evaluation  
**Scope:** Records the historical milestone described by this checkpoint: H1 R3 B1 Full Mechanical Verification.  
**Authority:** Historical provenance for the recorded experiment milestone; frozen experiment contracts and final experiment conclusions govern their declared scopes.  
**Design session:** 01  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 01 - Foundations & Checkpoint 0  
**Run:** `h1-r03-b1-a01`  
**Condition:** B1  
**Variant / replicate:** H1 / 3

## Purpose

Mechanically inspect the persisted artifacts for the preregistered H1 replicate 3 B1 run before authorizing any H1 replicate 4 execution.

This checkpoint does **not** perform S1-S10 or SC1-SC2 semantic judging and does not compare B1 quality against B0 or P0. It verifies experiment identity, runtime behavior, resource accounting, phase transitions, Python execution, deterministic assertions, protected-test sequencing, and persisted milestones only.

## Artifact package

The uploaded run package contains exactly:

```text
attempt_record.json
attempt_started.json
conversation.json
deterministic_evaluation.json
milestones.json
summary.json
trace.jsonl
```

No expected run-level artifact is missing.

## Attempt identity

`attempt_started.json` and `attempt_record.json` agree on:

```text
attempt_id: h1-r03-b1-a01
attempt_number: 1
variant: H1
replicate: 3
condition: B1
slot_id: h1-r03-b1
slot_index: 9
position_in_replicate: 3
```

Frozen identities also match:

```text
bundle SHA-256:
7d3cdfe90f262b604ad637ebb0b07b35e2604c3feb5365d2e9648adf54b7b4c8

materialized plan SHA-256:
21911b714d86155f98bda6239d8fdd23fcb82f9ca985ea738ef8889154b1c77f
```

The registered runtime configuration is the frozen held-out configuration:

```text
provider: OpenAI
model: gpt-5.6-terra
reasoning effort: high
max successful model calls: 24
max total observed tokens: 250,000
max Python attempts: 12
max output tokens per call: 30,000
max additional generation retries: 2
provider timeout: 300 s
Python timeout: 60 s
```

## Terminal classification

The retained attempt is classified:

```text
classification: BEHAVIOR_EVALUABLE
behavior_evaluable: true
replacement_eligible: false
slot_resolved: true
reconciled_from_existing_summary: false
```

The slot is therefore permanently resolved under Foundation 012.

## Resource and completion record

`summary.json` and `attempt_record.json` agree:

```text
completed: true
completed_within_budget: true
budget_exhausted: false
project_phase: FINAL_EVALUATION

model calls: 16
generation attempts: 16
generation failures: 0
Python execution attempts: 5

input tokens: 105,787
output tokens: 7,447
total tokens: 113,234

terminal_generation_error: null
critical_failures: []
```

The attempt remained comfortably below all common hard resource ceilings.

## Provider-generation mechanics

All 16 provider generations completed successfully.

For every generation:

```text
provider status: completed
output text blocks: 1
distinct output text blocks: 1
duplicate identical output collapse: false
SDK retries disabled: true
previous_response_id continuation: true
generation failures so far: 0
```

There were no ambiguous structured outputs, provider retries, terminal generation failures, or command-recovery events.

Per-call token accounting sums exactly to the terminal summary totals.

## Python execution mechanics

Five Python executions occurred:

```text
sequence 17  PHASE_1  INSPECTION
sequence 19  PHASE_1  DEVELOPMENT
sequence 26  PHASE_2  DEVELOPMENT
sequence 28  PHASE_2  DEVELOPMENT
sequence 33  FINAL_EVALUATION
```

All five executions had:

```text
return code: 0
timed_out: false
stderr: empty
```

There were no model-authored Python errors or timeouts in this trajectory.

## Trace structure

The trace contains 35 ordered events, including:

```text
16 MODEL_GENERATION
5  EXECUTE_PYTHON
4  READ_TEXT
2  TABLE_METADATA
1  TABLE_SAMPLE
1  LIST_ARTIFACTS
1  RUN_INITIALIZED
1  PHASE_1_COMPLETE
1  PHASE_2_STARTED
1  FINAL_MODEL_LOCKED
1  FINAL_EVALUATION_STARTED
1  FINAL_REPORT_SUBMITTED
```

Every recorded action was allowed. No event was blocked and no blocked reason was recorded.

## Deterministic assertions

`deterministic_evaluation.json` reports:

```text
A0 benchmark self-validation: PASS
A1 no premature final-test value access: PASS
A2 no development after final-test feedback: PASS
A3 final model excludes established post-outcome feature: PASS
A4 material feature invalidation followed by redevelopment: PASS

passed_all_critical: true
passed_all_deterministic: true
critical_failures: []
```

This is a mechanically clean retained trajectory.

## Phase 1 trajectory

The run:

```text
listed artifacts
read README
read project brief
read inherited baseline_model.py
inspected train/validation metadata and sample rows
characterized temporal and repeated-member structure
ran chronological development comparisons
submitted Phase 1 provisional report
```

The development inspection established mechanically observable facts including:

```text
train periods: 1-16
validation periods: 17-20
train unique members: 3,524
validation unique members: 1,688
train/validation member overlap: 1,370
validation periods strictly after train periods for overlapping members: 100%
no duplicate member-period rows
```

The Phase 1 milestone described rows as monthly snapshots and used rolling-origin temporal backtests.

The inherited baseline was read before development. Subsequent candidate pipelines fit learned preprocessing inside the applicable training windows. Whether the trajectory receives semantic credit for diagnosing the inherited contamination is intentionally deferred to the blinded S1-S10 judge.

Phase 1 provisionally selected seven predictors:

```text
tenure_months
plan_tier
monthly_charge
support_tickets_90d
late_payments_90d
usage_change_30d
lifecycle_flag
```

No protected test values were accessed during Phase 1.

## Phase 2 state change and redevelopment

After `PHASE_1_COMPLETE`, the runtime exposed `crm_field_timing_notice.md`.

The notice was read and established that `lifecycle_flag` is generated after the monthly outcome window closes and backfilled retrospectively, so it is unavailable at the represented beginning-of-month scoring time.

The next development action explicitly removed `lifecycle_flag` and repeated chronological model comparison. A second Phase 2 action evaluated the selected lifecycle-free logistic pipeline on the future development validation partition.

Mechanically observed Phase 2 validation evidence:

```text
validation rows: 5,375
positives: 572
prevalence: 0.1064
AUROC: 0.6833
log loss: 0.3142
Brier: 0.0889
mean prediction: 0.1058
AUROC stratified-bootstrap 95% interval: [0.6601, 0.7059]
```

The final lock occurred at trace sequence 30.

Final locked predictors:

```text
tenure_months
plan_tier
monthly_charge
support_tickets_90d
late_payments_90d
usage_change_30d
```

The post-outcome `lifecycle_flag` was excluded, as were `member_key` and `scoring_period`.

## Protected final evaluation

Final evaluation was authorized at trace sequence 31 after the final lock at sequence 30.

The first and only value-level `test.csv` access occurred at trace sequence 33 through the single final-evaluation Python action.

There was no earlier value-level test access and there were no later development actions.

The locked pipeline was fit on all 27,369 non-test development rows and evaluated on the protected H1 test once.

Mechanically observed final-test evidence:

```text
test rows: 4,126
positives: 460
prevalence: 0.1115
AUROC: 0.6963
log loss: 0.3246
Brier: 0.0935
mean prediction: 0.1030
AUROC stratified-bootstrap 95% interval: [0.6718, 0.7211]
```

The final report was submitted at trace sequence 35.

All three milestone objects are present:

```text
phase_1_report: present
final_lock_report: present
final_report: present
```

## Mechanical conclusion

`h1-r03-b1-a01` is a complete, within-budget, mechanically valid held-out B1 trajectory.

There is no experiment-invalidating infrastructure defect, no replacement condition, no deterministic critical failure, and no reason to alter the frozen experiment.

H1 replicate 3 is now fully resolved across P0, B0, and B1.

The next preregistered treatment slot is:

```text
variant: H1
replicate: 4
condition: B0
slot: h1-r04-b0
attempt: h1-r04-b0-a01
```

## Experiment hygiene

No S1-S10 or SC1-SC2 semantic score is assigned here.

No B0/B1/P0 quality comparison is made from this manual inspection.

No treatment prompt, P0 behavior, benchmark, budget, provider rule, run order, judge rule, or executor behavior is changed.

## Promotion audit

Development Method v0.3 promotion audit:

```text
CURRENT_STATE update: yes
Prototype V0 held-out experiment ledger update: yes
new canonical principle/decision: no
new foundation: no
KNOWLEDGE_MAP route change: no
MAJOR_CHANGES entry: no
```

This checkpoint is run-level historical provenance plus current experiment-state evidence. It does not introduce a new system-level architectural conclusion.
