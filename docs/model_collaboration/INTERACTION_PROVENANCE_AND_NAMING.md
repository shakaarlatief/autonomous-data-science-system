# Interaction Provenance and Conversation Naming

**Status:** Accepted collaboration/continuity convention  
**Date promoted:** 2026-08-26  
**Authority:** Canonical provider-neutral interaction-provenance convention under Development Method v0.5 and `docs/checkpoints/README.md`  
**Scope:** Preserve which concrete interaction environment, workspace, session, and conversation produced ADS development artifacts without making chat history authoritative.

## 1. Repository state, interaction session, and collaboration thread are different

A durable artifact may need three distinct provenance coordinates:

```text
repository state
    exact branch / commit / artifact authority

interaction session
    concrete ChatGPT / Claude / future environment that produced reasoning

collaboration thread
    bounded cross-model question or review, when applicable
```

These identities must not be collapsed.

The repository remains project authority even if the originating chat later disappears.

## 2. Shared project/workspace identity

Where the product supports a project/workspace concept, use:

```text
Autonomous Data Science System
```

for both ChatGPT and Claude.

The shared visible name improves human navigation but is not a unique session identifier.

## 3. Visible conversation naming

The accepted visible naming pattern is:

```text
NN - Main Topic / Stage
```

Each interaction environment maintains its own sequence because conversations may rotate independently and may overlap in time.

Examples:

```text
ChatGPT title  06 - Methodological Knowledge Universe Construction
Claude title   01 - ADS Development Review & Collaboration
```

## 4. Repository interaction-session identity

Use provider/environment-qualified session IDs:

```text
chatgpt-06
claude-01
```

This avoids one artificial global conversation counter while remaining globally unambiguous in repository provenance.

A model/configuration change inside the same long-lived conversation does not by itself create a new interaction-session ID.

## 5. Collaboration-message provenance

A substantive model-collaboration message should normally preserve:

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

Optional fields when materially useful:

```text
Model / configuration
Effort / reasoning mode
Interaction surface
Timestamp
Artifacts read
Source of a user/system-reported configuration value
```

Model or effort values should not be guessed. If the value comes from the human or product UI rather than model introspection, that source should be clear where it matters.

## 6. Checkpoint provenance

Historical checkpoints through Checkpoint 203 retain the original ChatGPT-specific contract:

```text
Design session
ChatGPT project
Session title
```

Beginning with Checkpoint 204, new checkpoints use the provider-neutral prospective contract defined in `docs/checkpoints/README.md`:

```text
Interaction environment
Project / workspace
Interaction session
Conversation title
Primary collaborator
```

Collaboration thread/role and model/configuration remain optional extensions where useful.

Historical checkpoints are not rewritten merely for cosmetic uniformity.

## 7. SOLO work versus collaborative work

Interaction provenance is required by the checkpoint contract whether the work is SOLO or collaborative.

A collaboration-thread field exists only when a checkpoint or message actually participates in an `MC-*` thread.

Therefore:

```text
interaction provenance
    !=
mandatory multi-model collaboration
```

## 8. Surface metadata

Interaction surface such as ordinary chat, Cowork, Claude Code, or another environment should be recorded only when it materially changes interpretation, permissions, tool access, or reproducibility.

Do not accumulate UI trivia merely because it is observable.

## 9. Provider neutrality

The convention must remain usable if ChatGPT or Claude is replaced or supplemented later.

Provider names are provenance values, not semantic authority. The accepted project method is based on collaborator roles, write scope, evidence, and repository authority rather than provider identity.