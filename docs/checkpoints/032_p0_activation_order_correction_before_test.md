# Checkpoint 32: P0 Activation-Order Correction Before Test

**Date:** 2026-08-09

## Purpose

Record a controller-ordering issue identified by inspection before the first local test run of P0, and the condition-neutral correction applied before any real-model P0 trajectory.

## Issue identified

The initial P0 runner applied a model state patch, instantiated newly applicable knowledge, and only then validated the command's `motivator_ids`.

That ordering creates an impossible requirement in one important case:

```text
current model response creates the first facts that satisfy an activation pattern
-> controller creates a new blocking knowledge question with a new canonical ID
-> same response is then required to cite that new ID as a motivator
```

The model could not have cited the ID because it did not exist when the response was generated.

This is an implementation semantics defect, not an experimental finding. It was detected before any real P0 run and before held-out execution.

## Correction

The operational P0 controller is now in:

```text
prototype_v0/src/ads_v0/p0_controller.py
```

Its ordering is:

```text
1. transactionally apply the model patch;
2. reopen already-existing knowledge instances affected by invalidation;
3. validate the action against the frontier visible when the model responded;
4. create the ACTION object;
5. instantiate newly applicable knowledge from the accepted patch;
6. execute the common command.
```

Consequences:

```text
ordinary action:
newly activated concern appears in the next state view;

phase transition:
newly activated blocking concern already exists before dispatch, so the phase
transition can still be prospectively blocked.
```

This preserves both causal fairness and the intended blocking semantics.

## Calibration CLI

`calibrate_p0.py` now imports the operational controller from `p0_controller.py`.

No B0/B1 code, held-out bundle, rubric, resource threshold, knowledge content, or continuation criterion changed.

## Additional regression tests

Two controller-order tests were added:

```text
new blocker created from the current patch does not retroactively invalidate the
same response's motivator references;

new blocker created from the current patch can still block an attempted Phase 1
transition before the transition executes.
```

The total new P0-related tests awaiting the first local execution are therefore:

```text
9 tests in test_p0.py
2 tests in test_p0_controller.py
11 new tests total
```

The prior suite contained 34 passing tests, so the expected total after this
correction is 45 if all tests pass.

## Status

No real P0 model call has occurred yet.

The immediate next action remains:

```text
git pull origin main
pytest
```
