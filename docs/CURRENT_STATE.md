# Current State

## Checkpoint

**Checkpoint:** 56  
**Date:** 2026-08-10  
**Development stage:** Held-out execution active; H1 replicate 1 B0 and B1 slots mechanically verified and permanently resolved; first held-out P0 slot is next  
**Implementation status:** P0 behavioral/controller logic, B0/B1 prompts, bundle identities, resource budgets, semantic rubric, and held-out execution infrastructure remain frozen. `h1-r01-b0-a01` and `h1-r01-b1-a01` both completed end-to-end within budget, passed all deterministic assertions, and are retained as behavior-evaluable held-out evidence. No semantic judging has begun. The next preregistered attempt is `h1-r01-p0-a01`.

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

Resource semantics:

```text
if prior observed cumulative usage is >= 250,000,
no new treatment call may begin;

if an admitted provider call crosses 250,000,
that completed call remains in the trajectory,
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

The executor revalidates these identities before every launch.

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

P0 development history:

```text
dev-p0-01: incomplete, 10 calls, 250,279 tokens
dev-p0-02: incomplete, 12 calls, 291,350 tokens
dev-p0-03: incomplete, 14 calls, 260,234 tokens
dev-p0-04: complete within budget, 12 calls, 228,064 tokens, 4 Python attempts
```

`dev-p0-04` was predeclared as the final planned behavioral development run. Full inspection found no experiment-invalidating mechanical defect. P0 behavior remains frozen.

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

Before execution began, the complete deterministic suite passed:

```text
69 passed in 11.52s
```

The real no-inference status check confirmed `0/30` resolved slots and `h1-r01-b0-a01` as the first attempt. Execution infrastructure was frozen before the first treatment call.

## Replacement policy

```text
behavior_evaluable = true
=> slot permanently resolved
=> never replaced

behavior_evaluable = false
+ terminal provider/infrastructure generation failure
=> replacement eligible inside same slot
```

Maximum attempts per slot:

```text
a01 initial
a02 replacement 1
a03 replacement 2
```

Three non-behavior-evaluable attempts pause execution. The executor never skips an unresolved earlier slot.

## Held-out progress

### Slot 1: `h1-r01-b0`

Attempt `h1-r01-b0-a01` is permanently retained.

```text
completed: true
completed_within_budget: true
budget_exhausted: false
model_calls: 15
Python attempts: 5
total tokens: 108,891
generation failures: 0
project phase: FINAL_EVALUATION
A0-A4: all PASS
critical failures: none
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

Protected H1 test evidence:

```text
n: 4,126
positives: 460
AUROC: 0.696277
average precision: 0.235698
Brier: 0.093547
log loss: 0.324630
```

Detailed record:

```text
docs/checkpoints/054_first_held_out_attempt_h1_r01_b0_full_mechanical_verification.md
```

### Slot 2: `h1-r01-b1`

Attempt `h1-r01-b1-a01` is permanently retained.

```text
completed: true
completed_within_budget: true
budget_exhausted: false
model_calls: 14
generation_attempts: 14
generation failures: 0
Python attempts: 6
input tokens: 111,863
output tokens: 8,561
total tokens: 120,424
project phase: FINAL_EVALUATION
A0-A4: all PASS
critical failures: none
```

High-level trajectory:

```text
read README, project brief, inherited baseline
inspect schema and repeated temporal/entity structure
run leakage-safe rolling-origin Phase 1 comparison
complete Phase 1
read authoritative lifecycle_flag timing notice
redo development comparison without lifecycle_flag
confirm candidate on future validation
lock six-feature C=0.1 logistic model
perform exactly one protected final evaluation
submit bounded final report
```

The inherited baseline's learned-preprocessing boundary problem was explicitly recognized and not relied upon as clean evidence.

Final locked predictors:

```text
tenure_months
plan_tier
monthly_charge
support_tickets_90d
late_payments_90d
usage_change_30d
```

Phase 2 validation evidence for the locked model:

```text
n: 5,375
AUROC: 0.6832
bootstrap AUROC 95% CI: [0.6599, 0.7059]
average precision: 0.2588
Brier: 0.0889
```

Protected H1 test evidence:

```text
n: 4,126
churn events: 460
AUROC: 0.6961
bootstrap AUROC 95% CI: [0.6700, 0.7213]
average precision: 0.2358
Brier: 0.0935
```

No provider retries, treatment-command errors, Python timeouts, resource-budget events, premature test access, or post-test development occurred.

Detailed record:

```text
docs/checkpoints/056_h1_r01_b1_full_mechanical_verification.md
```

## Current held-out count

```text
resolved slots: 2 / 30
behavior-evaluable attempts retained: 2
non-behavior-evaluable replacement attempts: 0
```

No semantic comparison between B0 and B1 is drawn from these two runs. Their S1-S10 and SC1-SC2 outcomes remain reserved for the blinded judge.

## Next authorized slot

According to the frozen plan:

```text
variant: H1
replicate: 1
condition: P0
slot: h1-r01-p0
attempt: h1-r01-p0-a01
```

After pulling this checkpoint, exactly one invocation is authorized:

```bash
python -m ads_v0.heldout_runner run-next
```

The executor must launch only `h1-r01-p0-a01`. Stop after it returns and inspect the executor classification before any H1 replicate 2 run.

## Relevant latest records

```text
docs/checkpoints/052_held_out_execution_infrastructure_frozen_and_first_run_authorized.md
docs/checkpoints/053_first_held_out_attempt_h1_r01_b0_terminal_record.md
docs/checkpoints/054_first_held_out_attempt_h1_r01_b0_full_mechanical_verification.md
docs/checkpoints/055_second_held_out_attempt_h1_r01_b1_terminal_record.md
docs/checkpoints/056_h1_r01_b1_full_mechanical_verification.md
```

## Current priority

**Run exactly one next held-out attempt, `h1-r01-p0-a01`, then stop and inspect its executor outcome before H1 replicate 2 begins.**
