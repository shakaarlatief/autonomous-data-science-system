# Checkpoint 350: Runtime Maintenance Preview.19 Live Source Published, Restart Pending

**Date:** 2026-09-07
**Status:** PASS / PREVIEW.19 SOURCE PUBLISHED + INDEPENDENT HASH VERIFICATION / ACTIVATION RESTART NEXT
**Checkpoint class:** LOCAL EXECUTION / LIFECYCLE PUBLICATION
**Project stage:** Research 122 runtime self-maintenance and device-independent access
**Scope:** Preserves successful source-only publication of the preview.19 flat runtime-maintenance schema correction, independent installed-hash verification, unchanged AB-020 semantic-Git, and the deliberate source-published/process-old boundary before activation.
**Authority:** Research 122 governs the architecture; Validation 108 owns the detailed publication evidence.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-19`
**Conversation title:** `19 - Hybrid PDF Intent Matrix and Isolation Qualification`
**Primary collaborator:** ChatGPT

The guarded ordinary-host publication completed successfully and explicitly performed no restart. The helper reran all staged/public/lifecycle tests, replaced exactly three qualified files with timestamped backups, then reran the live-disk regression suites.

Independent read-only verification after publication proved all three installed files exactly match the preview.19 candidate hashes:

```text
src/mcp-server-factory.mjs
  90b93ef7e8c384c441d53cf745537902ff8bd6cd2311af8efb0065565021adc8
src/surface-contracts.mjs
  9d5dc53098f843e7073f5c7c26fd10d4e2aa57dddb17c5458002138d295dc5f0
test/public-surface-registration.mjs
  a7450e461539ea2ff778fca8d23a3b2c084d98c93a19594c94af8e28450213ce
```

AB-020 semantic-Git remains exactly:

```text
3b2ddbbe00339045b81044bb3e1e39c314a461a7e0f8e4e608b79b4b0f37de02
```

The active process is intentionally still:

```text
0.1.1-preview.18-runtime-maintenance
62 tools
codexless-public-preview-v2
```

and the tunnel remains `live/ready`. This is the expected source-published/restart-pending boundary. The preview.18 runtime-maintenance tool is still not used for activation because its ChatGPT host projection failed the schema-fidelity gate.

```text
CHECKPOINT_350=RUNTIME_MAINTENANCE_PREVIEW19_LIVE_SOURCE_PUBLISHED_RESTART_PENDING
INSTALLED_HASHES=PASS
SEMANTIC_GIT_PRESERVED=true
RUNNING_PROCESS=preview.18/62
TUNNEL=live/ready
RESTART_PERFORMED=false
NEXT=MANUAL_RUNBOOK_CONTROLLED_PREVIEW19_ACTIVATION_RESTART
```
