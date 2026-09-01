# ADS Semantic Strict-Fast-Forward Pull Acceptance

**Status:** `VERIFIED_FOR_EXACT_CONTRACT`  
**Date:** 2026-09-01  
**Scope:** Stable acceptance boundary for the experimentally verified `codex.git_pull_ff_only` action.  
**Authority:** This acceptance is deliberately narrow. It does not extend to arbitrary Git commands or stronger repository mutations.

## Accepted capability

The direct model-free path is empirically verified for exactly:

```text
ChatGPT
    -> codex.git_pull_ff_only
    -> Codexless bounded public semantic action
    -> Codex App Server command/exec
    -> trusted ADS checkout
    -> strict fast-forward synchronization
```

The fixed backend remains:

```text
git pull --ff-only --no-rebase --no-tags --no-recurse-submodules origin v1-source-vault-bootstrap-resume
```

with no caller-controlled command, cwd, remote, URL, refspec, branch, credentials, permission profile, merge strategy, or rebase behavior.

## Required preconditions

The action remains acceptable only while the frozen fail-closed preconditions continue to hold:

```text
trusted ADS root
exact branch v1-source-vault-bootstrap-resume
exact upstream origin/v1-source-vault-bootstrap-resume
clean index
clean tracked working tree
no untracked files
no merge/rebase/cherry-pick/revert state
inherit profile ads-direct-git
inherit networkAccess true
readOnly downscope :read-only
Git metadata ACL integrity gate passes
```

## Verified evidence

Validation 021 proved a successful strict fast-forward from:

```text
063fdc99c76d7821efc58bb83823bcad33c068c5
```

to:

```text
93948ae2fbacb0b725aa7442283697e134dd1dbc
```

with:

```text
exit status 0
local HEAD == origin tracking HEAD
pre-operation HEAD ancestor of post-operation HEAD
branch unchanged
working tree clean
index clean
no untracked files
```

The first pull dispatch had previously exposed a recurring Windows ACL deny on `.git/FETCH_HEAD`; that blocker was diagnosed read-only, backed up, repaired through a separately authorized exact guarded change, and re-verified before the successful second dispatch.

## Operational gates

Before future direct-lane Git mutation after relevant runtime/sandbox lifecycle changes, use:

```text
docs/local_execution/AUTHORITY_BOOTSTRAP.md
docs/local_execution/ACL_INTEGRITY_GATE.md
```

A healthy HTTP/tunnel path is not enough. The correct ADS authority and the Windows Git metadata ACL state must both pass.

## Explicitly not accepted

This acceptance does not authorize or imply verification of:

```text
commit
push
force push
reset
checkout
rebase
merge commits
arbitrary fetch/refspec selection
arbitrary branch selection
arbitrary shell or Git command execution
public codex.process
permission widening
automatic ACL repair
```

Any such capability requires a separately frozen design and validation boundary.

## Source Vault relationship

The direct synchronization feasibility question that paused Source Vault work is now resolved for the required strict fast-forward synchronization contract. Project routing may therefore return to the Source Vault continuation sequence without treating Codexless as project authority or as a mandatory core dependency.
