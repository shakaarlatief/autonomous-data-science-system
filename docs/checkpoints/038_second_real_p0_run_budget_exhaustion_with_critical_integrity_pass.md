# Checkpoint 38: Second Real P0 Run Budget Exhaustion with Critical Integrity Pass

**Date:** 2026-08-09  
**Status:** Historical experiment record  
**Checkpoint class:** EXPERIMENT_EXECUTION  
**Project stage:** Prototype V0 development correction and behavioral freeze  
**Scope:** Records the historical milestone described by this checkpoint: Second Real P0 Run Budget Exhaustion with Critical Integrity Pass.  
**Authority:** Historical provenance for the recorded experiment milestone; frozen experiment contracts and final experiment conclusions govern their declared scopes.  
**Design session:** 01  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 01 - Foundations & Checkpoint 0

## Purpose

Record the terminal outcome of the second real-model P0 development-calibration trajectory after the two `dev-p0-01` controller/context corrections were deterministically validated.

This checkpoint records terminal facts only. The complete raw trajectory has not yet been inspected, so no further P0 implementation change is justified from this checkpoint alone.

No held-out H1/H2 treatment run has occurred.

---

## Run

```text
run_id: dev-p0-02
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

The resource envelope is unchanged from the preregistered common held-out protocol.

---

## Terminal result

```text
Condition: P0
Completed: False
Completed within budget: False
Budget exhausted: True
Successful model calls: 12
Generation attempts: 12
Generation failures: 0
Total observed tokens: 291,350
Python execution attempts: 4
Behavioral evaluation eligible: True
Critical deterministic assertions passed: True
```

Output was written locally to:

```text
results/raw/dev-p0-02
```

---

## Immediate interpretation

### 1. The run remains a treatment-resource failure

`dev-p0-02` did not complete within the frozen treatment envelope and remains behavior-evaluable under the preregistered rules.

The run crossed the 250,000-token ceiling on a completed provider call. Because cumulative token usage is observable only after a call returns, a single completed call may carry the total beyond the ceiling; that completed call remains part of the trajectory and no further treatment call may begin.

The observed total of 291,350 therefore does not mean the configured ceiling was silently raised.

### 2. Provider reliability remained clean

```text
generation attempts: 12
generation failures: 0
```

There is no terminal evidence of a provider-generation failure. The run stopped because of the local treatment resource rule.

### 3. The post-`dev-p0-01` corrections changed the observed trajectory materially

Relative to `dev-p0-01`:

```text
successful model calls: 10 -> 12
Python attempts:        2 -> 4
critical deterministic: fail -> pass
```

This is meaningful evidence that the corrected controller allowed substantially more project progression before the token ceiling was crossed.

However, resource viability is still unresolved because P0 again failed to finish inside the same 250,000-token envelope.

### 4. Critical deterministic pass is important but must be interpreted from raw artifacts

Unlike `dev-p0-01`, `dev-p0-02` reports:

```text
Critical deterministic assertions passed: True
```

This suggests the trajectory reached a state satisfying the current non-compensable deterministic integrity assertions even though the overall project did not finish.

The exact project position cannot be inferred safely from the terminal summary alone. In particular, the raw artifacts are needed to determine whether the run:

```text
completed Phase 2 repair;
reached final model lock;
performed protected final evaluation;
failed only before submit_final_report;
or stopped at another noncritical point.
```

### 5. Token overshoot requires per-call diagnosis

The final total exceeded the ceiling by:

```text
291,350 - 250,000 = 41,350 tokens
```

This indicates that the call which crossed the ceiling was itself large. The raw per-call usage is required to determine whether context growth is still monotonic, whether the state compaction materially flattened the curve, and whether any remaining cost is caused by duplicated context, useful project work, or additional controller friction.

---

## Comparison with `dev-p0-01`

| Measure | `dev-p0-01` | `dev-p0-02` |
|---|---:|---:|
| Completed | No | No |
| Budget exhausted | Yes | Yes |
| Successful model calls | 10 | 12 |
| Generation failures | 0 | 0 |
| Total observed tokens | 250,279 | 291,350 |
| Python attempts | 2 | 4 |
| Critical deterministic pass | No | Yes |

The larger absolute token total in `dev-p0-02` is not directly evidence that the compaction made token efficiency worse. Because the runner admits a call when cumulative usage is still below 250,000 and only observes the completed call's final usage afterward, the terminal overshoot can vary substantially depending on the size of the crossing call.

Per-call usage and cumulative curves are therefore required before comparing context efficiency.

---

## Required raw-artifact inspection

Inspect:

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

Answer at least:

```text
What exact phase/milestone had been reached at termination?
Which deterministic assertions passed and which noncritical assertions failed?
What was the per-call input/output/total token curve?
Did the two `dev-p0-01` retry-loop defects disappear?
How large were successive model-facing P0 state views?
How many state objects/relations existed and which remained current?
When did each knowledge component activate/reopen/resolve?
Was Phase 2 feature invalidation propagated precisely?
Did P0 preserve unrelated state during repair?
Was protected final evaluation performed legitimately?
Was the remaining failure primarily one missing final-report turn, broader token inefficiency, or new controller friction?
```

No third paid P0 development run should occur before this inspection.

---

## Experimental boundary remains unchanged

Do not change from this terminal result alone:

```text
B0/B1 prompts
four privileged knowledge components
P0 state vocabulary
H1/H2 bundles
semantic rubric or judge
held-out ordering
24-call ceiling
250,000-token ceiling
12-Python-attempt ceiling
provider model/reasoning configuration
continuation/falsification thresholds
```

`dev-p0-02` remains part of the development record regardless of the subsequent diagnosis.

---

## Next step

Package and inspect the complete `dev-p0-02` raw artifacts before any `dev-p0-03` run or held-out execution.
