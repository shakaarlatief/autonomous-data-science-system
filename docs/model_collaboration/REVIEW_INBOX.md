# Model Collaboration Review Inbox

**Date:** 2026-08-31  
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

This inbox intentionally does not duplicate that state except where needed to explain collaboration obligations.

## Pending model obligation

There is currently **no pending Claude obligation** in the active repository-preservation review.

MC-0008 completed both the independent and comparative phases. The next work belongs to normal ChatGPT task-owner governance: promote the accepted architecture through Research/Specification, implement it, repair known continuity/routing drift, and verify the resulting repository/chat-rotation gate.

## Most recently completed obligation

### MC-0008: repository governed-document metadata/reference-integrity architecture

```text
reviewer / counter-designer  Claude / claude-02
mode                         INDEPENDENT_THEN_COMPARATIVE
coordination branch          v1-source-vault-bootstrap-resume
frozen independent target    7794951cbedd16f2fd1a27170946aa59b952e27a
independent proposal commit  dbb3336f1b33e2409b3b4d96aba2d862573a154e
ChatGPT candidate commit     11a4520adaf83491f4e2063449ba9b4cbf631c2c
comparative review commit    acb0f80932441cacd324cbda1b29b8a530f73743
comparative result           SUPPORT_WITH_5_BOUNDED_AMENDMENTS
final disposition            ALL 5 AMENDMENTS ACCEPTED / ARCHITECTURE RECONCILED
status                       RESOLVED
```

Durable records:

```text
docs/model_collaboration/threads/MC-0008/BRIEF.md
docs/model_collaboration/threads/MC-0008/messages/001_claude_independent_governed_document_integrity_proposal.md
docs/model_collaboration/threads/MC-0008/messages/002_chatgpt_task_owner_disposition_and_candidate_integrity_architecture.md
docs/model_collaboration/threads/MC-0008/messages/003_claude_comparative_governed_document_integrity_review.md
docs/model_collaboration/threads/MC-0008/messages/004_chatgpt_final_reconciliation_and_accepted_integrity_architecture.md
docs/model_collaboration/threads/MC-0008/RESOLUTION.md
docs/model_collaboration/threads/MC-0008/STATE.json
docs/model_collaboration/threads/MC-0008/THREAD.md
```

Accepted direction includes family-aware prospective metadata contracts, numbered-identity uniqueness, declared-reference checks, branch-scoped live-state freshness, public aggregate repository-integrity validation, separate private-continuity status and chat-rotation preflight. Heavy universal metadata machinery remains rejected for V1.

## Earlier completed obligations

### MC-0007: Source Universe pre-deployment recovery hardening and Windows verification

```text
implementer/verifier   Claude Code / claude-code-01
mode                   COORDINATED_HANDOFF
implementation base    65bf6198ea77565551e4c4dabe690ce204497d79
implementation commit  a992fef2eda95109dacd06ee491f4604e6d11891
execution report       7ee480709aa1627cc770ebb4f229a3f82b189448
result                 F1-F4 FIXED / VERIFIED
status                 CLOSED / ACCEPTED
```

### MC-0006: Source Universe architecture and permanent Source Vault deployment review

```text
reviewer             Claude / claude-01
exact review target  4ee6b2a1ae9f2856c76ef7d3219031bd4acd364c
review result         YES, WITH PRECONDITIONS
must-fix architecture none
accepted hardening    F1-F4, completed through MC-0007
status                CLOSED / ARCHITECTURE RETAINED
```

MC-0005 remains closed with `SUPPORT_WITH_NONBLOCKING_IMPROVEMENTS`. MC-0001 through MC-0003 remain preserved in their thread records and are not repeated here.

## Deferred product collaboration

### MC-0004: next-generation Project Cockpit design exploration

```text
status        DEFERRED by project-owner routing decision at Checkpoint 267
target branch v1-cockpit-design-exploration
frozen head   04f2a907094b8023ac7377c399a6eef1a6e1da99
resume        only when the project owner explicitly returns to frontend work
```

There is no pending Claude obligation inside MC-0004.
