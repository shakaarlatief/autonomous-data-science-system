# Checkpoint 312: Machine Learning Large PDFs Require Hybrid Direct-Source Fallback

**Date:** 2026-09-06
**Status:** NATIVE PAGE-RANGE SPLITTER NOT SUFFICIENT FOR ALL LARGE PDFs / HYBRID OVERSIZED-PAGE ROUTE REQUIRED
**Checkpoint class:** LOCAL EXECUTION / DIRECT CHATGPT FILE ACCESS
**Project stage:** Research 117 / Research 119 direct local-file access
**Scope:** Preserves the generalization check of the Checkpoint 311 native-PDF splitter against the larger authorized Machine Learning PDFs and the discovery that several files contain individual pages whose native one-page PDFs exceed the host-qualified envelope.
**Authority:** Validation 070 is the detailed evidence. Research 119 remains the governing objective correction.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System + read-only `machine-learning` workspace
**Interaction session:** `chatgpt-18`
**Conversation title:** `18 - Astra Architecture Review and Multimodal Handoff Continuation`
**Primary collaborator:** ChatGPT

Fifteen PDFs in the registered Machine Learning workspace exceed the 7,417,428-byte highest clean whole-file host PASS.

Checkpoint 311's native page-range fallback remains valid for many of them, but it does not generalize to every file. Representative counterexamples include:

```text
51.Deep Learning2.annotated.pdf
    page 16    15,944,609-byte one-page PDF
    page 49     7,784,782-byte one-page PDF

11.Introduction.annotated.pdf
    page 12    17,597,874-byte one-page PDF

71.Reinforcement Learning.annotated.pdf
    page 18    14,059,747-byte one-page PDF

41.DeepLearning1.annotated.pdf
    page 39    14,048,969-byte one-page PDF
```

Basic pypdf content-stream compression and duplicate-object cleanup do not materially reduce the worst Deep Learning 2 pages. Page 16 contains many embedded image resources, so the native page payload itself is large.

This means a page-boundary splitter alone cannot guarantee that every output part will fit below the ChatGPT host envelope.

The current `codex.document_read` / `codex.document_render` 32 MiB source admission ceiling also prevents directly selecting/rendering one page from some 40-75 MiB Machine Learning PDFs. Therefore the next direct-access design must isolate a page/range internally before host handoff or page-render processing.

Accepted hierarchy after this checkpoint:

```text
unchanged native whole file
    preferred when qualified

native PDF page-range parts
    proven fallback when every required part fits

oversized single native page
    requires a faithful model-free page fallback
    likely isolated-page text + high-fidelity rendered image/resource
    no reasoning-model intermediary

Browser upload
    remains heavier fallback/comparison route
```

The Machine Learning workspace remains read-only. A production splitter/fallback should not require writing split files back into that source folder. Generated resources should be Codexless-owned and ephemeral or deterministically regenerated from verified source identity.

```text
CHECKPOINT_312 = MACHINE_LEARNING_LARGE_PDF_HYBRID_FALLBACK_REQUIRED
```
