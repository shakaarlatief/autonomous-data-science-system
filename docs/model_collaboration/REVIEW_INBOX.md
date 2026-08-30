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

### MC-0007: Source Universe pre-deployment recovery hardening and Windows verification

```text
implementer/verifier  Claude Code / claude-code-01
mode                  COORDINATED_HANDOFF
implementation base   65bf6198ea77565551e4c4dabe690ce204497d79
coordination branch   v1-source-vault-bootstrap-resume
status                ACTIVE
blocks                first permanent Source Registry / Source Vault write
non-blocking for      disk cleanup, free-space investigation, candidate private-location planning
```

Durable task:

```text
docs/model_collaboration/threads/MC-0007/BRIEF.md
docs/model_collaboration/threads/MC-0007/THREAD.md
docs/model_collaboration/threads/MC-0007/STATE.json
```

Expected Claude Code output:

```text
docs/model_collaboration/threads/MC-0007/messages/001_claude_code_source_hardening_verification.md
```

Claude Code trigger:

```text
Work in repository `shakaarlatief/autonomous-data-science-system`.
Coordination branch: `v1-source-vault-bootstrap-resume`.

Read `docs/current_routing.json` and `docs/model_collaboration/REVIEW_INBOX.md`
from that exact branch, then follow MC-0007's BRIEF.md, THREAD.md and STATE.json.

Implement and verify only the accepted Source Universe pre-deployment recovery hardening
against the exact MC-0007 implementation base. Respect the declared target write paths.
Run the required provider-free tests on this local Windows checkout and write the single
MC-0007 execution report permitted by the thread.

Do not create or migrate the permanent Source Registry, do not write the permanent Source Vault,
do not modify the original educational corpus, and do not perform the real permanent backup/restore.
If the branch, base, write-surface ownership or authoritative routing contradicts this prompt,
stop and report the mismatch rather than improvising.
```

## Waiting parent review

### MC-0006: Source Universe architecture and permanent Source Vault deployment review

```text
reviewer             Claude / claude-01
exact review target  4ee6b2a1ae9f2856c76ef7d3219031bd4acd364c
review result         YES, WITH PRECONDITIONS
must-fix architecture none
accepted hardening    F1-F4
status                WAITING / EXECUTION FOLLOW-UP PENDING
```

Claude's review is complete. ChatGPT independently traced and accepted F1-F4 while retaining the Source Universe architecture. MC-0006 now waits only for the separately scoped MC-0007 implementation/Windows evidence and final task-owner resolution.

Durable records:

```text
docs/model_collaboration/threads/MC-0006/messages/001_claude_source_universe_architecture_review.md
docs/model_collaboration/threads/MC-0006/messages/002_chatgpt_task_owner_disposition.md
docs/model_collaboration/threads/MC-0006/THREAD.md
docs/model_collaboration/threads/MC-0006/STATE.json
```

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
