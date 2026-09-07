# Validation 121: Preview.21 Post-Activation Status/Verify Qualified

**Date:** 2026-09-07
**Status:** PASS / PUBLIC READBACK CONFIRMS DURABLE PUBLISH + EXACT ACTIVE INSTALL
**Research:** Research 122
**Release:** `preview21-semantic-release-e2e`
**Source head:** `7aa303f4f362f7d4a3ae9b4d492679751c5e892b`
**Scope:** Qualify host-visible status of the existing publish operation and host-visible verification of the active preview.21 install before rollback.

## 1. Existing publish operation status

Fresh-host call:

```text
action     status
requestId  r122.preview21.publish.20260907.01
```

Returned result:

```json
{
  "schemaVersion": "codexless.runtime-release-operation.v1",
  "operationId": "rm_cad5ff919dff666fef050e98ddda8680",
  "requestId": "r122.preview21.publish.20260907.01",
  "releaseId": "preview21-semantic-release-e2e",
  "expectedSourceHead": "7aa303f4f362f7d4a3ae9b4d492679751c5e892b",
  "action": "publish_release",
  "status": "succeeded",
  "acceptedAtMs": 1788789572617,
  "armedAtMs": 1788789572625,
  "startedAtMs": 1788789573452,
  "finishedAtMs": 1788789577231,
  "errorCode": null,
  "recoveryAttempted": false,
  "recoverySucceeded": null,
  "surfaceVersion": "codexless-public-preview-v2"
}
```

This matches the independently inspected durable ledger from Validation 119.

## 2. Post-activation verify

Fresh-host call:

```text
action     verify
requestId  r122.preview21.verify.postactivation.20260907.01
```

Returned result:

```json
{
  "schemaVersion": "codexless.runtime-release.v1",
  "releaseId": "preview21-semantic-release-e2e",
  "requestId": "r122.preview21.verify.postactivation.20260907.01",
  "expectedSourceHead": "7aa303f4f362f7d4a3ae9b4d492679751c5e892b",
  "action": "verify",
  "status": "verified",
  "targetVersion": "0.1.1-preview.21-semantic-release-e2e",
  "targetSurfaceVersion": "codexless-public-preview-v2",
  "targetToolCount": 63,
  "fileCount": 2,
  "manifestSha256": "bb00583fd32fc7e512a16b7197b9e4ae9aed41bd1b5649c6015c1af47e20ca60",
  "mismatchCount": 0,
  "surfaceVersion": "codexless-public-preview-v2"
}
```

This is the exact inverse of Validation 118's pre-publication verification: before publish the verifier observed two mismatches; after semantic publication and activation it observes zero.

## 3. Receipt authority check

Neither public receipt exposed unexpected path/install root, PID, executable, command/argv, cwd, environment, credential, tunnel identity, permission profile, sandbox, URL, destination or arbitrary filesystem/process authority.

## 4. Independent live-state cross-check

Project-side read-only inspection after both public reads found:

```text
version                    0.1.1-preview.21-semantic-release-e2e
toolCount                  63
PID                        56332
instanceId                 ri_3ae38f351e0586505e9404d64dad5f24
surface-contracts SHA-256  09d2f19c0b3a86f1a8e11be9b360f455913d1acfb106ce672abb43d33b0d4f4a
registration SHA-256       a11d663baa88f3df7df5f92faad1c5abca67eb475860fadc5d1e8afc05d91bee
pending activation         absent
shared active lock         absent
active release             preview21-semantic-release-e2e
tunnel                     live / ready
```

No state changed during the two public reads.

## 5. Rollback gate

The active release now satisfies all prerequisites enforced by the semantic rollback path:

```text
prepared release binding exists
active release identity matches releaseId/source head
running contract matches active target contract
no pending activation
no shared mutation lock
snapshot/history available from the original publish operation
```

The next test is exactly one `rollback` mutation call with a new stable requestId. It must not be combined with restart. Expected initial state is `armed`. After the detached rollback publisher finishes, independent verification should show preview.20 source hashes restored while the preview.21 process remains alive, with a rollback-direction pending activation waiting for semantic restart.

```text
PREVIEW21_POSTACTIVATION_STATUS_VERIFY=PASS
NEXT=ROLLBACK_PUBLICATION_ONLY
```
