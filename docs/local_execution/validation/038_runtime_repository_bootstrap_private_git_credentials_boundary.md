# Runtime repository bootstrap and private Git credential boundary

**Date:** 2026-09-03
**Status:** `AUTHENTICATED PRIVATE SEMANTIC GIT END-TO-END PASS`
**Scope:** Preserve the first reviewed private runtime-repository materialization, root commit, and the newly reproduced authenticated-private-Git boundary in generalized semantic Git.
**Authority:** Local execution evidence. This record does not make the private runtime repository a project-development authority. It records that the reviewed root commit is now present on the private GitHub `main` branch, while the public ADS repository remains the sole project-development authority.

## Workspace authority

The private sibling checkout is admitted under both required layers:

```text
Codex trust              PASS
Codexless registry       PASS
workspaceId              ads-local-runtime
registry revision        2
registry contentHash     588cd49a5f4cc57386781b2c5432996df9ba391d711e551df453570078f8e2d8
root                     C:\Projects_Data\autonomous-data-science-system-local-runtime
allowed remote           origin
integrity policy         runtime-private-bootstrap
browser capability       not granted
```

Ordinary `codex.project_context`, `codex.command_exec`, and Git reads succeeded on that root with `ads-direct-git` and both trusted ancestors equal to the runtime repository.

## First `.ads-private` inventory and classification

The public ADS ignored runtime tree initially contained:

```text
176 files total
175 under .ads-private/codexless
1 .ads-private/source_vault_bootstrap.json
```

Two exact hotfix/publication backup files were classified as transient and excluded:

```text
.ads-private/codexless/activate-flexible-authority-publication.ps1.pre-workspace-registry-wiring-hotfix-20260903-131128.bak
.ads-private/codexless/flexible-authority-candidate/src/codexless-runtime.mjs.pre-workspace-registry-wiring-hotfix-20260903-131128.bak
```

`.ads-private/source_vault_bootstrap.json` was deliberately excluded from the first runtime-repository import because its semantic owner remains the separate private Source Vault continuity boundary. Its values were not printed during classification.

The resulting selected Codexless set was:

```text
selected files           173
selected bytes           2,489,405
obvious secret flags     0 after fixture normalization
```

One regression test had originally triggered the generic secret-assignment pattern because it intentionally wrote a fake API-key-looking value into a temporary `.env`. The test was changed to use a harmless value while preserving the actual policy assertion: the `.env` path itself remains sufficient to prove deterministic rejection. The focused regression remained:

```text
FLEXIBLE_AUTHORITY_REGRESSION=PASS tests=7
```

## Runtime repository materialization

The private runtime checkout was populated with exactly:

```text
.ads-private/codexless/    173 reviewed files
README.md                  repository-role summary
RUNTIME_STATE.json         provenance back to public ADS commit/checkpoint
.gitignore                 transient backup exclusions
```

`RUNTIME_STATE.json` points to public ADS authority:

```text
publicAdsCommit       94e7bf7a011c202d2c9def718e3f2eefd066f1b8
publicAdsCheckpoint   277
selectedFileCount     173
materializationClass  reviewed-non-secret-local-runtime-snapshot
```

A second scan over the completed 176-file runtime worktree returned:

```text
WORKTREE_FILES=176
WORKTREE_BYTES=2492135
FLAGGED_FILES=0
```

## Controlled commit-zero bootstrap

The generalized semantic commit contract intentionally requires an existing `expectedHead`, so commit zero used one narrow temporary bootstrap helper instead of weakening `codex.git_commit_paths`.

The helper verified before committing:

```text
exact runtime repository root
attached main branch
HEAD absent
exact expected private origin
RUNTIME_STATE public ADS pointer
176 selected worktree files
secret-like path/content checks
per-file <= 2 MiB
total <= 50 MiB
no NUL/binary content
exact staged-file count
only two known Markdown hard-break whitespace findings from preserved evidence
```

The root commit succeeded:

```text
HEAD
0ce61ba794929ee71c555d480a936fdced28ef2e

commit
Bootstrap reviewed local runtime evidence

tracked files
176

root parent verification
PASS: `git rev-list --parents -n 1 HEAD` returned only the new HEAD
```

The helper itself was not committed and was removed afterward. Final local status is clean:

```text
## main...origin/main [gone]
```

The `[gone]` state is expected because the private GitHub repository is still empty and no initial remote branch has been created.

## Newly reproduced private Git credential boundary

The first generalized semantic push attempt used:

```text
workspaceId   ads-local-runtime
expectedHead  0ce61ba794929ee71c555d480a936fdced28ef2e
```

It failed before any push occurred. The failure was the semantic push's pre-push `git fetch origin` running through Codex App Server `command/exec`, where the sandbox cannot access the user's Windows Git credential-manager / VS Code askpass state:

```text
git: 'credential-manager' is not a git command
askpass.sh: Permission denied
fatal: could not read Username for 'https://github.com'
```

This proves a new architecture fact:

```text
public repository anonymous fetch
    may work in command/exec

private authenticated fetch/pull/pre-push refresh
    cannot rely on command/exec credential access on this host
```

No remote push was attempted by this failed semantic action.

## Candidate correction

The flexible-authority candidate was corrected without changing any public MCP input schema. Network Git operations are now routed through the already-internal bounded host-process substrate while local authority checks, branch/upstream derivation, ancestry checks, staging/commit logic, and integrity reads remain authority-bounded.

Changed semantic behavior:

```text
git_fetch_origin
    exact registered remote fetch -> bounded host process

git_pull_ff_only
    exact FF-only pull -> bounded host process

git_push_ff_only
    pre-push fetch -> bounded host process
    exactly one non-force push -> bounded host process
    post-push fetch -> bounded host process
```

The caller still cannot provide cwd, URL, remote, branch, refspec, credentials, Git configuration, permission profile, sandbox, force, or host command.

Candidate hashes after correction:

```text
semantic-git.mjs
F9B65E6245BEB903AFE9805EB9091DCED907CAC5BC49FCB9E41EC299CAFEC96F

flexible-authority-regression.mjs
976935BF3F24E41776F76495A9718682D83DB12BEBDE94A3A14911C07B17174E
```

Verification:

```text
node --check semantic-git.mjs        PASS
FLEXIBLE_AUTHORITY_REGRESSION        PASS tests=7
```

A guarded host-terminal activation helper was prepared:

```text
.ads-private/codexless/activate-private-git-network-hotfix.ps1
```

It verifies the exact current live semantic-Git hash, exact corrected candidate hash, reruns the focused regression, creates a verified backup, atomically replaces only live `semantic-git.mjs`, checks the resulting live file, and restores the old file on failure.

The first activation attempt failed safely because this Windows PowerShell/.NET host rejects `File.Replace(..., $null, ...)` as an invalid empty backup path. The helper was corrected to supply an explicit same-directory backup path to `File.Replace`; its rollback path was strengthened to prove the exact baseline is preserved or restored. A subsequent `-WhatIf` preflight passed.

The actual host publication then passed:

```text
FLEXIBLE_AUTHORITY_REGRESSION=PASS tests=7
PRIVATE_GIT_NETWORK_HOTFIX_PREFLIGHT=PASS
PRIVATE_GIT_NETWORK_HOTFIX_RESULT=PASS
LIVE_SHA256_AFTER=F9B65E6245BEB903AFE9805EB9091DCED907CAC5BC49FCB9E41EC299CAFEC96F
```

The verified backup is:

```text
%LOCALAPPDATA%\Codexless\src\semantic-git.mjs.pre-private-git-network-20260903-140249.bak
```

ChatGPT independently re-read the installed live source after publication and verified exact candidate/live equality at:

```text
F9B65E6245BEB903AFE9805EB9091DCED907CAC5BC49FCB9E41EC299CAFEC96F
```

The currently running Node process has not yet been restarted, so these bytes are published on disk but the process still holds its previous in-memory implementation until the controlled restart.

## Initial private remote branch bootstrap

The one-time host push from the private runtime checkout succeeded:

```text
git push -u origin main
[new branch] main -> main
branch 'main' set up to track 'origin/main'
```

ChatGPT independently verified immediately afterward:

```text
HEAD        0ce61ba794929ee71c555d480a936fdced28ef2e
origin/main 0ce61ba794929ee71c555d480a936fdced28ef2e
status      ## main...origin/main
upstream    origin/main
```

This closes the commit-zero / absent-remote-branch bootstrap exception. The private runtime repository now has an ordinary attached local `main` with a same-name `origin/main` upstream, so subsequent Git operations can be tested through the stable semantic contracts without special branch creation.

## Restart and authenticated-private semantic Git qualification

After the controlled Codexless restart and tunnel reconnect, the tunnel returned:

```text
/healthz  HTTP 200 / live
/readyz   HTTP 200 / ready
```

The refreshed running implementation then passed the exact authenticated-private semantic Git qualification.

First, generalized fetch:

```text
codex.git_fetch_origin(workspaceId="ads-local-runtime")

operation      fetch
workspaceId    ads-local-runtime
branch         main
upstream       origin/main
remote         origin
hostProcess    true
exitCode       0
```

Second, generalized push against the already-equal private branch:

```text
codex.git_push_ff_only(
    workspaceId="ads-local-runtime",
    expectedHead="0ce61ba794929ee71c555d480a936fdced28ef2e"
)
```

returned:

```text
exitCode                     0
push result                  up to date
headBefore                   0ce61ba794929ee71c555d480a936fdced28ef2e
remoteTrackingHeadBefore     0ce61ba794929ee71c555d480a936fdced28ef2e
integrityPolicyId            runtime-private-bootstrap
integrity                    RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
hostProcess                  true
retried                      false
headAfter                    0ce61ba794929ee71c555d480a936fdced28ef2e
remoteTrackingHeadAfter      0ce61ba794929ee71c555d480a936fdced28ef2e
trackedWorkingTreeCleanAfter true
remoteRefreshAfterExitCode   0
postflightOk                 true
```

This is the decisive end-to-end proof that the stable generalized multi-repository surface works for an authenticated private Git repository while retaining server-owned workspace selection, remote selection, integrity policy, ordinary non-force semantics, no retry on uncertain push, and exact postflight equality verification.

The earlier private credential failure is therefore resolved by the bounded host-network transport correction, not by widening caller authority or exposing credentials.

No Source Vault payload, private Source Vault values, credentials, protected `.tmp`, or unrelated public ADS Git history was changed during this qualification.
