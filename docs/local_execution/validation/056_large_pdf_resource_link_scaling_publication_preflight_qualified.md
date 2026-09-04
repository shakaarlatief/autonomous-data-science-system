# Validation 056: Large PDF Resource-Link Scaling Publication Preflight Qualified

**Date:** 2026-09-04
**Status:** PASS / LARGE-PDF RESOURCE-LINK SCALING PREFLIGHT QUALIFIED / LIVE HOST TEST PENDING
**Research:** Research 117
**Live baseline:** `0.1.1-preview.13` / `codexless-public-preview-v2` / 56 tools
**Candidate target:** `0.1.1-preview.14` / `codexless-public-preview-v2` / 56 tools

## Motivation from the real Machine Learning corpus

A newly authorized read-only `machine-learning` workspace contains annotated lecture PDFs ranging from 4.23 MiB to 75.22 MiB. The currently relevant lecture-file sizes include:

```text
52.Trees.annotated.pdf                  4.23 MiB
31.ProbabilisticModels1.annotated.pdf   6.63 MiB
32.LinearModels2.annotated.pdf          8.31 MiB
61.SequentialModels.annotated.pdf      10.63 MiB
12.LinearModels1.annotated.pdf         11.07 MiB
22.Methodology2.annotated.pdf          12.20 MiB
72.Review.annotated.pdf                16.29 MiB
62.Matrices.annotated.pdf              18.90 MiB
41.DeepLearning1.annotated.pdf         28.75 MiB
21.Methodology1.annotated.pdf          30.67 MiB
71.Reinforcement Learning.annotated.pdf 33.25 MiB
Transformers.annotated.pdf             38.39 MiB
00.Preliminaries.annotated.pdf         38.89 MiB
11.Introduction.annotated.pdf          55.74 MiB
51.Deep Learning2.annotated.pdf        75.22 MiB
```

Every annotated lecture PDF is therefore above the existing 4 MiB experiment ceiling. Large-file scaling is not an edge case; it is required for the intended source corpus.

## Candidate design

The embedded `codex.document_file_read` route deliberately keeps its existing 4 MiB ceiling because it places PDF base64 directly in the tool result and already proved unsuitable for representative payloads.

Only `codex.document_file_link` is widened. The candidate adds a separate 96 MiB resource-link ceiling:

```text
embedded PDF tool-result ceiling       4 MiB / 4,194,304 bytes (unchanged)
resource-link source ceiling           96 MiB / 100,663,296 bytes
largest current ML lecture             75.22 MiB
```

Resource preparation no longer calls the embedded reader and no longer stores the PDF or its base64 in the process-level resource store. Instead it:

```text
resolve existing workspace read authority
canonicalize cwd/root/target
reject escape/symlink-junction drift
stat exact source
reject source > 96 MiB before payload materialization
read only the bounded PDF header for media validation
stream the source once to compute SHA-256
revalidate source identity after hashing
store only an opaque internal file binding + provenance + expiry
return the same small MCP resource_link tool result
```

At a later MCP resource fetch, the reader reopens the bound file and revalidates:

```text
canonical root/path
size
mtime
filesystem device/inode where available
full SHA-256
```

Only then does it construct the temporary base64 blob required by the MCP binary `resources/read` response. The resource store itself therefore retains no large PDF base64 between prepare and fetch.

This is an important scaling correction, but not a claim that a 75 MiB MCP resource fetch will pass the ChatGPT host/tunnel. MCP binary resource contents are still base64 encoded on the resource-read wire, so progressive live host qualification remains mandatory.

## Standards/product context

Current MCP schema defines `ResourceLink.size` as raw bytes before base64/tokenization and states that hosts may use it to estimate context usage. `resources/read` binary contents are base64 `blob` strings. The MCP specification does not establish a universal large-resource byte limit.

Current OpenAI ChatGPT file-upload documentation states a 512 MB hard per-file upload limit for ordinary ChatGPT/GPT uploads. That is useful context showing the target lecture corpus is well below normal ChatGPT file size limits, but it does **not** prove the MCP resource-link/tunnel path supports the same limit.

Official references:

```text
https://modelcontextprotocol.io/specification/2025-11-25/schema
https://help.openai.com/en/articles/20001052
```

## Regression and integrated staging

```text
DOCUMENT_FILE_READ_REGRESSION=PASS tests=7
DOCUMENT_RESOURCE_LINK_REGRESSION=PASS tests=9
BOUNDED_GIT_FETCH_ORIGIN=PASS tools=56
BOUNDED_GIT_PULL_FF_ONLY=PASS tools=56
PUBLIC_SURFACE_REGISTRATION=PASS tools=56
IMAGE_READ_REGRESSION=PASS tests=7
DOCUMENT_RENDER_REGRESSION=PASS tests=10
DOCUMENT_RESOURCE_LARGE_INTEGRATED_PREFLIGHT=PASS
DOCUMENT_RESOURCE_LARGE_PUBLICATION_PREFLIGHT=PASS
EXPECTED_PUBLIC_SERVER_VERSION=0.1.1-preview.14
EXPECTED_PUBLIC_SURFACE_VERSION=codexless-public-preview-v2
EXPECTED_PUBLIC_TOOL_COUNT=56
EMBEDDED_DOCUMENT_FILE_READ_LIMIT_BYTES=4194304
RESOURCE_LINK_DOCUMENT_LIMIT_BYTES=100663296
RESOURCE_PREPARE_RETAINS_BASE64=false
RESOURCE_FETCH_REVALIDATES_SIZE_MTIME_IDENTITY_SHA256=true
MODEL_TURN_REQUIRED=false
BROWSER_REQUIRED=false
NEW_EXTERNAL_DEPENDENCY=false
PAUSED_LOOPBACK_RENDER_TRANSPORT_OVERLAID=false
NO_LIVE_FILES_MODIFIED=true
```

New focused regression coverage proves that a PDF just above 4 MiB is still rejected by the embedded route but can be prepared/fetched through the resource-specific path, while a sparse source above 96 MiB fails before payload reading. Resource-store regression proves preparation does not call the byte-materialization method and only fetch invokes it.

## Live qualification plan

After guarded publication/restart, do not jump immediately to the 75 MiB file. Progressively discriminate host/tunnel limits using real lecture PDFs:

```text
4.23 MiB   52.Trees.annotated.pdf
8.31 MiB   32.LinearModels2.annotated.pdf
30.67 MiB  21.Methodology1.annotated.pdf
75.22 MiB  51.Deep Learning2.annotated.pdf
```

For each size, require:

```text
small original resource_link tool result
no maximum-chat-length/context failure
host PDF attachment materialization
no explicit inline PDF bytes in tool result
next-turn full-PDF access for at least the largest successful tier
```

If one tier fails, stop there and localize whether the limit is Codexless memory, tunnel/HTTP transport, MCP host resource handling, or ChatGPT file materialization before raising any ceiling further.

## Result

```text
LARGE_PDF_RESOURCE_LINK_SCALING_CANDIDATE      QUALIFIED LOCALLY
LIVE_RUNTIME                                  preview.13 / 56 unchanged
TARGET                                        preview.14 / 56
RESOURCE_LINK_LIMIT                           96 MiB
CURRENT_ML_LECTURE_CORPUS_COVERED_BY_LIMIT    YES
RESOURCE_STORE_PERSISTENT_BASE64               NO
LARGE_HOST_RESOURCE_FETCH                     UNPROVEN
NEXT                                           guarded publication -> restart -> progressive 4.23/8.31/30.67/75.22 MiB host tests
```
