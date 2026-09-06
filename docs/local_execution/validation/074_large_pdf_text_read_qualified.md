# Validation 074: Large-PDF Text Read Qualified

**Date:** 2026-09-06
**Status:** PASS / LARGE-SOURCE EMBEDDED TEXT REACHES CHATGPT DIRECTLY
**Research:** Research 117 / Research 119
**Scope:** End-to-end qualification of the Checkpoint 315 `codex.document_read` 96 MiB source-admission change against the real read-only Machine Learning source after the controlled Codexless/tunnel restart.

## Test target

```text
workspace     machine-learning
cwd           C:\School\Machine Learning
document      51.Deep Learning2.annotated.pdf
source bytes  78,874,939
page count    56
selected page 16
```

## Execution path

After the user completed the canonical controlled restart, ChatGPT invoked the unchanged existing public action:

```text
codex.document_read
cwd           C:\School\Machine Learning
documentPath  51.Deep Learning2.annotated.pdf
pages         [16]
maxCharacters 25000
```

No Plugin refresh was used because the public tool schema and count did not change.

## Direct execution evidence

```text
schemaVersion  codexless.document-read.v1
workspaceId    machine-learning
mediaType      application/pdf
source bytes   78,874,939
source SHA-256 3872d5b3957d4313ab154a8405222d47098dda50657b660330ea0eecdce24110
parser         pdfjs-dist 5.4.624
pageCount      56
selectedPages  [16]
returnedPages  [16]
ocrPerformed   false
```

Returned page-16 text:

```text
characterCount          17,999
returnedCharacterCount  17,999
textStatus              present
truncated               false
```

Concrete directly extracted content includes `StyleGAN (2018)`, `latent vector`, `per-layer noise`, the explanation that the latent vector is fed to each stage of the generator, and the later `changing the latent vector` section describing coarse, middle and fine style changes.

## Qualification result

This closes the exact pending experiment from Checkpoint 315:

```text
78,874,939-byte authorized local PDF
    -> existing machine-learning read authority
    -> codex.document_read
    -> bounded isolated pdfjs-dist@5.4.624 text extraction
    -> 17,999 embedded-text characters
    -> ordinary ChatGPT text context
```

No OCR, rendering, Browser, manual upload, source-workspace write, semantic worker or Codex reasoning-model turn was used.

The returned source SHA-256 exactly matches the already-qualified page-render route for the same PDF, proving the text and visual channels refer to the same local source identity.

## What this proves

```text
- the old 32 MiB document_read source ceiling was implementation policy, not a fundamental parser limit;
- first-class embedded-text extraction now works on the real 78.9 MB source under the 96 MiB ceiling;
- the Machine Learning source workspace remains read-only;
- large-source text and large-source visual access now both work directly in ordinary ChatGPT;
- no public tool-schema change or Plugin refresh was required.
```

## Remaining scope

```text
- sources above 96 MiB are still outside the current bounded direct-source envelope;
- scanned/image-only PDFs still need the visual route because document_read performs no OCR;
- automatic routing among whole-file handoff, native split, direct text and page render is not yet implemented;
- per-page rendered PNG ceilings still apply independently to the visual route.
```

## Result

```text
LARGE_PDF_TEXT_READ = PASS
SOURCE_BYTES = 78874939
SOURCE_SHA256 = 3872d5b3957d4313ab154a8405222d47098dda50657b660330ea0eecdce24110
PAGE16_TEXT_CHARACTERS = 17999
TRUNCATED = FALSE
OCR = NONE
BROWSER = NONE
MANUAL_UPLOAD = NONE
SOURCE_WORKSPACE_WRITE = NONE
REASONING_MODEL_INTERMEDIARY = NONE
NEXT = GENERALIZE_AUTOMATIC_HYBRID_DIRECT_SOURCE_POLICY
```
