# Validation 158: Semantic Git Commit Failure-Atomic Index Restoration Qualified

**Date:** 2026-09-09
**Status:** PASS / PREVIEW.29 LIVE / AUTOMATIC INDEX RESTORATION QUALIFIED
**Research:** Research 116 accepted operational follow-up during active Research 123
**Scope:** Close the recurring owner-manual `git restore --staged -- .` recovery gap left by `codex.git_commit_paths` when a guarded commit failed after exact staging but before a commit was created.

## 1. Root cause

The existing semantic commit contract required an initially empty Git index, staged only the declared paths, then ran later guards such as `git diff --cached --check`. If one of those later guards failed, the operation correctly refused to commit but deliberately preserved the staged index. That created a durable side effect from an otherwise failed semantic operation and blocked the next guarded commit with `GIT_COMMIT_PATHS_PRECONDITION_FAILED` until the owner manually ran an unstage command.

The recurring manual step was therefore a Runtime Bridge lifecycle defect, not an inherent Git requirement and not an owner responsibility that should remain in the normal workflow.

## 2. Accepted failure-atomic contract

`codex.git_commit_paths` still requires an empty index before it starts. Once its own exact staging begins, a definite pre-commit or commit failure now attempts a bounded restoration of only the declared transaction scope.

The restoration path is exactly:

```text
git restore --staged --source=HEAD -- <declared paths>
```

Automatic restoration is attempted only when the current HEAD can still be proven equal to the pre-call `expectedHead`. Before restoring, Codexless inspects the staged set and refuses automatic cleanup if the index contains a path outside the declared transaction scope. After restoring, it verifies that the index is empty. Working-tree edits are intentionally preserved.

The implementation does not use `git reset --hard`, checkout, branch movement, amend, rebase, force update, history rewrite, arbitrary ref selection, caller-selected Git routing, or a general host Git escape hatch.

If cleanup itself cannot be verified, the operation fails visibly with:

```text
GIT_COMMIT_PATHS_ROLLBACK_FAILED
```

and preserves the original failure code/message inside structured diagnostic details.

For a commit-result uncertainty, Codexless first reconciles HEAD. If HEAD is unchanged, bounded index restoration is allowed. If HEAD changed, Codexless does not risk undoing index state because the commit may actually have succeeded. That case remains fail-visible rather than being auto-retried or auto-reset.

## 3. Private runtime implementation and focused regression

Private local-runtime source head:

```text
ffb0356acb0dc69024146869c5bebe0ee76de5a3
```

Immutable release:

```text
releaseId               semantic-git-transactional-commit-v1
targetVersion           0.1.1-preview.29-semantic-git-transactional-commit
targetSurfaceVersion    codexless-public-preview-v2
targetToolCount         68
fileCount               3
runtimeDependencyCount  1
manifestSha256          6584ed40ad55547a1515ac09ca27492f422674a0b387028980455be5ecf8673c
```

The focused semantic Git regression now creates a real temporary Git fixture, writes trailing whitespace to a declared path, invokes `commitPaths`, verifies `GIT_COMMIT_PATHS_DIFF_CHECK_FAILED`, verifies automatic index restoration, confirms the working-tree edit remains, fixes the file, and retries the same semantic commit without any manual unstage. The retry succeeds.

```text
PASS commit diff-check failure restores the initially empty index and allows retry without manual unstage
FLEXIBLE_AUTHORITY_REGRESSION=PASS tests=12
```

## 4. Release qualification

Preparation succeeded with one exact runtime dependency. Prepublication verification reported the expected three source mismatches against preview.28.

Publication operation:

```text
operationId        rm_8b9929d99b5d6cd1eb07702060ff217e
requestId          r116.semantic-git-tx.publish.20260909.01
status             succeeded
errorCode           null
recoveryAttempted   false
```

Activation operation:

```text
operationId        rm_179d009f840cc1ea7947ea95325cd3e0
requestId          r116.semantic-git-tx.restart.20260909.01
status             succeeded
errorCode           null
recoveryAttempted   false
```

A transient 502 occurred for an ordinary command call while the bounded restart was actively replacing the worker. Durable restart status subsequently returned `succeeded`; no retry of the restart operation was issued.

Fresh postactivation release verification returned:

```text
status                   verified
targetVersion            0.1.1-preview.29-semantic-git-transactional-commit
targetToolCount          68
fileCount                3
runtimeDependencyCount   1
mismatchCount            0
```

## 5. Live public-workspace reproduction

After preview.29 activation, a new untracked Validation 158 file was deliberately given one trailing-whitespace line and passed as the only declared path to the live `codex.git_commit_paths` tool at public HEAD `87f8763bac9b3db98ed15097df3daa542090ec35`.

The live tool returned the expected guarded failure:

```text
errorCode          GIT_COMMIT_PATHS_DIFF_CHECK_FAILED
indexRestored      true
rollbackAttempted  true
rollbackPhase      pre_commit
rollbackCommand    git restore --staged --source=HEAD -- <declared paths>
```

Immediate read-only reconciliation established all three required postconditions:

```text
Git index        empty
HEAD             87f8763bac9b3db98ed15097df3daa542090ec35
working-tree file still present with the intentionally invalid line
```

No owner-side Git command and no manual unstage occurred between that failed live semantic commit and the corrected preservation commit for this checkpoint. The later successful `codex.git_commit_paths` call therefore serves as the live retry proof that the failed transaction no longer leaves the semantic Git workflow blocked.

## 6. Operational disposition

Routine guarded semantic-commit validation failures must no longer ask the owner to run `git restore --staged -- .`. The semantic operation that introduced temporary staging owns cleanup of that staging when cleanup is provably safe.

This does not create a general public unstage/reset authority and does not claim that every possible uncertain Git/process failure can be auto-recovered. The safety boundary is explicit:

```text
definite failure + unchanged HEAD + declared staged scope only
    -> automatically restore and verify empty index

rollback cannot be verified
    -> GIT_COMMIT_PATHS_ROLLBACK_FAILED

commit result uncertain + HEAD changed
    -> no automatic rollback, no blind retry, fail visibly
```

```text
VALIDATION158=PASS
LIVE_RUNTIME_VERSION=0.1.1-preview.29-semantic-git-transactional-commit
SEMANTIC_GIT_TOOL_COUNT=68
COMMIT_PRECALL_INDEX_REQUIRED_EMPTY=true
FAILED_DIFF_CHECK_INDEX_RESTORED=true
WORKING_TREE_EDIT_PRESERVED=true
OWNER_MANUAL_UNSTAGE_REQUIRED_FOR_ROUTINE_GUARDED_FAILURES=false
GENERAL_PUBLIC_RESET_AUTHORITY_ADDED=false
UNCERTAIN_COMMIT_HEAD_CHANGED_AUTO_ROLLBACK=false
NEXT=RETURN_TO_RESEARCH123_FRESH_HOST_GITHUB_READONLY_FOUNDATION_QUALIFICATION
```
