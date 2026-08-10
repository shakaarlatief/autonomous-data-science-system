# Current State

## Checkpoint

**Checkpoint:** 52  
**Date:** 2026-08-10  
**Development stage:** Held-out treatment execution infrastructure fully validated and frozen; first preregistered H1 attempt authorized  
**Implementation status:** P0 behavioral/controller logic is frozen. B0/B1 share the registered held-out resource envelope. Frozen H1/H2 bundles have been verified against pre-P0 SHA-256 identities, the exact 30-slot local run plan has been materialized, and the resumable one-attempt executor has passed the complete 69-test suite. A real no-inference status check reports `READY_INITIAL`, `0/30` resolved slots, and next attempt `h1-r01-b0-a01`. No H1/H2 treatment model call occurred before this checkpoint. The first explicit `run-next` call is now authorized.

## Primary purpose

> **Create the best possible data-science process for the particular project, where what “best” means is configurable according to project goals, constraints, required outputs, and desired human involvement.**

The LLM is one reasoning component inside a system that should operationalize methodological knowledge, project state, questions, evidence, claims, dependencies, repair, resource constraints, and selective human involvement.

## Prototype V0 question

> Can explicit project state, reusable knowledge activation, prospective safeguards, and dependency-aware repair make a strong LLM's data-science reasoning materially more reliable across a changing project than an equally capable simpler LLM workflow?

## Experimental conditions

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
```

Run design:

```text
H1: 5 runs per condition
H2: 5 runs per condition
B0/B1/P0: 10 held-out slots each
30 treatment slots total
```

Registered treatment configuration:

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
that completed call remains part of the trajectory,
the run is budget-exceeded,
and no later treatment call may begin.
```

Observable usage from failed provider attempts counts. Python errors/timeouts count when execution is actually attempted. Behavioral budget exhaustion is never replacement-run eligible.

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

The real local directories were revalidated and matched these identities exactly before run-plan materialization.

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

The materialized local execution plan is:

```text
results/held_out/run_plan.json
```

It must not be overwritten or regenerated after held-out execution begins.

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

No rubric, threshold, held-out bundle, B0/B1 prompt, or privileged knowledge component may be revised in response to held-out treatment outcomes.

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

`dev-p0-04` was predeclared as the final planned behavioral development run. Full inspection found no experiment-invalidating defect. P0 behavioral/controller logic remains frozen.

## Common B0/B1 resource parity

`BaselineTreatmentRunner` now enforces the same held-out token and Python ceilings when orchestration supplies them. Validated common semantics include pre-call token checks, failed-attempt observable token accounting, crossing-call retention, terminal completion above the token ceiling being classified as not within budget, Python-attempt accounting, and resource-budget trace events.

B0/B1 still do not receive P0's prospective protected-final-test safeguard.

## Held-out execution infrastructure

The planning layer provides frozen-bundle verification, exact 30-slot schedule materialization, stable attempt IDs, and run-plan overwrite protection.

The executor is:

```text
prototype_v0/src/ads_v0/heldout_runner.py
```

CLI:

```bash
python -m ads_v0.heldout_runner status
python -m ads_v0.heldout_runner run-next
```

`status` makes zero treatment model calls.

`run-next` may launch at most one attempt per explicit invocation. Before launch it revalidates frozen bundles, reconstructs the registered plan, requires exact equality with the materialized plan, selects only the earliest unresolved slot, and propagates the frozen model/resource configuration.

Attempt artifacts live under:

```text
results/held_out/attempts/<attempt_id>/
```

Before provider inference:

```text
attempt_started.json
```

After a valid treatment result:

```text
summary.json
attempt_record.json
```

An interrupted start marker without a valid summary blocks automatic duplicate execution. A valid summary without final executor bookkeeping is reconciled without launching another model attempt.

## Replacement policy

```text
behavior_evaluable = true
=> slot resolved
=> never replaced
```

This includes incomplete work, budget exhaustion, Python errors/timeouts, deterministic failures, semantic mistakes, and poor methodology.

```text
behavior_evaluable = false
terminal_generation_error = non-empty
=> replacement eligible inside the same slot
```

Maximum attempts inside one slot:

```text
a01 initial
a02 replacement 1
a03 replacement 2
```

Three non-behavior-evaluable attempts cause `REPLACEMENTS_EXHAUSTED` and execution pauses. The executor never skips a still-unresolved earlier slot.

## Final execution validation

The user pulled the executor and ran the complete deterministic suite:

```text
69 passed in 11.52s
```

Then the user ran the real no-inference status command:

```text
Status: READY_INITIAL
Resolved slots: 0/30
Next attempt: h1-r01-b0-a01
Initial attempt is ready for earliest unresolved slot h1-r01-b0.
Model attempt launched: False
```

This confirms that the real materialized plan and attempt ledger are clean at the execution boundary.

## Execution-infrastructure freeze

Held-out execution infrastructure is now frozen for ordinary use.

Do not change condition order, slot identities, resource budgets, replacement semantics, B0/B1 prompts, P0 behavioral/controller logic, provider/model configuration, bundle identities, phase semantics, attempt bookkeeping, or outcome classification merely to improve held-out results.

A future change during held-out execution is permitted only for a genuine common mechanical harness/runtime correctness defect under Foundation 012. Such a defect must be documented and tested, and affected comparable runs must be invalidated/rerun condition-neutrally as required by the preregistered policy.

## First authorized held-out attempt

```text
variant: H1
replicate: 1
condition: B0
slot: h1-r01-b0
attempt: h1-r01-b0-a01
```

Authorized command:

```bash
python -m ads_v0.heldout_runner run-next
```

The command may launch only this one attempt. After it returns, inspect the terminal output and persisted attempt artifacts before launching another attempt.

## Relevant latest records

```text
docs/checkpoints/049_held_out_plan_layer_deterministically_validated.md
docs/checkpoints/050_real_held_out_run_plan_materialized_and_frozen_inputs_verified.md
docs/checkpoints/051_resumable_one_attempt_held_out_executor_implemented.md
docs/checkpoints/052_held_out_execution_infrastructure_frozen_and_first_run_authorized.md
```

## Current priority

**Run exactly one held-out attempt with `python -m ads_v0.heldout_runner run-next`, then inspect its terminal outcome and persisted artifacts before any second attempt.**
