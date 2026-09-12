# Local Execution Operations Runbook

**Status:** Current evergreen operational procedure  
**Last reviewed:** 2026-09-12
**Scope:** Start, stop, restart, verify and reconnect the ADS Codexless loopback HTTP service and OpenAI Secure MCP Tunnel without relying on chat memory.  
**Authority:** Operational procedure only. `docs/CURRENT_STATE.md` and the active validation record own the current experiment, expected tool surface and next mutation. This runbook does not widen local authority or replace the security contracts in the validation records.

## Purpose

The ADS local-execution path must be recoverable from repository evidence even after a chat, terminal window, laptop restart or model context is lost.

The normal path is:

```text
ChatGPT developer MCP app
    -> OpenAI Secure MCP Tunnel
    -> local tunnel-client
    -> Codexless Streamable HTTP MCP
    -> Codex App Server
    -> host-configured trusted ADS repository
```

Do not reconstruct the startup procedure from conversation memory when this file is available.

## Public/private boundary

This public runbook records commands, public-safe derived locations, ports, profile names and verification procedure.

It deliberately does **not** record:

```text
CONTROL_PLANE_API_KEY value
CONTROL_PLANE_TUNNEL_ID value
private workspace/tunnel identifiers
other credentials or secrets
```

Those values are `RESOLVED_PRIVATE` operational state. Retrieve them from the accepted private/local continuity layer when needed. Never commit them to the public repository and never print them merely for diagnostics. The persistent profile may reference a local secret file, but neither the credential value nor its user-specific path belongs in public project history.

Do not substitute a general `OPENAI_API_KEY` for the dedicated tunnel runtime credential.

## Stable local endpoints

```text
Codexless HTTP host       127.0.0.1
Codexless HTTP port       7690
Codexless health          http://127.0.0.1:7690/healthz
Codexless MCP target      http://127.0.0.1:7690/mcp

Tunnel admin host         127.0.0.1
Tunnel admin port         8080
Tunnel liveness           http://127.0.0.1:8080/healthz
Tunnel readiness          http://127.0.0.1:8080/readyz
```

`/healthz` and `/readyz` have different meanings for the tunnel. Liveness alone does not prove the MCP backend is ready.

## Codexless installation and launcher

Use `%LOCALAPPDATA%` rather than embedding the Windows account name in public documentation.

In PowerShell:

```powershell
$CodexlessHome = Join-Path $env:LOCALAPPDATA "Codexless"
$CodexlessLauncher = Join-Path $CodexlessHome "bin\codexless-http.cmd"

$CodexlessHome
$CodexlessLauncher
Test-Path $CodexlessLauncher
```

For the currently accepted installation layout, `Test-Path` must return `True`.

The launcher resolves to the installed Codexless HTTP launch path and starts the Streamable HTTP MCP service in the foreground.

## Start Codexless HTTP

Open a dedicated **PowerShell** window and run:

```powershell
$CodexlessLauncher = Join-Path $env:LOCALAPPDATA "Codexless\bin\codexless-http.cmd"
& $CodexlessLauncher
```

Leave this window open. It is the primary place to inspect Codexless startup/runtime errors.

Do not start a second copy if port `7690` is already owned by the intended Codexless process.

### Verify Codexless health

Use a separate PowerShell window:

```powershell
Invoke-RestMethod "http://127.0.0.1:7690/healthz" | ConvertTo-Json -Depth 8
```

Confirm at least:

```text
ok            true
service       codexless-public
transport     streamable-http
version       expected installed version
toolCount     expected current total from CURRENT_STATE / active validation
defaultCwd    expected trusted ADS checkout
```

A successful `/healthz` response proves the HTTP runtime is live. When the tool surface has changed, verify the new expected `toolCount` before starting/refeshing downstream tunnel/app state.

Do not treat an ordinary browser GET to `/mcp` as an MCP protocol test. Streamable HTTP MCP requests require the protocol's expected request shape/content type.

## Stop Codexless HTTP

### Preferred path: foreground window still exists

In the PowerShell/terminal window running Codexless, press:

```text
Ctrl+C
```

If Windows asks whether to terminate the batch job, confirm it.

Wait until the command prompt returns before starting the replacement process.

### Recovery path: the foreground window is lost

Do **not** broadly kill every `node.exe` process.

Find the process that owns only the Codexless listener:

```powershell
$listener = Get-NetTCPConnection `
    -LocalAddress 127.0.0.1 `
    -LocalPort 7690 `
    -State Listen `
    -ErrorAction Stop |
    Select-Object -First 1

$codexlessPid = $listener.OwningProcess
Get-CimInstance Win32_Process -Filter "ProcessId = $codexlessPid" |
    Select-Object ProcessId, Name, CommandLine
```

Inspect `CommandLine`. It must identify the intended Codexless installation/launcher path before terminating anything.

Only after that identity check:

```powershell
Stop-Process -Id $codexlessPid
```

Then verify port `7690` is no longer listening before restarting.

## Restart Codexless HTTP

A controlled Codexless-only restart is:

```text
1. stop the existing foreground Codexless process with Ctrl+C;
2. confirm the prompt returned;
3. run the same `%LOCALAPPDATA%\Codexless\bin\codexless-http.cmd` launcher again;
4. leave the new process running in the foreground;
5. query http://127.0.0.1:7690/healthz from another PowerShell window;
6. confirm the expected version, toolCount and defaultCwd before continuing.
```

If `/healthz` still reports the old tool count after a source change, assume the old process was not actually replaced until process/listener inspection proves otherwise. Do not refresh the ChatGPT app against a stale runtime.

## Secure MCP Tunnel profile

The accepted tunnel-client runtime uses a persistent named profile rather than session-local shell variables.

Public-safe invariants:

```text
tunnel-client version family   v0.0.13
profile name                    ads-codexless-local-bridge
MCP target                      http://127.0.0.1:7690/mcp
health/admin listener           http://127.0.0.1:8080
```

The profile is stored in the tunnel client's user-local configuration directory. It contains the non-secret tunnel configuration and a reference to a separate local secret file containing the dedicated Runtime API key. The literal tunnel ID, credential value, user-specific secret-file path and other private coordinates remain `RESOLVED_PRIVATE` and must not be committed to this public repository.

Do not substitute a general `OPENAI_API_KEY` for the dedicated tunnel runtime credential. Do not copy the Runtime API key into the profile YAML, repository, shell history, screenshots, issue text or chat.

The profile and secret file must survive terminal closure and ordinary laptop restart. A new terminal therefore does not need to recreate `CONTROL_PLANE_API_KEY`, `CONTROL_PLANE_TUNNEL_ID`, `MCP_SERVER_URL` or `TUNNEL_EXE` as session-local environment variables.

## Verify tunnel configuration before run

With Codexless already healthy on port `7690`, resolve the user-local tunnel-client executable from the accepted private/local continuity layer and run:

```powershell
& $TunnelExe doctor --profile "ads-codexless-local-bridge"
```

Required healthy evidence includes:

```text
profile_load             PASS
control_plane_api_key    PASS
mcp_target               PASS http://127.0.0.1:7690/mcp
mcp_server_reachable     PASS
health_listener          PASS will bind http://127.0.0.1:8080
RESULT                   ok
```

A `405 Method Not Allowed` result while probing the Streamable HTTP MCP target is acceptable evidence that the route exists; an ordinary GET is not a valid MCP protocol request.

A doctor failure is a stop condition. Fix the reported configuration/runtime problem rather than broadening authority or substituting credentials.

## Start Secure MCP Tunnel

In a dedicated PowerShell window, using the accepted private/local executable path:

```powershell
& $TunnelExe run --profile "ads-codexless-local-bridge"
```

Leave this process running in the foreground. The persistent profile supplies the tunnel ID, MCP target and Runtime API-key reference, so no manual environment-variable rehydration is required after a normal terminal or laptop restart.

## Stop Secure MCP Tunnel

In the foreground PowerShell window running the tunnel client, press:

```text
Ctrl+C
```

Wait for the prompt to return before starting a replacement tunnel process.

## Verify tunnel liveness and readiness

From PowerShell or Command Prompt:

```powershell
curl.exe -sS -i http://127.0.0.1:8080/healthz
curl.exe -sS -i http://127.0.0.1:8080/readyz
```

Required healthy state:

```text
/healthz   HTTP 200 / live
/readyz    HTTP 200 / ready
```

Interpretation:

```text
healthz 200 + readyz 200
    tunnel process and MCP startup/readiness gate are healthy

healthz 200 + readyz 503
    tunnel is alive but the downstream MCP readiness probe failed
    inspect the Codexless foreground terminal first

healthz unavailable
    tunnel process/admin listener is not healthy or not running
```

A previous real failure mode was `readyz 503` while Codexless `/healthz` itself was live because the MCP allowlist contained a tool that the actual live factory had not registered. Therefore tunnel readiness is an important second gate after Codexless liveness.

## Full controlled restart order

Use this order when Codexless code/tool registration changed:

```text
1. stop tunnel-client with Ctrl+C;
2. stop Codexless HTTP with Ctrl+C;
3. restart Codexless from `%LOCALAPPDATA%\Codexless\bin\codexless-http.cmd`;
4. verify Codexless `/healthz` and the expected current toolCount;
5. resolve the accepted private/local tunnel-client executable path;
6. optionally run `& $TunnelExe doctor --profile "ads-codexless-local-bridge"` when configuration/readiness needs reconfirmation;
7. start `& $TunnelExe run --profile "ads-codexless-local-bridge"`;
8. verify tunnel `/healthz` is HTTP 200;
9. verify tunnel `/readyz` is HTTP 200;
10. only after both layers are healthy, refresh the ChatGPT developer MCP app if the tool surface changed;
11. perform a fresh read-only discovery check before invoking any newly added mutation tool.
```

The persistent profile and secret reference survive normal terminal closure and laptop restart, so the restart procedure must not require re-entering the tunnel ID or Runtime API key unless the credential/profile itself was intentionally rotated or removed.

This order prevents a ChatGPT app refresh from snapshotting a stale or partially registered MCP surface.

## Refresh the ChatGPT developer MCP app after a tool-surface change

As observed on 2026-09-01, the current UI path is:

```text
ChatGPT Settings
-> Plug-ins
-> ADS Codexless Local Bridge
-> scroll to the bottom information section
-> Vernieuwen
```

The exact product label/location may change over time. The invariant is to refresh/rescan the existing developer MCP app only after local Codexless and tunnel readiness are healthy.

After refresh, use a **fresh disposable ChatGPT conversation** for a read-only discovery check before the first invocation of a newly added mutation tool.

Do not delete or disconnect the existing app merely to refresh actions unless current product behavior explicitly requires that and the project has separately accepted the consequence.

## Common failure diagnostics

### Codexless `/healthz` still shows the old tool count

Likely causes:

```text
old process was never stopped
wrong installation tree was edited
new process started from a different launcher/source tree
```

Check the listener PID and command line for port `7690`. Do not start multiple competing instances.

### Tunnel `/healthz` is 200 but `/readyz` is 503

The tunnel client is alive, but its MCP startup probe is failing. Inspect the Codexless foreground terminal for initialization/registration errors before changing tunnel configuration.

### ChatGPT does not show a newly added tool

First establish:

```text
Codexless local health uses the expected new surface
Tunnel readyz is 200
```

Then refresh the existing developer MCP app and repeat discovery in a fresh chat. Do not infer a local runtime failure from stale ChatGPT action discovery alone.

### ChatGPT callable count differs from Codexless total tool count

Do not automatically classify the difference as stale discovery. Some actions may intentionally be private/app-only. Compare the active surface contract and visibility before diagnosing the count.

### Browser/manual GET reports unsupported media type on `/mcp`

A browser GET is not a valid Streamable HTTP MCP initialize request. Use `/healthz`, tunnel `/readyz`, or an actual MCP client/discovery flow instead.

### Windows Codex sandbox helper suddenly reports `program not found`

A reproduced 2026-09-07 failure returned:

```text
windows sandbox: orchestrator_helper_launch_failed
setup refresh failed to launch helper
helper=codex-windows-sandbox-setup.exe
error=program not found
```

First separate tunnel health from Codex App Server command execution. If the tunnel is still forwarding and Codexless is reachable, do not restart or reconfigure the tunnel merely because the Windows helper fails.

Inspect the current sandbox log and Codex installation generations. Public-safe locations are:

```powershell
$SandboxLog = Join-Path $HOME ".codex\.sandbox\sandbox.$((Get-Date).ToString('yyyy-MM-dd')).log"
$CodexBin = Join-Path $env:LOCALAPPDATA "OpenAI\Codex\bin"

Get-Content $SandboxLog -Tail 200

Get-ChildItem $CodexBin -Directory -ErrorAction SilentlyContinue |
    Select-Object Name, FullName, CreationTime, LastWriteTime |
    Sort-Object LastWriteTime -Descending

Get-ChildItem $CodexBin -Recurse -File -ErrorAction SilentlyContinue |
    Where-Object {
        $_.Name -in @(
            "codex.exe",
            "codex-command-runner.exe",
            "codex-windows-sandbox-setup.exe",
            "codex-code-mode-host.exe"
        )
    } |
    Select-Object FullName, Length, LastWriteTime
```

Look for a transition from a full generation-qualified helper path to a bare helper-name lookup, and determine whether another installation generation still contains the complete helper set. A failed `where.exe codex-windows-sandbox-setup.exe` is not decisive because healthy Codex normally resolves this helper relative to its own installation generation rather than requiring it on the global `PATH`.

If a complete generation exists but the running Codex process is orphaned from it, use the already-qualified bounded semantic restart rather than opening/closing the desktop UI or broadly killing Codex processes:

```text
codex.runtime_maintenance
    action: restart_codexless
    requestId: one new stable idempotency key
```

Then require durable `status=succeeded` and verify one fresh read-only command. The managed tunnel should remain running for this Codexless-only recovery path.

Do not claim that an app refresh/update caused the generation transition unless independent product evidence establishes that causal link. The observed filesystem timing is correlation evidence only.

### Semantic Git reports a `.git` metadata-write denial

Do not respond by making `.git` generally writable or broadening Windows ACLs. Semantic Git repository-metadata mutation is a distinct bounded authority class. The accepted implementation keeps read-only preflight/postflight through ordinary Codex authority while routing exact `git add` and `git commit` operations through the pre-existing bounded host Git substrate.

If this failure reappears after an update:

```text
1. verify ordinary read-only command execution first;
2. verify the live semantic-Git implementation is the accepted host-metadata-routing version;
3. keep expected-HEAD, exact-path staging, protected-path, diff, branch/upstream and parent checks enabled;
4. do not use ACL broadening, force operations or arbitrary host Git as a workaround;
5. repair or republish the bounded semantic Git implementation if the host-metadata route regressed.
```

Validation 127 / Checkpoint 369 own the qualification evidence for this recovery class.

### A guarded semantic commit fails after staging

Preview.29 changes the normal recovery contract. `codex.git_commit_paths` still requires an initially empty index, but staging introduced by that operation is now automatically restored after a definite pre-commit or commit failure when HEAD remains unchanged and every staged path belongs to the declared transaction scope. Working-tree edits are preserved.

Do not ask the owner to run `git restore --staged -- .` merely because `git diff --cached --check` or another guarded semantic-commit phase failed. First inspect the returned structured details. Healthy automatic recovery includes:

```text
indexRestored=true
rollbackAttempted=true
```

and must be followed by read-only reconciliation when the workflow needs stronger proof. If cleanup cannot be proven, the semantic tool returns `GIT_COMMIT_PATHS_ROLLBACK_FAILED`; preserve that failure and investigate rather than broadening Git authority. If a commit result is uncertain and HEAD changed, automatic rollback is intentionally suppressed because the commit may have succeeded.

Validation 158 / Checkpoint 401 own the live qualification for this transaction-recovery class.

## Security and authority invariants

Operational recovery must not silently change the accepted authority model.

Do not:

```text
expose codex.process on the public surface
switch to danger-full-access
broaden filesystem roots
broaden ACLs merely to make startup pass
replace the bounded Codex authority profile
print or commit tunnel credentials
substitute unrelated API credentials
run a Git mutation merely as a health check
use a wrapper or alternate command to route around ChatGPT/OpenAI safety
```

The active validation record governs any mutation experiment. Startup/restart success is infrastructure evidence, not authorization to perform the next Git action.

## Preservation rule

When the startup topology, launcher, tunnel version, environment-variable contract, ports, app-refresh procedure or recovery sequence changes materially:

```text
1. update this runbook in the same governed development boundary;
2. preserve any private exact values only in the accepted private/local continuity layer;
3. update current state only if the active project boundary changed;
4. verify repository integrity on the resulting public commit.
```

The repository, not the chat transcript, owns the durable operational procedure.
