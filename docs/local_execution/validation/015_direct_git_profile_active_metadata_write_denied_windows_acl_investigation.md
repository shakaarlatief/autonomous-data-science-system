# Direct Git profile active but Git metadata write denied: Windows ACL investigation

**Date:** 2026-09-01  
**Status:** `DIRECT_GIT_PROFILE_PARTIAL / PROFILE ACTIVE / FETCH_HEAD DENIED / STALE WORKSPACE-CAPABILITY DENY-ACE HYPOTHESIS IDENTIFIED / HOST ACL INSPECTION NEXT`  
**Scope:** Preserve the first runtime proof in which the custom `ads-direct-git` profile was genuinely active for model-free `command_exec`, together with the pinned Codex 0.151.0 source analysis of why `.git/FETCH_HEAD` can still be denied on Windows.  
**Authority:** Bounded local-execution evidence. This record does not yet classify the custom profile as operationally accepted or rejected and does not authorize Source Vault ingestion.  
**Declared references:** `research:105`, `checkpoint:270`, `path:docs/local_execution/validation/013_direct_lane_git_metadata_permission_profile_source_audit.md`, `path:docs/local_execution/validation/014_direct_git_profile_runtime_application_partial.md`, `path:docs/CURRENT_STATE.md`

## 1. Runtime profile application was proven

After the machine-local override was corrected to define both the custom profile and its Codex default selection, the real host-side Codexless HTTP runtime was restarted with:

```text
CODEXLESS_PROFILE=ads-direct-git
CODEXLESS_CONFIG_OVERRIDES_FILE=<private ignored override file>
CODEXLESS_DEFAULT_CWD=C:\Projects_Data\autonomous-data-science-system
```

The active host-side context then reported:

```text
activePermissionProfile:
  id      ads-direct-git
  extends :workspace

runtime workspace root:
  C:\Projects_Data\autonomous-data-science-system

sandbox projection:
  type          workspaceWrite
  writableRoots C:\Projects_Data\autonomous-data-science-system\.git
  networkAccess false

config override count:
  2
```

A direct `access=inherit` authority probe independently reported:

```text
permissionCeiling  ads-direct-git
permissionProfile  ads-direct-git
authoritySource    host-profile-override
trustedAncestor    c:\projects_data\autonomous-data-science-system
cwd                C:\Projects_Data\autonomous-data-science-system
```

A `readOnly` probe still downscoped correctly:

```text
permissionCeiling  ads-direct-git
permissionProfile  :read-only
authoritySource    host-profile-override
```

Therefore the earlier runtime-application ambiguity is closed: the custom profile was genuinely parsed, selected, bound to the trusted ADS root, and used as the model-free inherit ceiling.

## 2. Primary direct Git test still failed

The required primary test was then executed through the same model-free direct lane:

```text
git fetch origin
access=inherit
```

Observed result:

```text
command/exec failed:
sandbox denied exec error
exit code: 255

error: cannot open '.git/FETCH_HEAD': Permission denied
```

Therefore:

```text
.git/FETCH_HEAD writable through ads-direct-git   NO
```

No Codex model agent was launched and no formal Codex agent approval was requested or granted.

Because the primary fetch failed, no `git pull --ff-only` was attempted.

## 3. Final local Git state

```text
local HEAD
    063fdc99c76d7821efc58bb83823bcad33c068c5

origin/v1-source-vault-bootstrap-resume
    e14100a78d67fe7ed395d9768b115bbce7877c92

status
    ## v1-source-vault-bootstrap-resume...origin/v1-source-vault-bootstrap-resume [behind 7]
```

The tracked working tree remained clean. No commit, push, merge, rebase, reset, Source Universe mutation, tunnel restart, or authority broadening occurred.

## 4. Pinned Codex 0.151.0 source analysis

The follow-up source audit was pinned to the exact locally installed Codex release commit:

```text
Codex CLI             0.151.0
release commit        78c290807ce710180111df227df3b7a4fe845452
```

The source confirms that the profile is not merely cosmetic. App Server `command/exec` reloads the selected permission profile, obtains its effective permission profile and workspace roots, and passes that profile into `build_exec_request`. The core execution path then carries the permission profile into the Windows sandbox implementation.

The split filesystem policy also supports the intended semantic override. Its writable-root computation explicitly permits a more-specific write entry to remain writable while broader non-write entries become carveouts. The profile-level metadata guard similarly allows a sufficiently specific write entry beneath a normally protected metadata path.

Therefore the observed denial is not explained by Codexless failing to select the profile or App Server ignoring it.

## 5. Windows restricted-token enforcement introduces persistent ACL state

The exact Windows sandbox implementation uses capability SIDs and filesystem ACLs.

For each effective writable root it computes an allow path and for each read-only subpath it computes a deny path. The unelevated restricted-token runner then applies write-allow ACEs to allowed roots and write-deny ACEs to deny paths before spawning the sandboxed process.

Under the normal built-in workspace profile, the repository root is writable while existing `.git` is a read-only subpath. That causes the workspace capability SID to receive a deny-write ACE on the repository `.git` directory.

The capability SID used for the workspace root is persistent per canonical workspace path. The Codex source stores workspace capability SIDs keyed by canonicalized CWD and reuses the same SID on later runs.

Under `ads-direct-git`, the effective profile has both:

```text
repository root   writable with the persistent workspace-root capability SID
.git              additional writable root with its own root capability SID
```

The workspace-write token includes the capability SIDs for all currently allowed write roots.

This creates a strong state-transition hypothesis for the observed contradiction:

1. earlier normal `:workspace` execution placed a deny-write ACE for the persistent **workspace-root SID** on `.git`;
2. later `ads-direct-git` execution correctly adds/uses an additional `.git` write-root SID;
3. the same token still contains the persistent workspace-root SID because the repository root remains writable;
4. the runtime write-allow refresh path adds or refreshes allow ACEs for current roots, but the inspected source does not symmetrically remove an old deny-write ACE that is no longer part of the current policy;
5. Windows deny ACE semantics can therefore continue to deny `.git` when the token contains the workspace-root SID, even though `.git` also has a current allow root/SID.

This hypothesis fits all runtime observations: project context truthfully shows `.git` as a writable root, while the operating-system access check still returns `Permission denied` for `.git/FETCH_HEAD`.

## 6. Why this is not yet a final root-cause classification

The source evidence makes stale workspace-capability ACL state the strongest current explanation, but the actual `.git` DACL has not yet been inspected on the ADS machine after the profile transition.

The next diagnostic should therefore be read-only host ACL inspection, not another profile broadening experiment.

Required evidence:

```text
- current explicit/inherited ACL entries on the ADS .git directory
- the persistent workspace capability SID for the ADS repository
- the additional writable-root SID for the ADS .git directory, if already materialized
- whether .git contains a deny-write ACE for the workspace capability SID
- whether that deny ACE predates and survives the ads-direct-git profile transition
```

No ACL should be edited until this identity match is proven.

## 7. Current classification and next step

The bounded classification remains:

```text
DIRECT_GIT_PROFILE_PARTIAL
```

with a stronger sub-classification:

```text
PROFILE_SELECTION                  PASS
TRUSTED_ROOT_BINDING               PASS
READ_ONLY_DOWNSCOPE                PASS
DIRECT COMMAND PROFILE PROPAGATION PASS
GIT_METADATA_WRITE                 FAIL
WINDOWS_ACL_STATE HYPOTHESIS       STRONG / NOT YET HOST-CONFIRMED
```

The smallest next step is a read-only host ACL/capability-SID inspection. If the stale deny ACE is confirmed, the subsequent design decision is whether a narrowly governed ACL repair can make `ads-direct-git` operational without exposing generic unsandboxed process execution. If the ACL hypothesis is falsified, the audit should continue at the Windows sandbox enforcement seam before considering a dedicated bounded host-Git primitive.

Source Vault ingestion remains paused and unchanged during this investigation.
