# Tunnel client supply-chain verification passed

**Date:** 2026-08-31  
**Research:** `docs/research/098_codexless_local_execution_bridge_evaluation.md`  
**Classification:** `OFFICIAL_TUNNEL_CLIENT_ARCHIVE_VERIFIED_RUNTIME_KEY_NEXT`

## Observed state

The official OpenAI Secure MCP Tunnel client release archive for Windows AMD64 was downloaded from the OpenAI `tunnel-client` v0.0.13 release and verified before any credential was supplied to the executable.

```text
Release                         v0.0.13
Platform                        Windows AMD64
Archive                         tunnel-client-v0.0.13-windows-amd64.zip
Published SHA-256               MATCH
GitHub/Sigstore provenance      PASS
Signer repository               openai/tunnel-client
Signer workflow                 .github/workflows/release.yml@refs/tags/v0.0.13
Source ref                      refs/tags/v0.0.13
Source/build digest             4b5267f823be0b046bb883aacb51603cfde3a0ea
Runner environment              github-hosted
Tunnel runtime credential       NOT YET SUPPLIED
Tunnel daemon                   NOT YET CONNECTED
ChatGPT tool discovery          NOT YET STARTED
Source Vault ingestion          NOT STARTED
```

The archive SHA-256 matched the release-published checksum exactly, and `gh attestation verify` accepted the release provenance under the expected repository, workflow, source ref, source/build digest, OIDC issuer, and GitHub-hosted runner constraints.

No API key, token, credential, tunnel identifier, workspace identifier, or other private operational coordinate is recorded here.

## Boundary preserved

This verification establishes the provenance of the local tunnel-client binary package only. It does not establish runtime authorization or remote reachability.

The next bounded actions are to inspect the verified binary's version/quickstart interface, create a Restricted runtime API key with Tunnels Read + Use only, run tunnel-client doctor against the already-provisioned tunnel and local Codexless MCP endpoint, then start the foreground tunnel daemon and verify health/readiness before creating the ChatGPT custom connection.

Browser integration remains deferred. The first permanent Source Vault ingestion remains paused until the local-execution evaluation reaches an explicit classification boundary.
