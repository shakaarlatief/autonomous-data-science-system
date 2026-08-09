# Checkpoint 21: First Matched B0/B1 Semantic Comparison

**Date:** 2026-08-09

## Purpose

Record the first full semantic comparison between the behavior-evaluable B0 trajectory `dev-b0-03` and the behavior-evaluable B1 trajectory `dev-b1-01`.

This is development-calibration evidence only. It is not held-out evidence about P0 and it is not sufficient to estimate stable condition-level effects from one stochastic trajectory per condition.

## Matched configuration

Both runs used:

```text
model: gpt-5.6-terra
reasoning effort: high
max successful model calls: 20
max generation retries: 2
max output tokens per call: 30,000
same generated development case
same instrumented runtime
same command protocol
same deterministic evaluator
```

B1 differed only by receiving the four pre-specified methodological concepts statically in the system prompt:

```text
Protected Final Evaluation
Learned Transformation Evaluation Boundary
Prediction-Time Feature Eligibility
Generalization-Regime Reasoning
```

B1 still had no typed project state, dynamic activation, prospective action gate, or dependency-aware repair machinery.

## Operational comparison

| Measure | B0 `dev-b0-03` | B1 `dev-b1-01` |
|---|---:|---:|
| Completed | Yes | Yes |
| Successful model calls | 15 | 15 |
| Generation attempts | 15 | 15 |
| Generation failures | 0 | 0 |
| Deterministic assertions | All pass | All pass |
| Input tokens | 96,525 | 109,884 |
| Output tokens | 6,715 | 7,722 |
| Reported reasoning tokens | 1,203 | 2,060 |
| Total observed tokens | 103,240 | 117,606 |

B1 used 14,366 more observed tokens, approximately 13.9 percent more total usage.

Both runs used twelve ordinary project actions before/around milestone transitions:

```text
B0: 1 list + 4 text reads + 2 metadata reads + 1 table sample + 4 Python executions
B1: 1 list + 4 text reads + 2 metadata reads + 5 Python executions
```

The number of successful model turns was therefore identical. B1 shifted one action from direct table sampling into an additional Python analysis.

The first-call input difference was 241 tokens, reflecting the additional static methodological prompt. The larger trajectory-level difference cannot be attributed solely to that prompt because B1 also produced longer reasoning/output and retained a different interaction history.

## Semantic comparison

### 1. Protected final evaluation

Both B0 and B1 performed strongly.

Both conditions:

```text
kept test values untouched during development
explicitly locked the final model before final-test access
performed one final evaluation
made no development changes after test feedback
reported bounded final claims
```

The static Protected Final Evaluation concept did not create an observable advantage in this first pair because B0 already satisfied the requirement fully.

### 2. Learned transformation evaluation boundary

This is the clearest first-pair B1 improvement.

The inherited baseline contains:

```python
preprocessor_fit_frame = pd.concat([train[feature_columns], validation[feature_columns]])
preprocessor.fit(preprocessor_fit_frame)
```

B0 read this code and subsequently used train-only preprocessing in its own pipelines, but it never explicitly diagnosed the inherited validation estimate as contaminated by learned preprocessing fit on validation information.

B1 explicitly stated immediately after reading the inherited implementation:

```text
The inherited baseline leaks validation covariate information through preprocessing.
```

Its Phase 1 report also recorded:

```text
The inherited baseline improperly fit preprocessing on validation and will not be used.
```

This directly operationalized the supplied Learned Transformation Evaluation Boundary concept and converted an issue that B0 merely avoided into an explicit methodological conclusion.

### 3. Row-unit and generalization-regime reasoning

B1 was also more explicit than B0.

Both conditions discovered:

```text
many rows per underlying customer across time
unique (customer_id, snapshot_month) pairs
train months 1-16
validation months 17-20
substantial customer overlap across train and validation
```

B0 reasoned correctly in later-snapshot terms but left the observation-unit correction implicit.

B1's Phase 1 report explicitly stated:

```text
Rows are unique monthly customer snapshots.
```

It also quantified that 80.2 percent of validation customers occur in train and interpreted this as compatible with a future monthly scoring regime containing both continuing and new customers rather than mechanically requiring a pure unseen-customer split.

After Phase 2, B1 went further and quantified development performance separately for customers seen in train versus customers new to train:

```text
seen in train: AUROC approximately 0.693, n=4,587
new to train: AUROC approximately 0.656, n=709
```

This subgroup analysis was not mandatory, but it is a concrete value-add consistent with the supplied Generalization-Regime Reasoning component.

### 4. Prediction-time feature eligibility before Phase 2

No clear B1 advantage appeared before the authoritative notice.

Both conditions provisionally retained `account_state_code` because the visible README described it as available during monthly scoring and no stronger contradictory timing source was yet available.

This was correct for the benchmark. The feature should not be rejected merely because it is predictive or semantically opaque.

B0 actually expressed a more specific pre-notice uncertainty than B1 by noting that the upstream production timing of `account_state_code` should be verified before deployment.

B1 instead stated that the proposed predictors were documented as available at scoring time and left Phase 2 review as a general unresolved issue.

Therefore the static Prediction-Time Feature Eligibility concept did not produce an obvious first-pair benefit before the notice. Both treatments behaved acceptably.

### 5. Phase 2 repair

Both conditions performed very strongly.

After the authoritative notice established that `account_state_code` is generated after the outcome window and retrospectively backfilled, both runs:

```text
removed the feature immediately
re-established development evidence without it
retained unrelated project semantics
locked only after new valid evidence existed
excluded the invalid feature from the final model
```

B0 explicitly retired the old feature-dependent validation result.

B1 re-ran its expanding temporal model comparison without the feature and then performed a separate chronological development-holdout evaluation on months 17-20 before locking.

The latter creates a somewhat cleaner separation between model-family selection and final development evidence than B0's trajectory, which used the supplied validation partition during candidate comparison in both phases.

This difference is a quality improvement in the observed trajectory, but one paired development run is not sufficient to attribute it confidently to B1's static knowledge rather than model stochasticity.

### 6. Final model and final-test result

The final fitted models were nearly equivalent regularized logistic regressions with the same legitimate feature set.

```text
B0 selected logistic C=1
B1 selected logistic C=0.1
```

Final protected-test AUROC was effectively identical:

```text
B0: approximately 0.66004
B1: approximately 0.65995
```

The substantive value of B1 in this pair is therefore process explicitness and evidence structure, not predictive performance.

### 7. Claims and limitations

Both conditions made strong, appropriately bounded claims.

Both avoided:

```text
causal claims
unsupported intervention thresholds
post-test tuning
claims of universal generalization
```

B1 explicitly reported development-month variation and the weaker new-customer subgroup result. B0 instead emphasized limited evidence for entirely new customers without quantifying the subgroup.

Neither condition materially overclaimed the final test result.

## Shared weakness: optional uncertainty analysis

B1 did not fix the broader uncertainty-analysis weakness found in B0.

B0 used ordinary row-level bootstrap resampling for AUROC intervals/contrasts despite repeated customer observations.

B1 used outcome-stratified row-level bootstrap resampling for validation and test AUROC/AP intervals. Stratification preserves event prevalence but still treats customer-month rows as independent resampling units and therefore does not account for within-customer dependence.

This does not invalidate either condition's point metrics, model selection, protected-test discipline, or Phase 2 repair. It weakens the nominal interpretation of the reported bootstrap confidence intervals.

The shared weakness is useful calibration evidence: the four pre-specified knowledge components improve targeted concerns but do not constitute a complete methodology checklist.

It should not be retroactively added to B1 or P0 as a new privileged knowledge component for this V0 experiment.

## Resource interpretation

B1 consumed:

```text
109,884 input tokens
7,722 output tokens
2,060 reported reasoning tokens
117,606 total observed tokens
```

B0 consumed:

```text
96,525 input tokens
6,715 output tokens
1,203 reported reasoning tokens
103,240 total observed tokens
```

B1 therefore used:

```text
+13,359 input tokens
+1,007 output tokens
+857 reported reasoning tokens
+14,366 total tokens
```

B1's initial static prompt accounts for only part of this difference. The trajectory also contained more extensive forward-fold reasoning, an additional Python execution, known/new customer subgroup analysis, and a longer accumulated interaction history.

This first pair therefore suggests a real cost-quality trade-off rather than a pure prompt-overhead penalty.

The quality gains are concentrated in explicit treatment of the exact knowledge supplied to B1:

```text
clear diagnosis of learned-preprocessing leakage
explicit customer-month observation-unit statement
more explicit deployment-regime analysis
known/new customer validation subgroup analysis
```

However, B0 already matched B1 on the most important critical-integrity outcomes, especially protected-test discipline and Phase 2 feature invalidation/repair.

## Interface decision

The B1 trajectory reveals no new shared provider/runtime defect.

The common interface should remain unchanged.

Changing the reporting schema, command protocol, or budget now would risk adapting the experiment to observed development trajectories rather than testing the pre-specified treatment contrast.

## What the first pair supports

The first pair provides preliminary development evidence for the following narrow conclusions:

1. Both B0 and B1 are strong viable baselines under the common runtime.
2. Static methodological knowledge can improve explicit reasoning on concerns that the generic baseline may only handle implicitly.
3. B1's first-pair advantage is not in critical deterministic integrity or predictive accuracy; it is mainly in semantic explicitness, validation structure, and deployment-regime analysis.
4. Those gains came with approximately 13.9 percent more observed token usage in this pair.
5. Neither condition solved every methodological issue; both used resampling uncertainty that ignored repeated-customer dependence.
6. One matched pair is insufficient to determine whether these differences are stable treatment effects.

## Next experimental decision

Foundation 011 pre-specified three development-calibration runs per condition.

The common interface has now survived one behavior-evaluable run from each condition without generation failure, and no remaining shared defect has been identified.

The next step should therefore be to complete the remaining development-calibration replicates before P0 implementation or held-out budget freezing.

To reduce ordering bias, run the remaining replicates in alternating condition order rather than completing all of one condition first:

```text
dev-b0-04
dev-b1-02
dev-b1-03
dev-b0-05
```

All four should use the same common configuration as the first matched pair.

Do not change the knowledge prompts, benchmark, model, reasoning effort, call ceiling, per-call output ceiling, or runtime interface during these remaining development replicates unless a genuine condition-neutral infrastructure failure makes continuation impossible.

After all three behavior-evaluable runs per condition exist, compare:

```text
critical deterministic outcomes
semantic criteria
repair precision
explicitness of knowledge-component use
optional methodological errors
action counts
token distributions
run-to-run variance
```

Only then should the common held-out budget/evaluator protocol be frozen and P0 implementation begin.
