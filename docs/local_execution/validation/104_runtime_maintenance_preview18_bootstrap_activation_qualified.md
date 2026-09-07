# Validation 104: Runtime Maintenance Preview.18 Bootstrap Activation Qualified

**Date:** 2026-09-07
**Status:** PASS / ACTIVE PREVIEW.18 + LOCAL 62-TOOL DISCOVERY / CHATGPT HOST DISCOVERY NEXT
**Research:** Research 122
**Scope:** Verify the final bootstrap activation after source publication without yet invoking the new production mutation tool.

## 1. User-observed bootstrap result

After the full runbook-controlled restart, the local Codexless health endpoint returned:

```text
ok             true
service        codexless-public
transport      streamable-http
publicPreview  true
version        0.1.1-preview.18-runtime-maintenance
surfaceVersion codexless-public-preview-v2
toolCount      62
pid            11788
instanceId     ri_2814fbd1c3dda11cea2b6a818bd2b5b7
defaultCwd     C:\Projects_Data\autonomous-data-science-system
```

The tunnel returned HTTP 200 from both admin endpoints with bodies `live` and `ready`.

## 2. Independent exact-instance verification

A separate read-only ADS command verified:

```text
HealthOk                         true
Version                          0.1.1-preview.18-runtime-maintenance
ToolCount                        62
Surface                          codexless-public-preview-v2
HealthPid                        11788
ListenerPid                      11788
IdentityPid                      11788
HealthInstanceId                 ri_2814fbd1c3dda11cea2b6a818bd2b5b7
IdentityInstanceId               ri_2814fbd1c3dda11cea2b6a818bd2b5b7
IdentityVersion                  0.1.1-preview.18-runtime-maintenance
IdentityToolCount                62
ShutdownTokenPresentAndShapeValid true
ShutdownTokenExposedInHealth     false
TunnelHealth                     live
TunnelReady                      ready
```

This establishes that the active listener, private identity record and public health envelope refer to the exact same runtime instance.

## 3. Direct local MCP discovery

A read-only local MCP client performed:

```text
initialize                       PASS
notifications/initialized        HTTP 202
tools/list                       PASS
toolCount                        62
has codex.runtime_maintenance    true
```

The live tool reports title `Manage Codexless Runtime Lifecycle` and annotations:

```text
readOnlyHint      false
destructiveHint   true
idempotentHint    true
openWorldHint     false
```

The live input schema is exactly a closed `oneOf`:

```text
{ action: "restart_codexless", requestId: <bounded stable id> }
{ action: "status",            requestId: <bounded stable id> }
```

Both branches require `action` and `requestId` and set `additionalProperties: false`.

## 4. Evidence boundary

This validation proves active local preview.18 registration and local MCP discovery only. It does not prove that the ChatGPT host has refreshed its cached developer-MCP projection, and it does not prove a production self-restart yet.

The accepted sequence is now:

```text
local preview.18 / 62 tools       PASS
exact runtime identity            PASS
tunnel live/ready                 PASS
local MCP tools/list              PASS
ChatGPT app refresh               NEXT
fresh-chat host discovery         NEXT
first live restart_codexless      AFTER DISCOVERY ONLY
durable status recovery           AFTER LIVE RESTART
```

```text
PREVIEW18_BOOTSTRAP_ACTIVATION=PASS
LOCAL_MCP_DISCOVERY=PASS
CHATGPT_HOST_DISCOVERY=PENDING
LIVE_SELF_RESTART=PENDING
```
