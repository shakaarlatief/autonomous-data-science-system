# Current State

**Checkpoint:** 87  
**Date:** 2026-08-19  
**Development stage:** Prototype V0 held-out treatment execution complete; blinded semantic-evaluation supervisor implemented pending preflight  
**Resolved treatment slots:** 30 / 30  
**Remaining treatment slots:** 0 / 30  
**Next treatment slot:** none  
**Execution mode:** frozen treatment execution complete; semantic judging not yet started

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

Held-out treatment execution is complete. No B0, B1, or P0 treatment slot remains runnable.

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

## Post-execution observer correction

The optional live monitor incorrectly counted aggregate `mechanical_verification/index.json` as an attempt-level report, producing `integrity_failures=index` and a count one above the authoritative verifier total.

The monitor has been corrected to count only attempt-level reports with a valid `attempt_id` and `integrity_status`. This observer-only fix occurred after treatment execution completed and cannot have affected treatment evidence.

Detailed record:

```text
docs/checkpoints/086_post_execution_monitor_correction_and_public_release_preflight.md
```

## Blinded semantic-evaluation supervisor

A resumable condition-blind semantic-evaluation layer has now been added:

```text
prototype_v0/src/ads_v0/semantic_judge_supervisor.py
prototype_v0/tests/test_semantic_judge_supervisor.py
```

It uses the already calibrated `semantic_judge.py` implementation and does not change the registered rubric, judge model, two-pass rule, consensus rule, critical triggers, or treatment trajectories.

Before any judge inference it must:

```text
require EXPERIMENT_COMPLETE;
discover exactly one behavior-evaluable retained trajectory per frozen slot;
build the common external judge packet;
reject packet leakage of B0/B1/P0, slot IDs, or attempt IDs;
assign an opaque case identifier derived only from packet fingerprint;
write the treatment-to-case mapping to a separate local private decoder;
order judge work by opaque case identity rather than treatment order.
```

The private decoder is stored under ignored local `results/` state and is explicitly excluded from blinded review exports. It must not be inspected until all required blinded manual adjudications are frozen.

Each logical judge pass is persisted independently so completed judgments are never rerun because of their score. A condition-neutral transport-recovery rule, recorded before the first held-out semantic judge call, permits at most three provider attempts to obtain one usable logical pass when earlier provider attempts produce no usable judgment.

Detailed implementation boundary:

```text
docs/checkpoints/087_blinded_semantic_judge_supervisor_implemented_pending_preflight.md
```

At the current boundary:

```text
held-out semantic judge calls launched: 0
held-out semantic scores generated through this supervisor: 0
local deterministic validation after implementation: pending
30-case no-inference preparation validation: pending
```

## Next experimental stage

Do not run any further B0, B1, or P0 held-out treatment attempt.

First validate the new semantic orchestration without inference:

```bash
pytest
python -m ads_v0.heldout_monitor status
python -m ads_v0.semantic_judge_supervisor prepare
python -m ads_v0.semantic_judge_supervisor status
```

Expected semantic preflight shape:

```text
30 blinded cases prepared
0 model inference launched during preparation
0 / 60 logical judge passes persisted
30 / 30 treatment trajectories represented exactly once
next blinded work identified only by opaque case ID
```

After that preflight is reviewed, begin the preregistered blinded semantic evaluation:

```text
1. run two independent semantic-judge passes per retained trajectory;
2. combine exact and adjacent disagreements according to Foundation 012;
3. manually adjudicate every 0-vs-2 criterion disagreement and every SC disagreement while blinded;
4. freeze all blinded consensus values;
5. only then decode condition identity;
6. calculate H1, H2, and pooled comparisons and apply continuation/falsification criteria.
```

No unblinded midstream semantic scoring or condition comparison may occur.

## Public-release preflight

The repository/history audit has reported:

```text
blocking findings: 0
warnings: 4
result: PASS WITH WARNINGS
```

The warnings concern commit-email visibility, the absence of a chosen LICENSE, and two absolute local project-path references. None is evidence of a leaked credential or tracked runtime-result directory.

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
docs/checkpoints/087_blinded_semantic_judge_supervisor_implemented_pending_preflight.md
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

**Run the deterministic suite and no-inference semantic-judge preparation/status preflight. Do not launch paid held-out judge calls until that preflight is reviewed.**
