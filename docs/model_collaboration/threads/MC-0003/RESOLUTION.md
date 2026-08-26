# MC-0003 Resolution

**Thread:** MC-0003  
**Status:** RESOLVED / CLOSED  
**Resolution date:** 2026-08-26  
**Topic:** Deferred asynchronous review and catch-up architecture  
**Authority:** Collaboration-resolution provenance. The promoted collaboration protocol and Development Method govern current operation.

## Outcome

The deferred asynchronous catch-up pattern is accepted for current operational use.

Core rule:

```text
collaborator unavailable
    !=
project globally blocked
```

unless the specific review gate for the affected task has been reached.

The accepted pattern preserves:

```text
explicit review obligations
requirement separate from gate boundary
exact immutable review targets
multiple simultaneous pending review obligations
priority-based catch-up
one-by-one by default with bounded batching when justified
stale-target discipline
downstream impact analysis
protection of genuinely prospective/blind review gates
SOLO work without hidden review debt
```

## Empirical pressure test

MC-0002 and MC-0003 were simultaneously waiting for Claude while ChatGPT remained able to continue legitimate work.

Claude later processed both obligations in the inbox-defined order within one product session while preserving separate target heads, separate findings, and separate dispositions.

This directly supports the core asynchronous design rather than leaving it theoretical.

## Review findings retained

Claude's review at exact target:

```text
74fbf8f5dbf7b57bb5f3038b41122f20e09a4b53
```

identified:

```text
F1  REQUIRED + NONE was semantically ambiguous
F2  REVIEW_INBOX consistency is not mechanically guarded
F3  downstream cross-thread dependency impact is not machine-readable
```

Disposition:

```text
F1  corrected in the promoted protocol: NONE is valid only for OPTIONAL review
F2  accepted limitation; mechanization deferred until real drift/scale justifies it
F3  highest-priority future mechanical gap; no Specification 025 yet
```

## Scheduling decision

Unattended scheduled Claude review execution is not part of the current method. It remains a deferred option that may be revisited if product capabilities, concurrency safety, or usage economics materially change.

Manual triggering remains intentionally lightweight because the repository carries the catch-up state.

## No premature mechanical extension

Specification 024 is not retroactively expanded. No Specification 025 is opened at this boundary.

Future mechanization should be justified by real evidence such as repeated review-inbox drift, non-trivial cross-thread dependency chains, or reviewer-backlog scale that makes the current explicit process unreliable.