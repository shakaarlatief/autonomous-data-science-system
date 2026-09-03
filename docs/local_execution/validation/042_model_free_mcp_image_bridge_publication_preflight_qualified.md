# Validation 042: Model-Free MCP Image Bridge Publication Preflight Qualified

**Date:** 2026-09-03
**Status:** PREFLIGHT PASS / LIVE PUBLICATION REQUIRES HOST-STATE STEP
**Research:** Research 117

## Purpose

Test the cheapest direct-host architecture for local visual input before using another metered Codex model turn: an authority-bounded local image tool that returns standard MCP `image` content directly to ChatGPT.

## Candidate contract

The candidate introduces `codex.image_read` with only:

```text
cwd
imagePath
```

It requires the existing workspace `read` capability and performs no model call, OCR, rendering, Browser action, Agent call, Git operation, write, or external upload. PNG, JPEG and WebP are accepted by byte signature with a 10 MiB ceiling. Canonical path containment, file-identity revalidation, SHA-256 provenance and workspace-relative identity are preserved.

The MCP result is deliberately shaped like the already accepted Browser screenshot result:

```text
content:
    text metadata
    standard MCP image content

structuredContent:
    metadata only
```

The base64 image payload is not duplicated into structured JSON.

## Candidate validation

```text
IMAGE_READ_REGRESSION=PASS tests=7
FLEXIBLE_AUTHORITY_REGRESSION=PASS tests=7
BOUNDED_GIT_FETCH_ORIGIN=PASS tools=53
BOUNDED_GIT_PULL_FF_ONLY=PASS tools=53
PUBLIC_SURFACE_REGISTRATION=PASS tools=53
IMAGE_READ_PUBLICATION_PREFLIGHT=PASS
EXPECTED_PUBLIC_SERVER_VERSION=0.1.1-preview.10
EXPECTED_PUBLIC_SURFACE_VERSION=codexless-public-preview-v2
EXPECTED_PUBLIC_TOOL_COUNT=53
MODEL_TURN_REQUIRED=false
NEW_EXTERNAL_DEPENDENCY=false
NO_LIVE_FILES_MODIFIED=true
```

The existing live `codex.document_read` path was separately smoke-tested immediately before publication work and still returned page 1 of the known five-page qualification PDF through `pdfjs-dist@5.4.624` with the expected document SHA-256 and no OCR.

A staged `document-read-regression` run was intentionally not used as a publication gate. Its isolated parser permits filesystem reads only within the staged runtime tree and therefore correctly refuses a stage-local `node_modules` junction whose real target is outside that tree. The image candidate does not modify `document-reader.mjs` or its parser. Weakening parser isolation merely to make the staging fixture pass would be architecturally wrong.

## Live-publication attempt

ChatGPT attempted the guarded helper through the ordinary Codexless `command_exec` inherited-authority lane. The helper reran the complete image preflight successfully, then the host-state write to `%LOCALAPPDATA%\Codexless` was denied by the command sandbox before the first live replacement could occur.

Post-failure verification proved:

```text
live codexless-runtime.mjs   unchanged
live mcp-server-factory.mjs  unchanged
live surface-contracts.mjs   unchanged
live image-reader.mjs        absent
publication temp residue     absent
```

This is expected authority separation, not a candidate failure. It is also concrete evidence for the already-open narrow Codexless runtime self-maintenance architecture gap.

## Required next step

Run the guarded publication helper from the user's normal host PowerShell at the ADS repository root:

```powershell
& .\.ads-private\codexless\activate-image-read-publication.ps1 -Publish
```

Approve its exact `ShouldProcess` prompt. The helper does not restart Codexless. After publication, use the controlled restart/reconnect/schema-refresh runbook, verify `0.1.1-preview.10` / `codexless-public-preview-v2` / 53 tools, then test `codex.image_read` from a fresh disposable ChatGPT conversation against an authorized PNG containing visual-only information.

## Qualification result

```text
IMAGE_READ_CANDIDATE=QUALIFIED
LIVE_PUBLICATION=false
HOST_CHATGPT_MCP_IMAGE_VISION=NOT_YET_TESTED
EXTRA_CODEX_MODEL_TURN_REQUIRED_BY_CANDIDATE=false
```
