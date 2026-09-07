# Checkpoint 346: Runtime Maintenance Preview.18 Bootstrap Activation Qualified

**Date:** 2026-09-07
**Status:** PASS / PREVIEW.18 ACTIVE / 62-TOOL LOCAL DISCOVERY PASS / CHATGPT APP REFRESH NEXT
**Checkpoint class:** LOCAL EXECUTION / LIFECYCLE ACTIVATION
**Project stage:** Research 122 runtime self-maintenance and device-independent access
**Scope:** Qualifies the one final manual bootstrap restart that activated the already-published preview.18 runtime-maintenance source, exact runtime-instance binding, local 62-tool MCP discovery, and healthy tunnel recovery.
**Authority:** Research 122 governs the architecture; Validation 104 owns the detailed activation evidence.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-19`
**Conversation title:** `19 - Hybrid PDF Intent Matrix and Isolation Qualification`
**Primary collaborator:** ChatGPT

The runbook-controlled bootstrap restart completed successfully. The active local runtime now reports:

```text
ok             true
version        0.1.1-preview.18-runtime-maintenance
surfaceVersion codexless-public-preview-v2
toolCount      62
```

The production tunnel recovered to:

```text
/healthz  HTTP 200 / live
/readyz   HTTP 200 / ready
```

Independent read-only verification proved that the listener PID, `/healthz` PID, private runtime-instance PID and instance ID all match the same exact process. The private shutdown token is present with the expected opaque shape and is not exposed by `/healthz`.

A direct local MCP initialize + tools/list then succeeded against the active preview.18 process. The returned list contains exactly 62 tools and includes `codex.runtime_maintenance`. Its live input schema is the expected closed union of `{action: restart_codexless, requestId}` and `{action: status, requestId}`, with `additionalProperties: false`; annotations mark the restart action as destructive, idempotent and closed-world.

No production self-restart has been invoked yet. The next boundary is ChatGPT-host discovery: refresh the existing developer MCP app only now that local runtime and tunnel readiness are healthy, then use a fresh disposable chat to confirm `codex.runtime_maintenance` is projected before invoking it.

```text
CHECKPOINT_346=PREVIEW18_BOOTSTRAP_ACTIVATION_QUALIFIED
ACTIVE_VERSION=0.1.1-preview.18-runtime-maintenance
ACTIVE_TOOL_COUNT=62
LOCAL_MCP_DISCOVERY=PASS
TUNNEL=LIVE_READY
LIVE_SELF_RESTART_TESTED=false
NEXT=CHATGPT_APP_REFRESH_AND_FRESH_CHAT_DISCOVERY
```
