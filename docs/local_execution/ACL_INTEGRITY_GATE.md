# ADS Git Metadata ACL Integrity Gate

**Status:** Current evergreen operational procedure  
**Last reviewed:** 2026-09-01  
**Scope:** Read-only verification of Windows ACL state for ADS Git metadata before direct-lane Git mutation after relevant Codex/Codexless/sandbox lifecycle changes.  
**Authority:** Operational safety gate only. This document does not authorize ACL mutation or Git mutation. The active validation/current-state boundary remains authoritative for any write.

## Why this gate exists

ADS has now observed the same `.git/FETCH_HEAD` failure pattern twice. In both cases the `ads-direct-git` profile projected `.git` as writable while Windows still contained an applicable workspace-capability DENY ACE on `.git`, inherited by `FETCH_HEAD`.

The first occurrence was diagnosed and repaired in Validation 016. A later occurrence was confirmed during Validation 020 and the subsequent read-only ACL diagnosis. After a separately authorized guarded repair, Validation 021 proved the strict semantic fast-forward pull end to end.

The exact lifecycle event that recreated the DENY has not been isolated. Therefore a healthy Codexless process and a correct `ads-direct-git` authority report are not, by themselves, sufficient evidence that Windows still permits Git metadata writes.

## When to run

Run this gate before a direct-lane Git mutation when any relevant lifecycle event has occurred since the last verified mutation, including:

```text
Codexless restart
Codex App Server / Codex sandbox restart
permission-profile/bootstrap reload
host reboot or login-session change
sandbox/capability regeneration
any prior .git/FETCH_HEAD permission-denied result
```

If no relevant lifecycle change occurred and the active validation explicitly defines a narrower check, follow the active validation. When uncertain, prefer the read-only gate.

## Read-only inspection

From a normal host PowerShell opened in the ADS checkout:

```powershell
$AdsRoot = (git rev-parse --show-toplevel).Trim()
if (-not $AdsRoot) { throw "Could not resolve ADS Git root." }

$GitDir = Join-Path $AdsRoot ".git"
$FetchHead = Join-Path $GitDir "FETCH_HEAD"

Write-Host "`n=== .git ACL ==="
(Get-Acl $GitDir).Access |
    Select-Object `
        IdentityReference,
        AccessControlType,
        FileSystemRights,
        IsInherited,
        InheritanceFlags,
        PropagationFlags |
    Format-Table -AutoSize

Write-Host "`n=== FETCH_HEAD ACL ==="
(Get-Acl $FetchHead).Access |
    Select-Object `
        IdentityReference,
        AccessControlType,
        FileSystemRights,
        IsInherited,
        InheritanceFlags,
        PropagationFlags |
    Format-Table -AutoSize

Write-Host "`n=== .git SDDL ==="
(Get-Acl $GitDir).Sddl

Write-Host "`n=== FETCH_HEAD SDDL ==="
(Get-Acl $FetchHead).Sddl
```

This is inspection only. It must not be combined with `Set-Acl`, `icacls /grant`, `icacls /remove`, or any other ACL write unless a separate repair decision has already been authorized.

## Required interpretation

The accepted direct-lane state requires both of these properties:

```text
1. no applicable DENY ACE blocks the current sandbox/workspace capability
   from writing .git or .git\FETCH_HEAD;

2. the dedicated .git writable-root capability retains Modify access
   to the Git metadata path.
```

Machine-specific capability SIDs are not frozen in this public document. Resolve/compare them from the current host/runtime evidence and accepted private/local continuity rather than copying a historical SID from chat or an old validation into a repair script.

An ordinary user/account ALLOW does not neutralize a matching sandbox-capability DENY. If an applicable DENY is present, treat it as a stop condition even if another principal also has `Modify`.

## Stop condition

If the inspection shows any of the following, do not run the planned Git mutation:

```text
applicable DENY on .git
applicable inherited DENY on .git\FETCH_HEAD
missing Modify for the current .git writable-root capability
capability identity mismatch
ambiguous ACL/capability ownership
```

Do not use the Git mutation itself as a probe.

## Repair boundary

ACL repair is never automatic merely because a Git mutation is desired. A repair requires either a separately authorized evidence-driven step or an already-recorded standing authorization whose exact guard contract matches the fresh diagnosis. In either case the repair must at minimum:

```text
backs up the current .git SDDL to private/local temporary storage;
selects the exact ADS .git path only;
selects the exact currently diagnosed capability identity only;
selects explicit DENY rules only;
requires the exact expected rule count before removal;
verifies the expected count after in-memory removal;
writes only after all guards pass;
re-reads .git and FETCH_HEAD ACLs afterward;
confirms the intended DENY is absent;
confirms the dedicated .git writable capability still has Modify.
```

Do not hard-code a historical capability SID into the evergreen public procedure. The repair identity must come from current evidence.

Do not broaden filesystem roots, grant generic FullControl, modify unrelated repositories, alter `.agents` or `.codex`, or change tunnel/network authority as part of an ACL repair.

## Standing authorization for the exact recurring ADS Git-metadata defect

On 2026-09-05 the project owner explicitly granted standing authorization for future repair of the already-reproduced lifecycle-sensitive Codex workspace-capability DENY condition so repeated approval is not required when the exact same guarded defect recurs.

This standing authorization is deliberately narrow. It is valid only after fresh read-only diagnosis proves all of the following:

```text
target is the registered ADS repository's own .git metadata path
current sandbox token / authority evidence resolves the exact active workspace-capability SID
exactly two explicit DENY ACEs for that SID are present on .git
the dedicated .git writable capability is current and retains Modify on .git and FETCH_HEAD
no broader path, unrelated repository, credential, registry, service or host authority is involved
the guarded helper creates a pre-repair SDDL backup outside ordinary Git content
in-memory removal reaches exactly two removed / zero remaining before Set-Acl
post-repair .git and FETCH_HEAD contain no matching DENY
dedicated .git writable Modify remains present after repair
```

If any identity, rule count, path, capability, ACL shape, backup condition or postcondition differs, the standing authorization does not apply. Stop and obtain a new evidence-driven decision rather than broadening the repair.

The standing authorization does not grant arbitrary ACL mutation, generic permission widening, FullControl, historical-SID reuse, or automatic repair of unknown Git failures. The helper must resolve/use current evidence and fail closed on drift.

Primary evidence: Validation 064 and the guarded local-runtime helper preserved in the private local-runtime repository.
## Post-repair rule

A successful ACL repair does not itself authorize Git synchronization. After repair:

```text
1. verify ACL postconditions read-only;
2. re-verify the active ADS authority profile and readOnly downscope;
3. re-verify repository branch/upstream/cleanliness preconditions;
4. invoke only the mutation explicitly authorized by the active validation;
5. never auto-retry a failed or uncertain Git mutation.
```

## Evidence references

```text
docs/local_execution/validation/016_direct_git_acl_repair_network_profile_and_outer_tool_safety_boundary.md
docs/local_execution/validation/020_semantic_git_pull_ff_only_dispatched_local_fetch_head_denied.md
docs/local_execution/validation/021_semantic_git_pull_ff_only_verified_after_acl_repair.md
docs/local_execution/AUTHORITY_BOOTSTRAP.md
```

The public repository owns this stable procedure. Exact current capability identities, temporary backup locations, and other machine-specific values remain private/local operational state.
