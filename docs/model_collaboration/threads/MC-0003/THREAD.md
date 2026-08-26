# MC-0003: Deferred Review Catch-Up Architecture

**Status:** RESOLVED / CLOSED  
**Topic:** Design and review asynchronous deferred-review/catch-up semantics  
**Task owner:** ChatGPT  
**Initial designer:** ChatGPT  
**Reviewer:** Claude  
**Human decision authority:** Project owner  
**Review mode:** REVIEWED  
**Active branch at resolution:** `v1-multimodel-development-collaboration`  
**Active PR at resolution:** #76  
**Live transport:** GitHub Issue #79  
**Target research:** `docs/research/036_deferred_asynchronous_review_and_catchup_architecture.md`  
**Operational protocol:** `docs/model_collaboration/DEFERRED_REVIEW_AND_CATCHUP.md`  
**Review inbox:** `docs/model_collaboration/REVIEW_INBOX.md`  
**Machine-readable state:** `docs/model_collaboration/threads/MC-0003/STATE.json`  
**Target-state write owner:** none, thread closed  
**Current phase:** CLOSED_ACCEPTED  
**Next expected participant:** none

## Why this thread existed

The user identified a concrete case not explicit enough in MC-0001: one model may remain available for multiple tasks while another model is temporarily unavailable, yet some of those tasks should still receive later review.

MC-0003 designed and pressure-tested that extension without reopening the resolved MC-0001 architecture as a whole.

## Accepted core

```text
collaborator unavailable
    !=
project globally blocked
```

unless the specific review gate for the affected task has been reached.

The accepted protocol supports:

```text
explicit review obligations
requirement separate from gate boundary
exact frozen review targets
multiple pending reviewer obligations
catch-up ordering
one-by-one versus bounded batch review
downstream reliance and impact sweeps
stale/superseded review targets
prospective-review contamination protection
human-readable review inbox as non-authoritative routing convenience
```

## Exact reviewed target

Claude reviewed:

```text
74fbf8f5dbf7b57bb5f3038b41122f20e09a4b53
```

rather than silently treating a later descendant as equivalent.

Durable review:

```text
docs/model_collaboration/threads/MC-0003/messages/002_claude_deferred_catchup_review.md
commit e8e63faca8f2e181bdc389bf95a915f1d4cc42df
```

## Review result

Claude found the design sound for current protocol use and identified three residual issues:

```text
F1  REQUIRED + NONE was semantically ambiguous
F2  REVIEW_INBOX consistency is not mechanically guarded
F3  downstream cross-thread dependency impact is prose-only
```

Task-owner disposition:

```text
F1  accepted and clarified prospectively
F2  accepted limitation; mechanization deferred pending real drift/scale
F3  highest-priority future mechanical gap; no Specification 025 yet
```

The pressure test itself succeeded operationally: MC-0002 and MC-0003 waited simultaneously for Claude, then Claude processed both in the inbox-defined order while keeping exact targets and findings separate.

## Scheduled unattended review

Scheduled/unattended Claude review execution was considered separately and is not part of the accepted current method. It remains a deferred option because it does not create extra subscription capacity and introduces unattended write/concurrency and clarification risks.

## Resolution route

```text
messages/002_claude_deferred_catchup_review.md
messages/003_chatgpt_review_disposition.md
RESOLUTION.md
```

MC-0003 is closed. The accepted protocol may be included in the canonical multi-model development-method promotion audit.