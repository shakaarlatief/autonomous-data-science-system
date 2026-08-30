# Model Collaboration Review Inbox

**Date:** 2026-08-30  
**Status:** Current human-readable routing view  
**Authority:** Convenience index only. Per-thread `STATE.json`, `THREAD.md`, frozen requests, exact Git refs and resolution records remain authoritative.  
**Repository:** `shakaarlatief/autonomous-data-science-system`  
**Coordination branch:** `v1-source-vault-bootstrap-resume`

## Routing discipline

The repository and coordination branch above must be named explicitly in any human-to-model trigger prompt.

A collaborator should not infer or switch the coordination branch. If a trigger names a different branch than this routing state, the collaborator should stop and report the mismatch rather than choose a branch heuristically.

Live ADS product/checkpoint state belongs in:

```text
docs/CURRENT_STATE.md
docs/current_routing.json
```

This inbox intentionally does not duplicate that state except where needed to explain whether a collaboration obligation blocks it.

## Pending model obligation

### MC-0006: Source Universe architecture and permanent Source Vault deployment review

```text
reviewer            Claude / claude-01
review environment  normal Claude Project with full repository connector access
review mode         ADVERSARIAL_REVIEW
exact review target 4ee6b2a1ae9f2856c76ef7d3219031bd4acd364c
coordination branch v1-source-vault-bootstrap-resume
status              ACTIVE / REVIEW REQUEST OPEN
blocks              first permanent Source Registry / Source Vault write
non-blocking for    disk cleanup, free-space investigation, candidate private-location planning
```

Durable request:

```text
docs/model_collaboration/threads/MC-0006/BRIEF.md
docs/model_collaboration/threads/MC-0006/THREAD.md
docs/model_collaboration/threads/MC-0006/STATE.json
docs/model_collaboration/threads/MC-0006/messages/ENVIRONMENT_SELECTION.md
```

Expected Claude output:

```text
docs/model_collaboration/threads/MC-0006/messages/001_claude_source_universe_architecture_review.md
```

Normal Claude trigger:

```text
Work in repository `shakaarlatief/autonomous-data-science-system`.
Coordination branch: `v1-source-vault-bootstrap-resume`.

Read `docs/current_routing.json` and `docs/model_collaboration/REVIEW_INBOX.md`
from that exact branch, then follow the referenced MC-0006 brief/thread/state files and
perform the pending Source Universe architecture review against the exact frozen target.

Use the connected repository as the evidence base. Do not infer or switch the coordination branch.
Do not mutate the review target. Write only the review output permitted by MC-0006.
Where a conclusion genuinely requires local execution evidence rather than repository inspection,
identify the smallest targeted verification needed instead of performing deployment work.
If the named branch or authoritative routing contradicts this prompt, stop and report the mismatch.
```

Claude Code is not the substantive MC-0006 reviewer. It remains available for later narrow execution-based verification and Windows-local bootstrap/deployment tasks if MC-0006 identifies evidence gaps that cannot be resolved through repository inspection alone.

## Deferred product collaboration

### MC-0004: next-generation Project Cockpit design exploration

```text
status        DEFERRED by project-owner routing decision at Checkpoint 267
target branch v1-cockpit-design-exploration
frozen head   04f2a907094b8023ac7377c399a6eef1a6e1da99
resume        only when the project owner explicitly returns to frontend work
```

There is no pending Claude obligation inside MC-0004. The thread is preserved as the future Cockpit collaboration/recovery surface, not as an active blocker on the resumed Source Vault bootstrap.

## Most recently completed obligation

### MC-0005: Development Method v0.7 repository information architecture review

```text
reviewer            Claude
review mode         ADVERSARIAL_REVIEW
exact review target c834d8298b86a0185ffcc0ffa62d0e9c178cc2ad
review result        SUPPORT_WITH_NONBLOCKING_IMPROVEMENTS
must-fix findings    none
status               CLOSED / ACCEPTED WITH NON-BLOCKING IMPROVEMENTS
```

Durable records:

```text
docs/model_collaboration/threads/MC-0005/messages/001_claude_v07_information_architecture_review.md
docs/model_collaboration/threads/MC-0005/RESOLUTION.md
docs/model_collaboration/threads/MC-0005/STATE.json
```

The review supported the v0.7 architecture, identified one cheap Subject-index-versus-`KM-TOPIC` validation gap for immediate follow-up, clarified that exhaustive routing coverage is not semantic-routing correctness, and preserved checkpoint-range coarseness plus frontmatter-generated routing as future scale watchpoints rather than current blockers.

## Completed prior obligations

MC-0001 through MC-0003 remain preserved in their thread records and are not repeated here. MC-0004 is currently deferred rather than completed.
