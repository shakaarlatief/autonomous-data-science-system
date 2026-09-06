# Checkpoint 322: Hybrid PDF Intent Matrix Render Transport Gap Localized

**Date:** 2026-09-06
**Status:** INTENT MATRIX FAILED / TEXT BRANCHES QUALIFIED / DIRECT RENDER TRANSPORT FIX NEXT
**Checkpoint class:** EXPERIMENT_VERIFICATION
**Project stage:** Research 120 automatic hybrid PDF direct-source routing
**Scope:** Preserves the failed fresh-chat public `codex.pdf_access` intent matrix, the exact Call 2 input deviation, the successful text and auto-text routes, and the follow-up low-level discrimination showing that rendering-dependent routes fail because the current direct renderer batches pages into one Windows App Server stdout protocol that exceeds the already-known buffered capture ceiling.
**Authority:** Research 120 defines the architecture. Validation 080 contains the detailed execution and diagnosis evidence. Validation 048 / Checkpoint 289 govern the previously established Windows buffered-render transport limitation.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-19`
**Conversation title:** `19 - Hybrid PDF Intent Matrix and Isolation Qualification`
**Primary collaborator:** ChatGPT

Checkpoint 321 remains valid and closed the native hybrid route. The next fresh-host qualification deliberately moved to semantic intent routing.

The five-call disposable qualification produced:

```text
text                         PASS
visual                       FAIL
mixed                        FAIL
auto + visualRequired=false  PASS
auto + visualRequired=true   FAIL
```

The two successful branches returned the expected `direct-text` route and identical text for source pages 16 and 49.

All three rendering-dependent branches failed with:

```text
DOCUMENT_RENDER_PROTOCOL_ERROR
sandboxed renderer returned invalid JSON
```

Call 2 also contained a qualification-procedure deviation: `visualPages:[16,49]` was supplied in addition to the requested `pages:[16,49]`. No retry was made because the frozen test allowed exactly five ADS calls. Calls 3 and 5 matched their scheduled inputs and independently reproduced the same lower renderer failure, so the overall matrix failure does not depend on the Call 2 deviation.

Persistent-chat low-level discrimination then established:

```text
document_render pages [16,49]
    FAIL / invalid JSON

document_render page [16]
    PASS / 583,130-byte PNG
    aca9cfadbfcb99382e22a2472495f26d1ab097922ce9406d66a8121810a56023

document_render page [49]
    PASS / 535,152-byte PNG
    2eaaa5f2ffaae9b3d1e171d200d412dc1c545425d5f539e48513ac25c4e5e927
```

Those individual hashes exactly match Checkpoint 321. The failure is therefore not a page-fidelity regression.

The current direct renderer sends all requested pages through one sandbox child and one base64-bearing stdout JSON protocol. The two PNGs correspond to roughly 1.49 million base64 characters before JSON framing. Validation 048 / Checkpoint 289 had already established that this transport is unsuitable once the Windows buffered `command/exec` stdout capture exceeds approximately one MiB.

The failure therefore reactivates a known bounded implementation pressure rather than changing the Research 120 architecture:

```text
intent policy                       retained
native hybrid route                 retained
direct text                         retained
single-page direct render           retained
multi-page direct render transport  repair required
```

The smallest justified correction is to serialize direct source rendering internally as one read-only sandbox execution per selected page, then combine and validate the results under the existing public four-page request contract and aggregate semantic limits. This avoids widening authority or adopting the previously unqualified loopback transport merely to fix this smaller multi-page batching case.

The public >192 MiB facade isolation qualification is paused until the rendering-dependent intent matrix is repaired and requalified. It must not be used to skip over the failed public contract.

```text
CHECKPOINT_322 = HYBRID_PDF_INTENT_MATRIX_RENDER_TRANSPORT_GAP_LOCALIZED
```
