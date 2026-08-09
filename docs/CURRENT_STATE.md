# Current State

## Checkpoint

**Checkpoint:** 26  
**Date:** 2026-08-09  
**Development stage:** Baseline development calibration complete; full cross-run analysis pending  
**Implementation status:** Three behavior-evaluable B0 and three behavior-evaluable B1 development trajectories have completed under the fixed common configuration. All six completed successfully, had zero generation failures, and passed the current critical deterministic assertions. No further baseline replicate is currently required. The next step is full semantic/resource comparison before freezing the held-out protocol and implementing P0.

## Primary purpose

> **The system should create the best data-science process for the particular project, where what "best" means depends on the project's goals, constraints, required outputs, and desired level of human involvement.**

## System-level vision

Checkpoint 22 distinguishes three abstraction levels:

```text
1. Human-executed data-science project
2. Human + interactive LLM project
3. System-mediated data-science project
```

The long-term goal is not merely better prompting. The intended system should operationalize reusable process intelligence that otherwise remains in human methodological memory and project navigation, including project-state tracking, reusable knowledge, context-sensitive investigations, safeguards, dependency-aware repair, resource-aware prioritization, persistent project memory, and selective human escalation.

The LLM is a reasoning component inside that system, not the system itself.

B0 and B1 remain lower-level controls that test how much of a specific methodological benefit can already be achieved by a strong reasoner and static prompting before richer system machinery is credited.

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

B1 is the critical control. If B1 matches P0's reliability at materially lower complexity or cost, P0 should be simplified or rejected for this project scale.

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

The common runtime provides phase-aware artifact visibility, metadata/value access, declared-input Python execution, tracing, milestone transitions, final-model lock semantics, and resource accounting.

The deterministic evaluator checks benchmark validity, premature test access, post-test development, final feature legitimacy, and Phase 2 re-evaluation after material feature invalidation.

## Fixed development-calibration configuration

```text
model: gpt-5.6-terra
reasoning effort: high
max successful model calls: 20
max output tokens per call: 30,000
max additional generation retries: 2
request timeout: 300 seconds
strict Structured Outputs
multi-turn previous_response_id continuation
all-turn reasoning context
```

The six behavior-evaluable baseline runs were completed without changing this common configuration.

## Infrastructure diagnostics

`dev-b0-01` was not behavior-evaluable. It exposed the original 10,000-token output ceiling and missing incomplete-response usage accounting. Checkpoint 16 corrected both condition-neutrally.

`dev-b0-02` was not behavior-evaluable. It exposed duplicate-equal structured message blocks whose SDK aggregate was invalid as one JSON document. Checkpoint 17 added conservative duplicate-equal normalization while preserving ambiguity errors for distinct commands.

No later completed baseline run exposed another shared provider/runtime defect.

## Completed behavior-evaluable baseline calibration

| Run | Condition | Calls | Generation failures | Total observed tokens | Critical deterministic assertions |
|---|---|---:|---:|---:|---|
| `dev-b0-03` | B0 | 15 | 0 | 103,240 | Pass |
| `dev-b0-04` | B0 | 18 | 0 | 147,482 | Pass |
| `dev-b0-05` | B0 | 19 | 0 | 182,271 | Pass |
| `dev-b1-01` | B1 | 15 | 0 | 117,606 | Pass |
| `dev-b1-02` | B1 | 16 | 0 | 112,683 | Pass |
| `dev-b1-03` | B1 | 17 | 0 | 143,014 | Pass |

Replicate counts are now:

```text
B0: 3 / 3
B1: 3 / 3
```

Every behavior-evaluable baseline trajectory completed within the 20-call ceiling, with zero generation failures, and passed all current critical deterministic assertions.

## Resource observations

B0:

```text
calls: 15, 18, 19
mean calls: 17.33
mean total observed tokens: 144,331
token range: 79,031
```

B1:

```text
calls: 15, 16, 17
mean calls: 16.00
mean total observed tokens: approximately 124,434
token range: 30,331
```

The first matched pair had B1 using more tokens than B0. Across all three development replicates, the descriptive mean reverses: B0 used approximately 19,897 more tokens per run on average, about 16 percent relative to the B1 mean.

This reversal shows why a single trajectory cannot support a resource-efficiency conclusion. Raw trajectory decomposition is still required before interpreting condition-level efficiency.

The highest observed call count was 19 in `dev-b0-05`, leaving only one call of margin under the provisional 20-call ceiling. This must be considered when freezing the held-out resource envelope.

## Semantic evidence already reviewed

The first matched pair, `dev-b0-03` versus `dev-b1-01`, has been fully inspected.

Shared strong behavior included:

```text
protected final-test values during development
valid train-only learned preprocessing in the treatment's own models
chronological future-facing validation reasoning
appropriate provisional use of account_state_code under the initial documentation
immediate removal after the authoritative Phase 2 timing notice
fresh legitimate development evidence after invalidation
model lock before final-test access
no post-test development
bounded non-causal claims
```

The clearest first-pair B1 advantages were:

```text
explicit diagnosis of the inherited learned-preprocessing contamination
explicit customer-month observation-unit statement
more explicit deployment/generalization-regime reasoning
known-versus-new customer subgroup analysis
```

Both conditions also shared an optional methodological weakness: row-level bootstrap intervals did not account for repeated-customer dependence.

These observations must not be retroactively inserted as privileged prompt knowledge during V0.

## Pending semantic review

The remaining raw trajectories requiring full inspection are:

```text
dev-b0-04
dev-b0-05
dev-b1-02
dev-b1-03
```

The six-run comparison should cover:

```text
row-unit correction
inherited preprocessing contamination diagnosis
validation/generalization-regime reasoning
prediction-time feature eligibility
Phase 2 repair completeness and precision
final-test discipline
claim scope and limitations
optional methodological errors
action/tool usage
input/output/reasoning-token distributions
run-to-run variability
```

## Common-interface decision

The common interface remains fixed. No further B0/B1 development replicate should be run unless the cross-run review discovers that one of the six trajectories is unusable for a condition-neutral reason.

Do not change the benchmark, prompts, command protocol, milestone schema, model, reasoning effort, or development artifacts based on observed baseline weaknesses.

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

P0 implementation remains blocked until the six-run baseline analysis is complete and the common held-out evaluator/resource protocol is frozen independently of P0.

## Relevant checkpoints

```text
docs/checkpoints/016_first_real_model_calibration_output_budget.md
docs/checkpoints/017_duplicate_structured_output_normalization.md
docs/checkpoints/018_first_behavior_evaluable_b0_run.md
docs/checkpoints/019_first_b0_semantic_trajectory_review.md
docs/checkpoints/020_first_behavior_evaluable_b1_run.md
docs/checkpoints/021_first_matched_b0_b1_semantic_comparison.md
docs/checkpoints/022_system_level_abstraction_and_reusable_reasoning_vision.md
docs/checkpoints/023_second_behavior_evaluable_b0_calibration_run.md
docs/checkpoints/024_second_behavior_evaluable_b1_calibration_run.md
docs/checkpoints/025_third_behavior_evaluable_b1_calibration_run.md
docs/checkpoints/026_baseline_development_calibration_complete.md
```

## Current priority

**Q-042 remains highest priority**, but it has advanced from execution to analysis: the required B0/B1 development trajectories now exist. The open task is to determine what the full six-run evidence implies and freeze a fair common held-out protocol.

## Next step

Collect and inspect the raw artifacts for the four not-yet-reviewed trajectories, then perform the full six-run cross-run comparison.

Only after that comparison should the semantic evaluator rules and held-out resource envelope be frozen. P0 implementation comes after that boundary is fixed.
