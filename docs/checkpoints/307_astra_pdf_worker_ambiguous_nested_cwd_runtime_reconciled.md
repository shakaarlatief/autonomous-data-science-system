# Checkpoint 307: Astra PDF Worker Ambiguous, Nested-CWD Runtime Boundary Reconciled

**Date:** 2026-09-05
**Status:** FIRST LIVE SEMANTIC ATTEMPT AMBIGUOUS / ENVIRONMENT RECONCILED / CONTROLLED SECOND RUN READY
**Checkpoint class:** EXPERIMENT_EXECUTION / INFRASTRUCTURE
**Project stage:** Research 117/118 held-out large-PDF semantic qualification
**Scope:** Preserves the first formal GPT-6 Astra 11.8 MB PDF semantic-worker attempt, its preregistered `AMBIGUOUS` classification, and the subsequent model-free localization showing that maintained parsing/rendering is available but write-capable execution from the nested scratch cwd reproduces a Windows sandbox setup-refresh failure while the same maintained renderer succeeds from the registered repository root.
**Authority:** Validation 066 is the detailed evidence. Research 118 remains the governing architecture record. This checkpoint does not qualify semantic PDF understanding and does not authorize a blind retry; it establishes an evidence-driven controlled second-run condition.
**Interaction environment:** ChatGPT + Codex App Server
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-18`
**Conversation title:** `18 - Astra Architecture Review and Multimodal Handoff Continuation`
**Primary collaborator:** ChatGPT + GPT-6 Astra

First formal attempt:

```text
requestId    ads-astra-phase2-pdf-01
model        gpt-6-astra / high
source       11,825,407 bytes
source SHA   be09c6065c36a9beaa32e812382b7fee7d8366dcb23f99a49e88f7306c99bc7f
turn state   completed / terminal
classification
             AMBIGUOUS

parser       not-run
rendering    not-run
vision       not-run
answers      all unanswered
source drift none observed
```

The worker stopped because it could not establish the maintained PDF execution runtime with sufficient certainty and reported an execution setup-refresh failure. It did not fabricate page coverage or semantic answers.

Model-free reconciliation then established:

```text
maintained PDF Skill
    pdf:pdf
    bundle 26.904.11930

primary runtime
    C:\Users\shaka\.cache\codex-runtimes\codex-primary-runtime
    bundle 26.904.11930
    manifest SHA-256 83abea4f54dc8295a6ba4422131b72e71c4b3d557ce316349501b511bd6b0423

maintained Python
    3.12.14
    pdfplumber 0.11.9
    pypdf 6.10.0

maintained Poppler
    pdfinfo 26.07.0
    pdftoppm available

exact source
    pdfinfo page count 8 PASS
    pdfplumber all-page extraction PASS
    codex.document_read pages 1-8 PASS / no truncation

write-capable command from nested scratch cwd
    helper_unknown_error: setup refresh had errors
    REPRODUCED

same maintained pdftoppm from registered repository root
    one-page scratch render PASS
    eight-page scratch render PASS

local scratch PNG -> codex.image_read -> ChatGPT vision
    PASS
```

The eight-page Poppler diagnostic included the image-heavy pages that are approximately 3.35 MB each as PNGs. Those local files were hashed and then deleted. The worker scratch tree was restored to exactly `source.pdf` before any follow-up worker.

A separate diagnostic also showed that the existing stdout/base64 `codex.document_render` route succeeds for smaller single pages but can hit `DOCUMENT_RENDER_PROTOCOL_ERROR` for the image-heavy fixture. This does not invalidate its previous qualification; it supports the large-document design choice to keep rendered page bytes local and pass images through native local-image vision rather than a large serialized stdout envelope.

The first attempt therefore remains preserved as `AMBIGUOUS`, not silently overwritten by the diagnosis.

Controlled next condition:

```text
new formal task
    cwd = registered ADS repository root

worker file boundary
    .tmp/astra-phase2-pdf-worker-01/source.pdf
    + worker-created render outputs in that same scratch subtree only

runtime
    exact maintained primary-runtime paths supplied
    no installation

held-out evaluator
    remains outside worker prompt/workspace

forbidden
    Browser
    upload
    external storage
    answer key / generator / prior QA
    private candidate implementation
    unrelated repository content
```

This is a deliberate second experiment after the blocking environment was localized. It is not an automatic retry of an uncertain action.

Next: run the controlled second formal Astra worker under the reconciled repository-root execution context, then independently evaluate actual worker evidence and classify semantic workflow `PASS / FAIL / AMBIGUOUS` before any live receipt integration.
