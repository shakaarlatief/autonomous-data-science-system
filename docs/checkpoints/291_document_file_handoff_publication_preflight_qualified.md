# Checkpoint 291: Document File Handoff Publication Preflight Qualified

**Date:** 2026-09-04
**Status:** CANDIDATE QUALIFIED / HOST PUBLICATION PENDING
**Checkpoint class:** EXPERIMENT_VERIFICATION
**Project stage:** Research 117 reuse-first multimodal document architecture
**Scope:** Preserves preflight qualification of a minimal read-only `codex.document_file_read` candidate that returns exact authorized local PDF bytes as standard MCP `application/pdf` embedded-resource content for a ChatGPT native-file-promotion experiment.
**Authority:** Validation 050 is primary evidence. This checkpoint does not claim native ChatGPT PDF/file promotion and does not claim preview.12 is live.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-17`
**Conversation title:** `17 - MCP Image Bridge Publication Recovery and Multimodal Document Continuation`
**Primary collaborator:** ChatGPT

## Boundary

Checkpoint 290 reprioritized Research 117 toward first-party PDF reuse. The smallest candidate seam is now preflight-qualified:

```text
authorized local Windows PDF
    -> existing workspace read authority
    -> canonical bounded exact-byte read
    -> standard MCP embedded application/pdf resource
    -> ChatGPT host promotion experiment
```

Candidate public surface target:

```text
version        0.1.1-preview.12
surface        codexless-public-preview-v2
tool count     55
new action     codex.document_file_read
```

The action accepts only `cwd` and a workspace-relative `documentPath`. It performs no parser/render/OCR/Browser/Agent/Git/write/external-API work and exposes no caller-selected URI, MIME type, host path, permission profile or upload destination.

## Qualification

```text
DOCUMENT_FILE_READ_REGRESSION=PASS tests=5
BOUNDED_GIT_FETCH_ORIGIN=PASS tools=55
BOUNDED_GIT_PULL_FF_ONLY=PASS tools=55
PUBLIC_SURFACE_REGISTRATION=PASS tools=55
IMAGE_READ_REGRESSION=PASS tests=7
DOCUMENT_RENDER_REGRESSION=PASS tests=10
DOCUMENT_FILE_HANDOFF_PUBLICATION_PREFLIGHT=PASS
MODEL_TURN_REQUIRED=false
RENDERER_REQUIRED=false
OCR_REQUIRED=false
BROWSER_REQUIRED=false
NEW_EXTERNAL_DEPENDENCY=false
PAUSED_LOOPBACK_RENDER_TRANSPORT_OVERLAID=false
NO_LIVE_FILES_MODIFIED=true
```

The live process remains preview.11 / v2 / 54 tools and the existing `codex.document_read` smoke remains `SANDBOX` / `pdfjs-dist@5.4.624` / OCR false.

## Publication isolation

The guarded helper overlays only:

```text
src/document-file-reader.mjs                 NEW
src/codexless-runtime.mjs                    file-handoff wiring only
src/mcp-server-factory.mjs                   file-handoff tool/result wiring only
src/surface-contracts.mjs                    preview.12 / +1 action
test/document-file-read-regression.mjs       NEW
test/bounded-git-fetch-origin.mjs            55-tool expectation only
test/bounded-git-pull-ff-only.mjs             55-tool expectation only
test/public-surface-registration.mjs          file-handoff surface coverage
```

It explicitly preserves live preview.11 hashes for the paused renderer transport files and refuses staging if they drift:

```text
src/codex-authority-executor.mjs
src/document-renderer.mjs
src/document-render-child.mjs
test/document-render-regression.mjs
```

Thus Checkpoint 289's loopback candidate remains private and unpublished.

## Exact continuation

```text
1. preserve Checkpoint 291 / Validation 050 in public authority;
2. run the guarded host publication helper with -Publish and approve only its exact ShouldProcess target;
3. verify DOCUMENT_FILE_HANDOFF_PUBLICATION_RESULT=PASS and RESTART_PERFORMED=false;
4. follow docs/local_execution/OPERATIONS.md full restart order;
5. verify preview.12 / v2 / 55 tools plus tunnel health/readiness;
6. repeat document_read, image_read and small document_render smokes;
7. refresh the existing ChatGPT developer-MCP app;
8. in a fresh disposable chat call only codex.document_file_read on an authorized PDF;
9. determine whether the host receives/promotes an actual native PDF/file input rather than only metadata/resource bytes;
10. if native promotion passes, test CheatSheet_A4.pdf and Adobe Scan BDS_Exercises_Misha.pdf through the first-party PDF capability;
11. resume loopback transport work only if the native handoff is unavailable or materially inferior.
```

Primary evidence:

```text
docs/local_execution/validation/050_document_file_handoff_publication_preflight_qualified.md
docs/checkpoints/290_official_pdf_skill_local_ads_handoff_research_prioritized.md
docs/local_execution/validation/049_official_pdf_skill_local_ads_handoff_research_prioritized.md
docs/research/117_reuse_first_multimodal_document_architecture_and_local_media_handoff.md
```
