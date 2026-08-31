# Secure MCP Tunnel runtime ready

**Date:** 2026-08-31  
**Research:** `docs/research/105_codexless_local_execution_bridge_evaluation.md`  
**Classification:** `TUNNEL_RUNTIME_READY_CHATGPT_DISCOVERY_NEXT`

## Observed runtime state

The verified OpenAI `tunnel-client` v0.0.13 was started in foreground mode against the previously provisioned Secure MCP Tunnel, using the dedicated restricted runtime credential and the local Codexless Streamable HTTP MCP endpoint.

The local operator endpoints reported:

```text
/healthz   live
/readyz    ready
```

This establishes that the tunnel daemon is running, its local health surface is live, and its readiness gate is satisfied while forwarding to the governed local Codexless MCP service.

The current proven path is therefore:

```text
ChatGPT workspace association  -> provisioned
OpenAI Secure MCP Tunnel       -> provisioned
verified tunnel-client         -> running / ready
Codexless loopback MCP         -> running / ready
ADS project authority          -> accepted / bounded
ChatGPT custom tool discovery  -> NOT YET VERIFIED
```

No runtime API key, tunnel identifier, workspace identifier, token, or other secret/private operational coordinate is recorded here.

## Boundary preserved

This result does not yet prove that ChatGPT can discover or invoke Codexless tools. The next bounded step is to create the Developer Mode custom plug-in/app connection using the provisioned tunnel, verify tool discovery, and perform read-only ADS calls before any controlled write test.

Browser integration remains deferred. Source Vault ingestion remains paused until the local-execution evaluation reaches an explicit classification boundary.
