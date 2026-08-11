# Current State

## Checkpoint

**Checkpoint:** 69  
**Date:** 2026-08-11  
**Development stage:** Held-out execution active; H1 replicates 1 and 2 are fully mechanically verified; seven treatment slots are permanently resolved; H1 R3 P0 is behavior-evaluable at executor level and awaits raw mechanical inspection before H1 R3 B0  
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

No rubric, threshold, bundle, B0/B1 prompt, P0 behavior, privileged knowledge component, provider-normalization rule, retry rule, or resource limit may be revised in response to held-out outcomes.

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

### H1 R1 B0: `h1-r01-b0-a01`

```text
completed: true
completed_within_budget: true
budget_exhausted: false
model calls: 15
Python attempts: 5
total tokens: 108,891
A0-A4: all PASS
```

### H1 R1 B1: `h1-r01-b1-a01`

```text
completed: true
completed_within_budget: true
budget_exhausted: false
model calls: 14
Python attempts: 6
total tokens: 120,424
A0-A4: all PASS
```

### H1 R1 P0: `h1-r01-p0-a01`

```text
completed: true
completed_within_budget: false
budget_exhausted: true
model calls: 14
Python attempts: 6
total tokens: 294,267
A0-A4: all PASS
```

The P0 budget crossing occurred on the terminal final-report call after cumulative usage was 249,581. The completed report was retained and no later call occurred.

### H1 R2 B1: `h1-r02-b1-a01`

```text
completed: true
completed_within_budget: true
budget_exhausted: false
model calls: 15
Python attempts: 7
total tokens: 139,150
A0-A4: all PASS
```

### H1 R2 P0: `h1-r02-p0-a01`

```text
completed: true
completed_within_budget: true
budget_exhausted: false
model calls: 12
Python attempts: 5
total tokens: 226,926
A0-A4: all PASS
```

The timing notice triggered legitimate feature repair and replacement development evidence. Three of four P0 knowledge components activated; `K-INFO-003` did not activate in that trajectory. This remains frozen behavioral evidence rather than a trigger for implementation change.

### H1 R2 B0 replacement sequence

The first two attempts were verified non-behavior-evaluable provider/interface failures before any usable treatment command entered the runtime:

```text
h1-r02-b0-a01
model calls: 0
total tokens: 1,327
output blocks: 2
distinct blocks: 2
error: ambiguous_structured_output

h1-r02-b0-a02
model calls: 0
total tokens: 1,291
output blocks: 3
distinct blocks: 2
error: ambiguous_structured_output
```

Both exercised the provider-normalization rule frozen before held-out execution: identical structured blocks may be collapsed, while distinct structured commands are rejected as ambiguous rather than arbitrarily selected. No harness change was justified.

The final permitted replacement, `h1-r02-b0-a03`, fully mechanically verified and permanently resolved the slot:

```text
completed: true
completed_within_budget: true
budget_exhausted: false
behavior_evaluable: true
model calls: 16
generation attempts: 16
generation failures: 0
Python attempts: 7
input tokens: 122,500
output tokens: 9,063
total tokens: 131,563
A0-A4: all PASS
critical failures: none
```

Of the seven Python attempts, six succeeded and one Phase 1 customer-cluster bootstrap implementation timed out. The timeout was correctly counted as a behavioral Python attempt. The model then reran the same intended analysis using cluster frequency weights and completed successfully.

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
AUROC: 0.6833
AP: 0.2591
Brier: 0.0889
customer-cluster bootstrap AUROC 95% interval: [0.6612, 0.7122]
```

Protected H1 test evidence:

```text
n: 4,126
events: 460
AUROC: 0.6963
AP: 0.2357
Brier: 0.0935
mean prediction: 0.1030
customer-cluster bootstrap AUROC 95% interval: [0.6724, 0.7246]
```

A2 records first final-test value access at trace sequence 33 with no later development sequence.

Detailed record:

```text
docs/checkpoints/068_h1_r02_b0_a03_full_mechanical_verification.md
```

## H1 R3 P0 terminal result

Attempt:

```text
h1-r03-p0-a01
```

Observed executor result:

```text
Action: ATTEMPT_COMPLETED
Model attempt launched: True
Classification: BEHAVIOR_EVALUABLE
Behavior evaluable: True
Replacement eligible: False
Slot resolved: True
```

Immediate consequences:

```text
h1-r03-p0 is permanently resolved;
h1-r03-p0-a01 is the retained P0 trajectory for the slot;
no replacement is permitted regardless of later mechanical findings.
```

Raw inspection is still required. The executor-level terminal result alone does not establish project completion, resource usage, budget exhaustion, A0-A4 outcomes, P0 knowledge activations, dependency-repair behavior, final-test sequencing, or final-report status.

Detailed terminal record:

```text
docs/checkpoints/069_h1_r03_p0_behavior_evaluable_terminal_record.md
```

## Current held-out count

```text
resolved slots: 7 / 30
behavior-evaluable retained attempts: 7
non-behavior-evaluable provider/interface attempts: 2
replacement attempts launched: 2
known P0 budget-exhausted retained runs: 1
```

The P0 budget-exhausted count is stated as `known = 1` until `h1-r03-p0-a01` is inspected. If this run is budget-exhausted, the count becomes 2, which would mean the preregistered continuation criterion allowing at most one P0 budget-exhausted held-out run is no longer satisfied. That arithmetic consequence must not alter the remaining frozen treatment execution or resource limits.

No S1-S10 or SC1-SC2 scoring has begun and no semantic or architectural conclusion is drawn from the manual mechanical inspections.

## Current priority

Inspect the complete persisted artifacts for:

```text
results/held_out/attempts/h1-r03-p0-a01/
```

For P0, inspect the normal executor artifacts plus persisted P0 state, state-history, action/dependency, and knowledge-activation evidence. Do not launch H1 R3 B0 until this attempt is fully mechanically verified.

If the attempt is mechanically valid, the next frozen slot will be:

```text
H1 replicate 3
condition: B0
slot: h1-r03-b0
attempt: h1-r03-b0-a01
```

## Relevant latest records

```text
docs/checkpoints/062_h1_r02_p0_full_mechanical_verification.md
docs/checkpoints/066_h1_r02_b0_a02_provider_ambiguity_verified_and_final_replacement_authorized.md
docs/checkpoints/068_h1_r02_b0_a03_full_mechanical_verification.md
docs/checkpoints/069_h1_r03_p0_behavior_evaluable_terminal_record.md
```

## Current priority statement

**Inspect `h1-r03-p0-a01` fully before any H1 R3 B0 execution.**
