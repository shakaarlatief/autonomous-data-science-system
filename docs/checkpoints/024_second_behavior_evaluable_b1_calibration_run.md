# Checkpoint 24: Second Behavior-Evaluable B1 Calibration Run

**Date:** 2026-08-09  
**Status:** Historical experiment record  
**Checkpoint class:** EXPERIMENT_EXECUTION  
**Project stage:** Prototype V0 development calibration  
**Scope:** Records the historical milestone described by this checkpoint: Second Behavior-Evaluable B1 Calibration Run.  
**Authority:** Historical provenance for the recorded experiment milestone; frozen experiment contracts and final experiment conclusions govern their declared scopes.  
**Design session:** 01  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 01 - Foundations & Checkpoint 0

## Purpose

Record the operational result of the second behavior-evaluable B1 development-calibration trajectory, `dev-b1-02`, under the unchanged common baseline configuration.

This checkpoint records terminal-level operational evidence only. The remaining baseline replicates should be completed before full cross-run semantic and resource comparison, unless a genuine shared infrastructure defect appears.

## Run

```text
run_id: dev-b1-02
condition: B1
model: gpt-5.6-terra
reasoning effort: high
max successful model calls: 20
max generation retries: 2
max output tokens per call: 30,000
```

The benchmark, B1 prompt, model, common command protocol, runtime, evaluator, and resource settings were unchanged from `dev-b1-01`.

## Observed result

```text
Completed: True
Successful model calls: 16
Generation attempts: 16
Generation failures: 0
Total observed tokens: 112,683
Behavioral evaluation eligible: True
Critical deterministic assertions passed: True
```

The second B1 replicate therefore completed successfully and is eligible for later semantic interpretation.

## Operational comparison with the first B1 run

| Measure | `dev-b1-01` | `dev-b1-02` |
|---|---:|---:|
| Completed | Yes | Yes |
| Successful model calls | 15 | 16 |
| Generation failures | 0 | 0 |
| Critical deterministic assertions | Pass | Pass |
| Total observed tokens | 117,606 | 112,683 |

`dev-b1-02` used one additional successful model turn but 4,923 fewer observed tokens than `dev-b1-01`, approximately 4.2 percent less total token usage.

This is another useful calibration observation: model-call count and total token usage do not move mechanically together. A trajectory may use more turns while consuming fewer total tokens because per-turn input/output length and accumulated context differ.

## Current within-condition variability

The two completed B1 runs are relatively close in total token usage compared with the first two B0 runs:

```text
B1:
dev-b1-01 -> 15 calls, 117,606 tokens
dev-b1-02 -> 16 calls, 112,683 tokens

B0:
dev-b0-03 -> 15 calls, 103,240 tokens
dev-b0-04 -> 18 calls, 147,482 tokens
```

It is too early to infer that B1 is intrinsically less variable. Three runs per condition were pre-specified precisely because one or two stochastic trajectories are insufficient to estimate stable behavior or resource demand.

## Integrity result

`dev-b1-02` again passed the current critical deterministic assertions and had no provider-generation failures.

At terminal-summary level there is therefore no evidence of a shared provider/runtime defect, budget exhaustion, protected-test failure, post-test development, invalid final feature use, or missing Phase 2 repair.

Semantic details remain pending, including whether the static knowledge was used explicitly, how the row unit and generalization regime were handled, how inherited preprocessing contamination was discussed, Phase 2 repair precision, optional methodological errors, and action efficiency.

## Experimental discipline

Do not change the prompts, benchmark, model, reasoning effort, call ceiling, output ceiling, or common runtime.

Current behavior-evaluable baseline counts are:

```text
B0: 2 / 3
B1: 2 / 3
```

Continue the pre-specified alternating sequence:

```text
next: dev-b1-03
then: dev-b0-05
```

After those two runs complete, the project will have three behavior-evaluable development trajectories per baseline condition. The next major step will then be cross-run semantic/resource comparison and freezing the held-out evaluator and resource protocol before P0 implementation.
