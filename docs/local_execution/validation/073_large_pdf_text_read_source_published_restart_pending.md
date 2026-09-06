# Validation 073: Large-PDF Text Read Source Published, Restart Pending

**Date:** 2026-09-06
**Status:** STATIC PASS / LIVE SOURCE PUBLISHED / CONTROLLED RESTART PENDING
**Research:** Research 117 / Research 119
**Scope:** Extend the existing first-class `codex.document_read` embedded-text path from a 32 MiB source ceiling to a bounded 96 MiB source ceiling without changing the public tool schema or authority model.

## Baseline failure on the real source

Before publication, the live tool was called directly on:

```text
workspace     machine-learning
source        51.Deep Learning2.annotated.pdf
source bytes  78,874,939
page          16
```

The existing live tool failed before page selection with:

```text
DOCUMENT_SIZE_LIMIT
limitBytes  33,554,432
sizeBytes   78,874,939
```

This confirms that the remaining text-path limitation was a whole-source admission limit, not an oversized-page-only limit.

A separate small-source call on `32.LinearModels2.annotated.pdf` page 1 confirmed the existing live contract and parser:

```text
schemaVersion  codexless.document-read.v1
parser         pdfjs-dist 5.4.624
```

## Candidate design

The public action remains unchanged:

```text
codex.document_read(cwd, documentPath, pages?, maxCharacters?)
```

Only the bounded source ceiling changes:

```text
MAX_DOCUMENT_BYTES
32 MiB -> 96 MiB
```

The parent continues to read one bounded, stable source snapshot before parsing and preserves the existing canonical-path, file-identity, growth and SHA-256 semantics.

The isolated parser child was also tightened for large inputs. Its private protocol now receives the server-owned declared source byte count, preallocates exactly one bounded input buffer, rejects shorter/longer stdin than declared, and passes PDF.js a zero-copy `Uint8Array` view over that same buffer. This removes the old chunk-list plus `Buffer.concat` whole-source duplication and avoids an additional typed-array copy.

The existing child heap ceiling remains 256 MiB.

## Static qualification

Private candidate:

```text
.ads-private/codexless/large-pdf-text-read-candidate/
```

Checks:

```text
node --check document-reader.mjs        PASS
node --check document-reader-child.mjs  PASS

focused large-source tests
    tests 3
    pass  3
    fail  0
```

The focused tests establish:

```text
- a 40 MiB source above the old ceiling is admitted;
- the exact source size is passed to the isolated parser interface;
- the complete bounded source snapshot reaches that interface;
- a source above 96 MiB is rejected before parser start;
- the implementation ceiling is exactly 96 MiB.
```

## Guarded installed-source publication

Pre-publication live identities:

```text
src/document-reader.mjs
    SHA-256 bed85100abf31931512ab135eb5432b6e77a0f9d1b2ef65b3cf009e0bb527f2c

src/document-reader-child.mjs
    SHA-256 85fb07a8faa89781f6eb8fbe133436fcf2a222d64f3fd08011b68914544b95ef
```

Hash-verified backups were created:

```text
src/document-reader.mjs.pre-large-pdf-text-read-20260906.bak
src/document-reader-child.mjs.pre-large-pdf-text-read-20260906.bak
```

Published source identities, exactly matching the preserved candidate:

```text
src/document-reader.mjs
    SHA-256 42d1479f53558dfedbe048d29011229a88ca551e13d5fdd2970130a52eb31b58

src/document-reader-child.mjs
    SHA-256 588e14597e6dc39270860c00044e2ac7e720ffbaf045fbdb6e900162c421b140
```

Both published files passed `node --check`.

## Installed dependency smoke test

Before restart, the new source modules were exercised directly inside the installed Codexless dependency environment on a valid synthetic PDF larger than the old ceiling:

```text
source bytes    36,700,855
parser          pdfjs-dist 5.4.624
extracted text  large source installed smoke test
status          PASS
```

The temporary smoke-test file and script were removed afterward.

This is important because it tests the changed parent and child against the actual pinned live PDF.js dependency rather than only a fake parser.

## Workspace authority

A temporary exact-root `codexless-live` admission was used only for bounded installed-source publication/testing. It was removed afterward.

Durable registry after removal:

```text
revision       12
content hash   e648cfb1aaa295f44ba5327181738a7f485ed9ebb5c5ef6deee193bd3eb07322
workspaces     ads-public, ads-local-runtime, big-data-statistics, machine-learning
```

The `machine-learning` workspace remains strictly read-only.

## Private preservation

Private runtime evidence is synchronized to `origin/main` at:

```text
96f58fea13377943a0fbec2889384329bce49cb5
RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
postflightOk=true
```

## Exact next qualification

The currently running Codexless process still has the pre-publication module loaded.

Follow the canonical controlled Codexless/tunnel restart from `docs/local_execution/OPERATIONS.md`. The public tool schema and tool count did not change, so no Plugin refresh is required.

Then call in this same ChatGPT conversation:

```text
codex.document_read
cwd          C:\School\Machine Learning
documentPath 51.Deep Learning2.annotated.pdf
pages        [16]
maxCharacters 25000
```

PASS requires direct embedded text from page 16 to reach ChatGPT from the 78,874,939-byte authorized read-only source, with no OCR, Browser, source-workspace write, manual upload or reasoning-model intermediary.

## Result

```text
LARGE_PDF_TEXT_READ_CANDIDATE = STATIC_PASS
LIVE_SOURCE_PUBLICATION = PASS
INSTALLED_36MB_SMOKE = PASS
TOOL_SCHEMA_CHANGED = NO
LIVE_PROCESS_RESTART = PENDING
REAL_78MB_PAGE16_DOCUMENT_READ = PENDING
NEXT = CONTROLLED_RESTART_THEN_DOCUMENT_READ_PAGE16
```
