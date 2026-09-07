# Validation 110: Runtime Maintenance Preview.19 Fresh-Chat Schema Qualified

**Date:** 2026-09-07
**Status:** PASS / REFRESHED CHATGPT HOST PRESERVES STRUCTURED FLAT SCHEMA / NO MUTATION
**Research:** Research 122
**Scope:** Determine whether the refreshed ChatGPT host preserves the preview.19 runtime-maintenance callable schema strongly enough to authorize the first production self-restart test.

## 1. Fresh-host procedure

The user refreshed the existing ADS developer MCP app after Validation 109 had established active preview.19 / 62 tools and the process-live local flat MCP schema. A completely fresh disposable chat was then instructed to perform discovery only and not invoke any ADS tool.

The fresh chat reported `codex.runtime_maintenance` as exposed.

## 2. Host-projected callable schema

Observed definition:

```text
type codex.runtime_maintenance = (_: {
  action: "restart_codexless" | "status",
  requestId: string,
  // minLength: 1
  // maxLength: 128
  // pattern: /^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$/
}) => any;
```

This is materially different from Validation 105's failed preview.18 projection:

```text
preview.18 host projection  { [key: string]: any }   FAIL
preview.19 host projection  action + requestId      PASS
```

## 3. Qualification criteria

The fresh chat established all required conditions:

```text
codex.runtime_maintenance exposed                PASS
structured top-level object                      PASS
only action + requestId exposed                  PASS
action required                                  PASS
requestId required                               PASS
action enum structurally visible                 PASS
requestId string type visible                    PASS
requestId length/pattern visible                 PASS
generic index signature absent                   PASS
arbitrary host-process fields absent             PASS
```

The host display did not literally print the JSON-Schema line `additionalProperties: false`, but unlike the failed preview.18 projection it exposed a closed structured callable object containing only `action` and `requestId` and no generic index signature. This satisfies the qualification's explicitly accepted equivalent condition.

## 4. Authority boundary

The host-projected input exposes no PID, executable, command/argv, cwd, filesystem path, environment, URL, tunnel identity, credential, permission profile, sandbox, or other arbitrary process-control input. The only caller-controlled values are the two-action enum and bounded stable requestId.

No ADS tool was invoked in the fresh chat. Therefore no restart or other mutation occurred.

## 5. Next qualification

The first production self-restart may now be tested. It should use one predeclared stable requestId and exactly one `restart_codexless` call. The expected first receipt is `armed`, returned before the fixed destructive delay. The tunnel should remain running. After Codexless reconnects, status for the exact same requestId must resolve the durable operation to terminal `succeeded`; replaying the restart with the same requestId is permitted only as an explicit idempotency qualification after terminal status is established, not as an automatic retry.

```text
RUNTIME_MAINTENANCE_PREVIEW19_FRESH_CHAT_SCHEMA=PASS
LIVE_MUTATION=false
NEXT=FIRST_PRODUCTION_SELF_RESTART
```
