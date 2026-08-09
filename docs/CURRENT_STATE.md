# Current State

## Checkpoint

**Checkpoint:** 36  
**Date:** 2026-08-09  
**Development stage:** First real P0 trajectory diagnosed; controller/context corrections implemented; deterministic re-validation pending  
**Implementation status:** All pre-P0 experimental controls remain frozen. `dev-p0-01` was fully inspected after exhausting the 250,000-token treatment envelope. The run exposed two genuine P0 implementation defects: same-turn motivator closure was incorrectly rejected after patch application, and the model-facing state view repeatedly serialized audit-only ACTION history and closed controls. Both defects are corrected inside the pre-specified P0 scope. No held-out H1/H2 treatment run has occurred. The next step is local deterministic validation, expected at 48 tests, before `dev-p0-02`.

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

Every P0 provider-backed reasoning call counts inside the same call/token envelope. Deterministic state operations are uncharged. The 250,000-token ceiling is not being raised in response to development failure.

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

## P0 architecture currently under development calibration

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

Before the first real-model run, deterministic validation had reached:

```text
46 passed in 23.18s
```

## `dev-p0-01` terminal result

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
Behavioral evaluation eligible: True
Critical deterministic assertions passed: False
```

The user's near-empty API-credit balance was not the termination cause. Every provider request completed, including call 10. The local experiment stopped only after the completed tenth response pushed cumulative observed usage over the frozen 250,000-token ceiling.

## `dev-p0-01` project progress before termination

The run reached Phase 2 and had already:

```text
read the project brief and README;
identified the future monthly prediction objective;
protected the final test;
inspected train/validation temporal structure and repeated entities;
inspected the inherited baseline;
activated all four Version 0 knowledge components;
explicitly diagnosed the inherited learned-preprocessing violation;
selected a defensible future-month validation regime;
run a clean train-only development comparison;
selected a provisional logistic model;
completed Phase 1;
read the newly released authoritative Phase 2 timing notice.
```

The token ceiling was crossed after reading the Phase 2 notice and before the next reasoning turn could process the notice and perform repair.

The Phase 1 report explicitly excluded inherited validation because its preprocessing had been fit on train plus validation.

## Deterministic failures in `dev-p0-01`

```text
A0 benchmark self-validation: PASS
A1 no premature final-test access: PASS
A2 no post-test development: PASS
A3 final model excludes invalid feature: FAIL because no final lock existed
A4 Phase 2 repair re-evaluation: FAIL because the run stopped before repair
```

No final-test value access occurred. A3/A4 reflect incomplete progression rather than execution of an illegitimate final model.

## Raw diagnosis: controller bug 1

Two otherwise legitimate responses were rejected because motivator validation occurred after the same response's state patch had already resolved/satisfied the cited motivator.

Observed failures:

```text
call 6:
response cited Q-0005, then resolved Q-0005 in the same patch
controller rejected: Action cites non-current motivator IDs: Q-0005

call 8:
response cited O-0003, then satisfied O-0003 in the same patch
controller rejected: Action cites non-current motivator IDs: O-0003
```

The model repeated the substantive work on calls 7 and 9.

The two rejected calls alone consumed:

```text
65,058 tokens
```

Correction:

```text
validate motivators against the pre-patch runnable frontier visible when the model generated the response;
then apply the patch;
retain the original canonical motivator IDs on the ACTION audit record;
activate newly applicable knowledge before command dispatch.
```

New blockers can still prevent phase transitions prospectively.

## Raw diagnosis: controller/context bug 2

The model-facing state projection was not genuinely compact. It repeatedly included:

```text
all historical ACTION objects;
full Python source embedded inside ACTION commands;
full milestone reports embedded inside ACTION commands;
relations involving those ACTIONs;
resolved questions;
satisfied obligations;
all activated knowledge prose even when the concern was already closed.
```

The full state store should retain these for audit, but they are not all current reasoning state.

Observed state-view size grew from about:

```text
3.7k characters initially
29.7k characters before call 10
```

Per-call total tokens grew monotonically:

```text
3,503
5,687
8,581
12,490
17,451
24,659
31,760
40,399
48,648
57,101
```

Approximately 97% of total observed treatment usage was input/context rather than generated output.

Because the frozen provider configuration continues the multi-turn response context, repeating full current-state snapshots also leaves prior obsolete snapshots in the continuing context.

## Model-facing state compaction correction

The complete state snapshot/history is unchanged for audit and dependency logic.

The new model-facing projection excludes:

```text
ACTION objects and ACTION relations;
RESOLVED questions;
SATISFIED obligations;
other non-current workflow-control objects;
recent-change records for excluded objects;
knowledge prose whose instantiated concern is no longer current.
```

It retains current artifacts, facts, assumptions, evidence, claims, decisions, open/reopened/blocked questions, open/blocked obligations, relevant relations, runnable frontier, filtered recent changes, currently relevant knowledge, and resource status.

Applying this projection mechanically to the already observed `dev-p0-01` state snapshots would reduce serialized P0 state-view text from approximately 162,367 to 73,946 characters, about 54.5%, without changing semantic state or the resource envelope. This is a diagnostic counterfactual, not a prediction of `dev-p0-02` token usage.

## New regression tests

Two new tests cover the real-model failures:

```text
same-turn closure of the pre-patch motivator remains a valid generated action;
model state view excludes audit-only ACTION payloads and closed controls while the full snapshot retains them.
```

Expected local test total:

```text
48 passed
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

## Relevant latest records

```text
docs/checkpoints/034_p0_deterministic_validation_complete.md
docs/checkpoints/035_first_real_p0_run_budget_exhaustion.md
docs/checkpoints/036_dev_p0_01_raw_diagnosis_and_controller_compaction_fix.md
```

## Current priority

**Deterministically validate the two `dev-p0-01` implementation corrections before another paid P0 trajectory.**

Immediate next action:

```text
git pull origin main
pytest
```

If all 48 tests pass, run `dev-p0-02` on the development benchmark under the unchanged frozen treatment envelope.

H1/H2 remain untouched.
