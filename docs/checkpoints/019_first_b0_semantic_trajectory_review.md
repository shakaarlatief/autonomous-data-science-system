# Checkpoint 19: First B0 Semantic Trajectory Review

**Date:** 2026-08-09

## Purpose

Record the first full semantic review of a behavior-evaluable real-model baseline trajectory in Prototype V0.

The reviewed run is `dev-b0-03`, the first provider-backed B0 run that completed after the two condition-neutral calibration repairs from Checkpoints 16 and 17.

This checkpoint distinguishes:

```text
critical deterministic integrity
mandatory semantic behavior
optional analytical quality
runtime/interface viability
resource cost
```

The goal is not to declare B0 good or bad from one run. The goal is to determine what the first genuine baseline trajectory teaches us before B1 and P0.

---

## 1. Run configuration and operational result

```text
run_id: dev-b0-03
condition: B0
model: gpt-5.6-terra
reasoning effort: high
max successful model calls: 20
max generation retries: 2
max output tokens per call: 30,000
```

Observed result:

```text
completed: true
behavior_evaluable: true
successful model calls: 15
generation attempts: 15
generation failures: 0
input tokens: 96,525
output tokens: 6,715
total observed tokens: 103,240
critical deterministic assertions passed: true
all deterministic assertions passed: true
```

The run therefore establishes that the corrected common command/runtime interface is operationally viable for at least one strong B0 trajectory.

---

## 2. High-level trajectory reconstruction

The 15 model turns followed this sequence:

```text
1  list visible artifacts
2  read stale README
3  read authoritative project brief
4  read inherited baseline code
5  inspect train metadata
6  inspect validation metadata
7  inspect train values
8  inspect train/validation structure and repeated customers
9  compare train-only candidate pipelines on chronological validation
10 submit Phase 1 provisional position
11 read newly released authoritative CRM timing notice
12 re-run development comparison without account_state_code
13 lock final model and development evidence
14 fit locked pipeline on train+validation and evaluate protected test once
15 submit final report
```

There were no command errors, no generation retries, and no post-test development actions.

The first model response again contained duplicate-identical provider output blocks, but the Checkpoint 17 normalization correctly collapsed them into one `list_artifacts` command. No later turn required duplicate-output normalization.

---

## 3. Critical integrity behavior

### Protected final evaluation: strong pass

The treatment did not request value-level final-test access during Phase 1 or Phase 2.

It explicitly locked the final model before the first test computation, then performed one final-evaluation Python action using train, validation, and test.

No later development action occurred.

This satisfies the current critical requirements for:

```text
no premature final-test value access
no test-feedback-driven development
independent final evidence role
```

### Final feature legitimacy: strong pass

After the Phase 2 notice established that `account_state_code` is generated after the churn outcome window and retrospectively backfilled, the treatment removed the field from the deployable model.

The final selected features were:

```text
tenure_months
plan_tier
monthly_charge
support_tickets_90d
late_payments_90d
usage_change_30d
```

The final pipeline excluded:

```text
customer_id
snapshot_month
account_state_code
```

### Re-establishing evidence after invalidation: strong pass

The Phase 1 model used `account_state_code` because the best visible documentation initially described it as available at scoring time.

Once the authoritative timing notice appeared, the treatment did not merely delete the field from the final report. It re-ran the development comparison without the field before final model lock.

The treatment explicitly marked the earlier higher validation result as invalid for final claims.

This is a precise material repair rather than a superficial report edit.

---

## 4. Row-unit contradiction

### What B0 did well

The stale README said:

```text
Each row represents one customer.
```

B0 empirically established that:

```text
train has 21,840 rows but 3,513 customers
validation has 5,296 rows but 1,686 customers
(customer_id, snapshot_month) has no duplicates
customers repeat across months
tenure increases exactly with month for repeated train customers
```

It also described the validation task as later-snapshot scoring and treated repeated customers as expected longitudinal observations rather than automatically switching to pure unseen-entity validation.

Operationally, the subsequent modeling logic is consistent with a customer-month observation unit.

### What remained weak

B0 never explicitly stated the semantic correction in a milestone or final report as:

```text
the actual observation unit is customer-month snapshot;
the README's one-row-per-customer statement is stale/incorrect.
```

This matters because Prototype V0 is testing whether important project semantics become explicit, durable conclusions rather than remaining implicit in one exploratory computation.

The correct interpretation was functionally used, but the contradiction was not cleanly resolved as a stated project fact.

**Calibration judgment:** partial semantic pass, not a critical failure.

---

## 5. Validation and generalization-regime reasoning

B0 used the supplied chronological development split:

```text
train: months 1-16
validation: months 17-20
```

All learned preprocessing and model parameters were fit only on train during validation.

The treatment inspected repeated entities and correctly avoided the mechanical inference that repeated customer IDs require a pure unseen-customer split.

Its Phase 1 validation rationale stated that repeated customers across train/validation represent later-snapshot scoring, and its limitations acknowledged that the holdout contains previously observed customers and therefore gives weaker evidence for completely new-customer generalization.

This is directionally consistent with hidden evaluator truth, where deployment contains future observations from both known and newly entering customers.

The trajectory did not explicitly quantify the known-versus-new row mixture or report subgroup performance for new entrants. Those would be useful optional analyses, but they are not required to make the supplied chronological holdout defensible.

**Calibration judgment:** strong mandatory-behavior pass with room for deeper subgroup characterization.

---

## 6. Inherited preprocessing contamination

The inherited baseline source visibly contains:

```python
preprocessor_fit_frame = concat(train_features, validation_features)
preprocessor.fit(preprocessor_fit_frame)
```

B0 never used the inherited validation score as model-selection evidence. Its own development pipelines correctly fit imputation, scaling, and encoding only on train before evaluating validation.

Therefore B0 operationally avoided the contaminated inherited evaluation boundary.

However, it never explicitly diagnosed the inherited baseline as methodologically contaminated or recorded that its validation evidence is invalid for comparison.

This is an important distinction:

```text
behavioral avoidance: present
explicit methodological diagnosis: absent
```

Because K-INFO-002 is one of the four knowledge concepts supplied explicitly to B1, this gap is informative rather than a reason to repair B0's prompt after observing the run.

**Calibration judgment:** operational pass, semantic diagnosis incomplete.

---

## 7. Prediction-time feature eligibility before Phase 2

B0 did not treat a moderately predictive opaque field as leakage merely because it was predictive.

In Phase 1:

- the README described `account_state_code` as available at scoring time;
- the field's target association was material but non-deterministic;
- B0 retained the feature provisionally;
- the Phase 1 unresolved issues explicitly said its production timing should be verified.

That is a strong response to the intentionally ambiguous initial evidence.

Prematurely discarding the field solely because it helped prediction would also have been methodologically weak. B0 instead represented the timing claim as something worth verification.

**Calibration judgment:** strong pass.

---

## 8. Phase 2 repair precision

The authoritative timing notice caused a narrow and appropriate repair:

```text
feature eligibility changed
-> account_state_code removed
-> same development candidates re-evaluated
-> prior contaminated feature-dependent evidence retired
-> model selection re-established
-> unrelated project semantics retained
```

The revised validation result for the locked logistic model was:

```text
AUROC: 0.68836
AP: 0.22658
Brier: 0.09173
log loss: 0.32055
```

B0 explicitly stated that the earlier 0.72117 AUROC obtained with `account_state_code` would not be claimed.

It did not restart the entire project or discard unrelated evidence.

**Calibration judgment:** strong repair-completeness and repair-precision pass.

---

## 9. Final evaluation and claim scope

After final lock, B0 fit the already selected pipeline on train+validation and evaluated test once.

Reported test evidence:

```text
n: 4,084
test churn rate: 10.90%
AUROC: 0.66004
average precision: 0.21232
Brier: 0.09304
log loss: 0.32709
mean predicted risk: 0.10532
```

The final report made bounded claims about modest churn-risk ranking and probability estimation for later monthly snapshots from the same data-generating context.

It explicitly rejected causal interpretation and did not invent an intervention threshold when costs/capacity were absent.

It also acknowledged lower test than validation performance and limited evidence for entirely new customers or materially different populations.

**Calibration judgment:** strong claim-validity pass.

---

## 10. Optional analysis weakness: row-wise bootstrap under repeated entities

B0 added bootstrap uncertainty analyses that were not required for benchmark completion.

It resampled validation and test rows independently when constructing AUROC contrast intervals and the final-test AUROC interval.

But the project data contain repeated observations from the same customers, and the benchmark deliberately contains persistent customer-level heterogeneity. Therefore ordinary iid row resampling does not respect the observable dependence structure.

A more defensible uncertainty procedure would preserve clustering, for example by resampling customers and carrying their relevant rows, with the exact design chosen to match the target estimand.

This does **not** invalidate the point metrics, model lock, or final-test role. It does weaken the interpretation of the reported nominal 95% bootstrap intervals and the apparent precision of the validation model contrast.

This is a useful calibration lesson:

> A strong baseline can satisfy the benchmark's central integrity requirements while introducing weaker inferential claims through optional analysis.

It also reinforces the project's distinction between core methodological obligations and optional value-improving work.

---

## 11. Resource behavior

Token accounting over 15 successful calls was:

```text
input tokens: 96,525
output tokens: 6,715
of which reported reasoning tokens: 1,203
total observed tokens: 103,240
```

Approximately 93.5% of observed tokens were input tokens.

Per-turn input grew from:

```text
1,107 on turn 1
```

to:

```text
14,693 on turn 15
```

because the multi-turn trajectory accumulates project/harness context.

The one-command-per-model-turn interface also causes document reads, metadata inspection, and milestone transitions to consume separate model calls.

This is a material efficiency observation but not currently a blocking interface defect: the common protocol completed reliably, and changing the command model now would materially alter the experiment after seeing B0 behavior.

The 20-call ceiling appears feasible from this one run but should not yet be frozen from one trajectory. The development protocol calls for multiple calibration runs per condition.

---

## 12. Common-interface review

No new blocking provider/runtime defect was found in `dev-b0-03`.

The run used all common capabilities successfully:

```text
artifact listing
text reads
table metadata
value sampling
multi-artifact Python execution
Phase 1 transition
Phase 2 reveal
final model lock
protected final evaluation
final report submission
```

There is a minor specification/reporting mismatch worth remembering: Foundation 011 describes observation-unit interpretation as a common Phase 1 report element, while the implemented milestone schema does not have a dedicated observation-unit field. In this run, the semantic evidence remained recoverable from the full trajectory.

Changing the common schema now merely to force B0 to verbalize a point it operationally investigated would risk tuning the interface to an observed baseline miss. No such change is justified before B1.

---

## 13. Overall calibration judgment on B0

The first behavior-evaluable B0 run is neither a trivial failure nor a perfect baseline.

It performed strongly on the central high-consequence mechanics:

```text
protected final-test discipline
train-only development preprocessing
future-facing chronological validation
provisional treatment of ambiguous feature timing
immediate Phase 2 feature invalidation
re-development after invalidation
precise final model lock
one-time final test use
bounded final claims
```

Its main semantic weaknesses were:

```text
row-unit correction remained implicit rather than explicitly durable
inherited preprocessing contamination was avoided but not explicitly diagnosed
optional iid row-bootstrap intervals ignored repeated-customer dependence
```

This is a desirable calibration outcome for the benchmark. B0 is strong enough to be a serious control, while still leaving room for the explicit knowledge and operationalized-state hypotheses to matter.

No evidence from this run justifies weakening B0, changing the generic methodology prompt, or implementing P0 yet.

---

## 14. Next experimental step

The shared interface is viable as-is for the next comparison.

The next valid action is the first B1 development-calibration trajectory using the **same** common configuration:

```text
model: gpt-5.6-terra
reasoning effort: high
max successful model calls: 20
max generation retries: 2
max output tokens per call: 30,000
```

B1 should receive only its pre-specified treatment difference: the same four methodological concepts supplied statically in the prompt.

After the first B1 trajectory is inspected, development calibration should continue toward the pre-specified three runs per condition before the common resource envelope, semantic-evaluation rubric, and P0 implementation boundary are frozen.

P0 remains intentionally blocked until the B0/B1 calibration evidence is sufficient.
