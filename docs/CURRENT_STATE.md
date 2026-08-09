# Current State

## Checkpoint

**Checkpoint:** 21  
**Date:** 2026-08-09  
**Development stage:** Real-model baseline calibration and matched B0/B1 comparison  
**Implementation status:** One behavior-evaluable B0 trajectory and one matched B1 trajectory have now been fully inspected semantically. The common interface is viable as-is. Remaining development-calibration replicates should be completed before P0 implementation or held-out budget freezing.

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

## Common development-calibration configuration

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

These remain development-calibration settings, not frozen held-out budgets.

## Calibration history

### Infrastructure diagnostics

`dev-b0-01` exposed the original 10,000-token output ceiling and missing failed-response usage accounting. Checkpoint 16 corrected both condition-neutrally.

`dev-b0-02` exposed duplicate-equal structured message blocks whose SDK aggregate was not valid as one JSON document. Checkpoint 17 added conservative normalization while preserving ambiguity errors for distinct commands.

Neither diagnostic is behavior-evaluable.

### First behavior-evaluable B0

`dev-b0-03`:

```text
completed: true
successful model calls: 15
generation failures: 0
input tokens: 96,525
output tokens: 6,715
reported reasoning tokens: 1,203
total observed tokens: 103,240
all deterministic assertions passed: true
```

Checkpoint 19 records the semantic review.

### First behavior-evaluable B1

`dev-b1-01`:

```text
completed: true
successful model calls: 15
generation failures: 0
input tokens: 109,884
output tokens: 7,722
reported reasoning tokens: 2,060
total observed tokens: 117,606
all deterministic assertions passed: true
```

Checkpoint 21 records the matched semantic comparison.

## First matched B0/B1 comparison

| Measure | B0 `dev-b0-03` | B1 `dev-b1-01` |
|---|---:|---:|
| Completed | Yes | Yes |
| Successful model calls | 15 | 15 |
| Generation failures | 0 | 0 |
| Deterministic assertions | All pass | All pass |
| Input tokens | 96,525 | 109,884 |
| Output tokens | 6,715 | 7,722 |
| Reported reasoning tokens | 1,203 | 2,060 |
| Total observed tokens | 103,240 | 117,606 |

B1 used 14,366 more observed tokens, approximately 13.9 percent more than B0 in this first matched pair.

Both conditions used the same number of successful model turns and twelve ordinary project actions. B0 used one table sample and four Python executions; B1 used no table sample and five Python executions.

## Semantic findings from the first pair

### Strong behavior shared by B0 and B1

Both conditions:

```text
protected final-test values during development
used train-only learned preprocessing for valid evaluation
used a chronological future-facing validation interpretation
did not mechanically require unseen-entity splitting because IDs repeat
provisionally retained account_state_code while initial documentation supported availability
removed account_state_code immediately after the authoritative Phase 2 notice
re-established valid development evidence without the field
locked development choices before final-test access
performed one protected final evaluation
made no post-test development changes
made bounded non-causal claims
avoided inventing an intervention threshold without utility/capacity information
```

The final legitimate feature set was the same in both runs. Final protected-test AUROC was effectively identical at about 0.660.

### Clear B1 improvement: learned-transformation contamination

B0 read the inherited baseline and independently used valid train-only preprocessing, but never explicitly stated that the inherited validation estimate was contaminated because preprocessing was fit using train+validation.

B1 explicitly diagnosed this immediately:

```text
The inherited baseline leaks validation covariate information through preprocessing.
```

Its Phase 1 report also stated that the inherited baseline improperly fit preprocessing on validation and would not be used.

This is the clearest observed benefit from the static Learned Transformation Evaluation Boundary concept.

### B1 improvement: row unit and deployment regime

B0 operationally understood the repeated customer-month structure but left the durable observation-unit correction implicit.

B1 explicitly stated in its Phase 1 report:

```text
Rows are unique monthly customer snapshots.
```

B1 also quantified the 80.2 percent validation-customer overlap with train and correctly interpreted the deployment regime as future monthly scoring with both continuing and new customers.

After Phase 2 it additionally reported development performance for seen versus new customers:

```text
seen in train: AUROC approximately 0.693, n=4,587
new to train: AUROC approximately 0.656, n=709
```

This is a concrete value-add aligned with the supplied Generalization-Regime Reasoning concept.

### Prediction-time feature eligibility before Phase 2

No clear B1 advantage appeared before the timing notice.

Both conditions correctly retained `account_state_code` because the strongest visible timing evidence said it was available during monthly scoring.

B0 actually expressed a more specific provisional concern that its upstream production timing should be verified before deployment. B1 treated the documentation as sufficient provisional evidence and left Phase 2 review as a general unresolved issue.

Both behaviors remain acceptable for the benchmark.

### Phase 2 repair

Both repairs were strong and precise.

B0 explicitly retired the earlier feature-dependent validation result.

B1 re-ran expanding temporal model selection without the field and then separately evaluated the selected frozen pipeline on the chronological development holdout before locking. This creates somewhat cleaner observed separation between model-family selection and final development evidence than B0's trajectory, although one paired run cannot establish that this is a stable treatment effect.

## Shared methodological weakness

Both conditions introduced uncertainty intervals that did not account for repeated-customer dependence.

B0 used ordinary row-level bootstrap resampling.

B1 used outcome-stratified row-level bootstrap resampling. Stratification preserves event prevalence but still resamples customer-month rows as if they were independent units.

This weakness does not invalidate point metrics, model selection, final-test discipline, or Phase 2 repair. It weakens nominal bootstrap interval interpretation.

The issue is useful calibration evidence but must not be retroactively inserted as a new privileged B1/P0 knowledge component in V0.

## Resource interpretation

B1's additional static prompt adds direct context overhead, but the full +14,366-token difference cannot be attributed to prompt length alone.

B1 also:

```text
used more reported reasoning tokens
executed an additional Python development analysis
separated train-fold model selection from chronological validation assessment
quantified known-versus-new customer performance
produced a longer accumulated interaction history
```

The first pair therefore suggests a genuine cost-quality trade-off rather than pure prompt overhead.

B1's observed quality gains are concentrated in the concerns explicitly supplied to it, especially learned-preprocessing leakage and generalization-regime reasoning.

## Common-interface decision

No new provider/runtime defect was found in `dev-b1-01`.

Do not change the command protocol, milestone schema, model, reasoning effort, or budget based on this first pair.

The common interface should remain fixed during the remaining development-calibration replicates unless a genuine condition-neutral infrastructure failure makes continuation impossible.

## Automated validation

The latest code-affecting calibration repair remains CI-validated with:

```text
25 passed in 8.30s
```

No code was changed during Checkpoints 18-21 empirical review.

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
docs/checkpoints/021_first_matched_b0_b1_semantic_comparison.md
```

## P0 remains intentionally unimplemented

The experiment still requires the pre-specified baseline development calibration before P0 is built.

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

The first matched pair suggests that static knowledge improves some targeted semantic behaviors while B0 already performs strongly on the central critical-integrity mechanics. One pair is insufficient to estimate stable treatment differences or freeze the held-out protocol.

Foundation 011 pre-specified three development-calibration runs per condition.

## Next step

Complete the remaining four behavior-evaluable development-calibration trajectories with the common interface unchanged.

Use alternating order to reduce simple ordering bias:

```text
dev-b0-04
dev-b1-02
dev-b1-03
dev-b0-05
```

All four use the same model, reasoning effort, 20-call ceiling, two-retry allowance, and 30,000-token per-call ceiling.

After three behavior-evaluable runs per condition exist, compare run-to-run variance, semantic criteria, repair precision, critical outcomes, optional methodological errors, action counts, and token distributions. Then freeze the held-out evaluator/resource protocol and only then implement P0.
