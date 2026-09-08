# Validation 129: Private Companion Runtime Bridge Authority and Semantic Git Qualified

**Date:** 2026-09-08
**Status:** PASS / DEDICATED PRIVATE-COMPANION GIT POLICY LIVE / FULL REGISTERED WORKSPACE AUTHORITY QUALIFIED
**Research:** Research 123 supporting continuity infrastructure
**Scope:** Qualify the private companion repository as a first-class Codexless Runtime Bridge workspace with dedicated repository-specific integrity, full supported workspace/Git capabilities, semantic release publication, and authenticated private Git operation.

## 1. Starting boundary

The project owner cloned the existing private knowledge companion as a sibling repository at its intended local project location and added it to the current multi-root VS Code workspace.

The repository is:

```text
GitHub     shakaarlatief/autonomous-data-science-system-private
branch     main
remote     origin
role       private knowledge-preservation complement only
```

The public ADS repository remains the sole project-development authority. Granting operational write/Git capability to the private companion does not change that authority hierarchy.

The repository was first admitted as `ads-private` with read access so its `CURRENT_PRIVATE_STATE.md` could be reconstructed directly. The owner then explicitly requested that the private companion not be artificially downscoped relative to the other managed repositories.

## 2. Why a dedicated integrity policy was required

The existing `workspace-standard` policy intentionally rejects semantic Git capability. An attempted upgrade of `ads-private` to Git capability therefore failed closed with:

```text
WORKSPACE_POLICY_INCOMPATIBLE
workspace-standard is for ordinary non-Git filesystem/project authority;
semantic Git requires an explicit Git integrity policy
```

The runtime repository's `runtime-private-bootstrap` policy was not reused because it belongs to a different repository role. A new server-owned policy was implemented instead:

```text
integrityPolicyId       private-companion
protected policy        private-companion-v1
protected paths         [.git]
```

The private-companion integrity scanner preserves the companion's actual role. It requires the tracked routing/role files, validates the public-development-authority and continuity-anchor structure, rejects obvious secret-bearing paths/content, rejects bulk/source payload extensions, rejects ordinary ADS development-tree roots, rejects symlinks/non-regular/binary tracked content, and preserves bounded per-file/aggregate inspection limits.

The scanner deliberately treats continuity-anchor freshness as a separate claim. Its repository-safety PASS proves role/content safety for semantic push, not that the private anchor equals the latest public ADS checkpoint.

## 3. Candidate and regression qualification

A complete candidate overlay was exercised with workspace-local temporary state because the current Windows Codex sandbox correctly does not grant test writes to the user-profile temporary directory.

The final focused result was:

```text
FLEXIBLE_AUTHORITY_REGRESSION=PASS tests=11
```

The added cases prove:

```text
private-companion is a first-class semantic-Git integrity policy
.git remains protected
full supported workspace capability can be registered with origin
valid private knowledge role/content passes
public continuity checkpoint/commit fields remain typed
prohibited source payloads fail
missing role/anchor invariants fail
```

No public MCP action schema changed.

## 4. Durable runtime release

The implementation was preserved in the private local-runtime repository as:

```text
releaseId      private-companion-git-policy-v1
private HEAD   7297e7740f5973ed11d434c24b3e0c43b7a05205
manifest SHA   97fec40d085722260e6bf285774af39d9e55b296cf55138bfb0cb48e15a33044
file count     3
```

The exact target files are:

```text
src/workspace-registry.mjs
src/semantic-git.mjs
test/flexible-authority-regression.mjs
```

The semantic release lifecycle then returned:

```text
prepare                    prepared
pre-publication verify     verification_failed / mismatchCount=3
publish                    succeeded
restart activation         succeeded
post-activation verify     verified / mismatchCount=0
```

The pre-publication mismatch count is expected evidence that the three target bytes were not installed yet. Publication and activation retained the existing public runtime contract:

```text
version       0.1.1-preview.20-runtime-release
surface       codexless-public-preview-v2
tool count    63
```

This was an internal policy/authority extension, not a new public tool.

## 5. Final workspace admission

After activation, a fresh optimistic registry update succeeded.

The resulting durable entry is:

```text
workspaceId          ads-private
root                 RESOLVED_PRIVATE local sibling clone
capabilities         agent
                     browser
                     git_commit_paths
                     git_fetch
                     git_pull_ff_only
                     git_push_ff_only
                     read
                     write
semantic Git         enabled
allowed remote       origin
integrity policy     private-companion
protected policy     private-companion-v1
protected paths      [.git]
```

The registry advanced to:

```text
revision      17
contentHash   49f4c56a32b75f5d40ec07333394650bb2e71a69214c6ce3ca88241e70163557
```

## 6. Live authenticated private Git qualification

All four generalized semantic Git capability families are now live-reachable for the private companion.

Read/synchronization qualification:

```text
git_fetch_origin      PASS
git_pull_ff_only      PASS / Already up to date
```

A no-change semantic push executed the new policy and returned:

```text
PRIVATE_COMPANION_REPOSITORY_SAFETY=PASS
retried=false
headAfter == remoteTrackingHeadAfter
trackedWorkingTreeCleanAfter=true
postflightOk=true
```

A real private continuity-support mutation then qualified the commit path. Two exact declared files recorded the current Runtime Bridge workspace binding:

```text
machines/README.md
machines/runtime_bridge_workspace_2026-09-08.json
```

`codex.git_commit_paths` created:

```text
f3af071667b46fccb4ea852a429d696e376299c2
Record Runtime Bridge private companion authority
```

with exact parent `c470b64ea1fb8c10811c23d0a0ffe89e7b23d0d0`, clean index postflight and `postflightOk=true`.

`codex.git_push_ff_only` then published the same exact commit with:

```text
PRIVATE_COMPANION_REPOSITORY_SAFETY=PASS
retried=false
headAfter=f3af071667b46fccb4ea852a429d696e376299c2
remoteTrackingHeadAfter=f3af071667b46fccb4ea852a429d696e376299c2
trackedWorkingTreeCleanAfter=true
postflightOk=true
```

This is the first end-to-end proof that the private knowledge companion can be maintained through the same stable generalized semantic Git surface while retaining its distinct authority role.

## 7. Continuity disposition

The private companion's earlier public continuity anchor still points to an older public checkpoint at this exact validation moment. That does not invalidate its resolved private facts, but it must not be called fresh against the new public checkpoint until deliberately reconciled.

The correct completion sequence is:

```text
freeze the new public checkpoint
-> update private CURRENT_PRIVATE_STATE.md to that exact public checkpoint/commit
-> commit/push through the newly qualified ads-private semantic Git path
-> run scripts/check_private_continuity.py against the exact public target
```

This avoids recursive public/private anchoring while leaving the public repository as the sole development authority.

```text
PRIVATE_COMPANION_POLICY=LIVE_QUALIFIED
ADS_PRIVATE_FULL_WORKSPACE_CAPABILITY=PASS
ADS_PRIVATE_FETCH=PASS
ADS_PRIVATE_PULL=PASS
ADS_PRIVATE_COMMIT=PASS
ADS_PRIVATE_PUSH=PASS
PRIVATE_COMPANION_REPOSITORY_SAFETY=PASS
VALIDATION129=PASS
```
