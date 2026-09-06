# Validation 080: Hybrid PDF Access Fresh-Chat Intent Matrix Render Transport Failed

**Date:** 2026-09-06
**Status:** FAIL / TEXT ROUTES QUALIFIED / MULTI-PAGE DIRECT-RENDER TRANSPORT GAP LOCALIZED
**Research:** Research 120
**Scope:** Preserve the fresh-chat five-call `codex.pdf_access` intent-matrix qualification, including the exact Call 2 input deviation, the successful text-only branches, the rendering-dependent failures, and the subsequent persistent-chat low-level reproduction that localizes the failure to batched direct rendering through the known Windows buffered `command/exec` transport ceiling.

## 1. Fresh-chat execution contract

The disposable ChatGPT qualification made exactly five ADS calls, all to:

```text
codex.pdf_access
```

against:

```text
cwd             C:\School\Machine Learning
documentPath    51.Deep Learning2.annotated.pdf
source bytes    78,874,939
source SHA-256  3872d5b3957d4313ab154a8405222d47098dda50657b660330ea0eecdce24110
page count      56
```

No compensating ADS call, low-level PDF tool, Browser, Agent, OCR, source-workspace write, manual source upload, web search, ordinary ChatGPT PDF/file tooling, or reasoning-model intermediary was used inside that qualification.

The terminal result was:

```text
HYBRID_PDF_ACCESS_FRESH_CHAT_INTENT_MATRIX=FAIL
```

## 2. Call 1: explicit text

Input:

```text
intent          text
pages           [16,49]
maxCharacters   30000
```

Result:

```text
SUCCESS
facade schema       codexless.pdf-access-orchestrator.v1
policy schema       codexless.pdf-access-policy.v1
requested intent    text
effective intent    text
primary route       direct-text
text mode           direct
returned pages      [16,49]
total chars         19,344
truncated           false
resourceLinkCount   0
imageCount          0
OCR                 false
```

Per-page text:

```text
page 16   17,999 chars
page 49    1,345 chars
```

Page 16 included StyleGAN, latent-vector injection at successive generator stages, per-layer random noise, and coarse/middle/fine style copying. Page 49 included correlation versus causation and the burned-toast/toaster/smoke intervention example.

This verifies:

```text
text -> effective text -> direct-text
```

## 3. Call 2: explicit visual

The intended scheduled input was:

```text
intent   visual
pages    [16,49]
```

The actual call additionally supplied:

```text
visualPages [16,49]
```

This was an execution deviation from the frozen qualification prompt and must remain part of the evidence. Because the experiment required exactly five calls, no retry or compensating call was made.

The call independently failed at the lower renderer layer:

```text
DOCUMENT_RENDER_PROTOCOL_ERROR
sandboxed renderer returned invalid JSON
```

No successful facade envelope or image was returned. Therefore the intended visual routing semantics were not qualified by this call.

## 4. Call 3: explicit mixed

Exact scheduled input:

```text
intent          mixed
pages           [16,49]
visualPages     [16,49]
maxCharacters   30000
```

Result:

```text
FAIL
DOCUMENT_RENDER_PROTOCOL_ERROR
sandboxed renderer returned invalid JSON
```

No text or image content was returned because the combined route failed before a successful facade result was projected.

This call had no input deviation and independently establishes that a rendering-dependent facade route failed.

## 5. Call 4: auto without visual requirement

Input:

```text
intent          auto
pages           [16,49]
visualRequired  false
maxCharacters   30000
```

Result:

```text
SUCCESS
facade schema       codexless.pdf-access-orchestrator.v1
policy schema       codexless.pdf-access-policy.v1
requested intent    auto
effective intent    text
primary route       direct-text
text mode           direct
returned pages      [16,49]
total chars         19,344
truncated           false
resourceLinkCount   0
imageCount          0
OCR                 false
```

The returned text and character counts matched Call 1.

This verifies:

```text
auto + visualRequired=false -> effective text -> direct-text
```

## 6. Call 5: auto with visual requirement

Exact scheduled input:

```text
intent          auto
pages           [16,49]
visualPages     [16,49]
visualRequired  true
maxCharacters   30000
```

Result:

```text
FAIL
DOCUMENT_RENDER_PROTOCOL_ERROR
sandboxed renderer returned invalid JSON
```

No successful facade envelope, text, or image content was returned.

This call had no input deviation and independently establishes failure of the auto route once rendering is required.

## 7. Fresh-chat matrix disposition

```text
text                         VERIFIED
visual                       NOT VERIFIED / renderer failure
mixed                        NOT VERIFIED / renderer failure
auto + visualRequired=false  VERIFIED
auto + visualRequired=true   NOT VERIFIED / renderer failure
```

No image-content inspection or repeated-render SHA-256 comparison was possible in the five-call qualification because every rendering-dependent facade call returned no images.

## 8. Persistent-chat low-level discrimination

After the failed disposable qualification was reported back to the persistent ADS conversation, ChatGPT used the already-qualified low-level `codex.document_render` only for diagnosis.

The same source with both pages in one call reproduced the exact failure:

```text
pages [16,49]
-> DOCUMENT_RENDER_PROTOCOL_ERROR
-> sandboxed renderer returned invalid JSON
```

The same pages rendered individually:

```text
page 16
    PASS
    1240 x 1755
    583,130 bytes
    SHA-256 aca9cfadbfcb99382e22a2472495f26d1ab097922ce9406d66a8121810a56023

page 49
    PASS
    1240 x 1755
    535,152 bytes
    SHA-256 2eaaa5f2ffaae9b3d1e171d200d412dc1c545425d5f539e48513ac25c4e5e927
```

Both hashes exactly match the previously qualified Checkpoint 321 native-hybrid fallback images.

Therefore:

```text
page 16 renderer fidelity       preserved
page 49 renderer fidelity       preserved
single-page direct rendering    preserved
two-page batched direct render  fails
```

## 9. Root-cause localization

Validation 048 / Checkpoint 289 already established the relevant Windows transport constraint: buffered App Server `command/exec` under the Windows restricted-token sandbox has an approximately 1 MiB stdout capture ceiling, while the current `DocumentRenderer` serializes rendered PNGs as base64 inside one child stdout JSON protocol.

The live candidate currently sends the entire selected page list to one renderer child. For the two qualified images above, their base64 payloads alone are approximately:

```text
page 16   777,508 characters
page 49   713,536 characters
combined  1,491,044 characters
```

before JSON framing. Each page separately fits below the observed capture ceiling, while the two-page batch exceeds it. The observed failure pattern therefore matches the already-established transport limitation exactly.

This is a transport/batching defect. It is not evidence of a PDF.js/canvas fidelity failure, an intent-policy error, a ChatGPT image-projection failure, or a need for a semantic model intermediary.

## 10. Smallest justified implementation seam

The narrow correction is to change the low-level direct `DocumentRenderer` implementation, not the semantic route policy:

```text
public request may still select up to four pages

internally
    -> execute one read-only sandbox renderer child per selected source page
    -> keep each App Server stdout payload bounded
    -> preserve requested page order
    -> require page-count consistency
    -> combine validated page records
    -> preserve existing 4 MiB per-page and 8 MiB aggregate semantic limits
    -> preserve source identity revalidation
```

This should repair `codex.document_render` multi-page requests and, transitively, the direct visual/mixed/auto-visual `codex.pdf_access` routes.

It deliberately does not claim to solve a different known case where one individual rendered page itself produces more than the Windows buffered stdout envelope. That representative high-detail single-page transport gap remains separately bounded by Validation 048 / Checkpoint 289.

## 11. Result

```text
FRESH_CHAT_EXACT_FIVE_CALL_CONTRACT        PASS
CALL_2_INPUT_DEVIATION_PRESERVED           YES
TEXT_ROUTE                                 PASS
AUTO_TEXT_ROUTE                            PASS
VISUAL_ROUTE                               FAIL / NOT QUALIFIED
MIXED_ROUTE                                FAIL / NOT QUALIFIED
AUTO_VISUAL_ROUTE                          FAIL / NOT QUALIFIED
LOW_LEVEL_MULTI_PAGE_FAILURE_REPRODUCED    PASS
PAGE_16_SINGLE_RENDER                      PASS
PAGE_49_SINGLE_RENDER                      PASS
KNOWN_WINDOWS_CAPTURE_LIMIT_MATCH          YES
PDF_RENDERER_FIDELITY_DISPROVEN            NO
SEMANTIC_ROUTING_POLICY_DISPROVEN          NO
NEXT                                       SERIALIZE_DIRECT_RENDER_PAGES_THEN_RETEST
```
