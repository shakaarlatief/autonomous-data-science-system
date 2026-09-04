# Validation 046: Document Render Live Source Published, Restart Pending

**Date:** 2026-09-04
**Status:** PASS / LIVE SOURCE PUBLICATION VERIFIED / RESTART PENDING
**Research:** Research 117
**Experiment:** E117-4c
**Workspace:** `ads-public`
**Target runtime after restart:** `0.1.1-preview.11` / `codexless-public-preview-v2` / 54 tools

## Purpose

Preserve the exact host publication result for the preflight-qualified `codex.document_render` candidate before the required controlled Codexless/tunnel restart and ChatGPT schema refresh.

## Host publication result

The project owner ran the guarded host helper from ordinary PowerShell at the ADS root:

```powershell
& .\.ads-private\codexless\activate-document-render-publication.ps1 -Publish
```

Before mutation, the helper reran the full candidate preflight and returned:

```text
DOCUMENT_RENDER_REGRESSION=PASS tests=10
FLEXIBLE_AUTHORITY_REGRESSION=PASS tests=7
BOUNDED_GIT_FETCH_ORIGIN=PASS tools=54
BOUNDED_GIT_PULL_FF_ONLY=PASS tools=54
PUBLIC_SURFACE_REGISTRATION=PASS tools=54
IMAGE_READ_REGRESSION=PASS tests=7
DOCUMENT_RENDER_PUBLICATION_PREFLIGHT=PASS
EXPECTED_PUBLIC_SERVER_VERSION=0.1.1-preview.11
EXPECTED_PUBLIC_SURFACE_VERSION=codexless-public-preview-v2
EXPECTED_PUBLIC_TOOL_COUNT=54
RENDER_ISOLATION=codex-command-exec-read-only
RENDER_BACKEND=managed-pdfjs-dist+@napi-rs/canvas
MODEL_TURN_REQUIRED=false
NEW_EXTERNAL_DEPENDENCY=false
DOCUMENT_READ_STAGE_REGRESSION=preserved-by-unchanged-source-plus-live-smoke
```

The user then approved the helper's exact `ShouldProcess` prompt for target `%LOCALAPPDATA%\Codexless`. Publication completed:

```text
DOCUMENT_RENDER_PUBLICATION_RESULT=PASS
LIVE_FILES_UPDATED=src/codex-authority-executor.mjs,src/codexless-runtime.mjs,src/mcp-server-factory.mjs,src/surface-contracts.mjs,src/document-renderer.mjs,src/document-render-child.mjs,test/bounded-git-fetch-origin.mjs,test/bounded-git-pull-ff-only.mjs,test/public-surface-registration.mjs,test/document-render-regression.mjs
RESTART_PERFORMED=false
```

The helper is intentionally host-run because ordinary workspace authority does not include `%LOCALAPPDATA%`. This result therefore does not widen ADS workspace authority and does not close AB-002 / AB-017.

## Running-process verification before restart

After host publication, the still-running Codexless process was independently queried through the existing model-free bridge and returned:

```text
ok             true
service        codexless-public
transport      streamable-http
version        0.1.1-preview.10
surfaceVersion codexless-public-preview-v2
toolCount      53
defaultCwd     C:\Projects_Data\autonomous-data-science-system
```

This is expected. Source publication does not hot-reload the already-running Node process. The installed bytes target preview.11 / 54 tools, while the active process remains preview.10 / 53 tools until restart.

## Authority interpretation

```text
host publication helper             PASS
ordinary workspace authority        unchanged
%LOCALAPPDATA% generic access        not granted
runtime self-maintenance architecture still open under AB-002 / AB-017
running process hot reload           none
```

No direct ChatGPT/Codexless mutation of `%LOCALAPPDATA%` was used.

## Exact next step

Follow `docs/local_execution/OPERATIONS.md` full controlled restart order because Codexless code/tool registration changed:

```text
1. stop tunnel-client with Ctrl+C and keep its Git Bash shell open;
2. stop Codexless HTTP with Ctrl+C;
3. restart `%LOCALAPPDATA%\Codexless\bin\codexless-http.cmd`;
4. verify `/healthz` reports preview.11 / v2 / 54 tools and expected defaultCwd;
5. confirm tunnel variables remain SET without printing values;
6. start the tunnel and verify `/healthz` 200 plus `/readyz` 200;
7. refresh the existing ChatGPT developer MCP app;
8. use a fresh disposable ChatGPT conversation for read-only discovery and `codex.document_render` visual qualification;
9. repeat a live `codex.document_read` smoke after restart before stronger fidelity claims.
```

Live `codex.document_render` qualification remains pending until the refreshed host projection returns actual page-image content that ChatGPT can visually inspect.
