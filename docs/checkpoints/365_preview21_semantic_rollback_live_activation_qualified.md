# Checkpoint 365: Preview.21 Semantic Rollback Live Activation Qualified

**Date:** 2026-09-07
**Status:** PASS / SEMANTIC ROLLBACK ACTIVATION RETURNED TO PREVIEW.20 / FINAL PUBLIC READBACK NEXT
**Checkpoint class:** LIVE SEMANTIC ROLLBACK ACTIVATION QUALIFICATION
**Project stage:** Research 122 runtime self-maintenance and device-independent access
**Scope:** Qualifies the runtime activation half of the first explicit semantic rollback, including exact preview.21 -> preview.20 process replacement, restored-source retention, pending/active-state finalization and tunnel preservation.
**Authority:** Research 122 governs the architecture; Validation 123 owns detailed live evidence.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-19`
**Conversation title:** `19 - Hybrid PDF Intent Matrix and Isolation Qualification`
**Primary collaborator:** ChatGPT

Checkpoint 364 preserved the rollback-source-published / activation-pending boundary. ChatGPT then invoked exactly one bounded semantic restart:

```text
action     restart_codexless
requestId  r122.live.preview21.rollback.activation.20260907.01
```

The public restart call returned before destructive work:

```text
operationId        rm_ca482535bb5e44d82586298b04a39c3d
status             armed
acceptedAtMs       1788790744948
armedAtMs          1788790744953
startedAtMs        null
finishedAtMs       null
errorCode          null
recoveryAttempted  false
recoverySucceeded  null
```

Accepted-to-armed latency was 5 ms.

Independent post-delay inspection proved exact rollback activation:

```text
old version       0.1.1-preview.21-semantic-release-e2e
old PID           56332
old instanceId    ri_3ae38f351e0586505e9404d64dad5f24

new version       0.1.1-preview.20-runtime-release
new toolCount     63
new PID           10280
new instanceId    ri_39018a407e14b5fb789134bab0d1f398
PID changed       true
instance changed  true
```

The restored preview.20 installed hashes remain exact after restart:

```text
src/surface-contracts.mjs
9286d3838d227055f4591a75dbc2c76ef3c107a8fd99168197892c4d9b4db76b

test/public-surface-registration.mjs
b5b5781d71343fea66102fd27a652131b90913191b9f5179839dc81042ec9bb2
```

The managed tunnel remained the exact same process throughout:

```text
tunnel PID       67468
tunnel same PID  true
tunnel start UTC 2026-09-07T11:46:46.9863642Z
health           live
ready            ready
```

Release-aware finalization after the rollback restart is exactly as designed for a rollback to an unmanaged predecessor:

```text
pending activation   absent
shared mutation lock absent
active-release.json   absent
rollback operation    succeeded
```

The active managed-release pointer was removed rather than rewritten to another release because preview.21 was the first managed release and preview.20 was its unmanaged bootstrap predecessor.

A durable status read for the exact restart requestId returned:

```text
status             succeeded
startedAtMs        1788790748052
finishedAtMs       1788790750459
errorCode          null
recoveryAttempted  false
recoverySucceeded  null
```

Restart timing:

```text
accepted -> armed      5 ms
armed -> started       3,099 ms
started -> finished    2,407 ms
accepted -> finished   5,511 ms
```

The rollback publication operation remains independently durable `succeeded` with no recovery.

This completes the production rollback execution path:

```text
active preview.21
-> semantic rollback publication
-> exact preview.20 source snapshot restored
-> preview.21 process intentionally remains live
-> semantic restart
-> healthy preview.20 / 63 replacement
-> same tunnel preserved
-> pending + active managed-release state finalized
```

The only remaining AB-002 qualification is final public-tool readback from the refreshed host: status of the existing rollback operation and verification that the preview.21 target now mismatches in exactly two files after rollback. This final readback should perform no mutation.

```text
CHECKPOINT_365=PREVIEW21_SEMANTIC_ROLLBACK_LIVE_ACTIVATION_QUALIFIED
LIVE_VERSION=0.1.1-preview.20-runtime-release
ROLLBACK_RESTART_STATUS=succeeded
RESTORED_HASHES=exact
PENDING_ACTIVATION=false
ACTIVE_MANAGED_RELEASE=false
TUNNEL_PRESERVED=true
NEXT=FINAL_PUBLIC_ROLLBACK_STATUS_VERIFY
```
