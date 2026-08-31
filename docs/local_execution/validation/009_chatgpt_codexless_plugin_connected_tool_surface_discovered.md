# ChatGPT Codexless plug-in connected and tool surface discovered

**Date:** 2026-08-31  
**Research:** `docs/research/105_codexless_local_execution_bridge_evaluation.md`  
**Classification:** `CHATGPT_PLUGIN_CONNECTED_READ_ONLY_VALIDATION_NEXT`

## Observed product state

The custom ChatGPT developer-mode plug-in `ADS Codexless Local Bridge` was successfully connected through the provisioned OpenAI Secure MCP Tunnel while both the local Codexless MCP service and official tunnel-client runtime were healthy and ready.

The ChatGPT plug-in settings surface displayed discovered Codexless actions, including `codex.account_preflight`, confirming successful MCP tool discovery through the full product path.

```text
ChatGPT developer mode       ENABLED
Custom plug-in               CONNECTED
Secure MCP Tunnel            CONNECTED / READY
Codexless local MCP          READY
Tool discovery               PASS
Discovered action surface    VISIBLE IN CHATGPT
Browser integration          DEFERRED
Source Vault ingestion       NOT STARTED
```

The exact tunnel identifier, workspace identifier, runtime API key, and other private operational coordinates are intentionally omitted from this public record.

## Permission state

At connection time, the plug-in inherited the user's current default ChatGPT plug-in permission mode. No permission broadening was performed as part of this validation.

## Boundary preserved

This milestone proves transport and tool discovery only. It does not yet classify arbitrary local reads, writes, command execution, long-running process handling, or browser integration as accepted for ADS use.

The next bounded validation is a harmless read-only operation against the approved ADS repository, followed by a controlled disposable write test only if the read-only path behaves as expected. Source Vault ingestion remains paused until the local-execution evaluation reaches an explicit acceptance boundary.
