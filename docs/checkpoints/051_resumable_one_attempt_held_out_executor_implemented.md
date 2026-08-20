# Checkpoint 51: Resumable One-Attempt Held-Out Executor Implemented

**Date:** 2026-08-10  
**Status:** Historical infrastructure record  
**Checkpoint class:** INFRASTRUCTURE  
**Project stage:** Prototype V0 held-out execution preparation  
**Scope:** Records the historical milestone described by this checkpoint: Resumable One-Attempt Held-Out Executor Implemented.  
**Authority:** Historical provenance; current canonical documents and promoted sources govern current interpretation.  
**Design session:** 01  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 01 - Foundations & Checkpoint 0

## Purpose

Implement the condition-neutral execution layer that can advance the preregistered held-out experiment safely without accidentally launching multiple paid trajectories, skipping unresolved slots, or replacing behavioral failures.

No H1/H2 treatment call has occurred at this checkpoint.

## Preconditions already established

```text
P0 behavioral/controller logic frozen after dev-p0-04;
B0/B1 common 24-call / 250k-token / 12-Python envelope validated;
frozen H1/H2 identities verified in the real local environment;
results/held_out/run_plan.json materialized with the exact 30-slot order;
complete deterministic suite previously at 62/62.
```

## New module

```text
prototype_v0/src/ads_v0/heldout_runner.py
```

The module exposes two intentionally separate CLI actions:

```text
python -m ads_v0.heldout_runner status
python -m ads_v0.heldout_runner run-next
```

`status` performs no model inference.

`run-next` is explicit and may launch at most one paid treatment attempt. It never loops through the complete experiment.

## Execution-time freeze validation

Before any attempted launch the executor:

```text
loads the materialized run_plan.json;
loads the preregistered protocol;
revalidates both local H1/H2 bundle fingerprints;
rebuilds the expected plan deterministically;
requires exact structural equality between the materialized and expected plan.
```

Any plan edit, configuration drift, bundle modification, or fingerprint mismatch aborts before provider inference.

## Earliest-unresolved-slot rule

The executor scans the 30 slots in the registered order and can act only on the earliest unresolved slot.

It cannot skip to a later condition or replicate while an earlier slot is unresolved.

Initial attempt IDs remain:

```text
h1-r01-b0-a01
h1-r01-b1-a01
...
```

Replacement attempts remain inside the same slot:

```text
h1-r01-b0-a02
h1-r01-b0-a03
```

## Append-only attempt ledger

Attempts are stored under:

```text
results/held_out/attempts/<attempt_id>/
```

Before any model call begins the executor creates the attempt directory and writes:

```text
attempt_started.json
```

This contains the attempt identity, slot identity, plan SHA-256, bundle SHA-256, start time, and registered model/resource configuration.

After the treatment runner returns and writes `summary.json`, the executor writes:

```text
attempt_record.json
```

containing the outcome classification and a copy of the summary plus diagnostic wall-clock time.

## Crash/ambiguity semantics

If an attempt directory contains only `attempt_started.json` and no valid summary, execution pauses:

```text
INTERRUPTED_ATTEMPT
```

The executor does not assume that no paid provider work happened, so it refuses to duplicate that attempt automatically.

If `summary.json` exists but the final executor record does not, the next `run-next` invocation performs bookkeeping reconciliation only:

```text
RECONCILED_EXISTING_SUMMARY
Model attempt launched: False
```

This handles a crash after treatment artifacts were safely persisted but before executor bookkeeping finished.

## Replacement classification

A valid summary with:

```text
behavior_evaluable = true
```

resolves the slot regardless of whether the treatment completed successfully. Therefore the following are never replaced:

```text
budget exhaustion
incomplete work
Python exception/timeout
methodological error
deterministic critical failure
semantic error
poor model choice
poor resource efficiency
```

A summary with:

```text
behavior_evaluable = false
terminal_generation_error = non-empty
```

is classified as:

```text
NON_BEHAVIOR_EVALUABLE_PROVIDER_FAILURE
```

and may receive a replacement attempt in the same slot.

After three non-behavior-evaluable attempts (`a01`, `a02`, `a03`) the executor returns:

```text
REPLACEMENTS_EXHAUSTED
```

and launches nothing further until the experiment is investigated.

## Registered configuration passed to treatment runners

The production dispatch uses the materialized protocol configuration:

```text
provider: OpenAI
model: gpt-5.6-terra
reasoning effort: high
max successful model calls: 24
max observed total tokens: 250000
max Python execution attempts: 12
max additional generation retries: 2
max output tokens per call: 30000
Python timeout contract: 60 seconds
provider request timeout contract: 300 seconds
```

B0/B1 dispatch through the common baseline runner with the explicit resource limits. P0 dispatches through the frozen P0 runner with the same resource limits.

The executor validates the registered timeout values against the frozen Version 0 runtime constants before launch.

## New deterministic tests

Seven tests were added covering:

```text
first status is exactly h1-r01-b0-a01;
behavior-evaluable attempt resolves its slot and advances to h1-r01-b1-a01;
provider failure creates an in-slot a02 replacement;
three provider failures pause rather than advance;
interrupted attempt marker blocks duplicate execution;
summary-without-record is reconciled without a model call;
registered model/resource limits are passed and tampered run plans are rejected.
```

Expected complete suite after this checkpoint:

```text
69 passed
```

## Current decision

Do not run `run-next` yet. First pull this implementation and run the complete local deterministic suite. If all 69 tests pass, inspect no-inference `status` against the real materialized plan before authorizing the first held-out treatment attempt.
