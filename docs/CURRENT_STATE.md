# Current State

## Checkpoint

**Checkpoint:** 27  
**Date:** 2026-08-09  
**Development stage:** Baseline calibration analyzed; held-out protocol freeze pending  
**Implementation status:** All three B0 and all three B1 development-calibration trajectories have been fully analyzed. Baseline calibration is complete. No additional B0/B1 development runs are needed. No new shared runtime defect was found. The next required boundary is to freeze the held-out semantic evaluator and common resource protocol independently of P0, then implement P0.

## Primary purpose

> **The system should create the best data-science process for the particular project, where what "best" means depends on the project's goals, constraints, required outputs, and desired level of human involvement.**

## System-level vision

Checkpoint 22 distinguishes:

```text
1. Human-executed data-science project
2. Human + interactive LLM project
3. System-mediated data-science project
```

The long-term goal is not merely better prompting. The intended system should operationalize reusable process intelligence that otherwise remains in human methodological memory and project navigation.

The LLM is a reasoning component inside the intended system, not the system itself.

## Prototype V0 conditions

```text
B0
Strong LLM + Python + project artifacts + strong generic data-science instruction.

B1
Same model/tools + the same four methodological concepts supplied statically.
No typed state, dynamic activation, prospective gate, or dependency repair.

P0
Same model/tools + typed project state + four structured knowledge components
+ activation/applicability + prospective safeguards
+ dependency-aware repair + minimal state-derived action selection.
```

B1 remains the critical control. If B1 matches P0's reliability at materially lower complexity or cost, P0 should be simplified or rejected for this project scale.

## Development benchmark

The synthetic churn benchmark contains:

```text
train months 1-16
validation months 17-20
test months 21-24
repeated customers plus new entrants
stale README row-unit statement
inherited baseline with learned preprocessing fit on train+validation
opaque account_state_code initially documented as scoring-time information
Phase 2 authoritative notice showing account_state_code is post-outcome/backfilled
protected final test
```

## Baseline calibration complete

All behavior-evaluable development runs completed under the same fixed configuration:

| Run | Condition | Calls | Input tokens | Output tokens | Reasoning tokens | Total tokens | Python actions | Critical deterministic assertions |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `dev-b0-03` | B0 | 15 | 96,525 | 6,715 | 1,203 | 103,240 | 4 | Pass |
| `dev-b0-04` | B0 | 18 | 138,912 | 8,570 | 1,805 | 147,482 | 7 | Pass |
| `dev-b0-05` | B0 | 19 | 171,225 | 11,046 | 2,724 | 182,271 | 8 | Pass |
| `dev-b1-01` | B1 | 15 | 109,884 | 7,722 | 2,060 | 117,606 | 5 | Pass |
| `dev-b1-02` | B1 | 16 | 104,893 | 7,790 | 1,895 | 112,683 | 5 | Pass |
| `dev-b1-03` | B1 | 17 | 133,519 | 9,495 | 2,167 | 143,014 | 6 | Pass |

Every run had zero provider-generation failures.

## Resource calibration summary

B0:

```text
mean calls: 17.33
call range: 15-19
mean total tokens: 144,331
token range: 103,240-182,271
mean Python actions: 6.33
```

B1:

```text
mean calls: 16.00
call range: 15-17
mean total tokens: 124,434
token range: 112,683-143,014
mean Python actions: 5.33
```

The first matched pair made B1 look more expensive. Across all three runs, the descriptive mean reverses because later B0 trajectories performed substantially more optional analysis. This demonstrates that one trajectory is not sufficient for resource conclusions.

The highest observed baseline used 19 of the provisional 20 successful-call budget, so a held-out envelope frozen at exactly 20 would have little stochastic margin.

## Six-run semantic findings

### Strong behavior shared by both baseline conditions

Across all six runs:

```text
protected final-test values during development
fit learned preprocessing only on legitimate training/fold information in their own models
used future-facing temporal validation
avoided a mechanical GroupKFold response to repeated IDs
provisionally retained account_state_code while documentation supported scoring-time availability
removed account_state_code after the authoritative Phase 2 notice
re-established legitimate development evidence before locking
excluded the invalid field from the final model
performed one protected final evaluation after lock
made no post-test development changes
kept final claims bounded and non-causal
```

Final models converged to nearly equivalent regularized logistic regressions using the same six legitimate features. Protected-test AUROC was effectively identical at about 0.660.

### Clearest repeatable B1 advantage

The inherited baseline fits learned preprocessing on train+validation before evaluating validation.

Explicit diagnosis of that inherited evaluation-boundary violation occurred in:

```text
B0: 0 / 3
B1: 2 / 3
```

All B0 runs avoided the contaminated inherited evidence operationally, but none made the inherited validation contamination an explicit durable conclusion.

B1 improved this targeted concern but did not activate it perfectly in every run despite the concept being statically present in the prompt.

This is important calibration evidence for the future P0 activation hypothesis: **knowledge presence is not equivalent to reliable activation and project-state instantiation.**

### Row-unit semantics

All six runs operationally recognized repeated customer-month structure, but explicit durable correction of the stale README statement remained inconsistent. The clearest milestone-level correction occurred in `dev-b1-01`.

This leaves a meaningful target for P0 typed state: correct reasoning should become explicit project semantics rather than remaining recoverable only from exploratory actions.

### Generalization regime

Both conditions chose defensible temporal validation. B1 was somewhat more consistent in explicitly representing the future population as a mix of continuing and newly observed customers.

A cleaner separation between model selection and a later untouched development holdout appeared in two B1 trajectories (`dev-b1-01`, `dev-b1-03`) and none of the B0 trajectories, but `dev-b1-02` did not reproduce that pattern. Treat this as suggestive, not established.

### Prediction-time feature eligibility before Phase 2

All six correctly retained `account_state_code` under the initial evidence. B1 did not show a consistent advantage before the notice. B0 sometimes expressed more explicit residual timing uncertainty.

### Phase 2 repair

```text
B0: 3 / 3 strong repair
B1: 3 / 3 strong repair
```

This is a second ceiling effect. P0 dependency machinery must not receive credit merely for reproducing repair behavior that the simpler baselines already perform reliably on this development case.

### Optional methodological coverage

Only `dev-b0-05` independently used customer-cluster bootstrap uncertainty. The other five runs used row-level resampling that ignored repeated-customer dependence.

This remains secondary calibration evidence and must not be inserted retroactively as privileged V0 prompt knowledge.

## Tool-execution behavior

Provider generation was reliable, but model-authored Python occasionally failed:

```text
dev-b0-04: pandas execution error, then repaired
dev-b0-05: 60-second inefficient-bootstrap timeout, then repaired
dev-b1-02: pandas execution error after useful earlier output
```

These are behavioral execution/recovery events, not common harness defects.

## Implications for V0 hypotheses

```text
H1 typed state:
still open; baselines often reason correctly while leaving semantics implicit.

H2 knowledge activation:
meaningful target exists; B1 improved explicit learned-transformation diagnosis from 0/3 to 2/3 but static prompt presence was not perfectly activated.

H3 prospective safeguards:
development-case ceiling; all baselines protected test voluntarily.

H4 dependency-aware repair:
development-case ceiling; all baselines repaired the Phase 2 invalidation correctly.

H5 state-driven action selection:
still open; trajectory/resource variability is substantial and later B0 runs performed considerably more optional work.
```

## Common-interface decision

No new shared provider/runtime defect was found after Checkpoint 17.

Do not change B0/B1 prompts, benchmark semantics, or observed baseline weaknesses after calibration.

Any condition-neutral enforcement needed for the held-out resource protocol must be specified before P0 exists and applied equally to all conditions.

## P0 remains intentionally unimplemented

Planned minimal P0 state remains:

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

with relations:

```text
DEPENDS_ON
SUPPORTS
CONTRADICTS
ANSWERS
GENERATED_BY
```

and only the four pre-specified knowledge components.

## Relevant latest checkpoints

```text
docs/checkpoints/019_first_b0_semantic_trajectory_review.md
docs/checkpoints/021_first_matched_b0_b1_semantic_comparison.md
docs/checkpoints/022_system_level_abstraction_and_reusable_reasoning_vision.md
docs/checkpoints/026_baseline_development_calibration_complete.md
docs/checkpoints/027_full_six_run_baseline_calibration_analysis.md
```

## Current priority

**Q-042 has reached the protocol-freeze boundary.**

The real B0/B1 development evidence now exists and has been analyzed. The remaining work under Q-042 is to convert calibration observations into a pre-P0 held-out protocol.

## Next step

Freeze the held-out experimental protocol independently of P0, including:

```text
semantic-evaluation rubric and blinded judge procedure
critical-versus-noncritical scoring rules
common resource envelope
execution-failure accounting
efficiency measures
continuation/falsification criteria
held-out run counts and ordering
```

Only after that boundary is recorded should P0 implementation begin.
