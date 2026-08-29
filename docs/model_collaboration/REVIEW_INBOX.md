# Model Collaboration Review Inbox

**Date:** 2026-08-29  
**Status:** Current human-readable routing view  
**Authority:** Convenience index only. Per-thread `STATE.json`, `THREAD.md`, frozen requests, exact Git refs and resolution records remain authoritative.  
**Repository:** `shakaarlatief/autonomous-data-science-system`  
**Coordination branch:** `v1-cockpit-design-exploration`

## Routing discipline

The repository and coordination branch above must be named explicitly in any human-to-Claude trigger prompt.

Claude should not infer or switch the coordination branch. If a trigger names a different branch than this routing state, Claude should stop and report the mismatch rather than choose a branch heuristically.

Live ADS product/checkpoint state belongs in:

```text
docs/CURRENT_STATE.md
docs/current_routing.json
```

This inbox intentionally does not duplicate that state except where needed to explain whether a collaboration obligation blocks it.

## Pending model obligation

### MC-0005: Development Method v0.7 repository information architecture review

```text
reviewer            Claude
review mode         ADVERSARIAL_REVIEW
coordination branch v1-cockpit-design-exploration
exact review target c834d8298b86a0185ffcc0ffa62d0e9c178cc2ad
priority            normal
review gate         NONE / non-blocking
next actor          Claude
```

Read:

```text
docs/model_collaboration/threads/MC-0005/BRIEF.md
docs/model_collaboration/threads/MC-0005/THREAD.md
docs/model_collaboration/threads/MC-0005/STATE.json
```

Expected durable Claude output:

```text
docs/model_collaboration/threads/MC-0005/messages/001_claude_v07_information_architecture_review.md
```

The review asks Claude to challenge the responsibility split among the global canonical files, the semantic-only Knowledge Map, exhaustive topic routing, checkpoint semantic ranges, specialized indexes, authority/supersession rules, validators and scaling behavior.

It is intentionally non-blocking. Checkpoint 266 remains complete unless the eventual review produces a substantive finding that is later accepted through normal governance.

## Standard Claude trigger

Send exactly this short routing prompt from the Claude project/workspace:

```text
Work in repository `shakaarlatief/autonomous-data-science-system`.
Coordination branch: `v1-cockpit-design-exploration`.

Read `docs/current_routing.json` and `docs/model_collaboration/REVIEW_INBOX.md`
from that exact branch, then follow the referenced MC-0005 thread/request files and
proceed with the pending Claude obligation.

Do not infer or switch the coordination branch. If the named branch is missing,
or authoritative routing on that branch contradicts this prompt, stop and report
the mismatch instead of choosing another branch.
```

## Completed prior obligations

Previous Claude obligations in MC-0001 through MC-0004 remain preserved in their thread records and are not repeated here.
