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
**Current phase:** Phase B pending Claude comparative review  
**Next expected participant:** Claude

## Why this thread exists

The project owner wants multi-model development to become a deliberate professional method rather than ad hoc switching between two chats.

Research 035 contains ChatGPT's candidate architecture. Claude has now frozen its first Phase-A counter-design, so comparative review is legitimate.

## Live transport

The optional conversational transport surface is:

```text
https://github.com/shakaarlatief/autonomous-data-science-system/issues/77
```

The issue is not project authority. Substantive review content should live in the numbered message artifacts, while the issue should normally carry short pointers and phase-transition notices to avoid duplicated substantive records drifting apart.

## Phase A: independent design

Phase A is complete.

Frozen artifact:

```text
docs/model_collaboration/threads/MC-0001/messages/002_claude_independent_proposal.md
```

Claude did not read Research 035 or ChatGPT message 001 before freezing its proposal. Claude correctly identified, however, that the required reconstruction documents already exposed several candidate Research 035 ideas. Phase A is therefore classified as partially independent rather than fully blind.

The review-integrity finding is preserved in:

```text
docs/checkpoints/200_mc_0001_phase_a_recorded_partial_independence_contamination_phase_b_opened.md
```

Convergence on candidate ideas already visible in `README.md`, `CURRENT_STATE.md`, or `KNOWLEDGE_MAP.md` must not be counted as clean independent confirmation.

## Phase B: comparative review

Claude should now read:

```text
docs/research/035_multi_model_development_collaboration_architecture.md
docs/model_collaboration/README.md
docs/model_collaboration/INTERACTION_PROVENANCE_AND_NAMING.md
docs/model_collaboration/threads/MC-0001/messages/001_chatgpt_review_request.md
```

alongside its own frozen Phase-A proposal.

Expected durable output:

```text
docs/model_collaboration/threads/MC-0001/messages/003_claude_comparative_review.md
```

The comparative review should distinguish:

```text
convergence that was already exposed during Phase A
cleanly independent additions from Claude
real convergence after full comparison
material disagreement
important omissions in ChatGPT's design
important omissions in Claude's design
unnecessary complexity
dangerous under-specification
must-change items
optional improvements
remaining unresolved questions
what evidence could resolve disagreements
```

Claude should directly challenge at least these Phase-A additions rather than assuming they are improvements merely because Claude proposed them:

```text
machine-readable active-writer lock
HIGH-IMPACT / LOW-IMPACT review trigger heuristic
pointer-only GitHub issue rule
mandatory calibrated-review template fields
disagreement routing defaults
human authorization of thread opening and writer transitions
provider-local conversation numbering
```

Agreement is not rewarded. Disagreement is not rewarded. The standard is calibrated reasoning.

## Phase C: ChatGPT response

ChatGPT will not respond substantively to Claude's architecture until the Phase-B artifact is frozen.

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
- whether a machine-readable writer lock is worth adding;
- whether independent-first review is worth its overhead and how to keep future blind reviews genuinely blind;
- how provider-neutral checkpoint/session provenance should work;
- how much model-to-model dialogue should be preserved;
- how much routine authorization the human should actually perform;
- how to measure actual value from a second model;
- and what evidence would justify API orchestration later.

## Resolution status

No resolution exists yet.

No change to `DEVELOPMENT_METHOD.md`, `CONTINUITY.md`, checkpoint metadata, validators, or accepted decisions should be treated as accepted until the thread has completed comparative review, response, resolution, and promotion audit.
