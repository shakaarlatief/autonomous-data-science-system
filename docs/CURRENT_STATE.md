# Current State

## Checkpoint

**Checkpoint:** 70  
**Date:** 2026-08-18  
**Development stage:** Held-out execution active; seven treatment slots permanently resolved; H1 R3 P0 fully mechanically verified; next slot is H1 R3 B0  
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

H1 R1 P0 crossed the token ceiling on the terminal final-report call after cumulative usage was 249,581. The completed report was retained and no later treatment call occurred.

### H1 R2

```text
B1  h1-r02-b1-a01   complete, within budget, 15 calls, 7 Python, 139,150 tokens, A0-A4 PASS
P0  h1-r02-p0-a01   complete, within budget, 12 calls, 5 Python, 226,926 tokens, A0-A4 PASS
B0  h1-r02-b0-a03   complete, within budget, 16 calls, 7 Python, 131,563 tokens, A0-A4 PASS
```

The H1 R2 B0 slot required two replacements before the retained A03 trajectory:

```text
h1-r02-b0-a01  non-behavior-evaluable ambiguous_structured_output
h1-r02-b0-a02  non-behavior-evaluable ambiguous_structured_output
h1-r02-b0-a03  behavior-evaluable retained trajectory
```

Both provider/interface failures occurred before any usable treatment command entered the runtime and exercised provider-normalization behavior frozen before held-out execution. No harness change was made.

H1 R2 P0 correctly repaired `lifecycle_flag` timing invalidation and re-established eligible-feature evidence. `K-INFO-003` did not activate in that trajectory, which remains frozen behavioral evidence.

### H1 R3 P0: `h1-r03-p0-a01`

Fully mechanically verified result:

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

All 13 provider generations completed normally and all six Python executions succeeded. There were no provider failures, retries, Python timeouts, command errors, or architecture-control errors.

Exact cumulative token usage was 217,919 after call 12. Call 13, the protected final-evaluation generation, was therefore legitimately admitted. It contributed 40,566 tokens and moved cumulative usage to 258,485. The resource gate then terminated later treatment reasoning. No final-report call occurred.

The run completed the analytical trajectory through one protected final evaluation, but `milestones.json` has `final_report: null`; the top-level deliverable obligation remains open in the final P0 frontier. This incompleteness is behavioral and is retained without replacement.

All four frozen P0 knowledge components activated:

```text
K-INFO-001 Protected Final Evaluation
K-INFO-002 Learned Transformation Evaluation Boundary
K-INFO-003 Prediction-Time Feature Eligibility
K-VAL-001 Generalization-Regime Question
```

Phase 2 state repair was targeted:

```text
prior lifecycle availability fact: ACTIVE -> DISPUTED
provisional pipeline decision: PROVISIONAL -> REOPENED -> SUPERSEDED
Phase 1 model evidence: CURRENT -> INVALIDATED
Phase 1 robustness evidence: CURRENT -> INVALIDATED
replacement eligible evidence: CURRENT
replacement eligible pipeline decision: ACCEPTED
support-loss obligations: satisfied before final lock
```

The accepted temporal-validation and model-selection-metric decisions were preserved. As in H1 R2 P0, the lifecycle timing question was transiently reopened when its hard dependency on the superseded provisional decision became invalid, then resolved again after the eligible pipeline was established. Preserve this for later architecture diagnostics; do not score it manually during execution.

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
n: 5,375
AUROC: 0.683297
AP: 0.259117
log loss: 0.314238
Brier: 0.088899
```

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

First final-test value access was trace sequence 32, after final lock, with no later development sequence.

Detailed record:

```text
docs/checkpoints/070_h1_r03_p0_full_mechanical_verification_and_second_budget_exhaustion.md
```

## Preregistered resource consequence

P0 budget-exhausted retained runs now equal two:

```text
H1 R1 P0: budget exhausted
H1 R2 P0: within budget
H1 R3 P0: budget exhausted
```

The preregistered continuation criteria require no more than one P0 budget-exhausted run. That specific condition can no longer be satisfied regardless of later held-out outcomes.

This is an objective resource-envelope result, not a semantic or overall architectural verdict. The remaining frozen experiment must still be completed so reliability, semantic quality, repair precision, completion, false blocking, and comparative resource distributions can be evaluated without selective stopping. No treatment or budget change is permitted.

## Current held-out count

```text
resolved slots: 7 / 30
behavior-evaluable retained attempts: 7
non-behavior-evaluable provider/interface attempts: 2
replacement attempts launched: 2
P0 budget-exhausted retained runs: 2
```

No S1-S10 or SC1-SC2 judging has begun.

## Next authorized slot

According to the frozen plan:

```text
variant: H1
replicate: 3
condition: B0
slot: h1-r03-b0
attempt: h1-r03-b0-a01
```

Exactly one next `run-next` invocation is authorized after pulling Checkpoint 70. Stop immediately after its executor result before any H1 R3 B1 run.

## Relevant latest records

```text
docs/checkpoints/066_h1_r02_b0_a02_provider_ambiguity_verified_and_final_replacement_authorized.md
docs/checkpoints/068_h1_r02_b0_a03_full_mechanical_verification.md
docs/checkpoints/069_h1_r03_p0_behavior_evaluable_terminal_record.md
docs/checkpoints/070_h1_r03_p0_full_mechanical_verification_and_second_budget_exhaustion.md
```

## Current priority

**Advance exactly one preregistered slot to `h1-r03-b0-a01`, then stop and inspect its terminal classification before any further held-out execution.**
