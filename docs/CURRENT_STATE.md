# Current State

**Checkpoint:** 81  
**Date:** 2026-08-18  
**Development stage:** Prototype V0 held-out execution active; automated supervision validation gate  
**Resolved treatment slots:** 10 / 30  
**Next frozen slot:** `h1-r04-b1-a01`  
**Current authorization:** no paid held-out inference until the new supervisor passes deterministic and retroactive validation

## What we are building

The Autonomous Data Science System aims to create the best defensible data-science process for the particular project, where the meaning of "best" depends on project goals, constraints, deliverables, and desired human involvement while methodological integrity remains non-negotiable.

System-level architectural context:

```text
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
```

The LLM is one reasoning component inside a wider system. Explicit system mechanisms must earn their complexity empirically.

## Current experiment

Prototype V0 asks:

> Can explicit project state, reusable knowledge activation, prospective safeguards, and dependency-aware repair make a strong LLM's data-science reasoning materially more reliable across a changing project than an equally capable simpler LLM workflow?

B1 remains the primary architectural control.

Quick overview:

```text
prototype_v0/README.md
```

Frozen held-out protocol:

```text
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
```

Detailed run ledger:

```text
docs/experiments/prototype_v0/HELD_OUT_STATUS.md
```

No H1/H2 S1-S10 or SC1-SC2 semantic judging has begun.

## Current experiment counts

```text
resolved treatment slots: 10 / 30
remaining treatment slots: 20 / 30
behavior-evaluable retained attempts: 10
non-behavior-evaluable provider/interface attempts: 2
replacement attempts launched: 2
P0 budget-exhausted retained runs: 2
administrative pre-provider interruptions: 1
```

The next preregistered treatment slot remains:

```text
variant: H1
replicate: 4
condition: B1
slot: h1-r04-b1
attempt: h1-r04-b1-a01
```

It has not been skipped or reordered.

## New automated supervision layer

After ten resolved slots, the manual run-by-run transport and inspection loop was judged unnecessarily expensive and non-scalable.

Implemented:

```text
prototype_v0/src/ads_v0/heldout_verifier.py
    read-only mechanical verification of completed attempts

prototype_v0/src/ads_v0/heldout_supervisor.py
    bounded sequential orchestration around the unchanged frozen executor

prototype_v0/tests/test_heldout_verifier.py
prototype_v0/tests/test_heldout_supervisor.py
```

Detailed architecture:

```text
docs/foundations/015_held_out_supervision_and_mechanical_verification_architecture.md
```

Implementation checkpoint:

```text
docs/checkpoints/081_automated_held_out_supervision_implemented_pending_retroactive_validation.md
```

Major structural history:

```text
docs/MAJOR_CHANGES.md
```

## What the verifier checks

The first verifier version checks:

```text
M01 required attempt artifacts
M02 attempt identity / frozen slot mapping
M03 frozen plan and bundle provenance
M04 registered runtime configuration
M05 executor classification consistency
M06 resource and budget accounting
M07 trace sequencing and resource reconciliation
M08 exact deterministic-evaluator recomputation
M09 milestone / completion consistency
M10 protected final-test access sequencing
M11 conversation / model-call consistency
```

Verifier output is written outside the treatment attempt directories under:

```text
results/held_out/mechanical_verification/
```

Behavioral events such as Python errors, budget exhaustion, incomplete work, or deterministic failures are recorded but do not become replacement reasons.

## Supervisor boundary

The supervisor:

```text
uses heldout_runner.execute_next_attempt() unchanged;
remains sequential;
preserves frozen slot order;
preserves frozen replacement semantics;
does not modify B0/B1/P0;
does not expose previous outcomes to later treatments;
does not perform semantic judging;
does not write inside completed attempt directories;
can create compact review exports instead of one raw ZIP per ordinary run.
```

The frozen treatment experiment has therefore not changed.

## Validation gate before using the supervisor for paid inference

No new held-out attempt is authorized yet.

First run, from `prototype_v0/`:

```bash
pytest
python -m ads_v0.heldout_supervisor verify-existing
python -m ads_v0.heldout_supervisor export
```

Required result before prospective use:

```text
full pytest suite passes;
all completed held-out attempts are retroactively verified;
zero verifier integrity failures;
compact export is reviewed against existing manual records.
```

The retroactive pass must include the two non-behavior-evaluable H1 R2 B0 provider/interface attempts in addition to all retained behavior-evaluable attempts.

If the verifier exposes a verifier/supervisor defect, only that external supervision infrastructure may be repaired. No treatment, prompt, benchmark, budget, frozen rule, or semantic evaluator may be changed from held-out evidence.

## Important existing experimental consequence

P0 has exhausted the common 250,000-token envelope in two retained H1 runs:

```text
H1 R1 P0: budget exhausted
H1 R2 P0: within budget
H1 R3 P0: budget exhausted
```

The preregistered continuation criteria permit no more than one P0 budget-exhausted run. That specific criterion can no longer be satisfied regardless of later outcomes.

This is an objective resource result, not a semantic or overall architectural verdict. The remaining frozen experiment continues after the supervisor validation gate.

## Knowledge-preservation architecture

Current preservation flow remains Development Method v0.3:

```text
discussion
    -> checkpoint
    -> promotion audit
    -> canonical/foundational/specification update when warranted
    -> KNOWLEDGE_MAP routing update when warranted
    -> concise CURRENT_STATE

meaningful stage boundary
    -> knowledge reconciliation
```

Key preservation sources:

```text
docs/KNOWLEDGE_MAP.md
docs/DEVELOPMENT_METHOD.md
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
docs/MAJOR_CHANGES.md
```

## Minimum reading for a future session

```text
README.md
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
prototype_v0/README.md
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
docs/foundations/015_held_out_supervision_and_mechanical_verification_architecture.md
docs/experiments/prototype_v0/HELD_OUT_STATUS.md
```

## Current priority

**Validate the new external supervisor without inference. Do not launch `h1-r04-b1-a01` until the tests, retroactive verifier pass, and compact export have been reviewed.**
