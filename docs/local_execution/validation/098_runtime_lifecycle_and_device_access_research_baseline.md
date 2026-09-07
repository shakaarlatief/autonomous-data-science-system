# Validation 098: Runtime Lifecycle and Device Access Research Baseline

**Date:** 2026-09-07
**Status:** PASS / BASELINE EVIDENCE QUALIFIED / RESEARCH 122 ACTIVE
**Scope:** Qualify the repository, local-runtime and current upstream evidence needed to open the runtime self-maintenance and phone/device-access stage without prematurely broadening host authority or weakening tunnel security.

## Repository evidence

The requested work was already preserved before this stage:

```text
AB-001  device-independent ChatGPT access to local ADS connector
AB-002  narrow Codexless runtime self-maintenance authority
AB-006  task recovery after caller/tunnel/device interruption
AB-017  broader host-capability taxonomy beyond workspaces
```

AB-001 records the earlier empirical phone result:

```text
desktop/laptop connector use  PASS
same conversation on phone    401 tunnel_active_organization_required
laptop remained running       YES
```

AB-002 records repeated safe publication cases where ordinary workspace authority intentionally could not write the installed Codexless tree under `%LOCALAPPDATA%`, forcing guarded ordinary-host helpers or temporary exact-root admission. The backlog explicitly rejects solving this by registering the whole install/user-profile root as an ordinary workspace.

Research 116 also explicitly left runtime maintenance, process lifecycle, Windows services/registry and credential stores outside ordinary workspace authority.

## Current local topology

The accepted topology remains:

```text
ChatGPT developer MCP app
-> OpenAI Secure MCP Tunnel
-> local tunnel-client
-> Codexless Streamable HTTP MCP
-> local Codex authority/runtime
```

The current public command surface intentionally has no general host-process control.

## Exact installed tunnel-client capability probe

The current installed tunnel-client v0.0.13 was queried read-only. Its native managed-runtime command tree is present:

```text
runtimes cleanup
runtimes connect
runtimes create
runtimes list
runtimes rm
runtimes status
runtimes stop
```

`runtimes connect --help` states that it creates/reuses a tunnel alias and runs a native profile through managed local runtime supervision, and that this path should be used for a long-lived local runtime managed by Codex.

This matches current upstream OpenAI tunnel-client documentation:

```text
https://github.com/openai/tunnel-client/blob/master/docs/onboarding.md
https://github.com/openai/tunnel-client/blob/master/plugins/tunnel-mcp/skills/tunnel-mcp/references/runtime-flows.md
https://github.com/openai/tunnel-client/blob/master/plugins/tunnel-mcp/skills/tunnel-mcp/references/profiles-state-and-keys.md
```

## Managed-runtime state authority discriminator

A read-only local call to:

```text
tunnel-client runtimes list --json
```

failed under ordinary ADS workspace authority when the binary attempted to create its default platform state directory under the user profile. The failure was an access denial at state-directory creation, not a missing command or tunnel-client protocol failure.

The same command then succeeded when `TUNNEL_CLIENT_STATE_DIR` was redirected to a bounded ADS `.tmp` directory. It returned a valid empty alias inventory and exact state root inside that bounded directory.

Therefore:

```text
NATIVE_MANAGED_RUNTIME_SUPPORT            PRESENT
ORDINARY_WORKSPACE_ACCESS_TO_USER_STATE   DENIED AS DESIGNED
BOUNDED_ALTERNATE_STATE_ROOT              WORKS
ARCHITECTURE_SEAM                         DEDICATED RUNTIME-MAINTENANCE AUTHORITY
```

No live production tunnel, tunnel ID, runtime key or remote tunnel state was mutated during this probe.

## Self-restart dependency

A lifecycle tool hosted only inside Codexless cannot safely stop the process serving its own request and synchronously guarantee a final response. Stopping the tunnel has the same dependency at the transport layer.

This baseline therefore rejects a generic process-kill tool as the architecture. The candidate must use either a separate supervisor/front door or a bounded deferred restart helper that accepts a server-owned operation while the normal MCP path is still available and completes recovery independently.

## Current official phone/mobile product evidence

Current OpenAI Help Center documentation for Developer Mode/MCP apps states that MCP apps are not available on mobile and are web-only:

```text
https://help.openai.com/en/articles/12584461-developer-mode-and-full-mcp-connectors-in-chatgpt-beta
```

Current official tunnel-client OpenAPI also documents `tunnel_active_organization_required` as an organization-context error for organization-backed tunnels. This makes the historical phone failure consistent with a caller path that lacked the required active organization context, but does not establish that this exact missing context is the only mobile blocker.

The acceptance consequence is:

```text
DO NOT weaken tunnel auth/principal validation
DO NOT assume laptop/tunnel downtime from the phone 401
TEST native mobile and mobile web separately
PREFER mobile web if the supported web MCP surface works there
```

## Initial result

```text
REPOSITORY_PRIOR_WORK_FOUND              PASS
INSTALLED_TUNNEL_MANAGED_RUNTIME_FOUND   PASS
MANAGED_STATE_AUTHORITY_SEAM             REPRODUCED
CURRENT_SELF_RESTART_LIMIT               CONFIRMED ARCHITECTURALLY
OFFICIAL_NATIVE_MOBILE_MCP_SUPPORT        NOT AVAILABLE / WEB ONLY
PHONE_401_TUNNEL_DOWN_INFERENCE           REJECTED
RESEARCH_122                              OPEN
```
