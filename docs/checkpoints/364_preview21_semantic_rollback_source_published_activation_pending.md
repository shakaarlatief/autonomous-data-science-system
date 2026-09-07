# Checkpoint 364: Preview.21 Semantic Rollback Source Published, Activation Pending

**Date:** 2026-09-07
**Status:** PASS / SEMANTIC ROLLBACK SOURCE RESTORE SUCCEEDED / ROLLBACK ACTIVATION NEXT
**Checkpoint class:** LIVE SEMANTIC ROLLBACK PUBLICATION BOUNDARY
**Project stage:** Research 122 runtime self-maintenance and device-independent access
**Scope:** Preserves the first production rollback-source mutation performed through `codex.runtime_release`, independently verifies restored preview.20 source bytes, durable rollback state, and the still-running preview.21 process before rollback activation.
**Authority:** Research 122 governs the architecture; Validation 122 owns detailed live evidence.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-19`
**Conversation title:** `19 - Hybrid PDF Intent Matrix and Isolation Qualification`
**Primary collaborator:** ChatGPT

A refreshed disposable ChatGPT conversation made exactly one rollback mutation:

```text
action              rollback
releaseId           preview21-semantic-release-e2e
requestId           r122.preview21.rollback.20260907.01
expectedSourceHead  7aa303f4f362f7d4a3ae9b4d492679751c5e892b
```

The public call returned before detached rollback work began:

```text
schemaVersion      codexless.runtime-release-operation.v1
operationId        rm_c966d626b35654606c8278083d00e7ad
action             rollback_release
status             armed
acceptedAtMs       1788790498374
armedAtMs          1788790498380
startedAtMs        null
finishedAtMs       null
errorCode          null
recoveryAttempted  false
recoverySucceeded  null
```

Accepted-to-armed latency was 6 ms. The receipt exposed no unexpected path/install-root, PID, executable, command/argv, cwd, environment, credential, tunnel identity, permission profile, sandbox, URL, destination or arbitrary host/process/filesystem authority. The disposable chat then stopped exactly as instructed.

Independent project-side inspection after detached rollback publication completed found:

```text
operationId        rm_c966d626b35654606c8278083d00e7ad
action             rollback_release
status             succeeded
startedAtMs        1788790499211
finishedAtMs       1788790501421
errorCode          null
recoveryAttempted  false
recoverySucceeded  null
shared active lock absent
```

Timing:

```text
accepted -> armed      6 ms
armed -> started       831 ms
started -> finished    2,210 ms
accepted -> finished   3,047 ms
```

The rollback publisher restored the exact preview.20 installed hashes:

```text
src/surface-contracts.mjs
9286d3838d227055f4591a75dbc2c76ef3c107a8fd99168197892c4d9b4db76b

test/public-surface-registration.mjs
b5b5781d71343fea66102fd27a652131b90913191b9f5179839dc81042ec9bb2
```

The running process deliberately remains preview.21 until rollback activation:

```text
version      0.1.1-preview.21-semantic-release-e2e
toolCount    63
PID          56332
instanceId   ri_3ae38f351e0586505e9404d64dad5f24
tunnel       live / ready
```

The active managed-release record still points to preview.21, as required until rollback activation succeeds. A rollback-direction pending activation now binds:

```text
direction                 rollback
operationId               rm_c966d626b35654606c8278083d00e7ad
releaseId                 preview21-semantic-release-e2e
snapshotOperationId       rm_cad5ff919dff666fef050e98ddda8680
previousActiveOperationId null
previous contract         preview.20 / public-preview-v2 / 63
target contract           preview.21 / public-preview-v2 / 63
```

This is the exact inverse source-published / activation-pending split of Checkpoint 361. It proves semantic rollback can restore the previous installed source snapshot without stopping the active runtime or tunnel.

The next operation is one bounded `codex.runtime_maintenance restart_codexless` call with a new stable requestId. The release-aware supervisor should interpret the rollback pending state, stop preview.21, start preview.20 / 63 from the restored bytes, verify exact previous contract health, clear pending activation, remove the active managed-release pointer because this rollback returns to the unmanaged preview.20 bootstrap predecessor, and preserve the tunnel.

```text
CHECKPOINT_364=PREVIEW21_SEMANTIC_ROLLBACK_SOURCE_PUBLISHED_ACTIVATION_PENDING
ROLLBACK_PUBLICATION=PASS
RESTORED_SOURCE=PREVIEW20_EXACT
RUNNING_PROCESS=PREVIEW21
PENDING_ACTIVATION=rollback
NEXT=SEMANTIC_ROLLBACK_ACTIVATION
```
