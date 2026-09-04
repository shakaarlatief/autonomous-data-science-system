# Validation 050: Document File Handoff Publication Preflight Qualified

**Date:** 2026-09-04
**Status:** PASS / PUBLICATION PREFLIGHT QUALIFIED / LIVE HOST TEST PENDING
**Research:** Research 117
**Experiment:** E117-5c
**Live baseline:** `0.1.1-preview.11` / `codexless-public-preview-v2` / 54 tools
**Candidate target:** `0.1.1-preview.12` / `codexless-public-preview-v2` / 55 tools

## Purpose

Qualify the smallest reuse-first host experiment opened by Checkpoint 290: return one existing-authority local Windows PDF as standard MCP `application/pdf` resource content, without parsing/rendering/OCR/model/browser/write/Git/network behavior, and then use a fresh ChatGPT host to determine whether that MCP resource is promoted into native PDF/file-input treatment.

## Candidate semantic action

Candidate public action:

```text
codex.document_file_read
```

Public inputs:

```text
cwd
documentPath
```

The action requires the existing registered workspace `read` capability. It canonicalizes cwd/root/target, rejects absolute paths and parent traversal, rejects symlink/junction escape, uses a bounded file-handle read, verifies source identity across the read, validates PDF content by header rather than extension alone, records SHA-256 and byte length, and returns the exact source bytes as a standard MCP embedded resource:

```text
type       resource
mimeType   application/pdf
blob       base64-encoded exact source bytes
uri        codexless://document/<sha256>/<file-name>
```

The 4 MiB source ceiling is deliberately conservative for the first host-discrimination experiment. It admits the two representative PDFs that exposed the Checkpoint 289 render-transport problem (`CheatSheet_A4.pdf` and `Adobe Scan BDS_Exercises_Misha.pdf`) while keeping the initial host payload bounded. It intentionally does not yet admit the 7.99 MiB full-width cheat sheet.

## Protocol verification

The installed MCP SDK's current `CallToolResultSchema` accepts both embedded-resource and resource-link result content. A direct schema probe accepted an embedded `application/pdf` blob and an `application/pdf` `resource_link`.

The candidate uses embedded resource first because it carries the exact source bytes in the tool result and does not require a second resource-fetch contract. Resource-link routing remains a fallback experiment only if the ChatGPT host does not promote the embedded PDF.

## Focused candidate regression

```text
DOCUMENT_FILE_READ_REGRESSION=PASS tests=5
```

Coverage:

```text
exact PDF bytes + provenance
absolute/traversal rejection
non-PDF rejection
outside symlink/junction escape rejection
source >4 MiB rejection before allocation
```

## Integrated publication staging

The candidate was staged from the exact live preview.11 runtime plus only the file-handoff overlay. The paused Checkpoint 289 loopback transport files were explicitly required to remain byte-for-byte equal to live preview.11 inside the stage.

Accepted integrated results:

```text
DOCUMENT_FILE_READ_REGRESSION=PASS tests=5
BOUNDED_GIT_FETCH_ORIGIN=PASS tools=55
BOUNDED_GIT_PULL_FF_ONLY=PASS tools=55
PUBLIC_SURFACE_REGISTRATION=PASS tools=55
IMAGE_READ_REGRESSION=PASS tests=7
DOCUMENT_RENDER_REGRESSION=PASS tests=10
DOCUMENT_FILE_HANDOFF_PUBLICATION_PREFLIGHT=PASS
EXPECTED_PUBLIC_SERVER_VERSION=0.1.1-preview.12
EXPECTED_PUBLIC_SURFACE_VERSION=codexless-public-preview-v2
EXPECTED_PUBLIC_TOOL_COUNT=55
MCP_CONTENT_TYPE=embedded-resource/application-pdf
MODEL_TURN_REQUIRED=false
RENDERER_REQUIRED=false
OCR_REQUIRED=false
BROWSER_REQUIRED=false
NEW_EXTERNAL_DEPENDENCY=false
PAUSED_LOOPBACK_RENDER_TRANSPORT_OVERLAID=false
NO_LIVE_FILES_MODIFIED=true
```

The existing live `codex.document_read` path was then re-smoked separately and still returned exact embedded text `SANDBOX` through `pdfjs-dist@5.4.624` with OCR false.

Live health after preflight remains:

```text
version         0.1.1-preview.11
surfaceVersion  codexless-public-preview-v2
toolCount       54
```

## Guarded publication helper

Private ignored helper:

```text
.ads-private/codexless/activate-document-file-handoff-publication.ps1
SHA-256 ABF1542B51CAE9CDE71891A7A6F70AF6C52D15B3E795F21F432D228B0CBEE33C
```

The helper:

```text
pins exact preview.11 live hashes
pins exact candidate hashes
stages complete live runtime + only the file-handoff overlay
reruns accepted regressions
requires paused renderer/authority files to remain live-identical
requires preview.12 / v2 / 55-tool markers
uses SupportsShouldProcess for publication
backs up/replaces only the declared existing source/test files
adds only document-file-reader.mjs and its focused regression
performs no restart
rolls back touched live files on publication failure
```

Files deliberately excluded from this publication overlay:

```text
src/codex-authority-executor.mjs
src/document-renderer.mjs
src/document-render-child.mjs
test/document-render-regression.mjs
```

This prevents the paused loopback candidate from being smuggled into the native-file-handoff experiment.

## What remains unproven

Preflight does not establish the critical ChatGPT-host behavior:

```text
MCP application/pdf embedded resource
    -> native ChatGPT PDF/file input
    -> first-party PDF Skill / native multimodal PDF treatment
```

That requires guarded publication, controlled restart/schema refresh, and a fresh disposable ChatGPT conversation. The host test must distinguish actual PDF ingestion from merely receiving metadata or opaque base64/resource content.

## Result

```text
DOCUMENT_FILE_HANDOFF_CANDIDATE              QUALIFIED
MCP_EMBEDDED_PDF_RESULT_SHAPE                QUALIFIED
LIVE_RUNTIME_MODIFIED                        false
LIVE_BASELINE                                preview.11 / 54
TARGET                                       preview.12 / 55
CHATGPT_NATIVE_PDF_PROMOTION                 UNPROVEN
LOOPBACK_RENDER_PUBLICATION                  PAUSED
NEXT                                         guarded host publication, restart, schema refresh, fresh-host PDF promotion experiment
```
