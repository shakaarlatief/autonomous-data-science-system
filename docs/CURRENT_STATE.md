# Current State

## Checkpoint

**Checkpoint:** 19  
**Date:** 2026-08-09  
**Development stage:** Real-model baseline calibration and semantic trajectory comparison  
**Implementation status:** The first behavior-evaluable B0 trajectory has been fully reviewed. The common interface is viable as-is, B0 shows strong critical-integrity behavior with several semantic weaknesses, and the first B1 trajectory is now the required next experiment.

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

## First B0 semantic review

The complete `dev-b0-03` trajectory was reconstructed from:

```text
trace.jsonl
summary.json
deterministic_evaluation.json
milestones.json
conversation.json
```

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

The first B0 run was not semantically perfect.

1. **Row-unit correction remained implicit.** B0 empirically established repeated customer-month structure, unique customer-month pairs, and exact tenure/month progression, and then reasoned in later-snapshot terms. But it never cleanly recorded the durable semantic conclusion that the observation unit is a customer-month snapshot and the README's one-row-per-customer statement is stale.

2. **Inherited preprocessing contamination was avoided but not explicitly diagnosed.** B0 read the baseline code, never relied on its contaminated validation evidence, and built train-only pipelines. It did not explicitly state that fitting learned preprocessing on train+validation invalidates the inherited validation comparison.

3. **Optional iid bootstrap uncertainty was too strong for repeated entities.** B0 added row-wise bootstrap AUROC intervals/contrasts despite repeated observations from customers. Point metrics and the model lock remain valid, but nominal interval interpretation should account for within-customer dependence, for example through an estimand-appropriate clustered resampling design.

These weaknesses are useful calibration evidence. They show that a strong generic baseline can satisfy major integrity requirements while leaving important semantics implicit or introducing weaker inferential precision through optional analysis.

## Generalization-regime judgment

B0's use of the supplied chronological holdout is defensible for the intended deployment regime.

It explicitly recognized that train and validation share customers and interpreted this as later-snapshot scoring rather than automatically requiring pure unseen-entity validation. It also noted that evidence for entirely new customers is weaker.

It did not quantify known/new subgroup performance. That remains an optional depth opportunity rather than a blocking defect for this case.

## Phase 2 repair judgment

The repair was especially strong and precise:

```text
feature-timing fact changed
-> account_state_code removed
-> same candidate comparison re-run
-> old feature-dependent evidence retired
-> unrelated project semantics retained
-> final model locked only after new valid evidence existed
```

This gives B0 a serious baseline against which B1 and P0 must demonstrate additional value.

## Resource behavior

The first completed trajectory consumed:

```text
96,525 input tokens
6,715 output tokens
1,203 reported reasoning tokens within output usage
103,240 total observed tokens
15 successful calls
```

About 93.5% of observed tokens were input tokens. Per-turn input grew from 1,107 on the first turn to 14,693 on the final turn as the threaded project context accumulated.

The one-command-per-turn protocol therefore has material serial/context cost, but no blocking interface defect was observed. Changing the command model now after seeing B0 would materially alter the experiment and is not justified by this run.

## Common-interface decision

No further condition-neutral provider/runtime repair is required before B1.

A minor reporting-specification mismatch remains: Foundation 011 describes observation-unit interpretation as a Phase 1 report element, while the current milestone schema has no dedicated observation-unit field. The full trajectory still exposes enough evidence for semantic judging. Adding a field now merely to force an observed B0 omission would risk tuning the interface after seeing the baseline and would require rerunning B0 for parity.

Therefore the common interface should remain unchanged for the first B1 comparison.

## Automated validation

The latest code-affecting calibration repair remains CI-validated with:

```text
25 passed in 8.30s
```

No code was changed during the Checkpoint 18/19 empirical review.

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
```

## P0 remains intentionally unimplemented

The experiment still requires real B0/B1 calibration evidence before P0 is built.

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

B0 operational viability and one full B0 semantic trajectory are now known. The next uncertainty is whether the static four-component knowledge treatment B1 changes behavior meaningfully under the same common interface and budget.

The development protocol still calls for multiple calibration trajectories per condition before budgets and semantic-evaluation rules are frozen.

## Next step

Run the first B1 development-calibration trajectory with the exact same common configuration as `dev-b0-03`:

```text
condition: B1
model: gpt-5.6-terra
reasoning effort: high
max successful model calls: 20
max generation retries: 2
max output tokens per call: 30,000
```

Inspect that trajectory semantically before deciding the ordering of the remaining development-calibration replicates.

Do not implement P0 yet.
