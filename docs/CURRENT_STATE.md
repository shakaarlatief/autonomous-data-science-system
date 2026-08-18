# Current State

## Checkpoint

**Checkpoint:** 73  
**Date:** 2026-08-18  
**Development stage:** Held-out execution active; eight treatment slots permanently resolved; H1 R3 B0 fully mechanically verified; next slot is H1 R3 B1  
**Implementation status:** P0 behavioral/controller logic, B0/B1 prompts, bundle identities, resource budgets, semantic rubric, provider/model configuration, materialized run plan, common provider normalization, retry semantics, and held-out execution infrastructure remain frozen. No H1/H2 semantic judging has begun.

## Prototype V0 question

> Can explicit project state, reusable knowledge activation, prospective safeguards, and dependency-aware repair make a strong LLM's data-science reasoning materially more reliable across a changing project than an equally capable simpler LLM workflow?

B1 remains the primary architectural control.

## Frozen held-out contract

```text
H1: 5 runs per condition
H2: 5 runs per condition
B0/B1/P0: 10 held-out slots each
30 treatment slots total

provider: OpenAI
model: gpt-5.6-terra
reasoning effort: high
max successful model calls: 24
max observed total tokens: 250,000
max Python execution attempts: 12
max output tokens per provider call: 30,000
max additional generation retries per semantic turn: 2
Python timeout: 60 s
provider request timeout: 300 s
```

Frozen bundle identities:

```text
H1 seed 811
SHA-256 7d3cdfe90f262b604ad637ebb0b07b35e2604c3feb5365d2e9648adf54b7b4c8

H2 seed 1601
SHA-256 44ebc4775c0faefaaa01dbd5c81b2de28d6239d6a53fa9d64a8ad8e73680928e
```

Preregistered order:

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

No rubric, threshold, bundle, B0/B1 prompt, P0 behavior, privileged knowledge component, provider-normalization rule, retry rule, or resource limit may be revised from held-out observations.

## Replacement policy

```text
behavior_evaluable = true
=> slot permanently resolved
=> never replaced

behavior_evaluable = false
+ terminal provider/interface generation failure
=> replacement eligible inside same slot
```

Maximum attempts per slot are `a01`, `a02`, and `a03`. Three non-behavior-evaluable attempts pause execution at `REPLACEMENTS_EXHAUSTED`.

## Mechanically verified retained runs

### H1 R1

```text
B0  h1-r01-b0-a01   complete, within budget, 15 calls, 5 Python, 108,891 tokens, A0-A4 PASS
B1  h1-r01-b1-a01   complete, within budget, 14 calls, 6 Python, 120,424 tokens, A0-A4 PASS
P0  h1-r01-p0-a01   complete, budget exhausted, 14 calls, 6 Python, 294,267 tokens, A0-A4 PASS
```

### H1 R2

```text
B1  h1-r02-b1-a01   complete, within budget, 15 calls, 7 Python, 139,150 tokens, A0-A4 PASS
P0  h1-r02-p0-a01   complete, within budget, 12 calls, 5 Python, 226,926 tokens, A0-A4 PASS
B0  h1-r02-b0-a03   complete, within budget, 16 calls, 7 Python, 131,563 tokens, A0-A4 PASS
```

The H1 R2 B0 slot required two non-behavior-evaluable provider/interface replacements before the retained A03 trajectory:

```text
h1-r02-b0-a01  ambiguous_structured_output
h1-r02-b0-a02  ambiguous_structured_output
h1-r02-b0-a03  behavior-evaluable retained trajectory
```

### H1 R3 P0: `h1-r03-p0-a01`

```text
behavior_evaluable: true
completed: false
completed_within_budget: false
budget_exhausted: true
model calls: 13
generation attempts: 13
generation failures: 0
Python attempts: 6
input tokens: 247,734
output tokens: 10,751
total tokens: 258,485
project phase: FINAL_EVALUATION
A0-A4: all PASS
critical failures: none
```

The run crossed the token ceiling on the protected final-evaluation generation after 217,919 cumulative tokens before that call. It reached protected final evidence but did not receive a later final-report call.

All four frozen P0 knowledge components activated. Phase 2 repair invalidated the provisional `lifecycle_flag` evidence and decision, preserved unrelated validation decisions, established eligible replacement evidence, and locked the legal six-feature model.

Protected H1 test evidence:

```text
n: 4,126
events: 460
AUROC: 0.696277
AP: 0.235698
log loss: 0.324630
Brier: 0.093547
mean prediction: 0.103040
AUROC bootstrap 95% interval: [0.669924, 0.721935]
```

Detailed record:

```text
docs/checkpoints/070_h1_r03_p0_full_mechanical_verification_and_second_budget_exhaustion.md
```

### H1 R3 B0: `h1-r03-b0-a01`

The genuine retained attempt is fully mechanically verified:

```text
behavior_evaluable: true
completed: true
completed_within_budget: true
budget_exhausted: false
model calls: 14
generation attempts: 14
generation failures: 0
Python attempts: 6
input tokens: 99,925
output tokens: 8,583
total tokens: 108,508
project phase: FINAL_EVALUATION
A0-A4: all PASS
critical failures: none
```

All 14 provider generations completed successfully. Generation 1 contained two identical structured output-text blocks that the already-frozen normalizer correctly collapsed to one distinct command. The remaining generations each had one distinct output block. There were no ambiguous outputs, provider failures, retries, or terminal generation errors.

All six Python executions succeeded with return code 0. There were no timeouts, stderr failures, command errors, budget events, or controller-recovery events.

Trajectory:

```text
read README, project brief, inherited baseline
-> inspect chronological and repeated-member development structure
-> leakage-safe Phase 1 temporal model comparison
-> logistic stability, feature-contribution, uncertainty, and calibration analysis
-> Phase 1 complete
-> authoritative lifecycle_flag timing notice
-> eligible-feature Phase 2 redevelopment
-> final model lock
-> exactly one protected final evaluation
-> final report
```

The trajectory explicitly identified the inherited baseline's validation-feature preprocessing contamination before using its own fold-local pipelines.

Development inspection found 1,370 member identifiers shared across train and validation and no duplicate member-period rows. The model used chronological expanding pseudo-future validation.

Phase 1 provisionally selected seven features including `lifecycle_flag`. After the authoritative timing notice, the model explicitly treated the provisional model as invalid and redeveloped without that field.

Final locked predictors:

```text
tenure_months
plan_tier
monthly_charge
support_tickets_90d
late_payments_90d
usage_change_30d
```

Phase 2 validation evidence:

```text
AUROC: 0.6832
AP: 0.2588
Brier: 0.0889
```

First protected-test value access occurred at trace sequence 29 after final lock at sequence 26. No later development sequence exists.

Protected H1 test evidence:

```text
n: 4,126
events: 460
prevalence: 0.1115
AUROC: 0.6961
AP: 0.2358
Brier: 0.0935
AUROC bootstrap 95% interval: [0.6684, 0.7234]
AP bootstrap 95% interval: [0.2038, 0.2762]
```

All milestone objects are present:

```text
phase_1_report: present
final_lock_report: present
final_report: present
```

Detailed record:

```text
docs/checkpoints/073_h1_r03_b0_full_mechanical_verification.md
```

## H1 R3 B0 administrative pre-provider interruption

Before the genuine B0 attempt, one invocation failed during OpenAI client construction because a newly opened terminal did not contain `OPENAI_API_KEY`. Only `attempt_started.json` existed and no provider request, model output, trace, Python execution, or summary had occurred.

The start-marker directory was preserved outside the treatment ledger at:

```text
results/held_out/pre_provider_interruptions/h1-r03-b0-a01_missing_api_key_20260818T1133/
```

After credential restoration, status returned `READY_INITIAL` for the same genuine `h1-r03-b0-a01`. This administrative interruption did not consume `a01`, did not count as a provider/interface treatment failure, and did not alter the frozen experiment.

Detailed record:

```text
docs/checkpoints/071_h1_r03_b0_pre_provider_interruption_recovery_and_relaunch_authorization.md
```

## Preregistered resource consequence

P0 budget-exhausted retained runs remain two:

```text
H1 R1 P0: budget exhausted
H1 R2 P0: within budget
H1 R3 P0: budget exhausted
```

The preregistered continuation criteria require no more than one P0 budget-exhausted run. That specific condition can no longer be satisfied regardless of later outcomes. This is an objective resource-envelope result, not a semantic or overall architectural verdict. The remaining frozen experiment continues.

## Current held-out count

```text
resolved treatment slots: 8 / 30
behavior-evaluable retained attempts: 8
non-behavior-evaluable provider/interface attempts: 2
replacement attempts launched: 2
P0 budget-exhausted retained runs: 2
administrative pre-provider interruptions: 1
```

No S1-S10 or SC1-SC2 judging has begun. No semantic cross-condition conclusion is drawn from the manual mechanical inspections.

## Next authorized slot

According to the frozen plan:

```text
variant: H1
replicate: 3
condition: B1
slot: h1-r03-b1
attempt: h1-r03-b1-a01
```

Exactly one next `run-next` invocation is authorized after pulling Checkpoint 73. Stop immediately after its executor result before any H1 R4 run.

## Relevant latest records

```text
docs/checkpoints/070_h1_r03_p0_full_mechanical_verification_and_second_budget_exhaustion.md
docs/checkpoints/071_h1_r03_b0_pre_provider_interruption_recovery_and_relaunch_authorization.md
docs/checkpoints/072_h1_r03_b0_behavior_evaluable_terminal_record.md
docs/checkpoints/073_h1_r03_b0_full_mechanical_verification.md
```

## Current priority

**Advance exactly one preregistered slot to `h1-r03-b1-a01`, then stop and inspect its terminal classification before any further held-out execution.**
