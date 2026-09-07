# Validation 109: Runtime Maintenance Preview.19 Bootstrap Activation Qualified

**Date:** 2026-09-07
**Status:** PASS / ACTIVE PREVIEW.19 + PROCESS-LIVE FLAT MCP SCHEMA / CHATGPT HOST DISCOVERY PENDING
**Research:** Research 122
**Scope:** Verify preview.19 after the manual activation restart and establish the exact local/server baseline for the decisive fresh-host schema projection test.

## 1. User-observed health and tunnel result

After the controlled restart, Codexless returned:

```text
ok             true
service        codexless-public
transport      streamable-http
publicPreview  true
version        0.1.1-preview.19-runtime-maintenance-schema
surfaceVersion codexless-public-preview-v2
toolCount      62
pid            8564
instanceId     ri_e052fa7c74b0e00929277d8245c1bea6
defaultCwd     C:\Projects_Data\autonomous-data-science-system
```

The tunnel endpoints returned HTTP 200 with bodies `live` and `ready`.

## 2. Independent exact-instance verification

A separate read-only ADS verification established:

```text
HealthOk                          true
Version                           0.1.1-preview.19-runtime-maintenance-schema
ToolCount                         62
Surface                           codexless-public-preview-v2
HealthPid                         8564
ListenerPid                       8564
IdentityPid                       8564
HealthInstanceId                  ri_e052fa7c74b0e00929277d8245c1bea6
IdentityInstanceId                ri_e052fa7c74b0e00929277d8245c1bea6
IdentityVersion                   0.1.1-preview.19-runtime-maintenance-schema
IdentityToolCount                 62
ShutdownTokenPresentAndShapeValid true
ShutdownTokenExposedInHealth      false
TunnelHealth                      live
TunnelReady                       ready
```

The private runtime repository remains synchronized at `ac3e05de0ebd9553eafb322ce19ec17539f1c09d`; the only private working-tree state is protected untracked `.tmp` publication scratch.

## 3. Process-live local MCP schema verification

A direct local MCP client sent `initialize`, `notifications/initialized`, and `tools/list` to the active preview.19 process. Observed runtime-maintenance definition:

```text
toolCount              62
hasRuntimeMaintenance  true
type                   object
topLevelOneOf          false
properties             action, requestId
required               action, requestId
additionalProperties   false
actionEnum             restart_codexless, status
requestId.type         string
requestId.minLength    1
requestId.maxLength    128
requestId.pattern      ^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$
```

Annotations:

```text
readOnlyHint      false
destructiveHint   true
idempotentHint    true
openWorldHint     false
```

This is stronger than candidate/source evidence: the exact corrected schema is now serialized by the active production-local MCP process.

## 4. Evidence boundary

This validation does not yet establish ChatGPT host projection fidelity. Validation 105 showed that preview.18 local/MCP strictness was not sufficient because the fresh ChatGPT host genericized the top-level union. Therefore the project still requires a refreshed fresh-chat discovery test against preview.19.

The next accepted sequence is:

```text
preview.19 active local process     PASS
exact instance binding             PASS
local flat MCP schema              PASS
tunnel live/ready                  PASS
refresh existing developer MCP app NEXT
fresh-chat schema projection       NEXT
first live restart_codexless       ONLY AFTER HOST SCHEMA PASS
```

```text
PREVIEW19_BOOTSTRAP_ACTIVATION=PASS
LOCAL_FLAT_SCHEMA=PASS
CHATGPT_HOST_SCHEMA=PENDING
LIVE_SELF_RESTART=PENDING
```
