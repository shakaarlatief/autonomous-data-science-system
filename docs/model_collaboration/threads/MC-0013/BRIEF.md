# MC-0013 Brief: Independent Project-Knowledge Architecture Counter-Design

**Thread:** MC-0013
**Date opened:** 2026-09-13
**Review mode:** INDEPENDENT_THEN_COMPARATIVE
**Coordination branch:** `v1-source-vault-bootstrap-resume`
**Independent substantive base:** `233eb932062a24473fcc4f4fe93160c952eea426`
**Claude interaction:** `claude-03`
**Claude conversation title:** `03 - Project Knowledge Architecture Foundations and Design Method`
**Authority:** Collaboration evidence only. Requirements V0.2 remain the frozen candidate-acceptance authority. This thread cannot select a target architecture, amend requirements or authorize migration.
**Purpose:** Obtain an independent Claude architecture synthesis from the full Research 124 evidence field before exposing ChatGPT's first candidate-family synthesis, then use a later comparative phase to challenge and reconcile the designs.

## 1. Independence rationale

Research 124 has completed the empirical baseline, D1-D8 external evidence, requirements reconciliation, owner-source evaluation and cross-model ICM reconciliation. ChatGPT has now begun its first architecture-family synthesis, but that candidate content must remain hidden during Claude's first architecture-design pass.

Claude already knows the Research 124 evidence program through MC-0012, including ICM. The independence sought here is therefore **candidate-design independence**, not evidence blindness.

The substantive design base is frozen at:

```text
233eb932062a24473fcc4f4fe93160c952eea426
```

This exact commit contains the complete accepted evidence boundary through Research 132 / Checkpoint 474 and predates ChatGPT's first architecture-family synthesis.

## 2. Current-branch routing boundary

From current `v1-source-vault-bootstrap-resume`, Claude may read only the routing surfaces needed to locate this obligation:

```text
docs/current_routing.json
docs/model_collaboration/REVIEW_INBOX.md
docs/model_collaboration/threads/MC-0013/BRIEF.md
docs/model_collaboration/threads/MC-0013/THREAD.md
docs/model_collaboration/threads/MC-0013/STATE.json
```

All substantive project/evidence reads for the independent design must come from exact commit `233eb932062a24473fcc4f4fe93160c952eea426`.

Do **not** inspect descendant candidate-design content before Message 001 is frozen. In particular, do not read:

```text
docs/research/133_candidate_architecture_family_synthesis_and_falsification_frame.md
Checkpoint 475 or later checkpoint bodies
Research 124 sections added after the frozen base
current CURRENT_STATE synthesis added after the frozen base
```

If descendant candidate content is exposed unexpectedly, stop and report `INDEPENDENT_DESIGN_CONTAMINATED` rather than continuing as though the exposure had not happened.

## 3. Governing evidence to use

At the exact frozen base, reconstruct the architecture problem from the strongest sources. At minimum use:

```text
docs/research/PROJECT_KNOWLEDGE_ARCHITECTURE_REQUIREMENTS_V02.md
docs/research/124_scalable_repository_knowledge_architecture_and_reconstruction_redesign.md
docs/research/126_knowledge_identity_and_multi_axis_organization_deep_dive.md
docs/research/127_capture_consolidation_promotion_and_source_derived_state_deep_dive.md
docs/research/128_authority_activation_and_temporal_supersession_deep_dive.md
docs/research/129_consolidation_fidelity_provenance_and_maintenance_economics_deep_dive.md
docs/research/130_requirements_evidentiary_provenance_reconciliation.md
docs/research/131_owner_provided_icm_source_incremental_evaluation.md
docs/research/132_cross_model_icm_reconciliation_and_architecture_synthesis_readiness.md
docs/research/PROJECT_KNOWLEDGE_FAILURE_CORPUS.md
```

Use MC-0011 / MC-0012 material where it materially helps, especially Claude's own prior reasoning and the corrected density/granularity finding. Read additional frozen-base artifacts as needed.

Do not restart broad external research. If a genuine evidence gap blocks an architecture decision, identify it as a gap and explain what decision it blocks.

## 4. Independent architecture-design task

Reason from first principles and from the frozen requirements, not from the current repository's artifact families. The output should be architecture synthesis, not a technology shopping list and not a shallow scorecard tournament.

Address at least:

1. What semantic/functional responsibilities are unavoidable across any credible successor? Distinguish required semantics from optional physical components.
2. Which responsibilities need deterministic/project-controlled structure, which can live primarily in rich human-readable knowledge, and which may safely be derived probabilistically?
3. Construct several **materially different coherent architecture families**. Differences should concern authority model, semantic identity, current/history representation, lifecycle, workstream/control state, relation ownership, derived views or another deep axis, not cosmetic storage substitutions.
4. For each serious family, explain source of truth, write path, identity model, relationship model, reconstruction path, authority resolution, workstream continuation, capture/promotion, derived state, active-surface control, main lifecycle costs and strongest failure mode.
5. Identify any architecture conclusion that is effectively forced by V0.2 even though no mechanism is selected.
6. Identify attractive mechanisms that should remain optional because evidence does not justify universalizing them.
7. State the strongest architecture hypothesis you would currently take forward for deeper design, **without treating it as selected**, and state why it may be wrong.
8. Identify the cheapest high-information falsification probes that would distinguish the strongest competing hypotheses before major implementation.
9. Explicitly consider the named remaining risks from Research 132: identity merge/split governance, single-model baseline limitation, KA-R07 discovery circularity, evidence-class visibility, dispatch reliability, `C_failure`, and observability bias against simpler candidates.
10. Explain where ICM-derived mechanisms fit and where they do not. Do not privilege ICM because it was owner-provided.
11. Preserve architecture freedom around files, structured text, relational storage, static graphs, graph databases, event-oriented models, retrieval-first systems and hybrids unless evidence actually excludes them.
12. End with a clear judgment on what should happen after the independent design is frozen: direct comparative review, a mechanism probe first, or another bounded step.

You may disagree with V0.2 only by identifying an actual requirement defect. Do not silently weaken a requirement because it makes a candidate harder to design.

## 5. Required output

Write exactly one independent response at:

```text
docs/model_collaboration/threads/MC-0013/messages/001_claude_independent_architecture_counter_design.md
```

Include normal collaboration provenance plus:

```text
independence / contamination statement
strongest architecture hypothesis
strongest competing alternative
strongest failure mode of your own preferred hypothesis
what evidence would make you change your position
```

## 6. Write scope

Claude may write only:

```text
docs/model_collaboration/threads/MC-0013/messages/**
```

Do not modify Research 124, Requirements V0.2, routing, checkpoints, current state, implementation or canonical governance.

## 7. Phase transition

After Message 001 is committed and pushed, ChatGPT will inspect it independently against the frozen evidence. Only then will ChatGPT expose its own candidate-family synthesis for comparative review if that remains the highest-value next step.

```text
MC0013=OPEN
MODE=INDEPENDENT_THEN_COMPARATIVE
PHASE=INDEPENDENT_ARCHITECTURE_COUNTER_DESIGN
INDEPENDENT_BASE=233eb932062a24473fcc4f4fe93160c952eea426
CHATGPT_CANDIDATE_CONTENT=WITHHELD_UNTIL_MESSAGE_001_FROZEN
REQUIREMENTS_V02=FROZEN_UNCHANGED
TARGET_ARCHITECTURE=NOT_SELECTED
NEXT=CLAUDE_MESSAGE_001
```
