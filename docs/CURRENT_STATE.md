# Current State

**Checkpoint:** 89  
**Date:** 2026-08-19  
**Development stage:** Prototype V0 held-out treatment execution complete; blinded semantic evaluation authorized  
**Resolved treatment slots:** 30 / 30  
**Remaining treatment slots:** 0 / 30  
**Next treatment slot:** none  
**Execution mode:** frozen treatment execution complete; condition-blind semantic judge execution ready

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

Detailed completion record:

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

The registered continuation signal is already impossible on resource/completion outcomes alone because P0 completed only 3/10 runs within budget, exhausted the budget in 7/10 runs, and has a pooled median-token ratio of 2.160 versus B1. Semantic judging remains required to determine the registered overall interpretation and whether a strong-falsification condition is met.

## Post-execution observer correction

The optional held-out live monitor was corrected after treatment execution to ignore aggregate `mechanical_verification/index.json`. The user has confirmed the corrected authoritative display locally:

```text
active=none
completed_attempts=34
verified=34
integrity_failures=none
```

Detailed record:

```text
docs/checkpoints/086_post_execution_monitor_correction_and_public_release_preflight.md
```

## Blinded semantic-evaluation infrastructure

The semantic supervisor is:

```text
prototype_v0/src/ads_v0/semantic_judge_supervisor.py
prototype_v0/tests/test_semantic_judge_supervisor.py
```

It uses the already calibrated `semantic_judge.py` and preserves Foundation 012 exactly:

```text
30 retained trajectories
2 independent judge passes each
S1-S10
SC1-SC2
exact agreement retained
adjacent disagreement averaged
0-vs-2 disagreement requires blinded manual adjudication
SC disagreement requires blinded manual adjudication
```

Preparation requires the treatment experiment to be complete, discovers one retained behavior-evaluable trajectory per slot, builds the common external judge packet, rejects B0/B1/P0 and execution-identity leakage, assigns an opaque case ID derived only from packet fingerprint, and stores the treatment mapping in a separate local private decoder that is excluded from blinded exports.

## Semantic preflight result

The corrected no-inference preflight has now passed completely.

Observed locally:

```text
pytest: 84 passed in 12.14s
held-out monitor:
    active=none
    completed_attempts=34
    verified=34
    integrity_failures=none

semantic preparation:
    prepared blinded cases: 30 / 30
    model inference launched: 0

semantic status:
    prepared_cases=30
    logical_passes=0/60
    completed_cases=0/30
    manual_cases=0
    provider_calls=0
    next=case-0586d0f63f905bd0 pass 1
```

The earlier blind-ID unit-test failure was a false positive caused by a random hexadecimal digest containing the substring `b0`; only that test was corrected. Production semantic-supervisor code and prepared evidence packets were unchanged.

Detailed records:

```text
docs/checkpoints/087_blinded_semantic_judge_supervisor_implemented_pending_preflight.md
docs/checkpoints/088_semantic_judge_preflight_caught_false_positive_blind_id_test.md
docs/checkpoints/089_blinded_semantic_preflight_passed_and_judge_execution_authorized.md
```

At the current boundary:

```text
prepared blinded cases: 30 / 30
held-out semantic logical passes persisted: 0 / 60
held-out semantic provider calls launched: 0
condition decoder inspected: no
condition-level semantic comparison performed: no
```

## Next experimental stage

Do not run any further B0, B1, or P0 held-out treatment attempt.

The preregistered blinded semantic evaluation is now authorized. From `prototype_v0/` run:

```bash
python -m ads_v0.semantic_judge_supervisor run-batch --max-judge-calls 180
```

The bound of 180 is the absolute operational ceiling implied by 60 required logical passes and at most three provider attempts per logical pass. It is not a target. With no provider failures, 60 calls should complete the judge stage.

The supervisor persists each usable logical pass immediately, never reruns a completed pass because of its score, remains condition-blind, and produces one blinded review ZIP. It stops on `JUDGE_COMPLETE`, provider-attempt exhaustion for a logical pass, the explicit call bound, or another safety state.

After the batch stops:

```text
1. review the blinded export only;
2. manually adjudicate any required 0-vs-2 or SC disagreements while still blind;
3. freeze all blinded consensus/adjudication results;
4. only then use the private decoder;
5. calculate H1, H2, and pooled B0/B1/P0 comparisons;
6. apply the preregistered continuation/falsification criteria;
7. record the final V0 interpretation.
```

No unblinded semantic comparison may occur before blinded consensus and required adjudication are frozen.

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
docs/checkpoints/089_blinded_semantic_preflight_passed_and_judge_execution_authorized.md
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

**Run the authorized condition-blind semantic-judge batch. Do not inspect the private decoder or perform condition-level semantic comparison until blinded consensus and any required manual adjudications are frozen.**
