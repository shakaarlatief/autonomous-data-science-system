# Checkpoint 352: Runtime Maintenance Preview.19 Fresh-Chat Schema Qualified

**Date:** 2026-09-07
**Status:** PASS / CHATGPT HOST PRESERVES FLAT RUNTIME-MAINTENANCE SCHEMA / FIRST LIVE SELF-RESTART NEXT
**Checkpoint class:** HOST INTEGRATION / SAFETY QUALIFICATION
**Project stage:** Research 122 runtime self-maintenance and device-independent access
**Scope:** Preserves the decisive refreshed fresh-chat ChatGPT host qualification of the preview.19 flat runtime-maintenance schema before any production self-restart invocation.
**Authority:** Research 122 governs the architecture; Validation 110 owns the detailed host-projection evidence.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-19`
**Conversation title:** `19 - Hybrid PDF Intent Matrix and Isolation Qualification`
**Primary collaborator:** ChatGPT

After refreshing the existing ADS developer MCP app, a completely fresh disposable ChatGPT conversation discovered `codex.runtime_maintenance` and preserved the corrected preview.19 schema structurally. The fresh chat invoked no ADS tool.

Observed host-projected callable schema:

```text
type codex.runtime_maintenance = (_: {
  action: "restart_codexless" | "status",
  requestId: string,
  // minLength: 1
  // maxLength: 128
  // pattern: /^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$/
}) => any;
```

The host projection therefore passes the mutation-safety gate:

```text
tool exposed                         true
structured object                    true
generic map                          false
properties                           action, requestId
both required                        true
action enum                          restart_codexless | status
requestId type/bounds/pattern        visible
arbitrary additional properties      not structurally exposed
arbitrary host-process authority     absent
```

No separate annotations were visible in the host projection, but this does not weaken the callable schema. Direct local MCP evidence from Validation 109 still records the server annotations and exact `additionalProperties: false`.

The preview.18 host-projection failure from Checkpoint 347 is therefore resolved for this tool by the flat preview.19 schema. The next gate is the first production `restart_codexless` invocation from a fresh ChatGPT host conversation using one stable requestId, followed by durable status recovery after the runtime reconnects.

```text
CHECKPOINT_352=RUNTIME_MAINTENANCE_PREVIEW19_FRESH_CHAT_SCHEMA_QUALIFIED
CHATGPT_HOST_SCHEMA=PASS
LIVE_SELF_RESTART_INVOKED=false
NEXT=FIRST_LIVE_RESTART_CODEXLESS_QUALIFICATION
```
