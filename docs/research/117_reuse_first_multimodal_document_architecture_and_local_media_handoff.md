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

## 13. E117-2 live result: maintained Codex PDF Skill routed, visual render blocked

The first live reuse experiment is now complete. The `big-data-statistics` workspace was deliberately widened from `read` to `read + agent` only. Registry revision advanced to `4` with content hash `2960f0b113550301a692470b0f2ff527317812550b6d3ae7cd2e519c94ad9e80`; no write/browser/Git capability was added.

A bounded Codex turn on page 1 of `BDS-exam-24-25-solutions.pdf` successfully routed the maintained OpenAI PDF Skill. The visual inspection itself did not complete because the local renderer path was unavailable: the discovered Poppler executable was an uninitialized MiKTeX stub and no alternative renderer was available under the no-modification constraint. No source file was modified and no visual fact was invented.

This changes the evidence, but not the reuse-first conclusion:

```text
maintained PDF Skill exists and routes        proven
current-machine visual renderer is ready      not proven / blocked
custom ADS renderer is therefore necessary    not established
```

Primary evidence: `docs/local_execution/validation/040_codex_pdf_skill_visual_read_reuse_experiment.md`.

## 14. E117-3 live result: native Codex local-image vision qualified

A second bounded live experiment tested an existing authorized repository PNG through the exact installed Codex native image path. Codex used its maintained `view_image` capability and visually inspected the image successfully. It reported a concrete visual-only fact from the screenshot and required no file copy, conversion, render step, OCR path, or custom script. No authority or sandbox blocker occurred.

This is decisive positive reuse evidence for the downstream visual stage:

```text
existing authorized local image
    -> Codex native view_image / local image input
    -> model vision
    -> visual reasoning
```

Therefore Research 117 should not design a separate ADS image-understanding subsystem. The unresolved document problem is now narrower: obtain an authorized page/image representation from a PDF or other visually meaningful document and hand that representation to the already-working native image path.

Primary evidence: `docs/local_execution/validation/041_codex_native_local_image_view_qualified.md`.

## 15. E117-1 direct ChatGPT-host MCP image experiment is currently blocked by Browser compatibility state

The existing `codex.browser_screenshot` tool is already ideal for the direct host experiment because it returns a standard MCP image content block rather than base64 inside JSON. A fresh model-free `codex.browser_status` probe on 2026-09-03 returned:

```text
status: unavailable
reason: chrome_skill_unavailable
chromeSkill: missing
```

Therefore Research 117 cannot yet use the current Browser screenshot action to prove whether this ChatGPT developer-MCP host exposes MCP image content directly to the current ChatGPT model. This is a Browser compatibility/runtime state issue, not evidence for or against MCP image visibility itself.

The maintained `codexless-browser-repair` Skill was re-read. It requires model-free compatibility evidence first and explicitly forbids using private workarounds or broad authority changes merely to restore Browser. Research 117 should therefore diagnose the current Browser compatibility state through the governed repair path before any screenshot-based E117-1 test. No Browser repair has yet been accepted by this research record.

Current official evidence also confirms the architectural possibility but not the exact ChatGPT-host behavior:

```text
MCP tool results can contain ImageContent
OpenAI Responses/function outputs can carry image/file content
OpenAI native model inputs accept image and file inputs
```

The exact end-to-end ChatGPT developer-MCP projection remains an empirical host question.

## 16. E117-1 direct-host image bridge candidate is preflight-qualified

Because Browser is unavailable, Research 117 prepared the narrower generic seam required to test the actual host question without another Codex model turn: `codex.image_read`.

The candidate requires only existing workspace `read`, accepts one bounded workspace-relative PNG/JPEG/WebP, reuses the same canonical containment and file-identity principles as the document reader, records SHA-256 provenance, and returns the image as standard MCP `image` content plus compact metadata. It does not start a model turn, OCR, render, browse, mutate, use Git, or externally upload the file.

Qualification results:

```text
IMAGE_READ_REGRESSION=PASS tests=7
FLEXIBLE_AUTHORITY_REGRESSION=PASS tests=7
BOUNDED_GIT_FETCH_ORIGIN=PASS tools=53
BOUNDED_GIT_PULL_FF_ONLY=PASS tools=53
PUBLIC_SURFACE_REGISTRATION=PASS tools=53
IMAGE_READ_PUBLICATION_PREFLIGHT=PASS
EXPECTED_PUBLIC_SERVER_VERSION=0.1.1-preview.10
EXPECTED_PUBLIC_SURFACE_VERSION=codexless-public-preview-v2
EXPECTED_PUBLIC_TOOL_COUNT=53
MODEL_TURN_REQUIRED=false
NEW_EXTERNAL_DEPENDENCY=false
NO_LIVE_FILES_MODIFIED=true
```

A guarded live-publication attempt through ordinary `codex.command_exec` was blocked when that sandbox attempted to write `%LOCALAPPDATA%\\Codexless`. Post-failure hashes proved the live runtime remained exactly on preview.9 / 52 tools, `image-reader.mjs` remained absent, and no temporary publication residue remained. This is an authority-boundary result rather than a candidate failure.

The exact next step is a host PowerShell run of the guarded helper, followed by controlled restart/reconnect/schema refresh and a fresh disposable ChatGPT test. Only a visual-only fact from `codex.image_read` may establish that this ChatGPT developer-MCP host routes MCP image content into model vision.

Primary evidence: `docs/local_execution/validation/042_model_free_mcp_image_bridge_publication_preflight_qualified.md`.

## 17. E117-1 live result: direct ChatGPT-host MCP image vision qualified

The guarded `codex.image_read` candidate was published successfully through the host-state publication helper, followed by the repository-authoritative controlled restart/reconnect sequence and ChatGPT developer-MCP refresh. Read-only post-restart verification established live Codexless `0.1.1-preview.10`, surface `codexless-public-preview-v2`, 53 public tools, the expected ADS `defaultCwd`, tunnel `/healthz` HTTP 200, and tunnel `/readyz` HTTP 200. The refreshed ChatGPT tool projection exposes both `codex.image_read` and the preserved `codex.document_read` action.

A fresh disposable ChatGPT conversation then called only `codex.image_read` against the authorized repository PNG `frontend/e2e/visual.spec.ts-snapshots/overview-light-chromium-linux.png`. The prompt deliberately withheld the expected visual facts and prohibited Codex agent turns, Browser, OCR, shell execution, repository reads, web search, metadata inference, filename inference, and prior-knowledge substitution.

The fresh conversation explicitly reported receiving actual visual image content rather than only metadata/text and recovered multiple pixel-derived facts, including the `Customer Churn Prediction` dashboard, the right-side `What matters now` panel, the pale-orange `APPROVAL REQUIRED` card for `Missingness pattern investigation`, its `Approve & run` / `Reject` controls, and multiple `Runs & activity` states. Validation 041 had independently inspected the same image through Codex native `view_image` and already identified the same dashboard plus the right-side approval panel.

The exact host classification is therefore:

```text
MCP_IMAGE_TO_CHATGPT_VISION=PASS
MODEL_FREE_MCP_IMAGE_BRIDGE=LIVE_QUALIFIED
EXTRA_CODEX_MODEL_TURN_REQUIRED=false
BROWSER_REQUIRED=false
OCR_REQUIRED=false
CUSTOM_IMAGE_UNDERSTANDING_REQUIRED=false
```

This closes the unresolved E117-1 host question. Standard MCP image content returned by the bounded read-only `codex.image_read` path is sufficient for direct ChatGPT model vision in the exact tested developer-MCP host configuration.

Primary evidence: `docs/local_execution/validation/043_model_free_mcp_image_bridge_live_chatgpt_vision_qualified.md` and Checkpoint 284.

## 18. E117-4a live result: maintained primary-runtime Poppler page rendering qualified

The next reuse-first probe found that the maintained OpenAI/Codex primary runtime already contains a usable Poppler installation even though `pdftoppm` is absent from the ordinary host PATH and from `dependencies/bin/override`.

The installed primary-runtime Skills explicitly document `load_workspace_dependencies` as the preferred dependency resolver and `~/.cache/codex-runtimes/codex-primary-runtime/dependencies/` as the fallback when that loader is unavailable. The current Codexless public surface does not expose a `load_workspace_dependencies` action. Read-only inspection of the documented fallback root found Poppler `26.07.0` under `dependencies/native/poppler/Library/bin/`, and `runtime.json` independently lists `poppler` among the managed native dependencies for bundle `26.903.11726`.

A bounded two-page PDF probe was rendered model-free with the exact managed `pdftoppm.exe` at 150 DPI. It exited `0`, produced two PNG pages, and both pages were then visually inspected through the already-qualified `codex.image_read` path. The expected text, colored rectangles, diagonal line, and increasing bar geometry were visible.

This establishes the exact simple-case pipeline:

```text
authorized PDF bytes
    -> maintained OpenAI/Codex primary-runtime Poppler
    -> PNG page representation
    -> codex.image_read
    -> ChatGPT native vision
    -> PASS
```

Poppler emitted missing-display-font warnings for `Symbol` and `ArialUnicode`. They did not affect the synthetic probe, but they prevent a stronger representative-document fidelity claim until annotated/math/table/multi-column/scanned cases are tested.

Validation 040 therefore remains a valid execution result but must be interpreted narrowly: its Codex turn found an unusable MiKTeX `pdftoppm` stub and did not discover the managed primary-runtime Poppler path. It is no longer evidence that a separate Poppler installation is required.

The architectural gap is now a thin semantic seam rather than a rendering engine:

```text
workspace-authorized PDF
    -> supported managed-runtime resolution
    -> bounded selected-page rendering
    -> standard MCP image content
    -> source/render provenance
```

Primary evidence: `docs/local_execution/validation/044_managed_primary_runtime_poppler_page_rendering_probe_qualified.md` and Checkpoint 285.

## 19. Current disposition

```text
KEEP
    workspace-standard authority architecture
    live codex.document_read baseline
    live codex.image_read -> ChatGPT vision path
    maintained primary-runtime Poppler as the current PDF page-render reuse candidate
    deterministic provenance and fail-closed constraints

STOP FOR NOW
    custom codex.document_render implementation
    custom OCR subsystem
    custom DOCX/PPTX/XLSX adapters

INVESTIGATE FIRST
    native OpenAI PDF file-input multimodality
    installed Codex PDF/Documents/Presentations/Spreadsheets Skills
    document/page representation -> already-qualified native image path
    local-authorized-file -> native file-input handoff

BENCHMARK ONLY IF NEEDED
    MarkItDown
    Docling
    PyMuPDF4LLM
```

This is the current best reuse-first direction, not yet final architecture acceptance.
