# MC-0003: Deferred Review Catch-Up Architecture

**Status:** OPEN  
**Topic:** Design and later review asynchronous deferred-review/catch-up semantics  
**Task owner:** ChatGPT  
**Initial designer:** ChatGPT  
**Reviewer:** Claude  
**Human decision authority:** Project owner  
**Review mode:** REVIEWED  
**Active branch:** `v1-multimodel-development-collaboration`  
**Active PR:** #76  
**Live transport:** GitHub Issue #79  
**Target research:** `docs/research/036_deferred_asynchronous_review_and_catchup_architecture.md`  
**Operational protocol:** `docs/model_collaboration/DEFERRED_REVIEW_AND_CATCHUP.md`  
**Review inbox:** `docs/model_collaboration/REVIEW_INBOX.md`  
**Machine-readable state:** `docs/model_collaboration/threads/MC-0003/STATE.json`  
**Target-state write owner:** ChatGPT  
**Allowed reviewer write surface:** new immutable files under `docs/model_collaboration/threads/MC-0003/messages/`  
**Current phase:** DEFERRED_REVIEW_QUEUED  
**Next expected participant:** Claude

## Why this thread exists

The user identified a concrete case not explicit enough in MC-0001: one model may remain available for multiple tasks while another model is temporarily unavailable, yet some of those tasks should still receive later review.

This thread develops that extension without reopening the resolved MC-0001 architecture as a whole.

## Core question

```text
How can ADS let one collaborator keep progressing
without either globally blocking on an unavailable reviewer
or silently losing intended later review?
```

## Candidate direction frozen for review

The candidate design now proposes:

```text
explicit review obligations
review requirement separate from gate boundary
exact frozen review targets
multiple pending reviewer obligations
catch-up ordering
one-by-one versus batch review
downstream reliance and impact sweeps
stale/superseded review targets
prospective-review contamination protection
human-readable review inbox as non-authoritative routing convenience
future deterministic backlog discovery from per-thread state
```

## Exact review target

The candidate architecture was frozen before the review request at:

```text
74fbf8f5dbf7b57bb5f3038b41122f20e09a4b53
```

Claude's later review must be explicit about reviewing that frozen target. Descendant commits are not automatically covered.

## Review obligation

```text
requirement   REQUIRED
gate          BEFORE_MULTI_MODEL_METHOD_PROMOTION
priority      NORMAL
status        PENDING
```

This means Claude review is required before the deferred-review/catch-up architecture becomes part of the promoted multi-model Development Method, but Claude's immediate availability is not required for unrelated bounded work to continue.

## Relationship to Specification 024

Specification 024 remains frozen and awaits MC-0002 review.

MC-0003 uses the existing V1 `STATE.json` mechanics for ownership and next-actor routing, but it does not pretend that Specification 024 already encodes review-gate semantics that were not part of its frozen contract.

Any mechanical schema extension belongs in a later prospective specification after this design is reviewed.

## Review priority relative to MC-0002

MC-0002 should normally be reviewed first because Specification 024 classification depends on it.

MC-0003 review is required before final promotion of the multi-model collaboration method, but it does not block unrelated current work.

This gives the repository its first intentional multiple-item Claude catch-up backlog:

```text
MC-0002  higher-priority pending implementation review
MC-0003  normal-priority deferred architecture review
```

## Expected later Claude artifact

```text
docs/model_collaboration/threads/MC-0003/messages/002_claude_deferred_catchup_review.md
```

Claude should review the frozen Research 036 / protocol target, identify any required corrections, and challenge whether the proposal is too weak or too complex.

## Review focus

```text
1. Is requirement-vs-gate-boundary separation sufficient?
2. Are the candidate gate boundaries the right ones?
3. Does the review inbox create dangerous duplicate authority?
4. Is exact review-target freezing strong enough for delayed review?
5. Is downstream reliance / impact-sweep handling sufficient?
6. Are one-by-one and batch catch-up rules proportionate?
7. Are prospective/blind review protections strong enough?
8. Should any mechanical extension be smaller or larger than proposed?
9. Can several pending threads coexist safely without global collaborator locking?
10. What is the strongest failure mode still missing?
```

## Sequence from here

```text
MC-0003 waits for Claude
    while unrelated legitimate bounded work may continue

when Claude is available:
    MC-0002 normally first
    then MC-0003

Claude reviews exact MC-0003 target
    -> writes message 002 only
    -> ChatGPT integrates/routs findings
    -> only then consider later mechanical specification / promotion
```
