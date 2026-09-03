# Checkpoint 280: Reuse-First Document Architecture and Local Media Bridge Research

**Date:** 2026-09-03
**Status:** RESEARCH OPENED / NO NEW DOCUMENT IMPLEMENTATION ACCEPTED
**Checkpoint class:** ARCHITECTURE RESEARCH
**Project stage:** Codex/Codexless upstream ecosystem research, document-subsystem assumptions re-opened after live PDF qualification
**Scope:** Preserve the decision to stop before building `codex.document_render`, OCR, or custom Office adapters and instead test current OpenAI/Codex/mature-library reuse paths first.
**Authority:** Historical architecture/research boundary. Validation 039 and Checkpoint 279 remain authoritative for the already accepted `workspace-standard` and `codex.document_read` baseline.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-16`
**Conversation title:** `16 - Codex Live Task Viewer Publication and Source Vault Continuation`
**Primary collaborator:** ChatGPT
**Branch:** `v1-source-vault-bootstrap-resume`

## Trigger

After `codex.document_read` was live-qualified, the project owner explicitly challenged whether ADS was about to rebuild capabilities that OpenAI, Codex or mature document projects already provide. The project owner accepted that prior PDF implementation could become redundant if a better current architecture exists.

This checkpoint therefore records a deliberate **reuse-first stop rule** before additional document implementation.

## Most important findings

Research 117 found that current OpenAI PDF file inputs already supply a vision-capable model with both extracted text and an image of each PDF page. This means the conceptual `text + visual page` understanding pipeline already exists upstream.

The installed OpenAI Codex primary-runtime also currently exposes maintained skills for:

```text
PDF             read / render / visually inspect
DOCX            read/edit + render to page PNG for visual QA
PPTX            read/edit + render every slide for visual QA
XLSX/CSV/etc.   structured workbook analysis + rendered visual QA
```

Current Codex App Server/upstream source also supports image/local-image model inputs and `view_image`-style image attachment semantics.

Mature external candidates exist as well:

```text
Microsoft MarkItDown
Docling / docling-mcp
PyMuPDF4LLM
```

These findings make a broad custom ADS document stack premature.

## Current architectural disposition

```text
KEEP
    workspace-standard exact-root authority
    codex.document_read deterministic PDF text/provenance path

PAUSE
    codex.document_render implementation
    custom OCR implementation
    custom DOCX/PPTX/XLSX adapters

RESEARCH / PROVE
    MCP image-result -> ChatGPT model-vision visibility
    authorized local file -> native OpenAI file-input handoff
    Codex maintained PDF Skill on real authorized PDFs
    App Server localImage/image handoff
    native maintained Skills for DOCX/PPTX/XLSX

BENCHMARK ONLY IF NATIVE PATHS LEAVE GAPS
    MarkItDown
    Docling
    PyMuPDF4LLM
```

## Immediate experiment order

```text
E117-1 MCP image visibility through the actual ChatGPT developer-MCP host
E117-2 maintained Codex PDF Skill visual inspection on an authorized representative PDF
E117-3 exact installed App Server localImage capability/authority qualification
E117-4 representative PDF comparison against the deterministic PDF.js baseline
E117-5 DOCX/PPTX/XLSX maintained-skill qualification
E117-6 third-party converter benchmark only if justified by unresolved gaps
```

The existing ADS Browser screenshot action would be a low-cost E117-1 probe because it already emits MCP image content, but current local Browser status reports `chrome_skill_unavailable`. Browser repair is not part of this checkpoint and should not be undertaken merely to force the experiment.

## Continuity effect

Research 113 remains the broader active program. Research 117 is now a nested high-value architecture study because it directly tests whether ADS can delete/avoid future custom work by reusing current upstream capabilities.

MC-0010 remains important because Claude is separately asked to inspect current OpenAI Codex/App Server, Liyana's public Codexless repository and private ADS runtime evidence. Its conclusions should be considered before final document architecture promotion when available.

## Exact continuation

```text
1. run E117-1 if a standard image-returning MCP route becomes available without unrelated repair
2. qualify the maintained Codex PDF Skill and localImage semantics with the smallest safe experiment
3. compare against the current document_read baseline on representative real material
4. do not implement document_render/OCR/Office adapters until those results are reconciled
5. continue MC-0010 Claude dual-repository access/research path
6. run chat-rotation preflight only after this new Research 117 boundary is durably preserved
```
