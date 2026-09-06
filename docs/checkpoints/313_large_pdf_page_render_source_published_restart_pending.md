# Checkpoint 313: Large-PDF Page Render Source Published, Restart Pending

**Date:** 2026-09-06
**Status:** STATIC PASS / LIVE SOURCE PUBLISHED / RESTART + END-TO-END PAGE-16 QUALIFICATION NEXT
**Checkpoint class:** LOCAL EXECUTION / DIRECT CHATGPT FILE ACCESS
**Project stage:** Research 117 / Research 119 direct local-file access
**Scope:** Preserves the bounded implementation that raises only the renderer's source ceiling to 96 MiB, its static qualification against the real 78,874,939-byte Machine Learning source, guarded live publication, regression pass, and the exact post-restart `codex.document_render` page-16 qualification.
**Authority:** Validation 071 is the detailed evidence. Research 119 remains the governing objective correction.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System + read-only `machine-learning` workspace
**Interaction session:** `chatgpt-18`
**Conversation title:** `18 - Astra Architecture Review and Multimodal Handoff Continuation`
**Primary collaborator:** ChatGPT

The representative blocker from Checkpoint 312 is `51.Deep Learning2.annotated.pdf` page 16. Its native one-page PDF is 15,944,609 bytes, but the same maintained PDF.js + canvas runtime renders it at 150 DPI to a 583,130-byte PNG directly from the 78,874,939-byte read-only source.

The new candidate does not widen `codex.document_read`. It modifies only `document-renderer.mjs` so rendering may admit authorized PDF sources up to 96 MiB while source identity is checked with bounded streaming hashes rather than two whole-file parent buffers.

Accepted pre-restart evidence:

```text
real source render feasibility            PASS
real source embedded-text feasibility     PASS
candidate syntax                          PASS
candidate large-source tests              2 / 2 PASS
live source publication                   PASS
installed document-render regression      10 / 10 PASS
source workspace write                    NONE
reasoning-model intermediary              NONE
```

The temporary live-install workspace admission was removed after publication. Durable workspace registry is revision 9 with the normal four workspaces only.

Private runtime complement is synchronized at:

```text
e96d53248de6718d14072dd857325a15587be5dc
```

The exact next step is the canonical controlled Codexless/tunnel restart from `docs/local_execution/OPERATIONS.md`. Because no tool schema or count changed, do not refresh the ChatGPT Plugin for this experiment. After restart, call the already-existing `codex.document_render` in this same chat on Machine Learning page 16.

```text
CHECKPOINT_313 = LARGE_PDF_PAGE_RENDER_SOURCE_PUBLISHED_RESTART_PENDING
```
