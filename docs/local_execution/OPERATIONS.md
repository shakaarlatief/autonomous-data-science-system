# Local Execution Operations Runbook

**Status:** Current evergreen operational procedure  
**Last reviewed:** 2026-09-01  
**Scope:** Start, stop, restart, verify and reconnect the ADS Codexless loopback HTTP service and OpenAI Secure MCP Tunnel without relying on chat memory.  
**Authority:** Operational procedure only. `docs/CURRENT_STATE.md` and the active validation record own the current experiment, expected tool surface and next mutation. This runbook does not widen local authority or replace the security contracts in the validation records.

## Purpose

The ADS local-execution path must be recoverable from repository evidence even after a chat, terminal window or model context is lost.

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

This public runbook records commands, derived locations, ports, environment-variable names and verification procedure.

It deliberately does **not** record:

```text
CONTROL_PLANE_API_KEY value
CONTROL_PLANE_TUNNEL_ID value
private workspace/tunnel identifiers
other credentials or secrets
```

Those values are `RESOLVED_PRIVATE` operational state. Retrieve them from the accepted private/local continuity layer when needed. Never commit them to the public repository and never print them merely for diagnostics.

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

## Secure MCP Tunnel shell

The accepted tunnel-client runtime is operated from **Git Bash**.

Public-safe derived paths:

```bash
TUNNEL_HOME="$HOME/ADS-Private/Tooling/OpenAI-Tunnel-Client/v0.0.13"
TUNNEL_EXE="$TUNNEL_HOME/extracted/tunnel-client.exe"
export MCP_SERVER_URL="http://127.0.0.1:7690/mcp"
```

The same Git Bash shell should hold these session-local private variables:

```text
CONTROL_PLANE_API_KEY
CONTROL_PLANE_TUNNEL_ID
```

Check only whether variables are set, without printing their values:

```bash
for v in CONTROL_PLANE_API_KEY CONTROL_PLANE_TUNNEL_ID MCP_SERVER_URL TUNNEL_EXE; do
  if [ -n "${!v}" ]; then
    printf '%s: SET\n' "$v"
  else
    printf '%s: MISSING\n' "$v"
  fi
done
```

If the Git Bash shell was closed and the private variables are no longer present, restore their values from the accepted private/local continuity source. If manual secure entry is required, use non-echoing prompts rather than command-line literals:

```bash
read -rsp "Tunnel runtime API key: " CONTROL_PLANE_API_KEY
echo
export CONTROL_PLANE_API_KEY

read -rsp "Tunnel ID: " CONTROL_PLANE_TUNNEL_ID
echo
export CONTROL_PLANE_TUNNEL_ID
```

Do not place those literal values in this public runbook, shell history, screenshots, issue text or chat unless a secure operational step specifically requires them.

## Verify tunnel configuration before run

With Codexless already healthy on port `7690`, run in the tunnel Git Bash shell:

```bash
"$TUNNEL_EXE" doctor --explain
```

The doctor should confirm the configured tunnel runtime, MCP target and local listener prerequisites without revealing the private credential values.

A doctor failure is a stop condition. Fix the reported configuration/runtime problem rather than broadening authority or substituting credentials.

## Start Secure MCP Tunnel

In the same Git Bash shell:

```bash
"$TUNNEL_EXE" run
```

Leave this process running in the foreground.

Do not close that Git Bash shell during normal restart work if you want to retain its session-local environment variables.

## Stop Secure MCP Tunnel

In the foreground Git Bash window running the tunnel client, press:

```text
Ctrl+C
```

For a short controlled restart, keep the Git Bash shell itself open. The shell then retains the session-local variables while the tunnel process is stopped.

If the shell is closed, treat the private variables as no longer available and rehydrate them from private/local continuity before the next run.

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
1. stop tunnel-client with Ctrl+C, but keep its Git Bash shell open;
2. stop Codexless HTTP with Ctrl+C;
3. restart Codexless from `%LOCALAPPDATA%\Codexless\bin\codexless-http.cmd`;
4. verify Codexless `/healthz` and the expected current toolCount;
5. in Git Bash, confirm tunnel variables are SET without printing their values;
6. optionally run `"$TUNNEL_EXE" doctor --explain` when configuration/readiness needs reconfirmation;
7. start `"$TUNNEL_EXE" run`;
8. verify tunnel `/healthz` is HTTP 200;
9. verify tunnel `/readyz` is HTTP 200;
10. only after both layers are healthy, refresh the ChatGPT developer MCP app if the tool surface changed;
11. perform a fresh read-only discovery check before invoking any newly added mutation tool.
```

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
