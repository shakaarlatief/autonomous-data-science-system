# Checkpoint 27: Full Six-Run Baseline Calibration Analysis

**Date:** 2026-08-09  
**Status:** Historical verification record  
**Checkpoint class:** EXPERIMENT_VERIFICATION  
**Project stage:** Prototype V0 development calibration  
**Scope:** Records the historical milestone described by this checkpoint: Full Six-Run Baseline Calibration Analysis.  
**Authority:** Historical provenance for the recorded experiment milestone; frozen experiment contracts and final experiment conclusions govern their declared scopes.  
**Design session:** 01  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 01 - Foundations & Checkpoint 0

## Purpose

Complete the development-calibration comparison of all three behavior-evaluable B0 trajectories and all three behavior-evaluable B1 trajectories before any P0 implementation or held-out protocol freezing.

This checkpoint integrates:

```text
dev-b0-03
dev-b0-04
dev-b0-05
dev-b1-01
dev-b1-02
dev-b1-03
```

The first matched pair was reviewed previously in Checkpoints 19 and 21. The remaining four raw trajectories were then inspected from their complete `trace.jsonl`, `summary.json`, `deterministic_evaluation.json`, `milestones.json`, and `conversation.json` artifacts.

The goal is calibration, not hypothesis confirmation. All six runs use the same development case and therefore are not held-out evidence of generalization.

---

## 1. Common configuration

All behavior-evaluable baseline trajectories used:

```text
model: gpt-5.6-terra
reasoning effort: high
max successful model calls: 20
max output tokens per call: 30,000
max additional generation retries: 2
request timeout: 300 seconds
strict Structured Outputs
previous_response_id continuation
all-turn reasoning context
same benchmark
same runtime
same command protocol
same deterministic evaluator
```

B1 differed from B0 only by receiving the four pre-specified methodological concepts statically in the prompt:

```text
Protected Final Evaluation
Learned Transformation Evaluation Boundary
Prediction-Time Feature Eligibility
Generalization-Regime Reasoning
```

B1 still had no typed project state, dynamic knowledge activation, prospective action gate, or dependency-aware reopening machinery.

---

## 2. Operational results

| Run | Condition | Calls | Input tokens | Output tokens | Reported reasoning tokens | Total tokens | Python actions | Ordinary project actions |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `dev-b0-03` | B0 | 15 | 96,525 | 6,715 | 1,203 | 103,240 | 4 | 12 |
| `dev-b0-04` | B0 | 18 | 138,912 | 8,570 | 1,805 | 147,482 | 7 | 15 |
| `dev-b0-05` | B0 | 19 | 171,225 | 11,046 | 2,724 | 182,271 | 8 | 16 |
| `dev-b1-01` | B1 | 15 | 109,884 | 7,722 | 2,060 | 117,606 | 5 | 12 |
| `dev-b1-02` | B1 | 16 | 104,893 | 7,790 | 1,895 | 112,683 | 5 | 13 |
| `dev-b1-03` | B1 | 17 | 133,519 | 9,495 | 2,167 | 143,014 | 6 | 14 |

Every run:

```text
completed successfully
was behavior-evaluable
had zero provider-generation failures
passed all current critical deterministic assertions
excluded account_state_code from the final locked model
re-evaluated development after Phase 2 feature invalidation
accessed protected-test values only after final model lock
performed no development after final-test feedback
```

The duplicate-equal structured-output normalization was exercised again in `dev-b0-05` and `dev-b1-02` and behaved as designed. No distinct-command ambiguity occurred.

---

## 3. Resource distribution

### B0

```text
mean calls: 17.33
call standard deviation: 2.08
call range: 15-19

mean total tokens: 144,331
total-token standard deviation: 39,610
total-token range: 103,240-182,271

mean input tokens: 135,554
mean output tokens: 8,777
mean reported reasoning tokens: 1,911
mean Python actions: 6.33
mean ordinary project actions: 14.33
```

### B1

```text
mean calls: 16.00
call standard deviation: 1.00
call range: 15-17

mean total tokens: 124,434
total-token standard deviation: 16,278
total-token range: 112,683-143,014

mean input tokens: 116,099
mean output tokens: 8,336
mean reported reasoning tokens: 2,041
mean Python actions: 5.33
mean ordinary project actions: 13.00
```

The first matched pair had B1 using more tokens than B0. Across all three runs, the descriptive mean reverses: B0 used about 19,897 more total tokens per run on average.

This is not evidence that static prompting is intrinsically cheaper. The small calibration sample shows that trajectory choice dominates simple prompt-length accounting. B0's later runs performed more optional analyses, used more Python actions, and accumulated longer threaded context.

Run-to-run token variability was also much larger for B0 in this development sample. This is descriptive only and should not be generalized from three runs.

The 20-call ceiling was sufficient for all six trajectories, but `dev-b0-05` used 19 calls. A held-out budget frozen at exactly 20 would therefore have little stochastic margin.

---

## 4. Execution reliability beyond provider generation

Provider generation was fully reliable after the Checkpoint 17 adapter repair, but model-authored Python was not error-free.

Observed execution failures included:

```text
dev-b0-04: one pandas indexing/crosstab error, followed by a corrected rerun
dev-b0-05: one 60-second Python timeout during an inefficient clustered bootstrap, followed by an efficient rerun
dev-b1-02: one pandas crosstab error after useful earlier output had already been produced
```

These are behavioral/tool-execution events rather than shared runtime defects. They did not compromise final evidence or critical integrity, but they contributed to action and token cost.

This is useful for later P0 evaluation: robust project operation includes recovering from failed analyses without losing methodological state or repeating unrelated work.

---

## 5. Protected final evaluation

This criterion produced a ceiling effect during baseline development calibration.

```text
B0: 3/3 strong pass
B1: 3/3 strong pass
```

All six treatments voluntarily protected final-test values during development, locked the model before test access, evaluated test once, and made no post-test model changes.

The static Protected Final Evaluation knowledge therefore showed no observable development-case advantage over the already strong B0 prompt.

This does not make a future P0 prospective gate useless. It means this development case did not produce comparative behavioral failures on this mechanism. P0 must not be credited merely for blocking an action that the simpler baselines would not have attempted.

---

## 6. Learned-transformation evaluation boundary

All six treatments used legitimate train-only or fold-local learned preprocessing in their own model evaluations.

The meaningful difference concerns whether the inherited baseline's defect became an explicit methodological conclusion.

The inherited code fits preprocessing on concatenated train and validation features before evaluating validation.

### B0

Across all three B0 runs:

```text
own evaluation pipelines were leakage-safe
inherited contaminated evidence was not relied upon
explicit durable diagnosis of the inherited preprocessing violation was absent
```

`dev-b0-03`, `dev-b0-04`, and `dev-b0-05` all inspected the inherited code and then independently built legitimate pipelines, but none clearly recorded the inherited validation estimate as invalid because learned preprocessing had used validation information.

### B1

B1 was more reliable, but not perfect:

```text
dev-b1-01: explicit diagnosis
dev-b1-02: no explicit diagnosis
dev-b1-03: explicit diagnosis
```

`dev-b1-03` stated in its Phase 1 report that the inherited baseline had a preprocessing-leakage flaw because it fit preprocessing on validation and would not be used.

The resulting calibration pattern is therefore:

```text
explicit inherited-boundary diagnosis
B0: 0/3
B1: 2/3
```

This is the clearest repeatable semantic difference observed between the baseline conditions.

It also provides an important motivation for the P0 knowledge-activation hypothesis: static knowledge being present in the prompt improved recall, but did not guarantee that the concern became an explicit project conclusion in every trajectory.

This should remain a hypothesis to test, not a conclusion about P0 before P0 exists.

---

## 7. Row-unit contradiction

Every run discovered enough structural evidence to operate as if the table consisted of repeated customer-month snapshots:

```text
rows greatly exceed unique customers
customer IDs repeat across months
(customer_id, snapshot_month) is unique
chronology and tenure are coherent
validation contains continuing and newly observed customers
```

All six therefore avoided the dangerous operational interpretation of one independent row per unique customer.

However, explicit durable correction of the stale README statement remained inconsistent.

The strongest explicit statement remained `dev-b1-01`:

```text
Rows are unique monthly customer snapshots.
```

Other runs often used phrases such as `customer-month rows`, `longitudinal snapshots`, or future monthly snapshots, but did not consistently record the direct semantic correction that the README's one-row-per-customer statement is stale.

The six-run evidence therefore weakens the idea that static prompting alone reliably makes important semantic contradictions durable. It also shows that the current milestone schema permits correct operational behavior without forcing explicit state capture.

This is relevant to H1 but cannot be resolved until P0's typed state exists.

---

## 8. Validation and generalization-regime reasoning

All six runs chose defensible future-facing temporal validation rather than random row splitting or a mechanical GroupKFold response to repeated customer IDs.

This is a strong result for both baselines.

B1 was somewhat more consistent in making the deployment mixture explicit. Across B1 trajectories, the model repeatedly recognized that future scoring includes both continuing customers and customers first observed later. B1 runs also more often quantified known/new composition or subgroup performance.

B0 also reasoned well:

```text
dev-b0-03: correctly interpreted repeated customers as later-snapshot scoring and noted weaker evidence for new customers
dev-b0-04: inspected overlap and recurrence, then used forward internal and provided validation windows
dev-b0-05: explicitly quantified returning-versus-new validation performance
```

A second process distinction appeared in how the supplied validation period was used.

```text
B0-03: supplied validation participated in candidate comparison
B0-04: supplied validation participated in candidate comparison
B0-05: supplied validation participated in candidate comparison

B1-01: used temporal development selection before a cleaner final development holdout check
B1-02: supplied validation participated directly in candidate comparison
B1-03: used expanding-window temporal CV inside train and reserved supplied validation for one final development check
```

Thus B1 produced the cleaner selection-versus-development-holdout separation in 2 of 3 runs, but not reliably in all three.

This is suggestive rather than conclusive. The static Generalization-Regime knowledge appears capable of changing process structure, but ordinary stochastic trajectory variation remains substantial.

---

## 9. Prediction-time feature eligibility before Phase 2

All six runs provisionally retained `account_state_code` while the strongest visible documentation said it was available during monthly scoring.

This is correct. The benchmark was designed so that a strong treatment should not declare leakage merely because an opaque feature is predictive.

The B0 trajectories were, if anything, sometimes more explicit about residual uncertainty:

```text
dev-b0-03: production timing should be verified
dev-b0-04: availability was supported by documentation but not independently auditable
```

B1 did not show a consistent pre-notice advantage from having the Prediction-Time Feature Eligibility principle statically in its prompt.

Importantly, B1 also did not overreact by prematurely deleting the field. Static methodological knowledge therefore did not distort the evidence hierarchy in this case.

---

## 10. Phase 2 repair

This mechanism also produced near-ceiling baseline behavior.

```text
B0: 3/3 strong repair
B1: 3/3 strong repair
```

Every run responded to the authoritative timing notice by:

```text
recognizing account_state_code as unavailable at the represented prediction time
removing it from the deployable feature set
re-establishing development evidence without it before lock
retaining unrelated valid project semantics
locking only after legitimate evidence existed
```

Some trajectories used one revised-development action while others used two or three, but all achieved the required material repair.

Therefore P0's dependency machinery will face a strong falsification bar. On this benchmark scale, richer dependency state is not justified merely by the fact that it can reproduce a repair that B0/B1 already perform reliably.

P0 must demonstrate more reliable explicit reopening, precision, traceability, reduced human/system memory burden, or lower failure risk under changed state.

---

## 11. Final models, final evidence, and claims

All six runs converged to nearly equivalent regularized logistic models using the same legitimate six-feature set:

```text
tenure_months
plan_tier
monthly_charge
support_tickets_90d
late_payments_90d
usage_change_30d
```

Regularization differed slightly between trajectories, usually `C=1` or `C=0.1`, without material final-test impact.

Protected-test AUROC was effectively identical across the runs at approximately 0.660.

All six final reports were appropriately bounded. They avoided causal claims, avoided unsupported intervention thresholds, acknowledged temporal variation, and kept claims tied to the reduced legitimate feature set.

No meaningful B0/B1 predictive-performance difference exists on this deterministic benchmark instance. The experimental contrast is process quality, reliability, explicitness, repair semantics, and resource use rather than final AUROC.

---

## 12. Optional uncertainty analysis

The repeated-customer bootstrap weakness from the first pair did not remain universal.

Observed approaches were:

```text
dev-b0-03: row-level bootstrap; ignores repeated-customer dependence
dev-b0-04: row-level bootstrap; ignores repeated-customer dependence
dev-b0-05: customer-cluster bootstrap; respects customer clustering
dev-b1-01: row-level stratified bootstrap; ignores repeated-customer dependence
dev-b1-02: row-level bootstrap; ignores repeated-customer dependence
dev-b1-03: row-level bootstrap; ignores repeated-customer dependence
```

Only one of six runs independently selected a cluster-aware resampling unit, and that run was B0.

This is an important calibration lesson. Neither strong generic reasoning nor the four static B1 concepts provide comprehensive methodological coverage. The system-level knowledge architecture should eventually be able to represent such concerns, but this issue must not be inserted retroactively as privileged V0 treatment knowledge after observing the benchmark.

It remains secondary calibration evidence, not a new V0 requirement.

---

## 13. Action selection and unnecessary work

Later B0 runs performed materially more optional work than the first run.

`dev-b0-05`, for example, explored:

```text
multiple candidate model families
calibration
customer-cluster uncertainty
returning/new-customer performance
coefficient interpretation
recent-window training alternatives
revised model-family comparison after Phase 2
revised training-window comparison
```

Most analyses were defensible, but the trajectory reached 19 calls and 182,271 tokens. One clustered-bootstrap attempt timed out and had to be rerun efficiently.

B1 trajectories were somewhat more compact on average in this small sample while still providing strong methodology. This is relevant to H5: explicit process knowledge may reduce some exploratory wandering, but three development runs are far too few to establish a stable efficiency effect.

The eventual P0 should be judged not by minimizing actions but by reducing unjustified or orphaned work while still completing required investigation and repair.

---

## 14. What static prompting demonstrably bought in calibration

The six-run result is more nuanced than the first pair.

Static B1 knowledge did **not** produce a universal improvement across every criterion.

It did provide the clearest repeatable gain in exactly one targeted area:

```text
explicit inherited preprocessing-boundary diagnosis:
B0 0/3 versus B1 2/3
```

It also coincided with more consistently explicit deployment-regime reasoning and two trajectories with cleaner model-selection-versus-development-holdout separation.

But B1 did not improve:

```text
critical final-test discipline, already 3/3 in B0
Phase 2 repair, already 3/3 in B0
final predictive performance
pre-notice feature-timing caution
optional repeated-customer uncertainty analysis
```

And B1 itself failed to explicitly apply the learned-transformation concept in one of three runs despite having that concept in the prompt.

This is precisely the distinction the richer architecture is intended to test:

> Possessing relevant knowledge is not the same thing as reliably activating, instantiating, maintaining, and propagating it through project state.

Calibration now provides a concrete empirical reason to test that distinction rather than assuming it.

---

## 15. Implications for the Prototype V0 hypotheses

### H1: typed state improves semantic distinctions

Still open. Baseline runs often reason correctly while leaving important semantics implicit. This creates a meaningful target for P0 typed state, especially observation-unit facts, assumptions, evidence, and claims.

### H2: state-triggered reusable knowledge improves timely/reliable concern surfacing

Now has a useful baseline comparator. B1's static knowledge improved explicit preprocessing-boundary diagnosis from 0/3 to 2/3, but did not make activation perfect. P0 can therefore be tested on whether structured activation turns supplied knowledge into more reliable project obligations/conclusions rather than merely keeping it present in context.

### H3: prospective safeguards prevent invalid actions

The development case shows a ceiling effect: B0 and B1 voluntarily protected final test in all six runs. P0 should receive no credit for this mechanism on a trajectory where no baseline would have attempted the invalid action. Held-out results must determine whether the safeguard has comparative value.

### H4: dependency-aware correction improves repair

The development case also shows a strong baseline ceiling: all six repaired the Phase 2 feature invalidation correctly. P0 therefore faces a serious falsification test. Its richer dependency machinery must add reliability, explicitness, traceability, or precision beyond an already strong conversational repair process.

### H5: state-driven action selection reduces premature/unnecessary work

Still open. Resource and action variability is substantial. B0 averaged more calls/actions/tokens in this small calibration sample, but the evidence is too sparse to attribute this to condition rather than stochastic trajectory choice.

---

## 16. Common-interface conclusion

No remaining shared provider/runtime defect was discovered.

The common interface supported all six trajectories. Model-authored Python occasionally failed or timed out, but these were ordinary execution/recovery events rather than harness defects.

The interface should not be changed in response to semantic weaknesses observed during baseline calibration unless the next protocol-freeze step identifies a condition-neutral requirement needed for all held-out conditions.

---

## 17. Calibration conclusion

Q-042 has now moved beyond baseline execution and semantic comparison.

The major development-calibration findings are:

```text
B0 is a genuinely strong baseline, not a strawman.
B1 static knowledge improves some targeted explicit reasoning but not perfectly.
Both baselines are already near ceiling on protected-test discipline and Phase 2 repair.
Important semantics can remain implicit even when behavior is operationally correct.
Static knowledge presence does not guarantee activation.
Neither prompt condition provides complete methodological coverage.
Resource demand varies materially across stochastic trajectories.
The 20-call ceiling has insufficient margin for a confidently frozen held-out envelope.
No new common runtime defect requires repair.
```

This is sufficient to end baseline development calibration.

---

## 18. Next boundary

Do **not** run additional development B0/B1 replicates and do **not** implement P0 yet.

The next step is to freeze the held-out experimental protocol independently of P0, including:

```text
semantic-evaluation rubric and judge procedure
critical-versus-noncritical scoring rules
held-out resource envelope
how tool-execution failures are counted
which efficiency measures are primary versus diagnostic
continuation/falsification criteria
held-out run counts and ordering
```

Only after that protocol is recorded should P0 implementation begin.
