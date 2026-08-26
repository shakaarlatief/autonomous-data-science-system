# Continuity

**Status:** Current canonical continuity procedure  
**Aligned development-method version:** 0.5  
**Last reviewed:** 2026-08-26

## Purpose

This document defines how the Autonomous Data Science System project continues across chats, sessions, models, interaction products, or other context boundaries.

The central requirement is:

> **A new collaborator must be able to reconstruct current project state from persistent repository artifacts without requiring the previous conversation or relying on model memory.**

Long conversations are temporary working environments, not durable project storage.

Important knowledge must be durable, discoverable, correctly classified, and routed to the right authority layer.

---

## Repository authority across collaborators

The repository remains the durable source of truth whether the active collaborator is ChatGPT, Claude, a future model, or the human project owner.

A collaborator should not treat its own conversation history as stronger than repository state.

If repository artifacts disagree, resolve through status, scope, chronology, supersession, accepted specifications/decisions, or explicit open-question handling rather than hidden memory.

---

## Project/workspace and conversation naming

Where an interaction product supports projects/workspaces, use:

```text
Autonomous Data Science System
```

Visible development conversations use:

```text
NN - Main Topic / Stage
```

Each interaction environment has its own sequence because ChatGPT and Claude conversations may rotate independently.

Repository interaction-session IDs are provider/environment-qualified, for example:

```text
chatgpt-06
claude-01
```

Current known collaboration sessions:

```text
ChatGPT
    interaction session  chatgpt-06
    title                06 - Methodological Knowledge Universe Construction

Claude
    interaction session  claude-01
    title                01 - ADS Development Review & Collaboration
```

Session titles and IDs are provenance/navigation metadata. Repository correctness must never depend on the old chat remaining accessible.

See:

```text
docs/model_collaboration/INTERACTION_PROVENANCE_AND_NAMING.md
```

---

## Checkpoint interaction provenance

Historical checkpoints through Checkpoint 203 preserve the original ChatGPT-specific fields:

```text
Design session
ChatGPT project
Session title
```

Beginning with Checkpoint 204, the checkpoint contract is provider-neutral:

```text
Interaction environment
Project / workspace
Interaction session
Conversation title
Primary collaborator
```

Collaboration thread/role, model/configuration, effort/reasoning mode, and interaction surface may be recorded when materially useful.

The migration is prospective. Historical checkpoints are not rewritten merely for uniformity.

Canonical contract:

```text
docs/checkpoints/README.md
```

---

## When to rotate a conversation

Opening a new conversation is a continuity action, not a topic-management rule.

The active AI collaborator should proactively recommend rotation when context pressure or another practical boundary makes continuation less reliable than reconstructing cleanly.

Useful triggers include:

- conversation length/context pressure;
- difficulty retaining earlier reasoning still required for the task;
- tool/session degradation attributable to context length;
- approaching platform/model limits;
- or another interaction-boundary condition that threatens continuity.

A topic change, checkpoint, foundation, or implementation milestone is not by itself a reason to rotate.

---

## Proactive rotation procedure

Before a planned rotation, the active collaborator should normally:

1. preserve important uncheckpointed reasoning;
2. create a checkpoint when warranted;
3. perform the promotion audit;
4. ensure relevant canonical documents are current;
5. update `KNOWLEDGE_MAP.md` where routing changed;
6. ensure `CURRENT_STATE.md` is concise/current;
7. update detailed experiment/status ledgers if the next session depends on them;
8. preserve active collaboration state and pending review obligations;
9. record the exact next step and unresolved questions;
10. verify repository-only reconstruction;
11. propose a suitable next interaction-session ID/title;
12. use the standardized continuation prompt below.

The user should not need to manually summarize the prior conversation.

---

## Unplanned session-boundary recovery

A session may end before reconciliation is complete because of a context limit, client failure, tool interruption, browser/session loss, usage limit, or another hard boundary.

The next collaborator should not recreate missing context from memory.

Recovery procedure:

1. identify the active branch/PR from Git/GitHub evidence;
2. read `README.md`, `docs/CURRENT_STATE.md`, `docs/KNOWLEDGE_MAP.md`, and `docs/current_routing.json` from that branch;
3. inspect recent checkpoints, specifications, research files, result artifacts, collaboration threads, PRs, and commits near the boundary;
4. compare authority/status metadata with older routing wording;
5. identify what was substantively preserved and which routing/current-state updates were interrupted;
6. reconstruct from repository authority;
7. repair stale routing/canonical wording conservatively without rewriting historical conclusions;
8. reconcile open questions when status has changed;
9. preserve the new interaction-session provenance;
10. create a reconciliation checkpoint when the repair is substantive;
11. continue from the newest legitimate boundary.

Important distinction:

```text
substantive preservation failure
    important reasoning was never persisted

routing/reconciliation failure
    important reasoning exists but current routing/indexes lag
```

The project has repeatedly demonstrated the second recovery path in earlier ChatGPT session rotations.

---

## New-session/model start procedure

Any new substantive development session, regardless of provider, should reconstruct before making changes.

### Minimum reading order

1. `README.md`
2. `docs/CURRENT_STATE.md`
3. `docs/KNOWLEDGE_MAP.md`
4. `docs/current_routing.json`
5. `docs/VISION.md`
6. `docs/PRINCIPLES.md`
7. `docs/DECISIONS.md`
8. `docs/OPEN_QUESTIONS.md`
9. `docs/DEVELOPMENT_METHOD.md`
10. `docs/CONTINUITY.md`

Then follow the active-stage routes named by `CURRENT_STATE.md` and `KNOWLEDGE_MAP.md`.

If work is on a feature branch, verify the branch that actually contains the newest checkpoint/specification. Do not assume `main` is current merely because it is the default branch.

---

## Required reconstruction result

Before substantial work, the collaborator should be able to state:

- what ADS is trying to build;
- current development stage;
- accepted decisions and constraints;
- which ideas remain hypotheses/candidates;
- important unresolved questions;
- active branch/PR and current implementation/experiment slice;
- exact next legitimate step;
- governing documents for that step;
- active collaboration ownership/write scope when relevant;
- pending review/catch-up obligations when relevant;
- and any current routing/canonical drift.

If inconsistency remains, surface it explicitly rather than inventing a reconciliation.

---

## Standardized continuation prompt

The normal new-session prompt remains intentionally provider-neutral and stable:

```text
Continue the Autonomous Data Science System project from the repository. Treat the repository as the source of truth, not prior chat memory. First read README.md, docs/CURRENT_STATE.md, docs/KNOWLEDGE_MAP.md, and the governing documents they point to for the active stage. Reconstruct where the project currently stands, the important accepted conclusions and unresolved questions, and the next legitimate step. Follow the project's development/preservation method. Do not make changes yet; first align with me on the current state.
```

If the interaction has repository access, it should read the files itself.

If direct repository access is unavailable, provide the relevant repository artifacts rather than relying on remembered summaries.

---

# Multi-model continuity

## Shared repository instead of transcript relay

ChatGPT and Claude should communicate primarily through shared repository state, collaboration threads, and GitHub transport rather than repeated user copy/paste of entire conversations.

A model should reconstruct another collaborator's work from durable artifacts, not from a private handoff summary alone.

## Collaboration exchange

Canonical protocol:

```text
docs/model_collaboration/README.md
```

Active collaboration is organized by `MC-NNNN` threads containing a bounded brief, thread contract, optional machine-readable state, numbered messages, and resolution when terminal.

GitHub issues/PR comments may provide low-friction transport, but substantive conclusions must remain recoverable from repository artifacts.

## Independent-review continuity

If a review is meant to be blind/independent, reconstruction must not leak the candidate solution through current routing files.

Use an accepted pre-proposal repository ref plus neutral problem packet when practical. Preserve known exposure/contamination rather than pretending independence was stronger than it was.

---

# Deferred review and catch-up continuity

Canonical protocol:

```text
docs/model_collaboration/DEFERRED_REVIEW_AND_CATCHUP.md
```

A temporarily unavailable collaborator does not globally block ADS unless a specific review gate has been reached.

Intended review must remain explicit and must preserve an exact immutable target.

Pending obligations are routed through:

```text
docs/model_collaboration/REVIEW_INBOX.md
```

The inbox is convenience routing only. Per-thread state, review request, resolution, and exact Git refs are authoritative.

For Claude, the standard manual catch-up trigger is:

```text
Check the repository and docs/model_collaboration/REVIEW_INBOX.md, then proceed with the pending Claude reviews in order.
```

This tiny prompt is intentional. The repository carries the detailed contract.

If several related obligations are processed in one model session, each still requires a separate exact target, finding set, required correction set, and disposition.

Review of commit X does not imply review of descendant Y.

If a delayed review changes an upstream result, inspect downstream work that relied on it. Cross-thread dependency discovery is currently procedural and should become mechanical only after real dependency-chain evidence justifies it.

---

## SOLO continuity

A task intentionally performed in SOLO mode does not create hidden review debt merely because another model exists.

The project may legitimately spend many messages/tasks with ChatGPT only or Claude only.

Cross-model review should be invoked deliberately, not inferred from provider availability.

---

## Model/product usage constraints

Provider subscription limits, model effort settings, and interaction surfaces are operational constraints rather than project authority.

If one collaborator hits a usage limit, the project should use the deferred-review protocol rather than globally stopping unrelated work or silently dropping intended review.

Exact provider percentages/limits are not frozen into canonical architecture because products change.

---

## Scheduled/unattended review

Unattended scheduled model review is currently **not** part of the continuity method.

It was considered and deliberately deferred because:

```text
it does not create additional weekly subscription capacity
it introduces unattended write/concurrency risk
it cannot easily pause for clarification
it can consume scarce usage before the human can intervene
manual catch-up triggering is already low-friction
```

The option may be reconsidered later if product capabilities, write isolation, or workload scale changes materially.

---

## API orchestration

Programmatic OpenAI/Anthropic multi-model orchestration remains deferred.

API use is separately metered from interactive subscriptions and would introduce provider credentials, context duplication, retries, failure handling, and orchestration infrastructure.

Repository-mediated collaboration should continue until measured friction demonstrates that automation earns those costs.

---

## Proactive preservation during a session

The active AI collaborator should detect natural preservation points using `DEVELOPMENT_METHOD.md`.

Intended pattern:

```text
reason freely
    -> detect coherent milestone
    -> checkpoint when warranted
    -> promotion audit
    -> update durable knowledge/routing where warranted
    -> continue from the recorded next step
```

Preserve substantive evidence before cosmetic routing cleanup when a hard session boundary is near.

---

## End-of-session procedure

Before a deliberate stop/rotation, normally:

1. review what changed since the prior checkpoint;
2. preserve important reasoning;
3. update canonical documents where accepted knowledge changed;
4. record decisions/open questions;
5. preserve active collaboration status and pending reviews;
6. complete promotion audit;
7. update routing/status ledgers;
8. update `CURRENT_STATE.md`;
9. record exact next step/read set;
10. update interaction-session provenance;
11. verify repository-only reconstruction.

The goal is continuity, not bureaucracy.

---

## Current-state requirements

`docs/CURRENT_STATE.md` should answer:

```text
What are we building?
What stage are we in?
What accepted conclusions/constraints affect the next step?
What is the exact current priority?
What collaboration/review obligations are active?
What happens next?
What should a future collaborator read?
```

It should remain concise relative to foundations, research, checkpoints, and experiment ledgers.

---

## Knowledge-map requirements

Update `docs/KNOWLEDGE_MAP.md` when a future collaborator would otherwise be likely to look in the wrong place, including when:

- important new foundations/research/specifications are created;
- canonical authority changes;
- active branch-local work changes;
- a new collaboration subsystem/protocol becomes current;
- a source becomes superseded;
- or a major result changes the continuation route.

Routine checkpoint creation does not automatically require a map update.

---

## Knowledge reconciliation

At major stage boundaries, reconcile at least:

```text
README actual stage
CURRENT_STATE present-tense accuracy
KNOWLEDGE_MAP routing
DECISIONS / OPEN_QUESTIONS currency
important checkpoint promotions
active experiment/status ledgers
checkpoint interaction provenance
collaboration thread terminal/pending state
REVIEW_INBOX accuracy
MAJOR_CHANGES structural history
branch-local versus promoted state
```

---

## Deferred future continuity tooling

Current continuity remains based on Git + Markdown + explicit repository structure + narrowly earned validators.

Possible later tooling includes generated indexes, semantic retrieval, cross-thread dependency discovery, generated review inboxes, reconciliation assistants, or raw-conversation provenance archives.

Introduce them only after observed scale/consistency problems justify the complexity.

---

# Version relationship

Current continuity is aligned with Development Method v0.5.

Progression:

```text
v0.1
layered durable preservation + new-chat reconstruction

v0.2
proactive checkpoint detection + proactive rotation

v0.3
promotion audit + knowledge map + reconciliation + current-state discipline

v0.4
explicit checkpoint metadata contract + historical ChatGPT session provenance

v0.5
provider-neutral interaction provenance + governed multi-model collaboration
+ deferred review/catch-up + explicit collaboration continuity
```

Detailed preservation rationale remains in:

```text
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
```
