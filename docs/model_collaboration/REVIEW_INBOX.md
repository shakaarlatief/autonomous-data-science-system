# Model Collaboration Review Inbox

**Date:** 2026-08-26  
**Status:** Current human-readable routing view  
**Authority:** Convenience index only. Per-thread `STATE.json`, `THREAD.md`, frozen review requests, exact Git refs, and resolution records remain authoritative.  
**Purpose:** Let a returning collaborator discover pending review/catch-up obligations without relying on private chat memory.

## Current pending obligations

```text
NONE
```

MC-0004 no longer has a pending Claude review obligation. Phase A and Phase B are both durably preserved, and the thread has moved to Phase C realistic mockup evaluation with ChatGPT as the next expected actor.

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

MC-0004 Phase B
    Claude review commit   d94d696214a41d2a3904aa9ce2a42bdab5f2f3ce
    classification         COMPARATIVE_ONLY
    message                docs/model_collaboration/threads/MC-0004/messages/002_claude_comparative_review.md
    write-boundary check   only the declared message file changed

MC-0004 synthesis
    artifact               docs/research/038_mc0004_comparative_cockpit_design_synthesis_and_mockup_direction_set.md
    current phase          PHASE_C_MOCKUP_EVALUATION
```

---

## Important routing lesson from MC-0004

The first manual trigger for MC-0004 was too ambiguous:

```text
Check the repository and docs/model_collaboration/REVIEW_INBOX.md...
```

Claude remained oriented to an older branch whose inbox correctly said `NONE`, so it reconstructed stale collaboration state.

No candidate Cockpit material was exposed and Phase-A independence was not compromised.

Empirical lesson:

```text
cross-model handoff to work living only on an unpromoted branch
    -> explicitly identify repository + branch/ref + thread/routing surface
```

This lesson should be reconsidered for canonical method promotion when MC-0004 is resolved. The inbox remains a convenience view rather than authority.

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

When pending work exists only on an active/unpromoted branch, the manual trigger should name that branch explicitly rather than assuming the collaborator will discover it from a stale workspace state.

Scheduled unattended review execution is not part of the current method. Manual triggering remains sufficient at the present scale.

---

## Important limitation

This inbox remains a convenience view because Specification 024 does not encode explicit review-obligation/gate metadata.

It must never override a thread's authoritative state.

Long-term candidate direction, only if observed need justifies it:

```text
per-thread authoritative review obligation
        ->
deterministic backlog discovery
        ->
generated human-readable inbox
```

If this inbox and a thread disagree, the thread and exact repository evidence control and the inbox should be repaired.
