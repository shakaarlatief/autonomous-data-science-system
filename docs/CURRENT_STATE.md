# Current State

## Checkpoint

**Checkpoint:** 38  
**Date:** 2026-08-09  
**Development stage:** Second real P0 development run exhausted token budget but passed critical deterministic integrity; raw diagnosis pending  
**Implementation status:** All pre-P0 experimental controls remain frozen. The first P0 run exposed two implementation defects that were corrected and validated with 48/48 tests. The second real-model P0 development trajectory (`dev-p0-02`) progressed further and passed all current critical deterministic assertions, but again failed to complete within the unchanged 250,000-token envelope. No held-out H1/H2 treatment run has occurred. Do not run `dev-p0-03` before complete raw-artifact inspection of `dev-p0-02`.

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

A completed provider call may push cumulative usage above 250,000 because usage is only known after the call returns. That crossing call remains part of the trajectory and no further call may begin.

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

## `dev-p0-01`

The first P0 development run was behavior-evaluable but did not complete:

```text
Completed: False
Budget exhausted: True
Successful model calls: 10
Generation failures: 0
Input tokens: 242,743
Output tokens: 7,536
Total observed tokens: 250,279
Python execution attempts: 2
Critical deterministic assertions passed: False
```

Raw diagnosis found two implementation defects:

```text
1. same-turn motivator closure was incorrectly rejected after patch application;
2. model-facing state repeatedly serialized audit-only ACTION history and closed controls.
```

Corrections:

```text
validate motivators against the pre-patch frontier visible to the model;
allow the same response to resolve/satisfy its motivating concern;
retain complete state/history for audit;
compact only the model-facing current-state projection by excluding ACTION audit payloads,
closed workflow controls, and irrelevant old knowledge prose.
```

The full suite passed after these corrections:

```text
48 passed in 9.97s
```

## `dev-p0-02` terminal result

The second real-model P0 development trajectory used the unchanged resource envelope:

```text
Completed: False
Completed within budget: False
Budget exhausted: True
Successful model calls: 12
Generation attempts: 12
Generation failures: 0
Total observed tokens: 291,350
Python execution attempts: 4
Behavioral evaluation eligible: True
Critical deterministic assertions passed: True
```

Immediate implications:

```text
provider generation remained clean with 0 failures;
the local treatment token rule again stopped the run;
P0 progressed further than dev-p0-01, using 12 calls and 4 Python actions;
all current critical deterministic integrity assertions passed;
overall project completion still failed within budget.
```

The total exceeding 250,000 does not indicate a raised budget. A provider call was admitted while cumulative usage was below the ceiling and the completed call then carried cumulative usage to 291,350. The final overshoot was 41,350 tokens.

The critical deterministic pass is encouraging but cannot safely identify the exact project position from terminal output alone. Raw artifacts are needed to determine whether Phase 2 repair, final model lock, protected final evaluation, or only the final report had been reached before termination.

## Comparison of real P0 development runs

| Measure | `dev-p0-01` | `dev-p0-02` |
|---|---:|---:|
| Completed | No | No |
| Budget exhausted | Yes | Yes |
| Successful model calls | 10 | 12 |
| Generation failures | 0 | 0 |
| Total observed tokens | 250,279 | 291,350 |
| Python attempts | 2 | 4 |
| Critical deterministic pass | No | Yes |

The larger terminal token total in `dev-p0-02` is not enough to judge whether context compaction helped because crossing-call overshoot varies with the size of the final completed call. Per-call input/output usage and state-view sizes must be compared directly.

## Required `dev-p0-02` diagnosis

Inspect:

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
exact project phase at termination;
per-call token and cumulative-usage curves;
whether the two known retry-loop defects disappeared;
model-facing state-view sizes;
state-object/relation growth and current-state composition;
knowledge activation/reopening/resolution timing;
Phase 2 invalidation and dependency propagation precision;
preservation of unrelated valid state;
protected final-evaluation behavior;
whether only a final reporting turn was missing or broader work remained;
whether any remaining excessive cost is intrinsic architecture cost or another implementation defect.
```

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

Both `dev-p0-01` and `dev-p0-02` remain part of the development record.

## Relevant latest records

```text
docs/checkpoints/034_p0_deterministic_validation_complete.md
docs/checkpoints/035_first_real_p0_run_budget_exhaustion.md
docs/checkpoints/036_dev_p0_01_raw_diagnosis_and_controller_compaction_fix.md
docs/checkpoints/037_p0_controller_corrections_deterministically_validated.md
docs/checkpoints/038_second_real_p0_run_budget_exhaustion_with_critical_integrity_pass.md
```

## Current priority

**Inspect the complete `dev-p0-02` raw trajectory before any third P0 development run or held-out execution.**

H1/H2 remain untouched.
