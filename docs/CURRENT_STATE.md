# Current State

## Checkpoint

**Checkpoint:** 51  
**Date:** 2026-08-10  
**Development stage:** P0 behavior frozen; common held-out resource parity validated; frozen H1/H2 inputs verified; exact 30-slot local plan materialized; resumable one-attempt held-out executor implemented; deterministic validation pending  
**Implementation status:** No H1/H2 treatment model call has occurred. The real local H1/H2 bundles were verified against their pre-P0 SHA-256 identities and `results/held_out/run_plan.json` was materialized successfully. A new executor now supports no-inference status inspection and explicit one-attempt-at-a-time advancement with append-only attempt bookkeeping and preregistered replacement semantics. Seven new tests were added; expected complete suite is 69 tests.

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

Token rule:

```text
if prior cumulative observed usage is >= 250,000,
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

Both selected seeds were the first preregistered candidates and passed benchmark self-tests before P0 implementation.

## Real local freeze verification and run-plan materialization

After the planning layer passed 62/62 tests, the user ran:

```bash
python -m ads_v0.heldout_execution
```

Observed:

```text
Protocol: v0.1.0
Validated bundles: H1, H2
H1: seed=811 files=9 sha256=7d3cdfe90f262b604ad637ebb0b07b35e2604c3feb5365d2e9648adf54b7b4c8
H2: seed=1601 files=9 sha256=44ebc4775c0faefaaa01dbd5c81b2de28d6239d6a53fa9d64a8ad8e73680928e
Run slots: 30
Output: C:\Projects_Data\autonomous-data-science-system\prototype_v0\results\held_out\run_plan.json
```

This command made zero model/API calls. The output identities exactly match the committed pre-P0 freeze record.

`results/held_out/run_plan.json` is now the local execution plan and should not be overwritten or regenerated after held-out execution begins.

## Preregistered run order

```text
H1
replicate 1: B0, B1, P0
replicate 2: B1, P0, B0
replicate 3: P0, B0, B1
replicate 4: B0, B1, P0
replicate 5: B1, P0, B0

H2
replicate 1: P0, B0, B1
replicate 2: B0, B1, P0
replicate 3: B1, P0, B0
replicate 4: P0, B0, B1
replicate 5: B0, B1, P0
```

Stable first slot:

```text
slot: h1-r01-b0
initial attempt: h1-r01-b0-a01
```

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

No semantic rubric, threshold, bundle, B0/B1 prompt, or privileged knowledge component may be changed after this boundary.

## Frozen P0

Typed objects:

```text
ARTIFACT FACT ASSUMPTION QUESTION EVIDENCE CLAIM DECISION OBLIGATION ACTION
```

Relations:

```text
DEPENDS_ON SUPPORTS CONTRADICTS ANSWERS GENERATED_BY
```

Exactly four privileged knowledge components:

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

`dev-p0-04` was predeclared as the final planned P0 behavioral development run. Full inspection found no experiment-invalidating defect. P0 behavioral/controller logic is frozen.

Do not change P0 to improve held-out semantics, resource use, state relation quality, model choice, or report wording.

## Common B0/B1 resource parity

`BaselineTreatmentRunner` now supports and enforces the same held-out total-token and Python-attempt limits when orchestration supplies them.

Validated common semantics:

```text
pre-call token check
failed-attempt observable token accounting
crossing-call retention
terminal completion above token ceiling => completed but not within budget
Python-attempt accounting
execution blocking beyond Python ceiling
resource-budget trace events
```

B0/B1 still do not receive P0's prospective protected-final-test safeguard.

The complete suite passed 58/58 after this layer.

## Held-out planning layer

`ads_v0.heldout_execution` performs no treatment inference and provides:

```text
frozen-bundle identity verification
exact 30-slot schedule materialization
10-slot-per-condition validation
stable replacement-attempt IDs
resource-config snapshot
run-plan no-overwrite protection
```

The complete suite passed 62/62 after this layer.

## Resumable held-out executor now implemented

New module:

```text
prototype_v0/src/ads_v0/heldout_runner.py
```

Safe CLI separation:

```text
python -m ads_v0.heldout_runner status
python -m ads_v0.heldout_runner run-next
```

`status` validates inputs and reports the next action but makes zero model calls.

`run-next` may launch **at most one** treatment attempt per explicit invocation.

Before every launch the executor:

```text
revalidates both frozen local bundles;
rebuilds the plan from the preregistered protocol and verified identities;
requires exact equality with materialized run_plan.json;
selects only the earliest unresolved slot;
loads the registered model/resource configuration;
validates the frozen timeout contract.
```

Any plan edit, bundle drift, or configuration mismatch stops before inference.

## Attempt ledger and duplicate-run protection

Attempt artifacts are stored under:

```text
results/held_out/attempts/<attempt_id>/
```

Before provider inference:

```text
attempt_started.json
```

is persisted with slot identity, plan SHA-256, bundle SHA-256, start time, and registered configuration.

After a valid treatment `summary.json` exists:

```text
attempt_record.json
```

is written with outcome classification and diagnostic wall-clock time.

If only the start marker exists, status becomes:

```text
INTERRUPTED_ATTEMPT
```

and no duplicate attempt is launched automatically.

If a valid summary exists but the final executor record is missing, the next `run-next` call performs bookkeeping reconciliation only and launches no model attempt.

## Replacement policy encoded in executor

Behavior-evaluable attempt:

```text
behavior_evaluable = true
=> slot resolved
=> never replaced
```

This includes incomplete work, budget exhaustion, Python errors/timeouts, deterministic failure, semantic mistakes, and poor methodology.

Non-behavior-evaluable provider termination:

```text
behavior_evaluable = false
terminal_generation_error = non-empty
=> replacement eligible inside same slot
```

At most:

```text
a01 initial
a02 replacement 1
a03 replacement 2
```

If all three are non-behavior-evaluable, execution returns `REPLACEMENTS_EXHAUSTED` and pauses.

The executor never skips to a later slot while an earlier slot remains unresolved.

## New executor tests

Seven deterministic tests were added for:

```text
exact first slot h1-r01-b0-a01;
behavior-evaluable slot resolution and next-slot advancement;
in-slot provider-failure replacement;
pause after three non-behavior-evaluable attempts;
interrupted-start duplicate prevention;
summary-only reconciliation without a model call;
registered model/resource propagation and tampered-plan rejection.
```

Expected complete suite:

```text
69 passed
```

## Remaining pre-held-out work

Before the first H1/H2 paid treatment attempt:

```text
1. pull the executor implementation and run the complete suite;
2. require all 69 tests to pass;
3. run `python -m ads_v0.heldout_runner status` against the real materialized plan;
4. confirm status reports h1-r01-b0-a01 and zero resolved slots;
5. checkpoint the final execution-infrastructure freeze;
6. only then authorize the first explicit `run-next` call.
```

Semantic judging, adjudication, aggregation, and continuation/falsification logic remain to be implemented after treatment execution infrastructure is frozen. No semantic judge should inspect H1/H2 before treatment execution begins.

## Relevant latest records

```text
docs/checkpoints/047_common_baseline_resource_envelope_deterministically_validated.md
docs/checkpoints/048_held_out_bundle_validation_and_run_plan_materialization.md
docs/checkpoints/049_held_out_plan_layer_deterministically_validated.md
docs/checkpoints/050_real_held_out_run_plan_materialized_and_frozen_inputs_verified.md
docs/checkpoints/051_resumable_one_attempt_held_out_executor_implemented.md
```

## Current priority

**Deterministically validate the new one-attempt held-out executor. Do not run `run-next` yet. Expected complete suite: 69 passed.**
