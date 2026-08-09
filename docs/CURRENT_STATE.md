# Current State

## Checkpoint

**Checkpoint:** 20  
**Date:** 2026-08-09  
**Development stage:** Real-model baseline calibration and B0/B1 semantic trajectory comparison  
**Implementation status:** The first behavior-evaluable B0 and B1 trajectories have both completed under the same common configuration. B0 has been fully reviewed semantically; B1 has passed the operational and deterministic viability boundary and now requires full raw-trajectory review before more calibration runs or P0 implementation.

## Primary purpose

> **The system should create the best data-science process for the particular project, where what "best" means depends on the project's goals, constraints, required outputs, and desired level of human involvement.**

## Prototype V0 experimental question

Prototype V0 asks whether operationalized semantic machinery materially improves reliability beyond a strong reasoner and excellent prompting.

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

## Benchmark and common harness

The first synthetic benchmark is a 24-month customer-month churn project with:

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

The runtime provides phase-aware artifact visibility, metadata/value access, declared-input Python execution, condition-neutral tracing, Phase 1 / Phase 2 / final-evaluation transitions, milestone reports, and optional prospective final-test enforcement.

The deterministic evaluator checks benchmark validity, premature test access, post-test development, final feature legitimacy, and Phase 2 re-evaluation after material feature invalidation.

## Current development-calibration configuration

The common provisional configuration remains:

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

These are development-calibration settings, not frozen held-out budgets.

## Calibration history

### `dev-b0-01`

Infrastructure diagnostic only.

```text
10,000-token ceiling
provider status: incomplete
reason: max_output_tokens
successful model commands: 0
behavior_evaluable: false
```

Checkpoint 16 raised the calibration ceiling to 30,000, preserved failed-response usage/provider metadata, and separated infrastructure aborts from behavioral scores.

### `dev-b0-02`

Infrastructure diagnostic only.

The provider completed but returned two identical structured message outputs. The SDK aggregate concatenated them, which the old adapter could not parse as one JSON document.

```text
input tokens: 1,107
output tokens: 130
reasoning tokens: 41
total tokens: 1,237
successful model commands admitted by old adapter: 0
behavior_evaluable: false
```

Checkpoint 17 added conservative duplicate-equal structured-output normalization while rejecting distinct multiple commands as ambiguous.

### `dev-b0-03`

First genuine behavior-evaluable B0 trajectory.

```text
completed: true
successful model calls: 15
generation attempts: 15
generation failures: 0
input tokens: 96,525
output tokens: 6,715
reported reasoning tokens: 1,203
total observed tokens: 103,240
behavior_evaluable: true
all deterministic assertions passed: true
```

Checkpoint 18 recorded the operational result. Checkpoint 19 records the full semantic review.

### `dev-b1-01`

First genuine behavior-evaluable B1 trajectory.

```text
completed: true
successful model calls: 15
generation attempts: 15
generation failures: 0
total observed tokens: 117,606
behavior_evaluable: true
all critical deterministic assertions passed: true
```

Checkpoint 20 records this operational result. Full semantic review is still pending.

## First matched operational B0/B1 pair

| Measure | B0 `dev-b0-03` | B1 `dev-b1-01` |
|---|---:|---:|
| Completed | Yes | Yes |
| Successful model calls | 15 | 15 |
| Generation attempts | 15 | 15 |
| Generation failures | 0 | 0 |
| Behavior evaluable | Yes | Yes |
| Critical deterministic assertions passed | Yes | Yes |
| Total observed tokens | 103,240 | 117,606 |

B1 used 14,366 more observed tokens in this first matched pair, approximately 13.9 percent more than B0. This is descriptive only until the raw B1 trace is decomposed. It may reflect static-prompt overhead, more substantive reasoning, longer interactions, redundancy, or ordinary run variation.

The first pair has identical successful-call counts and no generation failures in either condition. The current 20-call and 30,000-token per-call ceilings are therefore operationally viable for at least one full run of each baseline condition.

## First B0 semantic review

The complete `dev-b0-03` trajectory was reconstructed from all five raw run artifacts.

### Strong B0 behavior

B0 performed strongly on the central integrity mechanics:

```text
no premature final-test values
no development after final-test feedback
train-only preprocessing during validation
chronological future-facing validation
no mechanical GroupKFold reaction to repeated IDs
appropriate provisional use of account_state_code under initial documentation
explicit unresolved concern about account_state_code production timing
immediate removal after authoritative Phase 2 notice
fresh development comparison without the invalid feature
explicit retirement of the earlier feature-dependent validation result
final model lock before test access
one final protected-test evaluation
bounded claims and no causal overclaim
no invented decision threshold when costs/capacity were absent
```

The final locked feature set excluded `account_state_code` and the final test AUROC was approximately 0.6600.

### B0 semantic weaknesses

1. **Row-unit correction remained implicit.** B0 empirically established repeated customer-month structure, unique customer-month pairs, and exact tenure/month progression, then reasoned in later-snapshot terms. It never cleanly recorded the durable semantic conclusion that the observation unit is a customer-month snapshot and the README's one-row-per-customer statement is stale.

2. **Inherited preprocessing contamination was avoided but not explicitly diagnosed.** B0 read the baseline code, never relied on its contaminated validation evidence, and built train-only pipelines. It did not explicitly state that fitting learned preprocessing on train+validation invalidates the inherited validation comparison.

3. **Optional iid bootstrap uncertainty was too strong for repeated entities.** B0 added row-wise bootstrap AUROC intervals/contrasts despite repeated customer observations. Point metrics and model lock remain valid, but nominal interval interpretation should account for within-customer dependence.

These weaknesses are especially informative for the B1 comparison because row-unit/generalization reasoning and learned-transformation boundaries are already among the four pre-specified static methodological concepts. They must not be converted into newly invented post-hoc requirements.

## B1 semantic questions now pending

The full `dev-b1-01` review should determine whether static knowledge materially changes behavior relative to B0, especially:

```text
Does B1 make the customer-month observation unit explicit?
Does it explicitly diagnose the inherited train+validation preprocessing contamination?
Does it reason more explicitly about the intended temporal/entity generalization regime?
Does it treat account_state_code appropriately before Phase 2 rather than rejecting it only because of generic leakage suspicion?
Does it repair Phase 2 evidence as precisely as B0?
Does it preserve strict final-test discipline?
Does it improve or worsen optional uncertainty analysis?
Does the additional token usage buy methodological value or mainly add overhead?
```

The raw trajectory must be inspected before any answer is recorded.

## Resource behavior

B0's first completed trajectory consumed:

```text
96,525 input tokens
6,715 output tokens
1,203 reported reasoning tokens within output usage
103,240 total observed tokens
15 successful calls
```

About 93.5 percent of B0's observed tokens were input tokens, with per-turn input growing from 1,107 on turn 1 to 14,693 on the final turn as threaded project context accumulated.

B1 consumed 117,606 total observed tokens in the first matched run. Its input/output/reasoning decomposition and per-turn growth are not yet known from the terminal summary and must be recovered from the raw artifacts.

The one-command-per-turn protocol has material serial/context cost, but the completed B0 review found no blocking interface defect. No common-interface change should be made before B1's trajectory is inspected.

## Common-interface decision

No condition-neutral provider/runtime repair is currently indicated.

A minor reporting-specification mismatch remains: Foundation 011 describes observation-unit interpretation as a Phase 1 report element, while the implemented milestone schema has no dedicated observation-unit field. The trajectory provides enough evidence for semantic judging. Adding a field after observing B0's omission would risk tuning the interface to an observed baseline weakness and require parity reruns.

The interface therefore remains unchanged for the B1 comparison.

## Automated validation

The latest code-affecting calibration repair remains CI-validated with:

```text
25 passed in 8.30s
```

No code has been changed during Checkpoints 18-20 empirical review.

Historical implementation/calibration checkpoints now include:

```text
docs/checkpoints/012_benchmark_generator_and_self_validation.md
docs/checkpoints/013_instrumented_workspace_and_deterministic_evaluator.md
docs/checkpoints/014_provider_neutral_baseline_runners.md
docs/checkpoints/015_real_model_calibration_infrastructure.md
docs/checkpoints/016_first_real_model_calibration_output_budget.md
docs/checkpoints/017_duplicate_structured_output_normalization.md
docs/checkpoints/018_first_behavior_evaluable_b0_run.md
docs/checkpoints/019_first_b0_semantic_trajectory_review.md
docs/checkpoints/020_first_behavior_evaluable_b1_run.md
```

## P0 remains intentionally unimplemented

The experiment still requires sufficiently understood B0/B1 calibration before P0 is built.

The planned minimal P0 state remains:

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

## Current priority

**Q-042 remains highest priority.**

The project now has one complete behavior-evaluable trajectory from each baseline condition under matched configuration. The immediate uncertainty is semantic: what did the static knowledge change, if anything, and was the additional resource use useful?

Foundation 011 still calls for multiple development-calibration trajectories per condition before semantic-evaluation rules and held-out budgets are frozen.

## Next step

Inspect the complete raw `dev-b1-01` trajectory and compare it directly with the already reviewed `dev-b0-03` trajectory.

Required B1 artifacts:

```text
trace.jsonl
summary.json
deterministic_evaluation.json
milestones.json
conversation.json
```

Do not run additional B0/B1 replicates and do not implement P0 until this first matched semantic comparison is complete.
