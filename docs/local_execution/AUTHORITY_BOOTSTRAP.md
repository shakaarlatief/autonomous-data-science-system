# ADS Codexless Authority Bootstrap

**Status:** Current evergreen operational procedure  
**Last reviewed:** 2026-09-01  
**Scope:** Restore and verify the ADS-specific Codexless authority configuration before starting the local Codexless HTTP runtime.  
**Authority:** Operational procedure only. The active validation record owns the mutation contract. This document restores an already accepted local authority configuration and does not authorize widening it.

Starting `codexless-http.cmd` by itself is not sufficient for ADS. The Codexless process inherits its ADS authority bootstrap from the PowerShell process that launches it.

Required launcher-shell variables:

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

Verify the local file read-only:

```powershell
Get-Content $env:CODEXLESS_CONFIG_OVERRIDES_FILE -Raw |
    ConvertFrom-Json |
    ConvertTo-Json -Depth 10
```

Then start Codexless from that same configured PowerShell process:

```powershell
$CodexlessLauncher = Join-Path $env:LOCALAPPDATA "Codexless\bin\codexless-http.cmd"
Test-Path $CodexlessLauncher
& $CodexlessLauncher
```

From another PowerShell window, verify HTTP identity:

```powershell
Invoke-RestMethod "http://127.0.0.1:7690/healthz" |
    ConvertTo-Json -Depth 8
```

HTTP health does not prove effective authority. After the tunnel is healthy, perform a read-only authority verification. The required ADS result is:

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

Use `docs/local_execution/OPERATIONS.md` for the full Codexless/tunnel start-stop-restart topology. This file adds the required ADS-specific authority bootstrap before the Codexless HTTP launch step.

Correct restart sequence:

```text
1. stop tunnel-client but preserve its Git Bash shell when practical
2. stop Codexless HTTP
3. derive ADS root and private override path
4. set the three CODEXLESS_* variables
5. verify override semantics
6. launch Codexless from that same PowerShell process
7. verify Codexless health/tool count
8. restart and verify Secure MCP Tunnel
9. refresh ChatGPT app only if action schema changed
10. perform read-only authority verification
11. mutate only when the active validation contract and all preconditions pass
```

Public Git owns the required variable names, derivation procedure, expected semantics and stop conditions. Private/local state owns machine-specific values and secrets.
