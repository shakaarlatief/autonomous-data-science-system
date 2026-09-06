# Validation 075: Hybrid PDF Routing Architecture and 192 MiB Source Published

**Date:** 2026-09-06
**Status:** ARCHITECTURE ACCEPTED / POLICY STATIC PASS / 192 MiB INSTALLED SOURCE PUBLISHED / RESTART PENDING
**Research:** Research 120
**Scope:** Preserve the accepted automatic hybrid PDF routing architecture, the managed content-addressed artifact-cache decision for generated split PDFs, the first deterministic route-policy candidate, and the installed-source increase of `document_read` / `document_render` from 96 MiB to 192 MiB.

## Architecture result

Research 120 accepts the following hierarchy:

```text
native/container request
    <= 7,000,000 bytes
        -> whole-file document_file_link
    > 7,000,000 bytes
        -> deterministic native PDF parts <= 7,000,000 bytes
    individual native page still oversized
        -> embedded text + rendered-page fallback

text request
    <= 192 MiB source
        -> document_read
    > 192 MiB source
        -> isolate bounded page/range -> document_read

visual request
    <= 192 MiB source
        -> document_render
    > 192 MiB source
        -> isolate bounded page/range -> document_render

mixed request
    -> text breadth + selective vision
    -> isolation first when source exceeds direct-processing envelope
```

The 7,000,000-byte native target is deliberately separate from the 192 MiB direct-processing limit because the former is constrained by the observed ChatGPT host materialization envelope while the latter is a Codexless processing-policy boundary.

## Split-part storage decision

Generated split PDFs must not be written beside the user's source files and must not be regenerated unconditionally on every request.

Accepted storage model:

```text
original PDF
    remains source of truth

Codexless-owned managed artifact cache
    -> small durable manifest
    -> reusable split PDF bytes / derived page artifacts
    -> bounded cache lifecycle
    -> deterministic regeneration after eviction
```

Logical artifact-set identity includes:

```text
workspaceId
source SHA-256
derivation/version identity
native-part target bytes
```

A cached derivative never becomes an independent authority object. Current source authority and source identity must be revalidated before reuse. Source drift creates a new artifact generation.

## 192 MiB candidate

Installed direct-processing changes:

```text
document_read source ceiling
    96 MiB -> 192 MiB

document_read parser child heap
    256 MiB -> 384 MiB

document_render source ceiling
    96 MiB -> 192 MiB
```

No public MCP schema/tool-count change was made.

The native whole-file resource-link preparation path was not raised merely for symmetry. Automatic routing should not select unchanged whole-file materialization beyond the conservative 7,000,000-byte host target.

## Static / feasibility verification

Private 192 MiB candidate checks:

```text
syntax checks                                      PASS
focused source-bound tests                         5 / 5 PASS
reader 128 MiB admission                           PASS
reader >192 MiB rejection                          PASS
renderer 128 MiB admission                         PASS
renderer >192 MiB rejection                        PASS
```

Maintained PDF.js/canvas feasibility on a valid synthetic >96 MiB PDF:

```text
source bytes      134,218,424
page count        1
embedded text     large 128 MiB pdfjs render smoke
rendered PNG      25,643 bytes
observed RSS      approximately 353 MiB
status            PASS
```

Installed source was then exercised directly with the actual pinned parser:

```text
source bytes      134,218,421
new max bytes     201,326,592
parser            pdfjs-dist 5.4.624
parser child heap 384 MiB
embedded text     large 128 MiB installed smoke
status            PASS
```

Temporary smoke artifacts were removed.

## Installed-source identities

Pre-publication hashes preserved as rollback backups:

```text
document-reader.mjs
42d1479f53558dfedbe048d29011229a88ca551e13d5fdd2970130a52eb31b58

document-reader-child.mjs
588e14597e6dc39270860c00044e2ac7e720ffbaf045fbdb6e900162c421b140

document-renderer.mjs
e8028cc913346b1d415aa419b252ed0efaf374b8d145ac08ddb836224b393f0f
```

Installed source after publication:

```text
document-reader.mjs
3888306fc880a8a463f165270a7235ab514a3b7f7913b869e3b2828df7d73b25

document-reader-child.mjs
08df457a76aff3d8fa83a3dec6113f4d6298a0f7bc1dc247f2e489244916a8e0

document-renderer.mjs
89344854a8f6955a0be67107d33587ab96d182af84f19b3cfe7e0c14110a91d0
```

All installed files passed syntax checks.

## Automatic-route policy candidate

A private policy-only implementation now exists for the first architecture seam. It deterministically maps caller intent and source bounds onto the proven primitives and derives an authority-scoped artifact-set key.

Policy test result:

```text
8 / 8 PASS
```

Covered routes include native whole file, split profiling, native parts plus oversized-page fallback, direct text, direct render, mixed text+vision and isolation above 192 MiB.

The policy candidate does not yet generate/cache artifacts or change the public MCP surface.

## Private preservation and durable workspace registry

The private runtime candidates and their tests are synchronized to `origin/main` at:

```text
fde55f1db3191086431f5a7d56fc416c1beebfa1
RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
postflightOk=true
```

The temporary exact-root `codexless-live` publication admission was removed after source publication/testing. Durable registry after removal:

```text
revision       14
content hash   7fb25c275497228e537a5bca518d75eb8d1ef61ab111676d9ff696c40a276129
workspaces     ads-public, ads-local-runtime, big-data-statistics, machine-learning
```

The Machine Learning workspace remains read-only.

## Restart boundary

The installed files are published, but the currently running Codexless process predates the 192 MiB publication. One controlled Codexless/tunnel restart is required before the public `codex.document_read` and `codex.document_render` tools expose the new envelope.

No Plugin refresh is required.

## Result

```text
RESEARCH_120_ARCHITECTURE = ACCEPTED_FOR_IMPLEMENTATION
SPLIT_STORAGE = MANAGED_CONTENT_ADDRESSED_CACHE
SOURCE_FOLDER_WRITES = NONE
ALWAYS_RESPLIT = NO
CACHE_REUSE_WITH_SOURCE_REVALIDATION = YES
DIRECT_PROCESSING_LIMIT = 192_MIB
NATIVE_HOST_TARGET = 7000000_BYTES
ROUTE_POLICY_STATIC_TESTS = 8_8_PASS
INSTALLED_GT96MIB_TEXT_SMOKE = PASS
LIVE_192MIB_PROCESS_RESTART = PENDING
NEXT = RESTART_THEN_IMPLEMENT_ARTIFACT_MANAGER_AND_SPLITTER_ISOLATOR
```
