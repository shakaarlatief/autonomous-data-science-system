# Validation 122: Preview.21 Semantic Rollback Source Published, Activation Pending

**Date:** 2026-09-07
**Status:** PASS / ROLLBACK SNAPSHOT RESTORED TO LIVE INSTALL / ACTIVATION NOT YET PERFORMED
**Research:** Research 122
**Release:** `preview21-semantic-release-e2e`
**Source head:** `7aa303f4f362f7d4a3ae9b4d492679751c5e892b`
**Scope:** Qualify detached semantic rollback publication separately from rollback runtime activation.

## 1. Public rollback dispatch

Exactly one fresh-host rollback call was made:

```json
{
  "schemaVersion": "codexless.runtime-release-operation.v1",
  "operationId": "rm_c966d626b35654606c8278083d00e7ad",
  "requestId": "r122.preview21.rollback.20260907.01",
  "releaseId": "preview21-semantic-release-e2e",
  "expectedSourceHead": "7aa303f4f362f7d4a3ae9b4d492679751c5e892b",
  "action": "rollback_release",
  "status": "armed",
  "acceptedAtMs": 1788790498374,
  "armedAtMs": 1788790498380,
  "startedAtMs": null,
  "finishedAtMs": null,
  "errorCode": null,
  "recoveryAttempted": false,
  "recoverySucceeded": null,
  "surfaceVersion": "codexless-public-preview-v2"
}
```

The public receipt returned 6 ms after acceptance and before destructive rollback work. No follow-up ADS action occurred in that disposable turn.

## 2. Durable detached completion

Independent server-owned ledger inspection later reported:

```text
operationId        rm_c966d626b35654606c8278083d00e7ad
action             rollback_release
status             succeeded
startedAtMs        1788790499211
finishedAtMs       1788790501421
errorCode          null
recoveryAttempted  false
recoverySucceeded  null
active lock        absent
```

Detached rollback therefore completed and released the shared mutation lock.

## 3. Exact source restoration

Direct read-only SHA-256 verification after rollback publication:

```text
src/surface-contracts.mjs
9286d3838d227055f4591a75dbc2c76ef3c107a8fd99168197892c4d9b4db76b

test/public-surface-registration.mjs
b5b5781d71343fea66102fd27a652131b90913191b9f5179839dc81042ec9bb2
```

These are the exact preview.20 expected-current hashes from Validation 117 and the original rollback snapshot from the preview.21 publication.

## 4. Rollback pending state

The durable pending record is:

```text
direction                 rollback
operationId               rm_c966d626b35654606c8278083d00e7ad
releaseId                 preview21-semantic-release-e2e
sourceHead                7aa303f4f362f7d4a3ae9b4d492679751c5e892b
manifest                  bb00583fd32fc7e512a16b7197b9e4ae9aed41bd1b5649c6015c1af47e20ca60
snapshotOperationId       rm_cad5ff919dff666fef050e98ddda8680
previousActiveOperationId null
previous contract         preview.20 / 63
target contract           preview.21 / 63
```

The original active-release record remains preview.21 until activation. This is intentional: source rollback publication alone must not claim runtime rollback success.

## 5. Process/tunnel split boundary

After rollback source publication:

```text
installed source   preview.20 exact bytes
running version    0.1.1-preview.21-semantic-release-e2e
running toolCount  63
PID                56332
instanceId         ri_3ae38f351e0586505e9404d64dad5f24
tunnel             live / ready
```

No Codexless or tunnel restart occurred during rollback publication.

## 6. Authority check

The public rollback receipt exposes no path/install root, PID, executable, command/argv, cwd, environment, credential, tunnel identity, permission profile, sandbox, URL, destination or arbitrary filesystem/process authority.

## 7. Next gate

Invoke one semantic `codex.runtime_maintenance restart_codexless` request. Expected healthy completion:

```text
preview.21 process replaced
preview.20 / 63 starts healthy
same tunnel process remains live/ready
restart durable status = succeeded
pending activation cleared
shared mutation lock cleared
active-release pointer removed
rollback operation remains durable succeeded
restored preview.20 hashes unchanged
```

Because preview.21 is the first managed release and its predecessor was the unmanaged preview.20 bootstrap runtime, successful rollback activation should remove `active-release.json` rather than point to another managed predecessor.

```text
PREVIEW21_SEMANTIC_ROLLBACK_PUBLICATION=PASS
NEXT=ROLLBACK_RESTART_ACTIVATION
```
