# Checkpoint 357: Runtime Release Preview.20 Live Activation Qualified

**Date:** 2026-09-07
**Status:** PASS / SEMANTIC PREVIEW.20 BOOTSTRAP ACTIVATION QUALIFIED / FRESH-HOST RUNTIME_RELEASE DISCOVERY NEXT
**Checkpoint class:** LIVE ACTIVATION QUALIFICATION
**Project stage:** Research 122 runtime self-maintenance and device-independent access
**Scope:** Qualifies the one-time preview.19 -> preview.20 semantic activation using the already-live bounded runtime-maintenance surface after source-only publication.
**Authority:** Research 122 governs the architecture; Validation 115 owns detailed live evidence.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-19`
**Conversation title:** `19 - Hybrid PDF Intent Matrix and Isolation Qualification`
**Primary collaborator:** ChatGPT

Checkpoint 356 preserved the deliberate split boundary: installed source already matched preview.20 while the executing process remained preview.19 / 62 tools.

ChatGPT then invoked the already-live preview.19 semantic maintenance surface exactly once:

```text
action     restart_codexless
requestId  r122.live.preview20.bootstrap.20260907.01
```

The dispatch returned before destructive work:

```text
schemaVersion      codexless.runtime-maintenance.v1
operationId        rm_9c152b017f3ac20fb4c97a1ec9ef1a56
status             armed
acceptedAtMs       1788787891966
armedAtMs          1788787891972
startedAtMs        null
finishedAtMs       null
errorCode          null
recoveryAttempted  false
recoverySucceeded  null
```

Independent post-delay inspection proved the old process was replaced directly by preview.20:

```text
old PID           69280
old instanceId    ri_780a50fef8f801bc0086ab8a40efd990
new PID           41548
new instanceId    ri_c8620c8dc49e8af26a2d0d7480c3cae1
new version        0.1.1-preview.20-runtime-release
new toolCount      63
surface            codexless-public-preview-v2
```

The listener PID equals the new health PID. Both PID and logical instance changed.

The managed tunnel was preserved as the exact same process:

```text
tunnel PID        67468
tunnel same PID   true
tunnel start UTC  2026-09-07T11:46:46.9863642Z
health            live
ready             ready
```

A durable status read for the exact same requestId then returned terminal success:

```text
status             succeeded
startedAtMs        1788787895046
finishedAtMs       1788787897453
errorCode          null
recoveryAttempted  false
recoverySucceeded  null
```

Timing:

```text
accepted -> armed     6 ms
armed -> started      3,074 ms
started -> finished   2,407 ms
accepted -> finished  5,487 ms
```

No recovery path was needed.

This is the first real qualification proving that after an ordinary-host source-only publication, the already-running old Codexless process can use the newly installed bootstrap-compatible supervisor to activate a new Codexless version itself without manual process or tunnel restart.

The current persistent ChatGPT conversation still exposes only its previously projected tool set. This is expected AB-008 host behavior and is not evidence that preview.20 lacks the new 63rd tool. The next gate is developer-plugin refresh plus fresh disposable chat discovery of `codex.runtime_release`, with no release mutation in that discovery turn.

```text
CHECKPOINT_357=RUNTIME_RELEASE_PREVIEW20_LIVE_ACTIVATION_QUALIFIED
LIVE_VERSION=0.1.1-preview.20-runtime-release
LIVE_TOOL_COUNT=63
INSTANCE_REPLACED=true
TUNNEL_PRESERVED=true
DURABLE_STATUS=succeeded
RECOVERY_REQUIRED=false
NEXT=FRESH_HOST_RUNTIME_RELEASE_SCHEMA_DISCOVERY
```
