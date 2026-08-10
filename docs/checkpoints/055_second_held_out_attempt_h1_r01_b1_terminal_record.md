# Checkpoint 55: Second Held-Out Attempt H1 R01 B1 Terminal Record

**Date:** 2026-08-10

## Purpose

Record the executor-level outcome of the second preregistered held-out slot before any later slot is launched.

## Attempt identity

```text
variant: H1
replicate: 1
condition: B1
slot: h1-r01-b1
attempt: h1-r01-b1-a01
```

This is the second slot in the frozen H1 replicate-1 order:

```text
B0, B1, P0
```

## Observed executor result

The user ran exactly one authorized command:

```bash
python -m ads_v0.heldout_runner run-next
```

Observed terminal output:

```text
Action: ATTEMPT_COMPLETED
Model attempt launched: True
Attempt: h1-r01-b1-a01
Classification: BEHAVIOR_EVALUABLE
Behavior evaluable: True
Replacement eligible: False
Slot resolved: True
```

## Immediate protocol consequences

```text
h1-r01-b1 is permanently resolved;
h1-r01-b1-a01 remains part of held-out evidence;
no replacement attempt is permitted for this slot;
no conclusion about completion, budget status, deterministic assertions, or semantics is inferred from executor classification alone.
```

`BEHAVIOR_EVALUABLE` means the run is retained even if its treatment behavior is incomplete, resource-expensive, methodologically poor, or deterministically invalid. Those outcomes are part of the experiment and are not replacement criteria.

## Required raw verification before slot 3

Inspect the complete persisted attempt directory:

```text
results/held_out/attempts/h1-r01-b1-a01/
```

At minimum verify:

```text
attempt_started.json
attempt_record.json
summary.json
deterministic_evaluation.json
milestones.json
conversation.json
trace.jsonl
```

Record:

```text
completion and completed-within-budget status;
token/call/Python resource use;
generation failures/retries;
critical deterministic assertions;
protected-test sequencing;
executor-attempt identity and resource-config consistency;
any runtime or bookkeeping anomaly.
```

Do not assign S1-S10 or SC1-SC2 manually. Semantic scoring remains reserved for the frozen blinded judge.

## Current decision

Do not launch the third held-out slot, `h1-r01-p0-a01`, until `h1-r01-b1-a01` has been mechanically verified from its persisted raw artifacts.
