# Validation 067: ChatGPT Host Capability Probe Live, Same-Chat Projection Stale

**Date:** 2026-09-06
**Status:** LIVE RUNTIME QUALIFIED / TUNNEL READY / CURRENT CHAT TOOL PROJECTION STALE / FRESH-CHAT HOST HANDSHAKE PENDING
**Research:** Research 117 / Research 119
**Scope:** Qualify the temporary model-free MCP Apps host-capability diagnostic needed to decide whether the current ChatGPT host advertises a direct `ui/update-model-context` `resourceLink` path before falling back to multi-PDF resource-link splitting.

## Governing objective

Research 119 remains authoritative. The target is ordinary ChatGPT gaining direct bounded access to authorized local-machine files through Codexless, not a semantic-worker intermediary and not automatically the future ADS product architecture.

The narrow open question is whether the current ChatGPT MCP Apps host advertises a supported model-context capability for `resourceLink` content. If it does, that route deserves a small direct-source qualification before PDF splitting. If it does not, the multi-native-PDF resource-link experiment remains the next direct-access candidate.

## Candidate

The private local-runtime repository preserves the complete reviewed candidate under:

```text
.ads-private/codexless/chatgpt-host-capability-probe-candidate/
```

The temporary live surface is:

```text
version     0.1.1-preview.15-host-capability-probe
toolCount   59
```

Added tools:

```text
codex.host_capability_probe
codex.host_capability_probe_report     app-only
codex.host_capability_probe_result
```

Added MCP App resource:

```text
ui://toolwire/chatgpt-host-capability-probe-v1.html
text/html;profile=mcp-app
```

The diagnostic performs only the standard MCP Apps `ui/initialize` handshake and records a whitelist of advertised host capability metadata. It reads no local file bytes, invokes no Browser, calls no upload/file-picker helper, and does not invoke `ui/update-model-context` or `ui/download-file` during capability discovery.

## Static qualification

Before publication:

```text
syntax checks                                      PASS
probe + factory tests                              9 / 9 PASS
formal guard regression                            PASS
flexible-authority regression                      7 / 7 PASS
real MCP SDK registration inspection               PASS
candidate/live source delta                        exactly 4 source files
```

The candidate distinguishes protocol support from host advertisement. MCP Apps defines `updateModelContext` and can advertise `resourceLink`, but that does not prove this exact ChatGPT host enables the modality.

## Publication and lifecycle

The exact candidate source was published to the installed Codexless source tree with pre-mutation backups and post-write SHA-256 verification. A temporary exact-root `codexless-live` workspace admission was used only because the existing public surface has no accepted semantic runtime-maintenance tool. After publication, that temporary Codexless admission was removed again so the runtime install is not left as an ordinary writable workspace.

Current durable workspace registry after removal:

```text
revision       7
content hash   5cd85c57465e7f3da0a19888f28c8e0afe128dbb32f7ff2f7056bd6021dbaa31
workspaces     ads-public, ads-local-runtime, big-data-statistics, machine-learning
```

The user then followed the canonical `docs/local_execution/OPERATIONS.md` lifecycle for a tool-surface change:

```text
stop tunnel while keeping its Git Bash shell open
stop/restart Codexless
verify local runtime
restart/verify tunnel
refresh existing ChatGPT Plugin
```

Direct post-restart evidence:

```text
Codexless /healthz
    ok          true
    version     0.1.1-preview.15-host-capability-probe
    toolCount   59

Secure MCP Tunnel /readyz
    ready
```

Therefore the new source is live and reachable through the tunnel.

## Same-conversation tool projection result

After the user refreshed `ADS Codexless Local Bridge`, ChatGPT re-ran tool discovery in this same persistent conversation using a `host_capability` query.

Result:

```text
live server surface             59 tools
new probe tools on live server  yes
current ChatGPT callable projection
    host-capability tools       NOT EXPOSED
```

The discovery response still reflected the older projected callable set. This is another concrete reproduction of the known same-conversation MCP tool-projection staleness already preserved by Validation 034 and AB-008.

This result does **not** establish that the fresh ChatGPT host cannot render or execute the MCP App. It establishes only that this existing conversation did not acquire the newly added tool schemas after refresh.

## Exact next experiment

A fresh disposable ChatGPT conversation is now required.

In that new conversation:

```text
1. verify the refreshed Plugin exposes codex.host_capability_probe and codex.host_capability_probe_result;
2. call codex.host_capability_probe;
3. allow the MCP App to complete its ui/initialize handshake;
4. call codex.host_capability_probe_result;
5. inspect only the whitelisted host capability receipt;
6. classify updateModelContext.resourceLink as ADVERTISED or NOT_ADVERTISED.
```

Decision rule:

```text
ADVERTISED
    -> qualify one tiny known PDF resourceLink through ui/update-model-context
    -> no Browser, upload, or semantic substitution

NOT_ADVERTISED
    -> stop this MCP Apps model-context route for the current host
    -> proceed to the deterministic multi-native-PDF document_file_link experiment
```

Do not infer large-file success merely from capability advertisement. A positive advertisement only permits the next small direct-source test.

## Result

```text
HOST_CAPABILITY_PROBE_SOURCE = LIVE
LIVE_VERSION = 0.1.1-preview.15-host-capability-probe
LIVE_TOOL_COUNT = 59
TUNNEL_READYZ = PASS
CURRENT_CHAT_PLUGIN_REFRESH = PERFORMED
CURRENT_CHAT_NEW_TOOL_PROJECTION = STALE
HOST_UPDATE_MODEL_CONTEXT_RESOURCE_LINK = NOT_YET_OBSERVED
NEXT = FRESH_DISPOSABLE_CHAT_HOST_CAPABILITY_HANDSHAKE
```
