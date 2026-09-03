# Workspace-standard ordinary-folder authority and document-read live qualification

**Date:** 2026-09-03
**Status:** `PASS / LIVE QUALIFIED`
**Scope:** Preserve the first live qualification of a generic non-Git read-only workspace together with the first-class `codex.document_read` PDF semantic action.
**Authority:** Local-execution validation evidence. This record proves the exact tested authority/tool boundary; it does not broaden workspace authority or imply OCR/rendering support.

## Generic ordinary-folder workspace authority

A user-selected ordinary non-Git folder was explicitly admitted as:

```text
workspaceId          big-data-statistics
capabilities         [read]
semantic Git         disabled
allowed remote       null
integrity policy     workspace-standard
protected policy     workspace-standard-v1
protected paths      []
```

The exact machine-local root is intentionally not needed in public project authority. The accepted property is that it is an explicit canonical exact-root registration, not a parent user profile / OneDrive / broad host root. Descendants are covered by longest-root resolution; siblings remain outside this admission unless independently registered.

The registry after this admission is:

```text
schemaVersion  1
revision       3
contentHash    a1b430bc29bb29aa9736db3d63c92746be698d445043d12a1fedf7a61aa37319
workspaces     ads-public, ads-local-runtime, big-data-statistics
```

This validates the `workspace-standard` follow-up to Research 116: ordinary non-Git read authority can be added through server-owned policy without another MCP schema publication. `workspace-standard` deliberately rejects semantic-Git capability because Git requires an explicit Git integrity policy.

## First-class document semantic action

The published/live surface is:

```text
Codexless version        0.1.1-preview.9
surface version          codexless-public-preview-v2
public MCP tool count    52
new semantic action      codex.document_read
parser backend           pdfjs-dist@5.4.624
```

The live server's own Streamable HTTP MCP `tools/list` returned:

```text
TOOL_COUNT=52
HAS_DOCUMENT_READ=True
DOCUMENT_TOOL=codex.document_read
```

The action is model-free and read-only. It requires only the existing workspace `read` capability and exposes no caller-selected permission profile, sandbox, executable/parser command, host route, workspaceId override, write/agent/browser/Git authority, OCR, or rendering.

## Parser hardening accepted before publication

Before publication, the PDF reader was hardened so untrusted parsing does not occur in the main Codexless event loop. The live candidate uses a dedicated Node parser child process with:

```text
PDF.js pinned version           5.4.624
V8 old-space ceiling            256 MiB
default hard parser deadline    30 seconds
bounded protocol stdout/stderr  yes
Node permission model           enabled
filesystem write permission     absent
child-process/worker permission absent
filesystem read scope           installed Codexless runtime tree
PDF JavaScript evaluation       disabled
system font lookup              disabled
worker fetch                     disabled
OCR                              not performed
```

The main process also performs a bounded file-handle read capped at the 32 MiB limit plus one byte, then revalidates file identity and size. This closes the pre-read-stat growth race that would otherwise allow an unbounded `readFile()` materialization.

Focused regression result:

```text
DOCUMENT_READ_REGRESSION=PASS tests=11
FLEXIBLE_AUTHORITY_REGRESSION=PASS tests=7
BOUNDED_GIT_FETCH_ORIGIN=PASS tools=52
BOUNDED_GIT_PULL_FF_ONLY=PASS tools=52
PUBLIC_SURFACE_REGISTRATION=PASS tools=52
DOCUMENT_READ_DEPENDENCY_CONTRACT=PASS pdfjs-dist@5.4.624
```

The added hardening regressions prove that a timed-out parser child is terminated and the same reader remains usable afterward, and that file growth beyond the byte ceiling is detected without reading past ceiling plus one.

Key live/candidate hashes:

```text
document-reader.mjs
BED85100ABF31931512AB135EB5432B6E77A0F9D1B2EF65B3CF009E0BB527F2C

document-reader-child.mjs
85FB07A8FAA89781F6EB8FBE133436FCF2A222D64F3FD08011B68914544B95EF

publication helper
42A8BFFC960E3F485D014D61AAFD99BD0AB052F0FE86E83D82D5C4A80723072C
```

## Real document qualification

After the controlled restart, app/schema refresh, and fresh disposable ChatGPT discovery, `codex.document_read` was invoked directly against the read-only `big-data-statistics` workspace. No `command_exec` parser fallback was used.

Exact result for `BDS-exam-24-25-solutions.pdf`, page 1:

```text
workspaceId            big-data-statistics
relative path          BDS-exam-24-25-solutions.pdf
media type             application/pdf
SHA-256                acaf11f8512a4b61f8887e3710a6c717676d6a9b8d9c418cbe8fa08cc9d3e9de
size                    160885 bytes
parser                  pdfjs-dist@5.4.624
total pages             5
returned pages          [1]
OCR performed           false
page-1 characters       1774
truncated               false
```

The extracted text contained the expected first two exam problems and solutions, which is sufficient to prove useful embedded-text extraction from a real personal PDF through the intended semantic action.

## Boundary and residual limitations

Accepted now:

```text
explicit ordinary non-Git exact-root admission
read-only document access under the existing workspace read capability
bounded PDF embedded-text extraction
page selection and deterministic text-output truncation
source hash / size / parser / page provenance
isolated parser failure and timeout containment
```

Not accepted or implemented by this validation:

```text
broad arbitrary-host filesystem authority
Codexless runtime-maintenance authority
document rendering
OCR
DOCX/PPTX/XLSX adapters
OS-level network sandbox for the parser child
```

Node's permission model is not claimed to be a complete OS-level network sandbox. The current parser path intentionally disables evaluation/fetch behavior and receives bounded document bytes plus bounded metadata. A stronger OS-level parser sandbox may be researched later without changing the stable `codex.document_read` contract.

## Result

```text
WORKSPACE_STANDARD_GENERIC_FOLDER_AUTHORITY=PASS
DOCUMENT_READ_LIVE_QUALIFICATION=PASS
```

No Source Vault payload/state, protected `.tmp` residue, credentials, or unrelated host authority was changed by this qualification.
