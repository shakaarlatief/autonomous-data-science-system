# Checkpoint 343: Runtime Maintenance Preview.18 Integration Qualified

**Date:** 2026-09-07
**Status:** PASS / PRODUCTION-SHAPED CODEXLESS-ONLY RESTART + 62-TOOL INTEGRATION QUALIFIED / GUARDED PUBLICATION PREFLIGHT NEXT
**Checkpoint class:** ARCHITECTURE / LOCAL EXECUTION / LIFECYCLE QUALIFICATION
**Project stage:** Research 122 runtime self-maintenance and device-independent access
**Scope:** Qualifies the production-shaped direct `codex.runtime_maintenance` dispatch path, exact runtime-instance binding, authenticated loopback graceful shutdown, fixed replacement launch, durable terminal state, and the private preview.18 62-tool integration candidate without mutating production.
**Authority:** Research 122 governs the architecture; Validation 101 owns the detailed evidence.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-19`
**Conversation title:** `19 - Hybrid PDF Intent Matrix and Isolation Qualification`
**Primary collaborator:** ChatGPT

The private runtime candidate is durably synchronized to `origin/main` at:

```text
610fb6c1480012b0db80965239493348e5de5a58
```

The candidate now closes the isolated process-identity and direct-dispatch questions left by Checkpoint 342. It uses a private random runtime instance ID plus a private shutdown token, requires the private identity and public loopback health response to describe the same exact runtime before shutdown, accepts shutdown only on the fixed loopback internal endpoint with both token and instance ID, waits for the old instance to disappear, launches one fixed server-owned worker definition, and requires a new instance ID plus the expected version/surface/tool count before recording success. No arbitrary PID kill path is used.

The direct semantic service persists and arms the operation before detached helper dispatch, returns the armed receipt before the fixed destructive delay, uses a durable active-operation lock, and treats replay of the same `requestId` as the same operation rather than a second restart.

Focused suites and functional probes pass:

```text
RUNTIME_MAINTENANCE_REGRESSION=PASS tests=12
DETACHED_RUNTIME_MAINTENANCE_REGRESSION=PASS tests=7
ONE_SHOT_RUNTIME_MAINTENANCE_REGRESSION=PASS tests=6

one-shot supervisor functional          PASS
direct dispatch functional              PASS
HTTP runtime-maintenance entrypoint      PASS
```

The private preview.18 integration candidate proposes:

```text
version    0.1.1-preview.18-runtime-maintenance
surface    codexless-public-preview-v2
toolCount  62
new tool   codex.runtime_maintenance
```

The new public contract is deliberately narrow: `restart_codexless` and `status`, each keyed only by caller-stable `requestId`. No caller PID, executable, command, path, cwd, environment, URL, tunnel identity, credential, permission-profile, sandbox, or arbitrary host-process control is accepted. The normal restart leaves the tunnel running.

The staged 62-tool surface and preserved document/Git regressions pass, including the complete hybrid-PDF route suite and >192 MiB isolation tests. Production remains unchanged and healthy on preview.17 / 61 tools with the tunnel live/ready.

```text
CHECKPOINT_343=RUNTIME_MAINTENANCE_PREVIEW18_INTEGRATION_QUALIFIED
LIVE_MUTATION=false
NEXT=GUARDED_PREVIEW18_PUBLICATION_PREFLIGHT
```
