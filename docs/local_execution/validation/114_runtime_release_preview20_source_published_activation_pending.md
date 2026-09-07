# Validation 114: Runtime Release Preview.20 Source Published, Activation Pending

**Date:** 2026-09-07
**Status:** PASS / SOURCE-ONLY PUBLICATION VERIFIED / NO RESTART YET
**Research:** Research 122
**Private source head:** `77e13dc69aec8e2fdc7ffa8379cccf039046785e`
**Scope:** Verify that the exact Checkpoint 355 helper published only the qualified preview.20 source/test target set, that the installed files match the preserved candidate byte-for-byte, and that preview.19 plus the managed tunnel remain live before semantic activation.

## 1. Publication result

The user ran the exact protected helper with `-Publish` and confirmed the high-impact action.

The helper re-ran the full preflight first, then emitted timestamped backup paths for all replacement targets, installed the hash-bound source additions/replacements, ran all nine public regressions from the live installed tree, and returned:

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

No rollback path was invoked.

## 2. Independent installed-byte verification

After publication, ChatGPT independently compared all candidate files in the preview.20 `src` and `test` directories to the installed Codexless equivalents.

Result:

```text
ComparedFiles  22
MismatchCount  0
```

This proves the installed source/test surface exactly matches the final private candidate, including files that were newly added and files that were already unchanged between preview.19 and preview.20.

## 3. Process and tunnel boundary

Independent health after source publication:

```text
version       0.1.1-preview.19-runtime-maintenance-schema
toolCount     62
surface       codexless-public-preview-v2
PID           69280
instanceId    ri_780a50fef8f801bc0086ab8a40efd990
```

Tunnel:

```text
/healthz  live
/readyz   ready
```

Therefore source publication did not implicitly restart the process or tunnel.

## 4. Private authority binding

The private runtime repository remained synchronized:

```text
HEAD      77e13dc69aec8e2fdc7ffa8379cccf039046785e
upstream  77e13dc69aec8e2fdc7ffa8379cccf039046785e
```

This is the same candidate bound into the qualified helper.

## 5. Activation boundary

The installed tree is now preview.20 while the executing process is still preview.19. This split is intentional and temporary.

The required next call is exactly one semantic restart through the currently live preview.19 maintenance surface. The bootstrap compatibility probe from Validation 113 already reproduced this old-process/new-supervisor boundary in isolation and passed replacement into preview.20 / 63.

No manual Codexless or tunnel restart is required for the activation attempt.

```text
PREVIEW20_SOURCE_PUBLICATION=PASS
INSTALLED_BYTES=EXACT
LIVE_PROCESS=PREVIEW19_62
TUNNEL_PRESERVED=true
RESTART_PERFORMED=false
NEXT=CODEX_RUNTIME_MAINTENANCE_ACTIVATION
```
