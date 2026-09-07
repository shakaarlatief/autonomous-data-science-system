# Validation 120: Preview.21 Semantic Release Live Activation Qualified

**Date:** 2026-09-07
**Status:** PASS / FIRST NORMAL FUTURE UPDATE COMPLETED THROUGH SEMANTIC RELEASE + SEMANTIC RESTART
**Research:** Research 122
**Release:** `preview21-semantic-release-e2e`
**Source head:** `7aa303f4f362f7d4a3ae9b4d492679751c5e892b`
**Scope:** Verify the first production update performed without an ordinary-host installed-source helper: semantic publication followed by semantic restart activation.

## 1. Activation dispatch

After Validation 119 independently proved source publication succeeded and left preview.20 running, one `codex.runtime_maintenance` restart was submitted:

```json
{
  "schemaVersion": "codexless.runtime-maintenance.v1",
  "operationId": "rm_f0b95f86e6421572f37f2da1775316e1",
  "requestId": "r122.live.preview21.activation.20260907.01",
  "action": "restart_codexless",
  "status": "armed",
  "acceptedAtMs": 1788789949817,
  "armedAtMs": 1788789949823,
  "startedAtMs": null,
  "finishedAtMs": null,
  "errorCode": null,
  "recoveryAttempted": false,
  "recoverySucceeded": null,
  "surfaceVersion": "codexless-public-preview-v2"
}
```

The public call returned in 6 ms before destructive work.

## 2. Exact runtime replacement

Pre-activation identity:

```text
version      0.1.1-preview.20-runtime-release
PID          41548
instanceId   ri_c8620c8dc49e8af26a2d0d7480c3cae1
toolCount    63
```

Post-activation identity:

```text
version      0.1.1-preview.21-semantic-release-e2e
PID          56332
instanceId   ri_3ae38f351e0586505e9404d64dad5f24
toolCount    63
surface      codexless-public-preview-v2
```

Both PID and logical instance changed.

## 3. Tunnel preservation

The tunnel listener remained:

```text
PID           67468
start UTC     2026-09-07T11:46:46.9863642Z
same PID      true
/healthz      live
/readyz       ready
```

No tunnel restart occurred.

## 4. Durable restart completion

Status for the exact restart requestId:

```json
{
  "schemaVersion": "codexless.runtime-maintenance.v1",
  "operationId": "rm_f0b95f86e6421572f37f2da1775316e1",
  "requestId": "r122.live.preview21.activation.20260907.01",
  "action": "restart_codexless",
  "status": "succeeded",
  "acceptedAtMs": 1788789949817,
  "armedAtMs": 1788789949823,
  "startedAtMs": 1788789952920,
  "finishedAtMs": 1788789955131,
  "errorCode": null,
  "recoveryAttempted": false,
  "recoverySucceeded": null,
  "surfaceVersion": "codexless-public-preview-v2"
}
```

No recovery path was needed.

## 5. Release-state finalization

After the replacement became healthy:

```text
pending-activation.json absent
active-operation.json   absent
active-release.json     present
active-history          present for rm_cad5ff...
```

Active release identity:

```text
releaseId                 preview21-semantic-release-e2e
sourceHead                7aa303f4f362f7d4a3ae9b4d492679751c5e892b
manifest                  bb00583fd32fc7e512a16b7197b9e4ae9aed41bd1b5649c6015c1af47e20ca60
snapshotOperationId       rm_cad5ff919dff666fef050e98ddda8680
previousActiveOperationId null
previous contract         preview.20 / 63
target contract           preview.21 / 63
activatedAtMs             1788789955123
```

The immutable history record is identical in release identity/contract and anchors later rollback.

## 6. Installed byte verification

Post-activation target SHA-256 values remain:

```text
09d2f19c0b3a86f1a8e11be9b360f455913d1acfb106ce672abb43d33b0d4f4a
a11d663baa88f3df7df5f92faad1c5abca67eb475860fadc5d1e8afc05d91bee
```

The semantic publish operation itself remains durable `succeeded` with no recovery.

## 7. Architectural conclusion

For the forward update path, AB-002's original operational objective is now demonstrated in production:

```text
no user-run installed-source publication helper
no manual Codexless stop/start
no manual tunnel stop/start
no caller path/process/command authority
```

Instead the update uses only fixed private release source, bounded semantic release actions and bounded semantic restart.

The remaining qualification before closing AB-002 should cover public post-activation `verify`/`status` and the explicit semantic rollback path back to preview.20, including source rollback publication, restart activation and final active-release/pending-state semantics.

```text
PREVIEW21_SEMANTIC_FORWARD_UPDATE=PASS
NEXT=POSTACTIVATION_VERIFY_STATUS_AND_ROLLBACK
```
