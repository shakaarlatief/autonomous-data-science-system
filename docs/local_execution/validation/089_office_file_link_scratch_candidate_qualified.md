# Validation 089: Office File-Link Scratch Candidate Qualified Before AB-020 Activation

**Date:** 2026-09-06
**Status:** PASS / OFFICE FILE-LINK SCRATCH CANDIDATE QUALIFIED / AB-020 LIVE ACTIVATION STILL REQUIRED
**Research:** Research 121
**Scope:** Preserve the non-secret architecture, hashes, regressions and deterministic host fixtures for the first DOCX/PPTX/XLSX whole-file handoff candidate while its implementation remains in protected private-runtime `.tmp`, so collaborators without local-machine access can reconstruct the qualified design before AB-020 is activated and the source becomes durable private Git evidence.

## Candidate architecture

The candidate adds one new public tool:

```text
codex.file_link
input: cwd + filePath only
```

Supported initial OOXML types are server-derived and fixed:

```text
.docx  application/vnd.openxmlformats-officedocument.wordprocessingml.document
.pptx  application/vnd.openxmlformats-officedocument.presentationml.presentation
.xlsx  application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
```

The candidate preserves existing PDF contracts unchanged. It introduces a separate file-link reader and separate `codexless://file-resource/{token}` resource store. Preparation requires existing workspace `read` authority, canonical cwd/root/target containment, a regular file, a supported extension, the OOXML ZIP local-file signature, a 32 MiB source ceiling, SHA-256 binding and pre/post file identity checks. `resources/read` revalidates path identity, file identity, exact byte length and SHA-256 before byte release. Resource tokens are random server-owned 256-bit values, expire after 15 minutes, and are capped at eight live entries. No caller MIME, URI, destination, parser, renderer, OCR, Browser, Agent, permission-profile or write control is accepted.

The original tool result contains metadata plus one MCP `resource_link`; it does not embed source bytes/base64.

## Proposed public surface

```text
server version  0.1.1-preview.17-office-file-link
surface         codexless-public-preview-v2
source tools    61
new tool        codex.file_link
```

## Focused candidate evidence

The new file-link suite passes 10/10:

```text
FILE_LINK_REGRESSION=PASS tests=10
```

Coverage includes:

```text
narrow stable fields and exact MIME allowlist
DOCX/PPTX/XLSX provenance and server-derived MIME
absolute/traversal rejection
unsupported-extension rejection
non-ZIP OOXML rejection
workspace escape through symlink/junction rejection
32 MiB source ceiling
metadata-only resource preparation
resources/read exact MIME/blob
server-owned URI scheme and bounded entry capacity
TTL expiry
prepared-source drift detection
malformed reader-envelope rejection
```

The complete staged public regression set also passes after the intentional 60 -> 61 tool-count update:

```text
BOUNDED_GIT_FETCH_ORIGIN=PASS tools=61
BOUNDED_GIT_PULL_FF_ONLY=PASS tools=61
DOCUMENT_FILE_READ_REGRESSION=PASS tests=7
DOCUMENT_RESOURCE_LINK_REGRESSION=PASS tests=9
DOCUMENT_RENDER_REGRESSION=PASS tests=10
IMAGE_READ_REGRESSION=PASS tests=7
PUBLIC_SURFACE_REGISTRATION=PASS tools=61
OFFICE_CANDIDATE_STAGED_REGRESSIONS=PASS scripts=7
```

Existing PDF file/resource/render behavior remains unchanged under those regressions.

## Candidate hashes

```text
file-link-reader.mjs
6394a83bf9f59b072e311e528d8f83e5e2d1b1df7c4b200aa99ab289b9d1c95d

file-resource-store.mjs
dea01debc69a3fe4a2d4dd785a71015c4d03f3d02f0c733d879cb9c97ea441e1

mcp-server-factory.mjs
9f6c002c4545ddde7963761c342f91657a0136eaa1954e1358ad49c57288cbdb

codexless-runtime.mjs
3a030c22d974f0fea504dc5f5b024054e4609738489c9920923c39817f78a552

surface-contracts.mjs
41a4188fa7edf10d3ec1bc79bbd02d2f7f68fdadd5373eba33896ca7f8cfa15c

file-link-regression.mjs
d378c7109ffaef4be58c68d26abef863e5cb4a59bc245a33aa1febc8250d5db6

public-surface-registration.mjs
ff6eba85ad20b99420de706aaa36b86ff7f875a99fd5929fcaeab6a08128bab5
```

## Deterministic fresh-host fixtures

A model-free Python standard-library generator creates three tiny deterministic OOXML ZIP packages in protected `.tmp` for later host qualification. The files deliberately contain distinctive text/structure and, for DOCX/PPTX, one embedded 64x64 four-quadrant PNG.

```text
office-handoff.docx
1,985 bytes
3bf55d3b8eb7ddcf260282224f409a2d27f00514fc61d444986630548c2bb65d
markers: DOCX_MARKER_ALPHA, table, embedded quadrant image

office-handoff.pptx
3,046 bytes
575f00d083c925f6bae9a76019ccc9095e82f2a85b7295c43502b38c6815b8c7
markers: PPTX_MARKER_BETA, PPTX_MARKER_GAMMA, two slides, embedded quadrant image

office-handoff.xlsx
2,585 bytes
7fe060a575346a2844940bd4eb14fd27dc9795f1b8ea1ee59ad3fd202f7aa731
markers: XLSX_MARKER_DELTA, XLSX_MARKER_EPSILON, two sheets, formulas, styled header
```

All three ZIP packages pass Python `ZipFile.testzip()`, and the candidate reader independently accepts each with the expected MIME, exact byte size and matching SHA-256.

These fixtures are qualification artifacts, not durable user documents. They remain ignored in protected `.tmp` until fresh-host qualification and should be removed afterward.

## Preservation boundary

The Office implementation is intentionally **not yet added as new tracked private files**. The currently running Codexless process still uses the old private-integrity enumeration implementation. Adding new tracked paths now would cross the previously reproduced 32 KiB envelope before the AB-020 live fix is active.

Checkpoint 330 already qualified the AB-020 source and guarded publication helper. Therefore the next action remains:

```text
publish qualified AB-020 semantic-git.mjs
-> controlled restart
-> real private semantic push above old 32 KiB tracked-path envelope
-> move qualified Office candidate from protected scratch into durable private Git
-> guarded preview.17 publication
-> fresh disposable DOCX/PPTX/XLSX host materialization/fidelity matrix
```

```text
OFFICE_FILE_LINK_SCRATCH_CANDIDATE=PASS
AB020_LIVE_ACTIVATION_REQUIRED=true
```
