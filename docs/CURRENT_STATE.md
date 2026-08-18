# Current State

**Checkpoint:** 80  
**Date:** 2026-08-18  
**Development stage:** Prototype V0 held-out execution active  
**Resolved treatment slots:** 10 / 30  
**Next frozen slot:** `h1-r04-b1-a01`

## What we are building

The Autonomous Data Science System aims to create the best defensible data-science process for the particular project, where the meaning of "best" depends on project goals, constraints, deliverables, and desired human involvement while methodological integrity remains non-negotiable.

System-level architectural context:

```text
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
```

The LLM is one reasoning component inside a wider system. Explicit system mechanisms must earn their complexity empirically.

## Current experiment

Prototype V0 asks:

> Can explicit project state, reusable knowledge activation, prospective safeguards, and dependency-aware repair make a strong LLM's data-science reasoning materially more reliable across a changing project than an equally capable simpler LLM workflow?

B1 remains the primary architectural control.

Quick overview:

```text
prototype_v0/README.md
```

Frozen held-out protocol:

```text
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
```

Detailed run ledger:

```text
docs/experiments/prototype_v0/HELD_OUT_STATUS.md
```

No H1/H2 S1-S10 or SC1-SC2 semantic judging has begun.

## Current experiment counts

```text
resolved treatment slots: 10 / 30
remaining treatment slots: 20 / 30
behavior-evaluable retained attempts: 10
non-behavior-evaluable provider/interface attempts: 2
replacement attempts launched: 2
P0 budget-exhausted retained runs: 2
administrative pre-provider interruptions: 1
```

## H1 replicate 4 status

The B0 slot is behavior-evaluable and fully mechanically verified:

```text
B0  h1-r04-b0-a01
completed: true
completed_within_budget: true
budget_exhausted: false
model calls: 16
Python attempts: 6
input tokens: 122,342
output tokens: 8,924
total tokens: 131,266
A0-A4: PASS
critical failures: none
```

All 16 provider generations completed successfully. The first generation contained two identical output-text blocks that the frozen normalizer correctly collapsed to one distinct command. There were no provider failures, retries, or ambiguous structured outputs.

The run made six Python attempts. One model-authored Phase 1 inspection script returned code 1 because of an attribute-access mistake; the model corrected the computation on the next Python attempt. There were no Python timeouts or infrastructure failures.

Phase 2 removed `lifecycle_flag`, regenerated development evidence, and locked the legal six-feature logistic pipeline.

Final locked predictors:

```text
tenure_months
plan_tier
monthly_charge
support_tickets_90d
late_payments_90d
usage_change_30d
```

The first and only value-level protected-test computation occurred at trace sequence 33 after final lock at sequence 30. No development followed protected-test feedback. The final report is present.

Protected H1 test evidence:

```text
n: 4,126
positives: 460
prevalence: 0.1115
AUROC: 0.6963
average precision: 0.2357
Brier: 0.0935
mean predicted risk: 0.1030
AUROC bootstrap 95% interval: [0.6693, 0.7204]
```

Detailed record:

```text
docs/checkpoints/080_h1_r04_b0_full_mechanical_verification.md
```

## Important current experimental consequence

P0 has exhausted the common 250,000-token envelope in two retained H1 runs:

```text
H1 R1 P0: budget exhausted
H1 R2 P0: within budget
H1 R3 P0: budget exhausted
```

The preregistered continuation criteria permit no more than one P0 budget-exhausted run. That specific criterion can no longer be satisfied regardless of later outcomes.

This is an objective resource result, not a semantic or overall architectural verdict. The frozen experiment continues unchanged.

## Frozen experiment integrity

The following remain frozen during held-out execution:

```text
P0 treatment behavior
B0/B1 prompts
P0 knowledge components
H1/H2 benchmark bundles
run order
resource budgets
provider/model configuration
provider normalization and retry semantics
semantic rubric
blinded judge protocol
continuation/falsification criteria
held-out executor behavior
```

No documentation or preservation update has changed treatment behavior.

## Knowledge-preservation architecture v0.3

Current preservation flow:

```text
discussion
    -> checkpoint
    -> promotion audit
    -> canonical/foundational/specification update when warranted
    -> KNOWLEDGE_MAP routing update when warranted
    -> concise CURRENT_STATE

meaningful stage boundary
    -> knowledge reconciliation
```

Key files:

```text
docs/KNOWLEDGE_MAP.md
docs/DEVELOPMENT_METHOD.md
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
docs/MAJOR_CHANGES.md
docs/experiments/prototype_v0/HELD_OUT_STATUS.md
```

## Next authorized action

According to the frozen preregistered order, the next slot is:

```text
variant: H1
replicate: 4
condition: B1
slot: h1-r04-b1
attempt: h1-r04-b1-a01
```

Exactly one next invocation is authorized:

```bash
python -m ads_v0.heldout_runner run-next
```

Stop immediately after the executor result. Do not begin H1 R4 P0 until the B1 terminal result has been classified and, if behavior-evaluable, mechanically inspected.

## Minimum reading for a future session

```text
README.md
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
prototype_v0/README.md
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
docs/experiments/prototype_v0/HELD_OUT_STATUS.md
```

For system-level architecture also read:

```text
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
```

For preservation-method context read:

```text
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
```

## Current priority

**Advance exactly one preregistered slot to `h1-r04-b1-a01`, then stop for terminal classification.**
