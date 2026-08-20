# Checkpoint 37: P0 Controller Corrections Deterministically Validated

**Date:** 2026-08-09  
**Status:** Historical verification record  
**Checkpoint class:** EXPERIMENT_VERIFICATION  
**Project stage:** Prototype V0 development correction and behavioral freeze  
**Scope:** Records the historical milestone described by this checkpoint: P0 Controller Corrections Deterministically Validated.  
**Authority:** Historical provenance for the recorded experiment milestone; frozen experiment contracts and final experiment conclusions govern their declared scopes.  
**Design session:** 01  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 01 - Foundations & Checkpoint 0

## Purpose

Record the deterministic validation boundary after the two `dev-p0-01` implementation corrections documented in Checkpoint 36.

Those corrections were:

```text
1. validate action motivators against the pre-patch runnable frontier visible to the model;
2. compact the model-facing P0 state projection so audit-only ACTION history and closed workflow controls are not repeatedly re-serialized as current reasoning state.
```

No held-out H1/H2 treatment run has occurred.

## Local validation result

After pulling the corrected controller/context implementation, the complete Prototype V0 test suite passed:

```text
48 passed in 9.97s
```

The suite includes the two regression tests added specifically from the first real-model P0 failure:

```text
same-turn closure of a pre-patch motivator remains a valid generated action;
model-facing state excludes audit-only ACTION payloads and closed controls while the full audited state retains them.
```

All pre-existing benchmark, runtime, baseline, provider-adapter, semantic-judge, typed-state, activation, dependency, repair-priority, phase-gate, and P0 orchestration tests continue to pass.

## Interpretation

The green suite establishes that the two development-debugging corrections are deterministically coherent with the rest of Prototype V0.

It does **not** establish that P0 is behaviorally superior to B0/B1 or that the next stochastic trajectory will complete within budget.

The next empirical question is narrower:

> Can the corrected P0 controller complete a real development trajectory within the already frozen common treatment envelope, without the artificial retry loops and repeated audit-context growth observed in `dev-p0-01`?

## Experimental boundary preserved

Nothing about the frozen held-out experiment changes.

Still unchanged:

```text
B0 and B1 prompts;
the four privileged methodological knowledge components;
P0 state object and relation vocabulary;
H1/H2 bundle identities;
held-out run counts and ordering;
semantic rubric and blinded judge;
continuation and falsification thresholds;
model and reasoning effort;
24 successful model calls;
250,000 observed treatment tokens;
12 Python execution attempts;
30,000 maximum output tokens per call;
previous_response_id continuation;
all-turn reasoning context.
```

The `dev-p0-01` failure remains part of the development record and is not discarded or relabeled.

## Decision

The corrected implementation is authorized for a second real-model development-calibration trajectory:

```text
dev-p0-02
```

The run must use the same development benchmark and the unchanged frozen common treatment envelope.

Do not begin H1/H2 held-out treatment execution yet.

## Next step

Run:

```bash
python -m ads_v0.calibrate_p0 \
  --bundle generated/development \
  --run-id dev-p0-02 \
  --output results/raw/dev-p0-02 \
  --model gpt-5.6-terra \
  --reasoning-effort high \
  --max-model-calls 24 \
  --max-total-tokens 250000 \
  --max-python-execution-attempts 12 \
  --max-generation-retries 2 \
  --max-output-tokens 30000
```

Inspect the terminal summary before running any further P0 replicate.
