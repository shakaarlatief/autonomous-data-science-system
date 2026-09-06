# Checkpoint 327: Hybrid PDF Fresh-Chat Intent Matrix Qualified

**Date:** 2026-09-06
**Status:** ALL FIVE PUBLIC INTENT ROUTES QUALIFIED / >192 MiB FACADE ISOLATION NEXT
**Checkpoint class:** LOCAL EXECUTION / DIRECT CHATGPT FILE ACCESS
**Project stage:** Research 120 automatic hybrid PDF direct-source routing
**Scope:** Preserves the successful fresh disposable five-call `codex.pdf_access` semantic intent matrix after the serialized-page renderer fix was activated.
**Authority:** Validation 085 contains the full five-call routing, text, image and deterministic-hash evidence.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-19`
**Conversation title:** `19 - Hybrid PDF Intent Matrix and Isolation Qualification`
**Primary collaborator:** ChatGPT

The previously failing high-level matrix is now fully qualified. Exactly five `codex.pdf_access` calls succeeded with no retries or alternate ADS tools:

```text
text                         -> text  -> direct-text
visual                       -> visual -> direct-render
mixed                        -> mixed -> direct-text-plus-selective-render
auto + visualRequired=false -> text  -> direct-text
auto + visualRequired=true  -> mixed -> direct-text-plus-selective-render
```

Every rendering-dependent call returned pages 16 and 49. Calls 2, 3 and 5 reproduced the same PNG hashes:

```text
page 16  aca9cfadbfcb99382e22a2472495f26d1ab097922ce9406d66a8121810a56023
page 49  2eaaa5f2ffaae9b3d1e171d200d412dc1c545425d5f539e48513ac25c4e5e927
```

Text routes returned the same untruncated 19,344 characters across pages 16 and 49. Direct image inspection succeeded for every image-bearing call. No native PDF resource link or host PDF materialization was involved.

This closes the renderer/intention-matrix repair sequence opened by Checkpoint 322. The remaining Research 120 public proof is now the high-level page/range-isolation path for a source above the 192 MiB direct-processing envelope.

```text
CHECKPOINT_327 = HYBRID_PDF_FRESH_CHAT_INTENT_MATRIX_QUALIFIED
```
