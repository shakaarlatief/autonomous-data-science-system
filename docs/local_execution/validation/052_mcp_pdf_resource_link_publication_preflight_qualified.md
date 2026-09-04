# Validation 052: MCP PDF Resource-Link Publication Preflight Qualified

**Date:** 2026-09-04
**Status:** PASS / PUBLICATION PREFLIGHT QUALIFIED / LIVE HOST TEST PENDING
**Research:** Research 117
**Experiment:** E117-5f
**Live baseline:** `0.1.1-preview.12` / `codexless-public-preview-v2` / 55 tools
**Candidate target:** `0.1.1-preview.13` / `codexless-public-preview-v2` / 56 tools

## Purpose

Qualify the next reuse-first whole-PDF transport experiment after Validation 051 proved that an MCP-returned PDF can become a ChatGPT-side attachment but representative inline embedded-resource payloads are unsuitable. The candidate must keep the original tool result small, preserve existing ADS local-file authority, and expose the PDF bytes only through the standard MCP resource-read path referenced by a `resource_link`.

## Candidate semantic action

```text
codex.document_file_link
```

Public inputs remain exactly:

```text
cwd
documentPath
```

The tool reuses the existing `DocumentFileReader` for workspace authority, canonical containment, source identity, PDF validation, SHA-256, filename/size provenance and the conservative 4 MiB first-experiment source ceiling. It does not accept a caller URI or resource identifier.

The candidate creates a server-owned opaque resource URI:

```text
codexless://document-resource/<64-hex-random-token>
```

and returns a small tool result containing metadata plus:

```text
type      resource_link
name      original filename
mimeType  application/pdf
size      original byte size
uri       server-owned opaque resource URI
```

The PDF base64 is **not** embedded in the tool result. The same server registers an MCP `ResourceTemplate` for the server-owned URI scheme; a later `resources/read` returns the PDF as standard `application/pdf` blob resource content.

## Resource lifetime and boundedness

The initial candidate keeps prepared resources process-local and ephemeral:

```text
maximum prepared entries  8
TTL                       15 minutes
opaque token              256 random bits
caller-selected URI       false
persistent storage        false
```

The store is instantiated once at Codexless runtime scope, rather than once per per-request MCP server object, so a tool call and later `resources/read` can share the same prepared resource during the process lifetime.

## Focused regression

```text
DOCUMENT_RESOURCE_LINK_REGRESSION=PASS tests=8
```

Coverage includes preparation without inline PDF bytes, exact separate resource-read bytes, invalid-scheme rejection, unknown-token rejection and bounded capacity eviction.

The public-surface regression additionally verifies that:

```text
codex.document_file_link is registered
public tool count is 56
only cwd/documentPath are accepted
caller resourceUri/uri inputs are rejected
tool result types are [text, resource_link]
tool result contains no PDF base64
codex.document_resource ResourceTemplate is registered
its callback returns application/pdf blob bytes through resource read
```

## Integrated staging result

A complete stage from exact live preview.12 plus only the resource-link overlay passed:

```text
DOCUMENT_RESOURCE_LINK_REGRESSION=PASS tests=8
DOCUMENT_FILE_READ_REGRESSION=PASS tests=5
BOUNDED_GIT_FETCH_ORIGIN=PASS tools=56
BOUNDED_GIT_PULL_FF_ONLY=PASS tools=56
PUBLIC_SURFACE_REGISTRATION=PASS tools=56
IMAGE_READ_REGRESSION=PASS tests=7
DOCUMENT_RENDER_REGRESSION=PASS tests=10
DOCUMENT_RESOURCE_LINK_INTEGRATED_PREFLIGHT=PASS
EXPECTED_PUBLIC_SERVER_VERSION=0.1.1-preview.13
EXPECTED_PUBLIC_SURFACE_VERSION=codexless-public-preview-v2
EXPECTED_PUBLIC_TOOL_COUNT=56
TOOL_RESULT_CONTENT=resource_link/application-pdf
RESOURCE_READ_CONTENT=blob/application-pdf
TOOL_RESULT_EMBEDS_PDF_BYTES=false
MODEL_TURN_REQUIRED=false
BROWSER_REQUIRED=false
NEW_EXTERNAL_DEPENDENCY=false
```

The existing Checkpoint 289 loopback-render transport remains outside the overlay. The staged `codex-authority-executor.mjs`, `document-renderer.mjs`, `document-render-child.mjs`, document-render regression and existing document-file reader were pinned to the exact preview.12 live baseline.

## Guarded publication helper

Private ignored helper:

```text
.ads-private/codexless/activate-document-resource-link-publication.ps1
SHA-256 89F2AE146E3690F8E3EF198AF714C7624BD88D80F1564B92B638C3CD758DB4DD
```

Its no-publish run reproduced all accepted tests and ended with:

```text
DOCUMENT_RESOURCE_LINK_PUBLICATION_PREFLIGHT=PASS
PAUSED_LOOPBACK_RENDER_TRANSPORT_OVERLAID=false
NO_LIVE_FILES_MODIFIED=true
```

The helper pins exact live preview.12 and candidate hashes, stages only the resource-link overlay, uses `SupportsShouldProcess`, backs up/replaces only declared live files, adds only the new resource store/regression, rolls back touched paths on failure and performs no restart.

Candidate file hashes:

```text
src/document-resource-store.mjs          399ABA2CB5A1EBCE5D1C543F824D8D4B08F073F3BBEE3913CBB031966776C83A
src/codexless-runtime.mjs                8C12A02BF670724B6931F435F9BCE27E7ACF5990831C97FBF8DFC83DEDA36F31
src/mcp-server-factory.mjs               035956CB43B7D7712D04DF8345BA0F7C0B4965883DE5180731394D08D9018CD9
src/surface-contracts.mjs                39E4DFE91513F0FD5F7DF695475A0665887409DBF291E00CD4094EC526B6AA61
test/document-resource-link-regression.mjs 307C03509EC6A9ED143DDEBB51AFDC0D0AB177C74E4FC177B5FBE5A0D98FD321
test/bounded-git-fetch-origin.mjs        9A543ED51EE0F03BE3ACC3C88779C1EC1402D505FD7C7FAF061F7D2DD1F1D8D1
test/bounded-git-pull-ff-only.mjs        7B778AEDD0403053F56F115C12E7382C08863F25AEA4E683B1055B60E353BCCD
test/public-surface-registration.mjs     95212D64ABDBA6D3AFDA9E71FEA86295B2CF8C7CF9C7D25E632ED29FF997A1B6
```

## What remains unproven

The protocol and local server behavior are qualified, but the decisive ChatGPT host behavior is still unknown:

```text
resource_link in tool result
    -> does ChatGPT issue resources/read?
    -> does the fetched PDF materialize as a normal file/attachment?
    -> does that avoid the representative inline-base64 chat/context failure?
    -> can a later turn inspect the complete PDF through native/built-in PDF handling?
```

A resource read still contains base64 on the MCP wire. This checkpoint does **not** assume that ChatGPT keeps those bytes out of the model/tool-result context; that is exactly what the live host experiment must discriminate.

## Result

```text
DOCUMENT_RESOURCE_LINK_CANDIDATE          QUALIFIED
TOOL_RESULT_INLINE_PDF_BYTES              false
SEPARATE_MCP_RESOURCE_READ                QUALIFIED LOCALLY
LIVE_RUNTIME_MODIFIED                     false
LIVE_BASELINE                             preview.12 / 55
TARGET                                    preview.13 / 56
CHATGPT_RESOURCE_LINK_FETCH               UNPROVEN
CHATGPT_REPRESENTATIVE_PDF_MATERIALIZE    UNPROVEN
BROWSER_ROUTE                             DEFERRED UNTIL THIS RESULT
LOOPBACK_RENDER_TRANSPORT                 REMAINS PAUSED
NEXT                                      guarded publication, restart/schema refresh, tiny host test, then representative PDF test
```
