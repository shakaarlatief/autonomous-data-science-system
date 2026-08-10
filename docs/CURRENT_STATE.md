# Current State

## Checkpoint

**Checkpoint:** 60  
**Date:** 2026-08-10  
**Development stage:** Held-out execution active; H1 replicate 1 fully mechanically verified; H1 replicate 2 B1 fully mechanically verified; next slot is H1 R2 P0  
**Implementation status:** P0 behavioral/controller logic, B0/B1 prompts, bundle identities, resource budgets, semantic rubric, provider/model configuration, run plan, and held-out execution infrastructure remain frozen. Four held-out slots are permanently resolved and behavior-evaluable. `h1-r02-b1-a01` completed end-to-end within budget and passed A0-A4. No H1/H2 semantic judging has begun.

## Primary purpose

> **Create the best possible data-science process for the particular project, where what “best” means is configurable according to project goals, constraints, required outputs, and desired human involvement.**

Prototype V0 tests whether explicit project state, reusable knowledge activation, prospective safeguards, dependency-aware repair, and state-derived action selection add reliable operational value beyond an equally capable simpler LLM workflow.

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

Crossing-call semantics remain frozen: a call may begin only if prior cumulative observed usage is below 250,000. If that admitted call crosses the ceiling, the call remains part of the trajectory, the run is marked budget-exhausted, and no later treatment call may begin. Observable failed-attempt usage counts. Behavioral budget exhaustion is not replacement eligible.

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

The materialized plan must not be regenerated or overwritten during held-out execution.

## Frozen semantic judge

Primary targeted architecture score:

```text
mean(S1, S2, S3, S6, S7)
```

Strong targeted pass requires all five targeted criteria to equal 2.0.

Pre-P0 calibration:

```text
59/60 exact ordinary-criterion agreements
1 adjacent disagreement
0 extreme disagreements
0 semantic-critical disagreements
0/6 manual-adjudication runs
```

No rubric, threshold, bundle, B0/B1 prompt, P0 behavior, or privileged knowledge component may be revised in response to held-out observations. No H1/H2 semantic judging has begun.

## Frozen P0

P0 uses typed state objects, the five registered relation types, exactly four privileged knowledge components, prospective final-test blocking, dependency-aware reopening/invalidation, and the state-derived runnable frontier. Development ended with `dev-p0-04`, which completed within the frozen envelope at 12 calls, 228,064 tokens, and 4 Python attempts. Full inspection found no experiment-invalidating defect, and P0 behavior was frozen before held-out execution.

## Held-out executor

```bash
python -m ads_v0.heldout_runner status
python -m ads_v0.heldout_runner run-next
```

`status` makes zero treatment calls. `run-next` launches at most one attempt and only for the earliest unresolved slot. The executor was frozen after the complete deterministic suite passed `69 passed in 11.52s` and a real no-inference status check confirmed the clean first slot.

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

## Held-out progress

### H1 R1 B0: `h1-r01-b0-a01`

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

Protected test: AUROC 0.696277, AP 0.235698, Brier 0.093547, log loss 0.324630.

Detailed record: `docs/checkpoints/054_first_held_out_attempt_h1_r01_b0_full_mechanical_verification.md`.

### H1 R1 B1: `h1-r01-b1-a01`

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

Protected test: AUROC 0.6961, AP 0.2358, Brier 0.0935.

Detailed record: `docs/checkpoints/056_h1_r01_b1_full_mechanical_verification.md`.

### H1 R1 P0: `h1-r01-p0-a01`

```text
completed: true
completed_within_budget: false
budget_exhausted: true
model calls: 14
Python attempts: 6
total tokens: 294,267
generation failures: 0
A0-A4: all PASS
critical failures: none
```

Cumulative usage was 249,581 after protected final evaluation, so the terminal report call was legitimately admitted and crossed the ceiling to 294,267. The final report was retained, the run was marked budget-exhausted, and no later treatment call occurred. All four P0 knowledge components activated and Phase 2 dependency repair was mechanically targeted.

Protected test: AUROC 0.69628, AP 0.23570, Brier 0.09355, log loss 0.32463.

Detailed record: `docs/checkpoints/058_h1_r01_p0_full_mechanical_verification_and_terminal_budget_crossing.md`.

### H1 R2 B1: `h1-r02-b1-a01`

Full raw mechanical verification is complete:

```text
completed: true
completed_within_budget: true
budget_exhausted: false
behavior_evaluable: true
model calls: 15
generation attempts: 15
generation failures: 0
Python attempts: 7
input tokens: 130,373
output tokens: 8,777
total tokens: 139,150
project phase: FINAL_EVALUATION
A0-A4: all PASS
critical failures: none
```

All seven Python executions returned code 0 with no timeout or stderr. No provider retry or resource-budget event occurred.

Trajectory:

```text
project brief / README / inherited baseline inspection
-> schema and temporal/entity inspection
-> development-only association checks
-> leakage-safe rolling Phase 1 model comparison
-> Phase 1 complete
-> authoritative lifecycle_flag timing notice
-> eligible-feature rolling re-evaluation
-> one chronological validation confirmation
-> final model lock
-> one protected test evaluation
-> final report
```

Phase 1 provisionally used seven predictors including `lifecycle_flag`. The authoritative Phase 2 notice caused the field to be removed and development evidence to be re-established.

Final locked predictors:

```text
tenure_months
plan_tier
monthly_charge
support_tickets_90d
late_payments_90d
usage_change_30d
```

Eligible-feature validation evidence:

```text
n: 5,375
AUROC: 0.6833
bootstrap AUROC 95% interval: [0.6601, 0.7059]
AP: 0.2591
Brier: 0.0889
log loss: 0.3142
```

Protected test evidence:

```text
n: 4,126
events: 460
AUROC: 0.6963
bootstrap AUROC 95% interval: [0.6718, 0.7211]
AP: 0.2357
Brier: 0.0935
log loss: 0.3246
```

Deterministic A2 records the first final-test access at trace sequence 31, with no later development sequence.

Detailed record: `docs/checkpoints/060_h1_r02_b1_full_mechanical_verification.md`.

## Current held-out count

```text
resolved slots: 4 / 30
behavior-evaluable retained attempts: 4
non-behavior-evaluable replacement attempts: 0
P0 budget-exhausted runs: 1
```

The preregistered continuation rule allows at most one P0 budget-exhausted held-out run. That allowance is already fully used by `h1-r01-p0-a01`. This arithmetic consequence must not alter future treatment execution, model behavior, or resource limits.

No semantic comparison or architectural conclusion is drawn from manual inspection. S1-S10 and SC1-SC2 remain reserved for the frozen blinded judge.

## Next authorized slot

According to the frozen plan:

```text
variant: H1
replicate: 2
condition: P0
slot: h1-r02-p0
attempt: h1-r02-p0-a01
```

Exactly one next `run-next` invocation is authorized after pulling Checkpoint 60. Stop after it returns and inspect the executor outcome before launching H1 R2 B0.

## Relevant latest records

```text
docs/checkpoints/056_h1_r01_b1_full_mechanical_verification.md
docs/checkpoints/058_h1_r01_p0_full_mechanical_verification_and_terminal_budget_crossing.md
docs/checkpoints/059_h1_r02_b1_terminal_record.md
docs/checkpoints/060_h1_r02_b1_full_mechanical_verification.md
```

## Current priority

**Advance exactly one preregistered slot to `h1-r02-p0-a01`, then stop and inspect its terminal classification before any further run.**
