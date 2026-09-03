# Research 117: Reuse-First Multimodal Document Architecture and Local Media Handoff

**Date:** 2026-09-03
**Status:** ACTIVE / REUSE-FIRST ARCHITECTURE RESEARCH
**Scope:** Re-evaluate the local ADS document roadmap after the live `codex.document_read` PDF qualification. Determine which document, rendering, vision, OCR, and Office-file capabilities already exist in current OpenAI/Codex ecosystems or mature libraries before ADS adds new custom parsers or renderers.
**Authority:** Level-2 architecture research. This record does not supersede Validation 039 or remove the accepted `codex.document_read` baseline. It deliberately pauses further custom document implementation until reuse experiments settle the next architecture.
**Declared references:** `research:113`, `research:114`, `research:115`, `research:116`, `checkpoint:279`, `path:docs/local_execution/validation/039_workspace_standard_and_document_read_live_qualified.md`, `path:docs/OPEN_ARCHITECTURE_BACKLOG.md`

## 1. Why this research was opened

Checkpoint 279 proved a professional first local binary-document path: explicit ordinary-workspace authority plus bounded PDF embedded-text extraction with provenance. The project owner then challenged the next assumption directly: ADS should not keep building a private PDF/document stack if current OpenAI/Codex capabilities or mature document systems already solve the hard parts better.

The decision criterion is therefore not whether ADS *can* implement rendering/OCR/adapters. It is whether doing so is the best architecture after current upstream capabilities are examined.

The governing principle is:

```text
reuse first
-> prove exact local/host capability
-> wrap only the missing authority/handoff seam
-> preserve semantic provenance and least authority
-> build custom parsing/rendering only where the reusable stack is inadequate
```

## 2. Official OpenAI file-input capability is already multimodal for PDF

Current OpenAI File Inputs documentation states that PDF files supplied as model file inputs are processed using both:

```text
extracted PDF text
+ an image of every PDF page
```

Both representations are supplied to vision-capable models. This is materially more complete than plain PDF text extraction and already matches the conceptual read + render pipeline ADS had been considering.

Official source:

```text
https://developers.openai.com/api/docs/guides/file-inputs
```

Evidence class: `A / OFFICIAL_DOCUMENTATION`.

Implication:

```text
ADS should not implement a second visual-understanding model pipeline.
If local authorized files can be safely handed into a native OpenAI file-input path,
that path is a primary reuse candidate.
```

## 3. Non-PDF Office files have different native semantics

The same official File Inputs guide distinguishes PDF from other document formats. For DOC/DOCX/PPT/PPTX and similar non-PDF files, the model receives extracted text rather than automatic page-image vision. The guide explicitly recommends converting to PDF when charts/diagrams/images matter. Spreadsheet inputs use spreadsheet-specific augmentation rather than generic document text extraction.

This argues against one generic flattened-text parser for every format.

Potential reuse routing is format-sensitive:

```text
PDF
    native OpenAI file input can already be text + page images

DOCX / PPTX when visuals matter
    convert/render through maintained document skill/runtime
    or convert to PDF before multimodal model inspection

XLSX
    preserve workbook/sheet/cell/formula semantics
    do not reduce to generic document text
```

Evidence class: `A / OFFICIAL_DOCUMENTATION`.

## 4. Current Codex App Server already understands image inputs

Current Codex App Server documentation/source exposes image/local-image turn inputs rather than requiring images to be flattened into text. Upstream Codex also has a `view_image` capability whose tests verify that a successful local image read becomes image model input and that sandbox-denied local images do not silently attach.

Official sources:

```text
https://developers.openai.com/codex/app-server
https://github.com/openai/codex/blob/main/codex-rs/core/tests/suite/view_image.rs
```

Evidence class: `A/B / OFFICIAL_DOCUMENTATION + OFFICIAL_SOURCE`.

Architectural implication:

```text
If ADS needs local visual inspection,
prefer an authority-bounded handoff into Codex/OpenAI's existing image input semantics
over inventing image reasoning inside Codexless.
```

The missing seam is therefore likely **authorized local media handoff**, not computer vision itself.

## 5. Installed Codex primary-runtime Skills already contain mature artifact workflows

A model-free live `codex.skill_list` / `codex.skill_read` probe on 2026-09-03 found current OpenAI primary-runtime skills on this machine for:

```text
pdf:pdf
    read / inspect / render / verify PDFs
    preferred visual workflow: render pages to PNG and inspect them
    uses Poppler + pdfplumber/pypdf-style extraction

documents:documents
    read/create/edit DOCX
    deterministic DOCX -> page PNG visual QA

presentations:Presentations
    read/create/edit PPTX
    render every final slide and visually inspect

spreadsheets:Spreadsheets
    read/analyze/edit XLSX/XLS/CSV/TSV
    preserves workbook values/formulas/objects and renders sheets/ranges for visual QA
```

This is strong current-machine evidence that OpenAI already maintains format-specific document/rendering workflows inside Codex. It materially changes the ADS roadmap.

Evidence class: `G / ADS LIVE CAPABILITY PROBE`.

Key conclusion:

```text
Do not build custom DOCX/PPTX/XLSX adapters by default.
First determine whether Codexless can safely expose/invoke the maintained Codex Skills
under the existing workspace authority model.
```

## 6. Mature third-party document systems are also reuse candidates

Three external ecosystems remain worth benchmarking when native OpenAI/Codex paths are insufficient.

### Microsoft MarkItDown

MarkItDown provides maintained conversion to Markdown across PDF, Word, PowerPoint, Excel and other formats and ships an MCP server.

Primary source:

```text
https://github.com/microsoft/markitdown
https://github.com/microsoft/markitdown/tree/main/packages/markitdown-mcp
```

Candidate role: lightweight semantic text/Markdown normalization.

### Docling

Docling targets richer document conversion including PDF layout, reading order, tables, formulas, images and OCR-oriented workflows across multiple formats; an MCP integration also exists.

Primary sources:

```text
https://github.com/docling-project/docling
https://github.com/docling-project/docling-mcp
```

Candidate role: sophisticated local structured-document fallback when native skills/file input are insufficient.

### PyMuPDF / PyMuPDF4LLM

PyMuPDF4LLM provides layout-aware Markdown/JSON-style extraction, page chunks, images/tables and optional OCR-oriented behavior on top of PyMuPDF.

Primary source:

```text
https://pymupdf.readthedocs.io/en/latest/pymupdf4llm/
```

Candidate role: stronger PDF-local extraction than bare PDF.js if a deterministic local converter is still useful.

Important licensing/dependency review remains required before any adoption. These are candidates, not accepted dependencies.

Evidence class: `B / PRIMARY PROJECT SOURCE` plus implementation comparison still pending.

## 7. Public Liyana Codexless remains a required reconciliation surface

Research 113/115 already make `liyana31811/Codexless` a primary comparator. Current document research retains that requirement:

```text
https://github.com/liyana31811/Codexless
https://github.com/liyana31811/Codexless/pulls
```

The relevant architectural principle is to avoid creating a parallel capability stack when upstream Codex already owns the capability. No current public document/PDF subsystem was found that ADS can simply adopt as-is, but the repository must remain part of final reconciliation before local divergence.

Evidence class: `B/E / PUBLIC SOURCE + OPEN PROPOSALS`.

## 8. Critical unresolved host question: MCP image output -> ChatGPT model vision

The Model Context Protocol supports image content in tool results, and OpenAI agent infrastructure can represent MCP image output as model image/tool output. However, that does not by itself prove the exact ChatGPT developer-MCP host projection used by ADS will expose returned MCP images to this conversation's model vision.

This exact host behavior must be experimentally proven rather than inferred from the protocol.

The preferred discriminating experiment is:

```text
1. use an existing or disposable low-risk MCP action that returns one unmistakable image content block
2. call it through a fresh ChatGPT developer-MCP projection
3. ask the model to report visual-only content that is absent from accompanying text/metadata
4. compare against the raw MCP response
5. classify:
       PASS  -> standard MCP image content is sufficient for visual local-page handoff
       FAIL  -> ChatGPT host does not expose it as model vision input
       AMBIGUOUS -> preserve limitation and do not build architecture on it
```

The current ADS Browser screenshot action would be an ideal reuse probe because it already returns MCP image content, but the local Browser status currently reports `chrome_skill_unavailable`. Browser repair is a separate capability issue and must not be performed merely to manufacture this document experiment.

## 9. Critical unresolved transport question: local authorized file -> native OpenAI file input

The OpenAI API already supports whole-file multimodal PDF processing, but ADS currently has no proven semantic path that converts:

```text
registered local workspace file
    -> current ChatGPT conversation's native file input
```

without either:

```text
manual upload
or
an additional model/API call
or
an unsupported host workaround
```

This transport seam deserves explicit research before `codex.document_render` is designed.

Potential directions:

```text
A. supported ChatGPT/MCP file-content or resource handoff if current host exposes one
B. authority-bounded upload into a native OpenAI file-input surface if product/API contract permits
C. Codex localImage / maintained Skill delegation, returning semantic findings to ChatGPT
D. standard MCP page-image output if end-to-end model visibility is proven
```

Do not implement a hidden second OpenAI API billing path merely to approximate native ChatGPT file handling without an explicit architectural decision.

## 10. Status of the existing `codex.document_read`

The new research does **not** invalidate Checkpoint 279.

Its accepted value remains:

```text
explicit workspace read authority
canonical path containment
bounded local bytes
no extra model call
pinned deterministic parser
page selection
SHA-256 / size / parser / page provenance
fail-closed media/authority handling
```

Its likely permanent role is now narrower:

```text
deterministic local text extraction + provenance
cheap preflight/fallback
possibly source evidence for higher-level document orchestration
```

rather than:

```text
foundation for a custom ADS parser/renderer/OCR implementation for every format
```

## 11. Architecture candidates after research

### Candidate A: Native/reuse-first orchestration - preferred research direction

```text
ADS workspace authority
    -> format/provenance preflight
    -> existing maintained native capability
         PDF: OpenAI file input or Codex PDF Skill
         image: Codex/localImage or standard MCP image if host-visible
         DOCX: Documents Skill
         PPTX: Presentations Skill
         XLSX: Spreadsheets Skill
    -> only custom adapter for an actual missing seam
```

Advantages:

```text
minimal duplicate parser/rendering code
benefits from upstream improvements
format-specific semantics retained
less maintenance and security surface
```

### Candidate B: Mature third-party converter behind ADS authority

Use MarkItDown/Docling/PyMuPDF4LLM only for gaps where native OpenAI/Codex workflows cannot satisfy deterministic local extraction, layout, OCR or structured conversion requirements.

### Candidate C: Custom ADS document stack

Continue custom `document_read`, `document_render`, `document_ocr`, Office adapters.

This remains a fallback architecture only. Research 117 currently finds insufficient justification to choose it before the reuse experiments complete.

## 12. Experiment plan

Run in this order:

```text
E117-1  MCP image visibility in ChatGPT host
E117-2  Codex maintained PDF Skill visual-read qualification on an authorized real PDF
E117-3  authority-bounded local image handoff through exact installed Codex App Server/localImage semantics
E117-4  compare PDF.js text baseline against one native/maintained richer path on representative annotated/math/table PDFs
E117-5  confirm DOCX/PPTX/XLSX routing through installed maintained Skills before considering adapters
E117-6  only if gaps remain, benchmark MarkItDown vs Docling vs PyMuPDF4LLM
```

Representative corpus should include:

```text
annotated lecture PDF
math/equation-heavy PDF
table/figure-heavy PDF
multi-column PDF
scanned/image-only page
DOCX with image/table
PPTX with visual slide
XLSX with formulas/chart
```

Measure:

```text
text fidelity
visual fidelity
layout/reading order
equation/table handling
OCR behavior
latency and memory
dependency/security footprint
provenance quality
authority containment
host/model handoff reliability
maintenance burden
```

## 13. Current disposition

```text
KEEP
    workspace-standard authority architecture
    live codex.document_read baseline
    deterministic provenance and fail-closed constraints

STOP FOR NOW
    custom codex.document_render implementation
    custom OCR subsystem
    custom DOCX/PPTX/XLSX adapters

INVESTIGATE FIRST
    native OpenAI PDF file-input multimodality
    installed Codex PDF/Documents/Presentations/Spreadsheets Skills
    App Server localImage/image semantics
    MCP image-result visibility in ChatGPT
    local-authorized-file -> native file-input handoff

BENCHMARK ONLY IF NEEDED
    MarkItDown
    Docling
    PyMuPDF4LLM
```

This is the current best reuse-first direction, not yet final architecture acceptance.
