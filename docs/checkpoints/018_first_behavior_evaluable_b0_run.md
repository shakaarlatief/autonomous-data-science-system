# Checkpoint 18: First Behavior-Evaluable B0 Calibration Run

**Date:** 2026-08-09  
**Status:** Historical experiment record  
**Checkpoint class:** EXPERIMENT_EXECUTION  
**Project stage:** Prototype V0 development calibration  
**Scope:** Records the historical milestone described by this checkpoint: First Behavior-Evaluable B0 Calibration Run.  
**Authority:** Historical provenance for the recorded experiment milestone; frozen experiment contracts and final experiment conclusions govern their declared scopes.  
**Design session:** 01  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 01 - Foundations & Checkpoint 0

## Purpose

Record the first real B0 trajectory that completed under the corrected common calibration interface and is therefore eligible for behavioral interpretation.

This checkpoint records only the operational facts available from the completed run summary. Full semantic interpretation is intentionally deferred until the raw trajectory artifacts are inspected.

## Run

```text
run_id: dev-b0-03
condition: B0
model: gpt-5.6-terra
reasoning effort: high
max successful model calls: 20
max generation retries: 2
max output tokens per call: 30,000
```

## Observed result

The run completed successfully:

```text
Completed: True
Successful model calls: 15
Generation attempts: 15
Generation failures: 0
Total observed tokens: 103,240
Behavioral evaluation eligible: True
Critical deterministic assertions passed: True
```

This is the first provider-backed B0 run in Prototype V0 that reached project completion without an infrastructure abort.

The two earlier runs remain calibration diagnostics rather than B0 behavioral evidence:

```text
dev-b0-01 -> incomplete response caused by the original 10,000-token ceiling
dev-b0-02 -> duplicate-equal structured output blocks exposed an adapter normalization defect
dev-b0-03 -> completed and behavior-evaluable
```

## Immediate implications

### 1. The common command/runtime interface is now operationally viable for B0

A strong model was able to complete the benchmark through the common command protocol in 15 successful model calls with no provider-generation failures.

This does not prove that every command was semantically good or that the interface is fully frozen, but it clears the first operational-viability hurdle.

### 2. The current 20-call ceiling is not immediately too small

The first completed B0 trajectory used 15 of the 20 available successful model calls.

That leaves a five-call margin in this single development trajectory. One run is not enough to freeze the common call budget, but the result is evidence that 20 calls is at least feasible for a strong B0 trajectory.

### 3. The 30,000-token per-call ceiling did not prevent completion

No generation failed and the trajectory completed. This establishes practical viability of the corrected per-call ceiling for at least one full B0 development run.

The 103,240-token total is an important resource observation and must be analyzed more closely before freezing the experimental budget. The raw trace is needed to distinguish input, visible output, reasoning, repeated-context, and tool-driven growth across turns.

### 4. Deterministic critical integrity checks passed

The completed run passed the current critical deterministic assertions. This is meaningful process evidence, but it is deliberately not sufficient for judging the quality of the B0 trajectory.

The deterministic evaluator does not fully judge, among other things:

```text
quality of row-unit interpretation
quality of generalization-regime reasoning
whether inherited preprocessing contamination was recognized for the right reason
quality and timing of feature-eligibility reasoning
precision of Phase 2 repair
strength and scope of claims
unnecessary or weak analysis
```

Those require semantic trajectory review.

## What is not yet concluded

Do not yet conclude that B0 is methodologically strong, that B1 is unnecessary, that the 20-call / 30,000-token protocol is frozen, or that P0 should be implemented.

The raw B0 artifacts must be reviewed before B1 is run so that any remaining common-interface defect can still be repaired condition-neutrally before paired baseline comparison.

Required artifacts from `results/raw/dev-b0-03/` are:

```text
trace.jsonl
summary.json
deterministic_evaluation.json
milestones.json
conversation.json
```

The next review should reconstruct the full trajectory and assess:

```text
artifact inspection order and command reliability
premature final-test behavior
row-unit contradiction resolution
validation/generalization reasoning
inherited preprocessing leakage recognition and handling
Phase 1 use of account_state_code
response to the authoritative Phase 2 timing notice
repair completeness and precision
final model lock and final-test use
final claim scope and limitations
call/token/tool costs
whether any shared interface ambiguity remains
```

## Experimental discipline

B1 should not be run yet. The next valid action is semantic inspection of `dev-b0-03`.

If the completed B0 trajectory reveals a genuine shared interface defect, it may be repaired condition-neutrally before B1. If the interface is viable, then B1 should be run with the same common configuration before P0 implementation begins.
