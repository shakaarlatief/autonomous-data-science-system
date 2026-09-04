# Checkpoint 288: Document Render Live ChatGPT Vision Qualified

**Date:** 2026-09-04
**Status:** LIVE QUALIFIED / E117-4D PASS
**Checkpoint class:** EXPERIMENT_VERIFICATION
**Project stage:** Research 117 reuse-first multimodal document architecture
**Scope:** Preserves successful post-restart live qualification of `codex.document_render` from authorized local PDF pages through the existing read-only Codex command sandbox, maintained primary-runtime PDF.js + canvas, standard MCP image content, and direct ChatGPT vision.
**Authority:** Validation 047 is the primary evidence. This checkpoint closes the live semantic page-render transport question but does not yet close representative PDF fidelity or broader document-format work.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-17`
**Conversation title:** `17 - MCP Image Bridge Publication Recovery and Multimodal Document Continuation`
**Primary collaborator:** ChatGPT

## Boundary

Checkpoint 287 preserved successful host publication while the old process still served preview.10 / 53 tools. The controlled restart, tunnel reconnection, and ChatGPT developer-MCP refresh have now completed successfully.

Live infrastructure is independently verified as:

```text
Codexless        0.1.1-preview.11
surface          codexless-public-preview-v2
public tools     54
health           PASS
tunnel health    200
tunnel ready     200
```

The prior `codex.document_read` semantic path survived restart and still returns `SANDBOX` through pinned `pdfjs-dist@5.4.624` with OCR disabled.

A fresh disposable ChatGPT conversation then invoked only `codex.document_render` on the known two-page authorized PDF and reported genuine visual-only page facts from both returned images. It received exact renderer metadata for maintained `pdfjs-dist@5.6.205` + `@napi-rs/canvas@0.1.100`, fixed 150 DPI, `codex-command-exec-read-only` isolation, `[1,2]` page selection, no OCR, and 1275 x 1651 PNGs.

It classified:

```text
MCP_DOCUMENT_RENDER_TO_CHATGPT_VISION=PASS
```

The continuing project session independently invoked the same live action after restart and received both standard MCP page images plus matching metadata. Direct vision again confirmed the expected page geometry and labels.

## Accepted live architecture

```text
authorized local PDF
    -> existing workspace read authority
    -> bounded source validation
    -> Codex command/exec :read-only sandbox
    -> maintained PDF.js + canvas
    -> in-memory page PNG(s)
    -> validated standard MCP image content
    -> ChatGPT native vision
```

Properties:

```text
extra Codex model turn    no
Browser                   no
OCR                       no
workspace write           no
host temp output          no
new external dependency   no
caller renderer control   no
```

## What remains open

The next question is fidelity and coverage rather than transport:

```text
mathematical notation
annotations
complex tables
multi-column layouts
unusual embedded fonts
scanned/image-only PDFs
large-document bounds / latency
```

No broader OCR or third-party fallback architecture should be added until representative tests expose a concrete gap. The broader `%LOCALAPPDATA%` runtime-maintenance authority question remains separate under AB-002 / AB-017.

## Exact continuation

```text
1. preserve this live qualification in Research 117, CURRENT_STATE, routing and Knowledge Map;
2. keep preview.11 / 54-tool runtime as the accepted live baseline;
3. define a bounded representative PDF fidelity matrix using already-authorized project/source material where possible;
4. test text-heavy, mathematical, annotated, table-heavy, multi-column and image-only/scanned cases without adding new adapters first;
5. characterize concrete fidelity/OCR gaps;
6. only benchmark MarkItDown, Docling, PyMuPDF4LLM or other fallback stacks if those gaps justify them.
```

Primary evidence:

```text
docs/local_execution/validation/047_document_render_live_chatgpt_vision_qualified.md
docs/local_execution/validation/046_document_render_live_source_published_restart_pending.md
docs/local_execution/validation/045_sandboxed_managed_pdf_render_publication_preflight_qualified.md
docs/research/117_reuse_first_multimodal_document_architecture_and_local_media_handoff.md
```
