# Current State

## Checkpoint

**Checkpoint:** 40  
**Date:** 2026-08-09  
**Development stage:** `dev-p0-02` corrections deterministically validated; third real-model P0 development run authorized  
**Implementation status:** All pre-P0 experimental controls remain frozen. `dev-p0-02` reached legitimate protected final evaluation and passed all deterministic assertions but exhausted the 250,000-token envelope before the final reporting turn. Its raw diagnosis exposed a canonical-ID handoff defect, a terminal budget-accounting edge case, and further audit-only model-context overhead. Those corrections are implemented and the complete Prototype V0 suite now passes 50/50 tests. `dev-p0-03` is authorized on the development benchmark under the unchanged common resource envelope. No held-out H1/H2 treatment run has occurred.

## Primary purpose

> **Create the best possible data-science process for the particular project, where what “best” means is configurable according to project goals, constraints, required outputs, and desired human involvement.**

The long-term target is a system-mediated data-science process that operationalizes methodological knowledge, questions, checks, dependencies, repair, persistent state, and selective human involvement. The LLM is one reasoning component inside that system, not the system itself.

## Prototype V0 question

> Can explicit project state, reusable knowledge activation, prospective safeguards, and dependency-aware repair make a strong LLM's data-science reasoning materially more reliable across a changing project than an equally capable simpler LLM workflow?

The semantic spine remains:

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

## Baseline development calibration

All six B0/B1 development trajectories were behavior-evaluable, completed, and passed the critical deterministic assertions.

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

Static knowledge helped but did not guarantee activation. Both baselines were already strong on protected-test discipline and Phase 2 repair, creating a meaningful falsification bar for P0.

## Frozen held-out protocol

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

A call may begin only if cumulative observed usage is below 250,000. Because usage is known only after completion, the admitted call may carry the total above the ceiling. That call remains part of the trajectory, the run must be marked budget-exceeded, and no additional model call may begin.

The resource envelope has not been increased in response to P0 development failures.

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

The controller supports state-triggered scoped activation, idempotent knowledge instances, hard-dependency propagation, support reassessment, prospective final-test blocking, state-derived action motivators, blocking/repair priority, phase-transition gates, dependency-aware reopening, append-only state history, and a compact current-state projection distinct from the full audit state.

## `dev-p0-01`

First real P0 development trajectory:

```text
Completed: False
Budget exhausted: True
Successful model calls: 10
Generation failures: 0
Input tokens: 242,743
Output tokens: 7,536
Total observed tokens: 250,279
Python attempts: 2
Critical deterministic pass: False
```

The run reached early Phase 2. Raw diagnosis exposed:

```text
1. same-turn motivator closure was incorrectly rejected after patch application;
2. model-facing state repeatedly serialized audit-only ACTION history and closed controls.
```

Those defects were corrected and the suite then passed 48/48 tests.

## `dev-p0-02`

Second real P0 development trajectory under the unchanged envelope:

```text
Completed: False
Completed within budget: False
Budget exhausted: True
Successful model calls: 12
Generation attempts: 12
Generation failures: 0
Input tokens: 279,352
Output tokens: 11,998
Total observed tokens: 291,350
Python execution attempts: 4
Behavioral evaluation eligible: True
Critical deterministic assertions passed: True
```

The run completed substantive work through legitimate final evaluation:

```text
1 read project brief
2 read README
3 inspect train metadata
4 inspect temporal/entity structure
5 inspect inherited baseline code
6 leakage-safe development model comparison
7 Phase 1 complete
8 read authoritative timing notice
9 Phase 2 eligible-feature re-evaluation
10 attempted final lock, rejected by temporary/canonical state-ID mismatch
11 final lock succeeds
12 single protected final evaluation
```

At termination only final evidence/state reconciliation and `submit_final_report` remained.

Every deterministic assertion passed:

```text
A0 benchmark self-validation: PASS
A1 no premature final-test access: PASS
A2 no development after final-test feedback: PASS
A3 final model excludes invalid post-outcome feature: PASS
A4 required Phase 2 re-evaluation: PASS
```

Final locked features:

```text
tenure_months
plan_tier
monthly_charge
support_tickets_90d
late_payments_90d
usage_change_30d
```

Final protected-test evidence:

```text
n_test: 4,084
prevalence: 0.10896
AUROC: 0.66004
log loss: 0.32709
Brier: 0.09304
customer-cluster bootstrap AUROC 95% interval: [0.63266, 0.68720]
```

The Phase 2 timing notice caused targeted repair rather than project reset: stale timing semantics and dependent evidence/claims were retired, the model decision was reconsidered, unrelated temporal-validation reasoning was preserved, eligible-feature evidence was re-established, and a repaired logistic model was locked.

## Context-efficiency progress

`dev-p0-02` used fewer tokens than `dev-p0-01` at every one of the first ten common call positions. By calls 8-10 the reduction was approximately 27-29%, confirming that the first state compaction materially helped.

The second raw diagnosis then exposed a missing handoff between temporary model-created client references and controller-assigned canonical IDs. Call 10 reused a temporary reference after it had become canonical and was rejected, costing 40,698 tokens before call 11 repeated the final lock successfully.

The controller now exposes the last accepted `client_ref -> canonical_state_id` mapping in the next private P0 state view.

The model-facing state projection was also further compacted by removing repeated audit-only object/relation timestamps and the repeated recent-change history tail. Full audit state/history remain unchanged.

On the exact `dev-p0-02` snapshots, this second generic projection would reduce combined serialized state-view text by about one third without changing semantic state or capabilities.

## Protocol-accounting correction

A terminal `submit_final_report` call that crosses the token ceiling is now correctly classified as:

```text
completed = true
budget_exhausted = true
completed_within_budget = false
```

This matches the already frozen protocol and does not relax the resource threshold.

## Deterministic validation after `dev-p0-02` corrections

The complete local suite now passes:

```text
50 passed in 12.76s
```

The added/strengthened regression coverage verifies:

```text
explicit temporary-client-ref -> canonical-ID handoff;
terminal completion above the token ceiling remains budget-exceeded;
model-facing state omits repeated audit timestamps/change-history metadata;
all earlier P0 and pre-P0 tests remain green.
```

This establishes deterministic coherence of the corrections only. It does not establish P0 resource viability or architectural superiority.

## What remains unchanged

```text
B0/B1 prompts
four privileged knowledge components
P0 state object/relation vocabulary
P0 dependency semantics
P0 prospective final-test gate
model and reasoning effort
previous-response continuation
all-turn reasoning context
H1/H2 frozen bundles
semantic rubric and judge
held-out run ordering
24-call ceiling
250,000-token ceiling
12-Python-attempt ceiling
continuation/falsification thresholds
```

Both failed P0 development runs remain part of the development record.

## Relevant latest records

```text
docs/checkpoints/036_dev_p0_01_raw_diagnosis_and_controller_compaction_fix.md
docs/checkpoints/037_p0_controller_corrections_deterministically_validated.md
docs/checkpoints/038_second_real_p0_run_budget_exhaustion_with_critical_integrity_pass.md
docs/checkpoints/039_dev_p0_02_raw_diagnosis_id_handoff_and_further_context_compaction.md
docs/checkpoints/040_p0_second_corrections_deterministically_validated.md
```

## Current priority

**Run `dev-p0-03` on the development benchmark under the unchanged frozen resource envelope.**

This run should determine whether the already specified P0 machinery can now complete end-to-end after removal of the concrete implementation/interface defects observed in the first two real P0 runs.

Do not begin held-out H1/H2 execution until `dev-p0-03` is inspected and the P0 development implementation is explicitly frozen for held-out use.
