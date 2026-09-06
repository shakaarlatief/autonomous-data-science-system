# Validation 070: Machine Learning Large-PDF Splitter Generalization

**Date:** 2026-09-06
**Status:** MIXED / PAGE-RANGE SPLITTING GENERALIZES TO MANY FILES / SINGLE-PAGE OVERSIZE BREAKS NATIVE-PDF-ONLY FALLBACK
**Research:** Research 117 / Research 119
**Scope:** Evaluate how the Checkpoint 311 deterministic native-PDF splitter would behave on the larger authorized PDFs in the `machine-learning` workspace, without modifying that read-only source workspace.

## Workspace boundary

The registered `machine-learning` workspace remains read-only. No source PDF or split output was written there. All inspection used model-free read-only command execution against the authorized workspace.

## Files above the known clean whole-file host PASS envelope

The known clean whole-PDF PASS remains 7,417,428 bytes. Fifteen PDFs in the machine-learning workspace exceed it:

```text
51.Deep Learning2.annotated.pdf            78,874,939 bytes   56 pages
11.Introduction.annotated.pdf              58,443,253 bytes   53 pages
unraveling-pca.pdf                         46,684,862 bytes  266 pages
00.Preliminaries.annotated.pdf             40,775,434 bytes   70 pages
Transformers.annotated.pdf                 40,254,527 bytes   34 pages
71.Reinforcement Learning.annotated.pdf    34,862,777 bytes   37 pages
book-v1.2.0-cropped.pdf                    33,385,812 bytes  265 pages
21.Methodology1.annotated.pdf              32,162,504 bytes   53 pages
41.DeepLearning1.annotated.pdf             30,148,932 bytes   41 pages
62.Matrices.annotated.pdf                  19,822,400 bytes   27 pages
72.Review.annotated.pdf                    17,080,579 bytes   13 pages
22.Methodology2.annotated.pdf              12,797,065 bytes   46 pages
12.LinearModels1.annotated.pdf             11,611,714 bytes   34 pages
61.SequentialModels.annotated.pdf          11,142,975 bytes   38 pages
32.LinearModels2.annotated.pdf              8,715,014 bytes   38 pages
```

At a 7,000,000-byte production planning target, source-byte lower bounds alone range from 2 parts for the smaller files to at least 12 parts for `51.Deep Learning2.annotated.pdf`. Those counts are only lower bounds because PDF page resources are not uniformly distributed.

## Exact representative partition: Deep Learning 2

A model-free pypdf partition planner serialized candidate contiguous page ranges in memory under a 7,000,000-byte target. It did not write outputs.

For `51.Deep Learning2.annotated.pdf`, ordinary page-range splitting can form many acceptable native PDF parts, but two individual pages cannot fit below the target by page-boundary splitting alone:

```text
page 16 single-page PDF    15,944,609 bytes
page 49 single-page PDF     7,784,782 bytes
```

The surrounding successful ranges show that the planner itself works as intended, for example:

```text
pages 1-7      4,380,348 bytes
pages 8-11     5,506,735 bytes
pages 12-14    6,432,947 bytes
pages 22-27    6,978,607 bytes
pages 38-41    6,952,103 bytes
```

But no page-range partition can reduce page 16 below the host envelope because the page itself is already much larger than it.

Basic pypdf stream compression/deduplication does not solve this example:

```text
page 16 plain               15,944,609 bytes
page 16 compressed content  15,937,733 bytes
page 16 deduplicated        15,944,298 bytes

page 49 plain                7,784,782 bytes
page 49 compressed content   7,782,882 bytes
```

The oversized page is not merely uncompressed drawing commands. Page 16 contains many embedded image XObjects, including one approximately 2.94 MB Flate image and numerous approximately 0.3 MB JPEG images, so its native page resource set itself is large.

## Other annotated PDFs show the same issue

Single-page serialization checks found pages above the 7,000,000-byte planning target in several other large annotated files:

```text
11.Introduction.annotated.pdf
    page 1     15,693,739 bytes
    page 12    17,597,874 bytes
    page 32    14,066,260 bytes
    page 45    10,062,435 bytes

Transformers.annotated.pdf
    page 1      8,583,619 bytes
    page 21     9,344,326 bytes
    page 32     9,422,430 bytes

00.Preliminaries.annotated.pdf
    page 39     7,215,493 bytes
    page 47     7,038,776 bytes

71.Reinforcement Learning.annotated.pdf
    page 18    14,059,747 bytes

21.Methodology1.annotated.pdf
    page 27    10,025,200 bytes

41.DeepLearning1.annotated.pdf
    page 39    14,048,969 bytes

62.Matrices.annotated.pdf
    page 3      7,090,215 bytes
```

By contrast, no single page above 7,000,000 bytes was found in the sampled smaller oversized PDFs:

```text
72.Review.annotated.pdf
22.Methodology2.annotated.pdf
12.LinearModels1.annotated.pdf
61.SequentialModels.annotated.pdf
32.LinearModels2.annotated.pdf
```

For those files, ordinary native page-range splitting remains a viable direct-source fallback in principle.

## Additional current-tool limitation

The existing first-class `codex.document_read` and `codex.document_render` tools currently reject sources larger than 33,554,432 bytes before page selection. For example, both reject the 78,874,939-byte Deep Learning 2 source even when only page 16 is requested.

Therefore the current fallback cannot simply say:

```text
oversized native page
    -> call document_render on that page
```

for these very large source PDFs. A new internal route must first isolate the page or otherwise operate without the current whole-source 32 MiB admission ceiling.

## Architecture consequence

Checkpoint 311 remains valid: deterministic native PDF parts are a proven direct-source fallback whenever every required part can fit below the host envelope.

Validation 070 narrows its generality:

```text
large PDF
    -> native page-range splitting
        -> works while each source page can be represented below host ceiling
        -> fails for a source page whose own native PDF representation exceeds ceiling
```

The production design therefore needs a hybrid direct-source policy rather than a native-PDF-only splitter.

Recommended bounded hierarchy:

```text
1. unchanged whole-file resource_link
   when the host-qualified envelope permits it

2. deterministic native PDF parts
   when contiguous page ranges fit below a conservative part ceiling

3. oversized-single-page model-free fallback
   isolate the exact page internally, then expose faithful page information directly to ChatGPT,
   preferably page text plus a bounded high-fidelity render/image representation

4. Browser upload
   remains a heavier fallback if a single original attachment is materially preferable
   and cleaner host primitives remain unavailable
```

The oversized-page route must not use another reasoning model. It should also avoid requiring write authority in the source workspace; the `machine-learning` workspace is intentionally read-only.

A clean implementation direction is a Codexless-owned ephemeral/generated-resource path: read the authorized source, verify source identity, deterministically isolate the requested page/range in memory or Codexless-owned temporary storage, and expose the resulting PDF/image resource to ChatGPT. This would also allow PDF text/render tooling to operate on isolated parts rather than rejecting a 75 MB source before page selection.

## Result

```text
MACHINE_LEARNING_PDFS_ABOVE_CLEAN_PASS = 15
PAGE_RANGE_NATIVE_SPLITTING = VIABLE_FOR_MANY_RANGES
NATIVE_PDF_ONLY_GENERALIZATION = FAIL
OVERSIZED_SINGLE_PAGE_EXAMPLES = CONFIRMED
LARGEST_OBSERVED_SINGLE_PAGE = 17,597,874 bytes
CURRENT_DOCUMENT_READ_RENDER_32MIB_SOURCE_LIMIT = RELEVANT
SOURCE_WORKSPACE_WRITE_REQUIRED = NO / SHOULD REMAIN NO
NEXT = QUALIFY_HYBRID_OVERSIZED_SINGLE_PAGE_DIRECT_SOURCE_ROUTE
```
