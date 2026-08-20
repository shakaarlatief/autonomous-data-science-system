# Checkpoint 35: First Real P0 Run Reaches Token Budget Before Completion

**Date:** 2026-08-09  
**Status:** Historical experiment record  
**Checkpoint class:** EXPERIMENT_EXECUTION  
**Project stage:** Prototype V0 development correction and behavioral freeze  
**Scope:** Records the historical milestone described by this checkpoint: First Real P0 Run Reaches Token Budget Before Completion.  
**Authority:** Historical provenance for the recorded experiment milestone; frozen experiment contracts and final experiment conclusions govern their declared scopes.  
**Design session:** 01  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 01 - Foundations & Checkpoint 0

## Purpose

Record the terminal-level outcome of the first genuine real-model P0 development-calibration trajectory before inspecting its complete raw trajectory.

Run:

```text
dev-p0-01
```

This is development calibration only. No held-out H1/H2 treatment run has occurred.

## Terminal result

```text
Condition: P0
Completed: False
Completed within budget: False
Budget exhausted: True
Successful model calls: 10
Generation attempts: 10
Generation failures: 0
Total observed tokens: 250,279
Python execution attempts: 2
Behavioral evaluation eligible: True
Critical deterministic assertions passed: False
```

The run crossed the registered 250,000 observed-token ceiling on its tenth successful model call. It therefore stopped under the common resource rule even though only 10 of 24 successful-call slots and 2 of 12 Python-attempt slots had been used.

## Immediate interpretation

This is not a provider-generation failure. All ten generations completed and there were zero generation failures. The trajectory is therefore behavior-evaluable.

The immediate empirical issue is resource efficiency / context growth: P0 consumed approximately 25,000 observed tokens per successful call on average before completion. That is materially above the development B0/B1 trajectories and exhausted the frozen token envelope long before the call ceiling.

The failed critical deterministic result must not yet be interpreted as an independent methodological failure. Because the run stopped before project completion, one or more milestone-dependent assertions may fail mechanically. The exact assertion IDs and trajectory cause must be read from the raw run artifacts before diagnosis.

## Investigation boundary

Do not run `dev-p0-02` yet.

The complete `dev-p0-01` artifacts must first be inspected, especially:

```text
summary.json
deterministic_evaluation.json
conversation.json
trace.jsonl
milestones.json
p0_state.json
p0_state_history.json
p0_knowledge_activations.json
```

The investigation should determine:

```text
where the run stopped in the project phase;
per-call token growth;
which state objects and active knowledge accumulated;
whether repeated full state views or other controller traffic created avoidable context growth;
whether the LLM was making useful project progress or being trapped by state/controller friction;
which critical deterministic assertions failed and why;
whether any fix is a genuine P0 implementation correction inside the preregistered scope or merely an attempt to improve a disappointing treatment result.
```

## Experimental integrity

Development debugging may repair a genuine P0 implementation defect because held-out execution has not begun. Any repair must stay inside the already registered P0 scope and must not change:

```text
B0/B1 prompts
four privileged knowledge components
held-out bundle identities
semantic rubric
held-out run ordering
common held-out resource envelope
continuation/falsification thresholds
```

The 250,000-token ceiling should not be raised merely because P0 exceeded it. The development investigation should first determine whether the implementation is unnecessarily serializing or repeating state/context that can be represented more efficiently without changing substantive treatment capability.
