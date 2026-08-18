# Current State

**Checkpoint:** 84  
**Date:** 2026-08-18  
**Development stage:** Prototype V0 held-out execution active  
**Resolved treatment slots:** 13 / 30  
**Remaining treatment slots:** 17 / 30  
**Next frozen slot:** `h1-r05-p0-a01`  
**Execution mode:** prospectively validated sequential supervisor; large bounded unattended batch authorized; optional read-only live monitor available

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

## Supervisor validation status

The held-out supervisor/verifier has passed both required validation stages:

```text
software tests before live use: 77 passed
retrospective verification: 12 / 12 PASS
first prospective batch: 3 / 3 new attempts PASS
current completed-attempt verification: 15 / 15 PASS
```

The first prospective batch launched, in frozen order:

```text
h1-r04-b1-a01
h1-r04-p0-a01
h1-r05-b1-a01
```

All three were behavior-evaluable and mechanically coherent. The supervisor stopped exactly at the explicit three-attempt limit and derived the correct next slot:

```text
h1-r05-p0-a01
```

Detailed record:

```text
docs/checkpoints/083_first_live_supervisor_batch_validated_and_unattended_execution_authorized.md
```

## Important current resource consequence

P0 has now exhausted the common 250,000-token envelope in three retained H1 runs:

```text
H1 R1 P0: budget exhausted
H1 R2 P0: within budget
H1 R3 P0: budget exhausted
H1 R4 P0: budget exhausted
```

The preregistered maximum of one P0 budget-exhausted run was already impossible after H1 R3. The frozen experiment continues unchanged so the remaining reliability, semantic, and comparative evidence can still be collected without selective stopping.

## Live observability before the large batch

A separate read-only monitor was added after the prospective supervisor smoke test:

```text
prototype_v0/src/ads_v0/heldout_monitor.py
prototype_v0/tests/test_heldout_monitor.py
```

This did **not** modify the validated supervisor, verifier, runner, treatments, protocol, or experiment state.

The monitor only reads the append-only attempt and verification directories and can display:

```text
active attempt identity
current phase
successful model generations observed in trace
Python attempts
generation errors
trace-event count
latest event type
completed attempt-record count
verification-report count
verification-integrity failures
```

It also prints periodic heartbeats. Stopping the monitor does not stop the supervisor.

Detailed record:

```text
docs/checkpoints/084_read_only_live_observability_added_before_large_unattended_batch.md
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

Before the large batch, pull the latest repository state and run the test suite once to validate the newly added monitor module:

```bash
git pull origin main
pytest
```

Then use two terminals from `prototype_v0/`.

Terminal 1, read-only observability:

```bash
python -m ads_v0.heldout_monitor watch
```

Terminal 2, actual experiment execution:

```bash
python -m ads_v0.heldout_supervisor run-batch --max-model-attempts 30
```

There are 17 unresolved treatment slots. If every remaining slot resolves on its first attempt, the supervisor will stop at `EXPERIMENT_COMPLETE` after 17 paid attempts. Provider-failure replacements consume additional attempt allowance. The supervisor must stop earlier if it encounters a mechanical integrity failure or another frozen runner safety state.

Do not invoke `heldout_runner run-next` separately while the supervisor workflow is active.

After the batch stops, upload the single compact supervisor export before beginning semantic judging.

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

**Validate the new read-only monitor with the software suite, then use the monitor and validated supervisor in separate terminals for the remaining large bounded held-out batch.**
