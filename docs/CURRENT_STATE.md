# Current State

## Checkpoint

**Checkpoint:** 25  
**Date:** 2026-08-09  
**Development stage:** Real-model baseline calibration and run-to-run variability measurement  
**Implementation status:** All three pre-specified B1 development-calibration trajectories are behavior-evaluable and complete. Two of three B0 trajectories are complete. Every completed baseline trajectory passes the current critical deterministic assertions. One final B0 replicate remains before cross-run baseline analysis, held-out protocol freezing, and P0 implementation.

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

B0 and B1 remain important lower-level controls because they test how much of a specific methodological benefit can already be achieved by a strong reasoner and static prompting before richer system machinery is credited.

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

Do not change these settings during the remaining baseline development calibration unless a genuine condition-neutral infrastructure failure makes continuation impossible.

## Infrastructure diagnostics

`dev-b0-01` was not behavior-evaluable. It exposed the original 10,000-token output ceiling and missing incomplete-response usage accounting. Checkpoint 16 corrected both condition-neutrally.

`dev-b0-02` was not behavior-evaluable. It exposed duplicate-equal structured message blocks whose SDK aggregate was invalid as one JSON document. Checkpoint 17 added conservative duplicate-equal normalization while preserving ambiguity errors for distinct commands.

No later completed run has exposed another shared provider/runtime defect.

## Behavior-evaluable calibration runs

| Run | Condition | Calls | Generation failures | Total observed tokens | Critical deterministic assertions |
|---|---|---:|---:|---:|---|
| `dev-b0-03` | B0 | 15 | 0 | 103,240 | Pass |
| `dev-b0-04` | B0 | 18 | 0 | 147,482 | Pass |
| `dev-b1-01` | B1 | 15 | 0 | 117,606 | Pass |
| `dev-b1-02` | B1 | 16 | 0 | 112,683 | Pass |
| `dev-b1-03` | B1 | 17 | 0 | 143,014 | Pass |

Current replicate counts:

```text
B0: 2 / 3
B1: 3 / 3
```

### B0 observations so far

`dev-b0-03` was fully reviewed semantically. It showed strong final-test discipline, defensible temporal validation reasoning, precise Phase 2 feature invalidation/repair, and bounded claims. Its main weaknesses were:

```text
row-unit correction remained implicit rather than explicit
inherited train+validation preprocessing contamination was avoided but not explicitly diagnosed
row-level bootstrap uncertainty ignored repeated-customer dependence
```

`dev-b0-04` also completed and passed all critical deterministic assertions but used substantially more resources:

```text
15 -> 18 calls relative to dev-b0-03
103,240 -> 147,482 total observed tokens
approximately +42.9% token usage
```

Its full semantic interpretation remains pending until the complete replicate set is available.

### B1 observations so far

`dev-b1-01` was fully compared with `dev-b0-03`. The first pair suggested that static methodological knowledge improved explicit reasoning on the exact supplied concepts, especially:

```text
explicit diagnosis of inherited learned-preprocessing contamination
explicit customer-month observation-unit statement
more explicit deployment/generalization-regime reasoning
known-versus-new customer subgroup analysis
```

B0 already matched B1 on central critical-integrity outcomes such as protected-test discipline and Phase 2 repair. Final protected-test AUROC in the first pair was effectively identical at about 0.660.

All three B1 development runs are now complete:

```text
dev-b1-01: 15 calls, 117,606 tokens
dev-b1-02: 16 calls, 112,683 tokens
dev-b1-03: 17 calls, 143,014 tokens
```

B1 mean calls across development calibration: 16.0.  
B1 mean total observed tokens: approximately 124,434.  
B1 token range: 30,331.

The third B1 run shows that B1 resource demand also varies materially. Model-call count alone is not a sufficient proxy for total token cost.

## Shared methodological weakness identified during calibration

The first semantically reviewed B0/B1 pair both introduced bootstrap intervals that resampled customer-month rows without accounting for repeated-customer dependence.

This does not invalidate point metrics, model selection, final-test discipline, or Phase 2 repair, but weakens nominal interval interpretation.

This issue is calibration evidence and must not be retroactively inserted as privileged B1/P0 prompt knowledge in Prototype V0.

## Common-interface decision

The common interface remains fixed.

Do not change the command protocol, milestone schema, benchmark, prompts, model, reasoning effort, or resource ceilings during the final baseline replicate.

Observed baseline weaknesses must remain evaluative evidence rather than becoming post-hoc prompt additions.

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

The baseline calibration boundary must be completed and the common held-out evaluator/resource protocol frozen independently of P0 before P0 is implemented.

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
```

## Current priority

**Q-042 remains highest priority:** characterize B0/B1 behavior and resource variability well enough to freeze a fair common held-out protocol independently of P0.

## Next step

Run the third and final B0 development-calibration trajectory under the unchanged common configuration:

```text
dev-b0-05
```

After it completes, there will be three behavior-evaluable development runs per baseline condition. The next phase is then a full cross-run baseline analysis covering deterministic outcomes, semantic criteria, repair precision, optional methodological errors, action counts, token distributions, and run-to-run variance. Only after that analysis should the held-out evaluator/resource protocol be frozen and P0 implementation begin.
