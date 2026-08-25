# MC-0001: Multi-Model Development Collaboration Architecture

**Status:** OPEN  
**Topic:** Design and pressure-test the collaboration architecture for ChatGPT + Claude + human development of ADS  
**Task owner:** ChatGPT  
**Independent reviewer / counter-designer:** Claude  
**Human decision authority:** Project owner  
**Review mode:** INDEPENDENT_THEN_COMPARATIVE  
**Active branch:** `v1-multimodel-development-collaboration`  
**Active PR:** #76  
**Stacked on:** `v1-source-vault-bootstrap` at `d9437a8ca07a444400a5eb44ac2c89e8108c91c2`  
**Live transport:** GitHub Issue #77  
**Target authority:** None yet. This thread is review provenance only.  
**Allowed reviewer write surface:** New immutable files under this thread's `messages/` directory and/or GitHub Issue #77. Claude should not modify target canonical/project-state files while acting as reviewer.  
**Current phase:** Phase A pending independent Claude proposal  
**Next expected participant:** Claude

## Why this thread exists

The project owner wants multi-model development to become a deliberate professional method rather than ad hoc switching between two chats.

Research 035 contains ChatGPT's candidate architecture, but the first review intentionally uses an independence-preserving sequence.

## Live transport

The optional conversational transport surface is:

```text
https://github.com/shakaarlatief/autonomous-data-science-system/issues/77
```

The issue is not project authority and is not required to survive as the only record of a material conclusion. Substantive independent/comparative review artifacts should be preserved under `messages/` whenever practical.

## Phase A: independent design

Claude should read:

```text
docs/model_collaboration/threads/MC-0001/BRIEF.md
docs/DEVELOPMENT_METHOD.md
docs/CONTINUITY.md
docs/checkpoints/README.md
README.md
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
```

and the governing artifacts those documents require for understanding the current development method.

Claude should **not read**:

```text
docs/research/035_multi_model_development_collaboration_architecture.md
```

until its independent Phase-A architecture has been durably recorded.

Requested Phase-A artifact:

```text
docs/model_collaboration/threads/MC-0001/messages/002_claude_independent_proposal.md
```

If Claude cannot write directly to the repository, it may post the complete structured response to GitHub Issue #77. Direct repository/issue writing is preferred so the user is not a routine message relay.

## Phase B: comparative review

After Phase A is frozen, Claude should read:

```text
docs/research/035_multi_model_development_collaboration_architecture.md
docs/model_collaboration/README.md
```

and produce:

```text
docs/model_collaboration/threads/MC-0001/messages/003_claude_comparative_review.md
```

The review should identify:

```text
real convergence
material disagreement
important omissions in ChatGPT's design
important omissions in Claude's independent design
unnecessary complexity
dangerous under-specification
must-change items
optional improvements
what evidence could resolve disagreements
```

Agreement should not be rewarded. Disagreement should not be rewarded. The standard is calibrated reasoning.

## Phase C: ChatGPT response

ChatGPT then reads the two Claude artifacts and responds in a new message rather than rewriting Claude's record.

Expected path:

```text
docs/model_collaboration/threads/MC-0001/messages/004_chatgpt_response_to_claude.md
```

Each material disagreement should be accepted, rejected with reasoning, or left explicitly unresolved.

## Phase D: resolution

Any remaining disagreement should be classified as one or more of:

```text
FACT
INTERPRETATION
REQUIREMENT
ARCHITECTURE
RISK
EVIDENCE_SUFFICIENCY
NORMATIVE / PROJECT_INTENT
SCOPE
```

Then route it to evidence, experiment, human decision, or deferral.

Only after this should the project decide whether to promote a multi-model Development Method revision.

## Current open questions

The cross-model review should especially challenge:

- whether a dedicated repository exchange is the right abstraction;
- whether issue/PR comments should be primary or secondary transport;
- whether one-owner-per-task is sufficient;
- whether independent-first review is worth its overhead;
- how provider-neutral checkpoint/session provenance should work;
- how much model-to-model dialogue should be preserved;
- how to measure actual value from a second model;
- and what evidence would justify API orchestration later.

## Resolution status

No resolution exists yet.

No change to `DEVELOPMENT_METHOD.md`, `CONTINUITY.md`, checkpoint metadata, or validators should be treated as accepted until the thread has completed its review and promotion audit.