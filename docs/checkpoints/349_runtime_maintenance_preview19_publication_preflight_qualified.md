# Checkpoint 349: Runtime Maintenance Preview.19 Publication Preflight Qualified

**Date:** 2026-09-07
**Status:** PASS / PREVIEW.19 SCHEMA-CORRECTION PUBLICATION PREFLIGHT QUALIFIED / ORDINARY-HOST PUBLICATION NEXT
**Checkpoint class:** LOCAL EXECUTION / LIFECYCLE PUBLICATION
**Project stage:** Research 122 runtime self-maintenance and device-independent access
**Scope:** Qualifies the exact guarded source-only publication package for the preview.19 flat runtime-maintenance schema correction after the fresh-host preview.18 projection failure.
**Authority:** Research 122 governs the architecture; Validation 107 owns the detailed publication-preflight evidence.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-19`
**Conversation title:** `19 - Hybrid PDF Intent Matrix and Isolation Qualification`
**Primary collaborator:** ChatGPT

The publication helper is bound to private head:

```text
ac3e05de0ebd9553eafb322ce19ec17539f1c09d
```

and has SHA-256:

```text
3ce8d4561886a8101525666cc6c084ed94b2f9607d36ec5a7ea797961b2be165
```

The package is deliberately minimal. It replaces exactly three existing installed files:

```text
src/mcp-server-factory.mjs
src/surface-contracts.mjs
test/public-surface-registration.mjs
```

No new runtime module is added. The running baseline must remain exact preview.18 / 62 tools and the tunnel must remain live/ready before mutation is allowed.

Two complete no-publish preflights passed. Each run verified the exact preview.18 live hashes, exact preview.19 candidate hashes, unchanged AB-020 semantic-Git source, eight staged public regressions, the new actual MCP wire-schema assertion, all three lifecycle suites, all three lifecycle functional probes, and the exact Windows `File.Replace` forward/rollback primitive used by publication.

The helper performs no restart. On publication success, the running process must still report preview.18 / 62 tools until independent installed-hash verification and a separate manual activation restart. Preview.18's host-projected mutation schema is intentionally not used to bootstrap preview.19.

```text
CHECKPOINT_349=RUNTIME_MAINTENANCE_PREVIEW19_PUBLICATION_PREFLIGHT_QUALIFIED
PREFLIGHT_RUNS=2/2
NO_LIVE_FILES_MODIFIED=true
RESTART_PERFORMED=false
NEXT=ORDINARY_HOST_PREVIEW19_PUBLICATION
```
