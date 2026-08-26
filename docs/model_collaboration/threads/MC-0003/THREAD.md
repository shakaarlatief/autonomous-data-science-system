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
**Current phase:** DESIGN_ACTIVE  
**Next expected participant:** ChatGPT

## Why this thread exists

The user identified a concrete case not explicit enough in MC-0001: one model may remain available for multiple tasks while another model is temporarily unavailable, yet some of those tasks should still receive later review.

This thread develops that extension without reopening the resolved MC-0001 architecture as a whole.

## Core question

```text
How can ADS let one collaborator keep progressing
without either globally blocking on an unavailable reviewer
or silently losing intended later review?
```

## Candidate direction under construction

The candidate design explores:

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

## Relationship to Specification 024

Specification 024 remains frozen and awaits MC-0002 review.

MC-0003 may use the existing V1 `STATE.json` mechanics for ownership and next-actor routing, but it must not pretend that Specification 024 already encodes review-gate semantics that were not part of its frozen contract.

Any mechanical schema extension belongs in a later prospective specification after this design is reviewed.

## Intended scheduling behavior

MC-0003 is deliberately a deferrable review item.

ChatGPT may complete and freeze the candidate design now. Claude does not need to be immediately available.

After the review target is frozen:

```text
MC-0003 -> WAITING for Claude
```

while other legitimate bounded tasks may continue.

This is itself the first direct pressure test of the new concept.

## Review priority relative to MC-0002

MC-0002 should normally be reviewed first because Specification 024 classification depends on it.

MC-0003 review is required before final promotion of the multi-model collaboration method, but it does not block unrelated current work.

## Expected later Claude artifact

```text
docs/model_collaboration/threads/MC-0003/messages/002_claude_deferred_catchup_review.md
```

Claude should review the frozen Research 036 / protocol target, identify any required corrections, and challenge whether the proposal is too weak or too complex.

## Current sequence

```text
ChatGPT freezes candidate design
    -> exact review target recorded
    -> MC-0003 transitions to WAITING
    -> REVIEW_INBOX exposes the obligation
    -> ChatGPT may continue legitimate work
    -> Claude later catches up after MC-0002
    -> findings integrated / routed
    -> only after review consider a later mechanical specification
```
