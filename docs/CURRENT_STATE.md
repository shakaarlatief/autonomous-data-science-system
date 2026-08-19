# Current State

**Checkpoint:** 86  
**Date:** 2026-08-19  
**Development stage:** Prototype V0 held-out treatment execution complete; blinded semantic evaluation pending  
**Resolved treatment slots:** 30 / 30  
**Remaining treatment slots:** 0 / 30  
**Next treatment slot:** none  
**Execution mode:** frozen held-out execution completed under the prospectively validated sequential supervisor

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

Held-out treatment execution is now complete. No treatment slot remains runnable.

## Final treatment-execution counts

```text
resolved treatment slots: 30 / 30
behavior-evaluable retained attempts: 30
B0 retained runs: 10
B1 retained runs: 10
P0 retained runs: 10
non-behavior-evaluable provider/interface attempts: 4
mechanically verified persisted attempts: 34
mechanical integrity PASS: 34
mechanical integrity FAIL: 0
administrative pre-provider interruptions: 1
```

The final compact supervisor export has been reviewed mechanically:

```text
heldout_supervisor_export_20260818T220552Z.zip
```

Detailed record:

```text
docs/checkpoints/085_held_out_execution_complete_and_full_compact_export_verified.md
```

## Final pooled mechanical outcomes

| Condition | Completed | Completed within budget | Budget exhausted | Final reports | Median total tokens | Median calls | Median Python |
|---|---:|---:|---:|---:|---:|---:|---:|
| B0 | 10 / 10 | 10 / 10 | 0 / 10 | 10 / 10 | 122,544.5 | 16 | 6 |
| B1 | 10 / 10 | 10 / 10 | 0 / 10 | 10 / 10 | 120,564.5 | 16 | 6 |
| P0 | 6 / 10 | 3 / 10 | 7 / 10 | 6 / 10 | 260,370.0 | 13 | 5 |

P0/B1 pooled median ratios:

```text
total tokens: 2.160
successful model calls: 0.813
Python attempts: 0.833
```

All 30 retained behavior-evaluable trajectories pass the registered deterministic A0-A4 checks according to the final mechanical-verification export.

## Continuation criterion status

The registered V0 continuation signal is already impossible on mechanical resource/completion outcomes alone.

Foundation 012 requires:

```text
P0 completed within budget: at least 9 / 10
P0 budget-exhausted runs: at most 1 / 10
P0/B1 median total-token ratio: at most 1.50
```

Observed:

```text
P0 completed within budget: 3 / 10
P0 budget-exhausted runs: 7 / 10
P0/B1 median total-token ratio: 2.160
```

Semantic judging is still required before deciding whether the overall V0 result meets a registered strong-falsification condition or should be classified as inconclusive/no demonstrated continuation signal.

## Final unattended batch

The final batch was:

```bash
python -m ads_v0.heldout_supervisor run-batch --max-model-attempts 30
```

Batch identity:

```text
batch-20260818T212414Z
```

Result:

```text
model attempts launched: 19
behavior-evaluable attempts in batch: 17
provider-failure attempts in batch: 2
stop reason: EXPERIMENT_COMPLETE
resolved slots: 30 / 30
```

The two provider failures occurred at H2 R5 B0 `a01` and `a02`; the registered final replacement `a03` completed and became the retained trajectory.

## Observer-only monitor correction

The uploaded live-monitor log exposed a display/counting defect:

```text
verified count was one too high
integrity_failures=index
```

The authoritative supervisor export shows 34 verified attempts and zero integrity failures. The monitor was accidentally counting aggregate `mechanical_verification/index.json` as though it were an attempt-level report.

The monitor has now been corrected to count only JSON objects that contain an attempt-level string `attempt_id` and an `integrity_status` of `PASS` or `FAIL`. A regression test was added that places `index.json` beside genuine attempt reports and verifies it is ignored.

This correction affects only the optional read-only observer and was made after treatment execution completed. It does not modify any held-out trajectory, verifier result, or supervisor decision.

Detailed record:

```text
docs/checkpoints/086_post_execution_monitor_correction_and_public_release_preflight.md
```

Local test-suite confirmation of this post-execution observer fix is still required before starting judge execution.

## Next experimental stage

Do not run any further B0, B1, or P0 held-out treatment attempt.

After pulling the latest repository state, run:

```bash
pytest
```

Then begin the preregistered blinded semantic evaluation:

```text
1. build condition-neutral normalized judge inputs for all 30 retained trajectories;
2. run two independent semantic-judge passes per trajectory;
3. score S1-S10 and SC1/SC2;
4. combine exact and adjacent disagreements according to Foundation 012;
5. manually adjudicate every 0-vs-2 criterion disagreement and every SC disagreement while blinded;
6. only after consensus is frozen, decode condition identity;
7. calculate H1, H2, and pooled comparisons and apply continuation/falsification criteria.
```

No unblinded midstream semantic scoring should occur.

## Public-release preflight

A local public-release audit has been run after adding a conservative repository/history scanner.

Result:

```text
blocking findings: 0
warnings: 4
result: PASS WITH WARNINGS
```

The warnings concern commit-email visibility, the absence of a chosen LICENSE, and two absolute local project-path references. None is evidence of a leaked credential or tracked runtime-result directory.

The repository should remain private through completion of the blinded semantic evaluation and final V0 interpretation. Publication preparation can continue without changing visibility.

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
docs/checkpoints/085_held_out_execution_complete_and_full_compact_export_verified.md
docs/checkpoints/086_post_execution_monitor_correction_and_public_release_preflight.md
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

**Pull the post-execution observer correction, run the deterministic test suite once, then begin the preregistered blinded semantic-judge stage without modifying or rerunning held-out treatment trajectories.**
