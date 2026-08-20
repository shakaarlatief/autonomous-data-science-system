# Checkpoint 41: Third Real P0 Run Budget Exhaustion Terminal Record

**Date:** 2026-08-09  
**Status:** Historical experiment record  
**Checkpoint class:** EXPERIMENT_EXECUTION  
**Project stage:** Prototype V0 development correction and behavioral freeze  
**Scope:** Records the historical milestone described by this checkpoint: Third Real P0 Run Budget Exhaustion Terminal Record.  
**Authority:** Historical provenance for the recorded experiment milestone; frozen experiment contracts and final experiment conclusions govern their declared scopes.  
**Design session:** 01  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 01 - Foundations & Checkpoint 0

## Purpose

Record the terminal outcome of the third real-model P0 development-calibration trajectory after the canonical-ID handoff, terminal budget-accounting, and second current-state compaction corrections were deterministically validated.

This checkpoint records terminal facts only. The raw `dev-p0-03` trajectory has not yet been inspected, so no semantic or implementation diagnosis is made here.

No held-out H1/H2 treatment run has occurred.

## Run

```text
run_id: dev-p0-03
bundle: generated/development
condition: P0
model: gpt-5.6-terra
reasoning effort: high
successful-call ceiling: 24
observed-token ceiling: 250,000
Python-attempt ceiling: 12
per-call output ceiling: 30,000
additional generation retries: 2
```

The treatment resource envelope was unchanged.

## Terminal result

```text
Condition: P0
Completed: False
Completed within budget: False
Budget exhausted: True
Successful model calls: 14
Generation attempts: 14
Generation failures: 0
Total observed tokens: 260,234
Python execution attempts: 4
Behavioral evaluation eligible: True
Critical deterministic assertions passed: False
```

Output was written locally to:

```text
results/raw/dev-p0-03
```

## Immediate facts

```text
all 14 provider generations completed successfully;
the run remained behavior-evaluable;
the local registered token rule stopped the run;
14/24 model-call slots were used;
4/12 Python-attempt slots were used;
the crossing call carried cumulative usage to 260,234;
the project did not complete within budget;
the current critical deterministic set did not fully pass.
```

The token overshoot above 250,000 is compatible with the frozen admission rule: a call may begin while cumulative observed usage is below the limit, and the completed call may move the total above it. No further call may then begin.

## Development-run comparison

| Measure | dev-p0-01 | dev-p0-02 | dev-p0-03 |
|---|---:|---:|---:|
| Completed | No | No | No |
| Budget exhausted | Yes | Yes | Yes |
| Successful model calls | 10 | 12 | 14 |
| Generation failures | 0 | 0 | 0 |
| Total observed tokens | 250,279 | 291,350 | 260,234 |
| Python attempts | 2 | 4 | 4 |
| Critical deterministic pass | No | Yes | No |

The terminal totals alone are insufficient to determine whether the second compaction improved the per-call token curve, why the critical deterministic result regressed from pass to fail, or what exact project stage was reached.

## Required raw diagnosis

Inspect the complete `dev-p0-03` artifacts before changing P0 or running another development/held-out trajectory:

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

Determine at least:

```text
exact project phase and milestones at termination;
which deterministic assertion(s) failed and why;
per-call input/output/total token curve;
cumulative token curve;
model-facing state-view sizes;
whether the canonical-ID handoff worked;
whether any controller/state-control errors occurred;
Phase 1 validation behavior;
Phase 2 timing response and dependency repair;
whether the final model was locked;
whether protected final evaluation was accessed;
whether unrelated state was preserved;
whether the run exposed another concrete implementation defect or instead reflects stochastic/model-level architectural cost.
```

## Experimental boundary

Do not alter from terminal output alone:

```text
B0/B1 prompts
four privileged knowledge components
P0 state vocabulary or dependency semantics
H1/H2 frozen bundles
semantic rubric or judge
held-out ordering
24-call ceiling
250,000-token ceiling
12-Python-attempt ceiling
provider model/reasoning configuration
continuation/falsification thresholds
```

`dev-p0-03` remains part of the development record regardless of subsequent diagnosis.

## Next step

Package and inspect the complete `dev-p0-03` raw artifacts before any additional P0 run or H1/H2 execution.
