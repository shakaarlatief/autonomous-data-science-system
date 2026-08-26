# Model Collaboration Review Inbox

**Date:** 2026-08-26  
**Status:** Candidate human-readable routing view  
**Authority:** Convenience index only. Per-thread `STATE.json`, `THREAD.md`, frozen review requests, and exact Git refs remain authoritative.  
**Purpose:** Let a returning collaborator discover pending review/catch-up obligations without relying on private chat memory.

## Current pending Claude obligations

### 1. MC-0002: Specification 024 implementation review

```text
status                 PENDING
requirement            REQUIRED
gate                    BEFORE_SPECIFICATION_024_CLASSIFICATION
priority                HIGHER
target head             a9efc43d7c441c8283d2cd954cc6fa1abd021689
thread                  docs/model_collaboration/threads/MC-0002/
live transport          GitHub Issue #78
expected output         messages/002_claude_implementation_review.md
```

Why first:

Specification 024 cannot be classified until MC-G16 direct review is completed. This is therefore the higher-priority catch-up item.

### 2. MC-0003: deferred asynchronous review/catch-up architecture

```text
status                 PREPARING_REVIEW_TARGET
requirement            REQUIRED
gate                    BEFORE_MULTI_MODEL_METHOD_PROMOTION
priority                NORMAL
target head             to be frozen after ChatGPT candidate design commit
thread                  docs/model_collaboration/threads/MC-0003/
live transport          GitHub Issue #79
expected output         messages/002_claude_deferred_catchup_review.md
```

Why deferrable:

This architecture extension should receive Claude challenge before the collaboration method is promoted, but Claude's immediate availability is not required for ChatGPT to preserve the candidate design or continue unrelated bounded work.

---

## Catch-up rule

When Claude returns, it should normally process:

```text
MC-0002 first
    because it blocks Specification 024 classification

then MC-0003
    because it blocks final collaboration-method promotion,
    not current unrelated bounded work
```

If a new pending item has an earlier or more consequential gate, ordering may change and the reason should be recorded.

---

## Important limitation

This inbox is currently maintained as a convenience view because Specification 024 does not yet encode explicit review-obligation/gate metadata.

It must never override a thread's authoritative state.

Long-term candidate direction:

```text
per-thread authoritative review obligation
        ↓
deterministic backlog discovery
        ↓
generated human-readable inbox
```

rather than two independently editable sources of truth.