# Current State

## Checkpoint

**Checkpoint:** 37  
**Date:** 2026-08-09  
**Development stage:** P0 post-diagnosis corrections deterministically validated; second real-model development run authorized  
**Implementation status:** All pre-P0 experimental controls remain frozen. The first real-model P0 development trajectory (`dev-p0-01`) exposed two implementation defects, both were corrected within the pre-specified P0 scope, and the complete Prototype V0 suite now passes 48/48 tests. `dev-p0-02` is authorized on the development benchmark under the unchanged common resource envelope. No held-out H1/H2 treatment run has occurred.

## Primary purpose

> **Create the best possible data-science process for the particular project, where what “best” means is configurable according to project goals, constraints, required outputs, and desired human involvement.**

The long-term target is a system-mediated data-science process that operationalizes methodological knowledge, questions, checks, dependencies, repair, persistent state, and selective human involvement. The LLM is one reasoning component inside that system, not the system itself.

## Experimental conditions

```text
B0
Strong LLM + Python + project artifacts + strong generic data-science guidance.

B1
Same model/tools + the same four methodological concepts supplied statically.
No typed state, dynamic activation, prospective gate, or dependency repair.

P0
Same underlying model/tools + typed project state
+ the same four structured knowledge components
+ state-triggered activation/applicability
+ prospective protected-test safeguard
+ dependency-aware repair
+ minimal state-derived runnable frontier
+ append-only state-change history.
```

B1 remains the primary architectural control. P0 must demonstrate value from operationalization rather than from receiving better methodological knowledge.

## Completed B0/B1 development calibration

All six behavior-evaluable baseline trajectories completed with zero provider-generation failures and passed the critical deterministic assertions.

```text
B0 calls: 15, 18, 19
B0 mean tokens: 144,331

B1 calls: 15, 16, 17
B1 mean tokens: 124,434
```

The clearest repeatable B1 semantic advantage was explicit diagnosis of inherited learned-preprocessing contamination:

```text
B0: 0 / 3 strong explicit diagnoses
B1: 2 / 3 strong explicit diagnoses
```

Both B0 and B1 were already 3/3 strong on protected-test discipline and Phase 2 repair, so P0 faces a meaningful falsification bar.

## Frozen held-out experiment

Authoritative protocol:

```text
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
prototype_v0/configs/held_out_protocol_v0_1.json
```

Run design:

```text
H1: 5 runs per condition
H2: 5 runs per condition
B0/B1/P0: 10 held-out runs each
30 treatment runs total
```

Common treatment envelope:

```text
24 successful model calls
250,000 observed treatment tokens
12 Python execution attempts
30,000 max output tokens per provider call
2 additional generation retries per semantic turn
60 s Python timeout
300 s provider timeout
```

Every P0 provider-backed reasoning call counts inside the same call/token envelope. Deterministic state operations are uncharged. The resource envelope is not being increased in response to development failures.

## Frozen held-out bundles

```text
H1
seed: 811
member_key / scoring_period / lifecycle_flag
SHA-256: 7d3cdfe90f262b604ad637ebb0b07b35e2604c3feb5365d2e9648adf54b7b4c8

H2
seed: 1601
account_ref / observation_period / profile_code
SHA-256: 44ebc4775c0faefaaa01dbd5c81b2de28d6239d6a53fa9d64a8ad8e73680928e
```

Both preregistered starting seeds passed immediately and were frozen before P0 implementation.

## Frozen semantic judge

Targeted architecture score:

```text
mean(S1, S2, S3, S6, S7)
```

Strong targeted pass requires all five targeted criteria to equal 2.0.

Pre-P0 judge calibration produced:

```text
59 / 60 exact ordinary-criterion agreements = 98.3%
1 adjacent disagreement
0 extreme disagreements
0 semantic-critical disagreements
0 / 6 manual-adjudication runs
```

The judge reproduced the important manual S3 result exactly: B0 0/3 strong versus B1 2/3 strong. No rubric, threshold, held-out bundle, B0/B1 prompt, or privileged knowledge component changed afterward.

## P0 architecture under development calibration

Typed state objects:

```text
ARTIFACT
FACT
ASSUMPTION
QUESTION
EVIDENCE
CLAIM
DECISION
OBLIGATION
ACTION
```

Relations:

```text
DEPENDS_ON
SUPPORTS
CONTRADICTS
ANSWERS
GENERATED_BY
```

Exactly four privileged knowledge components:

```text
K-INFO-001 Protected Final Evaluation
K-INFO-002 Learned Transformation Evaluation Boundary
K-INFO-003 Prediction-Time Feature Eligibility
K-VAL-001 Generalization-Regime Question
```

The controller supports state-triggered scoped activation, idempotent knowledge instances, hard-dependency propagation, support reassessment, prospective final-test blocking, state-derived action motivators, blocking/repair priority, phase-transition gates, dependency-aware reopening, and append-only state history.

## First real P0 development trajectory

`dev-p0-01` was behavior-evaluable but did not complete:

```text
Completed: False
Completed within budget: False
Budget exhausted: True
Successful model calls: 10
Generation attempts: 10
Generation failures: 0
Input tokens: 242,743
Output tokens: 7,536
Total observed tokens: 250,279
Python execution attempts: 2
```

The run stopped because the local experiment crossed the frozen 250,000-token ceiling. The user's near-empty API-credit balance was not the cause; all ten provider calls completed successfully.

The run reached Phase 2 after strong substantive progress: it protected the final test, identified repeated temporal entities, activated all four V0 knowledge components, explicitly diagnosed inherited preprocessing contamination, chose a defensible validation regime, established clean development evidence, completed Phase 1, and read the authoritative Phase 2 timing notice.

It stopped before the next reasoning turn could perform Phase 2 repair and final lock.

## `dev-p0-01` implementation defects and corrections

### 1. Same-turn motivator closure

Two valid actions were rejected because the response's state patch resolved/satisfied the cited motivator before the controller checked whether that motivator was current.

Observed wasted calls:

```text
call 6: 24,659 tokens
call 8: 40,399 tokens
combined: 65,058 tokens
```

Correction:

```text
validate motivators against the pre-patch frontier visible to the model;
then apply the patch;
allow the same response to resolve/satisfy its motivating concern;
retain the original canonical motivator on the ACTION audit record.
```

### 2. Audit history repeated as current reasoning state

The model-facing state projection repeatedly serialized historical ACTION objects, embedded Python source, embedded milestone reports, ACTION relations, resolved questions, satisfied obligations, and stale knowledge prose.

The complete audited state still needs those records, but the LLM does not need them resent as current reasoning state each turn.

Correction:

```text
retain full state/history for audit and dependency logic;
exclude ACTION objects and ACTION relations from the model-facing current-state view;
exclude resolved questions and satisfied obligations;
retain current facts, assumptions, evidence, claims, decisions, open concerns,
relevant relations, current frontier, relevant knowledge, and a filtered change tail.
```

On the exact `dev-p0-01` state snapshots, this projection would reduce serialized P0 state-view characters from approximately 162,367 to 73,946, about 54.5%, without changing the underlying semantic state.

## Deterministic validation after corrections

The complete local suite now passes:

```text
48 passed in 9.97s
```

The added regression tests directly cover both real-model defects while all earlier benchmark/runtime/provider/evaluator/P0 tests continue to pass.

This establishes deterministic coherence of the corrections only. It does not establish behavioral superiority or guarantee that the next stochastic P0 run will finish within budget.

## What remains unchanged

```text
B0/B1 prompts
four privileged knowledge components
P0 object/relation vocabulary
model and reasoning effort
previous_response_id continuation
all-turn reasoning context
H1/H2 bundles
semantic rubric and judge
held-out run ordering
24-call ceiling
250,000-token ceiling
12-Python-attempt ceiling
continuation/falsification thresholds
```

`dev-p0-01` remains part of the development record and is not discarded or relabeled.

## Relevant latest records

```text
docs/checkpoints/034_p0_deterministic_validation_complete.md
docs/checkpoints/035_first_real_p0_run_budget_exhaustion.md
docs/checkpoints/036_dev_p0_01_raw_diagnosis_and_controller_compaction_fix.md
docs/checkpoints/037_p0_controller_corrections_deterministically_validated.md
```

## Current priority

**Run the second real-model P0 development-calibration trajectory under the unchanged frozen treatment envelope.**

Run:

```bash
python -m ads_v0.calibrate_p0 \
  --bundle generated/development \
  --run-id dev-p0-02 \
  --output results/raw/dev-p0-02 \
  --model gpt-5.6-terra \
  --reasoning-effort high \
  --max-model-calls 24 \
  --max-total-tokens 250000 \
  --max-python-execution-attempts 12 \
  --max-generation-retries 2 \
  --max-output-tokens 30000
```

Inspect the terminal summary before any further P0 replicate.

H1/H2 remain untouched until P0 development debugging is complete and the implementation is frozen for held-out execution.
