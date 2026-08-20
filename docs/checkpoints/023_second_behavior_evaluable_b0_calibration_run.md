# Checkpoint 23: Second Behavior-Evaluable B0 Calibration Run

**Date:** 2026-08-09  
**Status:** Historical experiment record  
**Checkpoint class:** EXPERIMENT_EXECUTION  
**Project stage:** Prototype V0 development calibration  
**Scope:** Records the historical milestone described by this checkpoint: Second Behavior-Evaluable B0 Calibration Run.  
**Authority:** Historical provenance for the recorded experiment milestone; frozen experiment contracts and final experiment conclusions govern their declared scopes.  
**Design session:** 01  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 01 - Foundations & Checkpoint 0

## Purpose

Record the operational result of the second behavior-evaluable B0 development-calibration trajectory, `dev-b0-04`, under the unchanged common baseline configuration.

This checkpoint deliberately records only the terminal-level operational evidence. Full semantic comparison should be performed after the remaining baseline development replicates are available, unless a trajectory exposes a genuine shared infrastructure problem that requires earlier inspection.

## Run

```text
run_id: dev-b0-04
condition: B0
model: gpt-5.6-terra
reasoning effort: high
max successful model calls: 20
max generation retries: 2
max output tokens per call: 30,000
```

The common command protocol, benchmark, B0 prompt, runtime, and evaluator were unchanged from `dev-b0-03`.

## Observed result

```text
Completed: True
Successful model calls: 18
Generation attempts: 18
Generation failures: 0
Total observed tokens: 147,482
Behavioral evaluation eligible: True
Critical deterministic assertions passed: True
```

The second B0 replicate therefore completed successfully and is eligible for later semantic interpretation.

## Operational comparison with the first B0 run

| Measure | `dev-b0-03` | `dev-b0-04` |
|---|---:|---:|
| Completed | Yes | Yes |
| Successful model calls | 15 | 18 |
| Generation failures | 0 | 0 |
| Critical deterministic assertions | Pass | Pass |
| Total observed tokens | 103,240 | 147,482 |

`dev-b0-04` used three more successful model turns and 44,242 more observed tokens than `dev-b0-03`, approximately 42.9 percent more total token usage.

This is important calibration evidence because it demonstrates substantial run-to-run resource variation even within the same condition, model, benchmark, and fixed configuration.

## Budget implication

The 20-call development ceiling remained sufficient, but the margin narrowed from five unused calls in `dev-b0-03` to only two unused calls in `dev-b0-04`.

That does not justify changing the ceiling during the remaining baseline calibration. The development protocol is intentionally being held fixed so that run-to-run variability can be observed rather than tuned away after each trajectory.

However, the result increases the importance of using all three development replicates per condition before freezing the held-out resource envelope. A single completed run was clearly insufficient to characterize typical call or token demand.

The raw trajectory should later be decomposed to determine whether the additional effort reflects useful methodological depth, redundant analysis, stochastic variation in action selection, longer accumulated context, or another source.

## Integrity result

The second B0 run again passed the current critical deterministic assertions. At terminal-summary level, there is therefore no evidence of a new provider/runtime defect or critical-integrity failure.

This does not establish semantic equivalence with `dev-b0-03`; row-unit reasoning, inherited-baseline diagnosis, Phase 2 repair precision, optional uncertainty analysis, claim quality, and action efficiency still require trajectory-level review.

## Experimental discipline

Do not change the B0/B1 prompts, benchmark, model, reasoning effort, call ceiling, output ceiling, or common runtime in response to this run.

Continue the pre-specified alternating replicate order:

```text
dev-b1-02
dev-b1-03
dev-b0-05
```

P0 remains intentionally unimplemented until three behavior-evaluable development trajectories per baseline condition are available and the common held-out protocol can be frozen independently of P0.
