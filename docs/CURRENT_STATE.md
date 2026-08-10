# Current State

## Checkpoint

**Checkpoint:** 49  
**Date:** 2026-08-10  
**Development stage:** P0 behavior frozen; common baseline resource parity validated; held-out bundle verification and exact 30-slot planning layer deterministically validated; real local plan materialization is next  
**Implementation status:** The complete suite now passes 62/62 after adding execution-time frozen H1/H2 bundle verification, exact preregistered 30-slot schedule materialization, stable replacement-attempt identifiers, and run-plan overwrite protection. No held-out H1/H2 treatment call has occurred.

## Primary purpose

> **Create the best possible data-science process for the particular project, where what “best” means is configurable according to project goals, constraints, required outputs, and desired human involvement.**

The LLM is one reasoning component inside a system that should operationalize methodological knowledge, project state, questions, evidence, claims, dependencies, repair, resource constraints, and selective human involvement.

## Prototype V0 question

> Can explicit project state, reusable knowledge activation, prospective safeguards, and dependency-aware repair make a strong LLM's data-science reasoning materially more reliable across a changing project than an equally capable simpler LLM workflow?

## Conditions

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
B0/B1/P0: 10 held-out runs each
30 treatment slots total
```

Registered common treatment configuration:

```text
provider: OpenAI
model: gpt-5.6-terra
reasoning effort: high
24 successful model calls
250,000 observed total tokens
12 Python execution attempts
30,000 max output tokens per provider call
2 additional generation retries per semantic turn
60 s Python timeout
300 s provider timeout
```

Token semantics:

```text
if prior observed cumulative usage is >= 250,000,
no new treatment call may begin;

if an admitted completed call crosses 250,000,
that call remains in the trajectory,
the run becomes budget-exceeded,
and no later treatment call may begin.
```

Observable usage from failed provider attempts counts. Model-authored Python exceptions/timeouts count as attempts if execution is reached. Behavioral resource exhaustion is not replacement-run eligible.

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

Both seeds were the first preregistered candidates and passed benchmark self-tests before P0 implementation.

## Frozen semantic judge

Targeted architecture score:

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

No semantic rubric, threshold, held-out bundle, B0/B1 prompt, or privileged knowledge component may be changed after this boundary.

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

P0 development history:

```text
dev-p0-01: incomplete, 10 calls, 250,279 tokens
dev-p0-02: incomplete, 12 calls, 291,350 tokens
dev-p0-03: incomplete, 14 calls, 260,234 tokens
dev-p0-04: complete within budget, 12 calls, 228,064 tokens, 4 Python attempts
```

`dev-p0-04` was predeclared as the final planned behavioral development run. Full inspection found no experiment-invalidating mechanical defect. P0 behavioral/controller logic is frozen.

## Common baseline resource layer

`BaselineTreatmentRunner` now supports and enforces the held-out total-token and Python-attempt ceilings when orchestration supplies them.

Validated behaviors include:

```text
pre-call total-token checks
observable failed-attempt token accounting
crossing-call retention
terminal completion above token ceiling => completed but not within budget
Python-attempt accounting
blocking execution beyond Python ceiling
resource-budget trace events
```

B0/B1 do not receive P0's prospective final-test safeguard.

Deterministic validation after this layer:

```text
58 passed in 22.70s
```

## Held-out planning layer

Module:

```text
prototype_v0/src/ads_v0/heldout_execution.py
```

It performs no model inference. It provides:

```text
execution-time loading of the preregistered protocol;
loading of the pre-P0 frozen bundle identity record;
verification of H1/H2 case_id, surface_variant, selected seed, self-test status,
file count, and aggregate SHA-256;
exact materialization of the registered 30-slot H1/H2 order;
validation that every replicate contains B0, B1, and P0 exactly once;
validation of 10 slots per condition;
stable initial and replacement-attempt identifiers;
a deterministic run-plan JSON containing verified bundle identities and resource configuration;
no-overwrite protection for an existing run plan unless explicitly forced.
```

Stable slot example:

```text
slot: h1-r01-b0
initial attempt: h1-r01-b0-a01
replacement 1: h1-r01-b0-a02
replacement 2: h1-r01-b0-a03
```

Replacement attempts remain inside the original slot and therefore cannot alter preregistered order.

Foundation 012 replacement semantics remain unchanged:

```text
provider/infrastructure generation termination after registered retries
    -> non-behavior-evaluable, replacement eligible

Python error/timeout, methodological error, semantic failure, budget exhaustion,
or other treatment behavior
    -> behavior-evaluable, not replacement eligible
```

At most two replacement attempts are permitted after the initial attempt. If all three attempts for one slot terminate non-behavior-evaluable, execution must pause for investigation.

## Latest deterministic validation

The user pulled Checkpoints 47-48 and ran the complete suite:

```text
62 passed in 9.77s
```

This validates the current common resource and planning infrastructure. It does not constitute held-out evidence because no H1/H2 treatment inference has occurred.

## Immediate next action

Materialize the real local frozen run plan from the actual git-ignored H1/H2 bundle directories:

```bash
python -m ads_v0.heldout_execution
```

Expected behavior:

```text
validate H1/H2 against the committed pre-P0 fingerprints;
write results/held_out/run_plan.json;
make zero model/API calls.
```

Do not use `--force`. If `results/held_out/run_plan.json` already exists, stop and inspect rather than overwrite it.

## After plan materialization

Implement a resumable one-attempt-at-a-time `run-next` executor that:

```text
revalidates the frozen protocol and bundle identity before every launch;
reads the immutable materialized plan rather than recomputing order ad hoc;
selects only the earliest unresolved slot;
launches exactly one attempt per invocation;
passes the registered model/configuration and 24 / 250k / 12 limits explicitly;
persists attempt metadata before and after execution;
uses replacement attempts only for non-behavior-evaluable provider/infrastructure termination;
never replaces poor methodology, Python failures/timeouts, semantic mistakes,
deterministic failures, or treatment budget exhaustion;
pauses after three non-behavior-evaluable attempts in one slot;
never skips ahead while an earlier slot is unresolved.
```

No semantic judging should begin until treatment execution infrastructure is frozen and validated.

## Relevant latest records

```text
docs/checkpoints/045_dev_p0_04_full_inspection_and_p0_behavioral_freeze.md
docs/checkpoints/046_common_baseline_resource_envelope_implemented.md
docs/checkpoints/047_common_baseline_resource_envelope_deterministically_validated.md
docs/checkpoints/048_held_out_bundle_validation_and_run_plan_materialization.md
docs/checkpoints/049_held_out_plan_layer_deterministically_validated.md
```

## Current priority

**Materialize and inspect the real local frozen held-out run plan. Do not start any H1/H2 treatment call yet.**
