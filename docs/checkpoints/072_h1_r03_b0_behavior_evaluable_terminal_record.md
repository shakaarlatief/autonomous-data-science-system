# Checkpoint 72 - H1 R3 B0 behavior-evaluable terminal record

Date: 2026-08-18

## Observed executor result

The genuine initial H1 replicate 3 B0 attempt completed at the executor level with:

```text
Action: ATTEMPT_COMPLETED
Model attempt launched: True
Attempt: h1-r03-b0-a01
Classification: BEHAVIOR_EVALUABLE
Behavior evaluable: True
Replacement eligible: False
Slot resolved: True
```

## Immediate experimental consequence

Under the frozen replacement policy:

```text
behavior_evaluable = true
=> slot permanently resolved
=> never replaced
```

Therefore `h1-r03-b0-a01` is the retained trajectory for H1 R3 B0 and no replacement is permitted, regardless of later mechanical findings.

This terminal classification alone does not establish project completion, budget status, resource usage, deterministic A0-A4 results, provider retry behavior, Python outcomes, final-test sequencing, or final-report status. Those require inspection of the persisted run artifacts before H1 R3 B1 is launched.

## Current held-out count after terminal classification

```text
resolved treatment slots: 8 / 30
behavior-evaluable retained attempts: 8
non-behavior-evaluable provider/interface attempts: 2
replacement attempts launched: 2
P0 budget-exhausted retained runs: 2
administrative pre-provider interruptions: 1
```

No S1-S10 or SC1-SC2 semantic judging has begun.

## Next step

Inspect the complete persisted artifact directory:

```text
results/held_out/attempts/h1-r03-b0-a01/
```

Do not launch H1 R3 B1 until this B0 attempt has been fully mechanically verified.
