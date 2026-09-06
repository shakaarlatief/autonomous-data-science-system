# Validation 086: Hybrid PDF >192 MiB Public Facade Isolation Qualified

**Date:** 2026-09-06
**Status:** PASS / ALL PUBLIC PDF ROUTE CLASSES QUALIFIED / RESEARCH 120 PDF LEAF COMPLETE
**Research:** Research 120
**Scope:** Qualify the public high-level PDF facade page/range-isolation routes for a valid authorized source above the 192 MiB direct-processing envelope, including text, render, mixed projection, original-page provenance, managed-artifact reuse, direct ChatGPT image consumption and absence of source-adjacent derived files.

## 1. Controlled source

A deterministic valid one-page PDF was generated under protected private-runtime `.tmp` solely for this bounded qualification. The visible page contains ordinary embedded Helvetica text and simple vector graphics. A large unreferenced stream object raises the source above the direct-processing threshold without making the visible page itself complex.

```text
workspace            ads-local-runtime
relative path        .tmp/hybrid-pdf-isolation/public-isolation-over-192mib.pdf
source bytes         211,813,221
source SHA-256       00dfd5d9a983647bf7e35ee884796bc5f629807a1a1253ef613c42492e75c9c7
direct limit bytes   201,326,592
above direct limit   yes
page count           1
requested page       1
```

The source is intentionally synthetic. This qualification proves public facade size-gating, isolation, reuse and host projection mechanics. It does not claim that one sparse synthetic source represents the performance characteristics of every naturally complex 200+ MiB PDF.

## 2. Call 1: isolate then text

One `codex.pdf_access` call used explicit `text`, `pages:[1]`, `maxCharacters:10000`.

```text
facade schema        codexless.pdf-access-orchestrator.v1
policy schema        codexless.pdf-access-policy.v1
requested/effective  text / text
primary route        isolate-then-text
needsSplitProfile    true
text mode            isolated
generation status    generated
generation kind      page-isolation
generation key       24ef9217052288d105762fbea1e7148e3e2c736f7652c4d69be22c46c7fc0f43
generation id        0001788718124984-8e90ea76-154f-46ab-97ef-b3fc9ba00232
```

The generated managed artifact was:

```text
file name            isolate-p1-534f32c53733.pdf
artifact SHA-256     534f32c537334241d7cd3c3a9d571f919e7f3851c246171e67772b18849a5f03
artifact bytes       862
sourcePageMap        [1]
```

The isolated text adapter returned artifact page 1 mapped to original source page 1:

```text
ADS Hybrid PDF Isolation Qualification
Page 1: isolate then text and render
Original source page provenance must remain 1.
```

The result contained 122 characters, was not truncated, reported `sourcePageNumber:1`, performed no OCR, and projected zero resource links and zero images.

## 3. Call 2: isolate then render

A second `codex.pdf_access` call used explicit `visual` and `visualPages:[1]`.

```text
requested/effective  visual / visual
primary route        isolate-then-render
visual mode          isolated
generation status    reused
generation key       24ef9217052288d105762fbea1e7148e3e2c736f7652c4d69be22c46c7fc0f43
generation id        0001788718124984-8e90ea76-154f-46ab-97ef-b3fc9ba00232
artifact SHA-256     534f32c537334241d7cd3c3a9d571f919e7f3851c246171e67772b18849a5f03
sourcePageMap        [1]
```

The facade returned one MCP PNG mapped to original source page 1:

```text
width                 1275
height                1651
bytes                 48,898
SHA-256               aeb0cb98eb4ac5fc31ae099f42882e7c3d0c0bfdae6254b29bb2d865e3514427
sourcePageNumber      1
resourceLinkCount     0
imageCount            1
ocrPerformed          false
```

ChatGPT directly inspected the same-call image. It visibly shows the large title `ADS Hybrid PDF Isolation Qualification`, the two provenance/isolation text lines, a large outlined rectangle and a horizontal line. No extra ADS image-read tool was needed.

The renderer emitted the standard Node warning that `--allow-addons` must be used with extreme caution because it can invalidate the permission model. This does not negate the functional isolation-route result, but it is preserved as a security-hardening caution: the maintained native canvas addon is trusted, while the Node permission model must not be described as an OS-grade security boundary merely because this route passes.

## 4. Call 3: isolate then text plus render

A third `codex.pdf_access` call used explicit `mixed`, `pages:[1]`, `visualPages:[1]`, `maxCharacters:10000`.

```text
requested/effective  mixed / mixed
primary route        isolate-then-text-plus-render
text mode            isolated
visual mode          isolated
text generation      reused
visual generation    reused
generation key       24ef9217052288d105762fbea1e7148e3e2c736f7652c4d69be22c46c7fc0f43
generation id        0001788718124984-8e90ea76-154f-46ab-97ef-b3fc9ba00232
```

Both modalities reused the exact same 862-byte managed artifact and preserved `sourcePageNumber:1`. Text again returned the same 122 characters without truncation. The image again returned `1275 x 1651`, 48,898 bytes and SHA-256 `aeb0cb98eb4ac5fc31ae099f42882e7c3d0c0bfdae6254b29bb2d865e3514427`. Direct ChatGPT inspection again succeeded.

## 5. Source integrity and source-workspace cleanliness

After all three facade calls, an independent read-only hash check still returned:

```text
source bytes    211,813,221
source SHA-256  00dfd5d9a983647bf7e35ee884796bc5f629807a1a1253ef613c42492e75c9c7
```

A read-only directory listing of the source test directory contained exactly one file, the original synthetic source. No split PDF, isolated PDF, PNG or manifest was written beside it. The reusable derived PDF therefore remained in the Codexless-owned managed artifact layer rather than becoming a source-adjacent file.

## 6. Result and claim scope

```text
SOURCE_ABOVE_192_MIB                    PASS
ISOLATE_THEN_TEXT                       PASS
ISOLATE_THEN_RENDER                     PASS
ISOLATE_THEN_TEXT_PLUS_RENDER           PASS
ORIGINAL_SOURCE_PAGE_PROVENANCE         PASS
MANAGED_ARTIFACT_FIRST_GENERATION       PASS
MANAGED_ARTIFACT_REUSE                  PASS
DIRECT_CHATGPT_TEXT_CONSUMPTION         PASS
DIRECT_CHATGPT_IMAGE_CONSUMPTION        PASS
SOURCE_HASH_UNCHANGED                   PASS
NO_SOURCE_ADJACENT_DERIVED_FILES        PASS
OCR                                     NO
PDF_RESOURCE_LINKS                      0
PUBLIC_PDF_ROUTE_FAMILY                 QUALIFIED
```

Together with Checkpoints 320, 321 and 327, this closes the accepted Research 120 public PDF route family: native whole/split/hybrid behavior, direct text/render/mixed behavior, auto routing, and >192 MiB isolation are all qualified through the public facade.

## 7. Synthetic source cleanup

After all route, reuse, direct-inspection, source-hash and source-directory evidence above had been captured, the generated 211,813,221-byte synthetic test PDF was removed through an exact-path, exact-size-guarded cleanup inside protected private-runtime `.tmp`. The now-empty dedicated test directory was also removed. The cleanup reported:

```text
SYNTHETIC_ISOLATION_SOURCE_CLEANUP=PASS
fileExists=false
dirExists=false
```

No user source or repository-tracked file was deleted. The synthetic payload is therefore not retained merely to preserve this qualification; the repository record owns the durable evidence.
