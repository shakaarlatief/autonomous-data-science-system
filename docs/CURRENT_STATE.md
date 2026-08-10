# Current State

## Checkpoint

**Checkpoint:** 63  
**Date:** 2026-08-10  
**Development stage:** Held-out execution active; five slots permanently resolved; H1 R2 B0 A01 terminated as a non-behavior-evaluable provider failure and the slot remains unresolved pending raw inspection  
**Implementation status:** P0 behavioral/controller logic, B0/B1 prompts, bundle identities, resource budgets, semantic rubric, provider/model configuration, materialized run plan, and held-out execution infrastructure remain frozen. H1 R1 is fully mechanically verified. H1 R2 B1 and P0 are fully mechanically verified. `h1-r02-b0-a01` is replacement eligible but has not yet been raw-inspected. No H1/H2 semantic judging has begun.

## Prototype V0 question

> Can explicit project state, reusable knowledge activation, prospective safeguards, and dependency-aware repair make a strong LLM's data-science reasoning materially more reliable across a changing project than an equally capable simpler LLM workflow?

B1 remains the primary architectural control.

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

Registered common envelope:

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

Crossing-call semantics remain frozen: a call may begin only while prior cumulative observed usage is below 250,000. If that admitted call crosses the ceiling, the call remains in the trajectory, the run becomes budget-exhausted, and no later treatment call may begin. Behavioral budget exhaustion is behavior-evaluable and never replacement eligible.

Frozen bundle identities:

```text
H1 seed 811
SHA-256 7d3cdfe90f262b604ad637ebb0b07b35e2604c3feb5365d2e9648adf54b7b4c8

H2 seed 1601
SHA-256 44ebc4775c0faefaaa01dbd5c81b2de28d6239d6a53fa9d64a8ad8e73680928e
```

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

Strong targeted pass requires all five targeted criteria to equal 2.0. Pre-P0 judge calibration was 59/60 exact ordinary-criterion agreements, one adjacent disagreement, zero extreme disagreements, zero semantic-critical disagreements, and zero manual-adjudication runs out of six.

No rubric, threshold, bundle, B0/B1 prompt, P0 behavior, or privileged knowledge component may be revised from held-out observations. No H1/H2 semantic judging has begun.

## Held-out executor

```bash
python -m ads_v0.heldout_runner status
python -m ads_v0.heldout_runner run-next
```

`status` makes zero treatment calls. `run-next` launches at most one attempt and only for the earliest unresolved slot. The executor was frozen before held-out execution after `69 passed in 11.52s` and a clean real no-inference status check.

Replacement policy:

```text
behavior_evaluable = true
=> slot permanently resolved
=> never replaced

behavior_evaluable = false
+ terminal provider/infrastructure generation failure
=> replacement eligible inside same slot
```

Maximum attempts per slot: `a01`, `a02`, `a03`. A slot may not be skipped while unresolved.

## Mechanically verified held-out runs

### H1 R1 B0: `h1-r01-b0-a01`

```text
completed: true
completed_within_budget: true
budget_exhausted: false
model calls: 15
Python attempts: 5
total tokens: 108,891
A0-A4: all PASS
critical failures: none
```

Detailed record: `docs/checkpoints/054_first_held_out_attempt_h1_r01_b0_full_mechanical_verification.md`.

### H1 R1 B1: `h1-r01-b1-a01`

```text
completed: true
completed_within_budget: true
budget_exhausted: false
model calls: 14
Python attempts: 6
total tokens: 120,424
A0-A4: all PASS
critical failures: none
```

Detailed record: `docs/checkpoints/056_h1_r01_b1_full_mechanical_verification.md`.

### H1 R1 P0: `h1-r01-p0-a01`

```text
completed: true
completed_within_budget: false
budget_exhausted: true
model calls: 14
Python attempts: 6
total tokens: 294,267
A0-A4: all PASS
critical failures: none
```

The run was at 249,581 tokens after protected final evaluation. The terminal final-report call was legitimately admitted and crossed the ceiling to 294,267. The report was retained and no later treatment call occurred.

Detailed record: `docs/checkpoints/058_h1_r01_p0_full_mechanical_verification_and_terminal_budget_crossing.md`.

### H1 R2 B1: `h1-r02-b1-a01`

```text
completed: true
completed_within_budget: true
budget_exhausted: false
model calls: 15
Python attempts: 7
total tokens: 139,150
A0-A4: all PASS
critical failures: none
```

Detailed record: `docs/checkpoints/060_h1_r02_b1_full_mechanical_verification.md`.

### H1 R2 P0: `h1-r02-p0-a01`

```text
completed: true
completed_within_budget: true
budget_exhausted: false
behavior_evaluable: true
model calls: 12
Python attempts: 5
total tokens: 226,926
A0-A4: all PASS
critical failures: none
```

Phase 2 timing repair removed `lifecycle_flag`, invalidated affected Phase 1 evidence, reopened and superseded the provisional model decision, generated replacement eligible-feature evidence, and preserved unrelated accepted validation/metric decisions. Three of four P0 knowledge components activated; `K-INFO-003 Prediction-Time Feature Eligibility` did not activate, but the trajectory independently handled the timing issue correctly. This remains frozen behavioral evidence rather than a trigger for implementation change.

Detailed record: `docs/checkpoints/062_h1_r02_p0_full_mechanical_verification.md`.

## H1 R2 B0 A01 provider failure

Attempt:

```text
h1-r02-b0-a01
```

Observed executor result:

```text
Action: ATTEMPT_COMPLETED
Model attempt launched: True
Classification: NON_BEHAVIOR_EVALUABLE_PROVIDER_FAILURE
Behavior evaluable: False
Replacement eligible: True
Slot resolved: False
```

Protocol consequence:

```text
h1-r02-b0 remains the earliest unresolved slot;
h1-r02-b0-a01 is not behavior-evaluable treatment evidence;
no later H1 slot may start yet;
if raw inspection confirms ordinary provider/infrastructure termination,
the next permissible attempt is h1-r02-b0-a02.
```

Before launching `a02`, inspect the persisted artifacts to confirm that `summary.json`, `attempt_record.json`, resource accounting, and `terminal_generation_error` support the executor classification and that no common harness/runtime correctness defect caused the termination.

Detailed record: `docs/checkpoints/063_h1_r02_b0_a01_non_behavior_evaluable_provider_failure.md`.

## Current held-out count

```text
resolved slots: 5 / 30
behavior-evaluable retained attempts: 5
non-behavior-evaluable provider-failure attempts: 1
replacement attempts already launched: 0
P0 budget-exhausted runs: 1
```

The preregistered P0 budget-exhaustion allowance remains exactly one used run.

No semantic comparison or architectural conclusion is drawn from manual inspection. S1-S10 and SC1-SC2 remain reserved for the frozen blinded judge.

## Current priority

**Inspect the complete persisted artifacts for `h1-r02-b0-a01`. Do not invoke `run-next` again until the provider-failure classification is mechanically verified. If confirmed, the next attempt must be `h1-r02-b0-a02` in the same slot.**
