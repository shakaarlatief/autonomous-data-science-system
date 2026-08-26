# Model Collaboration Review Inbox

**Date:** 2026-08-26  
**Status:** Current human-readable routing view  
**Authority:** Convenience index only. Per-thread `STATE.json`, `THREAD.md`, frozen review requests, exact Git refs, and resolution records remain authoritative.  
**Purpose:** Let a returning collaborator discover pending review/catch-up obligations without relying on private chat memory.

## Current pending obligations

### 1. MC-0004: comparative next-generation Project Cockpit design review

```text
collaborator            Claude
review mode             INDEPENDENT_THEN_COMPARATIVE
current phase           PHASE_B_COMPARATIVE_REVIEW
priority                required comparative review before final ChatGPT synthesis
active branch           v1-cockpit-design-exploration
Phase-A review base     bedbd23f5aa5f35c79892ae633ccbc6da6ef7d88
Phase-A frozen commit   cd2e12f2c79ee3b2f205457c5940eb2022b4631a
Claude Phase-A message  docs/model_collaboration/threads/MC-0004/messages/001_claude_independent_phase_a_proposal.md
ChatGPT research        docs/research/037_project_cockpit_next_generation_visual_interaction_design_exploration_map.md
thread contract         docs/model_collaboration/threads/MC-0004/THREAD.md
thread state            docs/model_collaboration/threads/MC-0004/STATE.json
allowed write surface   docs/model_collaboration/threads/MC-0004/messages/**
```

Phase A is complete and remains historically classified:

```text
BLIND_TO_CANDIDATE
known candidate exposures: none
```

Phase B now explicitly permits Claude to read Research 037.

Required comparative output:

```text
compare the frozen Claude Phase-A proposal with Research 037
identify strongest convergence and material disagreement
identify ideas from each side that improve the other
preserve the strongest alternative after comparison
recommend which mechanisms/directions deserve realistic mockups first
state what should remain unresolved
state what evidence would change the recommendation
preserve the comparative response under MC-0004/messages/
```

Review gate:

```text
Claude Phase-B comparative review durably recorded
BEFORE
ChatGPT performs the final MC-0004 comparative synthesis / Phase-C handoff
```

---

## Important routing lesson from MC-0004

The first manual trigger for MC-0004 was too ambiguous:

```text
Check the repository and docs/model_collaboration/REVIEW_INBOX.md...
```

Claude remained oriented to an older branch whose inbox correctly said `NONE`, so it reconstructed stale collaboration state. No candidate Cockpit material was exposed and Phase-A independence was not compromised, but the event demonstrates that a cross-model handoff to work living only on an unpromoted branch must identify the target branch/ref explicitly.

For the current obligation, use:

```text
Open shakaarlatief/autonomous-data-science-system on branch
v1-cockpit-design-exploration, read docs/model_collaboration/REVIEW_INBOX.md
on that branch, and proceed with the pending MC-0004 review.
```

This operational lesson should be considered for canonical method promotion when MC-0004 is resolved; the inbox itself remains a convenience view rather than authority.

---

## Recently completed obligations

```text
MC-0002
    Claude review commit  9cf393f74e02e167d2f80c0381742ebd7e0c318e
    outcome               COLLABORATION_STATE_GUARD_ACCEPTED
    resolution            docs/model_collaboration/threads/MC-0002/RESOLUTION.md

MC-0003
    Claude review commit  e8e63faca8f2e181bdc389bf95a915f1d4cc42df
    outcome               deferred catch-up protocol accepted for current use
    resolution            docs/model_collaboration/threads/MC-0003/RESOLUTION.md

MC-0004 Phase A
    Claude proposal commit cd2e12f2c79ee3b2f205457c5940eb2022b4631a
    independence           BLIND_TO_CANDIDATE
    candidate exposures    none
```

---

## Catch-up rule

When pending obligations exist, a returning collaborator should normally process them by consequence and gate rather than simple creation time:

```text
1. review blocking target mutation / irreversible action
2. review blocking thread resolution or promotion
3. review with broad downstream dependency fan-out
4. ordinary required review
5. optional/advisory review
```

For each item, preserve the exact target head and separate disposition even if several related reviews are handled in one product session.

---

## Manual catch-up prompt rule

When the pending work exists only on an active/unpromoted branch, the manual trigger should name that branch explicitly rather than assuming the collaborator will discover it from a stale workspace state.

Current MC-0004 trigger:

```text
Open shakaarlatief/autonomous-data-science-system on branch
v1-cockpit-design-exploration, read docs/model_collaboration/REVIEW_INBOX.md
on that branch, and proceed with the pending MC-0004 review.
```

Scheduled unattended review execution is not part of the current method. Manual triggering remains sufficient at the present scale.

---

## Important limitation

This inbox remains a convenience view because Specification 024 does not encode explicit review-obligation/gate metadata.

It must never override a thread's authoritative state.

Long-term candidate direction, only if observed need justifies it:

```text
per-thread authoritative review obligation
        ↓
deterministic backlog discovery
        ↓
generated human-readable inbox
```

If this inbox and a thread disagree, the thread and exact repository evidence control and the inbox should be repaired.
