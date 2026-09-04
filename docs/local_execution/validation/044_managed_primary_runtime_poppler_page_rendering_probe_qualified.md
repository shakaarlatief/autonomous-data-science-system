# Validation 044: Managed Primary Runtime Poppler Page Rendering Probe Qualified

**Date:** 2026-09-04
**Status:** PASS / MANAGED RENDERER PATH QUALIFIED FOR BOUNDED PROBE
**Research:** Research 117
**Experiment:** E117-4a prerequisite
**Workspace:** `ads-public`
**Runtime:** OpenAI Codex primary runtime dependency bundle

## Purpose

Determine whether the current maintained OpenAI/Codex primary runtime already contains a usable PDF page renderer that Research 117 can reuse, rather than installing a separate system renderer or implementing a custom rendering engine.

This is a prerequisite probe for the broader representative-document comparison planned by E117-4. It does not by itself qualify complex annotated, mathematical, scanned, or table-heavy PDF fidelity.

## Maintained runtime discovery

The installed OpenAI Spreadsheets Skill explicitly documents the fallback dependency root:

```text
~/.cache/codex-runtimes/codex-primary-runtime/dependencies/
```

The installed Documents Skill also shows that maintained artifact helpers expect a Codex primary-runtime dependency tree and prepend `dependencies/bin/override` when the helper is run from the managed runtime.

A model-free read-only probe of the documented dependency root established:

```text
managed dependency root                       PRESENT
managed Python runtime                        PRESENT
dependencies/bin/override                     PRESENT
pdftoppm in bin/override                      MISSING
pdfinfo in bin/override                       MISSING
```

A narrower search inside that exact maintained dependency root then found the real Poppler binaries at:

```text
dependencies/native/poppler/Library/bin/pdftoppm.exe
dependencies/native/poppler/Library/bin/pdfinfo.exe
```

The installed `pdf:pdf` Skill package itself contains no bundled `pdftoppm.exe` and no renderer helper script. Therefore the earlier E117-2 failure did not prove that the maintained OpenAI runtime lacked Poppler. It proved that the bounded Codex PDF Skill turn did not resolve the managed native Poppler location and instead encountered the unrelated MiKTeX `pdftoppm` stub available through the ordinary host path.

## Managed renderer identity

Direct version/hash inspection returned:

```text
pdftoppm version     26.07.0
pdftoppm size        65840 bytes
pdftoppm SHA-256     62AE48206406FDF70A0073A26CFA4C95F14FCC750FE3391FFFBD4B706CEC7F6B
pdfinfo size         81712 bytes
pdfinfo SHA-256      3461C4882912AEFA23ED4755D61587B4E4C4AD619C1CF87CF1B203E8EF95360B
```

The managed Python runtime at the same dependency boundary has:

```text
reportlab    PRESENT
pypdf        PRESENT
pdfplumber   PRESENT
pdf2image    PRESENT
fitz         ABSENT
pymupdf      ABSENT
```

This is reuse evidence for the maintained Poppler path and does not adopt PyMuPDF or another new dependency.

## End-to-end bounded probe

A temporary two-page PDF was generated inside the existing ignored validation `generated/` area of the authorized ADS workspace. It used ordinary Helvetica text plus simple vector shapes so rendering correctness could be visually checked without introducing another external source or dependency.

Source PDF:

```text
size      2372 bytes
SHA-256   8B2B16CB65826E0F1D4EE47AF8801FA7530BACCDDC94E20EF3DFD52336A5A21F
```

The exact managed `pdftoppm.exe` was invoked directly at 150 DPI. It exited `0` and produced:

```text
page-1.png   30461 bytes   SHA-256 4CC4BE5E63D1EDB97783CB89451887AE81116E057B7C9DB172D107553C3DCFDA
page-2.png   26705 bytes   SHA-256 A5A7B55ED9CB972150C0179343D0426B28725A0D565D8C33E114BC2B7533834F
```

Poppler emitted two warnings:

```text
Syntax Error: No display font for 'Symbol'
Syntax Error: No display font for 'ArialUnicode'
```

Those warnings did not prevent the simple test document from rendering correctly, but they are material evidence that representative font/math/annotation coverage still needs qualification before stronger fidelity claims are made.

## Direct visual inspection

Both rendered pages were then passed through the already-qualified model-free `codex.image_read` path.

The returned image content visibly showed:

```text
page 1
    "MANAGED POPPLER PROBE"
    three stacked colored rectangles
    a diagonal line
    "PAGE 1"

page 2
    "SECOND PAGE CHECK"
    five bars increasing left to right
    "PAGE 2"
```

This proves the bounded pipeline:

```text
authorized PDF bytes
    -> maintained Codex primary-runtime Poppler
    -> PNG page representation
    -> codex.image_read
    -> ChatGPT native vision
```

for the exact simple test case.

## Runtime metadata

The maintained runtime root also exposes `runtime.json` with:

```text
bundleFormatVersion  2
bundleVersion        26.903.11726
targetPlatform       win32
targetArch           x64
pythonVersion        3.12.14
nodeVersion          v24.19.0
nativeDependencies   includes poppler
libreOfficeVersion   null
```

This gives a machine-readable runtime identity that is stronger than guessing from PATH. The installed Skills also explicitly state that `load_workspace_dependencies` is the preferred dependency-resolution mechanism and that the documented cache root is the fallback when that loader is unavailable. The current Codexless public surface does not expose a `load_workspace_dependencies` action, so any future wrapper must either reuse an upstream-supported resolver indirectly or fail visibly against the documented runtime manifest rather than silently hard-code an unverified binary path.

## Result

```text
PRIMARY_RUNTIME_POPPLER_PRESENT          PASS
PRIMARY_RUNTIME_POPPLER_EXECUTABLE      PASS
MODEL_FREE_PDF_TO_PNG_RENDER            PASS
MULTI_PAGE_OUTPUT                       PASS
PNG_TO_CHATGPT_VISION                    PASS
SYSTEM_POPPLER_INSTALL_REQUIRED          false
CUSTOM_RENDER_ENGINE_REQUIRED            false
REPRESENTATIVE_COMPLEX_PDF_FIDELITY      NOT YET QUALIFIED
READ_ONLY_SEMANTIC_RENDER_SEAM           STILL MISSING
```

## Architectural interpretation

The document problem is narrower again. ADS does not currently need to install another PDF renderer or implement PDF rasterization logic itself. The maintained OpenAI/Codex primary runtime already carries Poppler.

The missing reusable seam is now approximately:

```text
workspace-authorized PDF
    -> resolve maintained runtime dependency safely
    -> render selected page(s) in bounded temporary storage
    -> return standard MCP image content directly
    -> preserve source/render provenance
```

A future semantic tool may reasonably be named `codex.document_render`, but if implemented it should be a thin authority/provenance wrapper around the maintained renderer, not a custom PDF rendering engine. It should not expose arbitrary executable paths, arbitrary output destinations, shell arguments, or require caller-visible workspace write authority merely to inspect a document.

The runtime dependency location must be resolved through a maintained loader/runtime contract when available, with `runtime.json` and the documented fallback root treated as explicit compatibility evidence rather than an opaque path assumption.

## Scope limits

This validation does not establish:

```text
complex mathematical PDF fidelity
annotation rendering fidelity
embedded-font completeness
scanned-document OCR
large-document memory/latency bounds
page-selection API design
stable cross-version runtime-dependency resolution
DOCX/PPTX/XLSX rendering
```

Those remain Research 117 work.

## Qualification result

```text
RESEARCH_117_E117_4A=PASS
MANAGED_PRIMARY_RUNTIME_POPPLER=QUALIFIED_FOR_BOUNDED_PROBE
NEXT=design the smallest read-only semantic page-render seam around maintained Poppler and then run representative PDF fidelity qualification
```
