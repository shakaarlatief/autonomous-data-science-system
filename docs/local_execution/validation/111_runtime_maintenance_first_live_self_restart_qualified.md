# Validation 111: Runtime Maintenance First Live Self-Restart Qualified

**Date:** 2026-09-07
**Status:** PASS / PRODUCTION CODEXLESS-ONLY SELF-RESTART QUALIFIED
**Research:** Research 122
**Scope:** Verify the first real production restart through the bounded semantic lifecycle surface, including pre-destructive acknowledgement, exact process replacement, tunnel preservation, durable status recovery, and duplicate suppression.

## 1. Live dispatch

Exactly one fresh-host tool call was made:

```text
action     restart_codexless
requestId  r122.live.preview19.restart.20260907.01
```

No `status`, `command_exec`, retry, manual repair, or other ADS call was made in that dispatch turn.

The call returned successfully with:

```json
{
  "schemaVersion": "codexless.runtime-maintenance.v1",
  "operationId": "rm_acbd2b48836b13daf8ec97225d2d3c4d",
  "requestId": "r122.live.preview19.restart.20260907.01",
  "action": "restart_codexless",
  "status": "armed",
  "acceptedAtMs": 1788782488004,
  "armedAtMs": 1788782488012,
  "startedAtMs": null,
  "finishedAtMs": null,
  "errorCode": null,
  "recoveryAttempted": false,
  "recoverySucceeded": null,
  "surfaceVersion": "codexless-public-preview-v2"
}
```

This directly qualifies the required acknowledgement boundary: the operation was durably accepted and armed before the detached helper began destructive work.

## 2. Independent replacement verification

The pre-qualified live instance from Validation 109 was:

```text
PID         8564
instanceId  ri_e052fa7c74b0e00929277d8245c1bea6
```

A separate read-only ADS inspection after the restart observed:

```text
Version             0.1.1-preview.19-runtime-maintenance-schema
ToolCount           62
Surface             codexless-public-preview-v2
HealthPid           69280
ListenerPid         69280
IdentityPid         69280
HealthInstanceId    ri_780a50fef8f801bc0086ab8a40efd990
IdentityInstanceId  ri_780a50fef8f801bc0086ab8a40efd990
PidChanged          true
InstanceChanged     true
TunnelHealth        live
TunnelReady         ready
```

The replacement therefore satisfies both process and logical instance replacement, while keeping the expected version/tool surface.

## 3. Tunnel-preservation evidence

The operation was accepted at:

```text
2026-09-07T12:01:28.004Z
```

After restart, process start evidence showed:

```text
Codexless PID        69280
Codexless start UTC  2026-09-07T12:01:31.3907217Z
Codexless started after accepted  true

Tunnel PID           67468
Tunnel start UTC     2026-09-07T11:46:46.9863642Z
Tunnel started before accepted    true
Tunnel still listening            true
```

Together with post-restart `/healthz=live` and `/readyz=ready`, this establishes that the same already-running tunnel process survived the Codexless restart.

## 4. Durable terminal status

After independent health verification, one bounded status call with the exact same requestId returned:

```json
{
  "schemaVersion": "codexless.runtime-maintenance.v1",
  "operationId": "rm_acbd2b48836b13daf8ec97225d2d3c4d",
  "requestId": "r122.live.preview19.restart.20260907.01",
  "action": "restart_codexless",
  "status": "succeeded",
  "acceptedAtMs": 1788782488004,
  "armedAtMs": 1788782488012,
  "startedAtMs": 1788782491090,
  "finishedAtMs": 1788782493810,
  "errorCode": null,
  "recoveryAttempted": false,
  "recoverySucceeded": null,
  "surfaceVersion": "codexless-public-preview-v2"
}
```

Timing:

```text
accepted -> armed   8 ms
armed -> started    3,078 ms
started -> finished 2,720 ms
accepted -> finished 5,806 ms
```

No recovery path was needed.

## 5. Explicit idempotency replay

Only after terminal success was established, the exact same restart action and requestId were submitted again as a deliberate duplicate-suppression qualification. The result returned the same operationId, accepted/armed/started/finished timestamps and terminal `succeeded` state.

After waiting four seconds, which exceeds the fixed destructive delay, independent health remained:

```text
PID                 69280
instanceId          ri_780a50fef8f801bc0086ab8a40efd990
SameReplacementPid  true
SameReplacementInstance true
version             0.1.1-preview.19-runtime-maintenance-schema
toolCount           62
tunnel              live / ready
```

Therefore replay did not dispatch a second restart.

## 6. Qualified claim

The live accepted contract is now:

```text
ChatGPT fresh host
    -> bounded restart_codexless(requestId)
    -> armed receipt before destructive work
    -> detached helper replaces exact bound Codexless instance
    -> managed tunnel remains running
    -> replacement preview.19 / 62 tools becomes healthy
    -> durable status(requestId) returns succeeded
    -> duplicate restart with same requestId returns same operation
    -> no second restart occurs
```

This qualifies ordinary Codexless-only self-restart. It does not yet qualify semantic publication/verify/rollback into the installed runtime tree, nor does it make tunnel restart unnecessary for tunnel/profile/credential changes.

```text
FIRST_LIVE_SELF_RESTART=PASS
DURABLE_STATUS=PASS
TUNNEL_PRESERVATION=PASS
IDEMPOTENT_REPLAY=PASS
```
