# Checkpoint 401: Semantic Git Commit Failure-Atomic Index Restoration Qualified, GitHub Fresh-Host Next

**Date:** 2026-09-09
**Status:** PASS / RECURRING OWNER MANUAL UNSTAGE GAP CLOSED / RESEARCH 123 BOUNDARY RESTORED
**Checkpoint class:** INFRASTRUCTURE
**Project stage:** Research 123 active; Research 116 accepted semantic-Git reliability follow-up closed
**Scope:** Preserve the preview.29 failure-atomic semantic commit correction and live proof that a guarded post-staging failure restores the initially empty index without discarding working-tree edits or requiring an owner-side Git command.
**Authority:** Validation 158 owns the detailed implementation, regression, release and live-reproduction evidence. Research 116 owns the durable semantic Git architecture. Research 123 remains the active stage and owns the resumed next boundary.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** chatgpt-21
**Conversation title:** 21 - GitHub Device Flow Recovery and Authorization Diagnosis
**Primary collaborator:** ChatGPT

The recurring manual `git restore --staged -- .` interruption was localized to `codex.git_commit_paths`: its old contract intentionally left its exact staging behind when a later guard failed. That was fail-closed with respect to commit creation, but not failure-atomic with respect to the Git index.

Private local-runtime head `ffb0356acb0dc69024146869c5bebe0ee76de5a3` preserves immutable release `semantic-git-transactional-commit-v1`. Publication passed the full bounded release matrix, restart activated `0.1.1-preview.29-semantic-git-transactional-commit` without recovery, and postactivation verification reports 68 tools, one runtime dependency and zero mismatches.

The new semantic commit transaction restores only its own declared staged scope through `git restore --staged --source=HEAD -- <declared paths>` when HEAD is still exactly unchanged. It verifies the staged scope before cleanup and an empty index afterward while preserving working-tree edits. Cleanup uncertainty fails as `GIT_COMMIT_PATHS_ROLLBACK_FAILED`; a changed HEAD after an uncertain commit result is never auto-rolled back. No broad reset, history rewrite, arbitrary Git routing or new general public unstage authority was added.

A focused regression passed the exact trailing-whitespace failure plus corrected retry sequence. Preview.29 was then tested through the live public semantic tool itself: a deliberately invalid Validation 158 draft failed `git diff --cached --check`, and the returned structured details reported `indexRestored=true`, `rollbackAttempted=true`, and the bounded restore contract. Immediate reconciliation proved the index empty, HEAD unchanged and the working-tree file preserved. The corrected checkpoint preservation commit was then able to run without any owner manual unstage.

Research 123 is not displaced by this reliability correction. Its pre-existing Checkpoint 400 boundary resumes unchanged: refresh/rescan `Codexless Runtime Bridge`, open a fresh disposable ChatGPT conversation, and qualify the four already-live read-only GitHub foundation actions through the host projection before proceeding to additional GitHub actions or mutations.

```text
CHECKPOINT401=SEMANTIC_GIT_COMMIT_FAILURE_ATOMIC_INDEX_RESTORATION_QUALIFIED
LIVE_RUNTIME_VERSION=0.1.1-preview.29-semantic-git-transactional-commit
PRIVATE_RUNTIME_HEAD=ffb0356acb0dc69024146869c5bebe0ee76de5a3
FAILED_GUARDED_COMMIT_AUTO_UNSTAGE=PASS
WORKING_TREE_PRESERVATION=PASS
MANUAL_OWNER_UNSTAGE_NORMAL_PATH=ELIMINATED
GENERAL_RESET_AUTHORITY=NOT_ADDED
RESEARCH123=ACTIVE
NEXT=FRESH_CHAT_GITHUB_READONLY_FOUNDATION_SCHEMA_AND_LIVE_READ_QUALIFICATION
```
