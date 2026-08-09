# Current State

## Checkpoint

**Checkpoint:** 35  
**Date:** 2026-08-09  
**Development stage:** First real P0 development run completed as a behavior-evaluable budget-exhaustion failure; raw trajectory diagnosis pending  
**Implementation status:** All pre-P0 experimental controls remain frozen. The corrected P0 candidate passed 46/46 deterministic tests, but its first real-model development trajectory exhausted the registered 250,000-token envelope after only 10 successful model calls and did not complete. No held-out H1/H2 treatment run has occurred. Do not run another P0 trajectory until the complete `dev-p0-01` artifacts are inspected.

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

All six behavior-evaluable baseline trajectories completed with zero provider-generation failures and passed the critical deterministic assertions.

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

Every P0 provider-backed reasoning call counts inside the same call/token envelope. Deterministic state operations are uncharged.

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

It reproduced the key manual S3 result exactly: B0 0/3 strong versus B1 2/3 strong. No rubric, threshold, held-out bundle, B0/B1 prompt, or privileged knowledge component changed after calibration.

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

The controller supports state-triggered scoped activation, idempotent knowledge instances, hard-dependency propagation, support reassessment, prospective final-test blocking, state-derived action motivators, blocking/repair priority, phase-transition gates, dependency-aware reopening, and append-only state history.

Two controller edge cases were corrected before any real P0 model call: same-turn activation cannot retroactively require a newly created knowledge ID, and already-open feature/generalization concerns become repair-priority after material invalidation.

P0 retains the same external command set as B0/B1. P0-only state and architecture diagnostics are excluded from the primary blinded semantic score.

## Deterministic P0 validation

The corrected implementation passed:

```text
46 passed in 23.18s
```

This validates internal deterministic consistency only, not behavioral superiority.

## First real P0 development trajectory

Run:

```text
dev-p0-01
```

Terminal result:

```text
Completed: False
Completed within budget: False
Budget exhausted: True
Successful model calls: 10
Generation attempts: 10
Generation failures: 0
Total observed tokens: 250,279
Python execution attempts: 2
Behavioral evaluation eligible: True
Critical deterministic assertions passed: False
```

Immediate facts:

```text
all provider generations completed successfully;
this is not an infrastructure/provider failure;
the run crossed the 250,000-token ceiling on call 10;
it used only 10/24 successful-call slots and 2/12 Python-attempt slots;
the trajectory therefore terminated because of token usage rather than call/Python ceilings;
the run is behavior-evaluable under the registered rules.
```

The crude average is about 25,028 observed tokens per successful call. This is a major development-calibration signal because the baseline trajectories completed with substantially lower total resource use.

The failed critical deterministic result must not yet be interpreted as an independent methodological failure. Because the run did not complete, milestone-dependent assertions may fail mechanically. Exact assertion IDs and causes require raw-artifact inspection.

## Investigation required before another P0 run

Inspect the complete `dev-p0-01` artifacts:

```text
summary.json
deterministic_evaluation.json
conversation.json
trace.jsonl
milestones.json
p0_state.json
p0_state_history.json
p0_knowledge_activations.json
```

Determine:

```text
project phase at termination;
per-call token growth;
state-object and relation growth;
knowledge activation timing;
whether state views or controller traffic are repeatedly serializing avoidable context;
whether the LLM made useful project progress or encountered architecture friction;
which deterministic critical assertions failed and why;
whether any issue is a genuine implementation defect that may be repaired inside the frozen P0 scope.
```

Do not raise the frozen held-out resource envelope simply because P0 exceeded it. First determine whether P0 can represent the same preregistered semantics more efficiently without changing treatment capability.

## Registered continuation boundary

Held-out thresholds remain unchanged. P0 must satisfy integrity, cross-variant, completion, resource, and architecture-friction requirements and show material reliability improvement over B1.

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
docs/checkpoints/035_first_real_p0_run_budget_exhaustion.md
```

## Current priority

**Diagnose `dev-p0-01` from its complete raw trajectory before modifying P0 or running another real-model P0 trajectory.**

H1/H2 remain untouched.
