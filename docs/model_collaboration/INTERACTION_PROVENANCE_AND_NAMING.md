# Candidate Interaction Provenance and Conversation Naming

**Status:** Candidate pre-review refinement for MC-0001  
**Date:** 2026-08-25  
**Authority:** Working proposal only. This does not yet modify `DEVELOPMENT_METHOD.md`, `CONTINUITY.md`, or the checkpoint metadata contract.  
**Scope:** Preserve which concrete ChatGPT or Claude project/conversation produced collaboration messages while keeping the scheme provider-neutral enough for future collaborators.

## 1. Why repository provenance is not enough

A collaboration message can identify the repository commit it reviewed and still leave an important historical question unanswered:

```text
Which actual interaction produced this message?
```

For ADS development, that context matters because conversations are long-lived working environments with their own continuity, naming, model configuration, and platform-specific project context.

The desired provenance therefore separates:

```text
repository state
    from
interaction session
    from
collaboration thread
```

A future reader should be able to reconstruct all three without requiring the old chat to remain available.

## 2. Preserve the shared project identity

Both product workspaces should use:

```text
Autonomous Data Science System
```

as the visible project/workspace name where the product supports projects.

The common project name makes the human-facing organization symmetric across providers, but it is not enough to uniquely identify a conversation.

## 3. Conversation naming pattern

The candidate visible naming convention for both providers is:

```text
NN - Main Topic / Stage
```

This preserves the existing ChatGPT convention and gives Claude the same human-readable structure.

Each provider keeps its own sequence because ChatGPT and Claude conversations can rotate independently.

Examples:

```text
ChatGPT project: Autonomous Data Science System
ChatGPT title:   06 - Methodological Knowledge Universe Construction

Claude project:  Autonomous Data Science System
Claude title:    01 - Multi-Model Development Collaboration Review
```

The repository then gives those sessions unambiguous provider-qualified identities:

```text
chatgpt-06
claude-01
```

This is preferable to one global cross-provider conversation counter because two provider conversations may exist simultaneously and may have different lifetimes.

## 4. Candidate provenance envelope for model-to-model messages

A substantive collaboration message should normally preserve:

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

Optional fields where useful:

```text
Provider
Model / configuration
Interaction surface
Timestamp
Artifacts read
```

Example ChatGPT message:

```text
Author / collaborator: ChatGPT
Interaction environment: ChatGPT
Project / workspace: Autonomous Data Science System
Interaction session: chatgpt-06
Conversation title: 06 - Methodological Knowledge Universe Construction
Model / configuration: GPT-5.6 Sol
Collaboration thread: MC-0001
Role: TASK_OWNER / INITIAL_PROPOSER
Repository head reviewed: <sha>
```

Example Claude message:

```text
Author / collaborator: Claude
Interaction environment: Claude
Project / workspace: Autonomous Data Science System
Interaction session: claude-01
Conversation title: 01 - Multi-Model Development Collaboration Review
Model / configuration: product-displayed model/configuration when materially useful
Collaboration thread: MC-0001
Role: INDEPENDENT_REVIEWER / COUNTER_DESIGNER
Repository head reviewed: <sha>
```

## 5. Model name versus interaction identity

The stable provenance should not depend on a specific model name remaining available forever.

Therefore:

```text
interaction session identity
    should be stable

model / configuration
    is descriptive provenance
```

A later model switch inside the same product conversation should not create a new interaction-session identity merely because the selected model changed.

If the model change materially affects a consequential review, the message should record the model/configuration actually used.

## 6. Surface metadata

Products may expose different interaction surfaces, for example ordinary chat versus a more agentic/cowork mode.

A candidate optional field is:

```text
Interaction surface
```

This should be recorded only when it changes the interpretation or reproducibility of the work. The provenance system should not accumulate UI trivia merely because the field is available.

## 7. Historical ChatGPT metadata

Existing checkpoints use ChatGPT-specific fields:

```text
Design session
ChatGPT project
Session title
```

Those historical records should remain untouched.

If MC-0001 supports a provider-neutral future contract, the migration should be prospective:

```text
old checkpoints
    retain historical ChatGPT fields

new checkpoints after explicit method revision
    use provider-neutral interaction provenance
```

No historical checkpoint should be rewritten merely for cosmetic uniformity.

## 8. Relationship to collaboration intensity

Interaction provenance should not force multi-model collaboration.

A normal ChatGPT-only or Claude-only task may still preserve its interaction session through the ordinary checkpoint/continuity process without creating an `MC-*` thread.

The collaboration thread field exists only when the interaction participates in a cross-model thread.

Therefore:

```text
interaction provenance
    !=
mandatory collaboration provenance
```

## 9. Open questions for Claude review

MC-0001 should challenge at least:

- whether provider-local numbering plus provider-qualified IDs is better than a global development-session counter;
- whether model/configuration belongs in every substantive message or only consequential ones;
- whether interaction surface should be recorded;
- whether project/workspace names are stable enough to use directly;
- whether collaboration messages need timestamps in addition to Git commit time;
- how the checkpoint metadata contract should eventually generalize without making ordinary development cumbersome.

No answer is accepted merely because this candidate document proposes it.
