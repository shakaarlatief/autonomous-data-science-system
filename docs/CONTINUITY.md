# Continuity

**Status:** Current canonical continuity procedure  
**Aligned development-method version:** 0.4  
**Last reviewed:** 2026-08-22

## Purpose

This document defines how the Autonomous Data Science System project should continue across chats, sessions, models, or other context boundaries.

The central requirement is:

> **A new chat must be able to reconstruct the current project state from persistent repository artifacts without requiring the previous chat or relying on model memory.**

Long conversations are temporary working environments, not durable project storage.

Continuity therefore depends on more than preserving files. Important knowledge must also remain discoverable, correctly classified, current, and routed to the right authority layer.

---

## ChatGPT project and session naming

The current ChatGPT project is named:

```text
Autonomous Data Science System
```

Design chats use:

```text
NN - Main Topic / Stage
```

The number preserves chronology and the content-specific title makes earlier sessions easier to locate.

Session names are navigation and provenance metadata only. The repository must never depend on a chat retaining a particular title.

### Active development session

```text
Design session: 04
ChatGPT project: Autonomous Data Science System
Session title: 04 - Selective Context Promotion & Reasoning Vertical Slice
```

### Previous design sessions

```text
Design session: 03
Session title: 03 - Project Cockpit & V1 Integration

Design session: 02
Session title: 02 - Methodological Brain & Knowledge Units

Design session: 01
Session title: 01 - Foundations & Checkpoint 0
```

Every checkpoint created while this ChatGPT-based development process remains active must preserve the applicable:

```text
Design session
ChatGPT project
Session title
```

fields under `docs/checkpoints/README.md`.

Session provenance improves navigation and auditing, but repository state remains the source of truth across sessions.

---

## Why Session 04 exists

Session 03 reached the platform conversation-length limit immediately after the first RH-C selective-context result had been preserved.

The substantive work survived in:

```text
docs/research/020_first_horizon_relevance_and_selective_context_gate_design.md
docs/specifications/013_v1_horizon_relevance_and_selective_context.md
docs/checkpoints/142_relevance_and_selective_context_contract_frozen.md
experiments/retrieval/V1_SELECTIVE_CONTEXT_RESULT.md
```

The implementation and cross-platform result were therefore recoverable from the repository.

However, the boundary occurred before the normal promotion/reconciliation sequence was complete. At the start of Session 04:

```text
CURRENT_STATE still pointed to Checkpoint 141 and PR #10
KNOWLEDGE_MAP still routed through the pre-RH-C state
README still described RH-C as future work
OPEN_QUESTIONS still treated selective context as unvalidated
VISION contained stale current-implementation wording
MAJOR_CHANGES had not recorded the dense -> hybrid -> Horizon -> selective-context progression
Specification 013 remained frozen v0.1 despite a successful gate
PR #11 still described a future result rather than the measured outcome
```

Checkpoint 143 records the Session 04 recovery and promotion decision.

This is the same important distinction first exposed at the Session 02 -> Session 03 boundary:

```text
substantive preservation failure
    !=
routing/current-state reconciliation drift
```

The current project method should continue to preserve substantive research/specification/checkpoint/result artifacts before cosmetic or routing cleanup when a session is already near a hard boundary.

---

## When to start a new design chat

Opening a new chat is a continuity action, not a topic-management convention.

The AI design collaborator should proactively decide when rotation is warranted.

A new chat should normally be recommended when one or more of the following become material:

- the active conversation is becoming long enough that context loss or compression is a realistic risk;
- earlier reasoning that is still needed is becoming difficult to retain or recover reliably;
- responses or tool interactions begin to show continuity degradation attributable to session length;
- a platform or model context boundary is approaching;
- or another practical session-boundary condition makes continuing less reliable than rotating cleanly.

A topic change, checkpoint, foundation, or implementation milestone is not by itself a reason to rotate.

The goal is to use a chat while it remains an effective working context without waiting until continuity has already failed.

---

## Proactive rotation procedure

When the AI decides that a new chat should be opened, it should normally:

1. preserve important uncheckpointed reasoning;
2. perform the checkpoint promotion audit where appropriate;
3. ensure relevant canonical documents are current;
4. ensure `docs/KNOWLEDGE_MAP.md` routes to newly important durable knowledge;
5. ensure `docs/CURRENT_STATE.md` is concise and current;
6. ensure detailed active-experiment status is current if the next session depends on it;
7. record the exact next step and material unresolved questions;
8. verify that the repository is sufficient for reconstruction without the current conversation;
9. tell the user that rotation is appropriate;
10. propose the next numbered, content-specific session title;
11. use the standardized continuation prompt below.

The user should not need to summarize the previous chat manually.

---

## Unplanned session-boundary recovery

A session may end before the proactive rotation procedure can finish. Examples include:

```text
unexpected conversation-length limit
client/session failure
model/tool interruption
browser/session loss
other hard platform boundary
```

When this happens, the next session should **not** recreate missing context from memory or assume that the most prominent canonical document is necessarily the newest artifact.

The recovery procedure is:

1. identify the active repository branch or worktree from Git/GitHub evidence;
2. read `README.md`, `CURRENT_STATE.md`, and `KNOWLEDGE_MAP.md` from that branch;
3. inspect the latest checkpoints, specifications, research files, experiment results, PR state, and commits created near the boundary;
4. compare their authority/status metadata with any older canonical wording;
5. identify exactly which knowledge was preserved and which routing/current-state updates were interrupted;
6. reconstruct substantive state from repository authority, not prior-chat recollection;
7. repair stale canonical/routing documents conservatively without rewriting historical checkpoint conclusions;
8. reconcile `OPEN_QUESTIONS` when old experiment status has become materially stale;
9. update active session provenance for the new chat;
10. create a continuity/reconciliation checkpoint if the repair is substantive;
11. continue from the newest legitimate implementation/design boundary.

A useful distinction is:

```text
substantive preservation failure
    important reasoning was never persisted

versus

routing/reconciliation failure
    important reasoning was persisted but CURRENT_STATE / KNOWLEDGE_MAP /
    other current indexes lagged
```

Session 02 -> Session 03 and Session 03 -> Session 04 both validated the second recovery path.

---

## New-session start procedure

A new design session should reconstruct the project from repository state before beginning substantial new reasoning.

### Minimum reading order

1. `README.md`
2. `docs/CURRENT_STATE.md`
3. `docs/KNOWLEDGE_MAP.md`
4. `docs/VISION.md`
5. `docs/PRINCIPLES.md`
6. `docs/DECISIONS.md`
7. `docs/OPEN_QUESTIONS.md`
8. `docs/DEVELOPMENT_METHOD.md`
9. `docs/CONTINUITY.md`

Then follow the routing and explicit read instructions in `CURRENT_STATE.md` and `KNOWLEDGE_MAP.md`.

If active work is on a feature branch, the session must first verify that it is reading the branch that actually contains the latest checkpoints and specifications. The default branch must not be assumed to be current merely because it is named `main`.

The current active branch relationship is maintained in `CURRENT_STATE.md` and `KNOWLEDGE_MAP.md` rather than duplicated permanently here.

---

## Required behavior after reading

Before continuing substantial work, the new session should be able to state:

- what the project is trying to build;
- what stage the project is in;
- what has already been decided;
- which ideas remain hypotheses rather than accepted architecture;
- what major questions remain open;
- what experiment or implementation slice is currently active;
- what the exact next step is;
- which documents govern that next step;
- and whether any canonical/routing documents lag newer higher-relevance repository evidence.

If repository documents are inconsistent, the session should identify the conflict rather than invent a reconciliation.

---

## Knowledge authority during reconstruction

The default authority order is:

```text
1. frozen/accepted current specifications within their declared scope
2. current explicit decisions and accepted specifications
3. current vision/principles/current-state material
4. foundational design memos for rationale and durable hypotheses
5. research memos for current bounded design exploration
6. checkpoints/session records for historical state and human-review evidence
7. raw historical material for provenance
```

`docs/KNOWLEDGE_MAP.md` helps route to these sources but is not itself a replacement for them.

Candidate specifications deserve careful treatment: they can govern a bounded experiment by explicit checkpoint authority without becoming final architecture.

If a material conflict cannot be resolved by status, scope, chronology, or supersession information, it should become an explicit open question.

---

## Optional cross-session handoff verification

When the previous design session is still accessible after a new session has reconstructed repository state, an optional robustness check is to ask the previous session to independently review the reconstruction before substantial work continues.

This check is supplementary, not required. The previous chat is not an authority over the repository and continuity must not depend on it remaining available.

---

## Standardized new-chat prompt

When a new chat is opened for this project, the default first prompt is:

```text
Continue the Autonomous Data Science System project from the repository. Treat the repository as the source of truth, not prior chat memory. First read README.md, docs/CURRENT_STATE.md, docs/KNOWLEDGE_MAP.md, and the governing documents they point to for the active stage. Reconstruct where the project currently stands, the important accepted conclusions and unresolved questions, and the next legitimate step. Follow the project's development/preservation method. Do not make changes yet; first align with me on the current state.
```

This prompt is intentionally stable and generic. The user should not need to invent a custom handoff prompt for each session.

If the chat has direct repository access, it should read the files itself.

If direct repository access is unavailable, the relevant repository artifacts should be provided rather than relying on remembered summaries.

---

## Proactive preservation during a session

The user does not need to request every checkpoint explicitly.

The AI design collaborator should decide when preservation is warranted using `DEVELOPMENT_METHOD.md`.

The intended behavior is:

```text
continue freely while reasoning is developing
    -> detect a coherent conceptual or operational milestone
    -> create a checkpoint when warranted
    -> perform the promotion audit
    -> update durable knowledge/routing only when warranted
    -> resume from the recorded next step
```

Proactive preservation must preserve maturity distinctions. A compelling idea remains a design hypothesis until it has actually earned a stronger status.

When a conversation is already very long, preserving the substantive checkpoint/specification/result before continuing routing cleanup is preferable to delaying all preservation until one final batch.

---

## Promotion and continuity

A checkpoint alone is not enough when material has become important current knowledge.

A substantive checkpoint should explicitly ask whether material should be promoted into:

```text
canonical documents
foundations
research/specifications
experiment ledgers
KNOWLEDGE_MAP
MAJOR_CHANGES
```

No promotion is a valid outcome.

The requirement exists because historically safe information can still become practically lost if future sessions do not know where to find it.

---

## End-of-session procedure

Before a substantial session is deliberately abandoned because of length, a planned stop, or another known boundary, the project should create a checkpoint when material work remains unpreserved.

The end-of-session process should normally include:

1. review what changed since the previous checkpoint;
2. update canonical documents where accepted knowledge changed;
3. record new decisions where warranted;
4. record unresolved questions;
5. preserve long-form reasoning if compression would lose important context;
6. record strong hypotheses without presenting them as settled;
7. complete the promotion audit;
8. update `KNOWLEDGE_MAP.md` when routing changed;
9. update active experiment/status ledgers when relevant;
10. update `CURRENT_STATE.md` with concise present-tense state;
11. record the exact next step;
12. list the documents a new session should read;
13. update active session provenance where rotation is planned;
14. create a historical checkpoint/session record where useful;
15. verify the new-session reconstruction path before declaring handoff complete.

The project does not need a checkpoint after every short conversation. The purpose is continuity, not bureaucracy.

---

## Current-state document requirements

`docs/CURRENT_STATE.md` should answer:

```text
What are we building?
What development stage are we in?
What current conclusions or constraints materially affect the next step?
What is the exact current priority?
What should happen next?
What must a future session read?
```

It should remain concise compared with foundations, research, checkpoints, and experiment ledgers.

---

## Knowledge-map requirements

`docs/KNOWLEDGE_MAP.md` is a routing layer, not another foundation.

It should be updated when:

- an important new foundation/research/specification source is created;
- a checkpoint is promoted or becomes the latest human-review/result boundary;
- a canonical document changes role;
- an experiment-specific ledger is introduced or retired;
- a source becomes superseded;
- branch-local active work would otherwise be mistaken for default-branch state;
- or a future session would otherwise be likely to look in the wrong place.

Routine checkpoint creation does not automatically require a knowledge-map update.

---

## Major-changes ledger

`docs/MAJOR_CHANGES.md` records selective project-level structural changes.

It should be updated when a change materially alters:

```text
system-level vision
target architecture direction
prototype architecture
evaluation architecture
development methodology
knowledge-preservation architecture
major product interaction architecture
major experimental phase/frozen contract
repository structure that changes how future work should operate
```

It is not a replacement for Git history or checkpoints.

---

## Knowledge reconciliation

At meaningful stage boundaries, the project should perform the reconciliation process defined in `DEVELOPMENT_METHOD.md`.

A reconciliation should verify at minimum:

```text
README reflects the actual development stage;
CURRENT_STATE is concise and current;
KNOWLEDGE_MAP routes correctly;
important accepted decisions are recorded;
OPEN_QUESTIONS does not contain stale experiment status;
important recent checkpoint insights were promoted if warranted;
active experiment/status ledgers are current;
checkpoint/session provenance is current;
major structural changes are discoverable;
branch-local active work is not mistaken for stale default-branch state.
```

---

## Deferred future continuity tooling

The current continuity substrate remains Git + Markdown + explicit repository structure.

Future versions may introduce machine-readable metadata, semantic retrieval, generated indexes, dependency graphs, automated reconciliation proposals, or raw-conversation provenance archives.

Those options remain deferred until observed scale or consistency problems justify them.

---

## Version relationship

The current continuity procedure remains aligned with Development Method version 0.4.

The major methodological progression is:

```text
v0.1
layered durable preservation and explicit new-chat reconstruction

v0.2
proactive checkpoint detection and proactive chat rotation

v0.3
promotion audit + knowledge map + reconciliation + authority metadata
+ concise current state + experiment ledgers + major-changes history

v0.4
explicit checkpoint metadata contract + mechanical validation
+ normalized historical checkpoint provenance + required ChatGPT session provenance
```

The unplanned-boundary recovery procedure remains a continuity refinement within v0.4 rather than a separate development-method version.

Detailed preservation rationale:

```text
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
```
