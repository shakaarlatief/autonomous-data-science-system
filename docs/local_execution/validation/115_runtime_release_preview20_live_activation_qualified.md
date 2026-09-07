# Validation 115: Runtime Release Preview.20 Live Activation Qualified

**Date:** 2026-09-07
**Status:** PASS / OLD-PROCESS TO NEW-SOURCE SEMANTIC ACTIVATION QUALIFIED
**Research:** Research 122
**Scope:** Verify the first production activation of newly published preview.20 source through the already-live preview.19 `codex.runtime_maintenance` tool, including armed-before-destructive-work acknowledgement, exact process replacement, 63-tool target contract, tunnel preservation and durable terminal status.

## 1. Pre-activation boundary

Immediately before activation:

```text
installed source   preview.20 exact candidate bytes
running version    0.1.1-preview.19-runtime-maintenance-schema
running toolCount  62
PID                69280
instanceId         ri_780a50fef8f801bc0086ab8a40efd990
tunnel PID         67468
tunnel             live / ready
```

This was independently preserved in Validation 114.

## 2. One semantic restart dispatch

Exactly one restart mutation was submitted:

```text
action     restart_codexless
requestId  r122.live.preview20.bootstrap.20260907.01
```

Receipt:

```json
{
  "schemaVersion": "codexless.runtime-maintenance.v1",
  "operationId": "rm_9c152b017f3ac20fb4c97a1ec9ef1a56",
  "requestId": "r122.live.preview20.bootstrap.20260907.01",
  "action": "restart_codexless",
  "status": "armed",
  "acceptedAtMs": 1788787891966,
  "armedAtMs": 1788787891972,
  "startedAtMs": null,
  "finishedAtMs": null,
  "errorCode": null,
  "recoveryAttempted": false,
  "recoverySucceeded": null,
  "surfaceVersion": "codexless-public-preview-v2"
}
```

The 6 ms accepted-to-armed interval again establishes that the public call returned before destructive work.

## 3. Independent replacement verification

Five seconds after dispatch, direct local health/listener inspection observed:

```text
Version          0.1.1-preview.20-runtime-release
ToolCount        63
Surface          codexless-public-preview-v2
Pid              41548
InstanceId       ri_c8620c8dc49e8af26a2d0d7480c3cae1
ListenerPid      41548
OldPid           69280
OldInstanceId    ri_780a50fef8f801bc0086ab8a40efd990
PidChanged       true
InstanceChanged  true
```

The bootstrap compatibility logic therefore consumed the newly installed preview.20 surface contract rather than stale preview.19 expected version/tool-count values.

## 4. Tunnel preservation

The managed tunnel remained the same already-running process:

```text
TunnelPid        67468
TunnelSamePid    true
TunnelStartUtc   2026-09-07T11:46:46.9863642Z
TunnelHealth     live
TunnelReady      ready
```

No tunnel restart was required.

## 5. Durable terminal status

The exact same requestId was read through the bounded status action after the replacement became healthy.

Result:

```json
{
  "schemaVersion": "codexless.runtime-maintenance.v1",
  "operationId": "rm_9c152b017f3ac20fb4c97a1ec9ef1a56",
  "requestId": "r122.live.preview20.bootstrap.20260907.01",
  "action": "restart_codexless",
  "status": "succeeded",
  "acceptedAtMs": 1788787891966,
  "armedAtMs": 1788787891972,
  "startedAtMs": 1788787895046,
  "finishedAtMs": 1788787897453,
  "errorCode": null,
  "recoveryAttempted": false,
  "recoverySucceeded": null,
  "surfaceVersion": "codexless-public-preview-v2"
}
```

Timing:

```text
accepted -> armed     6 ms
armed -> started      3,074 ms
started -> finished   2,407 ms
accepted -> finished  5,487 ms
```

No recovery path was required.

## 6. Qualified architectural claim

The following real production path is now established:

```text
qualified source-only publication
    -> old preview.19 process remains live
    -> old process accepts bounded semantic restart
    -> newly installed supervisor derives preview.20 bootstrap contract
    -> exact old instance gracefully stops
    -> preview.20 / 63 replacement starts healthy
    -> same tunnel remains live/ready
    -> durable restart status returns succeeded
```

This removes the manual Codexless/tunnel stop-start step from future source-activation work, provided the new installed supervisor remains backward-compatible with the currently executing version during each upgrade seam.

## 7. Host projection boundary

The current persistent ChatGPT conversation was created before preview.20 became live and therefore should not be used to qualify discovery of the new `codex.runtime_release` tool. AB-008 already establishes that tool projections can remain stale within an existing conversation after a server-side surface change.

The next qualification must use a refreshed developer Plugin and a completely fresh disposable ChatGPT conversation. That turn should discover and report the exact projected `codex.runtime_release` schema without invoking it.

```text
PREVIEW20_SEMANTIC_ACTIVATION=PASS
LIVE_VERSION=0.1.1-preview.20-runtime-release
LIVE_TOOL_COUNT=63
TUNNEL_PRESERVATION=PASS
DURABLE_STATUS=PASS
NEXT=FRESH_CHAT_RUNTIME_RELEASE_SCHEMA
```
