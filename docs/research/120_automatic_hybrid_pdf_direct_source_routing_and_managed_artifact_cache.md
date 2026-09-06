# Research 120: Automatic Hybrid PDF Direct-Source Routing and Managed Artifact Cache

**Date:** 2026-09-06
**Status:** ACTIVE / FRESH-CHAT NATIVE SPLIT QUALIFIED / MIXED TEXT-VISION NEXT
**Scope:** Define the professional automatic routing architecture for direct ChatGPT access to authorized local PDFs across whole-file handoff, native PDF splitting, embedded-text extraction and rendered-page vision; define how generated split PDFs should be stored/reused without modifying source workspaces; and replace repeated ad-hoc source-limit increases with a bounded direct-processing envelope plus deterministic isolation fallback for very large sources.
**Declared references:** `research:119`, `checkpoint:311`, `checkpoint:312`, `checkpoint:314`, `checkpoint:316`, `path:docs/OPEN_ARCHITECTURE_BACKLOG.md`

## 1. Current proven primitives

Research 119 now has four complementary PDF primitives that are all direct-source, model-free routes into ordinary ChatGPT:

```text
codex.document_file_link
    actual/native PDF resource handoff

codex.document_read
    embedded PDF text -> ChatGPT text context

codex.document_render
    rendered PDF page -> ChatGPT native vision

deterministic native PDF splitting
    oversized source -> smaller native PDF parts -> document_file_link
```

Checkpoint 311 qualified deterministic multi-native-PDF handoff. Checkpoint 314 qualified direct page rendering from a 78,874,939-byte source. Checkpoint 316 qualified direct embedded-text extraction from the same source.

The remaining problem is no longer whether the mechanisms work independently. The remaining problem is how they should be selected, combined, cached and regenerated automatically and safely.

## 2. Separate the host-native envelope from Codexless processing envelopes

Two different classes of limits must remain explicit.

### Native ChatGPT PDF materialization

The clean observed host interval remains:

```text
highest clean whole-PDF PASS  7,417,428 bytes
lowest clean whole-PDF FAIL    7,993,210 bytes
```

The enforcing host component remains outside current Codexless control. Automatic routing must therefore use a conservative native target rather than assuming that increasing a Codexless constant raises ChatGPT's host materialization limit.

Accepted conservative native target:

```text
NATIVE_WHOLE_TARGET_BYTES = 7,000,000
NATIVE_PART_TARGET_BYTES  = 7,000,000
```

### Direct text/render processing

The 96 MiB `document_read` / `document_render` ceiling was a Codexless policy limit and is under our control. It was introduced as a qualified intermediate safety boundary, not a fundamental maximum.

The next bounded operational ceiling is:

```text
DIRECT_SOURCE_LIMIT_BYTES = 192 MiB = 201,326,592 bytes
```

This is intentionally a larger but still bounded direct-processing envelope. It comfortably covers ordinary 100-150 MB PDFs while preserving process/memory isolation. It is not the final architecture for arbitrarily large documents.

The text parser child heap is correspondingly raised from 256 MiB to 384 MiB. The renderer continues to hash sources in bounded chunks and does not retain two whole-source parent buffers.

The architecture explicitly rejects the pattern:

```text
96 MiB fails
-> change to 128 MiB
-> 128 MiB fails
-> change to 256 MiB
-> repeat forever
```

For sources above the direct-processing envelope, the correct long-term behavior is page/range isolation before text extraction or rendering.

## 3. User-intent-first routing

The best transport depends on what the user actually needs.

The initiating ChatGPT model determines the semantic intent from the conversation. Codexless then applies deterministic routing policy to the authorized source and requested modality.

Canonical intents:

```text
native
    user needs the actual PDF/container semantics or wants normal ChatGPT PDF attachment behavior

text
    user primarily needs searchable/extractable embedded text

visual
    user primarily needs figures, diagrams, layout, images, equations or page appearance

mixed
    user needs both textual and visual source evidence

auto
    caller has no stronger requirement; prefer efficient text breadth and add vision selectively
```

The route planner itself is model-free. It never interprets document semantics.

## 4. Automatic route matrix

### Native/container request

```text
source <= 7,000,000 bytes
    -> unchanged whole-file document_file_link

source > 7,000,000 bytes
    -> deterministic native split profile
    -> maximal contiguous native PDF parts <= 7,000,000 bytes
    -> document_file_link each part

individual source page still > 7,000,000-byte native-part target
    -> do not pretend native preservation is possible for that page
    -> mark the page as an oversized-page fallback
    -> provide embedded text + rendered page directly to ChatGPT
```

### Text request

```text
source <= 192 MiB
    -> document_read directly on requested page/range

source > 192 MiB
    -> isolate only the required page/range into a bounded derived PDF
    -> document_read the isolated PDF
```

### Visual request

```text
source <= 192 MiB
    -> document_render directly on requested page(s)

source > 192 MiB
    -> isolate requested page/range first
    -> document_render the isolated artifact
```

### Mixed request

```text
source <= 192 MiB
    -> embedded text for breadth
    -> selective page rendering where visual context matters

source > 192 MiB
    -> isolate bounded page/range artifacts
    -> text + selective render over those artifacts
```

For broad-document questions where relevant pages are not yet known, text should normally provide the inexpensive breadth pass and vision should be added selectively after relevant pages are identified.

## 5. Generated split PDFs are transport artifacts, not new source files

The original local PDF remains the source of truth.

Rejected design:

```text
C:\...\Machine Learning\large.pdf
C:\...\Machine Learning\large.part01.pdf
C:\...\Machine Learning\large.part02.pdf
...
```

Reasons:

```text
- source workspaces such as `machine-learning` are intentionally read-only;
- generated transport files would clutter the user's source folders;
- stale parts could survive after the source changes;
- duplicate files would become ambiguous sources of truth;
- cleanup and naming collisions become user-facing concerns.
```

Also rejected as the default:

```text
never save anything
-> re-split the full PDF from scratch on every request
```

That is correct but unnecessarily expensive for repeated use of large documents.

## 6. Accepted storage architecture: managed content-addressed artifact cache

The professional design is a third option:

```text
authorized source PDF
    -> source identity / SHA-256
    -> deterministic derivation manifest
    -> Codexless-owned managed artifact cache
         manifest
         native PDF parts when generated
         optional bounded page artifacts/renders when worth caching
```

The cache belongs to Codexless, not to the source workspace.

### Logical artifact-set identity

A derived artifact set is keyed by at least:

```text
workspaceId
source SHA-256
derivation/version identifier
native part target bytes
```

This means:

```text
same source + same algorithm/policy
    -> same logical artifact set

source content changes
    -> different SHA-256
    -> different artifact set

splitting algorithm/target changes
    -> different derivation key
```

The workspace identity remains part of the key/binding so a content hash by itself is never treated as authorization.

### Manifest is durable; large artifact bytes are cacheable

The recommended lifecycle is:

```text
small manifest
    -> persist as cheap provenance/index state

split PDFs / renders
    -> reusable managed cache entries
    -> bounded by server-owned disk policy
    -> may be evicted

artifact missing after eviction
    -> regenerate deterministically from the authorized source
```

This gives the user the practical benefit of persistent reuse without turning derived parts into permanent source files.

A manifest should record at least:

```text
workspaceId
source relative path
source SHA-256
source byte size
source page count
source identity timestamps needed for revalidation
splitter engine + version
routing/derivation version
native part target bytes
ordered page ranges
part byte sizes
part SHA-256 values
oversized native pages
generation timestamp
```

## 7. Authority and source-drift rules for cached artifacts

A cached split PDF is not an independent authority object.

Every access must still resolve the current workspace authority for the original source and revalidate the source binding before exposing a derived artifact.

```text
cached artifact exists
    + source authority still valid
    + source identity/hash still matches
        -> reuse

source identity changed
    -> cached artifact is stale
    -> do not serve it as current source evidence
    -> build a new artifact generation

source no longer authorized/available
    -> cached derivative must not become a bypass around source authority
```

This is critical even in a single-user local deployment because the architecture should not make cached derived data a hidden exfiltration surface.

## 8. Atomic and deterministic generation

Split generation should be crash-safe and reproducible.

Recommended sequence:

```text
1. resolve current source authority
2. canonicalize source path
3. record source size / mtime / file identity
4. compute source SHA-256
5. compute deterministic partition plan
6. write generated artifacts only inside a Codexless-owned staging area
7. compute every generated artifact SHA-256
8. verify source identity again
9. write/replace manifest atomically
10. atomically promote staged artifacts into the managed cache
```

An interrupted generation must leave either the previous complete generation or no generation, never a partially authoritative manifest.

## 9. Native split algorithm

The qualified Checkpoint 311 behavior remains the basis:

```text
- preserve page order;
- choose maximal contiguous page ranges whose serialized native PDF is <= 7,000,000 bytes;
- use exact serialized output size, not source-byte averages;
- keep source-page provenance in generated metadata;
- flag any single page whose one-page native PDF exceeds the target;
- never silently rasterize an oversized page and call it a native part.
```

The production implementation should use a maintained deterministic PDF library from the managed runtime. `pypdf 6.10.0` and `pdf-lib 1.17.1` are both present in the current primary runtime; the final splitter engine should be selected by fidelity/regression evidence rather than convenience alone.

## 10. Very large source architecture above 192 MiB

The 192 MiB ceiling should reduce near-term friction, but the router must not depend on it indefinitely.

For a very large source, for example a 600 MiB textbook where the user asks about page 317, the desired path is:

```text
600 MiB source
    -> bounded source profiler / isolator
    -> isolate page 317 or a small relevant range
    -> bounded derived PDF
        -> document_read
        -> document_render
```

The architecture should therefore introduce a model-free page/range isolator whose admission limit is independent of the direct text/render worker's whole-source buffering strategy.

The isolator may internally use a managed library and Codexless-owned temporary/cache storage, but it must remain authority-bounded and must not require write access to the source workspace.

## 11. Cache retention policy

Generated artifacts are a cache, not an archive.

The final production cache should have:

```text
bounded total disk quota
LRU/idle-age eviction
atomic cleanup
manifest-aware regeneration
no eviction while an artifact/resource is actively leased
```

The first product candidate now uses a bounded 2 GiB total managed-artifact quota and a 30-day idle horizon. These are operational defaults, not fundamental architectural maxima. They can be recalibrated from corpus/usage evidence without changing the source-authority or regeneration model.

Small manifests may be retained longer than the large byte artifacts because they are cheap and accelerate deterministic reconstruction.

## 12. Failure and fallback behavior

The router must fail over between faithful direct-source representations rather than inserting a reasoning model.

Examples:

```text
whole-file host handoff too large
    -> native split

native single page too large
    -> embedded text + rendered page

direct text source above processing ceiling
    -> isolate page/range then text

direct render source above processing ceiling
    -> isolate page/range then render

rendered PNG above page-image ceiling
    -> future bounded lower-DPI/tiled rendering fallback
```

A semantic Codex/Astra worker remains a separate optional delegated-analysis capability and is not part of this automatic direct-source fallback chain.

## 13. First implementation seam

The implementation should be layered rather than replacing the proven primitives.

```text
DocumentSourceProfiler
    authority + identity + type + size + page metadata

PdfAccessPolicy
    deterministic intent/size/capability route decision

PdfArtifactManager
    content-addressed manifest/cache lifecycle

PdfNativeSplitter / PageRangeIsolator
    deterministic derived PDF generation

existing primitives
    document_file_link
    document_read
    document_render
```

The first private policy candidate already implements deterministic route selection and an authority-scoped artifact-set key without changing the public MCP surface.

A future high-level public facade may wrap these pieces, but the exact public tool contract should be frozen only after the managed splitter/cache implementation is proven. Existing low-level primitives should remain available for qualification and debugging.

## 14. Verification strategy

Minimum qualification before promotion:

```text
route-policy unit tests
    small native -> whole file
    large native -> split profile
    oversized native page -> native parts + text/render fallback
    text/visual <= direct source ceiling -> direct primitive
    text/visual > direct source ceiling -> isolation route

cache tests
    deterministic key
    source drift invalidation
    authority revalidation
    atomic generation
    reuse after restart
    eviction + deterministic regeneration

splitter fidelity
    rendered-page equality/source-equivalence checks
    page order
    metadata/provenance
    oversized-page detection

real corpus
    Machine Learning large PDFs
    at least one source above 96 MiB
    at least one oversized single page
```

## 15. Accepted architecture disposition

```text
DIRECT_PROCESSING_SOURCE_CEILING
    192 MiB operational bound
    not a fundamental maximum

NATIVE_CHATGPT_TARGET
    7,000,000 bytes conservative target

SPLIT_PART_STORAGE
    Codexless-managed content-addressed artifact cache
    never source-adjacent by default

PERSISTENCE
    durable manifest + reusable cache bytes
    bytes may be evicted and regenerated deterministically

AUTHORITY
    always inherited/revalidated from original authorized source

AUTOMATIC_ROUTING
    intent-aware deterministic policy over proven primitives

VERY_LARGE_SOURCE
    isolate bounded page/range before text/render

NEXT
    controlled restart of the published preview.16 source;
    verify local 60-tool health and tunnel readiness;
    refresh the developer MCP app;
    fresh-chat discovery and representative codex.pdf_access qualification
```

## 16. Checkpoint 318 implementation qualification

The first two items in the earlier `NEXT` sequence are now complete.

### Live 192 MiB envelope

After the controlled restart, the existing public `codex.document_read` and `codex.document_render` tools both passed against the same valid 134,218,426-byte PDF. The direct-processing extension is therefore live-qualified rather than merely source-published.

### Managed core

The private implementation now includes:

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

Combined private regression result:

```text
42 / 42 PASS
```

The qualification covers the requirements identified in Section 14:

```text
route-policy tests                     PASS
source drift invalidation              PASS
authority revalidation                 PASS
atomic generation cleanup              PASS
reuse after manager reconstruction     PASS
eviction + deterministic regeneration  PASS
lease-aware eviction protection        PASS
rendered-page split equivalence         PASS
page order/provenance                   PASS
oversized-page detection                PASS
real Machine Learning corpus            PASS
```

A valid source above 192 MiB was also isolated to a bounded page artifact and then used for both embedded-text extraction and page rendering, with the result mapped back to the original source page. This closes the core very-large-source path experimentally.

The selected native splitter implementation is maintained primary-runtime `pypdf 6.10.0`. Real annotated Machine Learning PDFs emit bounded repair diagnostics for malformed object pointers; these warnings are preserved in generated manifests rather than silently discarded.

`51.Deep Learning2.annotated.pdf` now provides the representative mixed-native case under the accepted algorithm: all ordinary ranges fit the 7,000,000-byte native target while pages 16 and 49 remain individually oversized and therefore route to embedded text + rendered-page fallback.

The implementation is preserved in the private local-runtime repository at:

```text
3cf995e358425c4db970337f0413a8862bb5a564
RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
postflightOk=true
```

No new public MCP action has been exposed yet. The remaining Research 120 implementation step is now:

```text
qualified PdfAccessOrchestrator
    -> bounded public MCP facade
    -> resource_link projection for native whole/parts
    -> text projection for embedded text
    -> image projection for rendered pages
    -> full existing-surface regression
    -> guarded live publication only after PASS
```

Checkpoint 318 / Validation 076 are the detailed core-qualification boundary.

## 17. Checkpoint 319 public-facade publication boundary

The remaining public-facade implementation seam is now complete at the source-publication level.

The candidate exposes one bounded high-level action:

```text
codex.pdf_access
```

The public facade preserves the direct-source architecture rather than introducing a semantic worker. It projects native PDFs/parts as MCP `resource_link` content, embedded text as text metadata, and rendered fallback pages as ordinary MCP image content. The candidate also adds explicit result/cache bounds:

```text
native PDF resource links per result   <= 48
oversized-page fallback text           one shared total request budget
managed artifact quota                 2 GiB
managed artifact idle horizon          30 days
active leases                          protected from eviction
```

The combined private core/facade regression now passes:

```text
49 / 49 PASS
```

A staged mirror of the installed Codexless runtime also passes the adapted existing public regressions at the intended 60-tool candidate surface:

```text
bounded Git fetch                       PASS tools=60
bounded Git pull                        PASS tools=60
document file-read                      PASS tests=7
document render                         PASS tests=10
document resource-link                  PASS tests=9
image read                              PASS tests=7
public surface registration             PASS tools=60
```

The guarded host publication was then executed without widening ordinary workspace authority. Independent post-publication hashes show exact equality between the installed source/test payload and the qualified candidate/staging copies:

```text
source files matching candidate        17 / 17
adapted installed tests matching stage  4 / 4
```

The active process was intentionally not restarted by publication. It therefore remains on:

```text
0.1.1-preview.15-host-capability-probe
59 tools
```

with tunnel health/readiness still HTTP 200. This is a source-published, restart-pending state, not yet an end-to-end `codex.pdf_access` host qualification.

Private evidence is synchronized at:

```text
85b1de4bad00e71a723a6c7e3a89b959b2582241  Qualify hybrid PDF public facade candidate
8e2b98cfe5cd7eecafb9764dfd9e29b5602638d4  Record hybrid PDF live source publication
RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
postflightOk=true
```

Checkpoint 319 / Validation 077 are the detailed source-publication boundary.

## 18. Checkpoint 320 fresh-chat native split qualification

The preview.16 activation and first representative fresh-host route now pass end to end.

After the controlled restart and tunnel reconnect:

```text
version        0.1.1-preview.16-hybrid-pdf-access
toolCount      60
surfaceVersion codexless-public-preview-v2
tunnel health  200
tunnel ready   200
```

After the developer MCP app refresh, a fresh disposable ChatGPT conversation discovered `codex.pdf_access` and invoked it exactly once on:

```text
C:\School\Machine Learning\32.LinearModels2.annotated.pdf
intent=native
```

The facade selected:

```text
primary route  native-parts
native mode    parts
```

and returned the deterministic split previously qualified in the private/core evidence:

```text
pages 1-34   6,851,116 bytes
pages 35-38  1,646,076 bytes
```

The tool result contained metadata plus two PDF `resource_link` items and no inline PDF bytes/base64. The ChatGPT host then materialized both resources as actual conversation PDF files. Ordinary ChatGPT-side PDF tooling inspected the first materialized part successfully, confirmed 34 pages, and described concrete first-page visual/content structure.

This closes the native split route at the actual host boundary:

```text
authorized local PDF > native whole target
    -> codex.pdf_access
    -> deterministic managed native parts
    -> MCP resource_link projection
    -> host file materialization
    -> ordinary ChatGPT PDF inspection
```

No manual source upload, OCR, Browser, Agent, source-workspace write or reasoning-model intermediary was used.

The next bounded qualification is intentionally not another native split test. Use the same high-level facade against `51.Deep Learning2.annotated.pdf` to exercise mixed text/vision behavior and the individually oversized native pages 16 and 49. The goal is to prove that the facade can combine bounded native parts with direct embedded text and rendered-page image content in one automatic route, and that ChatGPT can consume those modalities without falling back to a semantic worker.

Checkpoint 320 / Validation 078 are the detailed fresh-host native split boundary.
