# Tunnel runtime doctor ready

**Date:** 2026-08-31  
**Research:** `docs/research/105_codexless_local_execution_bridge_evaluation.md`  
**Classification:** `TUNNEL_RUNTIME_DOCTOR_PASS_FOREGROUND_RUN_NEXT`

## Observed state

The official OpenAI `tunnel-client` v0.0.13 was configured in a machine-local shell with a dedicated restricted runtime API key, the provisioned tunnel identifier, and the local Codexless Streamable HTTP MCP endpoint.

No secret value is recorded here. The runtime API key remained session-local and was not echoed into the shell transcript. Exact tunnel/workspace identifiers remain private operational coordinates and are intentionally omitted from the public repository.

`tunnel-client doctor --explain` completed successfully.

```text
configuration source          flags/environment only
control-plane API key         PASS / environment reference
provisioned tunnel id         PASS
MCP target                    PASS / loopback Codexless endpoint
MCP reachability              PASS
OAuth metadata                PASS / not advertised
health listener               PASS / loopback
admin UI                      PASS / loopback
Codex tunnel plugin           SKIP / optional and not required for ChatGPT path
RESULT                        ok
NEXT                          tunnel-client run
```

The MCP reachability probe received HTTP 405 from the MCP endpoint. For this Streamable HTTP MCP target, that is evidence that the endpoint is reachable while rejecting the probe method rather than evidence of endpoint absence.

## Boundary preserved

The runtime key is deliberately restricted to the tunnel runtime use case. The optional Codex tunnel plugin remains uninstalled because the current evaluation is the ChatGPT-to-Codexless path, not the Codex-native plugin path.

Source Vault ingestion remains paused. The next bounded action is to start the verified tunnel client in the foreground with the existing session-local runtime configuration, verify local tunnel-client health/readiness, then create the ChatGPT custom tunnel connection and perform read-only tool discovery before any write-capability test.
