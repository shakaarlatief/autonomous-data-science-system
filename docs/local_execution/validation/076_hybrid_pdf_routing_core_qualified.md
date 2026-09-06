# Validation 076: Hybrid PDF Routing Core Qualified

**Date:** 2026-09-06
**Status:** CORE END-TO-END PASS / PUBLIC FACADE NEXT
**Research:** Research 120
**Scope:** Qualify the internal model-free automatic PDF routing core after the controlled restart, including the live 192 MiB direct-processing envelope, source profiling, deterministic native splitting, very-large-source page/range isolation, managed content-addressed artifact reuse, embedded-text and visual access to cached artifacts, ephemeral cached-PDF resources, and the high-level deterministic orchestrator. No new MCP tool is published at this boundary.

## 1. Live 192 MiB post-restart qualification

The restarted public runtime was exercised against one valid synthetic PDF above the previous 96 MiB boundary:

```text
source size       134,218,426 bytes
source SHA-256    26baf8fd80dfa447fba1a2be2dd7ab8f2d48f6f630ae623e38864ae7037fe532

document_read
    PASS
    page count     1
    embedded text  live 192 MiB runtime qualification

document_render
    PASS
    PNG bytes      23,067
    dimensions     1275 x 1651
    PNG SHA-256    9f9f2f95299b11d30eb70ff212eeb77a46179943090fa11680a0fa9d1d0796bc
```

The temporary qualification source was removed after the checks.

This closes the Checkpoint 317 restart-pending boundary:

```text
LIVE_192MIB_DOCUMENT_READ   = PASS
LIVE_192MIB_DOCUMENT_RENDER = PASS
```

## 2. Implemented private core

The Research 120 candidate now contains:

```text
PdfSourceProfiler
PdfAccessPolicy
PdfNativeSplitter
PageRangeIsolator
PdfArtifactManager
PdfArtifactTextReader
PdfArtifactRenderer
PdfArtifactResourceStore
PdfAccessOrchestrator
```

The architecture keeps the original authorized PDF as the sole source of truth. Generated PDFs are stored only in Codexless-managed state, never beside the source file.

Default logical state layout:

```text
~/.config/codexless/pdf-artifacts/v1/
    sets/<authority/source/derivation-key>/<immutable-generation>/
        manifest.json
        .access
        derived PDFs
    staging/
```

## 3. Authority and cache behavior

The implemented cache contract includes:

```text
workspace authority resolved from original source
canonical source path containment
streaming SHA-256 source identity
source size / mtime / file identity
source revalidation before generation
source revalidation after generation
source revalidation before cached artifact lease
source revalidation again before resource fetch
content-addressed derivation keys
immutable completed generations
staging then atomic directory promotion
corrupt artifact rejection and regeneration
reuse after manager reconstruction
quota/idle pruning mechanism
no eviction while an artifact/resource is actively leased
```

Source drift with the same filename does not reuse the old generation because the source SHA changes. Loss of original source authority cannot be bypassed through a cached derivative.

## 4. Native splitter / isolator

The selected implementation uses maintained primary-runtime Python with exact qualified dependency:

```text
pypdf 6.10.0
```

Native split rules:

```text
conservative part target      7,000,000 bytes
preserve source page order    YES
maximal contiguous ranges     YES
exact serialized size         YES
oversized one-page detection  YES
source-page provenance        YES
silent raster-as-native       NO
```

The page/range isolator is independent of the 192 MiB whole-source text/render admission. It can produce one bounded native derived PDF for selected pages from a larger source, after which the existing text/render semantics operate on the bounded artifact.

## 5. Very-large-source end-to-end qualification

A valid sparse PDF above the 192 MiB processing envelope was used to exercise the new fallback:

```text
source > 192 MiB
    -> source profile
    -> isolate original page 1
    -> bounded cached native PDF
    -> second request reuses same generation
    -> embedded text extraction from artifact
    -> page rendering from artifact
    -> map both outputs back to original source page 1
```

Observed result:

```text
ISOLATION_GENERATION       = PASS
ISOLATION_REUSE            = PASS
CACHED_ARTIFACT_TEXT       = PASS
CACHED_ARTIFACT_RENDER     = PASS
SOURCE_PAGE_PROVENANCE     = PASS
SOURCE_WORKSPACE_WRITE     = NONE
OCR                        = NONE
REASONING_MODEL_INTERMEDIARY = NONE
```

## 6. Cached embedded-text dependency correction

The private candidate originally exposed a qualification-layout issue: its copied parser child could not find `pdfjs-dist` because the candidate intentionally did not duplicate installed third-party `node_modules`.

The corrected design preserves the existing pinned parser contract while resolving the server-owned Codexless dependency explicitly:

```text
pdfjs-dist 5.4.624
```

The parser child receives only a server-resolved owned dependency root and remains under Node permission restrictions. No ad-hoc junction or copied dependency tree is required.

## 7. Splitter fidelity

A multi-page synthetic PDF was split into multiple native PDF parts. Every original source page and the corresponding generated-part page were independently rendered through the maintained PDF.js + `@napi-rs/canvas` stack.

For every page:

```text
width           identical
height          identical
rendered PNG SHA-256 identical
```

Result:

```text
NATIVE_SPLIT_RENDER_EQUIVALENCE = PASS
```

## 8. Candidate regression suite

Combined result:

```text
tests       42
pass        42
fail        0
cancelled   0
skipped     0
```

Coverage includes:

```text
route policy
high-level orchestrator
source identity / path containment / drift
native splitter
page-range isolator
artifact generation and reuse
corruption regeneration
reuse after manager reconstruction
eviction and deterministic regeneration
failed-generation atomic cleanup
lease-aware pruning
cached PDF text
cached PDF rendering
cached PDF MCP resource bytes
very-large-source isolation
splitter rendered-page equivalence
```

## 9. Real registered Machine Learning corpus

Read-only `pypdf 6.10.0` split planning against `32.LinearModels2.annotated.pdf` produced:

```text
pages 1-34     6,851,116 bytes
pages 35-38    1,646,076 bytes
oversized      none
```

Read-only planning against the 78,874,939-byte `51.Deep Learning2.annotated.pdf` produced 14 native parts plus two oversized individual pages:

```text
pages 1-7      4,380,348
pages 8-11     5,506,735
pages 12-14    6,432,947
page 15        5,984,175
page 16        OVERSIZED 15,944,609
pages 17-19    5,509,372
page 20        2,882,176
page 21        4,748,084
pages 22-27    6,978,607
pages 28-36    2,677,586
page 37        5,126,178
pages 38-41    6,952,103
page 42        6,586,933
pages 43-48    3,804,720
page 49        OVERSIZED 7,784,782
pages 50-56    2,866,873
```

This is exactly the intended native hybrid case: bounded native parts plus text/render fallback for oversized pages 16 and 49.

The annotated real PDFs also caused `pypdf` repair diagnostics such as `Ignoring wrong pointing object ...`. The implementation preserves bounded worker warnings in generated manifests instead of suppressing them silently.

## 10. High-level orchestrator

The private `PdfAccessOrchestrator` passed route tests for:

```text
native small source
    -> unchanged whole PDF resource

native larger source
    -> cached native parts

native oversized page
    -> native parts + text/render fallback

text <=192 MiB
    -> direct text

visual <=192 MiB
    -> direct render

mixed <=192 MiB
    -> text + selected source-page render

text >192 MiB
    -> selected-page isolation -> cached text

visual >192 MiB
    -> selected-page isolation -> cached render

mixed >192 MiB
    -> one isolation when visual pages are a subset of text pages
    -> a second isolation only when necessary
```

The initiating ChatGPT model remains responsible for semantic intent and relevant-page selection. The router itself remains deterministic/model-free.

## 11. Private preservation

The implementation and qualification evidence are preserved in the private local-runtime repository at:

```text
3cf995e358425c4db970337f0413a8862bb5a564
Qualify hybrid PDF routing core
```

Private push result:

```text
RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
postflightOk=true
local HEAD == origin/main
tracked working tree clean
```

## 12. Result

```text
LIVE_192MIB_RUNTIME              = PASS
HYBRID_ROUTE_POLICY              = PASS
PDF_SOURCE_PROFILER              = PASS
NATIVE_SPLITTER                  = PASS
PAGE_RANGE_ISOLATOR              = PASS
MANAGED_ARTIFACT_CACHE           = PASS
CACHE_RESTART_REUSE              = PASS
CACHE_EVICTION_REGENERATION      = PASS
ATOMIC_GENERATION_FAILURE        = PASS
SOURCE_DRIFT_INVALIDATION        = PASS
ACTIVE_LEASE_EVICTION_GUARD      = PASS
NATIVE_SPLIT_RENDER_EQUIVALENCE  = PASS
CACHED_EMBEDDED_TEXT             = PASS
CACHED_PAGE_RENDER               = PASS
CACHED_PDF_RESOURCE_STORE        = PASS
VERY_LARGE_SOURCE_TEXT           = PASS
VERY_LARGE_SOURCE_RENDER         = PASS
HIGH_LEVEL_ORCHESTRATOR          = PASS
PUBLIC_HIGH_LEVEL_MCP_FACADE     = NEXT
```

No public schema/tool-count change is made by this validation itself. The next bounded step is to integrate the qualified orchestrator into the live MCP runtime behind one high-level PDF access tool, verify content/resource/image projection and full surface regressions, then publish it only after those gates pass.
