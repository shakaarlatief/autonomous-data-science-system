# Validation 092: Office File-Link Preview.17 Publication Preflight Qualified

**Date:** 2026-09-06
**Status:** PASS / GUARDED PREVIEW.17 PUBLICATION PREFLIGHT QUALIFIED / HOST PUBLICATION NEXT
**Research:** Research 121
**Scope:** Qualify the exact guarded live-publication package for the durable DOCX/PPTX/XLSX `codex.file_link` candidate after AB-020 was live-qualified and the private candidate was preserved at `fa5cc2a6c3e6d47f45961ab475c2ac66c24aff0b`.

## 1. Live baseline

The preflight bound the currently installed runtime to:

```text
version        0.1.1-preview.16-hybrid-pdf-access
surface        codexless-public-preview-v2
toolCount      60
semantic-git   3b2ddbbe00339045b81044bb3e1e39c314a461a7e0f8e4e608b79b4b0f37de02
```

The semantic-Git hash is the already-live AB-020 correction and is explicitly required to remain unchanged through the Office publication.

## 2. Publication package

The guarded helper publishes exactly nine files:

```text
existing source replacements
  src/mcp-server-factory.mjs
  src/codexless-runtime.mjs
  src/surface-contracts.mjs

new source files
  src/file-link-reader.mjs
  src/file-resource-store.mjs

existing regression replacements
  test/public-surface-registration.mjs
  test/bounded-git-fetch-origin.mjs
  test/bounded-git-pull-ff-only.mjs

new regression
  test/file-link-regression.mjs
```

The existing files are bound to exact old/new SHA-256 values. New files are required to be absent before publication. Existing replacements receive timestamped backups. New files are removed on rollback. Every installed file is hash-verified after replacement. The helper deliberately performs no restart.

## 3. Candidate contract

The proposed live surface is:

```text
version        0.1.1-preview.17-office-file-link
surface        codexless-public-preview-v2
toolCount      61
new tool       codex.file_link
```

The tool accepts only `cwd` and `filePath`, with server-side MIME derivation for:

```text
.docx
.pptx
.xlsx
```

It reuses existing workspace `read` authority, canonical containment, exact size/identity/SHA-256 binding, expiring server-owned MCP resource tokens and read-time revalidation. It accepts no caller-selected MIME, resource URI, destination, parser, renderer, OCR, Browser, Agent, Git, permission-profile or write controls. The tool result carries metadata plus one `resource_link`; source bytes/base64 are served only through `resources/read`.

## 4. Preflight evidence

The no-publish staging run passed:

```text
FILE_LINK_REGRESSION=PASS tests=10
BOUNDED_GIT_FETCH_ORIGIN=PASS tools=61
BOUNDED_GIT_PULL_FF_ONLY=PASS tools=61
DOCUMENT_FILE_READ_REGRESSION=PASS tests=7
DOCUMENT_RESOURCE_LINK_REGRESSION=PASS tests=9
DOCUMENT_RENDER_REGRESSION=PASS tests=10
IMAGE_READ_REGRESSION=PASS tests=7
PUBLIC_SURFACE_REGISTRATION=PASS tools=61
FLEXIBLE_AUTHORITY_REGRESSION=PASS tests=8
OFFICE_FILE_LINK_PUBLICATION_PREFLIGHT=PASS
STAGED_PUBLIC_REGRESSIONS=PASS scripts=7
AB020_FLEXIBLE_AUTHORITY_REGRESSION=PASS tests=8
NO_LIVE_FILES_MODIFIED=true
RESTART_PERFORMED=false
```

The staged runtime therefore preserves all previously qualified PDF resource/read/render behavior, bounded Git registration behavior, the AB-020 integrity fix, and the exact 61-tool public registration while adding only the Office whole-file handoff surface.

## 5. Next action

The helper is prepared under protected private-runtime `.tmp` and should be run from ordinary host PowerShell with `-Publish`. After successful publication, independently verify installed hashes, preserve the source-published/restart-pending boundary, then follow `docs/local_execution/OPERATIONS.md` for the full controlled restart. Because the public tool surface changes from 60 to 61 tools, fresh ChatGPT discovery is required after the runtime/tunnel are healthy.

```text
OFFICE_FILE_LINK_PUBLICATION_PREFLIGHT=PASS
LIVE_FILES_MODIFIED=false
NEXT=ORDINARY_HOST_PUBLICATION
```
