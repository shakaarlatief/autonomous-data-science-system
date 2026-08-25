# Model Collaboration Exchange

**Status:** Candidate operational collaboration protocol under Research 035  
**Date:** 2026-08-25  
**Authority:** Collaboration provenance and working protocol only. This directory does not override accepted specifications, decisions, canonical current-state documents, promoted implementation, or the Development Method.  
**Governing research:** `docs/research/035_multi_model_development_collaboration_architecture.md`

## Purpose

This directory provides a dedicated asynchronous communication surface for strong AI collaborators working on the Autonomous Data Science System itself.

It exists because:

```text
repository as source of truth
    !=
a place for model-to-model review dialogue
```

Without a dedicated exchange, review requests, critiques, counterarguments, and unresolved disagreements would either be trapped in private chats or mixed into canonical project documents where they do not belong.

The exchange should reduce user copy-paste while keeping raw collaboration clearly separate from project authority.

The exchange is optional infrastructure for tasks that benefit from collaboration. It is not a requirement that every ADS task involve multiple models.

---

## Operating modes

The collaboration architecture must support several legitimate development modes.

### SOLO

One model works with the human and the repository without invoking another model for the bounded task.

This should remain the default for work where a second-model contribution is unlikely to justify the coordination cost, for example ordinary mechanical edits, local clarifications, low-risk implementation work under an accepted contract, or routine continuation.

A SOLO task does not need a model-collaboration thread merely to prove that collaboration was considered.

### REVIEWED

One model owns the task and another model performs a bounded review, critique, verification, or research role.

This is appropriate when independent pressure is useful but full joint design would be excessive.

### INDEPENDENT_THEN_COMPARATIVE

Two models first reason independently from a common neutral problem statement, then compare after both positions are frozen.

This is appropriate for high-impact architecture, experiment design, governance, or other decisions where anchoring risk is material.

### COORDINATED_HANDOFF

A bounded task or subtask is explicitly transferred from one collaborator to another with repository state, ownership scope, and outstanding obligations preserved.

The handoff is not the same as simultaneous co-ownership.

These modes are task-level choices. The project may move between ChatGPT-only, Claude-only, and collaborative work over time without changing its authority model.

---

## Core rules

1. The repository's normal authority hierarchy remains unchanged.
2. A collaboration thread is provenance, not a decision merely because two models participated.
3. Multi-model collaboration is selective, not universal. Single-model work remains first-class.
4. Every substantive collaborative bounded task has one task owner unless ownership is explicitly transferred.
5. Reviewers do not silently mutate the task owner's target state.
6. Reviewer messages may be added in the thread's allowed review surface without granting canonical write ownership.
7. High-impact reviews may use an independent-first phase before the reviewer sees the proposer's detailed solution.
8. Agreement is not the goal; disagreement is not the goal. Calibrated judgment is the goal.
9. Material unresolved disagreement must stay visible.
10. The human project owner remains the project-intent and normative authority.
11. API orchestration is not part of the current protocol.
12. Collaboration provenance should identify the originating interaction context well enough that a future reader can trace which project/chat/session produced a substantive message.

---

## Directory structure

Each collaboration has a stable thread ID:

```text
MC-NNNN
```

Candidate structure:

```text
threads/
    MC-0001/
        BRIEF.md
        THREAD.md
        messages/
            001_chatgpt_review_request.md
            002_claude_independent_proposal.md
            003_claude_comparative_review.md
            004_chatgpt_response.md
            ...
        RESOLUTION.md
```

`RESOLUTION.md` should not exist until the thread actually reaches a durable resolution or explicit unresolved/deferred terminal state.

---

## Thread metadata

`THREAD.md` should identify at least:

```text
Thread ID
Topic
Status
Task owner
Reviewer(s)
Human decision authority
Branch / PR
Review mode
Scope
Allowed reviewer write surface
Current phase
Next expected participant/action
```

The thread should reference accepted repository artifacts rather than reproduce them.

---

## Interaction-session identity

Repository authority and interaction provenance are different concerns.

A collaboration message should be traceable to the concrete conversation that produced it without making the repository depend on that conversation remaining accessible.

The candidate provider-neutral provenance model separates:

```text
collaborator identity
provider / interaction environment
workspace or project name
interaction-session identifier
conversation title
interaction surface, where useful
model / configuration, where useful
collaboration role
collaboration thread
repository head reviewed
```

For example, the current ChatGPT work could conceptually record:

```text
Collaborator: ChatGPT
Interaction environment: ChatGPT
Project / workspace: Autonomous Data Science System
Interaction session: chatgpt-06
Conversation title: 06 - Methodological Knowledge Universe Construction
Model / configuration: GPT-5.6 Sol
Collaboration thread: MC-0001
Role: TASK_OWNER / INITIAL_PROPOSER
```

A first Claude development chat could conceptually record:

```text
Collaborator: Claude
Interaction environment: Claude
Project / workspace: Autonomous Data Science System
Interaction session: claude-01
Conversation title: 01 - Multi-Model Development Collaboration Review
Model / configuration: as displayed in the product, when useful
Collaboration thread: MC-0001
Role: INDEPENDENT_REVIEWER / COUNTER_DESIGNER
```

The exact field names are not yet canonical. This is a candidate shape to be pressure-tested in MC-0001 before changing the checkpoint contract.

Historical ChatGPT-specific checkpoint metadata must remain intact. A future provider-neutral contract should extend or supersede prospectively rather than rewrite historical provenance.

---

## Conversation naming

The candidate naming rule is intentionally simple.

Both ChatGPT and Claude should use the same visible title pattern inside the shared project name:

```text
NN - Main Topic / Stage
```

Each interaction environment maintains its own sequence because ChatGPT and Claude conversations can rotate independently.

Repository provenance disambiguates them with an environment-qualified session identity such as:

```text
chatgpt-06
claude-01
```

This avoids forcing both products into one artificial global chat counter while still making every exchange unambiguous.

The first Claude conversation for MC-0001 is therefore a candidate for:

```text
01 - Multi-Model Development Collaboration Review
```

within the Claude project:

```text
Autonomous Data Science System
```

This naming proposal is not yet canonical and should be challenged by Claude during the independent review.

---

## Message contract

A substantive message should normally begin with a small provenance envelope. Candidate fields are:

```text
Thread
Message
Author / collaborator
Role
In reply to
Interaction environment
Project / workspace
Interaction session
Conversation title
Repository head reviewed
Purpose
```

Optional fields where they materially improve reproducibility or interpretation include:

```text
Model / configuration
Interaction surface
Artifacts read
Position / findings
Evidence / repository references
Strongest objection or failure mode
Alternative considered
Uncertainty
What would change my view
Requested next action
```

The provenance envelope should identify the originating chat, but the substantive message should still stand on its own if the chat later disappears.

Messages should remain focused. A 100-page research artifact belongs in `docs/research/`, not inside a message file.

After another participant has relied on a message, substantive correction should normally be a new message rather than historical rewriting.

---

## Review modes

### DIRECT_REVIEW

The reviewer reads the proposal and critiques it directly.

Use for ordinary bounded work where anchoring risk is low relative to coordination cost.

### INDEPENDENT_THEN_COMPARATIVE

Phase A:

```text
reviewer reads neutral problem brief + governing accepted state
reviewer records its own design/findings
reviewer does not read proposer's detailed solution yet
```

Phase B:

```text
reviewer reads the proposal
reviewer records comparison, convergence, disagreement, omissions,
and what evidence could distinguish alternatives
```

Use for high-impact architecture, experiment design, governance, or other decisions where independent epistemic pressure is valuable.

### ADVERSARIAL_REVIEW

Reviewer is specifically tasked with finding falsifiers, hidden assumptions, leakage, failure modes, weak gates, or unsupported claims.

This does not license performative disagreement.

---

## Write authority

The collaboration exchange introduces a narrow exception to one-task-owner branch ownership.

The task owner owns target-state edits.

A designated reviewer may add **new** message files under the active thread's `messages/` directory or use the linked GitHub review/issue surface.

The reviewer should not edit canonical/current-state/target implementation files while remaining in reviewer role.

If a reviewer is asked to implement a patch, ownership of that patch must be explicit or the patch should occur on a reviewer-owned branch for later integration.

A SOLO task requires no second-model write coordination because only the active collaborator owns the bounded task.

---

## Optional GitHub transport

A thread may link a GitHub issue or PR discussion as a lower-friction asynchronous transport surface.

Conceptually:

```text
GitHub issue / PR comments
    live transport

thread message artifacts
    durable structured review provenance

accepted project docs / code
    authority after promotion
```

If a collaborator cannot write GitHub comments, repository message files remain sufficient.

No future continuation should depend on an issue comment being the only place where a material conclusion was preserved.

---

## Genuine-review requirements

When substantially agreeing, a reviewer should still state:

```text
strongest plausible failure mode
strongest alternative considered
what would make support change
remaining weak/provisional parts
```

When materially disagreeing, a reviewer should state:

```text
exact disputed choice
why it matters
preferred alternative
what would make the reviewer accept the original
whether the disagreement is factual, interpretive, architectural,
risk-based, evidence-sufficiency based, scope-based, or normative
```

No participant should manufacture objections merely to appear independent.

---

## Resolution

A collaboration thread may end as:

```text
RESOLVED
UNRESOLVED
DEFERRED
SUPERSEDED
ABANDONED
```

The resolution should point to any promoted canonical artifact and preserve important residual disagreement.

A thread does not itself promote knowledge.

The normal project checkpoint/promotion method still governs acceptance.

---

## Current trial

The first thread is:

```text
MC-0001
Multi-model development collaboration architecture
```

It uses `INDEPENDENT_THEN_COMPARATIVE` review with:

```text
ChatGPT   initial proposer / task owner
Claude    independent counter-designer + comparative reviewer
Human     project-intent arbiter
```

The trial should be treated as evidence about this protocol itself. If the protocol creates unnecessary friction, anchoring, ambiguity, duplicated work, or excessive provenance burden, Research 035 should be revised rather than defended.
