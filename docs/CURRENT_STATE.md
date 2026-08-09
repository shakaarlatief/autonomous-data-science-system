# Current State

## Checkpoint

**Checkpoint:** 48  
**Date:** 2026-08-10  
**Development stage:** P0 behavior frozen; B0/B1 resource parity validated; held-out bundle verification and exact 30-slot run-plan materialization implemented; deterministic validation pending  
**Implementation status:** The complete suite passed 58/58 after common B0/B1 resource-envelope enforcement. The next condition-neutral held-out layer now validates local H1/H2 bundles against the identities frozen before P0 implementation and materializes the exact preregistered 30-slot schedule with stable replacement-attempt identifiers. Four new deterministic tests were added. No held-out H1/H2 treatment call has occurred.

## Primary purpose

> **Create the best possible data-science process for the particular project, where what “best” means is configurable according to project goals, constraints, required outputs, and desired human involvement.**

The LLM is one reasoning component inside a system that should operationalize methodological knowledge, project state, questions, evidence, claims, dependencies, repair, resource constraints, and selective human involvement.

## Prototype V0 question

> Can explicit project state, reusable knowledge activation, prospective safeguards, and dependency-aware repair make a strong LLM's data-science reasoning materially more reliable across a changing project than an equally capable simpler LLM workflow?

Semantic spine:

```text
PROJECT STATE
  -> KNOWLEDGE ACTIVATION
  -> QUESTIONS / OBLIGATIONS / CONSTRAINTS
  -> RUNNABLE ACTIONS
  -> EXECUTION
  -> EVIDENCE
  -> STATE UPDATE
  -> DEPENDENCY IMPACT / REOPENING
```

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

Common treatment configuration:

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

Token semantics remain:

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

Both seeds were the first preregistered candidates and passed deterministic benchmark self-tests before P0 implementation.

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

The judge reproduced the key development S3 result exactly: B0 0/3 strong versus B1 2/3 strong.

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
dev-p0-01: incomplete, 10 calls, 250,279 tokens, early Phase 2
dev-p0-02: incomplete, 12 calls, 291,350 tokens, reached final evaluation
dev-p0-03: incomplete, 14 calls, 260,234 tokens, repaired Phase 2 evidence
dev-p0-04: complete within budget, 12 calls, 228,064 tokens, 4 Python attempts
```

`dev-p0-04` was predeclared as the final planned behavioral development run before its result was known. Full inspection found no experiment-invalidating mechanical defect. P0 behavioral/controller logic is frozen and must not be tuned for held-out semantic scores, efficiency, state relation quality, model choice, or report wording.

## Common baseline resource layer

`BaselineTreatmentRunner` now enforces the same optional held-out token and Python ceilings as P0 when orchestration supplies them.

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

Deterministic validation after this implementation:

```text
58 passed in 22.70s
```

## Held-out pre-execution planning now implemented

New module:

```text
prototype_v0/src/ads_v0/heldout_execution.py
```

It performs no model inference. It now provides:

```text
execution-time loading of the preregistered protocol;
execution-time loading of the pre-P0 frozen bundle identity record;
verification of H1/H2 case_id, surface_variant, selected seed, self-test status,
file count, and aggregate SHA-256 fingerprint;
exact materialization of the registered 30-slot H1/H2 order;
validation that each replicate contains B0, B1, and P0 exactly once;
validation of 10 slots per condition;
stable initial and replacement-attempt identifiers;
a deterministic run-plan JSON containing the verified bundle identities and
registered treatment resource configuration;
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
or any other treatment behavior
    -> behavior-evaluable, not replacement eligible
```

At most two replacement attempts are permitted after the initial attempt. If all three attempts for one slot terminate non-behavior-evaluable, execution must pause for investigation.

## New run-plan tests

Four tests were added for:

```text
exact preregistered 30-slot order and per-condition counts;
stable attempt IDs inside a slot;
exact frozen-bundle acceptance and tamper rejection;
run-plan resource snapshot and no-overwrite protection.
```

Expected complete suite:

```text
62 passed
```

## Remaining pre-held-out engineering

After the new plan/bundle-validation tests pass:

```text
1. validate the real local H1/H2 bundles and materialize results/held_out/run_plan.json;
2. implement a safe resumable sequential run-next executor;
3. ensure replacement attempts remain inside their original slot and are used only
   for non-behavior-evaluable provider/infrastructure termination;
4. implement batch blinded semantic judging;
5. implement blinded manual-adjudication routing;
6. aggregate semantic/resource/completion outcomes and apply the preregistered
   continuation/falsification rules.
```

The planned executor should advance one unresolved attempt at a time rather than accidentally launching all 30 paid trajectories. This keeps the preregistered ordering deterministic while allowing infrastructure failures to be inspected and replaced under the frozen policy.

## Relevant latest records

```text
docs/checkpoints/045_dev_p0_04_full_inspection_and_p0_behavioral_freeze.md
docs/checkpoints/046_common_baseline_resource_envelope_implemented.md
docs/checkpoints/047_common_baseline_resource_envelope_deterministically_validated.md
docs/checkpoints/048_held_out_bundle_validation_and_run_plan_materialization.md
```

## Current priority

**Run the complete local test suite. Expected result: 62 passed. Do not start any H1/H2 treatment call yet.**
