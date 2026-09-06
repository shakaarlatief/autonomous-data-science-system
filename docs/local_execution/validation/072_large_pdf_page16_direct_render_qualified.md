# Validation 072: Large-PDF Page 16 Direct Render Qualified

**Date:** 2026-09-06
**Status:** PASS / LARGE-SOURCE PAGE RENDER REACHES CHATGPT DIRECTLY
**Research:** Research 117 / Research 119
**Scope:** End-to-end qualification of the Checkpoint 313 renderer-only large-source admission change against the real read-only Machine Learning source after the controlled Codexless/tunnel restart.

## Test target

```text
workspace
    machine-learning

cwd
    C:\School\Machine Learning

document
    51.Deep Learning2.annotated.pdf

source size
    78,874,939 bytes

page count
    56

selected page
    16
```

Checkpoint 312 had already established that page 16 serializes as a 15,944,609-byte one-page native PDF, so native page-range splitting cannot conservatively transport this page under the known ChatGPT whole-PDF host envelope.

## Execution path

After the user completed the canonical controlled Codexless/tunnel restart from `docs/local_execution/OPERATIONS.md`, ChatGPT invoked the already-existing public tool with no Plugin refresh:

```text
codex.document_render
cwd          C:\School\Machine Learning
documentPath 51.Deep Learning2.annotated.pdf
pages        [16]
```

No new tool schema was required.

The live tool succeeded under the existing read-only Machine Learning workspace authority and returned standard MCP image content directly to ChatGPT.

## Direct execution evidence

```text
schemaVersion
    codexless.document-render.v1

workspaceId
    machine-learning

source relativePath
    51.Deep Learning2.annotated.pdf

source mediaType
    application/pdf

source SHA-256
    3872d5b3957d4313ab154a8405222d47098dda50657b660330ea0eecdce24110

source size
    78,874,939 bytes

renderer
    pdfjs-dist + @napi-rs/canvas

isolation
    codex-command-exec-read-only

DPI
    150

permissionProfile
    :read-only

pageCount
    56

selectedPages
    [16]

OCR
    false
```

Returned page image:

```text
pageNumber
    16

mediaType
    image/png

width
    1240

height
    1755

sizeBytes
    583,130

SHA-256
    aca9cfadbfcb99382e22a2472495f26d1ab097922ce9406d66a8121810a56023
```

The live returned PNG hash is exactly the same as the pre-restart model-free feasibility probe from Validation 071.

## ChatGPT-native visual inspection

The returned MCP image was visible to ChatGPT itself and was inspected without OCR or a reasoning-model intermediary.

Concrete visible page features include:

```text
- a top section with the sentence "It doesn't always work perfectly, though.";
- a side-by-side image showing a person riding a horse and a stylized/zebra-like transformed version;
- a middle slide titled "StyleGAN (2018)" with a generator architecture diagram;
- labels in that diagram including "latent vector" and "per-layer noise";
- explanatory text on the right describing StyleGAN and the use of latent vectors at multiple layers;
- a lower slide titled "changing the latent vector";
- a grid of generated face examples on the left of that lower slide;
- explanatory text on the right discussing source and destination latent vectors and how changing layers affects features.
```

This visual inspection is direct ChatGPT evidence from the returned image, not information reconstructed from prior text extraction.

## Qualification result

This closes the exact Checkpoint 313 pending experiment:

```text
78,874,939-byte authorized local PDF
    -> existing machine-learning read authority
    -> Codexless document_render
    -> bounded model-free PDF.js + canvas render
    -> 583,130-byte standard MCP PNG
    -> ChatGPT native vision
```

No source file was copied into the ChatGPT conversation as a whole attachment, but ChatGPT directly received a faithful model-free visual representation of the requested page. No Browser upload, OCR, semantic worker, Codex reasoning turn, source-workspace write, or manual file upload was used.

## What this proves and does not prove

Proven:

```text
- the old 32 MiB render-source admission ceiling was not fundamental;
- authorized PDFs up to the new 96 MiB renderer ceiling can be page-rendered directly when the selected render itself remains within the existing PNG ceilings;
- oversized native single pages can still be exposed directly to ChatGPT visually without a semantic intermediary;
- the Machine Learning workspace can remain read-only;
- same-chat qualification works after restart because the public tool schema did not change.
```

Not yet proven:

```text
- every page in every <=96 MiB PDF will fit under the current 4 MiB per-page PNG ceiling;
- direct embedded-text extraction from >32 MiB PDFs through codex.document_read;
- a unified automatic hybrid dispatcher choosing native whole file vs native split vs large-source page render/text;
- direct whole-file DOCX/PPTX/XLSX handoff.
```

## Private runtime preservation

The private local-runtime candidate was updated from pending to qualified and synchronized to `origin/main` at:

```text
889148f7263bb4ce9baddf52ce079a3bc2c943db
RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
postflightOk=true
```

## Result

```text
LARGE_PDF_PAGE16_DIRECT_RENDER = PASS
SOURCE_BYTES = 78874939
PAGE16_NATIVE_PDF_BYTES = 15944609
PAGE16_RENDER_BYTES = 583130
PAGE16_RENDER_SHA256 = aca9cfadbfcb99382e22a2472495f26d1ab097922ce9406d66a8121810a56023
CHATGPT_NATIVE_VISUAL_INSPECTION = PASS
SOURCE_WORKSPACE_WRITE = NONE
MANUAL_UPLOAD = NONE
BROWSER = NONE
OCR = NONE
REASONING_MODEL_INTERMEDIARY = NONE
NEXT = GENERALIZE_HYBRID_DIRECT_SOURCE_POLICY_AND_TEXT_PATH
```
