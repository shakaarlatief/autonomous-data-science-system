# Checkpoint 351: Runtime Maintenance Preview.19 Bootstrap Activation Qualified

**Date:** 2026-09-07
**Status:** PASS / PREVIEW.19 ACTIVE + FLAT LOCAL MCP SCHEMA VERIFIED / CHATGPT HOST REFRESH NEXT
**Checkpoint class:** LOCAL EXECUTION / LIFECYCLE ACTIVATION
**Project stage:** Research 122 runtime self-maintenance and device-independent access
**Scope:** Qualifies the manual activation restart for the preview.19 flat-schema correction, exact runtime-instance binding, tunnel recovery, and process-live local MCP schema fidelity before ChatGPT host refresh.
**Authority:** Research 122 governs the architecture; Validation 109 owns the detailed activation evidence.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-19`
**Conversation title:** `19 - Hybrid PDF Intent Matrix and Isolation Qualification`
**Primary collaborator:** ChatGPT

The manual runbook-controlled activation restart completed successfully. Active Codexless now reports:

```text
version        0.1.1-preview.19-runtime-maintenance-schema
surfaceVersion codexless-public-preview-v2
toolCount      62
pid            8564
instanceId     ri_e052fa7c74b0e00929277d8245c1bea6
```

Independent read-only verification proved that the listener PID, public health PID, private runtime-identity PID and instance ID all refer to the same process. The private shutdown token exists with the expected opaque shape and is not exposed through `/healthz`. The tunnel is `live/ready`.

A direct process-live MCP `initialize` + `tools/list` returned exactly 62 tools and included `codex.runtime_maintenance` with the corrected flat schema:

```text
type                    object
top-level oneOf         false
properties              action, requestId
required                action, requestId
additionalProperties    false
action enum             restart_codexless, status
requestId length        1..128
requestId pattern       ^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$
```

Tool annotations remain `readOnlyHint=false`, `destructiveHint=true`, `idempotentHint=true`, `openWorldHint=false`.

No production self-restart has been invoked yet. The next gate is ChatGPT host projection after refreshing the existing developer MCP app and opening a fresh disposable conversation. Only if that fresh chat structurally exposes the same flat schema may the first live `restart_codexless` qualification proceed.

```text
CHECKPOINT_351=RUNTIME_MAINTENANCE_PREVIEW19_BOOTSTRAP_ACTIVATION_QUALIFIED
ACTIVE_PREVIEW19=true
LOCAL_MCP_FLAT_SCHEMA=PASS
TUNNEL=live/ready
LIVE_SELF_RESTART=false
NEXT=REFRESH_APP_AND_FRESH_CHAT_SCHEMA_DISCOVERY
```
