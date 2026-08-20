# Checkpoint 25: Third Behavior-Evaluable B1 Calibration Run

**Date:** 2026-08-09  
**Status:** Historical experiment record  
**Checkpoint class:** EXPERIMENT_EXECUTION  
**Project stage:** Prototype V0 development calibration  
**Scope:** Records the historical milestone described by this checkpoint: Third Behavior-Evaluable B1 Calibration Run.  
**Authority:** Historical provenance for the recorded experiment milestone; frozen experiment contracts and final experiment conclusions govern their declared scopes.  
**Design session:** 01  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 01 - Foundations & Checkpoint 0

## Purpose

Record the operational result of the third and final pre-specified B1 development-calibration trajectory, `dev-b1-03`, under the unchanged common baseline configuration.

This checkpoint records terminal-level operational evidence only. Full semantic comparison across all baseline replicates is deferred until the final B0 replicate is complete.

## Run

```text
run_id: dev-b1-03
condition: B1
model: gpt-5.6-terra
reasoning effort: high
max successful model calls: 20
max generation retries: 2
max output tokens per call: 30,000
```

The benchmark, B1 prompt, command protocol, runtime, evaluator, model, and resource settings were unchanged from the earlier B1 development runs.

## Observed result

```text
Completed: True
Successful model calls: 17
Generation attempts: 17
Generation failures: 0
Total observed tokens: 143,014
Behavioral evaluation eligible: True
Critical deterministic assertions passed: True
```

The third B1 replicate therefore completed successfully and is eligible for later semantic interpretation.

## B1 development-calibration series

| Run | Calls | Generation failures | Total observed tokens | Critical deterministic assertions |
|---|---:|---:|---:|---|
| `dev-b1-01` | 15 | 0 | 117,606 | Pass |
| `dev-b1-02` | 16 | 0 | 112,683 | Pass |
| `dev-b1-03` | 17 | 0 | 143,014 | Pass |

Across the three B1 development runs:

```text
calls: 15, 16, 17
mean calls: 16.0

total observed tokens: 117,606; 112,683; 143,014
mean total observed tokens: approximately 124,434
range: 30,331 tokens
```

`dev-b1-03` used 30,331 more tokens than `dev-b1-02`, approximately 26.9 percent more, despite adding only one successful model turn. This reinforces the earlier finding that model-call count alone is not a sufficient proxy for total resource demand.

## Operational implications

B1 has now completed all three pre-specified development-calibration replicates without a provider-generation failure and with all current critical deterministic assertions passing.

The 20-call ceiling was sufficient in every B1 run, leaving margins of five, four, and three unused successful model calls respectively.

The third run also shows that B1 resource use is not as tightly clustered as the first two runs suggested. Any comparison of B0 versus B1 efficiency must therefore use the complete replicate sets rather than the first pair or first two runs.

## What is not yet concluded

Do not yet infer a stable B0/B1 difference in token cost, call count, semantic quality, or variance. The final B0 development replicate is still missing.

Do not change the prompt, benchmark, runtime, model, reasoning effort, call ceiling, retry allowance, or output-token ceiling.

Do not implement P0 yet.

## Next step

Run the third and final B0 development-calibration replicate:

```text
dev-b0-05
```

using the unchanged common configuration.

Once it completes, there will be three behavior-evaluable runs per baseline condition. The next phase is then a cross-run baseline analysis covering deterministic outcomes, semantic behavior, repair precision, resource distributions, action counts, and run-to-run variance. That analysis should inform the common held-out evaluator/resource protocol before P0 is implemented.
