# Validation 084: Hybrid PDF Render Serialization Live Activation Qualified

**Date:** 2026-09-06
**Status:** PASS / LIVE ACTIVATION QUALIFIED / FRESH-HOST INTENT MATRIX NEXT
**Research:** Research 120
**Scope:** Preserve the controlled-restart activation of the serialized-page renderer correction and verify the exact formerly failing two-page low-level render path in the running preview.16 process before repeating the high-level fresh-chat intent matrix.

## Restart evidence

After Checkpoint 325 source publication, the user completed the repository-governed controlled restart. Post-restart local health reported:

```text
ok             true
service        codexless-public
transport      streamable-http
version        0.1.1-preview.16-hybrid-pdf-access
surfaceVersion codexless-public-preview-v2
toolCount      60
defaultCwd      C:\Projects_Data\autonomous-data-science-system
```

Tunnel verification reported:

```text
/healthz HTTP 200 / live
/readyz  HTTP 200 / ready
```

## Direct post-restart discriminator

The persistent ChatGPT conversation then invoked the exact low-level request that failed before the renderer correction:

```text
codex.document_render
cwd            C:\School\Machine Learning
documentPath   51.Deep Learning2.annotated.pdf
pages          [16,49]
```

The live call succeeded and returned both images in one public request:

```text
schemaVersion  codexless.document-render.v1
source bytes   78,874,939
source SHA-256 3872d5b3957d4313ab154a8405222d47098dda50657b660330ea0eecdce24110
pageCount      56
selectedPages  [16,49]
ocrPerformed   false
warnings       []
```

Returned PNGs:

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

Those hashes exactly match the earlier individually qualified Checkpoint 321 images and the pre-fix single-page discriminator. The same two-page request was repeated during the persistent-session activation smoke and continued to return the identical pair of hashes, giving additional deterministic evidence after restart.

## Direct image inspection

The returned images were directly visible to ChatGPT from the same tool response.

Page 16 visibly contains the StyleGAN material, including a black `StyleGAN (2018)` header, a generator diagram labeled with latent-vector and per-layer-noise inputs, and a later `changing the latent vector` panel showing face grids and layer-selection arrows.

Page 49 visibly contains a collage near the top and a lower slide titled `correlation and causation`, including the statements that correlated variables support prediction and that correlation does not imply causation, alongside the explanatory toaster/smoke text.

This confirms direct image-content delivery remains intact for the repaired multi-page route.

## Result

```text
CONTROLLED_RESTART                 PASS
LOCAL_PREVIEW16_60_TOOLS           PASS
TUNNEL_HEALTH_READY                PASS / PASS
FORMERLY_FAILING_RENDER_[16,49]    PASS
PAGE16_HASH_PRESERVED              PASS
PAGE49_HASH_PRESERVED              PASS
DIRECT_IMAGE_DELIVERY              PASS
LOW_LEVEL_RENDER_FIX_LIVE          YES
HIGH_LEVEL_INTENT_MATRIX           NOT YET REQUALIFIED
NEXT                               FRESH_DISPOSABLE_INTENT_MATRIX
```
