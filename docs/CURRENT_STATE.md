# Current State

**Checkpoint:** 94  
**Date:** 2026-08-19  
**Development stage:** Prototype V0 treatment and semantic inference complete; blinded consensus frozen and independently verified; deterministic condition decoding pending  
**Resolved treatment slots:** 30 / 30  
**Semantic logical passes:** 60 / 60  
**Completed blinded semantic cases:** 30 / 30  
**Manual adjudication required:** 0 / 30  
**Execution mode:** no further treatment or semantic-judge inference is authorized for Prototype V0

## Current experiment

Prototype V0 asks:

> Can explicit project state, reusable knowledge activation, prospective safeguards, and dependency-aware repair make a strong LLM's data-science reasoning materially more reliable across a changing project than an equally capable simpler LLM workflow?

B1 remains the primary architectural control.

Frozen protocol:

```text
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
```

Detailed held-out ledger:

```text
docs/experiments/prototype_v0/HELD_OUT_STATUS.md
```

## Fixed treatment evidence

Held-out treatment execution is complete:

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
```

The registered continuation signal is already impossible on resource/completion outcomes alone:

```text
P0 completed within budget: 3 / 10
P0 budget-exhausted runs: 7 / 10
P0/B1 pooled median-token ratio: 2.160
```

Treatment completion provenance:

```text
docs/checkpoints/085_held_out_execution_complete_and_full_compact_export_verified.md
```

## Fixed semantic evidence

The preregistered two-pass semantic judge completed successfully:

```text
semantic batch: semantic-batch-20260819T121018Z
provider calls launched: 60
logical passes persisted: 60 / 60
completed blinded cases: 30 / 30
provider failures: 0
manual-adjudication cases: 0
stop reason: JUDGE_COMPLETE
```

Two-pass agreement over 300 ordinary semantic comparisons:

```text
exact agreement: 288 / 300 = 96.0%
adjacent disagreements: 12 / 300 = 4.0%
extreme 0-vs-2 disagreements: 0
```

Semantic-critical agreement:

```text
60 / 60 exact
SC1 consensus flags: 0 / 30
SC2 consensus flags: 0 / 30
```

No manual semantic adjudication is required.

Detailed provenance:

```text
docs/checkpoints/090_blinded_semantic_judge_execution_complete.md
```

## Blinded freeze complete

The user pulled the freeze/monitor implementation and validated it locally:

```text
pytest: 95 passed in 20.43s
semantic monitor: 60/60 passes, 30/30 cases, 0 manual, 60 provider calls
freeze verify: 30 cases, 60 passes, 0 manual cases, private decoder read=no
freeze status: FROZEN
```

Frozen semantic aggregate SHA-256:

```text
836a6677e2803338697395afea431de5af0fc8ece469940bb687855bf7ec0757
```

The uploaded frozen decoder-free ZIP was independently checked against its own freeze manifest:

```text
archive entries: 243
freeze-covered files: 242
file hash mismatches: 0
recomputed aggregate matches frozen aggregate: yes
private decoder included: no
```

Therefore the condition-blind evidence boundary is complete and condition decoding is now authorized.

Condition-blind aggregate semantic shape at freeze:

```text
S1 mean: 1.000
S2 mean: 1.650
S3 mean: 1.683
S4 mean: 1.033
S5 mean: 2.000
S6 mean: 2.000
S7 mean: 1.967
S8 mean: 1.967
S9 mean: 1.733
S10 mean: 1.900
blinded targeted mean: 1.660
strong-targeted-pass cases: 0 / 30
```

Freeze provenance:

```text
docs/checkpoints/092_blinded_semantic_consensus_freeze_implemented_pending_validation.md
docs/checkpoints/093_blinded_semantic_freeze_independently_verified_and_unblinding_authorized.md
```

## Deterministic post-freeze decoder

A reproducible decoder is now implemented:

```text
prototype_v0/src/ads_v0/semantic_judge_decode.py
prototype_v0/tests/test_semantic_judge_decode.py
```

It must first recompute the blinded freeze aggregate without reading `private_decoder.json`. Only after exact freeze agreement may it reveal the mapping.

The decoder then produces:

```text
30 run-level decoded rows
pooled B0/B1/P0 summaries
H1 and H2 summaries by condition
paired replicate-level targeted-score differences
critical-failure counts
completion/budget summaries
median resource ratios
registered continuation-component facts
```

It explicitly does not infer P0-internal architecture-specific clauses such as false blocking, broad reopening/over-invalidation, or held-out hard coding. Those remain a separate post-unblinding diagnostic stage.

Implementation provenance:

```text
docs/checkpoints/094_post_freeze_condition_decoder_implemented_pending_validation.md
```

## Next step

From the repository root, pull the latest decoder implementation, then from `prototype_v0/` run:

```bash
git pull origin main
pytest
python -m ads_v0.semantic_judge_decode verify-freeze
python -m ads_v0.semantic_judge_decode decode
```

Expected predecode freeze identity:

```text
836a6677e2803338697395afea431de5af0fc8ece469940bb687855bf7ec0757
```

The `decode` command is the first authorized read of the private condition mapping. It launches no model calls and does not modify frozen evidence.

Upload the resulting:

```text
semantic_judge_decoded_<timestamp>.zip
```

After decoded common semantic/mechanical outcomes are independently reviewed:

```text
1. determine the P0 versus B1 semantic reliability result;
2. inspect the separate P0 architecture diagnostics required by Foundation 012;
3. apply every continuation and strong-falsification clause;
4. record the final Prototype V0 classification;
5. decide what architecture, if any, should survive into the next system iteration.
```

## Execution and observability architecture

The project now uses the system-level principle:

```text
execution / reasoning
    -> persisted structured state or events
    -> read-only observability
    -> human interface
```

Canonical principle:

```text
docs/PRINCIPLES.md, P-022
```

Deep rationale:

```text
docs/foundations/016_execution_observability_separation.md
```

Prototype observers:

```text
prototype_v0/src/ads_v0/heldout_monitor.py
prototype_v0/src/ads_v0/semantic_judge_monitor.py
```

## Knowledge and continuity

Minimum reading for a future session:

```text
README.md
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
prototype_v0/README.md
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
docs/foundations/015_held_out_supervision_and_mechanical_verification_architecture.md
docs/foundations/016_execution_observability_separation.md
docs/experiments/prototype_v0/HELD_OUT_STATUS.md
docs/checkpoints/093_blinded_semantic_freeze_independently_verified_and_unblinding_authorized.md
docs/checkpoints/094_post_freeze_condition_decoder_implemented_pending_validation.md
```

## Current priority

**Validate and run the deterministic post-freeze decoder, then upload its compact decoded ZIP. No further treatment or semantic-judge inference is allowed.**
