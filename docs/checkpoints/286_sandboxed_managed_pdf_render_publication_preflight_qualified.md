# Checkpoint 286: Sandboxed Managed PDF Render Publication Preflight Qualified

**Date:** 2026-09-04
**Status:** CANDIDATE QUALIFIED / HOST PUBLICATION PENDING
**Checkpoint class:** EXPERIMENT_VERIFICATION
**Project stage:** Research 117 reuse-first multimodal document architecture
**Scope:** Preserves publication-preflight qualification of `codex.document_render`, using maintained primary-runtime PDF.js + canvas inside the existing Codex read-only command sandbox and returning standard MCP page images without workspace/temp writes or an extra model turn.
**Authority:** Historical experiment boundary. Validation 045 is primary evidence; live qualification still requires guarded publication, controlled restart/reconnect/schema refresh, and a fresh ChatGPT visual test.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-17`
**Conversation title:** `17 - MCP Image Bridge Publication Recovery and Multimodal Document Continuation`
**Primary collaborator:** ChatGPT

## Boundary

Checkpoint 285 proved that maintained primary-runtime Poppler can rasterize PDF pages, but left a security question unresolved: a direct native Poppler child would execute with ordinary Codexless host identity.

Checkpoint 286 resolves that design question without weakening read authority. Direct discrimination proved the existing Codex `command/exec` read-only sandbox denies writes to both the workspace and ordinary `%TEMP%`, allows managed runtime reads, and blocks tested non-loopback TCP while permitting loopback. The maintained primary runtime also contains `pdfjs-dist@5.6.205` plus `@napi-rs/canvas@0.1.100`, allowing page rasterization wholly in memory.

The preferred candidate is now:

```text
workspace-authorized PDF
    -> canonical containment + bounded source preflight
    -> existing Codex command/exec :read-only sandbox
    -> maintained primary-runtime PDF.js + canvas
    -> in-memory PNG page(s)
    -> bounded internal stdout protocol
    -> validated source/render provenance
    -> standard MCP image content
    -> ChatGPT native vision
```

This is a thin authority/handoff seam, not a new rendering engine.

## Candidate contract

```text
new tool                         codex.document_render
expected public version          0.1.1-preview.11
surface                          codexless-public-preview-v2
expected public tools            54
model turn                       none
new external dependency          none
caller write authority           none
renderer sandbox                 codex command/exec :read-only
renderer                         managed pdfjs-dist + @napi-rs/canvas
DPI                              fixed 150
selected pages                   maximum 4
per-page PNG ceiling             4 MiB
aggregate PNG ceiling            8 MiB
OCR                              none
```

The internal renderer transport receives a bounded larger stdout ceiling because image base64 exceeds the public 32 KiB command-output cap. That option remains internal to `CodexAuthorityExecutor.exec`; the strict public `codex.command_exec` schema rejects `outputBytesCap`.

## Verification

```text
DOCUMENT_RENDER_REGRESSION=PASS tests=10
FLEXIBLE_AUTHORITY_REGRESSION=PASS tests=7
BOUNDED_GIT_FETCH_ORIGIN=PASS tools=54
BOUNDED_GIT_PULL_FF_ONLY=PASS tools=54
PUBLIC_SURFACE_REGISTRATION=PASS tools=54
IMAGE_READ_REGRESSION=PASS tests=7
DOCUMENT_RENDER_PUBLICATION_PREFLIGHT=PASS
PUBLIC_COMMAND_INTERNAL_OUTPUT_CAP_REMOTE_SCHEMA=REJECTED
MODEL_TURN_REQUIRED=false
NEW_EXTERNAL_DEPENDENCY=false
NO_LIVE_FILES_MODIFIED=true
```

A separate current-live `codex.document_read` semantic smoke also passed on the generated one-page PDF through the existing pinned `pdfjs-dist@5.4.624` reader. Its isolated stage regression remains intentionally unsuitable for the stage-local `node_modules` junction because the accepted Node permission model cannot traverse that junction.

The first sandbox probe's standard-font warnings were resolved without enabling system fonts. Managed font files were present and sandbox-readable; PDF.js Node factory semantics required normalized filesystem path strings rather than `file://` URL strings. The corrected renderer produced the synthetic test pages without warnings, and host-side visual materialization of the same rendering stack was visibly correct through `codex.image_read`.

## Publication state

The guarded host helper is prepared and its no-publish preflight passed:

```text
.ads-private/codexless/activate-document-render-publication.ps1
SHA-256 C2C73B571E0BC3A296BB79DA00B4F2472FD23C358889931BB500EA42576061AF
```

Current live state remains preview.10 / 53 tools. No live Codexless file was modified by this checkpoint.

## Exact continuation

```text
1. run .\.ads-private\codexless\activate-document-render-publication.ps1 -Publish from ordinary host PowerShell at the ADS root;
2. approve only its exact ShouldProcess publication prompt;
3. inspect the complete publication output before restart;
4. if PASS, follow docs/local_execution/OPERATIONS.md full controlled restart order exactly: stop tunnel first, stop Codexless, restart/verify preview.11 and 54 tools, restart/verify tunnel health + readiness, then refresh ChatGPT app;
5. repeat a live codex.document_read smoke after restart;
6. in a fresh disposable ChatGPT conversation, discover and call codex.document_render on a known authorized PDF;
7. require actual page-image visual facts for live qualification;
8. only after live semantic qualification begin representative annotated/math/table/multi-column/scanned PDF fidelity work.
```

Research 117 remains active. Source Vault ingestion and the broader paused work remain unchanged.

Primary evidence:

```text
docs/local_execution/validation/045_sandboxed_managed_pdf_render_publication_preflight_qualified.md
docs/research/117_reuse_first_multimodal_document_architecture_and_local_media_handoff.md
docs/local_execution/validation/044_managed_primary_runtime_poppler_page_rendering_probe_qualified.md
docs/local_execution/validation/043_model_free_mcp_image_bridge_live_chatgpt_vision_qualified.md
```
