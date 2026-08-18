# Continuity

**Status:** Current canonical continuity procedure  
**Aligned development-method version:** 0.3  
**Last reviewed:** 2026-08-18

## Purpose

This document defines how the Autonomous Data Science System project should continue across chats, sessions, models, or other context boundaries.

The central requirement is:

> **A new chat must be able to reconstruct the current project state from persistent repository artifacts without requiring the previous chat or relying on model memory.**

Long conversations are temporary working environments, not durable project storage.

Continuity therefore depends on more than preserving files. Important knowledge must also remain discoverable, correctly classified, and current.

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

A chat may contain many topics and many checkpoints while continuity remains healthy.

## When to start a new design chat

Opening a new chat is a continuity action, not a topic-management convention.

The AI design collaborator should proactively decide when rotation is warranted.

A new chat should normally be recommended only when one or more of the following become material:

- the active conversation is becoming long enough that context loss or compression is a realistic risk;
- earlier reasoning that is still needed is becoming difficult to retain or recover reliably;
- responses or tool interactions begin to show continuity degradation attributable to session length;
- a platform or model context boundary is approaching;
- or another practical session-boundary condition makes continuing less reliable than rotating cleanly.

A topic change, checkpoint, foundation, or implementation milestone is not by itself a reason to rotate.

The goal is to use a chat while it remains an effective working context without waiting until continuity has already failed.

## Proactive rotation procedure

When the AI decides that a new chat should be opened, it should normally:

1. preserve any important uncheckpointed reasoning;
2. perform the checkpoint promotion audit where appropriate;
3. ensure relevant canonical documents are current;
4. ensure `docs/KNOWLEDGE_MAP.md` routes to any newly important durable knowledge;
5. ensure `docs/CURRENT_STATE.md` is concise and current;
6. ensure detailed active-experiment status is current if the next session depends on it;
7. record the exact next step and material unresolved questions;
8. verify that the repository is sufficient for reconstruction without the current conversation;
9. tell the user that rotation is appropriate;
10. propose the next numbered, content-specific session title;
11. provide a minimal continuation prompt if useful.

The user should not need to summarize the previous chat manually.

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

For active Prototype V0 held-out work, the normal additional reading set is:

```text
prototype_v0/README.md
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
docs/experiments/prototype_v0/HELD_OUT_STATUS.md
```

If the current task concerns the broader system-level vision rather than only V0 execution, also read:

```text
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
```

The exact historical reading set should follow current routing rather than an obsolete fixed list of checkpoints.

## Required behavior after reading

Before continuing substantial work, the new session should be able to state:

- what the project is trying to build;
- what stage the project is in;
- what has already been decided;
- which ideas remain hypotheses rather than accepted architecture;
- what major questions remain open;
- what experiment or prototype is currently active, if any;
- what the exact next step is;
- and which documents govern that next step.

If repository documents are inconsistent, the session should identify the conflict rather than invent a reconciliation.

## Knowledge authority during reconstruction

The default authority order is:

```text
1. frozen specifications/contracts within their declared scope
2. current explicit decisions and canonical specifications
3. current vision/principles/current-state material
4. foundational design memos for rationale and durable hypotheses
5. checkpoints/session records for historical state
6. raw historical material for provenance
```

`docs/KNOWLEDGE_MAP.md` helps route to these sources but is not itself a replacement for them.

If a material conflict cannot be resolved by status, scope, or supersession information, it should become an explicit open question.

## Suggested new-chat prompt

A minimal continuation prompt is:

```text
Continue the Autonomous Data Science System project.
Read the repository state and the context required by CURRENT_STATE.md and KNOWLEDGE_MAP.md first.
Reconstruct where the project stands, distinguish accepted decisions from active hypotheses and historical material,
and continue from the recorded next step.
```

If the chat has direct repository access, it should read the files itself.

If direct repository access is unavailable, the relevant repository artifacts should be provided rather than relying on remembered summaries.

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

## Promotion and continuity

A checkpoint alone is not enough when the material has become important current knowledge.

A substantive checkpoint should therefore explicitly ask whether material should be promoted into:

```text
canonical documents
foundations
specifications/contracts
experiment ledgers
KNOWLEDGE_MAP
MAJOR_CHANGES
```

No promotion is a valid outcome.

This requirement exists because historically safe information can still become practically lost if future sessions do not know where to find it.

## End-of-session procedure

Before a substantial session is abandoned because of length, context limits, a deliberate stop, or another session boundary, the project should create a checkpoint when material work remains unpreserved.

The end-of-session process should normally include:

1. review what changed since the previous checkpoint;
2. update canonical documents where accepted knowledge changed;
3. record new decisions;
4. record unresolved questions;
5. preserve long-form reasoning if compression would lose important context;
6. record strong hypotheses without presenting them as settled;
7. complete the promotion audit;
8. update `KNOWLEDGE_MAP.md` when routing changed;
9. update the active experiment ledger when relevant;
10. update `CURRENT_STATE.md` with only the concise present-tense state;
11. record the exact next step;
12. list the documents a new session should read;
13. create a historical checkpoint/session record where useful.

The project does not need a checkpoint after every short conversation. The purpose is continuity, not bureaucracy.

## Current-state document requirements

`docs/CURRENT_STATE.md` should remain concise compared with foundations, checkpoints, and experiment ledgers.

It should answer:

```text
What are we building?
What development stage are we in?
What current conclusions or constraints materially affect the next step?
What is the exact current priority?
What should happen next?
What must a future session read?
```

It should not contain a growing duplicate of every run, checkpoint, or foundation.

Detailed long-running experiment mechanics should live in experiment-specific status documents.

For Prototype V0:

```text
docs/experiments/prototype_v0/HELD_OUT_STATUS.md
```

## Knowledge map requirements

`docs/KNOWLEDGE_MAP.md` should remain a routing layer, not another foundation.

It should be updated when:

- an important new foundation is created;
- a checkpoint is promoted into a durable source;
- a canonical document changes role;
- an experiment-specific ledger is introduced or retired;
- a source becomes superseded;
- or a future session would otherwise be likely to look in the wrong place.

Routine checkpoint creation does not automatically require a knowledge-map update.

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
major experimental phase/frozen contract
repository structure that changes how future work should operate
```

It is not a replacement for Git history or checkpoints.

## Knowledge reconciliation

At meaningful stage boundaries, the project should perform the reconciliation process defined in `DEVELOPMENT_METHOD.md`.

The continuity-specific goal is to verify that a new session can find the correct current knowledge without depending on historical-memory luck.

A reconciliation should therefore verify at minimum:

```text
CURRENT_STATE is concise and current;
KNOWLEDGE_MAP routes correctly;
important accepted decisions are recorded;
OPEN_QUESTIONS does not contain obviously stale priorities;
important recent checkpoint insights were promoted if warranted;
active experiment ledgers are current;
major structural changes are discoverable.
```

## Deferred future continuity tooling

The current continuity substrate remains Git + Markdown + explicit repository structure.

Future versions may introduce machine-readable metadata, semantic retrieval, generated indexes, dependency graphs, automated reconciliation proposals, or raw-conversation provenance archives.

Those options are preserved in Foundation 014 but remain deferred until observed scale or consistency problems justify them.

## Version relationship

The current continuity procedure is aligned with Development Method version 0.3.

The major methodological progression is:

```text
v0.1
layered durable preservation and explicit new-chat reconstruction

v0.2
proactive checkpoint detection and proactive chat rotation

v0.3
promotion audit + knowledge map + reconciliation + authority metadata
+ concise current state + experiment ledgers + major-changes history
```

Detailed preservation rationale:

```text
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
```
