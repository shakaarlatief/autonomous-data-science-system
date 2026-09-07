# Checkpoint 356: Runtime Release Preview.20 Source Published, Activation Pending

**Date:** 2026-09-07
**Status:** PASS / PREVIEW.20 SOURCE PUBLISHED AND VERIFIED / LIVE ACTIVATION NEXT
**Checkpoint class:** SOURCE PUBLICATION BOUNDARY
**Project stage:** Research 122 runtime self-maintenance and device-independent access
**Scope:** Preserves successful preview.20 source-only publication, independent installed-hash verification, and the still-running preview.19 / tunnel boundary before semantic activation.
**Authority:** Research 122 governs the architecture; Validation 114 owns the detailed evidence.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-19`
**Conversation title:** `19 - Hybrid PDF Intent Matrix and Isolation Qualification`
**Primary collaborator:** ChatGPT

The exact guarded preview.20 helper qualified in Checkpoint 355 was run manually with `-Publish` and explicit high-impact confirmation.

The helper reported:

```text
RUNTIME_RELEASE_PREVIEW20_PUBLICATION_RESULT=PASS
CANDIDATE_HEAD=77e13dc69aec8e2fdc7ffa8379cccf039046785e
TARGET_VERSION=0.1.1-preview.20-runtime-release
TARGET_TOOL_COUNT=63
LIVE_DISK_PUBLIC_REGRESSIONS=PASS scripts=9
RUNNING_PROCESS_STILL=0.1.1-preview.19-runtime-maintenance-schema/62
TUNNEL_STILL=live/ready
RESTART_PERFORMED=false
```

Timestamped backups were created for every replacement target. New runtime-release modules/tests were added only where the exact preflight required prior absence.

Independent ChatGPT-side post-publication verification compared every candidate `src` and `test` file against the installed Codexless tree:

```text
ComparedFiles   22
MismatchCount   0
```

The still-running process remained the already-qualified preview.19 instance:

```text
version       0.1.1-preview.19-runtime-maintenance-schema
toolCount     62
surface       codexless-public-preview-v2
PID           69280
instanceId    ri_780a50fef8f801bc0086ab8a40efd990
```

The managed tunnel remained:

```text
health  live
ready   ready
```

Private source authority remained exactly synchronized:

```text
private HEAD      77e13dc69aec8e2fdc7ffa8379cccf039046785e
private upstream  77e13dc69aec8e2fdc7ffa8379cccf039046785e
```

This is the deliberate source-published / activation-pending boundary. Preview.20 bytes are installed and regression-qualified, but preview.20 is not yet live because the current process has not been replaced.

The next operation is now semantic and does not require another ordinary-host stop/start. The already-live preview.19 `codex.runtime_maintenance` tool should be invoked exactly once with a new stable requestId. The newly installed bootstrap-compatible supervisor is expected to derive preview.20 / 63 from its own newly installed surface constants, gracefully stop the bound preview.19 instance, start the replacement worker, preserve the tunnel, and return durable terminal status after reconnection.

```text
CHECKPOINT_356=RUNTIME_RELEASE_PREVIEW20_SOURCE_PUBLISHED_ACTIVATION_PENDING
INSTALLED_SOURCE_MATCHES_CANDIDATE=true
RUNNING_VERSION=0.1.1-preview.19-runtime-maintenance-schema
RUNNING_TOOL_COUNT=62
TARGET_VERSION=0.1.1-preview.20-runtime-release
TARGET_TOOL_COUNT=63
TUNNEL=live/ready
NEXT=SEMANTIC_PREVIEW20_ACTIVATION
```
