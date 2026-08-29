# Continuity

**Status:** Current canonical continuity procedure  
**Aligned development-method version:** 0.6  
**Last reviewed:** 2026-08-29

## Purpose

This document defines how the Autonomous Data Science System project continues across chats, sessions, models, branches and context boundaries.

> A new collaborator must be able to reconstruct current project state from persistent repository artifacts without requiring the previous conversation or relying on model memory.

Long conversations are temporary working environments. Important knowledge must be durable, discoverable, correctly classified and routed to the right authority layer.

## Repository authority

The repository remains the durable source of truth whether the active collaborator is ChatGPT, Claude, a future model or the human project owner.

Conversation history may help, but must not override repository state. If repository artifacts disagree, resolve through status, scope, chronology, supersession and accepted authority. If material ambiguity remains, surface it explicitly rather than guessing.

## Interaction/session naming

Shared project/workspace:

```text
Autonomous Data Science System
```

Visible conversations use:

```text
NN - Main Topic / Stage
```

Provider-local repository session IDs allow independent rotation:

```text
ChatGPT  chatgpt-10  10 - Project Cockpit Design Exploration
Claude   claude-01   01 - ADS Development Review & Collaboration
```

Canonical naming/provenance rules:

```text
docs/model_collaboration/INTERACTION_PROVENANCE_AND_NAMING.md
```

Session identity is provenance/navigation metadata, not project authority.

## Proactive rotation

Rotate a conversation before context quality becomes fragile. Typical signals include very long design sequences, repeated reconstruction difficulty, context-window warnings, or a natural stage boundary.

Before planned rotation:

1. preserve any meaningful checkpoint/open review state;
2. update current routing if the boundary changed;
3. ensure new durable knowledge is routed in the Knowledge Map when warranted;
4. preserve exact branch/commit/test/review state needed for continuation;
5. start the next conversation with the standardized reconstruction prompt.

If the boundary is unexpected, reconstruct from the repository first and repair stale routing/provenance only after determining what actually survived.

## Required new-session reconstruction

A new session should not begin by reading arbitrary recent files or trusting prior chat memory.

Read in this order:

1. `README.md`
2. `docs/CURRENT_STATE.md`
3. `docs/KNOWLEDGE_MAP.md`
4. `docs/current_routing.json`
5. governing canonical documents/specifications pointed to by the current route
6. the current checkpoint/research boundary
7. specialized ledgers/manifests for the active topic

Then use the **Evergreen topic library** in `docs/KNOWLEDGE_MAP.md` to retrieve any broader knowledge relevant to the task without needing to remember document numbers.

This is important because current-state routing and historical/domain discovery are different jobs.

## Knowledge Map continuity contract

`docs/KNOWLEDGE_MAP.md` must always retain:

```text
Current continuation route
    exact active state and next reading

Evergreen topic library
    topic -> canonical/deep/evidence/specialized sources across the project
```

Current-stage work may update the continuation route, but must not replace the evergreen library.

Structural integrity is checked by:

```text
scripts/check_knowledge_map.py
.github/workflows/knowledge-map-integrity.yml
```

The map is navigation, not an authority database. A session still reasons from document status, scope, chronology and accepted contracts.

## Standard continuation prompt

The normal new-session prompt remains intentionally provider-neutral and stable:

> Continue the Autonomous Data Science System project from the repository. Treat the repository as the source of truth, not prior chat memory. First read README.md, docs/CURRENT_STATE.md, docs/KNOWLEDGE_MAP.md, and the governing documents they point to for the active stage. Reconstruct where the project currently stands, the important accepted conclusions and unresolved questions, and the next legitimate step. Follow the project's development/preservation method. Do not make changes yet; first align with me on the current state.

The collaborator should then use the evergreen topic library to expand beyond the immediate boundary when the task touches older or adjacent knowledge.

## Continuity across branches

Always distinguish:

```text
active development branch
promoted integration branch
main/default branch
historical experiment branches
```

The current branch and promoted integration SHA are recorded in:

```text
docs/current_routing.json
README.md
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
```

A new collaborator must not silently switch branches based on model memory.

## Checkpoint continuity

Checkpoints preserve meaningful project-state boundaries, not every commit.

Under Development Method v0.6, micro-iterations within one open review question are normally aggregated. Git preserves the exact implementation sequence; the checkpoint preserves the meaningful state transition.

When continuing an open checkpoint, distinguish:

```text
still same review question
    bounded update/iteration may remain inside that checkpoint boundary

review interpretation/status/continuation changed materially
    create a new checkpoint
```

Historical closed checkpoints remain immutable except for explicit provenance/metadata repair that does not rewrite substantive history.

## Verification continuity

A new session must know not only whether tests passed, but **what verification tier actually ran**.

Preserve when relevant:

```text
verification tier  V0 / V1 / V2 / V3 / V4
exact tests/workflow run
implementation target SHA
human-review status
whether a broader gate is still required before acceptance/promotion
```

Never describe a V1 targeted or V2 subsystem pass as a complete V3 Cockpit pass.

Risk-scaled verification is governed by `docs/DEVELOPMENT_METHOD.md`.

Cockpit selector/workflow:

```text
scripts/select_cockpit_verification.py
.github/workflows/cockpit-reintegration-fidelity.yml
```

## Model-collaboration continuity

When a collaboration thread is active, reconstruct it from:

```text
docs/model_collaboration/threads/<THREAD>/STATE.json
docs/model_collaboration/threads/<THREAD>/THREAD.md
docs/model_collaboration/REVIEW_INBOX.md
```

Important continuity fields include task owner, target-state writer, next expected actor, independence/exposure status, frozen review base, allowed secondary write surfaces and unresolved obligations.

A review tied to one immutable target must not be silently applied to a newer descendant.

Canonical collaboration method:

```text
docs/model_collaboration/README.md
docs/model_collaboration/DEFERRED_REVIEW_AND_CATCHUP.md
```

## Recovery after unplanned context loss

When a chat ends unexpectedly:

1. identify the active repository/branch;
2. read current routing and the latest checkpoint rather than assuming the final chat message committed successfully;
3. inspect recent Git chronology when needed;
4. separate implementation state from documentation/provenance state;
5. detect stale routing/session metadata;
6. preserve the exact surviving product/experiment boundary;
7. repair continuity metadata conservatively;
8. do not recreate substantive decisions from memory if the repository already contains stronger evidence.

Important distinction:

```text
substantive preservation failure
    knowledge/implementation actually missing

routing/provenance drift
    knowledge exists but current pointers/session metadata are stale
```

The second should be repaired, not treated as lost knowledge.

## Periodic reconciliation

At meaningful stage boundaries, verify:

```text
README / CURRENT_STATE / current_routing agree
KNOWLEDGE_MAP current route is accurate
KNOWLEDGE_MAP evergreen topic coverage is still broad
important new research/specifications are discoverable by topic
canonical docs have not become stale
specialized ledgers remain linked
interaction session metadata is current
checkpoint metadata passes
collaboration obligations are discoverable
verification tier/status is represented accurately
```

Do not run this whole reconciliation after every small implementation commit.

## Current exact continuation

Current repository context:

```text
branch               v1-cockpit-design-exploration
checkpoint           265
interaction session  chatgpt-10
conversation title   10 - Project Cockpit Design Exploration
latest specification Specification 024
```

Checkpoint 265 changes the development method and knowledge-routing architecture. It does not change the active Cockpit product decision.

The current product human-review gate remains Checkpoint 264:

```text
General project discussion
    same visible footprint as WorkUnit boxes
    selected frame on visible project box only

WorkUnit conversations
    selected frame on visible WorkUnit surface only
```

After that is confirmed, resume Checkpoint 258 / Research 097 Adaptive Conversation Dock review.

## Version relationship

Development Method v0.6 strengthens continuity by:

- restoring an evergreen global topic library;
- making that library part of standard reconstruction;
- preserving verification-tier semantics across sessions;
- aggregating micro-iterations within meaningful review boundaries;
- correcting current provider-neutral interaction identity;
- retaining repository-first reconstruction after unexpected chat boundaries.

Deep preservation rationale remains in:

```text
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
docs/research/064_rapid_iteration_repository_preservation_audit_and_checkpoint_hygiene.md
docs/research/103_repository_knowledge_discoverability_and_risk_scaled_verification_audit.md
```
