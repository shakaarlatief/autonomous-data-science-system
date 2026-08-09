# Current State

## Checkpoint

**Checkpoint:** 31  
**Date:** 2026-08-09  
**Development stage:** Initial P0 implementation candidate; deterministic validation pending  
**Implementation status:** All pre-P0 experimental controls are frozen. The first implementation of typed P0 state, four-component knowledge activation, dependency-aware repair, runnable-frontier validation, prospective protected-test blocking, P0 Structured Outputs, and P0 development calibration tooling has been added. No real-model P0 run has been executed yet. The immediate next step is the full deterministic test suite.

## Primary purpose

> **Create the best possible data-science process for the particular project, where what “best” means is configurable according to the project's goals, constraints, required outputs, and desired human involvement.**

The working methodological floor is semantic validity, information legitimacy, evidence validity, claim validity, and traceability/dependency integrity.

## System-level vision

The project distinguishes:

```text
1. Human-executed data-science process
2. Human + interactive LLM process
3. System-mediated data-science process
```

The long-term goal is not merely better prompting. The system should operationalize reusable process intelligence that otherwise depends on human methodological memory, steering, checking, and project navigation. The LLM is a reasoning component inside that system, not the system itself.

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

B1 remains the primary architectural control. P0 must demonstrate value from operationalization, not from receiving better methodological knowledge.

## Baseline development calibration

All six behavior-evaluable B0/B1 development trajectories completed with zero provider-generation failures and passed the current critical deterministic assertions.

```text
B0
calls: 15, 18, 19
mean calls: 17.33
mean tokens: 144,331

B1
calls: 15, 16, 17
mean calls: 16.00
mean tokens: 124,434
```

The clearest repeatable B1 semantic advantage was explicit inherited learned-preprocessing diagnosis:

```text
B0: 0 / 3 strong explicit diagnoses
B1: 2 / 3 strong explicit diagnoses
```

Static knowledge therefore helped but did not guarantee activation. Both B0 and B1 were already 3/3 strong on protected-test discipline and Phase 2 repair, creating a serious falsification bar for P0.

## Frozen held-out protocol

Authoritative protocol:

```text
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
prototype_v0/configs/held_out_protocol_v0_1.json
```

Held-out design:

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

Every provider-backed P0 state/repair reasoning call counts inside this same envelope. Deterministic state operations do not create hidden model budget.

## Frozen H1/H2 identities

Both preregistered starting seeds passed all benchmark self-tests immediately.

```text
H1
seed: 811
surface: member_key / scoring_period / lifecycle_flag
SHA-256: 7d3cdfe90f262b604ad637ebb0b07b35e2604c3feb5365d2e9648adf54b7b4c8

H2
seed: 1601
surface: account_ref / observation_period / profile_code
SHA-256: 44ebc4775c0faefaaa01dbd5c81b2de28d6239d6a53fa9d64a8ad8e73680928e
```

Registry:

```text
prototype_v0/configs/held_out_bundle_fingerprints_v0_1.json
```

These bundles were frozen before P0 implementation.

## Frozen semantic evaluator

Primary criteria remain S1-S10 from Foundation 012. The targeted architecture score is:

```text
mean(S1, S2, S3, S6, S7)
```

A strong targeted pass requires all five targeted criteria to equal 2.0.

Every behavior-evaluable held-out run receives two fresh condition-blinded judge passes. The primary judge packet excludes condition labels, treatment prompts, and P0-only internal state.

## Semantic judge calibration complete

The judge was calibrated on the six already-observed development baseline trajectories before P0 implementation.

```text
34 tests passed before judge execution
12 independent judge calls
59 / 60 exact ordinary-criterion agreements = 98.3%
1 adjacent disagreement
0 extreme disagreements
0 semantic-critical disagreements
0 / 6 manual-adjudication runs
```

The judge reproduced the important manual S3 pattern exactly:

```text
B0 S3=2: 0 / 3
B1 S3=2: 2 / 3
```

Development targeted means were 1.50 for B0 and 1.73 for B1. This remains calibration evidence only.

No rubric, continuation threshold, held-out bundle, or treatment condition was changed after judge calibration.

## P0 implementation candidate

New implementation files:

```text
prototype_v0/src/ads_v0/p0.py
prototype_v0/src/ads_v0/p0_schema.py
prototype_v0/src/ads_v0/p0_openai_model.py
prototype_v0/src/ads_v0/calibrate_p0.py
prototype_v0/tests/test_p0.py
```

### Typed state

Implemented object types:

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

Relations remain exactly:

```text
DEPENDS_ON
SUPPORTS
CONTRADICTS
ANSWERS
GENERATED_BY
```

State objects record canonical ID, type, status, scope, proposition content, source references, semantic tags, creation step, and update step. State history is append-only.

### Dependency repair

Hard `DEPENDS_ON` failure deterministically reopens or invalidates downstream hard dependents while preserving unrelated objects. Loss of one `SUPPORTS` path creates a reassessment obligation rather than blindly invalidating the supported target.

### Four and only four privileged knowledge components

```text
K-INFO-001 Protected Final Evaluation
K-INFO-002 Learned Transformation Evaluation Boundary
K-INFO-003 Prediction-Time Feature Eligibility
K-VAL-001 Generalization-Regime Question
```

Unlike B1, P0 does not receive the whole library as one static prompt block. Components instantiate scoped questions/obligations only when current state patterns make them applicable. Activation is idempotent and existing instances can reopen.

### Runnable frontier

Every proposed P0 command must cite at least one current motivator:

```text
open/reopened question
open obligation
reopened decision
project deliverable need
```

Blocking and repair concerns receive priority. ACTION objects are controller-maintained and record proposal/execution status plus `GENERATED_BY` relations to motivators.

### Prospective safeguard

P0 enables the common runtime's protected-final-evaluation gate. Premature value-level test access is blocked before execution and recorded diagnostically.

### Common external behavior

P0 retains exactly the same external project command set as B0/B1. The model response adds a structured state patch and motivator references around the common command. The blinded semantic normalizer ignores P0 internal state traffic and patch metadata.

### Provider semantics

`OpenAIP0ResponsesModel` subclasses the already calibrated OpenAI adapter so P0 keeps the same provider/model, high reasoning effort, previous-response threading, all-turn reasoning context, SDK retry disabling, timeout, usage accounting, and duplicate-equal structured-output normalization. Only the strict response schema differs.

### P0 development outputs

`calibrate_p0.py` writes the common trajectory artifacts plus:

```text
p0_state.json
p0_state_history.json
p0_knowledge_activations.json
```

These are architecture diagnostics and remain excluded from the primary blinded semantic score.

## New deterministic tests awaiting execution

Nine new tests cover:

```text
hard dependency propagation and unrelated-state preservation
support reassessment without blind invalidation
idempotent K-INFO-002 activation
K-INFO-003 and K-VAL-001 state-pattern activation
prospective protected-test blocking
minimal P0 runner completion
blinded normalizer exclusion of P0 internals
P0 OpenAI adapter schema use
strict P0 response-schema structure
```

The prior suite had 34 passing tests. If all nine new tests pass, the expected total is 43.

## Registered continuation boundary

P0 only earns a continuation signal if the preregistered integrity, cross-variant, completion, cost, and architecture-friction conditions all hold and it shows material reliability improvement over B1.

The material improvement routes remain:

```text
A. at least 2 fewer critical integrity failures than B1 across 10 held-out runs

OR

B. pooled targeted architecture score at least +0.30 over B1
   AND at least 2 additional strong targeted-pass runs
```

No threshold may be revised because of P0 development behavior.

## Relevant latest records

```text
docs/foundations/010_minimum_falsification_prototype_and_experimental_contract.md
docs/foundations/011_prototype_v0_technical_specification.md
docs/foundations/012_preregistered_held_out_evaluation_protocol.md

docs/checkpoints/027_full_six_run_baseline_calibration_analysis.md
docs/checkpoints/028_preregistered_held_out_protocol.md
docs/checkpoints/029_frozen_heldout_bundles_and_semantic_judge_infrastructure.md
docs/checkpoints/030_semantic_judge_calibration_and_p0_boundary.md
docs/checkpoints/031_initial_p0_implementation_candidate.md
```

## Current priority

**Validate the initial P0 implementation deterministically before any paid P0 run.**

Immediate next action:

```text
git pull origin main
pytest
```

If the full suite passes, record that boundary and run the first real-model P0 development-calibration trajectory on the development case only. H1/H2 remain untouched until P0 development debugging is complete.
