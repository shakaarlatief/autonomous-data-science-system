# Current State

## Checkpoint

**Checkpoint:** 67  
**Date:** 2026-08-10  
**Development stage:** Held-out execution active; H1 R2 B0 resolved on final permitted replacement A03, which is behavior-evaluable at executor level and awaits raw mechanical inspection before H1 R3 begins  
**Implementation status:** P0 behavioral/controller logic, B0/B1 prompts, bundle identities, resource budgets, semantic rubric, provider/model configuration, materialized run plan, common provider normalization, retry semantics, and held-out execution infrastructure remain frozen. H1 R1 is fully mechanically verified. H1 R2 B1 and P0 are fully mechanically verified. H1 R2 B0 A01 and A02 were fully verified non-behavior-evaluable provider/interface failures. A03 has now resolved the B0 slot as behavior-evaluable. No H1/H2 semantic judging has begun.

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
+ terminal provider/interface generation failure before usable treatment continuation
=> replacement eligible inside same slot
```

Maximum attempts per slot:

```text
a01 initial
a02 replacement 1
a03 replacement 2
```

Three non-behavior-evaluable attempts would pause execution at `REPLACEMENTS_EXHAUSTED`.

## Mechanically verified behavior-evaluable runs

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

The P0 budget crossing occurred on the terminal final-report call after cumulative usage was 249,581. The report was retained and no later call occurred.

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

### H1 R2 P0: `h1-r02-p0-a01`

```text
completed: true
completed_within_budget: true
budget_exhausted: false
model calls: 12
Python attempts: 5
total tokens: 226,926
A0-A4: all PASS
critical failures: none
```

This P0 run correctly removed `lifecycle_flag` after the authoritative timing notice, re-established eligible-feature evidence, and preserved unrelated valid state. Three of four P0 knowledge components activated; `K-INFO-003` did not activate, but the trajectory independently handled the timing issue correctly. This remains frozen behavioral evidence.

## H1 R2 B0 replacement sequence

### A01: `h1-r02-b0-a01`

Fully verified non-behavior-evaluable provider/interface failure:

```text
model calls: 0
generation attempts: 1
generation failures: 1
Python attempts: 0
total tokens: 1,327
structured_output_error: ambiguous_structured_output
output_text_block_count: 2
distinct_output_text_block_count: 2
retryable: false
```

No usable B0 treatment command entered the runtime.

### A02: `h1-r02-b0-a02`

Fully verified non-behavior-evaluable provider/interface failure:

```text
model calls: 0
generation attempts: 1
generation failures: 1
Python attempts: 0
total tokens: 1,291
structured_output_error: ambiguous_structured_output
output_text_block_count: 3
distinct_output_text_block_count: 2
retryable: false
```

No usable B0 treatment command entered the runtime.

Both failures exercised the provider-normalization behavior frozen before held-out execution: identical structured blocks may be collapsed, while distinct structured commands are rejected as ambiguous rather than arbitrarily selected. Neither event justified a harness change.

### A03: `h1-r02-b0-a03`

The final permitted replacement returned:

```text
Action: ATTEMPT_COMPLETED
Model attempt launched: True
Attempt: h1-r02-b0-a03
Classification: BEHAVIOR_EVALUABLE
Behavior evaluable: True
Replacement eligible: False
Slot resolved: True
```

Immediate consequences:

```text
h1-r02-b0 is permanently resolved;
A03 is the retained behavior-evaluable attempt for the slot;
A01 and A02 remain provider/interface failure records only;
REPLACEMENTS_EXHAUSTED was not reached.
```

Raw inspection of A03 is still required. The terminal classification does not establish project completion, resource usage, deterministic A0-A4 outcomes, final-test sequencing, or final-report status.

Detailed terminal record:

```text
docs/checkpoints/067_h1_r02_b0_a03_behavior_evaluable_terminal_record.md
```

## Current held-out count

```text
resolved slots: 6 / 30
behavior-evaluable retained attempts: 6
non-behavior-evaluable provider/interface failure attempts: 2
replacement attempts launched: 2
P0 budget-exhausted runs: 1
```

No S1-S10 or SC1-SC2 semantic judging has begun.

## Next step

Inspect the complete persisted artifacts for:

```text
results/held_out/attempts/h1-r02-b0-a03/
```

At minimum inspect:

```text
attempt_started.json
attempt_record.json
summary.json
deterministic_evaluation.json
conversation.json
trace.jsonl
milestones.json
```

Do not launch the next preregistered slot until A03 is fully mechanically verified.

If A03 is mechanically valid, the next frozen slot will be:

```text
H1 replicate 3
condition: P0
slot: h1-r03-p0
attempt: h1-r03-p0-a01
```

## Relevant latest records

```text
docs/checkpoints/062_h1_r02_p0_full_mechanical_verification.md
docs/checkpoints/064_h1_r02_b0_a01_provider_ambiguity_verified_and_replacement_authorized.md
docs/checkpoints/066_h1_r02_b0_a02_provider_ambiguity_verified_and_final_replacement_authorized.md
docs/checkpoints/067_h1_r02_b0_a03_behavior_evaluable_terminal_record.md
```

## Current priority

**Inspect `h1-r02-b0-a03` fully before any H1 R3 execution.**
