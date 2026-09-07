# Validation 123: Preview.21 Semantic Rollback Live Activation Qualified

**Date:** 2026-09-07
**Status:** PASS / EXPLICIT SEMANTIC ROLLBACK ACTIVATED PREVIEW.20 SUCCESSFULLY
**Research:** Research 122
**Release:** `preview21-semantic-release-e2e`
**Scope:** Verify the first full rollback activation after semantic rollback source publication.

## 1. Restart dispatch

After Validation 122 established preview.20 source restored while preview.21 remained active, one bounded maintenance restart was submitted:

```json
{
  "schemaVersion": "codexless.runtime-maintenance.v1",
  "operationId": "rm_ca482535bb5e44d82586298b04a39c3d",
  "requestId": "r122.live.preview21.rollback.activation.20260907.01",
  "action": "restart_codexless",
  "status": "armed",
  "acceptedAtMs": 1788790744948,
  "armedAtMs": 1788790744953,
  "startedAtMs": null,
  "finishedAtMs": null,
  "errorCode": null,
  "recoveryAttempted": false,
  "recoverySucceeded": null,
  "surfaceVersion": "codexless-public-preview-v2"
}
```

The call returned 5 ms after acceptance and before destructive work.

## 2. Exact runtime rollback

Before restart:

```text
version      0.1.1-preview.21-semantic-release-e2e
PID          56332
instanceId   ri_3ae38f351e0586505e9404d64dad5f24
toolCount    63
```

After restart:

```text
version      0.1.1-preview.20-runtime-release
PID          10280
instanceId   ri_39018a407e14b5fb789134bab0d1f398
toolCount    63
surface      codexless-public-preview-v2
```

PID and logical instance both changed.

## 3. Installed source remains rolled back

Post-restart SHA-256 values:

```text
src/surface-contracts.mjs
9286d3838d227055f4591a75dbc2c76ef3c107a8fd99168197892c4d9b4db76b

test/public-surface-registration.mjs
b5b5781d71343fea66102fd27a652131b90913191b9f5179839dc81042ec9bb2
```

These remain the exact preview.20 baseline hashes.

## 4. Tunnel preservation

The tunnel remained:

```text
PID           67468
start UTC     2026-09-07T11:46:46.9863642Z
same PID      true
/healthz      live
/readyz       ready
```

No tunnel restart occurred.

## 5. Durable restart completion

Status for `r122.live.preview21.rollback.activation.20260907.01`:

```json
{
  "schemaVersion": "codexless.runtime-maintenance.v1",
  "operationId": "rm_ca482535bb5e44d82586298b04a39c3d",
  "requestId": "r122.live.preview21.rollback.activation.20260907.01",
  "action": "restart_codexless",
  "status": "succeeded",
  "acceptedAtMs": 1788790744948,
  "armedAtMs": 1788790744953,
  "startedAtMs": 1788790748052,
  "finishedAtMs": 1788790750459,
  "errorCode": null,
  "recoveryAttempted": false,
  "recoverySucceeded": null,
  "surfaceVersion": "codexless-public-preview-v2"
}
```

No recovery path was needed.

## 6. Managed release state finalization

After successful rollback activation:

```text
pending-activation.json absent
active-operation.json   absent
active-release.json     absent
rollback operation      durable succeeded
```

Removing the active-release pointer is correct because the rollback predecessor is preview.20, which predates the managed release chain. The immutable activation-history record of the prior preview.21 release remains available as historical evidence while no release is currently active.

## 7. Architectural conclusion

Both forward and explicit rollback runtime transitions are now production-qualified using only narrow semantic surfaces:

```text
forward:
private release -> prepare -> verify -> publish -> restart -> verify

rollback:
active release -> rollback publish -> restart -> previous runtime
```

Neither path required caller-selected install paths/processes/commands, a user-run `%LOCALAPPDATA%` publication helper, or manual Codexless/tunnel restart.

One final read-only host qualification remains useful before AB-002 closure: public `status` for the rollback requestId should return `rollback_release / succeeded`, and `verify` for the preview.21 release should now return `verification_failed` with exactly two mismatches because preview.20 source is active again.

```text
PREVIEW21_SEMANTIC_ROLLBACK_ACTIVATION=PASS
NEXT=FINAL_PUBLIC_ROLLBACK_READBACK
```
