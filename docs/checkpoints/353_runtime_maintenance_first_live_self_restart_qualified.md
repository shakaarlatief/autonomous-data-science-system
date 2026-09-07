# Checkpoint 353: Runtime Maintenance First Live Self-Restart Qualified

**Date:** 2026-09-07
**Status:** PASS / FIRST PRODUCTION SELF-RESTART + DURABLE STATUS + IDEMPOTENT REPLAY QUALIFIED
**Checkpoint class:** LIVE LIFECYCLE QUALIFICATION
**Project stage:** Research 122 runtime self-maintenance and device-independent access
**Scope:** Qualifies the first production `codex.runtime_maintenance` restart on active preview.19, exact replacement-instance recovery, tunnel preservation, durable terminal status, and same-request idempotent replay without a second restart.
**Authority:** Research 122 governs the architecture; Validation 111 owns the detailed live evidence.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-19`
**Conversation title:** `19 - Hybrid PDF Intent Matrix and Isolation Qualification`
**Primary collaborator:** ChatGPT

A refreshed fresh ChatGPT conversation invoked exactly one live restart with stable request ID:

```text
r122.live.preview19.restart.20260907.01
```

The dispatch returned successfully before destructive work and reported:

```text
schemaVersion      codexless.runtime-maintenance.v1
operationId        rm_acbd2b48836b13daf8ec97225d2d3c4d
action             restart_codexless
status             armed
acceptedAtMs       1788782488004
armedAtMs          1788782488012
startedAtMs        null
finishedAtMs       null
errorCode          null
recoveryAttempted  false
recoverySucceeded  null
```

Independent post-dispatch inspection then proved the old preview.19 process was replaced:

```text
old PID            8564
new PID            69280
old instanceId     ri_e052fa7c74b0e00929277d8245c1bea6
new instanceId     ri_780a50fef8f801bc0086ab8a40efd990
version            0.1.1-preview.19-runtime-maintenance-schema
toolCount          62
surface            codexless-public-preview-v2
```

The new listener PID, private runtime identity PID and public health PID all match. The managed tunnel remained healthy and ready. Its current listener process started before the maintenance operation and remained the listener after Codexless replacement, establishing that the ordinary Codexless restart path did not restart the tunnel.

A subsequent `status` call using the exact same requestId returned the same operation with terminal `succeeded`:

```text
startedAtMs        1788782491090
finishedAtMs       1788782493810
errorCode          null
recoveryAttempted  false
recoverySucceeded  null
```

The accepted-to-armed interval was 8 ms, armed-to-start delay was 3,078 ms, and the helper completed the replacement approximately 2,720 ms after starting.

An explicit idempotency replay then called `restart_codexless` again with the exact same requestId only after terminal success had been established. It returned the exact same operationId and terminal timestamps. After waiting beyond the destructive delay, the replacement PID and instanceId remained unchanged, proving no second restart was launched.

```text
CHECKPOINT_353=RUNTIME_MAINTENANCE_FIRST_LIVE_SELF_RESTART_QUALIFIED
DISPATCH_ARMED_BEFORE_DESTRUCTIVE_WORK=true
DURABLE_STATUS=succeeded
INSTANCE_REPLACED=true
TUNNEL_PRESERVED=true
IDEMPOTENT_REPLAY_NO_SECOND_RESTART=true
```
