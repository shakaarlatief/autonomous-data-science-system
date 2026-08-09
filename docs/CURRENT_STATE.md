# Current State

## Checkpoint

**Checkpoint:** 33  
**Date:** 2026-08-09  
**Development stage:** Corrected initial P0 implementation candidate; deterministic validation pending  
**Implementation status:** All pre-P0 experimental controls are frozen. The initial P0 implementation now includes typed state, the same four methodological knowledge components with state-triggered activation, dependency-aware reopening, support reassessment, runnable-frontier validation, prospective protected-test blocking, strict P0 Structured Outputs, development calibration tooling, corrected same-turn activation ordering, and repair-priority promotion for already-open feature/generalization concerns after material invalidation. No real-model P0 run has occurred yet.

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

B1 is the primary architectural control. P0 must demonstrate value from operationalization rather than from receiving better methodological knowledge.

## Completed B0/B1 development calibration

All six behavior-evaluable baseline trajectories completed with zero provider-generation failures and passed the current critical deterministic assertions.

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

Static knowledge helped but did not guarantee activation. Both B0 and B1 were already 3/3 strong on protected-test discipline and Phase 2 repair, creating a serious falsification bar for P0.

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

P0 has no hidden provider-backed reasoning budget. Every P0 model call counts inside the same model-call/token envelope. Deterministic state operations are uncharged.

## Frozen held-out bundles

Both preregistered starting seeds passed immediately:

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

These identities were frozen before P0 implementation.

## Frozen semantic judge

The targeted architecture score remains:

```text
mean(S1, S2, S3, S6, S7)
```

Strong targeted pass requires all five targeted criteria to equal 2.0.

Pre-P0 judge calibration on the six development baselines produced:

```text
59 / 60 exact ordinary-criterion agreements = 98.3%
1 adjacent disagreement
0 extreme disagreements
0 semantic-critical disagreements
0 / 6 manual-adjudication runs
```

It reproduced the key manual S3 pattern exactly:

```text
B0 S3=2: 0 / 3
B1 S3=2: 2 / 3
```

No rubric, continuation threshold, held-out bundle, B0/B1 prompt, or privileged knowledge component was changed after calibration.

## P0 implementation files

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

Objects:

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

State records canonical IDs, type-specific status, scope, proposition content, source references, semantic tags, creation/update steps, and append-only history.

Hard `DEPENDS_ON` failure reopens or invalidates downstream hard dependents while unrelated state stays current. Loss of one `SUPPORTS` path creates a reassessment obligation instead of blindly invalidating its target.

### Four and only four privileged knowledge components

```text
K-INFO-001 Protected Final Evaluation
K-INFO-002 Learned Transformation Evaluation Boundary
K-INFO-003 Prediction-Time Feature Eligibility
K-VAL-001 Generalization-Regime Question
```

P0 does not receive the entire library as one static B1-style prompt block. Components instantiate scoped questions/obligations when current state makes them applicable. Activation is idempotent and existing instances can reopen.

### Runnable frontier

Every P0 command must cite a current motivator:

```text
open/reopened question
open obligation
reopened decision
project deliverable need
```

Blocking and repair concerns receive priority. ACTION objects are controller-maintained and retain `GENERATED_BY` links to motivators.

### Corrected activation ordering

A newly applicable blocking knowledge instance may be created by facts in the current model patch. The controller must not require the same response to cite an ID that did not exist when it was generated.

Operational order is now:

```text
1. transactionally apply patch
2. reopen existing affected knowledge instances
3. validate motivators against the frontier visible when the model responded
4. create ACTION object
5. instantiate newly applicable knowledge
6. execute common command
```

Ordinary actions see the new concern on the next turn. Phase-transition actions can still be blocked before transition because newly activated blockers exist before dispatch.

### Repair-priority correction

If a feature-eligibility or validation-regime assumption is invalidated while its knowledge-derived question is already OPEN, that existing scoped question is now explicitly promoted to `priority:repair` rather than remaining an ordinary unresolved question. This lets final lock be blocked until material repair is resolved without creating duplicates.

Both controller corrections were made before any real P0 model call or held-out run.

### Common external behavior and provider semantics

P0 retains the same external command set as B0/B1. Its response adds `state_patch` and `motivator_ids` around the same command. The blinded semantic normalizer ignores P0 state-view messages and patch metadata.

`OpenAIP0ResponsesModel` subclasses the calibrated OpenAI adapter and keeps the same model, reasoning effort semantics, previous-response threading, all-turn context, disabled SDK retries, timeout, usage accounting, and duplicate-equal output normalization. Only the strict response schema changes.

### P0 diagnostic outputs

`calibrate_p0.py` writes the common run artifacts plus:

```text
p0_state.json
p0_state_history.json
p0_knowledge_activations.json
```

These are architecture diagnostics and are excluded from the primary blinded semantic score.

## Deterministic validation pending

The pre-P0 suite had 34 passing tests.

New P0 tests:

```text
9 in test_p0.py
3 in test_p0_controller.py
12 new tests total
```

Expected total if all pass:

```text
46 passed
```

No paid P0 run should begin before this suite is green.

## Registered continuation boundary

The held-out thresholds remain unchanged. P0 must satisfy all integrity, cross-variant, completion, resource, and architecture-friction requirements and show material reliability improvement over B1.

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
docs/checkpoints/033_p0_open_feature_repair_priority_correction.md
```

## Current priority

**Validate the corrected P0 implementation deterministically before any paid P0 run.**

Immediate next action:

```text
git pull origin main
pytest
```

If all 46 tests pass, record that boundary and run the first real-model P0 development-calibration trajectory on the development case only. H1/H2 remain untouched until P0 development debugging is complete.
