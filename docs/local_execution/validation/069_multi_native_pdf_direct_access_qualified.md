# Validation 069: Multi-Native-PDF Direct ChatGPT Access Qualified

**Date:** 2026-09-06
**Status:** PASS / LARGE SOURCE REPRESENTED AS THREE NATIVE PDF PARTS / CHATGPT DIRECT SOURCE ACCESS VERIFIED
**Research:** Research 117 / Research 119
**Scope:** Qualify the deterministic multi-native-PDF fallback selected by Checkpoint 310 for an authorized PDF above the current whole-file host-materialization envelope, without Browser, upload UI, OCR, or a reasoning-model intermediary.

## Governing objective

Research 119 remains authoritative. The target is direct bounded ChatGPT access to authorized local-machine files through Codexless. A valid fallback may transform one source into deterministic, faithful, model-free source parts, but ChatGPT itself must receive those source parts directly.

## Source fixture

The qualification reused the established eight-page held-out synthetic PDF:

```text
path
    .tmp/astra-phase2-pdf-worker-01/source.pdf

bytes
    11,825,407

SHA-256
    be09c6065c36a9beaa32e812382b7fee7d8366dcb23f99a49e88f7306c99bc7f

pages
    8
```

The exact source identity was rechecked immediately before splitting.

## Why three parts were required

The clean whole-file host-materialization evidence remains:

```text
highest confirmed PASS    7,417,428 bytes
lowest confirmed FAIL     7,993,210 bytes
```

A naive two-part split at pages 1-4 / 5-8 produced:

```text
pages 1-4    7,870,684 bytes
pages 5-8    3,955,248 bytes
```

The first part exceeds the highest clean PASS and would not be a conservative qualification.

A deterministic exhaustive contiguous-range size check using the maintained primary-runtime `pypdf` found that the minimum-partition solution under the 7,417,428-byte qualification ceiling is three parts. The selected partition was:

```text
part 1    source pages 1-3    3,936,427 bytes
part 2    source page  4      3,935,151 bytes
part 3    source pages 5-8    3,955,281 bytes
```

Every part is therefore well below the known clean PASS envelope.

## Deterministic source-part construction

The parts were produced model-free with the maintained Codex primary-runtime Python and `pypdf`. The split copies source PDF pages directly into new valid PDFs and adds only provenance metadata:

```text
source SHA-256
source page range
source page count
qualification part index
```

Final identities:

```text
part 1
    file      source.part01.pages-01-03.pdf
    bytes     3,936,427
    SHA-256   0a79b2ce840f212bc19414fee5e2250176d1b19077c8cdf81d2df35ac078e9fd

part 2
    file      source.part02.pages-04-04.pdf
    bytes     3,935,151
    SHA-256   f29512500f6c3c243081b243aee70e8ae66c8c7ff61179297f3f7bde096dd7d1

part 3
    file      source.part03.pages-05-08.pdf
    bytes     3,955,281
    SHA-256   47b3104546f193695048b706a0475e754c370b1bc35c29f8773879b3883a6013
```

The splitter was rerun and all three part hashes plus the manifest hash reproduced exactly.

## Fidelity verification before handoff

The original source and all three parts were rendered model-free with the maintained primary-runtime Poppler renderer at the same resolution.

Ordered render SHA-256 comparison returned exact equality for all eight pages:

```text
source page 1 == part render    PASS
source page 2 == part render    PASS
source page 3 == part render    PASS
source page 4 == part render    PASS
source page 5 == part render    PASS
source page 6 == part render    PASS
source page 7 == part render    PASS
source page 8 == part render    PASS
```

Therefore the split preserved rendered page content exactly for this fixture.

## Direct Codexless handoff

The existing already-qualified `codex.document_file_link` tool was called once for each part from the same ordinary ChatGPT conversation.

All three calls returned only the small `codexless.document-resource-link.v1` metadata receipt. No PDF bytes/base64 were embedded in those tool-result envelopes.

The ChatGPT host then materialized all three PDFs into this conversation as ordinary file objects.

Host-side materialization evidence:

```text
part 1
    host file ID
        file_0000000080508243b90f16e63ec354e6
    ChatGPT-side path
        /mnt/data/source.part01.pages-01-03.pdf

part 2
    host file ID
        file_0000000073bc81f4bbe20007e88ccd11
    ChatGPT-side path
        /mnt/data/source.part02.pages-04-04.pdf

part 3
    host file ID
        file_00000000cd4c8210a36a275e8dad6011
    ChatGPT-side path
        /mnt/data/source.part03.pages-05-08.pdf
```

This is direct host evidence from the current conversation, not inferred from earlier resource-link tests.

## ChatGPT-side native PDF verification

After materialization, ordinary ChatGPT-side PDF tooling was used on the `/mnt/data` files rather than ADS/Codexless document readers.

The ChatGPT PDF Skill's `pdf_inspect.py` reported:

```text
part 1    3 pages    metadata source range 1-3
part 2    1 page     metadata source range 4-4
part 3    4 pages    metadata source range 5-8
```

The same Skill's `render_pdf.py` rendered all eight materialized pages successfully. ChatGPT visually inspected the resulting contact sheet and observed concrete source content across all three native parts:

```text
source page 1
    opening inventory: 137 units
    instruction says closing inventory appears on the last page

source page 2
    three-bar chart A/B/C
    B tallest, C intermediate, A shortest

source pages 3-5
    large synthetic raster/noise image payloads
    page text states there are no hidden semantic facts

source page 6
    Inspection batch: Q7M-42
    Release status: HOLD
    red circular visual marker

source page 7
    states middle image pages contain no inventory adjustment
    instructs using page 1 and page 8 for net inventory change

source page 8
    closing inventory: 219 units
```

Because pages 1 and 8 reside in different native part files, ChatGPT can also reason directly across the part boundary. For example, the inventory change supported by the source is:

```text
219 - 137 = +82 units
```

No semantic worker supplied those facts to ChatGPT.

## What this PASS establishes

This qualification establishes:

```text
authorized oversized PDF source
    -> deterministic faithful native PDF parts
    -> existing codex.document_file_link per part
    -> all parts materialize into one ordinary ChatGPT conversation
    -> ChatGPT directly inspects and reasons across the complete ordered source
```

For this fixture, this is a valid direct-source fallback beyond the current one-file materialization envelope.

## What this PASS does not establish

It does **not** establish:

```text
the unchanged 11,825,407-byte PDF materializes as one native ChatGPT file
7,417,428 bytes is a universal exact host limit
all PDFs can always be partitioned conveniently
split PDFs preserve every possible document-wide feature
signatures, outlines, cross-document links, attachments, forms, or document-level semantics survive arbitrary splitting
multi-part UX is automatically acceptable as the final product experience
```

Those remain separate architecture/product-quality questions.

## Decision

The experiment succeeds strongly enough to retain deterministic native PDF splitting as a real direct-access fallback, not merely a speculative architecture.

It should still be treated as a fallback beneath unchanged whole-file handoff because multiple files are less elegant than one source attachment and some PDF-wide semantics can span the original document container.

The next engineering decision is therefore not whether this mechanism works. It does. The next question is whether to productize it as the large-PDF fallback now, or first compare its practical UX/semantic trade-offs against the remaining heavier Browser-upload fallback and any newly available native host file primitive.

## Result

```text
SOURCE_IDENTITY = PASS
MINIMUM_CONSERVATIVE_PART_COUNT = 3
PART_GENERATION_DETERMINISTIC = PASS
PAGE_RENDER_FIDELITY = 8/8 EXACT MATCH
DOCUMENT_FILE_LINK_PART_1 = PASS
DOCUMENT_FILE_LINK_PART_2 = PASS
DOCUMENT_FILE_LINK_PART_3 = PASS
CHATGPT_HOST_MATERIALIZATION = 3/3 PASS
CHATGPT_NATIVE_PDF_INSPECTION = PASS
CROSS_PART_REASONING = PASS
SEMANTIC_INTERMEDIARY = NONE
MULTI_NATIVE_PDF_DIRECT_ACCESS = PASS
```
