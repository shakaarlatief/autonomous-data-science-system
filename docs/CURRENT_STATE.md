# Current State

## Checkpoint

**Checkpoint:** 41  
**Date:** 2026-08-09  
**Development stage:** Third real P0 development trajectory exhausted the frozen token envelope and failed the current critical deterministic set; raw diagnosis pending  
**Implementation status:** All pre-P0 experimental controls remain frozen. The corrected P0 implementation passed 50/50 deterministic tests before `dev-p0-03`. The third real-model P0 development run used the unchanged 24-call / 250,000-token / 12-Python envelope, reached 14 successful model calls and 260,234 observed tokens, did not complete, and did not pass all current critical deterministic assertions. No held-out H1/H2 treatment run has occurred. Do not modify P0 or run another trajectory until the complete `dev-p0-03` artifacts are inspected.

## Primary purpose

> **Create the best possible data-science process for the particular project, where what “best” means is configurable according to project goals, constraints, required outputs, and desired human involvement.**

The long-term target is a system-mediated data-science process that operationalizes methodological knowledge, questions, checks, dependencies, repair, persistent state, and selective human involvement. The LLM is one reasoning component inside that system, not the system itself.

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

## Baseline calibration

All six B0/B1 development trajectories completed and passed critical deterministic assertions.

```text
B0 calls: 15, 18, 19
B0 mean tokens: 144,331

B1 calls: 15, 16, 17
B1 mean tokens: 124,434
```

The clearest repeatable B1 semantic advantage was explicit inherited learned-preprocessing diagnosis:

```text
B0: 0/3 strong
B1: 2/3 strong
```

Both simpler conditions were already strong on protected-test discipline and Phase 2 repair.

## Frozen held-out protocol

Authoritative files:

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

A call may begin only while cumulative observed usage is below 250,000. The completed crossing call remains part of the trajectory, marks the run budget-exceeded, and prevents any further call.

Frozen held-out bundles:

```text
H1 seed 811
SHA-256 7d3cdfe90f262b604ad637ebb0b07b35e2604c3feb5365d2e9648adf54b7b4c8

H2 seed 1601
SHA-256 44ebc4775c0faefaaa01dbd5c81b2de28d6239d6a53fa9d64a8ad8e73680928e
```

No held-out treatment trajectory has run.

## Frozen semantic judge

Targeted score:

```text
mean(S1, S2, S3, S6, S7)
```

Pre-P0 calibration:

```text
59/60 exact ordinary-criterion agreements
1 adjacent disagreement
0 extreme disagreements
0 semantic-critical disagreements
0/6 manual-adjudication runs
```

No rubric, threshold, bundle, B0/B1 prompt, or privileged knowledge component changed afterward.

## P0 architecture under development calibration

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

The controller supports scoped activation, idempotent knowledge instances, hard-dependency propagation, support reassessment, prospective final-test blocking, state-derived motivators/frontier, blocking and repair priority, phase gates, dependency-aware reopening, append-only audit history, and a compact model-facing current-state projection.

## Real P0 development history

### `dev-p0-01`

```text
Completed: False
Budget exhausted: True
Calls: 10
Tokens: 250,279
Python: 2
Generation failures: 0
Critical deterministic pass: False
```

Reached early Phase 2. Raw diagnosis found two implementation defects:

```text
same-turn motivator closure was incorrectly rejected;
audit-only ACTION history and closed controls were repeatedly serialized to the model.
```

Both were corrected and regression-tested.

### `dev-p0-02`

```text
Completed: False
Budget exhausted: True
Calls: 12
Tokens: 291,350
Python: 4
Generation failures: 0
Critical deterministic pass: True
```

Reached legitimate final evaluation. It completed Phase 2 targeted repair, locked a six-feature eligible logistic model, and evaluated the protected test once. Only final state/evidence reconciliation and `submit_final_report` remained.

Final test AUROC was approximately 0.66004. All deterministic assertions A0-A4 passed.

Raw diagnosis found:

```text
missing temporary-client-ref -> canonical-state-ID handoff, causing one rejected final-lock turn;
remaining audit timestamps/change-history overhead in the model-facing state view;
a terminal budget-accounting edge case.
```

Corrections implemented:

```text
explicit last_patch_client_ref_map in the private next-turn state view;
remove audit-only timestamps/change-history from repeated model state;
terminal completion above token limit is correctly marked budget-exceeded.
```

The complete local suite then passed:

```text
50 passed in 12.76s
```

### `dev-p0-03`

Third real P0 development trajectory under the same frozen envelope:

```text
Completed: False
Completed within budget: False
Budget exhausted: True
Successful model calls: 14
Generation attempts: 14
Generation failures: 0
Total observed tokens: 260,234
Python execution attempts: 4
Behavioral evaluation eligible: True
Critical deterministic assertions passed: False
```

Terminal facts only are currently known. The run used more call slots than either prior P0 development run and crossed the token ceiling by 10,234 tokens on its final admitted call. The terminal summary does not identify the failed critical assertion or exact project phase.

Do not interpret the regression from critical-pass in `dev-p0-02` to critical-fail in `dev-p0-03` until the raw trajectory is inspected. It may reflect stochastic model behavior, incomplete progression, state/controller friction, or another implementation defect.

## What remains unchanged

```text
B0/B1 prompts
four privileged knowledge components
P0 state vocabulary and dependency semantics
P0 prospective final-test gate
model and reasoning effort
previous-response continuation
all-turn reasoning context
H1/H2 frozen bundles
semantic rubric and judge
held-out ordering
24-call ceiling
250,000-token ceiling
12-Python-attempt ceiling
continuation/falsification thresholds
```

All three P0 development trajectories remain part of the development record.

## Relevant latest records

```text
docs/checkpoints/038_second_real_p0_run_budget_exhaustion_with_critical_integrity_pass.md
docs/checkpoints/039_dev_p0_02_raw_diagnosis_id_handoff_and_further_context_compaction.md
docs/checkpoints/040_p0_second_corrections_deterministically_validated.md
docs/checkpoints/041_third_real_p0_run_budget_exhaustion_terminal_record.md
```

## Current priority

**Inspect the complete `dev-p0-03` raw trajectory before modifying P0, running another development trajectory, or beginning H1/H2.**

Required artifacts:

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
