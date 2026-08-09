# Current State

## Checkpoint

**Checkpoint:** 34  
**Date:** 2026-08-09  
**Development stage:** P0 deterministic validation complete; first real-model P0 development run authorized  
**Implementation status:** All pre-P0 experimental controls are frozen. The corrected initial P0 implementation passed the complete deterministic suite with 46/46 tests. No real-model P0 run has occurred yet. The next step is the first paid P0 development-calibration trajectory on the development case only.

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

## Current P0 implementation

Files:

```text
prototype_v0/src/ads_v0/p0.py
prototype_v0/src/ads_v0/p0_controller.py
prototype_v0/src/ads_v0/p0_schema.py
prototype_v0/src/ads_v0/p0_openai_model.py
prototype_v0/src/ads_v0/calibrate_p0.py
prototype_v0/tests/test_p0.py
prototype_v0/tests/test_p0_controller.py
```

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

The controller supports:

```text
state-triggered scoped knowledge activation
idempotent knowledge instances
hard DEPENDS_ON propagation
SUPPORTS reassessment obligations
prospective final-test blocking
state-derived action motivators
blocking/repair priority
phase-transition gates
dependency-aware reopening
append-only state history
```

Two implementation edge cases were corrected before any real P0 model call:

```text
same-turn activation does not retroactively require citing a just-created knowledge ID;
already-open feature/generalization concerns are promoted to repair priority after material invalidation.
```

P0 retains the same external command interface as B0/B1 and the same underlying model/provider semantics. Its primary blinded semantic score excludes P0-only internal state and architecture diagnostics.

## Deterministic P0 validation complete

The local full test suite passed after the corrected P0 implementation was pulled:

```text
46 passed in 23.18s
```

Composition:

```text
34 pre-P0 tests
9 P0 core tests
3 P0 controller tests
```

This validates the implementation candidate deterministically. It does not establish behavioral superiority.

The green suite covers the new P0 machinery together with the unchanged pre-existing benchmark/runtime/provider/evaluator tests.

## First real P0 development run

The first paid P0 trajectory is now authorized on the development benchmark only:

```text
run_id: dev-p0-01
bundle: generated/development
condition: P0
model: gpt-5.6-terra
reasoning effort: high
successful-call ceiling: 24
observed-token ceiling: 250,000
Python-attempt ceiling: 12
per-call output ceiling: 30,000
additional generation retries: 2
```

Purpose:

```text
verify real-model P0 schema use
observe state-patch coherence over a full trajectory
observe knowledge activation timing
check for controller deadlock or excessive friction
observe Phase 2 dependency repair
check resource-envelope viability
confirm the common semantic normalizer can judge the resulting external behavior
```

The development run is implementation calibration only. H1/H2 remain untouched.

If a genuine P0 implementation defect is found during development calibration, it may be repaired provided the change stays inside the pre-specified P0 scope and does not use held-out treatment behavior.

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
docs/checkpoints/034_p0_deterministic_validation_complete.md
```

## Current priority

**Run the first real-model P0 development-calibration trajectory.**

Do not begin held-out H1/H2 execution until P0 development debugging is complete and the implementation is frozen for held-out use.
