# Validation 071: Large-PDF Page Render Source Published, Restart Pending

**Date:** 2026-09-06
**Status:** CANDIDATE STATIC PASS / LIVE SOURCE PUBLISHED / CONTROLLED RESTART PENDING
**Research:** Research 117 / Research 119
**Scope:** Preserve the implementation and publication boundary for extending the existing model-free `codex.document_render` path to authorized PDF sources up to 96 MiB without changing the public tool schema.

## Why this candidate exists

Validation 070 established that native PDF page-range splitting is not universal because several real Machine Learning PDFs contain individual pages whose one-page native PDF representation still exceeds the ChatGPT host-materialization envelope.

The representative source is:

```text
C:\School\Machine Learning\51.Deep Learning2.annotated.pdf
bytes     78,874,939
pages     56

page 16 native one-page PDF
bytes     15,944,609
```

A model-free feasibility probe using the same maintained PDF.js + canvas stack as the existing renderer succeeded directly against that 78,874,939-byte read-only source:

```text
page 16
    150 DPI
    1240 x 1755
    PNG bytes   583,130
    PNG SHA-256 aca9cfadbfcb99382e22a2472495f26d1ab097922ce9406d66a8121810a56023
```

The same bounded 256 MiB Node heap also extracted 17,999 embedded-text characters from page 16. Therefore the page itself is processable model-free; the blocking issue was the renderer's inherited 32 MiB whole-source admission ceiling.

## Candidate design

The renderer now has a separate:

```text
MAX_RENDER_SOURCE_BYTES = 96 MiB
```

Rather than reading the entire source into the renderer parent process twice for identity checks, the candidate:

```text
- reads only the first 1,024 bytes for PDF-header validation;
- hashes the authorized source in 1 MiB chunks before rendering;
- invokes the unchanged renderer child inside the existing Codex read-only command sandbox;
- hashes the source again afterward;
- preserves path, size, mtime, dev/inode and SHA-256 drift detection;
- keeps the 4 MiB per-page PNG ceiling;
- keeps the 8 MiB aggregate rendered-image ceiling;
- keeps `codex.document_read` at its existing 32 MiB source ceiling for now.
```

This is a narrower change than globally raising all document limits and does not require writing into the read-only Machine Learning workspace.

## Static qualification

Private candidate location:

```text
.ads-private/codexless/large-pdf-page-render-candidate/
```

Private preservation commit before publication:

```text
461592465b921aa13be8e531dad8bd9641918e1f
```

Static checks:

```text
node --check document-renderer.mjs                  PASS
large-source candidate tests                       2 / 2 PASS
real page-16 PDF.js+canvas feasibility             PASS
real page-16 combined render+text at 256 MiB heap  PASS
```

## Controlled live publication

A temporary exact-root `codexless-live` workspace admission was created only for the already-qualified source publication, then removed after source/test verification.

Pre-mutation live renderer:

```text
src/document-renderer.mjs
bytes      19,155
SHA-256    d447190589e61e04e500e31995b64151d9b47388ba77f26745a20642933de4c0
```

Backup:

```text
src/document-renderer.mjs.pre-large-pdf-page-render-20260906.bak
SHA-256    d447190589e61e04e500e31995b64151d9b47388ba77f26745a20642933de4c0
```

Published live renderer:

```text
src/document-renderer.mjs
SHA-256    e8028cc913346b1d415aa419b252ed0efaf374b8d145ac08ddb836224b393f0f
```

Candidate and published live source match after BOM/line-ending/trailing-newline normalization:

```text
normalized SHA-256
086495484c2210599c3efb5256937c4d4ad215c90589dd3d10fc6cdc0d08829f
```

The installed renderer regression was updated to the new render-specific source ceiling and rerun:

```text
DOCUMENT_RENDER_REGRESSION=PASS
10 / 10 checks PASS
```

The temporary workspace admission was removed. Durable registry after removal:

```text
revision       9
content hash   12a82d711f0a4ec71eebc67acf5ed46ed2c0530481a88bb6f93fa51c55266dd0
workspaces     ads-public, ads-local-runtime, big-data-statistics, machine-learning
```

Private post-publication evidence is synchronized at:

```text
e96d53248de6718d14072dd857325a15587be5dc
RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
postflightOk=true
```

## Exact next qualification

The currently running Codexless process still has the pre-publication module loaded. Follow the canonical controlled restart order in `docs/local_execution/OPERATIONS.md`, then call the unchanged existing tool in this same ChatGPT conversation:

```text
codex.document_render
cwd          C:\School\Machine Learning
documentPath 51.Deep Learning2.annotated.pdf
pages        [16]
```

No Plugin refresh is required because the tool schema and tool count did not change.

PASS requires one standard MCP PNG image to reach ChatGPT directly from the 78,874,939-byte authorized local source, under the existing read-only Machine Learning authority, with no Browser, upload, OCR, source-workspace write, or reasoning-model intermediary.

## Result

```text
LARGE_PDF_PAGE_RENDER_CANDIDATE = STATIC_PASS
LIVE_SOURCE_PUBLICATION = PASS
TOOL_SCHEMA_CHANGED = NO
LIVE_PROCESS_RESTART = PENDING
END_TO_END_CHATGPT_PAGE16_IMAGE = PENDING
NEXT = CONTROLLED_RESTART_THEN_DOCUMENT_RENDER_PAGE16
```
