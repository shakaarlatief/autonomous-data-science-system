# Checkpoint 344: Runtime Maintenance Preview.18 Publication Preflight Qualified

**Date:** 2026-09-07
**Status:** PASS / GUARDED PREVIEW.18 PUBLICATION PREFLIGHT QUALIFIED / ORDINARY-HOST PUBLICATION NEXT
**Checkpoint class:** LOCAL EXECUTION / LIFECYCLE PUBLICATION
**Project stage:** Research 122 runtime self-maintenance and device-independent access
**Scope:** Qualifies the exact guarded source-only publication package for the preview.18 `codex.runtime_maintenance` integration after Checkpoint 343, including live-baseline binding, candidate hashes, staged 62-tool regressions, lifecycle regressions/probes, Windows atomic replacement smoke coverage and rollback semantics.
**Authority:** Research 122 governs the architecture; Validation 102 owns the detailed publication evidence.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-19`
**Conversation title:** `19 - Hybrid PDF Intent Matrix and Isolation Qualification`
**Primary collaborator:** ChatGPT

The guarded helper is prepared in protected private-runtime scratch and is bound to private candidate head:

```text
610fb6c1480012b0db80965239493348e5de5a58
```

Helper SHA-256:

```text
5c1de81279e4dbf4fb009aa585ca8d832cfd863dbe8765e6139ab75a0542802f
```

Two complete no-publish preflights passed. Each run verified the live preview.17 / 61-tool baseline, exact candidate hashes, unchanged AB-020 semantic-Git source, live tunnel `live/ready`, the eight staged public regressions, the 12/12 + 7/7 + 6/6 lifecycle suites, all three isolated lifecycle probes, and the same Windows `File.Replace` forward/rollback primitive that publication will use.

The publication package replaces four live source files and three live regression files, and adds seven new runtime-maintenance source modules. Existing files use same-directory temporary copies plus `File.Replace(candidateTemp, livePath, timestampedBackup, true)` with immediate old/new hash verification. New files use same-directory temp + move. Any failure removes exact newly added files and restores completed replacements from verified backups using the already-qualified rollback primitive.

The helper performs no restart. A successful publication will therefore leave the running process on preview.17 / 61 tools until independent installed-hash verification and a separate runbook-controlled bootstrap restart.

```text
CHECKPOINT_344=RUNTIME_MAINTENANCE_PREVIEW18_PUBLICATION_PREFLIGHT_QUALIFIED
NO_LIVE_FILES_MODIFIED=true
RESTART_PERFORMED=false
NEXT=ORDINARY_HOST_PUBLISH
```
