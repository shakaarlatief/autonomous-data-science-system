# Existing-chat developer MCP invocation blocked

**Date:** 2026-08-31  
**Research:** `docs/research/105_codexless_local_execution_bridge_evaluation.md`  
**Classification:** `PLUGIN_DISCOVERED_HOST_INVOCATION_BLOCKED_IN_EXISTING_CHAT`

## Observed state

The custom ChatGPT plug-in `ADS Codexless Local Bridge` was installed successfully and its Codexless action surface was visible in ChatGPT settings. The Secure MCP Tunnel runtime remained healthy and ready, with the local Codexless MCP server running behind the tunnel.

A read-only local repository inspection was then requested from the pre-existing ADS conversation after explicitly mentioning the new plug-in. ChatGPT loaded the Codexless developer-MCP tool namespace for the turn, but the first attempted model-free local read was rejected by the ChatGPT host before reaching the local bridge:

```text
FORBIDDEN: This conversation does not support developer MCPs
```

The attempted action was a read-only `git rev-parse --show-toplevel` call scoped to the ADS repository. No local command was dispatched through Codexless and no local file, process, repository, Source Vault, or registry state was modified.

## Interpretation

This is not evidence of a Codexless, tunnel-client, local MCP, project-authority, or tunnel-readiness failure. Those layers had already passed their respective doctor/health/readiness checks and ChatGPT had already discovered the plug-in action surface.

The failure is currently classified as a ChatGPT conversation-host capability boundary affecting this already-running conversation. The next bounded test is to start a fresh chat after the developer plug-in is already installed and repeat the same read-only local inspection there before changing any local permissions, tunnel configuration, or Codexless settings.

## Boundary preserved

```text
Codexless local MCP            READY
Secure MCP Tunnel runtime      READY
ChatGPT plug-in installation   READY
ChatGPT tool discovery         READY
Existing-chat invocation       BLOCKED BY HOST
Local write validation         NOT STARTED
Source Vault ingestion         NOT STARTED
```

No permission broadening is authorized by this result.
