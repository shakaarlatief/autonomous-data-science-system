# ADS Codexless Authority Bootstrap

**Status:** Current evergreen operational procedure  
**Last reviewed:** 2026-09-01  
**Scope:** Restore and verify the ADS-specific Codexless authority configuration before starting the local Codexless HTTP runtime, then apply the required Git metadata ACL integrity gate before direct-lane Git mutation after relevant lifecycle changes.  
**Authority:** Operational procedure only. The active validation/current-state boundary owns mutation authority. This document restores already accepted local authority and safety gates and does not authorize widening them.

Starting `codexless-http.cmd` by itself is not sufficient for ADS. The Codexless process inherits its ADS authority bootstrap from the PowerShell process that launches it.

## Required launcher-shell variables

```text
CODEXLESS_PROFILE
CODEXLESS_CONFIG_OVERRIDES_FILE
CODEXLESS_DEFAULT_CWD
```

Accepted profile:

```text
ads-direct-git
```

Derive the repository root and accepted private override path from the ADS checkout rather than chat memory:

```powershell
$AdsRoot = (git rev-parse --show-toplevel).Trim()
if (-not $AdsRoot) { throw "Could not resolve ADS Git root." }

$OverridePath = Join-Path $AdsRoot ".ads-private\codexless\ads-direct-git-overrides.json"
Test-Path $OverridePath
```

The override file must exist. Then, in the same PowerShell process that will launch Codexless:

```powershell
$env:CODEXLESS_PROFILE = "ads-direct-git"
$env:CODEXLESS_CONFIG_OVERRIDES_FILE = $OverridePath
$env:CODEXLESS_DEFAULT_CWD = $AdsRoot

Get-ChildItem Env:CODEXLESS* | Sort-Object Name
```

The accepted override semantics are equivalent to:

```text
default_permissions = ads-direct-git
ads-direct-git extends :workspace
.git writable
network.enabled = true
```

Verify the local override file read-only:

```powershell
Get-Content $env:CODEXLESS_CONFIG_OVERRIDES_FILE -Raw |
    ConvertFrom-Json |
    ConvertTo-Json -Depth 10
```

## Launch Codexless from the configured parent shell

```powershell
$CodexlessLauncher = Join-Path $env:LOCALAPPDATA "Codexless\bin\codexless-http.cmd"
Test-Path $CodexlessLauncher
& $CodexlessLauncher
```

Leave that PowerShell process open while Codexless runs.

From another PowerShell window, verify HTTP identity:

```powershell
Invoke-RestMethod "http://127.0.0.1:7690/healthz" |
    ConvertTo-Json -Depth 8
```

HTTP health does not prove effective authority.

## Required read-only authority verification

After the Secure MCP Tunnel is healthy, verify the effective authority through the bridge. The required ADS result is:

```text
permission ceiling        ads-direct-git
effective inherit profile ads-direct-git
authority source           host-profile-override
inherit networkAccess      true
readOnly effective profile :read-only
```

Observed stop-condition fallback:

```text
permission ceiling        :workspace
effective inherit profile :workspace
authority source           codex-quiet-profile-resolver
networkAccess              false
```

If that fallback or any authority mismatch appears, stop before mutation. Do not use the planned mutation as a probe and do not widen permissions merely to make it pass.

## Required Git metadata ACL integrity gate

ADS has observed that the Windows workspace-capability DENY on `.git` can reappear after later Codex/Codexless/sandbox lifecycle activity even though `ads-direct-git` still reports `.git` as writable.

The exact lifecycle trigger has not been isolated. Therefore, after relevant lifecycle changes and before direct-lane Git mutation, apply the read-only procedure in:

```text
docs/local_execution/ACL_INTEGRITY_GATE.md
```

The gate must establish both:

```text
no applicable DENY blocks .git or .git\FETCH_HEAD
current dedicated .git writable-root capability retains Modify access
```

If the ACL gate fails, stop. ACL repair is never automatic. A repair requires separate evidence, backup, explicit authorization, exact identity/rule-count guards, and post-repair read-only verification.

Do not hard-code historical capability SIDs into this evergreen bootstrap. Current capability identities are machine/runtime-specific evidence and remain private/local operational state.

## Relationship to the full operations runbook

Use:

```text
docs/local_execution/OPERATIONS.md
```

for the full Codexless/tunnel start-stop-restart topology.

Use:

```text
docs/local_execution/ACL_INTEGRITY_GATE.md
```

for the Windows Git metadata ACL safety gate.

The authority bootstrap and ACL gate are additional requirements around the generic HTTP/tunnel lifecycle. A healthy HTTP process and ready tunnel are necessary but not sufficient evidence for an ADS Git mutation.

## Correct restart and mutation-readiness sequence

```text
1. stop tunnel-client but preserve its Git Bash shell when practical
2. stop Codexless HTTP
3. derive ADS root and private override path
4. set the three CODEXLESS_* variables in the parent PowerShell
5. verify override semantics
6. launch Codexless from that same PowerShell process
7. verify Codexless health/tool count
8. restart and verify Secure MCP Tunnel
9. refresh ChatGPT app only if action schema changed
10. perform read-only authority verification
11. if a relevant sandbox/runtime lifecycle change occurred, perform ACL_INTEGRITY_GATE read-only
12. verify branch/upstream/working-tree preconditions defined by the active mutation contract
13. mutate only when the active validation/current-state boundary explicitly permits it
```

## Fail-closed rules

Do not proceed to mutation when any of these is true:

```text
CODEXLESS_* bootstrap missing
wrong effective profile
networkAccess false for required inherit mutation
readOnly does not downscope to :read-only
trusted ADS root mismatch
Git metadata ACL gate fails
repository precondition fails
planned operation requires permission widening
planned operation requires automatic ACL repair
```

Public Git owns the required variable names, derivation procedure, expected semantics, verification sequence, ACL gate, and stop conditions. Private/local state owns machine-specific values, current capability identities, temporary ACL backup paths, and secrets.
