# Current State

## Checkpoint

**Checkpoint:** 30  
**Date:** 2026-08-09  
**Development stage:** Final pre-P0 controls complete; P0 implementation authorized  
**Implementation status:** B0/B1 development calibration is complete and fully analyzed. The held-out protocol is preregistered, H1/H2 are frozen and fingerprinted, and the condition-blinded two-pass semantic judge has been calibrated successfully on all six development baseline trajectories. No substantive evaluator amendment was required. P0 may now be implemented inside the already frozen Version 0 scope.

## Primary purpose

> **Create the best possible data-science process for the particular project, where what “best” means is configurable according to the project's goals, constraints, required outputs, and desired human involvement.**

The working quality floor is semantic validity, information legitimacy, evidence validity, claim validity, and traceability/dependency integrity.

## System-level vision

The project distinguishes three abstraction levels:

```text
1. Human-executed data-science project
2. Human + interactive LLM project
3. System-mediated data-science project
```

The long-term goal is not merely better prompting. The intended system should operationalize reusable process intelligence that otherwise remains in human methodological memory and project navigation.

The LLM is a reasoning component inside the intended system, not the system itself.

## Prototype V0 question

> Can explicit project state, reusable knowledge activation, prospective safeguards, and dependency-aware repair make a strong LLM's data-science reasoning materially more reliable across a changing project than an equally capable simpler LLM workflow?

The semantic spine under test is:

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
Strong LLM + Python + project artifacts + strong generic data-science instruction.

B1
Same model/tools + the same four methodological concepts supplied statically.
No typed state, dynamic activation, prospective gate, or dependency repair.

P0
Same underlying model/tools + minimal typed project state
+ the same four structured knowledge components
+ activation/applicability
+ prospective protected-test safeguard
+ dependency-aware repair
+ minimal state-derived action selection
+ append-only state-change history.
```

B1 is the primary architectural control. If B1 matches P0's reliability at materially lower complexity or cost, P0 should be simplified or rejected for this project scale.

## Development benchmark

Synthetic monthly churn with:

```text
train months 1-16
validation months 17-20
test months 21-24
repeated customers plus new entrants
stale README one-row-per-customer statement
inherited baseline with learned preprocessing fit on train+validation
opaque account_state_code initially documented as scoring-time information
Phase 2 authoritative notice showing account_state_code is post-outcome/backfilled
protected final test
```

## Completed baseline calibration

| Run | Condition | Calls | Total tokens | Python actions | Critical deterministic |
|---|---|---:|---:|---:|---|
| `dev-b0-03` | B0 | 15 | 103,240 | 4 | Pass |
| `dev-b0-04` | B0 | 18 | 147,482 | 7 | Pass |
| `dev-b0-05` | B0 | 19 | 182,271 | 8 | Pass |
| `dev-b1-01` | B1 | 15 | 117,606 | 5 | Pass |
| `dev-b1-02` | B1 | 16 | 112,683 | 5 | Pass |
| `dev-b1-03` | B1 | 17 | 143,014 | 6 | Pass |

Every behavior-evaluable baseline run completed with zero provider-generation failures and passed the current critical deterministic assertions.

Resource calibration:

```text
B0 mean calls: 17.33
B0 mean tokens: 144,331
B0 mean Python actions: 6.33

B1 mean calls: 16.00
B1 mean tokens: 124,434
B1 mean Python actions: 5.33
```

The highest baseline used 19 calls, which motivated the preregistered held-out call ceiling of 24.

## Main baseline semantic findings

Across all six runs both baseline conditions strongly handled:

```text
protected final-test discipline
legitimate preprocessing in their own pipelines
future-facing temporal validation
non-mechanical treatment of repeated entities
provisional use of the opaque field under initial documentation
Phase 2 removal of the newly invalid feature
fresh legitimate development evidence before lock
one final protected evaluation
bounded non-causal claims
```

The clearest repeatable B1 advantage was explicit inherited-preprocessing diagnosis:

```text
B0: 0 / 3 explicit strong diagnoses
B1: 2 / 3 explicit strong diagnoses
```

This gives P0 a concrete knowledge-activation target: static knowledge presence helped, but did not guarantee activation.

All six baseline runs repaired the Phase 2 timing change strongly, so P0 dependency machinery faces a real ceiling/falsification test rather than a weak control.

## Preregistered held-out protocol

Authoritative files:

```text
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
prototype_v0/configs/held_out_protocol_v0_1.json
```

Run counts:

```text
H1: 5 runs per condition
H2: 5 runs per condition
B0/B1/P0: 10 held-out runs each
30 treatment runs total
```

Common treatment resource envelope:

```text
maximum successful model calls: 24
maximum observed total treatment tokens: 250,000
maximum Python execution attempts: 12
maximum output tokens per provider call: 30,000
maximum additional generation retries: 2
Python timeout: 60 seconds
provider request timeout: 300 seconds
```

Every P0 LLM call, including state/repair reasoning, counts within the same call/token envelope. Deterministic state operations do not create hidden reasoning budget.

## Frozen held-out bundles

Both preregistered starting seeds passed all benchmark self-tests immediately.

```text
H1
seed: 811
surface: member_key / scoring_period / lifecycle_flag
aggregate SHA-256:
7d3cdfe90f262b604ad637ebb0b07b35e2604c3feb5365d2e9648adf54b7b4c8

H2
seed: 1601
surface: account_ref / observation_period / profile_code
aggregate SHA-256:
44ebc4775c0faefaaa01dbd5c81b2de28d6239d6a53fa9d64a8ad8e73680928e
```

Registry:

```text
prototype_v0/configs/held_out_bundle_fingerprints_v0_1.json
```

These bundles were frozen before P0 implementation.

## Frozen semantic evaluator

Primary semantic criteria:

```text
S1 row-unit correction
S2 validation/generalization reasoning
S3 inherited preprocessing contamination
S4 pre-Phase2 prediction-time feature eligibility
S5 authoritative timing-notice response
S6 repair completeness
S7 repair precision
S8 claim validity
S9 final validation rationale
S10 final conclusions answer the project question
```

Scale:

```text
0 = materially wrong / absent / invalid
1 = acceptable but incomplete / implicit / weakly justified
2 = explicit, correct, scoped, and methodologically strong
```

Every held-out behavior-evaluable trajectory receives two fresh condition-blinded judge passes. P0-only internal state is excluded from the primary semantic packet.

Targeted architecture score:

```text
mean(S1, S2, S3, S6, S7)
```

Strong targeted pass requires all five targeted criteria to equal 2.0.

## Semantic judge calibration

After the judge infrastructure was added, the local suite passed:

```text
34 passed in 8.68s
```

Two independent judge passes were then run on all six development baseline trajectories.

Inter-pass consistency:

```text
exact ordinary-criterion agreement: 59 / 60 = 98.3%
adjacent disagreements: 1 / 60
extreme disagreements: 0 / 60
semantic-critical disagreements: 0
manual-adjudication runs: 0 / 6
```

The single adjacent disagreement was `dev-b0-03` on S2 and was resolved mechanically to 1.5 under the preregistered rule.

Development consensus targeted scores:

```text
B0:
dev-b0-03 = 1.5
dev-b0-04 = 1.4
dev-b0-05 = 1.6
mean = 1.50

B1:
dev-b1-01 = 1.8
dev-b1-02 = 1.6
dev-b1-03 = 1.8
mean = 1.73
```

The judge reproduced the important manual pattern for S3 exactly:

```text
B0 S3=2: 0 / 3
B1 S3=2: 2 / 3
```

No baseline development run achieved a strong targeted pass. S1 remained 1.0 in all six under the deliberately strict preregistered anchor requiring explicit retirement of stale row-unit documentation as well as correct operational semantics.

Judge usage over the 12 calibration calls was 243,898 tokens total, approximately 20,325 per pass. Judge cost is evaluation overhead and is not charged to treatment budgets.

Decision: the semantic judge is accepted without substantive rubric modification.

## Registered continuation boundary

P0 provides a continuation signal only if all registered integrity, cross-variant, completion, cost, and friction requirements hold and it shows material reliability improvement over B1.

The two material-improvement routes are:

```text
A. at least 2 fewer critical integrity failures than B1 across 10 held-out runs

OR

B. pooled targeted-architecture mean at least +0.30 over B1
   AND at least 2 additional strong targeted-pass runs
```

Additional requirements include no more critical failures than B1, no critical architecture-induced false block/over-invalidation, no variant-specific targeted deficit larger than 0.10, at least 9/10 P0 completions within budget, and median token/call/Python ratios each no greater than 1.50 versus B1.

## P0 implementation scope now authorized

The final pre-P0 control boundary is complete.

P0 may implement only the already specified Version 0 machinery:

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

Statuses remain type-specific, and relations remain:

```text
DEPENDS_ON
SUPPORTS
CONTRADICTS
ANSWERS
GENERATED_BY
```

The four and only four privileged reusable knowledge components remain:

```text
K-INFO-001 Protected Final Evaluation
K-INFO-002 Learned Transformation Evaluation Boundary
K-INFO-003 Prediction-Time Feature Eligibility
K-VAL-001 Generalization-Regime Question
```

Required P0 mechanics:

```text
compact current-state view per reasoning cycle
state patches rather than conversational-memory reconstruction
idempotent scoped knowledge activation
prospective protected-test gate
deterministic relation/integrity validation
dependency-aware reopening for hard dependencies
support reassessment rather than blind recursive invalidation
state-derived runnable frontier
append-only state-change history
common external command interface
common deterministic evaluator
separate architecture diagnostics
```

P0 must not add a specialist reviewer, hidden extra model, new privileged methodology, held-out-specific rules, or uncounted treatment reasoning.

## Relevant latest records

```text
docs/foundations/010_minimum_falsification_prototype_and_experimental_contract.md
docs/foundations/011_prototype_v0_technical_specification.md
docs/foundations/012_preregistered_held_out_evaluation_protocol.md

docs/checkpoints/027_full_six_run_baseline_calibration_analysis.md
docs/checkpoints/028_preregistered_held_out_protocol.md
docs/checkpoints/029_frozen_heldout_bundles_and_semantic_judge_infrastructure.md
docs/checkpoints/030_semantic_judge_calibration_and_p0_boundary.md
```

## Current priority

**Begin P0 implementation without changing the frozen held-out benchmark, semantic rubric, continuation thresholds, B0/B1 prompts, or privileged V0 knowledge set.**

The next engineering step is to implement the minimal typed state store, structured knowledge activation, dependency repair, runnable-frontier validation, P0 treatment runner, and P0 diagnostic outputs, then validate them with deterministic tests before any real P0 development-calibration run.
