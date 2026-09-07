# Research 121: Non-PDF File Capability Matrix and Native Handoff Reuse

**Date:** 2026-09-06
**Status:** ACTIVE / OFFICE PREVIEW.17 SOURCE PUBLISHED / CONTROLLED RESTART NEXT
**Scope:** Determine the professional direct-source architecture for authorized DOCX, PPTX and XLSX files after the PDF route family closed under Research 120. Prefer whole-file/native ChatGPT handoff when the host can consume the original file faithfully; add model-free structure or rendering fallbacks only where direct native handling is insufficient.
**Declared references:** `research:119`, `research:120`, `checkpoint:328`, `path:docs/OPEN_ARCHITECTURE_BACKLOG.md`

## 1. Governing objective

The objective remains direct ChatGPT access to authorized local files, not delegated interpretation merely because a file lives on the local machine. The next format work should therefore start from the question:

```text
Can the original authorized file reach ordinary ChatGPT through a supported host/file transport first?
```

Only if the answer is no, or if the native host path loses material content such as embedded visuals, formulas, charts or structure, should a format-specific fallback be added.

## 2. Current official product evidence

OpenAI's current file-upload documentation explicitly lists the common Office Open XML formats among supported ChatGPT uploads:

```text
DOCX
PPTX
XLSX
```

Source: OpenAI Help Center, `What types of files are supported?`
https://help.openai.com/en/articles/8983675-what-types-of-files-are-supported

The current File Uploads FAQ states that ChatGPT can work with documents, spreadsheets and presentations, gives a general 512 MB per-file hard upload limit, and notes an approximately 50 MB spreadsheet limit depending on row size. Those product upload limits are useful context but are **not evidence that MCP resource-link materialization has the same envelope**. Research 117 already showed that the ChatGPT host's resource-link materialization envelope for PDFs is materially smaller than the ordinary manual-upload product limit.

Source: OpenAI Help Center, `File Uploads FAQ`
https://help.openai.com/en/articles/8555545-file-uploads-faq

A current OpenAI Enterprise guidance page describes DOCX/PPTX as text-based retrieval inputs and XLS/XLSX as commonly handled through code analysis, while visual retrieval is called out specifically for PDFs. This is architecture-relevant evidence that successful whole-file handoff does not automatically prove visual fidelity for Office documents. Because that page is Enterprise-oriented, it is a **design hint**, not a claim about the exact Plus-host behavior in this project.

Source: OpenAI Help Center, `Optimizing File Uploads in ChatGPT Enterprise`
https://help.openai.com/en/articles/10029836

## 3. Current MCP evidence

The maintained Model Context Protocol is not PDF-specific. Tool results may return a `resource_link` carrying a URI, name, MIME type and size. The client can resolve that resource through `resources/read`, whose binary resource contents carry a MIME type plus blob payload.

Sources:

```text
MCP 2025-11-25 Tools
https://modelcontextprotocol.io/specification/2025-11-25/server/tools

MCP 2025-11-25 Resources
https://modelcontextprotocol.io/specification/2025-11-25/server/resources
```

Therefore there is no protocol-level reason to invent a separate transport mechanism merely because the source is DOCX, PPTX or XLSX. The first discriminator should be whether the current ChatGPT host materializes and consumes those MIME types when supplied through the same resource-link pattern already qualified for PDFs.

## 4. Existing local implementation seam

The existing whole-PDF resource-link path already has the hard parts required for a generic binary file handoff:

```text
workspace authority resolution
canonical path containment
regular-file check
bounded size check
SHA-256 binding
pre/post source identity checks
ephemeral server-owned opaque resource token
TTL and bounded entry count
resources/read revalidation before byte release
resource_link metadata with name, MIME type and size
no file bytes/base64 in the original tool result
```

The PDF restriction is local rather than protocol-driven. The current file reader hard-codes `application/pdf`, requires a PDF header, and the current resource store rejects any prepared binding whose media type is not PDF. The resource-link/store lifecycle itself is otherwise generic.

This makes reuse preferable to a new transport stack.

## 5. Candidate architecture

Add one narrow generic whole-file handoff surface, provisionally named `codex.file_link`, while preserving the existing PDF tools unchanged.

First accepted format set:

```text
.docx  application/vnd.openxmlformats-officedocument.wordprocessingml.document
.pptx  application/vnd.openxmlformats-officedocument.presentationml.presentation
.xlsx  application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
```

The first candidate should:

```text
require the existing workspace read capability only
accept only cwd + one workspace-relative filePath
reject absolute paths, parent traversal, junction/symlink escape and non-files
bind size, identity and SHA-256 before exposing a resource link
use an explicit extension/MIME allowlist
require the OOXML ZIP signature for the first candidate rather than trusting the extension alone
serve bytes only through an opaque, expiring server-owned resources/read binding
revalidate source identity/content before byte release
return no binary/base64 bytes in the tool result
expose no executable, parser, Browser, Agent, write, sandbox or destination controls
leave the existing PDF-specific path frozen rather than silently changing its contract
```

A stronger OOXML package classifier may later inspect the package structure if the simple ZIP-signature + extension/MIME binding proves insufficient. Do not add that complexity before the host-transport discriminator shows the route is useful.

## 6. Candidate size policy

Do not infer the generic MCP handoff ceiling from ChatGPT manual-upload limits. The first Office qualification should use tiny deterministic samples. A source-side preparation ceiling can remain conservative and explicit; host materialization scaling should be measured separately per format only if real use requires it.

This avoids repeating the PDF mistake of conflating:

```text
server can prepare/read a resource
```

with:

```text
ChatGPT host can materialize that resource into the conversation/file layer at the same size
```

## 7. Fresh-host capability matrix

Create deterministic synthetic files that exercise more than plain text:

```text
DOCX
    heading + paragraph
    table
    embedded image

PPTX
    multiple slides
    titles/body text
    shapes or diagram
    embedded image

XLSX
    multiple sheets
    numeric/text cells
    formula
    chart or structured formatting
```

Then, in a fresh disposable ChatGPT conversation, qualify exactly one native file-link call per format and distinguish four separate questions:

```text
1. Did the resource_link resolve/materialize into the host file layer?
2. Can ChatGPT access the file's text/data/structure?
3. Can ChatGPT access embedded visual/layout content that matters?
4. Does the route preserve enough fidelity that a format-specific fallback is unnecessary?
```

The answer may differ by format. A materialized PPTX that yields text but not slide visuals is not equivalent to a fully faithful native presentation route. An XLSX that materializes into the spreadsheet/code-analysis path may already be sufficient without a custom parser.

## 8. Fallback decision rule

Do not pre-build Office parsers or renderers. Use the matrix result:

```text
native materialization + sufficient fidelity
    -> keep whole-file handoff as the default

native materialization + missing visual/structural fidelity
    -> preserve native file plus add only the missing model-free view

host does not materialize the MIME type
    -> research the narrowest faithful model-free parser/render route for that format
```

For DOCX/PPTX, visual fidelity may require page/slide rendering later. For XLSX, structure/formulas/data should be tested before considering any custom extraction because ChatGPT already has spreadsheet-aware workflows.

## 9. Security and authority invariants

The generic handoff must not become an arbitrary local-file exfiltration primitive. The format allowlist, workspace authority, canonical-path containment, read-only capability, size bound, exact source binding and expiring server-owned token remain mandatory. No caller-selected MIME type is accepted; MIME derives from the server's extension/type policy.

Do not broaden the first candidate to executables, archives, arbitrary binary blobs, credentials, databases or unknown extensions simply because MCP resources can technically carry arbitrary bytes.

## 10. Relationship to the PDF hardening caveat

Checkpoint 328 exposed Node's standard `--allow-addons` warning on cached PDF rendering. That warning remains an AB-027 hardening trigger and does not justify using rendering as the default for Office files. Native whole-file handoff should be tried first precisely because it is both simpler and preserves the original source.

## 11. Next implementation step

The private-runtime preservation gate reached its previously reproduced 32 KiB tracked-path enumeration edge before a clean new candidate file could be added. Checkpoint 330 / Validation 088 qualify the bounded AB-020 correction and guarded publication preflight. Therefore the immediate sequence is:

```text
AB-020 live proof completed above the old 32 KiB envelope
-> Office candidate durably preserved in private Git
-> publish the guarded preview.17 Office file-link package
-> qualify authority, MIME allowlist, binding, TTL, drift and no-inline-bytes tests
-> generate tiny deterministic DOCX/PPTX/XLSX fixtures
-> stage/public-regress without changing existing PDF contracts
-> guarded publication and controlled restart
-> fresh disposable three-format host-materialization/fidelity matrix
-> add format-specific fallback only where the matrix demonstrates a real gap
```

This research deliberately stops before assuming that successful manual uploads imply successful MCP materialization or that successful file materialization implies full multimodal fidelity.
