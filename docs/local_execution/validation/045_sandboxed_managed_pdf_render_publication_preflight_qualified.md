# Validation 045: Sandboxed Managed PDF Render Publication Preflight Qualified

**Date:** 2026-09-04
**Status:** PASS / PUBLICATION PREFLIGHT QUALIFIED / LIVE PUBLICATION PENDING
**Research:** Research 117
**Experiment:** E117-4b
**Workspace:** `ads-public`
**Target public runtime:** `0.1.1-preview.11` / `codexless-public-preview-v2` / 54 tools

## Purpose

Qualify the smallest read-only semantic PDF page-render seam after Validation 044 proved that maintained OpenAI/Codex runtime dependencies already contain viable rendering components.

The key design question was whether untrusted PDF rendering could remain behind the existing Codex `command/exec` read-only sandbox instead of launching a native renderer directly with ordinary Codexless host identity.

## Sandbox discrimination

Read-only `codex.command_exec` probes established:

```text
workspace write attempt                 DENIED
%TEMP% write attempt                    DENIED
loopback TCP 127.0.0.1:7690            ALLOWED
non-loopback TCP 1.1.1.1:443           DENIED / EACCES
managed runtime file read               ALLOWED
```

A file-output renderer therefore cannot write PNGs into the workspace or ordinary host temp directory while remaining read-only. This is a useful fail-closed property and should not be weakened. The tested sandbox blocks ordinary non-loopback TCP, but loopback remains available, so this is not a claim of complete network isolation from local services.

## Maintained in-memory rendering path

The current OpenAI/Codex primary-runtime dependency bundle contains:

```text
pdfjs-dist                       5.6.205
@napi-rs/canvas                  0.1.100
@napi-rs/canvas-win32-x64-msvc  0.1.100
```

`pdfjs-dist` itself declares `@napi-rs/canvas` as a dependency. A read-only sandbox probe successfully rendered an authorized PDF page entirely in memory:

```text
PDF bytes
    -> maintained pdfjs-dist
    -> maintained @napi-rs/canvas
    -> in-memory PNG buffer
    -> stdout protocol
```

A representative synthetic page produced a valid 1275 x 1651 PNG of 47,742 bytes under the `:read-only` permission profile with no filesystem output.

## Standard-font resolution correction

The first sandbox child probe warned that PDF.js could not load its own `LiberationSans` standard-font files. Direct sandboxed reads proved those files existed and were readable. The cause was interface semantics rather than authority: PDF.js' Node binary-data factory ultimately passes its configured factory location to `fs.readFile`, so `file://` URL strings failed while normalized forward-slash filesystem paths with a trailing slash succeeded.

After that correction the same sandboxed renderer produced the synthetic probe without the warning. Host-side visual materialization of the identical maintained rendering stack was inspected through `codex.image_read` and visibly preserved the three colored rectangles, diagonal line, increasing bar sequence, labels and page headings from both synthetic pages.

## Candidate semantic action

The preflight candidate introduces:

```text
codex.document_render
```

Public input contract:

```text
cwd
documentPath     workspace-relative PDF path
pages            required ordered unique 1-based pages, maximum 4
```

The caller cannot select executable, backend, renderer arguments, DPI, output path, permission profile, sandbox, workspaceId override, Browser, Agent, OCR, Git, write authority or internal output ceiling.

The renderer wrapper:

```text
1. resolves existing workspace read authority;
2. proves canonical cwd/document containment;
3. performs bounded source read and PDF header validation;
4. resolves maintained primary-runtime package identities;
5. invokes one fixed child through existing command/exec with access=readOnly and capability=read;
6. renders at fixed 150 DPI entirely in memory;
7. permits at most 4 pages, 4 MiB per PNG and 8 MiB aggregate PNG bytes;
8. validates PNG signature, dimensions, byte count and SHA-256;
9. re-reads and re-hashes the source after rendering and fails if content changed;
10. returns provenance plus one standard MCP image block per selected page.
```

No renderer temp file is required.

## Internal output ceiling

The existing public `codex.command_exec` intentionally truncates output at 32 KiB. Useful PNG base64 can exceed that. The candidate adds an **internal-only** `outputBytesCap` option to `CodexAuthorityExecutor.exec`, bounded to at most 12 MiB; `codex.document_render` uses 11,750,000 bytes.

The public `codex.command_exec` MCP schema remains unchanged and strict. Registration regression explicitly proves that a remote input containing `outputBytesCap` is rejected. This internal transport allowance is therefore not new caller authority.

## Verification

Focused candidate regression:

```text
DOCUMENT_RENDER_REGRESSION=PASS tests=10
```

Coverage includes managed dependency resolution, fixed read-only sandbox invocation, caller page order, page-range propagation, path/traversal/duplicate/page-count rejection, junction escape rejection, capability denial, oversized-source rejection, source mutation detection, truncation fail-closed behavior and fixed implementation ceilings.

Integrated staged preflight:

```text
DOCUMENT_RENDER_REGRESSION=PASS tests=10
FLEXIBLE_AUTHORITY_REGRESSION=PASS tests=7
BOUNDED_GIT_FETCH_ORIGIN=PASS tools=54
BOUNDED_GIT_PULL_FF_ONLY=PASS tools=54
PUBLIC_SURFACE_REGISTRATION=PASS tools=54
IMAGE_READ_REGRESSION=PASS tests=7
DOCUMENT_RENDER_PUBLICATION_PREFLIGHT=PASS
PUBLIC_COMMAND_INTERNAL_OUTPUT_CAP_REMOTE_SCHEMA=REJECTED
EXPECTED_PUBLIC_SERVER_VERSION=0.1.1-preview.11
EXPECTED_PUBLIC_SURFACE_VERSION=codexless-public-preview-v2
EXPECTED_PUBLIC_TOOL_COUNT=54
MODEL_TURN_REQUIRED=false
NEW_EXTERNAL_DEPENDENCY=false
NO_LIVE_FILES_MODIFIED=true
```

The staged `document_read` parser regression is intentionally not run through the stage-local `node_modules` junction because its accepted Node permission isolation cannot traverse that junction into the live dependency tree. `document_read` implementation/dependency files are unchanged by this candidate, and a separate current-live semantic smoke returned `SANDBOX` from the generated PDF through `pdfjs-dist@5.4.624` successfully before publication.

## Guarded publication helper

Prepared ignored host helper:

```text
.ads-private/codexless/activate-document-render-publication.ps1
```

Preflight SHA-256:

```text
C2C73B571E0BC3A296BB79DA00B4F2472FD23C358889931BB500EA42576061AF
```

Its no-publish preflight passed. The helper pins exact preview.10 live hashes and candidate hashes, stages the candidate over the current runtime, reruns the accepted regression set, requires preview.11/v2/54 markers, and uses `ShouldProcess` plus backup/rollback. It never restarts Codexless automatically.

## Result

```text
READ_ONLY_SANDBOX_RENDER_ROUTE            PASS
MANAGED_PDFJS_CANVAS_REUSE                PASS
WORKSPACE_WRITE_REQUIRED                  false
HOST_TEMP_WRITE_REQUIRED                  false
NEW_EXTERNAL_DEPENDENCY                   false
EXTRA_CODEX_MODEL_TURN_REQUIRED           false
PUBLIC_COMMAND_AUTHORITY_WIDENED          false
DOCUMENT_RENDER_PUBLICATION_PREFLIGHT      PASS
LIVE_PUBLICATION                           PENDING
REPRESENTATIVE_COMPLEX_PDF_FIDELITY        NOT YET QUALIFIED
```

## Exact next step

Run the guarded helper from ordinary host PowerShell at the ADS root:

```powershell
& .\.ads-private\codexless\activate-document-render-publication.ps1 -Publish
```

Approve only the exact `ShouldProcess` publication prompt. After a successful publication, follow `docs/local_execution/OPERATIONS.md` exactly: stop tunnel first, stop Codexless, restart and verify preview.11 / 54 tools, restart and verify tunnel health/readiness, refresh the ChatGPT developer MCP app, then use a fresh disposable conversation to test `codex.document_render` directly.
