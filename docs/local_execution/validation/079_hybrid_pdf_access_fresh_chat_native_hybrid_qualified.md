# Validation 079: Hybrid PDF Access Fresh-Chat Native Hybrid Qualified

**Date:** 2026-09-06
**Status:** PASS / END-TO-END NATIVE + TEXT + VISION HYBRID HOST QUALIFIED
**Research:** Research 120
**Scope:** Verify that one fresh-chat `codex.pdf_access` call can route a 78,874,939-byte authorized PDF into bounded native PDF parts plus direct embedded-text and rendered-image fallback for individually oversized native pages; verify direct ChatGPT inspection of the returned images, complete host materialization of every native resource, and ordinary ChatGPT-side inspection of one materialized PDF part.

## 1. Live runtime

Independent current local verification in the persistent ADS conversation remains:

```text
Codexless ok       true
version            0.1.1-preview.16-hybrid-pdf-access
surfaceVersion     codexless-public-preview-v2
toolCount          60
tunnel /healthz    HTTP 200
tunnel /readyz     HTTP 200
```

## 2. Fresh-chat one-tool constraint

The fresh disposable ChatGPT qualification used exactly one ADS tool:

```text
codex.pdf_access
```

on:

```text
cwd             C:\School\Machine Learning
documentPath    51.Deep Learning2.annotated.pdf
intent          native
maxCharacters   50000
```

No low-level PDF tool, Browser, Agent, shell, OCR or web-search route was used to recover or supplement the ADS result.

## 3. Direct facade route evidence

```text
facade schema      codexless.pdf-access-orchestrator.v1
routing schema     codexless.pdf-access-policy.v1
requested intent   native
effective intent   native
primary route      native-parts-plus-page-fallback
native mode        parts-plus-page-fallback
native generation  reused
native target      7,000,000 bytes
```

Source:

```text
filename    51.Deep Learning2.annotated.pdf
bytes       78,874,939
SHA-256     3872d5b3957d4313ab154a8405222d47098dda50657b660330ea0eecdce24110
page count  56
```

The native and fallback coverage together spans all 56 source pages.

## 4. Native resource links

Fourteen bounded native PDF resource links were returned:

```text
01  pages 1-7     4,380,348 bytes  part-0001-p0001-p0007.pdf
02  pages 8-11    5,506,735 bytes  part-0002-p0008-p0011.pdf
03  pages 12-14   6,432,947 bytes  part-0003-p0012-p0014.pdf
04  page 15       5,984,175 bytes  part-0004-p0015-p0015.pdf
05  pages 17-19   5,509,372 bytes  part-0005-p0017-p0019.pdf
06  page 20       2,882,176 bytes  part-0006-p0020-p0020.pdf
07  page 21       4,748,084 bytes  part-0007-p0021-p0021.pdf
08  pages 22-27   6,978,607 bytes  part-0008-p0022-p0027.pdf
09  pages 28-36   2,677,586 bytes  part-0009-p0028-p0036.pdf
10  page 37       5,126,178 bytes  part-0010-p0037-p0037.pdf
11  pages 38-41   6,952,103 bytes  part-0011-p0038-p0041.pdf
12  page 42       6,586,933 bytes  part-0012-p0042-p0042.pdf
13  pages 43-48   3,804,720 bytes  part-0013-p0043-p0048.pdf
14  pages 50-56   2,866,873 bytes  part-0014-p0050-p0056.pdf
```

Every native artifact is below the 7,000,000-byte target.

## 5. Individually oversized native-page fallback

### Page 16

```text
classified oversized  true
fallback mode          direct
embedded text          present
text chars             17,999
truncated              false
rendered image         present
width x height         1240 x 1755
PNG bytes              583,130
PNG SHA-256            aca9cfadbfcb99382e22a2472495f26d1ab097922ce9406d66a8121810a56023
```

Returned text included:

```text
StyleGAN (2018)
latent vector
per-layer noise
Coarse styles copied
Middle styles copied
Fine styles
```

### Page 49

```text
classified oversized  true
fallback mode          direct
embedded text          present
text chars             1,345
truncated              false
rendered image         present
width x height         1240 x 1755
PNG bytes              535,152
PNG SHA-256            2eaaa5f2ffaae9b3d1e171d200d412dc1c545425d5f539e48513ac25c4e5e927
```

Returned text included:

```text
correlation and causation
Correlation does not imply causation.
No correlation without causation.
```

and the burned-toast/smoke distinction between prediction and intervention.

## 6. Projection and payload separation

```text
resourceLinkCount  14
imageCount         2
```

The structured/text result itself contained:

```text
PDF bytes/base64          NONE
rendered-image base64     NONE
```

The PDFs were emitted as separate MCP resource-link content items and the PNGs as separate MCP image content items. Literal `sha1_base64` strings inside extracted page-16 LaTeX/accessibility text are source text, not transport payload.

## 7. Direct image-content inspection

The fresh ChatGPT model directly inspected both images delivered by the one facade call.

Page 16 concrete visual evidence:

```text
portrait page with stacked slide panels and right-side prose
horse/rider versus zebra-like transformed example
StyleGAN (2018) black title bar
red latent-vector path entering multiple generator stages
green per-layer noise inputs
two generated face portraits
changing-the-latent-vector face grids and source/destination manipulation diagram
```

Page 49 concrete visual evidence:

```text
upper-left humorous apparent-causality collage
blue OdedRechavi Twitter link
black-header slide titled correlation and causation
correlated and causes emphasized in blue
bold statements about correlation not implying causation
right-side predictive-versus-intervention explanation
```

No additional ADS call was used for either image inspection.

## 8. ChatGPT host materialization

All fourteen native PDF resources materialized as actual conversation files:

```text
HOST_MATERIALIZATION = PASS 14/14
```

The reported file mapping was:

```text
pages 1-7
file_00000000ca3081f497354c394fd73e46
/mnt/data/51.Deep_Learning2.annotated.pages-1-7.pdf

pages 8-11
file_000000000a5c820a81278750f8fecb43
/mnt/data/51.Deep_Learning2.annotated.pages-8-11.pdf

pages 12-14
file_0000000004b88210afa475c9d502d593
/mnt/data/51.Deep_Learning2.annotated.pages-12-14.pdf

page 15
file_0000000001d881f48d79ec7afce7342d
/mnt/data/51.Deep_Learning2.annotated.pages-15-15.pdf

pages 17-19
file_000000003b788243b46e35f217fd928b
/mnt/data/51.Deep_Learning2.annotated.pages-17-19.pdf

page 20
file_000000008ee88243890d5f9f2066ee8c
/mnt/data/51.Deep_Learning2.annotated.pages-20-20.pdf

page 21
file_0000000074d08246b1acf231bb3bf64c
/mnt/data/51.Deep_Learning2.annotated.pages-21-21.pdf

pages 22-27
file_0000000064d481f4b58a3ced1ac2acd8
/mnt/data/51.Deep_Learning2.annotated.pages-22-27.pdf

pages 28-36
file_00000000efe08210849c50663aebe076
/mnt/data/51.Deep_Learning2.annotated.pages-28-36.pdf

page 37
file_00000000d1c48210a0f66818876e1101
/mnt/data/51.Deep_Learning2.annotated.pages-37-37.pdf

pages 38-41
file_000000004ec88210b86ce8f5a743fb19
/mnt/data/51.Deep_Learning2.annotated.pages-38-41.pdf

page 42
file_0000000009548210a38a44f6ee1a2af8
/mnt/data/51.Deep_Learning2.annotated.pages-42-42.pdf

pages 43-48
file_00000000a96c820aafc00beb93872533
/mnt/data/51.Deep_Learning2.annotated.pages-43-48.pdf

pages 50-56
file_00000000c1b48243b4e3fff42ec11b64
/mnt/data/51.Deep_Learning2.annotated.pages-50-56.pdf
```

This is direct host evidence that the 14 resource links were not merely advertised.

## 9. Ordinary ChatGPT-side materialized PDF inspection

Exactly one materialized native part was inspected after host resolution:

```text
/mnt/data/51.Deep_Learning2.annotated.pages-1-7.pdf
```

Normal ChatGPT-side PDF tooling reported:

```text
total pages  7
page size    595 x 842 pt
encrypted    false
annotations  4
```

The rendered first page showed:

```text
Deep generative models
Part 1: Generator networks
Machine Learning at Vrije Universiteit Amsterdam
generative-model explanatory prose
generative models slide with realistic generated faces
Karras et al. Style-Based Generator citation
visual shorthand slide
neural-network trapezoid plus multivariate-normal schematic
```

The fresh ChatGPT response identified use of its ordinary installed PDF Skill scripts for this post-materialization inspection, not another ADS operation.

## 10. Evidence separation

```text
A. codex.pdf_access
   facade/policy versions
   source identity
   route/mode
   14 native parts
   oversized pages 16 and 49
   text fallback metadata/content
   rendered-image metadata
   projection counts

B. ChatGPT host
   14 host file IDs
   14 /mnt/data paths
   14/14 materialization

C. direct image inspection
   visual observations from both images returned by the one facade call

D. ordinary ChatGPT-side materialized PDF inspection
   seven-page part metadata
   first-page render and concrete content
```

## 11. Result

```text
FRESH_CHAT_TOOL_DISCOVERY                 = PASS
CODEX_PDF_ACCESS_CALL                     = PASS
NATIVE_PARTS_PLUS_PAGE_FALLBACK            = PASS
NATIVE_RESOURCE_LINKS                      = PASS 14
OVERSIZED_NATIVE_PAGES                     = PASS pages 16,49
EMBEDDED_TEXT_FALLBACK                     = PASS 2/2
RENDERED_IMAGE_FALLBACK                    = PASS 2/2
DIRECT_CHATGPT_IMAGE_INSPECTION            = PASS 2/2
INLINE_PDF_PAYLOAD                         = NONE
INLINE_RENDERED_IMAGE_BASE64               = NONE
HOST_NATIVE_PART_MATERIALIZATION           = PASS 14/14
CHATGPT_SIDE_MATERIALIZED_PDF_INSPECTION   = PASS
OCR                                        = NONE
BROWSER                                    = NONE
AGENT                                      = NONE
SOURCE_WORKSPACE_WRITE                     = NONE
MANUAL_SOURCE_UPLOAD                       = NONE
WEB_SEARCH                                 = NONE
REASONING_MODEL_INTERMEDIARY_IN_FACADE     = NONE
NEXT                                       = PUBLIC_INTENT_MATRIX_AND_>192MIB_ISOLATION
```

Fresh-chat terminal marker:

```text
HYBRID_PDF_ACCESS_FRESH_CHAT_NATIVE_HYBRID=PASS
```

This qualification closes the `intent=native` hybrid-native route at the actual host boundary. Remaining Research 120 public-surface evidence should target explicit `text`, `visual`, `mixed`, `auto`, and then the >192 MiB page/range-isolation route through the same facade.