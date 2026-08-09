# Current State

## Checkpoint

**Checkpoint:** 32  
**Date:** 2026-08-09  
**Development stage:** Initial P0 implementation candidate corrected; deterministic validation pending  
**Implementation status:** All pre-P0 experimental controls are frozen. The first P0 implementation now includes typed state, four-component state-triggered knowledge activation, dependency-aware repair, runnable-frontier validation, prospective protected-test blocking, strict P0 Structured Outputs, a development calibration CLI, and a corrected controller ordering that avoids retroactively requiring a model response to cite knowledge-instance IDs created by that same response. No real-model P0 run has occurred yet.

## Primary purpose and system vision

> **Create the best possible data-science process for the particular project, where what “best” means is configurable according to the project's goals, constraints, required outputs, and desired human involvement.**

The long-term target is a system-mediated data-science process that operationalizes methodological knowledge, questions, checks, dependencies, repair, persistent state, and selective human involvement. The LLM is one reasoning component inside that system, not the system itself.

## Prototype V0 conditions

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

## Baseline development calibration

All six behavior-evaluable B0/B1 runs completed with zero provider-generation failures and passed the current critical deterministic assertions.

```text
B0 calls: 15, 18, 19
B0 mean tokens: 144,331

B1 calls: 15, 16, 17
B1 mean tokens: 124,434
```

The clearest repeatable B1 semantic advantage was explicit inherited learned-preprocessing diagnosis:

```text
B0: 0 / 3 strong explicit diagnoses
B1: 2 / 3 strong explicit diagnoses
```

Static knowledge therefore helped but did not guarantee activation. Both baseline conditions were already 3/3 strong on protected-test discipline and Phase 2 repair.

## Frozen held-out experiment

Protocol:

```text
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
prototype_v0/configs/held_out_protocol_v0_1.json
```

Runs:

```text
H1: 5 per condition
H2: 5 per condition
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

P0 has no hidden provider-backed reasoning budget. Deterministic state operations are uncharged, but every P0 LLM reasoning call counts within the same model-call/token envelope.

## Frozen held-out bundles

Both preregistered starting seeds passed immediately.

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

Registry:

```text
prototype_v0/configs/held_out_bundle_fingerprints_v0_1.json
```

These identities were frozen before P0 implementation.

## Frozen semantic evaluator and calibration

The targeted architecture score is:

```text
mean(S1, S2, S3, S6, S7)
```

Strong targeted pass requires all five targeted criteria to equal 2.0.

The two-pass condition-blinded judge was calibrated on all six baseline development trajectories before P0 implementation:

```text
59 / 60 exact ordinary-criterion agreements = 98.3%
1 adjacent disagreement
0 extreme disagreements
0 semantic-critical disagreements
0 / 6 manual-adjudication runs
```

It reproduced the important manual S3 pattern exactly:

```text
B0 S3=2: 0 / 3
B1 S3=2: 2 / 3
```

No rubric, continuation threshold, held-out bundle, B0/B1 prompt, or privileged knowledge component was changed after judge calibration.

## P0 implementation candidate

Implementation files:

```text
prototype_v0/src/ads_v0/p0.py
prototype_v0/src/ads_v0/p0_controller.py
prototype_v0/src/ads_v0/p0_schema.py
prototype_v0/src/ads_v0/p0_openai_model.py
prototype_v0/src/ads_v0/calibrate_p0.py
prototype_v0/tests/test_p0.py
prototype_v0/tests/test_p0_controller.py
```

### Typed state

Object types:

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

State records canonical IDs, type-specific status, scope, proposition content, sources, semantic tags, creation/update steps, and append-only change history.

Hard `DEPENDS_ON` failure reopens or invalidates downstream hard dependents while unrelated state remains current. Loss of a `SUPPORTS` path creates a reassessment obligation rather than blindly invalidating the supported target.

### Four and only four privileged components

```text
K-INFO-001 Protected Final Evaluation
K-INFO-002 Learned Transformation Evaluation Boundary
K-INFO-003 Prediction-Time Feature Eligibility
K-VAL-001 Generalization-Regime Question
```

P0 does not receive the entire library as one B1-style static prompt block. Components instantiate scoped questions/obligations from current state patterns. Activation is idempotent and existing instances can reopen.

### Runnable frontier

Every P0 command cites at least one current motivator:

```text
open/reopened question
open obligation
reopened decision
project deliverable need
```

Blocking and repair concerns receive priority. ACTION objects are controller-maintained and retain `GENERATED_BY` relations to motivators.

### Corrected activation ordering

An implementation issue was identified before any real P0 run: if a current state patch itself caused a new blocking knowledge instance to be created, the initial ordering could have required the same model response to cite that newly created canonical ID even though the ID did not exist when the response was generated.

The operational controller in `p0_controller.py` now uses:

```text
1. apply patch transactionally
2. reopen existing affected knowledge instances
3. validate motivators against the frontier visible when the model responded
4. create ACTION object
5. instantiate newly applicable knowledge
6. execute common command
```

For an ordinary action, the new concern enters the next state view. For a phase-transition action, the new blocker exists before dispatch and can still prevent the transition. This correction happened before any real P0 model call or held-out run.

`calibrate_p0.py` uses this corrected controller.

### Common external behavior and blinding

P0 uses the same external command set as B0/B1. Its response adds `state_patch` and `motivator_ids` around the same command. The primary semantic normalizer ignores P0 state-view messages and patch metadata, so internal architecture does not automatically earn semantic score.

### Provider semantics

`OpenAIP0ResponsesModel` subclasses the calibrated OpenAI adapter and retains the same model, reasoning effort semantics, previous-response threading, all-turn context, disabled SDK retries, timeout, usage accounting, and duplicate-equal output normalization. Only the strict output schema changes.

### P0 diagnostic artifacts

The P0 development CLI writes the common run outputs plus:

```text
p0_state.json
p0_state_history.json
p0_knowledge_activations.json
```

These remain architecture diagnostics and are excluded from the primary blinded semantic score.

## Deterministic tests awaiting execution

The pre-P0 suite had 34 passing tests.

Added P0 tests:

```text
9 tests in test_p0.py
2 activation-order regression tests in test_p0_controller.py
11 new tests total
```

Expected total if all pass:

```text
45 passed
```

No paid P0 run should be started before this deterministic suite is green.

## Registered continuation boundary

The held-out continuation/falsification thresholds remain unchanged. P0 must satisfy all integrity, cross-variant, completion, resource, and friction requirements and show material reliability improvement over B1.

Material improvement remains either:

```text
A. at least 2 fewer critical integrity failures than B1 across 10 held-out runs

OR

B. pooled targeted architecture score at least +0.30 over B1
   AND at least 2 additional strong targeted-pass runs
```

## Relevant latest records

```text
docs/checkpoints/030_semantic_judge_calibration_and_p0_boundary.md
docs/checkpoints/031_initial_p0_implementation_candidate.md
docs/checkpoints/032_p0_activation_order_correction_before_test.md
```

## Current priority

**Validate the corrected P0 implementation deterministically before any paid P0 run.**

Immediate next action:

```text
git pull origin main
pytest
```

If all 45 tests pass, record that boundary and run the first real-model P0 development-calibration trajectory on the development case only. H1/H2 remain untouched until P0 development debugging is complete.
