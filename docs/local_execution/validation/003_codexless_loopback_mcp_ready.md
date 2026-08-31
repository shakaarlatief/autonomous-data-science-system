# Codexless loopback MCP validation

**Date:** 2026-08-31  
**Research:** `docs/research/105_codexless_local_execution_bridge_evaluation.md`  
**Classification:** `LOOPBACK_MCP_READY_SECURE_TUNNEL_NEXT`

## Result

After the Codexless local install and project-authority doctor passed, the public Codexless HTTP transport was started against the ADS repository and validated locally before any tunnel or ChatGPT custom connection was created.

Observed result:

```text
Codexless version        0.1.1-preview.5
surface                  codexless-public-preview-v1
transport                streamable-http
public tool count        42
health endpoint          PASS / ok=true
ready endpoint           PASS / ok=true
local bind               loopback only
ChatGPT tunnel           NOT YET CONFIGURED
ChatGPT custom plugin    NOT YET CONNECTED
browser integration      DEFERRED
Source Vault ingestion   NOT STARTED
```

The local HTTP service reported the intended ADS repository as its default working root. No public inbound listener was opened; Codexless remained on its loopback-only transport.

## Boundary

This validation proves only the local MCP service boundary. It does not prove Secure MCP Tunnel connectivity, ChatGPT tool discovery, read-only local calls from ChatGPT, write confirmation behavior, or accepted ADS adoption.

The next bounded step is to provision and validate an authenticated Secure MCP Tunnel, then add the resulting tunnel to ChatGPT Developer Mode and inspect the discovered tool metadata before any tool invocation.
