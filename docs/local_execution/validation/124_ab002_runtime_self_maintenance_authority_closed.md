# Validation 124: AB-002 Runtime Self-Maintenance Authority Closed

**Date:** 2026-09-07
**Status:** PASS / FINAL PUBLIC ROLLBACK READBACK + MACHINE STATE CLOSE AB-002
**Research:** Research 122
**Backlog item:** AB-002
**Release:** `preview21-semantic-release-e2e`
**Private source head:** `7aa303f4f362f7d4a3ae9b4d492679751c5e892b`
**Scope:** Combine the final fresh-host rollback readback with the already-qualified forward/rollback execution chain and independent final machine state to decide AB-002 closure.

## 1. Fresh-host rollback status

The disposable qualification chat read the existing rollback requestId:

```text
action     status
requestId  r122.preview21.rollback.20260907.01
```

Returned result:

```json
{
  "schemaVersion": "codexless.runtime-release-operation.v1",
  "operationId": "rm_c966d626b35654606c8278083d00e7ad",
  "requestId": "r122.preview21.rollback.20260907.01",
  "releaseId": "preview21-semantic-release-e2e",
  "expectedSourceHead": "7aa303f4f362f7d4a3ae9b4d492679751c5e892b",
  "action": "rollback_release",
  "status": "succeeded",
  "acceptedAtMs": 1788790498374,
  "armedAtMs": 1788790498380,
  "startedAtMs": 1788790499211,
  "finishedAtMs": 1788790501421,
  "errorCode": null,
  "recoveryAttempted": false,
  "recoverySucceeded": null,
  "surfaceVersion": "codexless-public-preview-v2"
}
```

This exactly matches the independent durable rollback ledger inspected in Validation 122.

## 2. Fresh-host post-rollback verify

The second and final read used:

```text
action     verify
requestId  r122.preview21.verify.postrollback.20260907.01
```

Returned result:

```json
{
  "schemaVersion": "codexless.runtime-release.v1",
  "releaseId": "preview21-semantic-release-e2e",
  "requestId": "r122.preview21.verify.postrollback.20260907.01",
  "expectedSourceHead": "7aa303f4f362f7d4a3ae9b4d492679751c5e892b",
  "action": "verify",
  "status": "verification_failed",
  "targetVersion": "0.1.1-preview.21-semantic-release-e2e",
  "targetSurfaceVersion": "codexless-public-preview-v2",
  "targetToolCount": 63,
  "fileCount": 2,
  "manifestSha256": "bb00583fd32fc7e512a16b7197b9e4ae9aed41bd1b5649c6015c1af47e20ca60",
  "mismatchCount": 2,
  "surfaceVersion": "codexless-public-preview-v2",
  "is_error": true
}
```

This was the preregistered healthy post-rollback result. The prepared release still describes two preview.21 target files while the live install has returned to preview.20. Therefore the verifier must report exactly two mismatches. `is_error=true` is the expected tool-result representation of that mismatch state and is not a rollback failure.

## 3. Public authority surface remained narrow

Neither final read exposed:

```text
filesystem path / install root
PID / arbitrary process selector
executable / command / argv
cwd / environment
credential / tunnel identity
permission profile / sandbox
URL / destination
arbitrary host-process or filesystem authority
```

No mutation was invoked after these reads.

## 4. Independent final machine state

Project-side read-only inspection afterward confirmed:

```text
version                    0.1.1-preview.20-runtime-release
toolCount                  63
surface                     codexless-public-preview-v2
PID                        10280
instanceId                 ri_39018a407e14b5fb789134bab0d1f398
surface-contracts SHA-256  9286d3838d227055f4591a75dbc2c76ef3c107a8fd99168197892c4d9b4db76b
registration SHA-256       b5b5781d71343fea66102fd27a652131b90913191b9f5179839dc81042ec9bb2
pending activation         absent
active-release pointer     absent
shared mutation lock       absent
rollback operation         succeeded
tunnel health              live
tunnel readiness           ready
private HEAD               7aa303f4f362f7d4a3ae9b4d492679751c5e892b
private upstream           7aa303f4f362f7d4a3ae9b4d492679751c5e892b
private tracked status     clean
```

## 5. Closure matrix

The evidence chain now covers every accepted AB-002 capability:

```text
Validation 111  semantic Codexless-only restart and idempotent replay
Validation 112  production-shaped semantic release/rollback candidate and recovery design
Validation 116  fresh-host strict runtime-release schema
Validation 117  genuine committed next-version bundle
Validation 118  prepare + real pre-publication installed-byte verifier
Validation 119  semantic installed-source publication
Validation 120  semantic forward activation and active-release finalization
Validation 121  public forward status + zero-mismatch verify
Validation 122  semantic rollback source restoration
Validation 123  semantic rollback activation and managed-state finalization
Validation 124  public rollback status + expected two-mismatch verify + final machine state
```

The one-time preview.18/19/20 bootstrap helpers remain historical migration evidence. They are not needed for an ordinary future release of the accepted architecture, as demonstrated by preview.21.

## 6. Acceptance decision

AB-002 required tightly bounded publication/recovery of the installed Codexless runtime without turning `%LOCALAPPDATA%` into an ordinary workspace and without general process authority. The accepted implementation now satisfies that exact objective through two semantic surfaces:

```text
codex.runtime_release
    prepare | publish | verify | rollback | status

codex.runtime_maintenance
    restart_codexless | status
```

Caller input remains semantic and bounded. Installation paths, process ownership, regression execution, snapshots, publication destination, lifecycle launch, tunnel handling and recovery logic remain server-owned. Production qualification demonstrates forward update and explicit rollback end to end.

Decision:

```text
AB002_RUNTIME_SELF_MAINTENANCE_AUTHORITY=CLOSED
REOPEN_ON_MATERIAL_NEW_TOPOLOGY_OR_REPRODUCED_FAILURE=true
RESEARCH122_CONTINUES_FOR_DEVICE_ACCESS=true
```
