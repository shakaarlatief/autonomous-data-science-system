# Checkpoint 315: Large-PDF Text Read Source Published, Restart Pending

**Date:** 2026-09-06
**Status:** STATIC PASS / LIVE SOURCE PUBLISHED / RESTART + REAL PAGE-16 TEXT QUALIFICATION NEXT
**Checkpoint class:** LOCAL EXECUTION / DIRECT CHATGPT FILE ACCESS
**Project stage:** Research 117 / Research 119 direct local-file access
**Scope:** Preserves the bounded `codex.document_read` source-ceiling extension from 32 MiB to 96 MiB, its child-side large-input memory tightening, guarded installed-source publication, installed 36.7 MB PDF.js smoke pass, and the exact post-restart real Machine Learning page-16 qualification.
**Authority:** Validation 073 is the detailed evidence. Research 119 remains the governing objective correction.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System + read-only `machine-learning` workspace
**Interaction session:** `chatgpt-18`
**Conversation title:** `18 - Astra Architecture Review and Multimodal Handoff Continuation`
**Primary collaborator:** ChatGPT

The remaining large-source text limitation is now localized and addressed in source.

Before publication, live `codex.document_read` rejected `51.Deep Learning2.annotated.pdf` page 16 because the 78,874,939-byte source exceeded the 33,554,432-byte whole-source admission ceiling before page selection.

The candidate raises only that bounded source ceiling to 96 MiB while preserving the public `codex.document_read` schema and read-only authority model. The isolated parser child now receives the exact declared source size, uses one exact bounded stdin buffer instead of chunk-list plus `Buffer.concat` duplication, and gives PDF.js a zero-copy `Uint8Array` view.

Accepted pre-restart evidence:

```text
live baseline 78,874,939-byte source rejection     CONFIRMED
candidate syntax                                   PASS
focused large-source tests                         3 / 3 PASS
installed source publication                       PASS
installed valid 36,700,855-byte PDF.js smoke       PASS
parser                                             pdfjs-dist 5.4.624
source workspace write                             NONE
reasoning-model intermediary                       NONE
public tool schema/count change                    NONE
```

The temporary installed-runtime workspace admission was removed after publication/testing. Durable workspace registry is revision 12 with only the normal four workspaces.

Private runtime complement is synchronized at:

```text
96f58fea13377943a0fbec2889384329bce49cb5
```

The exact next action is the canonical controlled Codexless/tunnel restart from `docs/local_execution/OPERATIONS.md`. No Plugin refresh is required. After restart, call the existing `codex.document_read` in this same chat on `51.Deep Learning2.annotated.pdf` page 16 with `maxCharacters=25000`.

A PASS should establish first-class direct embedded-text extraction from the real 78.9 MB local PDF and close the large-source text gap for sources within the new 96 MiB ceiling.

```text
CHECKPOINT_315 = LARGE_PDF_TEXT_READ_SOURCE_PUBLISHED_RESTART_PENDING
```
