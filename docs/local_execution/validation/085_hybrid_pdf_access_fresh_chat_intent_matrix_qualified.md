# Validation 085: Hybrid PDF Fresh-Chat Intent Matrix Qualified

**Date:** 2026-09-06
**Status:** PASS / ALL FIVE PUBLIC INTENT ROUTES QUALIFIED / >192 MiB FACADE ISOLATION NEXT
**Research:** Research 120
**Scope:** Preserve the fresh disposable ChatGPT five-call `codex.pdf_access` intent-matrix requalification after the serialized-page renderer correction was published and activated.

## Test source

```text
workspace     machine-learning
cwd           C:\\School\\Machine Learning
document      51.Deep Learning2.annotated.pdf
source bytes  78,874,939
source SHA256 3872d5b3957d4313ab154a8405222d47098dda50657b660330ea0eecdce24110
page count    56
selected      [16,49]
```

Exactly five ADS calls were made, all `codex.pdf_access`, in the frozen order. No call failed, no retry was made, and no compensating ADS tool was used.

## Routing matrix

```text
CALL 1 explicit text
requested intent  text
effective intent  text
primary route     direct-text
pages             [16,49]
text chars        17,999 + 1,345 = 19,344
truncated         false
resource links    0
images            0

CALL 2 explicit visual
requested intent  visual
effective intent  visual
primary route     direct-render
rendered pages    [16,49]
resource links    0
images            2

CALL 3 explicit mixed
requested intent  mixed
effective intent  mixed
primary route     direct-text-plus-selective-render
text pages        [16,49]
rendered pages    [16,49]
text chars        19,344
resource links    0
images            2

CALL 4 auto / visualRequired=false
requested intent  auto
effective intent  text
primary route     direct-text
pages             [16,49]
text chars        19,344
resource links    0
images            0

CALL 5 auto / visualRequired=true
requested intent  auto
effective intent  mixed
primary route     direct-text-plus-selective-render
text pages        [16,49]
rendered pages    [16,49]
text chars        19,344
resource links    0
images            2
```

Facade schema stayed `codexless.pdf-access-orchestrator.v1`; routing-policy schema stayed `codexless.pdf-access-policy.v1`.

## Render determinism

Every rendering-dependent call returned both pages with the same live metadata:

```text
page 16
1240 x 1755
583,130 bytes
aca9cfadbfcb99382e22a2472495f26d1ab097922ce9406d66a8121810a56023

page 49
1240 x 1755
535,152 bytes
2eaaa5f2ffaae9b3d1e171d200d412dc1c545425d5f539e48513ac25c4e5e927
```

Calls 2, 3 and 5 were identical for both PNG hashes, dimensions and byte sizes. These live hashes also match the earlier qualified Checkpoint 321/326 values.

## Direct host/model evidence

The same-call MCP images were directly inspected by ChatGPT. Page 16 visibly contained the StyleGAN material, including `StyleGAN (2018)`, the latent-vector/per-layer-noise generator schematic, and `changing the latent vector` face-grid material. Page 49 visibly contained the collage and the lower `correlation and causation` slide with the explanatory causality text.

There was no PDF host materialization stage in this matrix. Every call reported `toolProjection.resourceLinkCount=0`; text/image structured metadata contained no rendered-image base64; rendering used ordinary MCP image content.

## Excluded mechanisms

```text
OCR                       NO
Browser                   NO
Agent / model turn        NO
web search                NO
ordinary ChatGPT PDF tool NO
source-workspace write    NO
manual source upload      NO
other ADS tool            NO
```

The internal renderer remained model-free and read-only.

## Result

```text
TEXT_ROUTE                         PASS
VISUAL_ROUTE                       PASS
MIXED_ROUTE                        PASS
AUTO_TEXT_ROUTE                    PASS
AUTO_MIXED_ROUTE                   PASS
RENDER_PAGES_16_49_ALL_CALLS       PASS
REPEATED_PNG_HASHES_IDENTICAL      PASS
DIRECT_IMAGE_INSPECTION            PASS
RESOURCE_LINK_COUNT_ALL_ZERO       PASS
FRESH_CHAT_INTENT_MATRIX           PASS
NEXT                               >192 MiB PUBLIC FACADE ISOLATION
```

Terminal qualification marker from the disposable chat:

```text
HYBRID_PDF_ACCESS_FRESH_CHAT_INTENT_MATRIX=PASS
```
