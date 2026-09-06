# Checkpoint 316: Large-PDF Text Read Qualified

**Date:** 2026-09-06
**Status:** PASS / LARGE-SOURCE TEXT DIRECT-SOURCE ROUTE QUALIFIED
**Checkpoint class:** LOCAL EXECUTION / DIRECT CHATGPT FILE ACCESS
**Project stage:** Research 117 / Research 119 direct local-file access
**Scope:** Preserves the successful same-chat `codex.document_read` qualification of page 16 from the 78,874,939-byte `51.Deep Learning2.annotated.pdf` source after the controlled restart.
**Authority:** Validation 074 is the detailed evidence. Research 119 remains the governing objective correction.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System + read-only `machine-learning` workspace
**Interaction session:** `chatgpt-18`
**Conversation title:** `18 - Astra Architecture Review and Multimodal Handoff Continuation`
**Primary collaborator:** ChatGPT

The exact pending experiment from Checkpoint 315 now passes.

```text
source PDF                  78,874,939 bytes
source SHA-256              3872d5b3957d4313ab154a8405222d47098dda50657b660330ea0eecdce24110
selected page               16
embedded text characters    17,999
parser                      pdfjs-dist 5.4.624
truncated                   false
OCR                         false
```

The embedded text reached ordinary ChatGPT directly through the existing `codex.document_read` action under the read-only Machine Learning authority. The returned content includes StyleGAN material such as `latent vector`, `per-layer noise`, generator-stage explanations, and the `changing the latent vector` section.

This source SHA-256 exactly matches the Checkpoint 314 page-render qualification, so the first-class text and visual routes are now both qualified against the same 78.9 MB local PDF.

No manual upload, Browser, OCR, semantic worker, Codex reasoning turn or source-workspace write was used.

The current direct-source PDF hierarchy is therefore:

```text
small/native whole PDF
    -> document_file_link when host materialization fits

larger native PDF
    -> deterministic native PDF parts when parts fit

embedded text from authorized PDF <=96 MiB
    -> document_read

page visuals from authorized PDF <=96 MiB
    -> document_render when rendered PNG fits
```

The next work should not re-prove large-source text or visual access. It should generalize the automatic hybrid policy that selects the best direct-source route for a requested PDF and falls back cleanly when one route hits its independent envelope.

```text
CHECKPOINT_316 = LARGE_PDF_TEXT_READ_QUALIFIED
```
