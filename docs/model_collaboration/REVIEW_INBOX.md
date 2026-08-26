# Model Collaboration Review Inbox

**Date:** 2026-08-26  
**Status:** Current human-readable routing view  
**Authority:** Convenience index only. Per-thread `STATE.json`, `THREAD.md`, frozen review requests, exact Git refs, and resolution records remain authoritative.  
**Purpose:** Let a returning collaborator discover pending review/catch-up obligations without relying on private chat memory.

## Current pending obligations

```text
NONE
```

MC-0002 and MC-0003 were both completed by Claude in the inbox-defined order on 2026-08-26 and subsequently resolved by the task owner.

Completed route:

```text
MC-0002
    Claude review commit  9cf393f74e02e167d2f80c0381742ebd7e0c318e
    outcome               COLLABORATION_STATE_GUARD_ACCEPTED
    resolution            docs/model_collaboration/threads/MC-0002/RESOLUTION.md

MC-0003
    Claude review commit  e8e63faca8f2e181bdc389bf95a915f1d4cc42df
    outcome               deferred catch-up protocol accepted for current use
    resolution            docs/model_collaboration/threads/MC-0003/RESOLUTION.md
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

## Standardized manual catch-up prompt

When this inbox contains pending Claude work, the current low-friction user prompt is:

```text
Check the repository and docs/model_collaboration/REVIEW_INBOX.md, then proceed with the pending Claude reviews in order.
```

The equivalent instruction may be used for another collaborator by naming the relevant pending work if the inbox contains mixed obligations.

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