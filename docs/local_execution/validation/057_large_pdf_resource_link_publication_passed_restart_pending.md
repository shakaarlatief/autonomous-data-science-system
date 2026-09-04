# Validation 057: Large PDF Resource-Link Publication Passed, Restart Pending

**Date:** 2026-09-04
**Status:** PASS / LIVE FILE PUBLICATION COMPLETE / RESTART PENDING
**Research:** Research 117
**Published target:** `0.1.1-preview.14` / `codexless-public-preview-v2` / 56 tools

The guarded host publication helper was run from ordinary PowerShell with explicit confirmation of the exact target `C:\Users\shaka\AppData\Local\Codexless`.

Accepted publication evidence:
```text
DOCUMENT_FILE_READ_REGRESSION=PASS tests=7
DOCUMENT_RESOURCE_LINK_REGRESSION=PASS tests=9
BOUNDED_GIT_FETCH_ORIGIN=PASS tools=56
BOUNDED_GIT_PULL_FF_ONLY=PASS tools=56
PUBLIC_SURFACE_REGISTRATION=PASS tools=56
IMAGE_READ_REGRESSION=PASS tests=7
DOCUMENT_RENDER_REGRESSION=PASS tests=10
DOCUMENT_RESOURCE_LARGE_PUBLICATION_PREFLIGHT=PASS
EXPECTED_PUBLIC_SERVER_VERSION=0.1.1-preview.14
EXPECTED_PUBLIC_SURFACE_VERSION=codexless-public-preview-v2
EXPECTED_PUBLIC_TOOL_COUNT=56
EMBEDDED_DOCUMENT_FILE_READ_LIMIT_BYTES=4194304
RESOURCE_LINK_DOCUMENT_LIMIT_BYTES=100663296
RESOURCE_PREPARE_RETAINS_BASE64=false
RESOURCE_FETCH_REVALIDATES_SIZE_MTIME_IDENTITY_SHA256=true
PAUSED_LOOPBACK_RENDER_TRANSPORT_OVERLAID=false
DOCUMENT_RESOURCE_LARGE_PUBLICATION_RESULT=PASS
PAUSED_LOOPBACK_RENDER_TRANSPORT_MODIFIED=false
RESTART_PERFORMED=false
```

Post-publication independent hash verification matched the exact qualified candidate for all six changed live files: `document-file-reader.mjs`, `document-resource-store.mjs`, `mcp-server-factory.mjs`, `surface-contracts.mjs`, `document-file-read-regression.mjs`, and `document-resource-link-regression.mjs`.

The still-running process correctly continued to report preview.13 / v2 / 56 because the helper intentionally did not restart Codexless. This is expected and proves the new files are published on disk but not yet active in the process.

Next: perform the repository-authoritative controlled tunnel/Codexless restart, verify preview.14 / v2 / 56 plus tunnel health/readiness, rerun preserved document smokes, refresh the ChatGPT app schema if needed, then begin progressive real-host large-PDF tests at 4.23 MiB, 8.31 MiB, 30.67 MiB, and 75.22 MiB.
