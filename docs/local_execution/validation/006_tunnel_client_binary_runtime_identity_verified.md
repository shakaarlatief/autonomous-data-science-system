# Tunnel client binary runtime identity verified

**Date:** 2026-08-31  
**Research:** `docs/research/105_codexless_local_execution_bridge_evaluation.md`  
**Classification:** `TUNNEL_CLIENT_BINARY_READY_RUNTIME_KEY_NEXT`

## Observed state

The verified OpenAI Secure MCP Tunnel client archive was extracted locally and the native Windows AMD64 client was executed only for non-mutating informational commands.

Observed runtime identity:

```text
Version                  0.0.13
Embedded source commit   4b5267f823be0b046bb883aacb51603cfde3a0ea
Quickstart interface     PASS
Credential supplied      NO
Tunnel connection        NOT STARTED
```

The embedded source revision exactly matches the source revision already verified through the release checksum and GitHub/Sigstore provenance evidence recorded in validation 005.

The built-in quickstart also confirmed the intended supported flow for this evaluation: use a separate runtime API key for `tunnel-client doctor` / `tunnel-client run`, keep admin-key use separate, and give the runtime principal only the tunnel permissions required to read and use the provisioned tunnel.

## Boundary preserved

No runtime API key, admin API key, tunnel credential, token, or other secret was supplied to the binary or recorded in the repository. The tunnel daemon has not yet been connected to the provisioned tunnel.

The next bounded action is to create a restricted runtime API key with Tunnels Read + Use only, keep the secret machine-local, then configure and doctor the verified tunnel client against the already-running Codexless loopback MCP endpoint before any ChatGPT tool discovery.
