# Checkpoint 361: Preview.21 Semantic Release Source Published, Activation Pending

**Date:** 2026-09-07
**Status:** PASS / FIRST LIVE SEMANTIC SOURCE PUBLICATION SUCCEEDED / ACTIVATION PENDING
**Checkpoint class:** LIVE SEMANTIC PUBLICATION BOUNDARY
**Project stage:** Research 122 runtime self-maintenance and device-independent access
**Scope:** Preserves the first production source mutation performed entirely through `codex.runtime_release`, independently verifies installed target hashes and durable release state, and freezes the old-process/new-source boundary before restart activation.
**Authority:** Research 122 governs the architecture; Validation 119 owns detailed live evidence.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-19`
**Conversation title:** `19 - Hybrid PDF Intent Matrix and Isolation Qualification`
**Primary collaborator:** ChatGPT

A refreshed disposable ChatGPT conversation made exactly one mutation call:

```text
action              publish
releaseId           preview21-semantic-release-e2e
requestId           r122.preview21.publish.20260907.01
expectedSourceHead  7aa303f4f362f7d4a3ae9b4d492679751c5e892b
```

The public tool returned before destructive work with:

```text
schemaVersion      codexless.runtime-release-operation.v1
operationId        rm_cad5ff919dff666fef050e98ddda8680
action             publish_release
status             armed
acceptedAtMs       1788789572617
armedAtMs          1788789572625
startedAtMs        null
finishedAtMs       null
errorCode          null
recoveryAttempted  false
recoverySucceeded  null
```

Accepted-to-armed latency was 8 ms. The receipt exposed no unexpected path/install-root, PID, executable, command/argv, cwd, environment, credential, tunnel identity, permission profile, sandbox, URL, destination or arbitrary host-process/filesystem authority. No second ADS call was made in that disposable qualification turn.

Independent project-side inspection after the detached publisher completed found the durable operation at terminal success:

```text
status             succeeded
startedAtMs        1788789573452
finishedAtMs       1788789577231
errorCode          null
recoveryAttempted  false
recoverySucceeded  null
active lock        absent
```

Timing:

```text
accepted -> armed      8 ms
armed -> started       827 ms
started -> finished    3,779 ms
accepted -> finished   4,614 ms
```

The release publisher created the expected forward pending-activation record:

```text
direction                 forward
operationId               rm_cad5ff919dff666fef050e98ddda8680
releaseId                 preview21-semantic-release-e2e
manifestSha256            bb00583fd32fc7e512a16b7197b9e4ae9aed41bd1b5649c6015c1af47e20ca60
previousActiveOperationId null
previous version          0.1.1-preview.20-runtime-release
previous toolCount        63
target version            0.1.1-preview.21-semantic-release-e2e
target toolCount          63
```

Independent installed-byte verification shows both targets now equal the preview.21 manifest target hashes:

```text
src/surface-contracts.mjs
09d2f19c0b3a86f1a8e11be9b360f455913d1acfb106ce672abb43d33b0d4f4a

test/public-surface-registration.mjs
a11d663baa88f3df7df5f92faad1c5abca67eb475860fadc5d1e8afc05d91bee
```

At the same time, the executing process is deliberately still preview.20:

```text
version      0.1.1-preview.20-runtime-release
toolCount    63
PID          41548
instanceId   ri_c8620c8dc49e8af26a2d0d7480c3cae1
tunnel       live / ready
```

This is the exact source-published / activation-pending split required by the architecture. It is also the decisive proof that `%LOCALAPPDATA%\Codexless` source publication itself has now occurred through the semantic release tool rather than an ordinary-host PowerShell helper.

The next operation is one semantic `codex.runtime_maintenance restart_codexless` call. The release-aware restart supervisor should detect the pending forward contract, stop the bound preview.20 instance, start preview.21 / 63, verify exact target health, record the release as active, clear pending activation and preserve the managed tunnel.

```text
CHECKPOINT_361=PREVIEW21_SEMANTIC_RELEASE_SOURCE_PUBLISHED_ACTIVATION_PENDING
SEMANTIC_PUBLISH=PASS
INSTALLED_TARGET_HASHES=EXACT
PUBLISH_STATUS=succeeded
PENDING_ACTIVATION=forward
RUNNING_VERSION=preview.20
NEXT=SEMANTIC_RESTART_ACTIVATION
```
