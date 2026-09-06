# Checkpoint 311: Multi-Native-PDF Direct ChatGPT Access Qualified

**Date:** 2026-09-06
**Status:** PASS / OVERSIZED PDF DIRECT-SOURCE FALLBACK QUALIFIED / PRODUCTIZATION DECISION NEXT
**Checkpoint class:** LOCAL EXECUTION / DIRECT CHATGPT FILE ACCESS
**Project stage:** Research 117 / Research 119 direct local-file access
**Scope:** Preserves the successful deterministic split of the 11,825,407-byte eight-page source into three native PDFs below the known clean host-materialization PASS envelope, exact render fidelity across all eight pages, 3/3 `document_file_link` materialization into one ordinary ChatGPT conversation, direct ChatGPT PDF inspection, and cross-part reasoning without a semantic intermediary.
**Authority:** Validation 069 is the detailed evidence. Research 119 remains the governing objective correction.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-18`
**Conversation title:** `18 - Astra Architecture Review and Multimodal Handoff Continuation`
**Primary collaborator:** ChatGPT

Source:

```text
bytes       11,825,407
SHA-256     be09c6065c36a9beaa32e812382b7fee7d8366dcb23f99a49e88f7306c99bc7f
pages       8
```

A conservative two-part split was rejected because pages 1-4 alone produced approximately 7.87 MiB, above the highest clean host PASS of 7,417,428 bytes. A deterministic contiguous-range search selected the minimum conservative three-part partition:

```text
pages 1-3    3,936,427 bytes
page 4       3,935,151 bytes
pages 5-8    3,955,281 bytes
```

Rerunning the splitter reproduced all output hashes exactly. Model-free Poppler render comparison against the original returned 8/8 exact page-image hash matches.

All three existing `codex.document_file_link` calls succeeded and the ChatGPT host materialized the parts as actual conversation files. Ordinary ChatGPT-side PDF inspection reported 3 + 1 + 4 pages, matching the complete ordered eight-page source.

Direct visual inspection across the three files recovered source facts including the page-1 opening inventory of 137 units, page-2 A/B/C chart with B tallest, page-6 inspection batch Q7M-42 with release status HOLD and red visual marker, and page-8 closing inventory of 219 units. ChatGPT could therefore reason directly across part boundaries, including the source-supported inventory change of +82 units.

Accepted classification:

```text
MULTI_NATIVE_PDF_DIRECT_ACCESS = PASS
SEMANTIC_MODEL_INTERMEDIARY = NONE
UNCHANGED_OVERSIZED_WHOLE_FILE_MATERIALIZATION = NOT_ESTABLISHED
```

The mechanism is now a real fallback candidate rather than speculative architecture. It remains subordinate to unchanged native whole-file handoff because multi-file UX is less elegant and arbitrary PDFs may contain document-wide semantics that splitting does not preserve automatically.

The next architecture decision is whether to productize this deterministic multi-part fallback for oversized PDFs now or compare its practical UX/semantic trade-offs against the still-heavier Browser upload fallback and any newly available supported native host primitive before implementation.

```text
CHECKPOINT_311 = MULTI_NATIVE_PDF_DIRECT_ACCESS_QUALIFIED
```
