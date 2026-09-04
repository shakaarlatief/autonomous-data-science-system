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

## 19. E117-4b publication-preflight result: sandboxed maintained PDF.js + canvas page rendering qualified

Validation 044 proved that maintained primary-runtime Poppler could rasterize PDF pages, but direct Poppler execution would have launched an untrusted-document parser with ordinary Codexless host identity. E117-4b therefore tested whether the existing Codex `command/exec` read-only sandbox could own the render execution instead.

Direct discrimination established:

```text
workspace write under :read-only      denied
ordinary %TEMP% write                 denied
managed runtime reads                 allowed
non-loopback TCP probe                denied / EACCES
loopback TCP                           available
```

Because the maintained primary runtime also contains `pdfjs-dist@5.6.205`, `@napi-rs/canvas@0.1.100`, and the matching Windows canvas package, Research 117 qualified an in-memory renderer child that needs no workspace or host-temp output:

```text
authorized PDF
    -> existing workspace read authority
    -> canonical containment + bounded source preflight
    -> existing Codex command/exec :read-only sandbox
    -> maintained primary-runtime PDF.js + canvas
    -> in-memory PNG page(s)
    -> bounded internal stdout protocol
    -> page/image/source provenance validation
    -> standard MCP image content
```

The candidate semantic surface is `codex.document_render`. Public inputs are only `cwd`, one bounded workspace-relative `documentPath`, and an ordered unique list of at most four 1-based pages. DPI is fixed at 150. The caller cannot select the executable, backend, arbitrary arguments, output path, permission profile, sandbox, Browser, Agent, OCR, Git, workspace identity override, write authority, or the larger internal renderer transport ceiling.

The internal stdout ceiling required for page-image base64 is exposed only inside `CodexAuthorityExecutor.exec`; the strict public `codex.command_exec` schema rejects the corresponding field. This therefore does not widen remote caller authority.

The first PDF.js sandbox probe exposed a standard-font path-resolution warning even though the managed font files existed and were readable. The issue was resolved by supplying normalized filesystem-path strings rather than `file://` URL strings to PDF.js' Node data factories. The corrected maintained renderer produced the synthetic visual probe without that warning. Host-side visual materialization of the same stack was inspected through `codex.image_read` and preserved the expected page headings, bars/rectangles, labels and diagonal geometry.

Qualification results:

```text
DOCUMENT_RENDER_REGRESSION=PASS tests=10
FLEXIBLE_AUTHORITY_REGRESSION=PASS tests=7
BOUNDED_GIT_FETCH_ORIGIN=PASS tools=54
BOUNDED_GIT_PULL_FF_ONLY=PASS tools=54
PUBLIC_SURFACE_REGISTRATION=PASS tools=54
IMAGE_READ_REGRESSION=PASS tests=7
DOCUMENT_RENDER_PUBLICATION_PREFLIGHT=PASS
PUBLIC_COMMAND_INTERNAL_OUTPUT_CAP_REMOTE_SCHEMA=REJECTED
EXPECTED_PUBLIC_SERVER_VERSION=0.1.1-preview.11
EXPECTED_PUBLIC_SURFACE_VERSION=codexless-public-preview-v2
EXPECTED_PUBLIC_TOOL_COUNT=54
MODEL_TURN_REQUIRED=false
NEW_EXTERNAL_DEPENDENCY=false
NO_LIVE_FILES_MODIFIED=true
```

This supersedes direct Poppler execution as the preferred semantic-seam candidate while retaining Checkpoint 285 as independent reuse evidence that the managed runtime already contained a viable renderer. Live publication remains separate because `%LOCALAPPDATA%\\Codexless` is intentionally outside ordinary workspace authority. The existing AB-002 / AB-017 authority work remains the future owner of that broader runtime-maintenance architecture; E117-4b does not solve it by widening workspace access.

Primary evidence: `docs/local_execution/validation/045_sandboxed_managed_pdf_render_publication_preflight_qualified.md` and Checkpoint 286.

## 20. E117-4d live result: sandboxed document rendering reaches ChatGPT vision

After successful host publication, the repository-authoritative controlled restart/reconnect sequence and ChatGPT app refresh completed. Live verification established Codexless `0.1.1-preview.11`, surface `codexless-public-preview-v2`, 54 tools, tunnel health/readiness HTTP 200, and preserved `codex.document_read` behavior.

A fresh disposable ChatGPT conversation then invoked only `codex.document_render` on the known two-page authorized PDF. It explicitly reported receiving actual PNG page images and recovered multiple visual-only facts from both pages that were absent from the prompt. It also reported the exact maintained renderer metadata: `pdfjs-dist@5.6.205`, `@napi-rs/canvas@0.1.100`, fixed 150 DPI, `codex-command-exec-read-only` isolation, `[1,2]` page selection and no OCR.

The fresh host classified:

```text
MCP_DOCUMENT_RENDER_TO_CHATGPT_VISION=PASS
```

The continuing Chat 17 session independently reproduced the live call, received both standard MCP page images, and visually confirmed the same page geometry and labels.

This closes the semantic PDF page-render transport question for the exact tested configuration:

```text
workspace-authorized PDF
    -> existing read authority
    -> bounded source validation
    -> Codex command/exec :read-only sandbox
    -> maintained PDF.js + canvas
    -> in-memory PNG page(s)
    -> standard MCP image content
    -> ChatGPT native vision
    -> PASS
```

No intermediate workspace image, Browser, OCR, extra image-read hop, new external dependency, or Codex model turn is required for the tested path.

Primary evidence: `docs/local_execution/validation/047_document_render_live_chatgpt_vision_qualified.md` and Checkpoint 288.

## 21. E117-5a representative result: Windows buffered command/exec transport ceiling localized

Representative real-document testing exposed a transport limitation that the smaller Checkpoint 288 qualification did not exercise.

Ordinary mathematical and text-heavy pages continue to pass. A dense page producing a 6.9 MiB PNG correctly fails the semantic 4 MiB page guard. However, an image-only cheat sheet, scanned/handwritten page, and dense theory sheet each render successfully through the maintained PDF.js + canvas stack to PNGs of roughly 1.16-1.23 MiB, yet live `codex.document_render` fails with `DOCUMENT_RENDER_PROTOCOL_ERROR / invalid JSON`.

The failure is now localized to buffered App Server transport rather than rendering fidelity. Current official Codex App Server documentation defines a 1 MiB default per-stream `command/exec` capture limit, while current Windows restricted-token source requires that default buffered cap and rejects custom output caps/streaming for that sandbox. Inspection of the preview.11 candidate found that its internal 11.75 MiB allowance was applied only after the App Server response and was never forwarded upstream. The fake regression executor therefore missed the real Windows cap.

Accepted claim scope is corrected to:

```text
ordinary/smaller page render -> ChatGPT vision     QUALIFIED
representative >1 MiB PNG stdout transport         NOT QUALIFIED
semantic 4 MiB page limit                          WORKING / FAIL-CLOSED
maintained PDF.js + canvas renderer                still preferred
OCR/fallback stack requirement                     NOT ESTABLISHED
```

A private ignored correction candidate now keeps command stdout as compact control JSON and transfers page bytes through a bounded authenticated parent-owned loopback binary channel. The parent generates a random 256-bit token and ephemeral `127.0.0.1` destination; the caller cannot select either. Aggregate/page/header limits and parent hash/signature/dimension verification remain bounded. Focused candidate unit regression passes 10 tests, but the cross-boundary Windows sandbox transport is not yet live-qualified and must not be published.

Primary evidence: `docs/local_execution/validation/048_representative_pdf_fidelity_exposes_windows_command_exec_capture_ceiling.md` and Checkpoint 289.

## 22. E117-5b result: first-party Chat PDF Skill makes native local-file handoff the next reuse-first experiment

The project owner surfaced the current first-party ChatGPT PDF plugin/Skill after Checkpoint 289 localized the page-image transport ceiling. Its router identifies PDF as a Skill and, in Chat, falls back to `/home/oai/skills/pdfs/SKILL.md`. The current Chat PDF Skill was read directly and is itself a mature render-first workflow covering visual review, extraction, OCR, preflight, editing, renderer comparison and verification. The installed Codex primary runtime separately exposes the maintained `pdf:pdf` Skill for local-machine PDFs.

This changes priority, not the evidence already accepted. ADS already owns the local Windows authority side:

```text
registered local workspace
    -> existing read capability
    -> canonical containment
    -> exact local bytes + provenance
```

The missing question is whether those exact authorized PDF bytes can cross the developer-MCP host boundary as a standard MCP PDF resource and be promoted into the same native PDF/file-input treatment available to an ordinary Chat attachment.

The exact installed MCP SDK used by Codexless supports both embedded resource content and resource links in tool results. A model-free schema probe accepted both an embedded `application/pdf` blob and an `application/pdf` `resource_link`. Current OpenAI documentation also confirms MCP-based ChatGPT apps, native model file inputs, and file/resource outputs, but it does not clearly specify the exact inbound promotion rule needed here. Therefore this remains an empirical host question rather than an inferred capability.

The existing ADS Browser upload path can already bind an authorized local file to a Chrome file chooser using canonical path, size and SHA-256. That is retained as a diagnostic/fallback, not the preferred architecture, because it depends on UI state and effectively automates manual upload.

The Checkpoint 289 authenticated loopback page-image transport candidate is consequently paused before publication. The preferred next experiment is the smaller semantic seam:

```text
authorized local PDF
    -> bounded ADS file reader
    -> standard MCP application/pdf resource
    -> ChatGPT host
    -> native PDF/file interpretation if supported
    -> first-party PDF capability
```

A private ignored candidate now implements only that authority/provenance reader and an embedded-resource result shape. Its focused reader regression passes 5 tests and candidate surface target is preview.12 / 55 tools. No live runtime file has been changed and no host claim is made yet.

The earlier temporary `tunnel_active_organization_required` observation is not attributed to the PDF plugin. The project owner clarified that the message originated from the phone; mobile/device connector behavior is already a separate deferred architecture topic.

Primary evidence: `docs/local_execution/validation/049_official_pdf_skill_local_ads_handoff_research_prioritized.md` and Checkpoint 290.

## 23. E117-5c result: bounded MCP PDF resource handoff candidate preflight-qualified

The minimal local-PDF handoff candidate is now publication-preflight qualified without changing the live preview.11 runtime.

Candidate action:

```text
codex.document_file_read
```

It accepts only `cwd` plus one bounded workspace-relative PDF path, requires existing workspace `read`, performs canonical containment and identity checks, enforces a conservative 4 MiB source limit, validates PDF bytes, records SHA-256/size/name/provenance, and returns the exact source bytes as standard MCP embedded `application/pdf` resource content. It starts no model turn and uses no parser, renderer, OCR, Browser, Git, write authority, upload destination or external API.

The exact installed MCP SDK accepts the candidate embedded-resource shape. Integrated staging from live preview.11 plus only the file-handoff overlay passed:

```text
DOCUMENT_FILE_READ_REGRESSION=PASS tests=5
BOUNDED_GIT_FETCH_ORIGIN=PASS tools=55
BOUNDED_GIT_PULL_FF_ONLY=PASS tools=55
PUBLIC_SURFACE_REGISTRATION=PASS tools=55
IMAGE_READ_REGRESSION=PASS tests=7
DOCUMENT_RENDER_REGRESSION=PASS tests=10
DOCUMENT_FILE_HANDOFF_PUBLICATION_PREFLIGHT=PASS
EXPECTED_PUBLIC_SERVER_VERSION=0.1.1-preview.12
EXPECTED_PUBLIC_SURFACE_VERSION=codexless-public-preview-v2
EXPECTED_PUBLIC_TOOL_COUNT=55
PAUSED_LOOPBACK_RENDER_TRANSPORT_OVERLAID=false
NO_LIVE_FILES_MODIFIED=true
```

The staging helper explicitly pins the live preview.11 hashes of `codex-authority-executor.mjs`, `document-renderer.mjs`, `document-render-child.mjs`, and the live document-render regression. Those paused loopback-transport files are not part of the preview.12 overlay.

The live process remains preview.11 / 54 tools and `codex.document_read` still returns `SANDBOX` through `pdfjs-dist@5.4.624` with OCR false.

The critical host question therefore remains cleanly isolated: after guarded publication/restart/schema refresh, does ChatGPT treat the returned MCP PDF resource as an actual native PDF/file input that can feed the first-party PDF capability? No answer is inferred before that host experiment.

Primary evidence: `docs/local_execution/validation/050_document_file_handoff_publication_preflight_qualified.md` and Checkpoint 291.

## 24. E117-5d live result: MCP PDF resource materializes attachment but not same-turn native PDF input

After guarded preview.12 publication, controlled restart, and ChatGPT app refresh, live Codexless reported `0.1.1-preview.12` / `codexless-public-preview-v2` / 55 tools. The existing `codex.document_read` smoke remained valid. A corrected `codex.document_render` smoke against `docs/local_execution/validation/generated/e117_managed_poppler_probe/probe.pdf` also succeeded, confirming that the earlier post-refresh render failure was only an incorrect test path and not a preview.12 regression.

The new `codex.document_file_read` host experiment then produced two distinct results.

First, a representative 1,679,081-byte `CheatSheet_A4.pdf` repeatedly triggered the ChatGPT UI error `maximum chat length is reached` in fresh chats that could immediately answer an ordinary `hello`. Its inline base64 representation is approximately 2.24 million characters before protocol overhead. The exact host limit is unknown, but the inline embedded-resource approach is not viable for representative files as tested.

Second, a tiny 2,372-byte two-page `probe.pdf` succeeded. The host visibly materialized the MCP-returned PDF as a `probe.pdf` attachment/file card in the conversation. However, the same assistant turn explicitly did not receive parsed PDF content, rendered pages, or a native visual representation in model context and therefore could not report content/layout facts. The exact host verdict was:

```text
MCP_PDF_RESOURCE_TO_CHATGPT_NATIVE_PDF=FAIL
```

The important corrected decomposition is therefore:

```text
ADS exact local PDF bytes -> MCP application/pdf resource       PASS
ChatGPT host file/attachment materialization                    PASS
same-turn automatic native PDF model promotion                  FAIL
representative inline-base64 embedded-resource transport         FAIL AS TESTED
```

This still leaves one smaller reuse-first question open because the host created a file attachment artifact. Before resuming the paused loopback renderer transport, test whether the first-party PDF Skill can consume that already-materialized `probe.pdf` in the **next turn of the same disposable conversation**. That requires no ADS code change, restart, or schema refresh.

If next-turn first-party PDF consumption passes, the remaining transport problem becomes avoiding inline binary payloads for representative files, with a server-owned MCP `resource_link` plus resource-read route the next candidate. If it fails, the materialized file card is not a usable bridge into first-party PDF understanding.

Primary evidence: `docs/local_execution/validation/051_mcp_pdf_resource_materializes_attachment_but_not_same_turn_native_pdf.md` and Checkpoint 292.

## 25. E117-5e claim correction: next-turn native PDF access passed, explicit PDF-plugin invocation remains unproven

The follow-up conversation visibly showed the user's `@PDF` text as ordinary prompt text rather than a confirmed plugin/source pill. The returned answer nevertheless recovered the exact two-page visual facts from `probe.pdf` after that PDF had been materialized by the preceding ADS tool turn.

The accepted conclusion is therefore narrower and stronger in the right place:

```text
MCP-returned PDF -> host attachment/file materialization          PASS
same-turn native PDF model access                               FAIL
next-turn normal ChatGPT inspection of materialized PDF          PASS
explicit user-visible @PDF plugin invocation                     UNPROVEN
PDF Skill/plugin required for the successful next-turn read      NOT ESTABLISHED
```

Current OpenAI product documentation distinguishes Skills from native file handling: Skills are reusable workflows/instructions and can be used automatically when helpful; plugins may package Skills and can also be explicitly selected or @-mentioned when available. Separately, OpenAI models support PDF/file inputs directly. Therefore the observed next-turn success must not be attributed specifically to the visible PDF plugin unless that invocation is independently proven.

For Research 117, the important architectural result is that the ChatGPT host-created PDF attachment becomes readable/visually inspectable on a subsequent turn without another ADS read/render call. This is enough to keep the two-stage local-authority -> host attachment -> native ChatGPT PDF handling route alive even if the PDF plugin itself was not invoked.

The next transport question remains unchanged: avoid multi-megabyte inline base64 for representative PDFs. Test server-owned `resource_link` plus resource-fetch/materialization semantics before resuming the paused loopback renderer transport.

## 26. E117-5f publication-preflight result: MCP resource-link PDF transport qualified locally

Checkpoint 292 narrowed the full-PDF problem to transport. The tiny embedded MCP PDF became a ChatGPT-side attachment and was fully inspectable on the next turn, including automatic use of the built-in PDF Skill and its renderer-parity workflow. The representative 1.68 MiB cheat sheet, however, expands to roughly 2.24 million base64 characters inside the embedded-resource tool result and repeatedly hit the host's misleading `maximum chat length is reached` failure.

E117-5f therefore changes only the transport envelope. The new candidate `codex.document_file_link` reuses the already-qualified `DocumentFileReader` authority/provenance path but returns a small MCP `resource_link` rather than embedding the PDF bytes in the tool result. A runtime-scoped, process-local resource store owns an opaque 256-bit-random `codexless://document-resource/<token>` URI, keeps at most eight prepared PDFs for fifteen minutes, and serves the exact PDF bytes only through the standard MCP `resources/read` callback. The caller cannot select the resource URI.

Integrated staging passed:

```text
DOCUMENT_RESOURCE_LINK_REGRESSION=PASS tests=8
DOCUMENT_FILE_READ_REGRESSION=PASS tests=5
BOUNDED_GIT_FETCH_ORIGIN=PASS tools=56
BOUNDED_GIT_PULL_FF_ONLY=PASS tools=56
PUBLIC_SURFACE_REGISTRATION=PASS tools=56
IMAGE_READ_REGRESSION=PASS tests=7
DOCUMENT_RENDER_REGRESSION=PASS tests=10
DOCUMENT_RESOURCE_LINK_PUBLICATION_PREFLIGHT=PASS
EXPECTED_PUBLIC_SERVER_VERSION=0.1.1-preview.13
EXPECTED_PUBLIC_SURFACE_VERSION=codexless-public-preview-v2
EXPECTED_PUBLIC_TOOL_COUNT=56
TOOL_RESULT_CONTENT=resource_link/application-pdf
RESOURCE_READ_CONTENT=blob/application-pdf
TOOL_RESULT_EMBEDS_PDF_BYTES=false
MODEL_TURN_REQUIRED=false
BROWSER_REQUIRED=false
NEW_EXTERNAL_DEPENDENCY=false
PAUSED_LOOPBACK_RENDER_TRANSPORT_OVERLAID=false
NO_LIVE_FILES_MODIFIED=true
```

The candidate also verifies the registered MCP `ResourceTemplate` callback directly, not only the tool-result schema. It preserves the existing embedded `codex.document_file_read` route for A/B evidence and does not overlay the paused Checkpoint 289 loopback-render transport.

The decisive host behavior remains unproven. A separate `resources/read` response still carries the PDF as base64 on the MCP wire, so Research 117 must not assume that ChatGPT handles it as an out-of-band file transfer. After guarded publication/restart/schema refresh, the live experiment must determine whether ChatGPT actually follows the resource link, materializes the PDF and avoids the representative inline-tool-result failure. If that route fails or is materially inferior, the next primary whole-PDF experiment is ADS Browser upload into ChatGPT's normal file-input control.

Primary evidence: `docs/local_execution/validation/052_mcp_pdf_resource_link_publication_preflight_qualified.md` and Checkpoint 293.

## 27. Current disposition

```text
KEEP
    workspace-standard authority architecture
    live codex.document_read baseline
    live codex.image_read -> ChatGPT vision path
    maintained primary-runtime PDF.js + canvas as the accepted renderer for qualified ordinary pages
    Checkpoint 288 direct ChatGPT page-vision path within its tested smaller-page scope
    managed Poppler as independent reuse evidence / fallback comparator
    deterministic provenance and fail-closed constraints

STOP FOR NOW
    custom PDF rendering engine
    custom OCR subsystem
    custom DOCX/PPTX/XLSX adapters

INVESTIGATE FIRST
    codex.document_file_link -> MCP resource_link/resources-read -> ChatGPT whole-PDF materialization
    if resource_link fails/inferior: ADS Browser -> normal ChatGPT file upload
    native OpenAI PDF file-input multimodality only if a separate API path is explicitly accepted

KEEP AS SUPPORTING / FALLBACK
    installed Codex PDF/Documents/Presentations/Spreadsheets Skills
    document/page representation -> already-qualified native image path

PAUSE UNTIL WHOLE-PDF HANDOFF RESULT
    authenticated parent-owned loopback binary transfer across actual Windows :read-only sandbox

BENCHMARK ONLY IF NEEDED
    MarkItDown
    Docling
    PyMuPDF4LLM
```

This is the current best reuse-first direction, not yet final architecture acceptance.
