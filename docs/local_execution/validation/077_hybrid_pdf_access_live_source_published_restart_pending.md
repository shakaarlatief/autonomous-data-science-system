# Validation 077: Hybrid PDF Access Live Source Published, Restart Pending

**Date:** 2026-09-06
**Status:** PASS / LIVE SOURCE PUBLICATION VERIFIED / RESTART PENDING
**Research:** Research 120
**Scope:** Qualify the bounded public `codex.pdf_access` facade, regress the 60-tool public surface in a staged installed-runtime mirror, preserve the candidate in the private runtime repository, verify guarded host publication into the installed Codexless source/test tree, and distinguish published disk state from the still-running 59-tool process.

## 1. Public facade contract

The candidate adds one high-level read-only MCP action:

```text
codex.pdf_access
```

Accepted public inputs remain bounded to:

```text
cwd
documentPath
intent
pages
visualPages
visualRequired
maxCharacters
```

The facade does not accept caller-selected executables, output paths, resource URIs, permission profiles, sandboxes, Browser operations, OCR switches, Git routing, or Agent routing.

Canonical intents:

```text
native
text
visual
mixed
auto
```

## 2. Projection behavior

The facade projection can return one result containing ordinary MCP content of multiple faithful modalities:

```text
text metadata
application/pdf resource_link for original source PDF
application/pdf resource_link for managed native PDF artifacts
image/png content for rendered page fallbacks
```

Image base64 is removed from structured/text metadata. Managed artifact resource links use only server-owned `codexless://pdf-artifact/<token>` URIs. Original source links continue to use the existing server-owned document-resource scheme.

## 3. Result and cache bounds

The publication candidate includes:

```text
native PDF resource links per result   <= 48
oversized-page embedded text           one shared total request budget
managed cache total byte quota          2 GiB
managed cache idle horizon              30 days
active artifact/resource lease          prevents eviction
source authority revalidation           required before reuse/fetch
```

The source PDF remains the sole source of truth. Cached artifacts are transport derivatives, not independent authority objects.

## 4. Private candidate regression

Combined private suite:

```text
tests       49
pass        49
fail        0
cancelled   0
skipped     0
```

The additional public-facade qualification covers MCP projection, malformed projection rejection, native-resource result bounding, shared fallback text budgeting, and managed-cache pruning after successful access.

## 5. Staged installed-runtime regression

A complete staging mirror was assembled from the current installed Codexless runtime resources plus the candidate overlay. Required non-code runtime resources were copied into the stage before testing.

The first full regression correctly exposed stale test expectations rather than implementation defects:

```text
two Git-preservation scripts still expected 56 tools
installed render regression still described/asserted the superseded 96 MiB source ceiling
```

Those expectations were updated only to the already-accepted current boundary: 60 candidate tools and the already-live-qualified 192 MiB render-source ceiling.

Final staged regression:

```text
BOUNDED_GIT_FETCH_ORIGIN=PASS tools=60
BOUNDED_GIT_PULL_FF_ONLY=PASS tools=60
DOCUMENT_FILE_READ_REGRESSION=PASS tests=7
DOCUMENT_RENDER_REGRESSION=PASS tests=10
DOCUMENT_RESOURCE_LINK_REGRESSION=PASS tests=9
IMAGE_READ_REGRESSION=PASS tests=7
PUBLIC_SURFACE_REGISTRATION=PASS tools=60
```

The refactored candidate `DocumentReader` also passed a real read-only Machine Learning smoke on `32.LinearModels2.annotated.pdf`:

```text
source bytes  8,715,014
page count    38
selected page 1
text chars    2,000 requested/returned
OCR           false
result        PASS
```

## 6. Private preservation

The candidate was preserved and pushed at:

```text
85b1de4bad00e71a723a6c7e3a89b959b2582241
Qualify hybrid PDF public facade candidate
```

After live-source publication verification, the private evidence was updated and pushed at:

```text
8e2b98cfe5cd7eecafb9764dfd9e29b5602638d4
Record hybrid PDF live source publication
```

Both private pushes returned:

```text
RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
postflightOk=true
local HEAD == origin/main
tracked working tree clean
```

## 7. Guarded live publication

The normal `ads-local-runtime` workspace authority correctly refused direct writes into `%LOCALAPPDATA%\Codexless`; no authority was widened and no durable `codexless-live` workspace was registered.

A guarded ordinary-host PowerShell helper was therefore used. It bound the exact live baseline hashes and exact candidate hashes, required expected-new source files to be absent, reran qualification gates, used same-directory atomic replacement for existing files, timestamped backups, exact hash verification for changed/new files, and rollback to the verified baseline on failure. The helper intentionally did not restart Codexless.

The user reported completion. Independent read-only verification then established:

```text
LIVE_SOURCE_MATCH = PASS files=17
LIVE_TEST_MATCH   = PASS files=4
```

The 17 source matches include:

```text
codexless-runtime.mjs
document-reader.mjs
document-reader-child.mjs
document-render-child.mjs
document-renderer.mjs
mcp-server-factory.mjs
surface-contracts.mjs
document-access-policy.mjs
pdf-access-orchestrator.mjs
pdf-access-tool-projection.mjs
pdf-artifact-manager.mjs
pdf-artifact-renderer.mjs
pdf-artifact-resource-store.mjs
pdf-artifact-text-reader.mjs
pdf-native-splitter.mjs
pdf-native-worker.py
pdf-source-profiler.mjs
```

The four adapted installed regression files also match the qualified staged versions:

```text
bounded-git-fetch-origin.mjs
bounded-git-pull-ff-only.mjs
document-render-regression.mjs
public-surface-registration.mjs
```

## 8. Post-publication verification boundary

A read-only sandbox attempt to execute the installed regression scripts reconfirmed the first two pure-read Git-preservation checks at 60 tools, then stopped when a later regression attempted to create a temporary directory inside the installed test tree:

```text
EPERM: operation not permitted, mkdtemp ...\Codexless\test\.document-file-root-XXXXXX
```

This is an expected authority limitation of the read-only verification route. It is not evidence of a candidate or publication defect. The guarded host helper had already run the writable staged/installed regression gates before reporting success, and independent exact-hash verification provides the post-publication evidence.

## 9. Running process remains old until restart

Immediately after publication, the live process and tunnel remained healthy:

```text
Codexless ok       true
version            0.1.1-preview.15-host-capability-probe
toolCount          59
defaultCwd         expected ADS checkout
tunnel /healthz    HTTP 200
tunnel /readyz     HTTP 200
```

This is the expected state because source publication and process activation are deliberately separate operations.

## 10. Result

```text
PUBLIC_FACADE_SCHEMA                 = PASS
PUBLIC_FACADE_PROJECTION             = PASS
PRIVATE_CORE_REGRESSION              = PASS 49/49
STAGED_PUBLIC_SURFACE_REGRESSION     = PASS
PRIVATE_CANDIDATE_PRESERVATION       = PASS
GUARDED_LIVE_SOURCE_PUBLICATION      = PASS
LIVE_SOURCE_HASH_MATCH               = PASS 17/17
LIVE_TEST_HASH_MATCH                 = PASS 4/4
RUNNING_PROCESS_STILL_PREVIEW15      = PASS / EXPECTED
RUNTIME_AUTHORITY_WIDENING           = NONE
SOURCE_WORKSPACE_WRITE               = NONE
OCR                                  = NONE
REASONING_MODEL_INTERMEDIARY         = NONE
CONTROLLED_RESTART                   = NEXT
FRESH_CHAT_CODEX_PDF_ACCESS_TEST     = NEXT
```

The next step is the exact full controlled restart sequence in `docs/local_execution/OPERATIONS.md`, followed by local preview.16 / 60-tool health verification, tunnel readiness, ChatGPT app refresh, fresh-chat discovery, and representative end-to-end `codex.pdf_access` qualification.