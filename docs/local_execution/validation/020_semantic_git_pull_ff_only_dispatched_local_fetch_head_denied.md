# Semantic strict-fast-forward Git pull dispatched, local FETCH_HEAD write denied

**Date:** 2026-09-01  
**Status:** `SEMANTIC_GIT_PULL_FF_ONLY_DISPATCHED / LOCAL FILESYSTEM DENIED / REPOSITORY UNCHANGED`  
**Scope:** Preserve the first controlled ChatGPT dispatch of `codex.git_pull_ff_only` under the frozen Validation 019 contract.  
**Authority:** Bounded local-execution evidence only. This record does not authorize retry, ACL mutation, permission widening, alternate Git mutation, Codex agent fallback, or Source Vault ingestion.

## Result

The Validation 019 preflight passed and ChatGPT dispatched `codex.git_pull_ff_only` exactly once. The call reached local Codex App Server `command/exec`; it was not blocked by the outer ChatGPT/OpenAI tool-safety layer.

The fixed pull then failed locally when Git attempted to open `.git/FETCH_HEAD`:

```text
exit status  1
stdout       empty
stderr       error: cannot open '.git/FETCH_HEAD': Permission denied

command/exec failed: exec failed: sandbox error: sandbox denied exec error,
exit code: 1, stdout: , stderr: error: cannot open '.git/FETCH_HEAD': Permission denied
```

No retry or fallback was attempted.

## Preflight

```text
branch
    v1-source-vault-bootstrap-resume

upstream
    origin/v1-source-vault-bootstrap-resume

local HEAD
    063fdc99c76d7821efc58bb83823bcad33c068c5

origin/v1-source-vault-bootstrap-resume
    9882bdc8aa550e23da6f592fbc7cfcf8e959c48c

status
    ## v1-source-vault-bootstrap-resume...origin/v1-source-vault-bootstrap-resume [behind 16]

working tree/index
    clean
    no staged changes
    no unstaged tracked changes
    no untracked files

operation state
    no merge/rebase/cherry-pick/revert state detected
```

The branch was 0 ahead / 16 behind and fast-forwardable according to the current remote-tracking state.

## Authority evidence at dispatch

All Validation 019 authority invariants matched before the mutation:

```text
permission ceiling        ads-direct-git
effective inherit profile ads-direct-git
authority source           host-profile-override
inherit networkAccess      true
trusted ADS root           C:\Projects_Data\autonomous-data-science-system
readOnly effective profile :read-only
```

Therefore this result is not explained by the earlier accidental restart fallback to `:workspace` / `networkAccess=false`.

## Postflight

```text
branch after
    v1-source-vault-bootstrap-resume

local HEAD after
    063fdc99c76d7821efc58bb83823bcad33c068c5

origin/v1-source-vault-bootstrap-resume after
    9882bdc8aa550e23da6f592fbc7cfcf8e959c48c

status after
    ## v1-source-vault-bootstrap-resume...origin/v1-source-vault-bootstrap-resume [behind 16]

working tree/index after
    clean
    no staged changes
    no unstaged tracked changes
    no untracked files

local HEAD == origin-tracking HEAD
    false
```

`HEAD` did not change, so the ancestor postcondition was not applicable.

No reset, checkout, fetch fallback, rebase, merge, rollback, retry, commit, push, alternate Git mutation, `codex.process`, or Codex agent was used.

## Interpretation

This experiment separates the stack more precisely:

```text
ChatGPT semantic pull discovery                 PASS
outer ChatGPT/OpenAI dispatch                   PASS
Validation 019 preconditions                    PASS
ads-direct-git profile selection                PASS
inherit networkAccess=true                      PASS
readOnly -> :read-only                          PASS
local Git pull process reached                  PASS
.git/FETCH_HEAD write                           DENIED BY LOCAL SANDBOX/FILESYSTEM
strict fast-forward checkout synchronization    NOT PROVEN
repository mutation                             NONE OBSERVED
```

The same `.git/FETCH_HEAD` symptom had previously been resolved during Validation 016 by a narrow host ACL repair, after which `git fetch origin` crossed the filesystem boundary and later the semantic fetch in Validation 018 completed successfully. The recurrence after later Codexless/runtime restarts is therefore a regression or runtime-state discrepancy that requires fresh read-only diagnosis.

Do not infer the cause yet. Plausible classes that must be distinguished by evidence include:

```text
host ACL state changed or was regenerated
sandbox capability identity changed across restart
current .git writable capability no longer matches host ACL state
pull execution projects filesystem authority differently from the verified fetch path
another local sandbox/Windows permission boundary is active
```

## Next diagnostic boundary

Before any retry or repair, inspect read-only host state and compare it with the current runtime authority projection. At minimum determine:

```text
current ACL on .git
current ACL on .git\FETCH_HEAD
whether an explicit/inherited DENY ACE is present
which capability SID currently has Modify on .git/FETCH_HEAD
which capability identity the current ads-direct-git sandbox is using for workspace and .git writable-root projection
whether those identities match the accepted post-Validation-016 state
```

If a stale or regenerated deny is confirmed, a separate narrowly guarded repair decision is required before any second pull dispatch. If ACL state is already correct, investigate the sandbox projection/execution path instead.

Validation 019 explicitly forbids automatic retry and permission/ACL widening merely to make the experiment pass. That stop condition remains in force.

## Classification

```text
SEMANTIC_GIT_FETCH_ORIGIN                  VERIFIED
SEMANTIC_GIT_PULL_FF_ONLY_CONTRACT         FROZEN
LOCAL PULL TOOL IMPLEMENTATION             COMPLETE / TESTED
CHATGPT PULL DISPATCH                      VERIFIED
LOCAL PULL EXECUTION                       REACHED
LOCAL FETCH_HEAD WRITE                     DENIED
DIRECT MODEL-FREE CHECKOUT SYNCHRONIZATION NOT PROVEN
REPOSITORY                                 CLEAN / UNCHANGED
SOURCE VAULT                               PAUSED / UNCHANGED
```
