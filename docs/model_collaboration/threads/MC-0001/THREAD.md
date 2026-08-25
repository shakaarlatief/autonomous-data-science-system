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
**Current phase:** Phase D bounded Claude challenge pending  
**Next expected participant:** Claude

## Why this thread exists

The project owner wants multi-model development to become a deliberate professional method rather than ad hoc switching between two chats.

Research 035 contains ChatGPT's candidate architecture. Claude has now completed both its first counter-design and its full comparative review. ChatGPT has responded point-by-point in message 004. The thread is now narrowed to the remaining material disagreements rather than reopening the whole architecture.

## Live transport

The optional conversational transport surface is:

```text
https://github.com/shakaarlatief/autonomous-data-science-system/issues/77
```

The issue is not project authority. Substantive review content should live in the numbered message artifacts, while the issue should normally carry short pointers and phase-transition notices to avoid duplicated substantive records drifting apart.

A disclosed full-content issue comment remains acceptable as a fallback if direct durable file writing is temporarily unavailable. Once the durable file exists, the issue should point to it rather than maintaining two evolving substantive copies.

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

Phase B is complete.

Frozen artifact:

```text
docs/model_collaboration/threads/MC-0001/messages/003_claude_comparative_review.md
```

Claude compared its frozen proposal against Research 035, the collaboration protocol, and the interaction-provenance candidate. It explicitly separated contaminated convergence from genuinely new convergence, revised several of its own Phase-A positions, identified omissions on both sides, and preserved remaining disagreements.

Major Claude conclusions include:

```text
machine-checkable collaboration state is a must-address gap
future blind-review packets need explicit contamination protection
HIGH / LOW impact triggers are useful working defaults
issue transport should be pointer-first with disclosed fallback
human authorization should be reserved for consequential / contested transitions
provider-local conversation numbering with environment-prefixed IDs is preferred
role taxonomy and lifecycle vocabulary are useful but should not become mandatory ceremony
```

## Phase C: ChatGPT response

Phase C is complete.

Frozen artifact:

```text
docs/model_collaboration/threads/MC-0001/messages/004_chatgpt_response_to_claude.md
```

ChatGPT accepted several Claude contributions, modified others, and rejected blanket defaults where they would introduce systematic bias or unnecessary human burden.

Important ChatGPT positions include:

```text
accept the need for machine-readable collaboration-state support
reject a single global active-writer field as too coarse
prefer scoped per-thread target-write ownership + allowed write surfaces
classify JSON as a coherence guard, not a true distributed lock
strengthen blind review around accepted base refs + neutral problem packets
accept HIGH / LOW as provisional rather than final
route REQUIREMENT to canonical authority before human arbitration
reject universal "more risk-averse wins" routing
reject universal "narrow scope wins" routing
accept ROLE != WRITE_SCOPE
accept provider-local environment-prefixed session IDs
preserve model effort / reasoning mode only when known, without guessing
```

## Phase D: bounded challenge and resolution

Claude should now read message 004 and perform one bounded challenge pass focused on the genuinely unresolved items rather than re-reviewing the entire architecture.

Expected durable output:

```text
docs/model_collaboration/threads/MC-0001/messages/005_claude_phase_d_challenge.md
```

For each item below Claude should state:

```text
AGREE
DISAGREE
PARTIAL / QUALIFIED
```

plus the strongest reason and what evidence would change its view.

Questions:

```text
1. Is ChatGPT correct to reject a single global active-writer lock and
   prefer a scoped per-thread target-write / allowed-surface model?
2. Is ChatGPT correct that a JSON record is only a coherence guard,
   not a true lock?
3. Should REQUIREMENT route to canonical authority before the human?
4. Should blanket "risk-averse wins" and "narrow-scope wins" defaults
   be rejected in favor of consequence/authority-sensitive routing?
5. Is ROLE != WRITE_SCOPE the correct abstraction?
6. Is accepted-base-ref + neutral-brief reconstruction the correct
   default for future intentionally blind counter-designs?
7. Are there any material objections to provider-local session numbering,
   environment-prefixed IDs, or the proposed provenance envelope?
```

After message 005, remaining disagreements should be routed to one of:

```text
bounded design / prototype
repository or external evidence
human project-intent decision
explicit deferral with reopen criteria
```

The thread should not continue indefinitely merely because more dialogue is possible.

## Current open questions

The cross-model review still needs to close or route:

- exact machine-readable collaboration-state representation and validation semantics;
- whether stronger hard branch-protection machinery is ever warranted;
- whether HIGH / LOW remains sufficient after several real threads;
- whether all eight role labels remain useful in practice;
- whether GitHub Issue transport remains legible at larger collaboration volume;
- exact mandatory/optional provenance fields for model/configuration/effort;
- and how much real marginal value justifies selective independent review over time.

## Resolution status

No final resolution exists yet.

No change to `DEVELOPMENT_METHOD.md`, `CONTINUITY.md`, checkpoint metadata, validators, or accepted decisions should be treated as accepted until Phase D is closed, remaining disagreements are routed, and the normal promotion audit is complete.
