# Checkpoint 287: Document Render Live Source Published, Restart Pending

**Date:** 2026-09-04
**Status:** LIVE SOURCE PUBLISHED / CONTROLLED RESTART PENDING
**Checkpoint class:** EXPERIMENT_VERIFICATION
**Project stage:** Research 117 reuse-first multimodal document architecture
**Scope:** Preserves successful guarded host publication of the Checkpoint 286 `codex.document_render` candidate into the installed Codexless source tree, while the existing process still serves preview.10 / 53 tools pending the repository-authoritative controlled restart.
**Authority:** Historical experiment boundary. Validation 046 owns the publication evidence; this checkpoint does not yet claim restarted preview.11 runtime health, tunnel readiness, refreshed ChatGPT discovery, or live page-image qualification.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-17`
**Conversation title:** `17 - MCP Image Bridge Publication Recovery and Multimodal Document Continuation`
**Primary collaborator:** ChatGPT

## Boundary

Checkpoint 286 qualified the candidate and guarded helper without touching the installed runtime. The project owner has now executed that exact helper from ordinary host PowerShell and approved only the helper's `ShouldProcess` publication target `%LOCALAPPDATA%\Codexless`.

Publication returned:

```text
DOCUMENT_RENDER_PUBLICATION_PREFLIGHT=PASS
DOCUMENT_RENDER_PUBLICATION_RESULT=PASS
EXPECTED_PUBLIC_SERVER_VERSION=0.1.1-preview.11
EXPECTED_PUBLIC_SURFACE_VERSION=codexless-public-preview-v2
EXPECTED_PUBLIC_TOOL_COUNT=54
RENDER_ISOLATION=codex-command-exec-read-only
RENDER_BACKEND=managed-pdfjs-dist+@napi-rs/canvas
MODEL_TURN_REQUIRED=false
NEW_EXTERNAL_DEPENDENCY=false
RESTART_PERFORMED=false
```

Updated installed-runtime files were exactly the expected document-render source/test set recorded in Validation 046.

A separate model-free post-publication health query proved the old foreground process is still serving:

```text
0.1.1-preview.10
codexless-public-preview-v2
53 tools
```

That split state is expected and is the reason restart is now mandatory before any ChatGPT tool-surface refresh.

## Authority boundary

This checkpoint does not solve host runtime maintenance by broadening ordinary workspace authority. Publication still used the guarded user-host route because `%LOCALAPPDATA%` remains outside ordinary project-workspace admission. AB-002 and AB-017 remain the future architecture owners for a narrow semantic runtime-maintenance capability.

## Exact continuation

The governing procedure has been freshly resolved and read from `docs/local_execution/OPERATIONS.md`.

```text
1. stop tunnel-client first with Ctrl+C; keep the Git Bash shell open;
2. stop Codexless HTTP with Ctrl+C;
3. restart Codexless from `%LOCALAPPDATA%\Codexless\bin\codexless-http.cmd`;
4. verify Codexless health reports preview.11 / v2 / 54 tools and expected defaultCwd;
5. confirm tunnel variables are SET without printing values;
6. restart tunnel; verify healthz 200 and readyz 200;
7. refresh the existing ChatGPT developer MCP app only after both layers are healthy;
8. use a fresh disposable chat to discover and invoke `codex.document_render` on a known authorized PDF;
9. require actual visual page facts before classifying the live bridge PASS;
10. repeat `codex.document_read` smoke after restart;
11. only then begin representative annotated/math/table/multi-column/scanned PDF fidelity qualification.
```

Research 117 remains active. Source Vault and v17 viewer work remain paused as previously recorded.

Primary evidence:

```text
docs/local_execution/validation/046_document_render_live_source_published_restart_pending.md
docs/local_execution/validation/045_sandboxed_managed_pdf_render_publication_preflight_qualified.md
docs/checkpoints/286_sandboxed_managed_pdf_render_publication_preflight_qualified.md
docs/local_execution/OPERATIONS.md
```
