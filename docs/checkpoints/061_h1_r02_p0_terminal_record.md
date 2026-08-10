# Checkpoint 61: H1 R2 P0 Terminal Record

**Date:** 2026-08-10

## Purpose

Record the executor-level outcome of the fifth preregistered held-out slot before any raw artifact inspection or later held-out execution.

No semantic S1-S10 or SC1-SC2 judging is performed at this checkpoint.

## Attempt identity

```text
variant: H1
replicate: 2
condition: P0
slot: h1-r02-p0
attempt: h1-r02-p0-a01
```

## Observed executor result

The user ran the authorized one-attempt command:

```bash
python -m ads_v0.heldout_runner run-next
```

Observed terminal output:

```text
Action: ATTEMPT_COMPLETED
Model attempt launched: True
Attempt: h1-r02-p0-a01
Classification: BEHAVIOR_EVALUABLE
Behavior evaluable: True
Replacement eligible: False
Slot resolved: True
```

## Immediate protocol consequences

The executor classification is sufficient to establish only the following:

```text
h1-r02-p0 is permanently resolved;
h1-r02-p0-a01 is retained as held-out evidence;
no replacement attempt is permitted for this slot;
the experiment advances only after raw mechanical inspection is complete.
```

A behavior-evaluable result remains retained regardless of whether the underlying P0 trajectory completed the project, exhausted its token budget, encountered Python errors, failed deterministic assertions, or later receives weak semantic scores.

## What is not yet established

The terminal executor output does not reveal:

```text
completed vs incomplete
completed_within_budget
budget_exhausted
model-call count
total token usage
Python execution count
provider retry count
A0-A4 deterministic outcomes
critical deterministic failures
P0 state-control consistency
knowledge activations
Phase 2 dependency repair
final model lock
protected-test sequencing
final report status
```

These must be read from the persisted attempt artifacts before H1 R2 B0 is authorized.

## Required artifact directory

```text
results/held_out/attempts/h1-r02-p0-a01/
```

Inspect at minimum:

```text
attempt_started.json
attempt_record.json
summary.json
deterministic_evaluation.json
milestones.json
conversation.json
trace.jsonl
p0_state.json
p0_state_history.json
p0_knowledge_activations.json
```

## Held-out count after this terminal result

```text
resolved slots: 5 / 30
behavior-evaluable retained attempts: 5
non-behavior-evaluable replacement attempts: 0
known P0 budget-exhausted runs: 1
```

The known P0 budget-exhausted count remains 1 until the raw `h1-r02-p0-a01` summary is inspected. The preregistered continuation threshold must not be inferred from the terminal executor classification alone.

## Freeze discipline

P0 behavior, B0/B1 prompts, bundles, resource limits, provider/model configuration, run order, semantic rubric, and execution infrastructure remain frozen. No implementation change is permitted in response to this held-out outcome unless a genuine common mechanical harness defect is demonstrated under the preregistered protocol.

## Current decision

Do not launch `h1-r02-b0-a01` yet. First inspect the complete persisted artifacts for `h1-r02-p0-a01` and record its mechanical completion, resource, deterministic, state-repair, and protected-test outcome.
