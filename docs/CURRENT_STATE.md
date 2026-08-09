# Current State

## Checkpoint

**Checkpoint:** 46  
**Date:** 2026-08-10  
**Development stage:** P0 behavior frozen; common B0/B1 held-out resource envelope implemented; deterministic validation pending  
**Implementation status:** The final planned P0 development trajectory (`dev-p0-04`) completed end-to-end within the independently frozen resource envelope and full raw inspection found no experiment-invalidating defect. P0 behavioral/controller logic is frozen. B0/B1 now implement the same optional token/Python accounting needed for the preregistered held-out 24-call / 250,000-token / 12-Python envelope. Four baseline resource tests were added. No held-out H1/H2 treatment run has occurred.

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

## Baseline development calibration

All six B0/B1 development trajectories completed and passed critical deterministic assertions.

```text
B0 calls: 15, 18, 19
B0 mean tokens: 144,331

B1 calls: 15, 16, 17
B1 mean tokens: 124,434
```

Clearest repeated B1 semantic advantage:

```text
explicit inherited learned-preprocessing diagnosis
B0: 0/3 strong
B1: 2/3 strong
```

Both simpler conditions were already strong on protected-test discipline and Phase 2 repair.

## Frozen held-out protocol

Authoritative records:

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

Total-token rule:

```text
if prior cumulative observed usage is >= 250,000,
no new model call may begin;

if an admitted completed call crosses the ceiling,
the call remains in the trajectory,
the run is marked budget-exceeded,
and no later treatment call may begin.
```

Observable failed-attempt usage counts. Python exceptions/timeouts count when execution is actually attempted. Behavioral budget exhaustion is never replacement-run eligible.

Frozen bundles:

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

Strong targeted pass requires all five targeted criteria to equal 2.0.

Pre-P0 calibration:

```text
59/60 exact ordinary-criterion agreements
1 adjacent disagreement
0 extreme disagreements
0 semantic-critical disagreements
0/6 manual-adjudication runs
```

The judge reproduced the key development S3 comparison exactly: B0 0/3 strong versus B1 2/3 strong.

## Frozen P0

P0 typed objects:

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
dev-p0-04: COMPLETE WITHIN BUDGET, 12 calls, 228,064 tokens, 4 Python attempts
```

The first three runs exposed generic prototype/controller defects that were documented and repaired during development. `dev-p0-04` was predeclared as the final planned behavioral development run before its result was known.

Full inspection of `dev-p0-04` found:

```text
0 P0 state-control errors
0 treatment-command recovery loops
0 model-generation failures
0 resource-budget events
all four knowledge components activated
explicit inherited preprocessing diagnosis
future temporal/repeated-entity validation reasoning
strong targeted Phase 2 repair
six-feature eligible final model
single protected final evaluation after lock
no post-test development
all deterministic assertions passed
```

Two ordinary semantic imperfections remain for held-out scoring rather than tuning: row-unit contradiction correction can be implicit rather than maximally explicit, and pre-Phase-2 feature-timing uncertainty can be only moderately qualified.

P0 behavioral/controller logic is now **frozen**. Do not run another P0 development trajectory and do not change P0 to improve benchmark scores, resource use, state relation quality, model choice, or reporting style.

## Common baseline resource enforcement now implemented

`BaselineTreatmentRunner` now supports optional:

```text
max_total_tokens
max_python_execution_attempts
```

and records:

```text
completed_within_budget
budget_exhausted
python_execution_attempts
```

Held-out orchestration will explicitly pass the frozen 250,000-token and 12-Python ceilings. Development CLI defaults remain unset for these two new limits so historical B0/B1 calibration commands remain reproducible.

Baseline enforcement now mirrors the registered/P0 semantics for:

```text
pre-call token checks
failed-attempt observable token accounting
crossing-call retention
terminal completion above ceiling => completed but not within budget
Python-attempt counting
blocking execution beyond the Python ceiling
resource-budget trace events
```

B0/B1 still do not receive P0's prospective protected-final-test gate. This change is resource-control parity only.

Four resource regression tests were added. Expected full suite:

```text
58 passed
```

## Remaining pre-held-out engineering

After deterministic validation of the baseline resource layer:

```text
1. load/validate the frozen protocol and bundle fingerprints at execution time;
2. materialize the exact preregistered 30-slot H1/H2 run plan;
3. support replacement-attempt identifiers for non-behavior-evaluable provider failures without changing slot order;
4. implement safe sequential held-out execution for B0/B1/P0;
5. implement batch blinded semantic judging;
6. implement blinded manual-adjudication routing;
7. aggregate semantic/resource/completion outcomes and apply continuation/falsification rules.
```

These are common experiment-control tasks, not treatment tuning.

## Relevant latest records

```text
docs/checkpoints/043_p0_reference_semantics_validated_and_final_development_run_boundary.md
docs/checkpoints/044_final_p0_development_run_terminal_success.md
docs/checkpoints/045_dev_p0_04_full_inspection_and_p0_behavioral_freeze.md
docs/checkpoints/046_common_baseline_resource_envelope_implemented.md
```

## Current priority

**Run the complete local test suite. Expected result: 58 passed. Do not begin H1/H2 execution yet.**
