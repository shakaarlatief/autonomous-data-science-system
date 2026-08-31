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

### MC-0008: comparative repository governed-document integrity review

```text
reviewer                  Claude / claude-02
conversation title        02 - Repository Governance & Integrity
mode                      INDEPENDENT_THEN_COMPARATIVE
coordination branch       v1-source-vault-bootstrap-resume
exact pre-proposal ref    7794951cbedd16f2fd1a27170946aa59b952e27a
independent proposal      messages/001_claude_independent_governed_document_integrity_proposal.md
candidate for comparison  messages/002_chatgpt_task_owner_disposition_and_candidate_integrity_architecture.md
phase                     WAITING_FOR_COMPARATIVE_REVIEW
next actor                Claude
write scope               docs/model_collaboration/threads/MC-0008/messages/** only
```

Purpose:

```text
compare the frozen ChatGPT candidate against Claude's already-preserved independent position
identify genuine convergence and material disagreement
challenge expanded V1 scope around validation/evidence, collaboration provenance, live-state freshness, reference existence, aggregate gating and private sync
identify candidate overreach, omissions and any must-fix issue before canonical promotion or implementation
```

Durable routing:

```text
docs/model_collaboration/threads/MC-0008/BRIEF.md
docs/model_collaboration/threads/MC-0008/THREAD.md
docs/model_collaboration/threads/MC-0008/STATE.json
docs/model_collaboration/threads/MC-0008/messages/001_claude_independent_governed_document_integrity_proposal.md
docs/model_collaboration/threads/MC-0008/messages/002_chatgpt_task_owner_disposition_and_candidate_integrity_architecture.md
```

Expected comparative response:

```text
docs/model_collaboration/threads/MC-0008/messages/003_claude_comparative_governed_document_integrity_review.md
```

MC-0008 blocks implementing or canonically promoting the new repository-wide metadata/reference-integrity mechanism until the comparative pass is preserved and dispositioned. It is not a Source Universe data-integrity defect. The project owner has chosen to complete this repository-preservation reflection before returning to permanent source ingestion.

## Most recently completed obligations

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

Durable records:

```text
docs/model_collaboration/threads/MC-0007/BRIEF.md
docs/model_collaboration/threads/MC-0007/messages/001_claude_code_source_hardening_verification.md
docs/model_collaboration/threads/MC-0007/RESOLUTION.md
docs/model_collaboration/threads/MC-0007/STATE.json
docs/model_collaboration/threads/MC-0007/THREAD.md
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

Durable records:

```text
docs/model_collaboration/threads/MC-0006/messages/001_claude_source_universe_architecture_review.md
docs/model_collaboration/threads/MC-0006/messages/002_chatgpt_task_owner_disposition.md
docs/model_collaboration/threads/MC-0006/RESOLUTION.md
docs/model_collaboration/threads/MC-0006/STATE.json
docs/model_collaboration/threads/MC-0006/THREAD.md
```

The Source Universe architecture remains accepted. The four narrow partial-failure/operator-recovery findings were independently dispositioned, implemented, directly regression-tested, and exercised on the real local Windows checkout without touching the permanent vault.

## Deferred product collaboration

### MC-0004: next-generation Project Cockpit design exploration

```text
status        DEFERRED by project-owner routing decision at Checkpoint 267
target branch v1-cockpit-design-exploration
frozen head   04f2a907094b8023ac7377c399a6eef1a6e1da99
resume        only when the project owner explicitly returns to frontend work
```

There is no pending Claude obligation inside MC-0004. The thread is preserved as the future Cockpit collaboration/recovery surface, not as an active blocker on the resumed Source Vault bootstrap.

## Earlier completed obligations

MC-0005 remains closed with `SUPPORT_WITH_NONBLOCKING_IMPROVEMENTS`. MC-0001 through MC-0003 remain preserved in their thread records and are not repeated here.
