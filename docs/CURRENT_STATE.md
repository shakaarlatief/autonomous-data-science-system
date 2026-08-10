# Current State

## Checkpoint

**Checkpoint:** 58  
**Date:** 2026-08-10  
**Development stage:** Held-out execution active; all three H1 replicate 1 conditions fully mechanically verified; next slot is H1 replicate 2 B1  
**Implementation status:** P0 behavioral/controller logic, B0/B1 prompts, bundle identities, resource budgets, semantic rubric, provider/model configuration, and held-out execution infrastructure remain frozen. H1 replicate 1 now contains one permanently retained behavior-evaluable attempt for B0, B1, and P0. B0 and B1 completed within budget. P0 completed the project but its terminal final-report generation crossed the 250,000-token ceiling, so `completed=true`, `budget_exhausted=true`, and `completed_within_budget=false`. All three runs passed A0-A4. No H1/H2 semantic judging has begun.

## Primary purpose

> **Create the best possible data-science process for the particular project, where what “best” means is configurable according to project goals, constraints, required outputs, and desired human involvement.**

Prototype V0 asks whether explicit project state, reusable knowledge activation, prospective safeguards, and dependency-aware repair make a strong LLM's data-science reasoning materially more reliable across a changing project than an equally capable simpler LLM workflow.

## Frozen experimental conditions

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

Crossing-call semantics remain frozen:

```text
if prior cumulative usage is already >= 250,000,
no new treatment call may begin;

if prior usage is below 250,000 and the next completed call crosses the ceiling,
that call remains in the trajectory,
the run becomes budget-exhausted,
and no later treatment call may begin.
```

A terminal call that crosses the ceiling may therefore yield `completed=true` but `completed_within_budget=false`. Observable failed-attempt usage counts. Python errors/timeouts count if execution is reached. Behavioral resource exhaustion is never replacement-run eligible.

## Frozen held-out bundles

```text
H1
case_id: churn_v0_h1
seed: 811
SHA-256: 7d3cdfe90f262b604ad637ebb0b07b35e2604c3feb5365d2e9648adf54b7b4c8

H2
case_id: churn_v0_h2
seed: 1601
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

The materialized plan must never be regenerated or overwritten during held-out execution.

## Frozen semantic judge

Primary targeted architecture score:

```text
mean(S1, S2, S3, S6, S7)
```

Strong targeted pass requires all five targeted criteria to equal 2.0.

Pre-P0 judge calibration:

```text
59/60 exact ordinary-criterion agreements
1 adjacent disagreement
0 extreme disagreements
0 semantic-critical disagreements
0/6 manual-adjudication runs
```

No rubric, threshold, bundle, B0/B1 prompt, P0 behavior, or privileged knowledge component may be revised from held-out observations. No H1/H2 semantic judging has begun.

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

P0 development ended with `dev-p0-04`, which completed within the frozen envelope at 12 calls, 228,064 tokens, and 4 Python attempts. Full inspection found no experiment-invalidating defect and P0 behavior was frozen before held-out execution.

## Held-out executor

```bash
python -m ads_v0.heldout_runner status
python -m ads_v0.heldout_runner run-next
```

`status` makes zero treatment calls. `run-next` launches at most one attempt and only for the earliest unresolved slot. Before held-out execution began, the complete deterministic suite passed `69 passed in 11.52s` and the real no-inference status check confirmed the clean first slot.

Replacement policy:

```text
behavior_evaluable = true
=> slot permanently resolved
=> never replaced

behavior_evaluable = false
+ terminal provider/infrastructure generation failure
=> replacement eligible inside same slot
```

Maximum attempts per slot are `a01`, `a02`, and `a03`.

## H1 replicate 1: fully mechanically verified

### B0: `h1-r01-b0-a01`

```text
completed: true
completed_within_budget: true
budget_exhausted: false
model calls: 15
Python attempts: 5
total tokens: 108,891
generation failures: 0
A0-A4: all PASS
critical failures: none
```

Protected test:

```text
AUROC: 0.696277
average precision: 0.235698
Brier: 0.093547
log loss: 0.324630
```

Detailed record: `docs/checkpoints/054_first_held_out_attempt_h1_r01_b0_full_mechanical_verification.md`.

### B1: `h1-r01-b1-a01`

```text
completed: true
completed_within_budget: true
budget_exhausted: false
model calls: 14
Python attempts: 6
total tokens: 120,424
generation failures: 0
A0-A4: all PASS
critical failures: none
```

The inherited preprocessing-boundary problem was explicitly recognized and the Phase 2 timing notice triggered legitimate re-evaluation without `lifecycle_flag`.

Protected test:

```text
AUROC: 0.6961
average precision: 0.2358
Brier: 0.0935
```

Detailed record: `docs/checkpoints/056_h1_r01_b1_full_mechanical_verification.md`.

### P0: `h1-r01-p0-a01`

Executor classification remains:

```text
BEHAVIOR_EVALUABLE
replacement_eligible: false
slot_resolved: true
```

Raw mechanical outcome:

```text
completed: true
completed_within_budget: false
budget_exhausted: true
model calls: 14
generation attempts: 14
generation failures: 0
Python attempts: 6
input tokens: 283,377
output tokens: 10,890
total tokens: 294,267
A0-A4: all PASS
critical failures: none
```

The token crossing occurred only on the terminal final-report call:

```text
cumulative after call 13 / protected final evaluation: 249,581
call 14 / submit_final_report: 44,686
terminal cumulative: 294,267
```

Because 249,581 was below the ceiling before call 14 began, the call was legitimately admitted. Its final report was retained and executed, then `RESOURCE_BUDGET_EXHAUSTED` was recorded with `total_token_budget_crossed_by_completed_terminal_call`. No later model call occurred.

All six Python executions succeeded with return code 0 and no timeout. There were no provider retries, state-control errors, or treatment-command recovery loops.

All four P0 knowledge components activated once. The terminal typed state explicitly represented the customer-month observation unit, the future temporal validation regime, inherited preprocessing contamination, and the authoritative Phase 2 timing correction.

Phase 2 state repair was targeted:

```text
F-0005 ACTIVE -> DISPUTED
D-0001 ACCEPTED -> REOPENED -> SUPERSEDED
D-0004 ACCEPTED -> REOPENED -> SUPERSEDED
E-0001 CURRENT -> INVALIDATED
E-0002 CURRENT -> INVALIDATED
O-0004/O-0005/O-0006 OPEN -> SATISFIED
```

Unrelated accepted validation and metric decisions were preserved. Replacement eligible-feature evidence was established before final lock.

Final locked predictors for all three H1 R1 runs were the same six legitimate variables:

```text
tenure_months
plan_tier
monthly_charge
support_tickets_90d
late_payments_90d
usage_change_30d
```

P0 protected test:

```text
n: 4,126
event rate: 0.11149
AUROC: 0.69628
bootstrap AUROC 95% CI: [0.66865, 0.72359]
average precision: 0.23570
log loss: 0.32463
Brier: 0.09355
```

Detailed record: `docs/checkpoints/058_h1_r01_p0_full_mechanical_verification_and_terminal_budget_crossing.md`.

## Current held-out count

```text
resolved slots: 3 / 30
behavior-evaluable retained attempts: 3
non-behavior-evaluable replacement attempts: 0
P0 budget-exhausted runs: 1
```

The preregistered continuation rule allows at most one P0 budget-exhausted held-out run. The first P0 run has therefore used that entire allowance. Any later P0 budget exhaustion would exceed that specific continuation threshold. This arithmetic consequence must not alter treatment execution, model behavior, or resource limits.

No semantic comparison or architectural conclusion is drawn from H1 replicate 1. S1-S10 and SC1-SC2 remain reserved for blinded judging after execution infrastructure and treatment trajectories are collected according to protocol.

## Next authorized slot

According to the frozen plan:

```text
variant: H1
replicate: 2
condition: B1
slot: h1-r02-b1
attempt: h1-r02-b1-a01
```

Exactly one next `run-next` invocation is authorized after pulling Checkpoint 58. Stop after it returns and inspect the executor outcome before launching the H1 R2 P0 slot.

## Relevant latest records

```text
docs/checkpoints/054_first_held_out_attempt_h1_r01_b0_full_mechanical_verification.md
docs/checkpoints/056_h1_r01_b1_full_mechanical_verification.md
docs/checkpoints/057_first_held_out_p0_attempt_h1_r01_terminal_record.md
docs/checkpoints/058_h1_r01_p0_full_mechanical_verification_and_terminal_budget_crossing.md
```

## Current priority

**Advance exactly one preregistered slot to `h1-r02-b1-a01`, then stop and inspect its terminal classification before any further run.**
