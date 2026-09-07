# Validation 119: Preview.21 Semantic Release Source Published, Activation Pending

**Date:** 2026-09-07
**Status:** PASS / FIRST SEMANTIC INSTALLED-SOURCE PUBLICATION QUALIFIED
**Research:** Research 122
**Release:** `preview21-semantic-release-e2e`
**Source head:** `7aa303f4f362f7d4a3ae9b4d492679751c5e892b`
**Scope:** Qualify the first detached `codex.runtime_release publish` against the real installed Codexless tree before runtime activation.

## 1. Public dispatch receipt

Exactly one publish call was made in the refreshed disposable chat. Initial result:

```json
{
  "schemaVersion": "codexless.runtime-release-operation.v1",
  "operationId": "rm_cad5ff919dff666fef050e98ddda8680",
  "requestId": "r122.preview21.publish.20260907.01",
  "releaseId": "preview21-semantic-release-e2e",
  "expectedSourceHead": "7aa303f4f362f7d4a3ae9b4d492679751c5e892b",
  "action": "publish_release",
  "status": "armed",
  "acceptedAtMs": 1788789572617,
  "armedAtMs": 1788789572625,
  "startedAtMs": null,
  "finishedAtMs": null,
  "errorCode": null,
  "recoveryAttempted": false,
  "recoverySucceeded": null,
  "surfaceVersion": "codexless-public-preview-v2"
}
```

The call returned 8 ms after acceptance and before detached publication began. No follow-up ADS call occurred in that qualification turn.

## 2. Durable operation completion

Independent read-only inspection of the server-owned release ledger later found:

```text
operationId        rm_cad5ff919dff666fef050e98ddda8680
status             succeeded
startedAtMs        1788789573452
finishedAtMs       1788789577231
errorCode          null
recoveryAttempted  false
recoverySucceeded  null
shared active lock absent
```

This proves the detached publisher completed and released the shared runtime mutation lock.

## 3. Pending activation contract

The server-owned pending record exists and binds exactly:

```text
direction           forward
releaseId           preview21-semantic-release-e2e
sourceHead          7aa303f4f362f7d4a3ae9b4d492679751c5e892b
manifest            bb00583fd32fc7e512a16b7197b9e4ae9aed41bd1b5649c6015c1af47e20ca60
snapshotOperation   rm_cad5ff919dff666fef050e98ddda8680
previous active     null
previous contract   preview.20 / public-preview-v2 / 63
target contract     preview.21-semantic-release-e2e / public-preview-v2 / 63
```

The snapshot operation ID equals the publication operation ID, as designed.

## 4. Installed target verification

Direct SHA-256 reads of the two installed targets now equal the qualified release target hashes:

```text
src/surface-contracts.mjs
09d2f19c0b3a86f1a8e11be9b360f455913d1acfb106ce672abb43d33b0d4f4a

test/public-surface-registration.mjs
a11d663baa88f3df7df5f92faad1c5abca67eb475860fadc5d1e8afc05d91bee
```

Therefore semantic publication changed the real installed tree exactly as specified.

## 5. Process and tunnel remain old/live

Read-only health after publication:

```text
version       0.1.1-preview.20-runtime-release
toolCount     63
PID           41548
instanceId    ri_c8620c8dc49e8af26a2d0d7480c3cae1
tunnel health live
tunnel ready  ready
```

Publication itself did not restart Codexless or the tunnel.

## 6. Authority boundary

The public publish receipt exposed no path/install root, PID, executable, command/argv, cwd, environment, credential, tunnel identity, permission profile, sandbox, URL, destination or arbitrary filesystem/process authority.

This is the first production proof that installed Codexless source can be updated through the semantic release surface itself, without asking the user to run the previous `%LOCALAPPDATA%` publication helper.

## 7. Next gate

Activation remains a separate semantic mutation. Invoke `codex.runtime_maintenance restart_codexless` exactly once with a new stable requestId. After it returns `armed`, independently verify preview.21 health, exact process replacement, same tunnel PID, durable restart status, cleared pending activation and active-release record before any further release mutation.

```text
PREVIEW21_SEMANTIC_PUBLISH=PASS
LIVE_SOURCE=PREVIEW21
LIVE_PROCESS=PREVIEW20
NEXT=SEMANTIC_ACTIVATION
```
