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

---

## Core rules

1. The repository's normal authority hierarchy remains unchanged.
2. A collaboration thread is provenance, not a decision merely because two models participated.
3. Every substantive bounded task has one task owner unless ownership is explicitly transferred.
4. Reviewers do not silently mutate the task owner's target state.
5. Reviewer messages may be added in the thread's allowed review surface without granting canonical write ownership.
6. High-impact reviews may use an independent-first phase before the reviewer sees the proposer's detailed solution.
7. Agreement is not the goal; disagreement is not the goal. Calibrated judgment is the goal.
8. Material unresolved disagreement must stay visible.
9. The human project owner remains the project-intent and normative authority.
10. API orchestration is not part of the current protocol.

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

## Message contract

A substantive message should normally begin with:

```text
Thread
Message
Author
Role
In reply to
Repository head reviewed
Purpose
```

Then include only the fields useful to the message, such as:

```text
Artifacts read
Position / findings
Evidence / repository references
Strongest objection or failure mode
Alternative considered
Uncertainty
What would change my view
Requested next action
```

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

The trial should be treated as evidence about this protocol itself. If the protocol creates unnecessary friction, anchoring, ambiguity, or duplicated work, Research 035 should be revised rather than defended.