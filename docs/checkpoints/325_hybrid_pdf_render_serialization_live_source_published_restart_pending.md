# Checkpoint 325: Hybrid PDF Render Serialization Live Source Published / Restart Pending

**Date:** 2026-09-06
**Status:** LIVE SOURCE PUBLISHED / CONTROLLED RESTART PENDING
**Checkpoint class:** LOCAL EXECUTION / DIRECT CHATGPT FILE ACCESS
**Project stage:** Research 120 automatic hybrid PDF direct-source routing
**Scope:** Preserves successful publication of the Checkpoint 323 renderer-serialization correction and its matching adapted public regression into the installed Codexless preview.16 tree, with independent exact-hash verification and no process restart yet.
**Authority:** Validation 083 is the exact publication and verification evidence. `docs/local_execution/OPERATIONS.md` governs restart order.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-19`
**Conversation title:** `19 - Hybrid PDF Intent Matrix and Isolation Qualification`
**Primary collaborator:** ChatGPT

The qualified host helper completed successfully and reported all seven live-disk public regressions PASS. Independent post-publication reads confirmed exact installed hashes:

```text
document-renderer.mjs
42199fca624f931f0076a502dbe4c4710f26f0769db50a64a2ac2174b6899b43

document-render-regression.mjs
3e60f761ebf5d68dcf4b05969e62dc3cf3d6931aebe4ab7403b66fc37ac4b725
```

The running process still reports:

```text
0.1.1-preview.16-hybrid-pdf-access
60 tools
codexless-public-preview-v2
```

and the tunnel was still `healthz=200` / `readyz=200` before restart. Because `RESTART_PERFORMED=false`, none of this proves that the new renderer implementation is active in the running process.

The next action is the full controlled restart from `docs/local_execution/OPERATIONS.md`. Stop the tunnel first while keeping its Git Bash shell open, then stop and restart Codexless, verify local health/tool count, restart and verify the tunnel, and only then perform the fresh disposable intent-matrix qualification.

```text
CHECKPOINT_325 = HYBRID_PDF_RENDER_SERIALIZATION_LIVE_SOURCE_PUBLISHED_RESTART_PENDING
```
