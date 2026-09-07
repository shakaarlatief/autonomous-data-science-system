# Checkpoint 362: Preview.21 Semantic Release Live Activation Qualified

**Date:** 2026-09-07
**Status:** PASS / FIRST END-TO-END SEMANTIC RELEASE + SEMANTIC RESTART ACTIVATION QUALIFIED
**Checkpoint class:** LIVE END-TO-END SEMANTIC UPDATE QUALIFICATION
**Project stage:** Research 122 runtime self-maintenance and device-independent access
**Scope:** Qualifies activation of the first release published through `codex.runtime_release`, including exact process replacement, active-release finalization, pending-state clearance, tunnel preservation, durable restart status and exact installed target hashes.
**Authority:** Research 122 governs the architecture; Validation 120 owns detailed live evidence.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-19`
**Conversation title:** `19 - Hybrid PDF Intent Matrix and Isolation Qualification`
**Primary collaborator:** ChatGPT

Checkpoint 361 preserved the source-published / activation-pending boundary after the first live semantic publish. ChatGPT then invoked exactly one bounded restart mutation through the existing maintenance surface:

```text
action     restart_codexless
requestId  r122.live.preview21.activation.20260907.01
```

The public maintenance call returned before destructive work:

```text
operationId        rm_f0b95f86e6421572f37f2da1775316e1
status             armed
acceptedAtMs       1788789949817
armedAtMs          1788789949823
startedAtMs        null
finishedAtMs       null
errorCode          null
recoveryAttempted  false
recoverySucceeded  null
```

Accepted-to-armed latency was 6 ms.

Independent post-delay inspection proved exact replacement of the preview.20 process by the release target:

```text
old version       0.1.1-preview.20-runtime-release
old PID           41548
old instanceId    ri_c8620c8dc49e8af26a2d0d7480c3cae1

new version       0.1.1-preview.21-semantic-release-e2e
new toolCount     63
new PID           56332
new instanceId    ri_3ae38f351e0586505e9404d64dad5f24
PID changed       true
instance changed  true
```

The managed tunnel remained the exact same process:

```text
tunnel PID       67468
tunnel same PID  true
tunnel start UTC 2026-09-07T11:46:46.9863642Z
health           live
ready            ready
```

The release-aware supervisor finalized release state successfully:

```text
pending activation   absent
shared active lock   absent
active release        preview21-semantic-release-e2e
active schema         codexless.runtime-release-active.v2
snapshotOperationId  rm_cad5ff919dff666fef050e98ddda8680
previous active       null
previous contract     preview.20 / public-preview-v2 / 63
target contract       preview.21-semantic-release-e2e / public-preview-v2 / 63
activatedAtMs         1788789955123
```

The immutable active-history record exists and matches the active release exactly. The original semantic publish operation remains durable `succeeded`.

A status read for the exact restart requestId returned:

```text
status             succeeded
startedAtMs        1788789952920
finishedAtMs       1788789955131
errorCode          null
recoveryAttempted  false
recoverySucceeded  null
```

Restart timing:

```text
accepted -> armed      6 ms
armed -> started       3,097 ms
started -> finished    2,211 ms
accepted -> finished   5,314 ms
```

The two installed release targets still exactly match the preview.21 hashes after activation:

```text
src/surface-contracts.mjs
09d2f19c0b3a86f1a8e11be9b360f455913d1acfb106ce672abb43d33b0d4f4a

test/public-surface-registration.mjs
a11d663baa88f3df7df5f92faad1c5abca67eb475860fadc5d1e8afc05d91bee
```

This completes the decisive normal-update proof for the forward path:

```text
committed private release bundle
-> fresh-host semantic prepare
-> installed-byte preverify
-> semantic publish into installed Codexless tree
-> independent source/status verification
-> semantic restart activation
-> exact preview.21 health
-> same tunnel process preserved
-> active release finalized
```

No ordinary-host `%LOCALAPPDATA%` publication helper and no manual Codexless/tunnel restart were used for preview.21.

The next gate is host-visible post-activation release verification/status, followed by the live rollback path. Because the `codex.runtime_release` schema/tool count did not change between preview.20 and preview.21, the already refreshed disposable chat can be reused for read-only `verify` and `status` qualification before any rollback mutation.

```text
CHECKPOINT_362=PREVIEW21_SEMANTIC_RELEASE_LIVE_ACTIVATION_QUALIFIED
LIVE_VERSION=0.1.1-preview.21-semantic-release-e2e
LIVE_TOOL_COUNT=63
SEMANTIC_PUBLICATION=true
SEMANTIC_ACTIVATION=true
ORDINARY_HOST_PUBLICATION_HELPER=false
MANUAL_RUNTIME_RESTART=false
TUNNEL_PRESERVED=true
NEXT=POSTACTIVATION_VERIFY_STATUS_THEN_ROLLBACK
```
