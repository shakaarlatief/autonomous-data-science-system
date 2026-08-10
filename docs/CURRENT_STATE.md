# Current State

## Checkpoint

**Checkpoint:** 54  
**Date:** 2026-08-10  
**Development stage:** Held-out execution active; first H1/B0 slot fully mechanically verified and permanently resolved; second preregistered H1/B1 slot authorized  
**Implementation status:** P0 behavioral/controller logic and held-out execution infrastructure remain frozen. The first actual held-out attempt, `h1-r01-b0-a01`, completed end-to-end within the registered resource envelope, passed every deterministic assertion, and is valid behavior-evaluable held-out evidence. No semantic judging has begun. The next executable slot is `h1-r01-b1-a01`.

## Primary purpose

> **Create the best possible data-science process for the particular project, where what “best” means is configurable according to project goals, constraints, required outputs, and desired human involvement.**

The LLM is one reasoning component inside a system that should operationalize methodological knowledge, project state, questions, evidence, claims, dependencies, repair, resource constraints, and selective human involvement.

## Prototype V0 question

> Can explicit project state, reusable knowledge activation, prospective safeguards, and dependency-aware repair make a strong LLM's data-science reasoning materially more reliable across a changing project than an equally capable simpler LLM workflow?

## Frozen conditions

```text
B0
Strong LLM + Python + project artifacts + strong generic data-science guidance.

B1
Same model/tools + the same four methodological concepts supplied statically.
No typed state, dynamic activation, deterministic gates, or dependency-aware repair.

P0
Same underlying model/tools + typed project state
+ the same four structured knowledge components
+ state-triggered activation/applicability
+ prospective protected-test safeguard
+ dependency-aware repair
+ state-derived runnable frontier
+ append-only audit history.
```

B1 remains the primary architectural control.

## Frozen held-out protocol

Authoritative records:

```text
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
prototype_v0/configs/held_out_protocol_v0_1.json
prototype_v0/configs/held_out_bundle_fingerprints_v0_1.json
results/held_out/run_plan.json
```

Run design:

```text
H1: 5 runs per condition
H2: 5 runs per condition
B0/B1/P0: 10 held-out slots each
30 treatment slots total
```

Registered common treatment envelope:

```text
provider: OpenAI
model: gpt-5.6-terra
reasoning effort: high
24 successful model calls
250,000 observed total treatment tokens
12 Python execution attempts
30,000 max output tokens per provider call
2 additional generation retries per semantic turn
60 s Python timeout
300 s provider request timeout
```

Token rule:

```text
if prior cumulative observed usage is >= 250,000,
no new treatment call may begin;

if an admitted provider call crosses 250,000,
that completed call remains part of the trajectory,
the run becomes budget-exceeded,
and no later treatment call may begin.
```

Observable failed-attempt usage counts. Model-authored Python exceptions/timeouts count when execution is reached. Behavioral failures and budget exhaustion are never replacement-run eligible.

## Frozen held-out bundles

```text
H1
case_id: churn_v0_h1
surface_variant: held_out_h1
seed: 811
file_count: 9
SHA-256: 7d3cdfe90f262b604ad637ebb0b07b35e2604c3feb5365d2e9648adf54b7b4c8

H2
case_id: churn_v0_h2
surface_variant: held_out_h2
seed: 1601
file_count: 9
SHA-256: 44ebc4775c0faefaaa01dbd5c81b2de28d6239d6a53fa9d64a8ad8e73680928e
```

The real local directories matched these frozen identities exactly before execution began. The executor revalidates them before each launch.

## Preregistered order

```text
H1
r1: B0, B1, P0
r2: B1, P0, B0
r3: P0, B0, B1
r4: B0, B1, P0
r5: B1, P0, B0

H2
r1: P0, B0, B1
r2: B0, B1, P0
r3: B1, P0, B0
r4: P0, B0, B1
r5: B0, B1, P0
```

The materialized plan must not be regenerated or overwritten after held-out execution began.

## Frozen semantic judge

Primary targeted architecture score:

```text
mean(S1, S2, S3, S6, S7)
```

Strong targeted pass requires all five targeted criteria to equal 2.0.

Judge calibration before P0 implementation:

```text
59/60 exact ordinary-criterion agreements
1 adjacent disagreement
0 extreme disagreements
0 semantic-critical disagreements
0/6 manual-adjudication runs
```

No rubric, threshold, bundle, B0/B1 prompt, or privileged knowledge component may be revised in response to held-out outcomes.

No H1/H2 semantic judging has begun.

## Frozen P0

Typed objects:

```text
ARTIFACT FACT ASSUMPTION QUESTION EVIDENCE CLAIM DECISION OBLIGATION ACTION
```

Relations:

```text
DEPENDS_ON SUPPORTS CONTRADICTS ANSWERS GENERATED_BY
```

Exactly four privileged components:

```text
K-INFO-001 Protected Final Evaluation
K-INFO-002 Learned Transformation Evaluation Boundary
K-INFO-003 Prediction-Time Feature Eligibility
K-VAL-001 Generalization-Regime Question
```

Development history:

```text
dev-p0-01: incomplete, 10 calls, 250,279 tokens
dev-p0-02: incomplete, 12 calls, 291,350 tokens
dev-p0-03: incomplete, 14 calls, 260,234 tokens
dev-p0-04: complete within budget, 12 calls, 228,064 tokens, 4 Python attempts
```

`dev-p0-04` was predeclared as the final planned behavioral development run. Full inspection found no experiment-invalidating defect. P0 behavior remains frozen.

## Held-out execution infrastructure

Executor:

```bash
python -m ads_v0.heldout_runner status
python -m ads_v0.heldout_runner run-next
```

`status` makes zero treatment calls. `run-next` launches at most one attempt and only for the earliest unresolved slot.

Attempt artifacts:

```text
results/held_out/attempts/<attempt_id>/attempt_started.json
results/held_out/attempts/<attempt_id>/summary.json
results/held_out/attempts/<attempt_id>/attempt_record.json
```

Before held-out execution began, the complete local suite passed:

```text
69 passed in 11.52s
```

The real status check then confirmed `0/30` resolved and `h1-r01-b0-a01` as the first attempt. Execution infrastructure was frozen before the first treatment call.

## Replacement policy

```text
behavior_evaluable = true
=> slot permanently resolved
=> never replaced

behavior_evaluable = false
+ terminal provider/infrastructure generation failure
=> replacement eligible in same slot
```

Maximum attempts inside one slot:

```text
a01 initial
a02 replacement 1
a03 replacement 2
```

Three non-behavior-evaluable attempts pause execution. The executor never skips an unresolved earlier slot.

## Held-out progress

### Slot 1: `h1-r01-b0`

Attempt:

```text
h1-r01-b0-a01
```

Executor classification:

```text
BEHAVIOR_EVALUABLE
replacement_eligible: false
slot_resolved: true
```

Full raw mechanical verification:

```text
completed: true
completed_within_budget: true
budget_exhausted: false
model_calls: 15
generation_attempts: 15
generation_failures: 0
Python attempts: 5
input_tokens: 101,457
output_tokens: 7,434
total_tokens: 108,891
project phase: FINAL_EVALUATION
```

All registered deterministic assertions passed:

```text
A0 PASS
A1 PASS
A2 PASS
A3 PASS
A4 PASS
critical_failures: none
```

High-level trajectory:

```text
list/read documentation and baseline
inspect schema and repeated temporal/entity structure
run leakage-safe chronological Phase 1 comparison
complete Phase 1
read authoritative lifecycle_flag timing notice
re-evaluate without lifecycle_flag
lock six-feature logistic model
perform exactly one protected final evaluation
submit bounded final report
```

Final locked predictors:

```text
tenure_months
plan_tier
monthly_charge
support_tickets_90d
late_payments_90d
usage_change_30d
```

Protected H1 test result for the locked model:

```text
n: 4,126
positives: 460
AUROC: 0.696277
average precision: 0.235698
Brier: 0.093547
log loss: 0.324630
```

No provider retries, treatment-command errors, Python timeouts, or resource-budget events occurred. No development followed protected-test access.

This checkpoint does **not** assign semantic S1-S10 or SC1-SC2 scores. Those remain for the preregistered blinded judge.

Detailed record:

```text
docs/checkpoints/054_first_held_out_attempt_h1_r01_b0_full_mechanical_verification.md
```

## Current held-out count

```text
resolved slots: 1 / 30
behavior-evaluable attempts retained: 1
non-behavior-evaluable replacement attempts: 0
```

## Next authorized slot

According to the frozen plan:

```text
variant: H1
replicate: 1
condition: B1
slot: h1-r01-b1
attempt: h1-r01-b1-a01
```

Authorized command after pulling this checkpoint:

```bash
python -m ads_v0.heldout_runner run-next
```

The executor must launch only `h1-r01-b1-a01`.

## Relevant latest records

```text
docs/checkpoints/051_resumable_one_attempt_held_out_executor_implemented.md
docs/checkpoints/052_held_out_execution_infrastructure_frozen_and_first_run_authorized.md
docs/checkpoints/053_first_held_out_attempt_h1_r01_b0_terminal_record.md
docs/checkpoints/054_first_held_out_attempt_h1_r01_b0_full_mechanical_verification.md
```

## Current priority

**Run exactly one next held-out attempt, `h1-r01-b1-a01`, then stop and inspect its executor outcome before any P0 held-out attempt.**
