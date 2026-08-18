# Current State

**Checkpoint:** 83  
**Date:** 2026-08-18  
**Development stage:** Prototype V0 held-out execution active  
**Resolved treatment slots:** 13 / 30  
**Remaining treatment slots:** 17 / 30  
**Next frozen slot:** `h1-r05-p0-a01`  
**Execution mode:** prospectively validated sequential supervisor; large bounded unattended batch authorized

## Current experiment

Prototype V0 asks:

> Can explicit project state, reusable knowledge activation, prospective safeguards, and dependency-aware repair make a strong LLM's data-science reasoning materially more reliable across a changing project than an equally capable simpler LLM workflow?

B1 remains the primary architectural control.

Frozen held-out protocol:

```text
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
```

Detailed run ledger:

```text
docs/experiments/prototype_v0/HELD_OUT_STATUS.md
```

No H1/H2 S1-S10 or SC1-SC2 semantic judging has begun.

## Current counts

```text
resolved treatment slots: 13 / 30
remaining treatment slots: 17 / 30
behavior-evaluable retained attempts: 13
non-behavior-evaluable provider/interface attempts: 2
replacement attempts launched: 2
P0 budget-exhausted retained runs: 3
administrative pre-provider interruptions: 1
completed attempt directories mechanically verified: 15
mechanical integrity failures: 0
```

## First prospective supervisor batch passed

The first live batch used:

```bash
python -m ads_v0.heldout_supervisor run-batch --max-model-attempts 3
```

Batch:

```text
batch-20260818T170118Z
```

It launched exactly three paid attempts in the frozen order:

```text
h1-r04-b1-a01
h1-r04-p0-a01
h1-r05-b1-a01
```

All three were behavior-evaluable, permanently resolved their treatment slots, and passed all M01-M11 mechanical integrity checks.

Post-batch verifier state:

```text
15 completed attempt directories verified
15 integrity PASS
0 integrity FAIL
```

The supervisor stopped exactly because the explicit three-attempt batch limit was reached and derived the correct next slot:

```text
h1-r05-p0-a01
```

Detailed record:

```text
docs/checkpoints/083_first_live_supervisor_batch_validated_and_unattended_execution_authorized.md
```

## New retained mechanical outcomes

### H1 R4 B1

```text
attempt: h1-r04-b1-a01
completed: true
budget exhausted: false
model calls: 16
Python attempts: 6
total tokens: 152,391
A0-A4: PASS
review flags: none
```

Final lock sequence 30, protected-test access sequence 33, final report sequence 35.

### H1 R4 P0

```text
attempt: h1-r04-p0-a01
completed: false
budget exhausted: true
model calls: 14
Python attempts: 5
total tokens: 262,255
A0-A4: PASS
review flags: budget_exhausted, incomplete_run
```

The run reached final lock and one protected-test evaluation but no final report before the resource envelope stopped further reasoning.

This is the third retained P0 budget exhaustion:

```text
H1 R1 P0: budget exhausted
H1 R2 P0: within budget
H1 R3 P0: budget exhausted
H1 R4 P0: budget exhausted
```

The preregistered maximum of one P0 budget-exhausted run was already impossible after H1 R3. The frozen experiment continues unchanged.

### H1 R5 B1

```text
attempt: h1-r05-b1-a01
completed: true
budget exhausted: false
model calls: 17
Python attempts: 7
total tokens: 155,299
A0-A4: PASS
review flags: python_execution_error_or_timeout
```

One model-authored Python execution returned code 1. The trajectory remained behavior-evaluable and completed normally. Final lock was sequence 32, protected-test access sequence 35, and final report sequence 37.

## Supervisor status

The supervision layer has now passed both validation stages:

```text
software tests: 77 passed
retrospective verification before paid use: 12 / 12 PASS
first prospective batch: 3 / 3 new attempts PASS
current completed-attempt verification: 15 / 15 PASS
```

The validated implementation remains frozen for Prototype V0 operational use unless a genuine condition-neutral infrastructure defect is discovered.

The supervisor still:

```text
uses the unchanged frozen execute_next_attempt() path;
runs sequentially only;
preserves slot order and replacement semantics;
does not modify B0, B1, or P0;
does not expose previous outcomes to later treatments;
does not perform semantic judging;
does not write verifier output into treatment attempt directories.
```

## Next authorized action

The next frozen treatment is:

```text
variant: H1
replicate: 5
condition: P0
slot: h1-r05-p0
attempt: h1-r05-p0-a01
```

The live smoke-test gate is complete. A large bounded supervisor batch is now authorized:

```bash
python -m ads_v0.heldout_supervisor run-batch --max-model-attempts 30
```

There are 17 unresolved treatment slots. If every remaining slot resolves on its first attempt, the command will stop at `EXPERIMENT_COMPLETE` after 17 paid attempts. Provider-failure replacements consume additional attempt allowance. The supervisor must stop earlier if it encounters a mechanical integrity failure or another frozen runner safety state.

Do not invoke `heldout_runner run-next` separately while the supervisor workflow is active.

After the batch stops, review its single compact export before beginning semantic judging.

## Knowledge and continuity

Minimum reading for a future session:

```text
README.md
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
prototype_v0/README.md
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
docs/foundations/015_held_out_supervision_and_mechanical_verification_architecture.md
docs/experiments/prototype_v0/HELD_OUT_STATUS.md
```

System-level architecture:

```text
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
```

Knowledge-preservation architecture:

```text
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
```

## Current priority

**Use the validated supervisor to continue the remaining held-out treatment execution in one large bounded sequential batch where possible, then stop for compact-export review before semantic evaluation.**