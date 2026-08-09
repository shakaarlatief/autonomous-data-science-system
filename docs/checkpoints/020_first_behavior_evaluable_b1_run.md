# Checkpoint 20: First Behavior-Evaluable B1 Calibration Run

**Date:** 2026-08-09

## Purpose

Record the first real B1 trajectory that completed under the same common calibration interface and resource configuration as the first behavior-evaluable B0 trajectory.

This checkpoint records only the operational facts available from the terminal summary. Full semantic comparison against B0 is intentionally deferred until the complete raw B1 trajectory is inspected.

## Run

```text
run_id: dev-b1-01
condition: B1
model: gpt-5.6-terra
reasoning effort: high
max successful model calls: 20
max generation retries: 2
max output tokens per call: 30,000
```

B1 receives the same model, tools, runtime, artifact world, and generic data-science guidance as B0, plus the same four pre-specified methodological concepts supplied statically in prompt prose:

```text
Protected Final Evaluation
Learned Transformation Evaluation Boundary
Prediction-Time Feature Eligibility
Generalization-Regime Reasoning
```

It still receives no typed project state, dynamic knowledge activation, prospective action gate, or dependency-aware repair machinery.

## Observed result

The run completed successfully:

```text
Completed: True
Successful model calls: 15
Generation attempts: 15
Generation failures: 0
Total observed tokens: 117,606
Behavioral evaluation eligible: True
Critical deterministic assertions passed: True
```

This is the first provider-backed B1 trajectory eligible for methodological interpretation.

## First operational B0/B1 comparison

The first behavior-evaluable trajectories now provide a matched operational pair:

| Measure | B0 `dev-b0-03` | B1 `dev-b1-01` |
|---|---:|---:|
| Completed | Yes | Yes |
| Successful model calls | 15 | 15 |
| Generation attempts | 15 | 15 |
| Generation failures | 0 | 0 |
| Behavior evaluable | Yes | Yes |
| Critical deterministic assertions passed | Yes | Yes |
| Total observed tokens | 103,240 | 117,606 |

B1 therefore used 14,366 more observed tokens than B0 in this first matched pair, approximately 13.9 percent more total observed tokens.

This difference is descriptive calibration evidence only. The raw B1 artifacts must be inspected before attributing the additional tokens to useful methodological reasoning, static-knowledge prompt overhead, longer tool interactions, redundant work, or another source.

## Immediate implications

### 1. B1 is operationally viable under the common interface

Like B0, B1 completed in 15 successful model calls with no provider-generation failures. The 20-call ceiling and 30,000-token per-call ceiling were sufficient for this first B1 trajectory.

### 2. The first matched pair has identical call counts

The static knowledge treatment did not increase the number of successful model turns in this single pair. It did increase total observed token usage.

The semantic review must determine whether this extra token use corresponds to better explicit methodological reasoning, unnecessary verbosity, or ordinary stochastic variation.

### 3. Both conditions pass the current critical deterministic checks

The deterministic evaluator does not yet distinguish the two first runs on critical assertions. Any B1 advantage or disadvantage in this pair is therefore likely to appear in semantic quality, repair precision, explicitness, optional analysis quality, or efficiency rather than the current critical pass/fail layer.

### 4. No experimental conclusion should be drawn yet

One B0 and one B1 development trajectory are not sufficient to estimate condition-level behavior. Foundation 011 planned multiple development-calibration runs per condition before freezing the held-out protocol.

The immediate next step is semantic review of `dev-b1-01`, not another replicate and not P0 implementation.

## Required B1 semantic review

Inspect the complete raw trajectory from:

```text
results/raw/dev-b1-01/trace.jsonl
results/raw/dev-b1-01/summary.json
results/raw/dev-b1-01/deterministic_evaluation.json
results/raw/dev-b1-01/milestones.json
results/raw/dev-b1-01/conversation.json
```

The comparison should specifically test whether B1's static methodological concepts materially changed behavior relative to B0, including:

```text
explicit row-unit correction
validation/generalization-regime reasoning
explicit diagnosis of the inherited train+validation preprocessing contamination
prediction-time eligibility reasoning before Phase 2
reaction to the authoritative Phase 2 notice
repair completeness and precision
final-test discipline
claim scope and limitations
quality of optional uncertainty analysis
unnecessary/redundant analyses
call/token/tool efficiency
```

The B0 review found two especially informative semantic weaknesses to compare against without changing the evaluation contract:

```text
row-unit correction was operationally understood but remained implicit
inherited preprocessing contamination was avoided but not explicitly diagnosed
```

B1 should not be judged by a newly invented requirement merely because B0 exposed these weaknesses. They are already within the pre-specified semantic criteria and knowledge components.

## Experimental discipline

Do not implement P0 yet.

Do not interpret this first pair as generalization evidence. Both trajectories use the development calibration case.

Do not change the common interface or resource configuration based only on the operational B1 summary. Any remaining shared defect must be demonstrated from the trajectory itself and repaired condition-neutrally.

The next valid action is full semantic inspection of `dev-b1-01` and direct comparison with `dev-b0-03` before deciding the ordering and number of remaining development-calibration replicates.
