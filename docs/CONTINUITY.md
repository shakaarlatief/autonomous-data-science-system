# Continuity

**Status:** Current canonical continuity procedure  
**Aligned development-method version:** 0.7  
**Last reviewed:** 2026-08-30

## Purpose

This document defines how the Autonomous Data Science System project continues across chats, sessions, models, branches and context boundaries.

> A new collaborator must be able to reconstruct current project state from persistent repository artifacts without requiring the previous conversation or relying on model memory.

Long conversations are temporary working environments. Important knowledge must be durable, discoverable, correctly classified and routed to the right authority layer.

## Repository authority

The repository remains the durable source of truth whether the active collaborator is ChatGPT, Claude, a future model or the human project owner.

Conversation history may help, but must not override repository state. If repository artifacts disagree, resolve through status, scope, chronology, supersession and accepted authority. If material ambiguity remains, surface it explicitly rather than guessing.

## Separation of continuity concerns

Continuity should reconstruct state from dedicated owners rather than duplicating volatile information inside this procedure:

```text
docs/README.md
    what repository/document families exist and what each is for

docs/current_routing.json
    compact machine-readable current pointer

docs/CURRENT_STATE.md
    current human-readable state and exact next step

docs/KNOWLEDGE_MAP.md
    evergreen subject library for broader/older knowledge
```

This file explains **how to use those surfaces**. It should not carry a copied current checkpoint, branch, review gate or latest test run.

## Interaction/session naming

Visible conversations use:

```text
NN - Main Topic / Stage
```

Provider-local repository session IDs may use forms such as:

```text
chatgpt-10
claude-01
```

Canonical naming/provenance rules live in:

```text
docs/model_collaboration/INTERACTION_PROVENANCE_AND_NAMING.md
```

Session identity is provenance/navigation metadata, not project authority.

### Automatic new-session allocation

Every newly opened persistent ADS conversation is a new interaction session for provenance, including a conversation opened only because the previous one hit a length/context limit while the underlying project stage remains unchanged.

A new session must **not** inherit the previous conversation's provider-local session ID or visible conversation title merely because `CURRENT_STATE.md` still records that previous session at reconstruction time.

During repository-first reconstruction of a new ADS conversation, the collaborator must proactively:

1. recognize that the interaction itself is new;
2. derive the next provider-local sequence number from the latest durable interaction provenance for that environment;
3. establish a fresh `NN - Main Topic / Stage` title based on the active work reconstructed from the repository;
4. use that new session identity in the conversation immediately rather than continuing under the prior title;
5. once project-state alignment/authorization permits repository writes, update the live interaction context in `CURRENT_STATE.md` before substantive new durable work is attributed to the session.

The human project owner should not need to remind the collaborator to rotate the session ID/title after opening a continuation chat. This is part of the reconstruction procedure itself.

If the product UI cannot be renamed programmatically by the active tool surface, the repository must still establish and use the correct canonical title immediately; the UI limitation must never be used as a reason to reuse stale session provenance.

## Required new-session reconstruction

A new session should not begin by reading arbitrary recent files or trusting prior chat memory.

Read in this order:

1. `README.md`
2. `docs/README.md`
3. `docs/current_routing.json`
4. `docs/CURRENT_STATE.md`
5. `docs/KNOWLEDGE_MAP.md`
6. governing canonical documents/specifications routed by the current state
7. the current checkpoint/research boundary
8. specialized ledgers/manifests for the active topic

Then use the subject library in `docs/KNOWLEDGE_MAP.md` to retrieve broader knowledge relevant to the task without needing to remember document numbers.

Structural reconstruction and semantic retrieval are deliberately separate jobs:

```text
docs/README       structure -> artifact role
CURRENT_STATE     live state -> next action
KNOWLEDGE_MAP     subject -> relevant knowledge
```

The automatic new-session allocation rule above is part of this reconstruction. The prior session metadata found in `CURRENT_STATE.md` is evidence about the previous interaction, not permission to reuse it in the newly opened conversation.

## Standard continuation prompt

A provider-neutral continuation prompt may use:

> Continue the Autonomous Data Science System project from the repository. Treat the repository as the source of truth, not prior chat memory. First read README.md, docs/README.md, docs/current_routing.json, docs/CURRENT_STATE.md, and docs/KNOWLEDGE_MAP.md. Reconstruct where the project currently stands, the important accepted conclusions and unresolved questions, and the next legitimate step. Treat this conversation as a new interaction session: proactively establish the next provider-local session ID and a fresh `NN - Main Topic / Stage` title from the active repository state instead of reusing the previous session's title. Follow the project's development/preservation method. Do not make substantive project changes yet; first align with me on the current state.

The collaborator should expand through the Knowledge Map whenever the task touches older or adjacent knowledge.

## Proactive conversation rotation

Rotate a conversation before context quality becomes fragile. Typical signals include very long design sequences, repeated reconstruction difficulty, context-window warnings, or a natural stage boundary.

Before planned rotation:

1. preserve any meaningful checkpoint/open review state;
2. update `current_routing.json` and `CURRENT_STATE.md` if the live boundary changed;
3. ensure new durable knowledge is routed in the Knowledge Map when warranted;
4. preserve exact branch/commit/test/review state needed for continuation in the live state or governing evidence;
5. start the next conversation with repository-first reconstruction and automatic fresh session/title allocation.

If the boundary is unexpected, reconstruct from the repository first, allocate the new interaction identity, and repair stale routing/provenance only after determining what actually survived.

## Continuity across branches

Always distinguish:

```text
active development branch
promoted integration branch
main/default branch
historical experiment branches
```

The live branch/promotion pointer belongs in `docs/current_routing.json` and is explained in `docs/CURRENT_STATE.md`. Do not copy it into stable navigation documents unless a historical record specifically needs that exact context.

A new collaborator must not silently switch branches based on model memory.

## Checkpoint continuity

Checkpoints preserve meaningful project-state boundaries, not every commit.

Under Development Method v0.7, micro-iterations within one open review question are normally aggregated. Git preserves the exact implementation sequence; the checkpoint preserves the meaningful state transition.

When continuing an open checkpoint, distinguish:

```text
still the same review question
    bounded update/iteration may remain inside that checkpoint boundary

review interpretation/status/continuation changed materially
    create a new checkpoint
```

Historical closed checkpoints remain immutable except for explicit provenance/metadata repair that does not rewrite substantive history.

Checkpoint roles and metadata are defined by `docs/checkpoints/README.md`.

## Knowledge continuity

The global Knowledge Map is an evergreen semantic library, not a second current-state file.

Its continuity contract is:

```text
every numbered Foundation      routed to >=1 subject
every numbered Specification   routed to >=1 subject
every numbered Research record routed to >=1 subject
every numbered checkpoint      covered by >=1 semantic checkpoint range
important specialized indexes  remain globally reachable
```

A source may belong to multiple subjects. This is desirable when it improves retrieval.

Structural integrity is checked by:

```text
scripts/check_knowledge_map.py
.github/workflows/knowledge-map-integrity.yml
```

The map is navigation, not an authority database. A session still reasons from document status, scope, chronology and accepted contracts.

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

Never describe a V1 targeted or V2 subsystem pass as a complete V3 integrated pass.

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

1. identify the repository and likely active branch;
2. read the structural guide, current routing and current state;
3. establish a fresh provider-local interaction-session ID and conversation title for the newly opened recovery chat instead of reusing the ended session's metadata;
4. verify the current checkpoint exists rather than assuming the final chat message committed successfully;
5. inspect recent Git chronology when needed;
6. separate implementation state from documentation/provenance state;
7. detect stale routing/session metadata;
8. use the Knowledge Map to reconstruct older governing knowledge by subject;
9. preserve the exact surviving product/experiment boundary;
10. repair continuity metadata conservatively;
11. do not recreate substantive decisions from memory if the repository already contains stronger evidence.

Important distinction:

```text
substantive preservation failure
    knowledge/implementation actually missing

routing/provenance drift
    knowledge exists but discovery or current pointers are stale
```

The second should be repaired, not treated as lost knowledge.

## Periodic reconciliation

At meaningful stage boundaries, verify separately:

```text
CURRENT_STATE / current_routing agree
root README remains stable and non-duplicative
docs/README still describes the actual repository artifact families
KNOWLEDGE_MAP retains exhaustive subject coverage
important new research/specifications/foundations are topic-routed
checkpoint ranges cover newly created checkpoint numbers
canonical docs have not become stale
specialized ledgers remain linked
interaction provenance is coherent
checkpoint metadata passes
collaboration obligations are discoverable
verification tier/status is represented accurately
```

Do not run the whole reconciliation after every small implementation commit.

## Version relationship

Development Method v0.7 strengthens continuity by giving each navigation surface one primary responsibility:

```text
structure     docs/README.md
live state    CURRENT_STATE.md + current_routing.json
subject map   KNOWLEDGE_MAP.md
procedure     CONTINUITY.md
method        DEVELOPMENT_METHOD.md
```

Deep preservation rationale remains in:

```text
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
docs/research/064_rapid_iteration_repository_preservation_audit_and_checkpoint_hygiene.md
docs/research/103_repository_knowledge_discoverability_and_risk_scaled_verification_audit.md
docs/research/104_repository_information_architecture_and_exhaustive_knowledge_routing_refinement.md
```
