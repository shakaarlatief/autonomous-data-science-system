# Checkpoint 297: Large PDF Resource-Link Scaling Publication Preflight Qualified

**Date:** 2026-09-04
**Status:** LARGE-PDF SCALING CANDIDATE QUALIFIED / PUBLICATION PENDING
**Checkpoint class:** EXPERIMENT_VERIFICATION
**Project stage:** Research 117 reuse-first multimodal document architecture
**Scope:** Preserves the large-file `codex.document_file_link` scaling candidate after the real Machine Learning lecture corpus proved the old 4 MiB ceiling is inadequate.
**Authority:** Validation 056 is primary evidence. This checkpoint does not claim preview.14 is live or that large MCP resource fetches pass the ChatGPT host.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-17`
**Conversation title:** `17 - MCP Image Bridge Publication Recovery and Multimodal Document Continuation`
**Primary collaborator:** ChatGPT

## Boundary

Checkpoint 296 qualified scanned/image-heavy whole-PDF access under the existing small-file envelope. The newly authorized read-only Machine Learning corpus contains annotated lecture PDFs from 4.23 MiB to 75.22 MiB, so every lecture exceeds the old 4 MiB file-handoff ceiling.

The preview.14 candidate keeps embedded `codex.document_file_read` at 4 MiB and gives only resource-link preparation a separate 96 MiB ceiling. Preparation now streams validation/SHA-256 and stores only an ephemeral immutable file binding rather than persistent PDF base64. Resource fetch revalidates canonical path, size, mtime, filesystem identity and SHA-256 before constructing the MCP blob.

Accepted preflight:

```text
DOCUMENT_FILE_READ_REGRESSION=PASS tests=7
DOCUMENT_RESOURCE_LINK_REGRESSION=PASS tests=9
PUBLIC_SURFACE_REGISTRATION=PASS tools=56
IMAGE_READ_REGRESSION=PASS tests=7
DOCUMENT_RENDER_REGRESSION=PASS tests=10
DOCUMENT_RESOURCE_LARGE_PUBLICATION_PREFLIGHT=PASS
RESOURCE_LINK_DOCUMENT_LIMIT_BYTES=100663296
RESOURCE_PREPARE_RETAINS_BASE64=false
RESOURCE_FETCH_REVALIDATES_SIZE_MTIME_IDENTITY_SHA256=true
PAUSED_LOOPBACK_RENDER_TRANSPORT_OVERLAID=false
NO_LIVE_FILES_MODIFIED=true
```

## Exact continuation

```text
1. preserve Checkpoint 297 / Validation 056 publicly;
2. run the private guarded large-resource publication helper with -Publish from ordinary PowerShell;
3. review exact publication output before restart;
4. controlled restart and verify preview.14 / v2 / 56 plus tunnel health/readiness;
5. progressive fresh-chat resource-link materialization tests at 4.23, 8.31, 30.67 and 75.22 MiB;
6. stop at the first failed size tier and localize the actual transport layer before changing limits;
7. if 75.22 MiB materializes, perform next-turn full-PDF inspection to qualify the current lecture corpus end to end;
8. only then decide whether 96 MiB is an accepted product ceiling or merely the first qualified research envelope.
```
