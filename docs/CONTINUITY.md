# Continuity

## Purpose

This document defines how the Autonomous Data Science System project should continue across chats, sessions, models, or other context boundaries.

The central requirement is:

> **A new chat must be able to reconstruct the current project state from persistent repository artifacts without requiring the previous chat or relying on model memory.**

This requirement exists because long conversations are temporary working environments, not durable project storage.

## ChatGPT project and session naming

The current ChatGPT project is named:

`Autonomous Data Science System`

Design chats use a numbered, content-specific naming convention:

```text
NN - Main Topic / Stage
```

Examples:

```text
01 - Foundations & Checkpoint 0
02 - System Definition & Success Criteria
03 - Knowledge Architecture
```

The number preserves chronology. The content-specific title makes old sessions discoverable without requiring the user to remember which numbered chat contained a topic.

Session names are navigation and provenance metadata. The repository must never depend on a chat retaining a particular title.

If a session evolves beyond its initial title, checkpoints remain the authoritative record of the specific conceptual milestones reached inside that session. A chat may therefore contain more than one checkpoint.

## New-session start procedure

A new design session should begin by reading the repository rather than asking the user to manually restate the project.

### Minimum reading order

1. `README.md`
2. `docs/CURRENT_STATE.md`
3. `docs/VISION.md`
4. `docs/PRINCIPLES.md`
5. `docs/DECISIONS.md`
6. `docs/OPEN_QUESTIONS.md`
7. `docs/DEVELOPMENT_METHOD.md`
8. this file, `docs/CONTINUITY.md`

Then read the foundational or historical documents explicitly listed in `CURRENT_STATE.md` as relevant to the next step.

At Checkpoint 2, this includes:

- `docs/foundations/001_initial_vision_and_reasoning.md`
- `docs/foundations/002_epistemic_integrity_and_project_constitution.md`
- `docs/checkpoints/000_checkpoint_0.md`
- `docs/checkpoints/001_primary_purpose_and_project_intent.md`
- `docs/checkpoints/002_epistemic_integrity_and_project_constitution.md`

### Required behavior after reading

The new session should be able to state, before continuing substantial design work:

- what the project is trying to build;
- what stage the project is in;
- what has already been decided;
- which ideas are still hypotheses rather than accepted architecture;
- what major questions remain open;
- and what the recorded next step is.

If repository documents are inconsistent, the session should identify the conflict rather than invent a reconciliation.

## Suggested new-chat prompt

A minimal continuation prompt can be:

```text
Continue the Autonomous Data Science System project.
Read the repository state and the context required by CURRENT_STATE.md first.
Reconstruct where the project stands, distinguish accepted decisions from open hypotheses,
and continue from the recorded next step.
```

If the chat has access to the GitHub repository directly, the session should read the files itself.

If direct repository access is unavailable, the relevant files should be provided to the new session rather than relying on remembered summaries.

## Proactive preservation during a session

Beginning with continuity procedure version 0.2, the user does not need to request every checkpoint explicitly.

The AI design collaborator should decide when repository preservation is warranted, using the criteria in `DEVELOPMENT_METHOD.md`.

The intended behavior is:

```text
continue freely while reasoning is still developing
    -> detect when a coherent conceptual milestone has formed
    -> preserve it before the next major topic or before continuity risk grows
    -> resume discussion from the recorded next step
```

Proactive checkpointing must preserve maturity distinctions. A compelling idea should remain a design hypothesis unless it has actually reached the status required for a principle or decision.

## End-of-session procedure

Before a substantial session is abandoned because of length, context limits, a change of topic, or a deliberate stopping point, the project should create a checkpoint when the session contains material that has not yet been preserved.

The end-of-session process should normally include:

1. review what changed since the previous checkpoint;
2. update canonical documents where accepted knowledge changed;
3. record new decisions;
4. record unresolved questions;
5. preserve long-form reasoning if compression would lose important context;
6. record important design hypotheses without presenting them as settled;
7. update `CURRENT_STATE.md`;
8. record the exact next step;
9. list the documents a new session should read;
10. create a historical checkpoint or session record when useful.

The project does not need a checkpoint after every short conversation. The purpose is continuity, not bureaucracy.

## Current-state document requirements

`CURRENT_STATE.md` should remain relatively concise compared with foundational memos.

It should answer:

- What are we building?
- What development stage are we in?
- What principles or conclusions are currently established?
- What strong hypotheses are active but not yet validated?
- What has explicitly not been decided?
- What are we working on now?
- What should happen next?
- What must a future session read?

It should not become a duplicate of every other file.

## Conflict resolution across time

The project is expected to change.

Therefore, future sessions must distinguish current state from historical reasoning.

A practical priority order is:

1. current accepted decisions and current specifications;
2. current principles;
3. current-state summary;
4. foundational memos for detailed rationale;
5. checkpoints and session records for historical context;
6. raw archived conversations, if introduced later.

A historical memo can explain why a decision was originally made without implying that the decision is still current.

## Superseded material

When an important document or decision becomes outdated, it should not simply disappear if its history matters.

Prefer one of the following:

- mark the old item as superseded and link to the replacement;
- preserve the old version through Git history and document the replacement decision;
- move historical material to an archive if the active structure later requires it.

The exact archive strategy has not yet been standardized.

## Conversation capacity should not determine project quality

The project should behave as though any chat may eventually end.

Important reasoning should therefore be extracted before it becomes dependent on inaccessible context.

This does **not** mean constantly summarizing everything. It means making checkpointing a normal part of the development process.

## Model independence

Continuity should not depend on one specific LLM remembering prior conversations.

A future GPT, Claude, Gemini, open-source model, human collaborator, or other agent should be able to understand the project from the repository if given the appropriate access and instructions.

This is one reason the repository must distinguish explicit decisions, principles, hypotheses, and historical reasoning.

## Continuity as a system requirement

The continuity method being used to build this project also suggests a requirement for the future Autonomous Data Science System itself.

Long-running data projects should have explicit persistent state so that execution can resume after:

- a model context ends;
- an agent is replaced;
- a process crashes;
- a human pauses the project;
- a different model provider is used;
- or the project is revisited months later.

The implementation of that future project-state mechanism has not yet been selected.

## Version history

### Version 0.2

**Introduced:** Checkpoint 2, 2026-08-08

Changes:

- added the numbered, content-specific design-session naming convention;
- clarified that session names are provenance rather than system dependencies;
- made proactive checkpoint detection part of the continuity process;
- updated the required historical context through Checkpoint 2.

### Version 0.1

**Introduced:** Checkpoint 0, 2026-08-07

Initial cross-chat continuity procedure.

**Current continuity procedure version:** 0.2
