# Validation 061: Clean 6.63 MiB Resource-Link Host Materialization Passed

**Date:** 2026-09-04
**Status:** PASS / CLEAN 6.63 MiB HOST MATERIALIZATION QUALIFIED
**Research:** Research 117

A fresh no-folder single-file qualification tested `31.ProbabilisticModels1.annotated.pdf` through only `codex.document_file_link`. The ADS tool succeeded with a small metadata-only `codexless.document-resource-link.v1` result.

Direct evidence: filename `31.ProbabilisticModels1.annotated.pdf`; MIME type `application/pdf`; exact size 6,954,298 bytes; SHA-256 `c16a8f5aa92db5af2d82d44f90cb14fcc1c5a46d1deb5575d6472b7c6e2c6da0`; no PDF bytes/base64 in the original tool result; no maximum-chat-length/request-size/transport/timeout/context failure.

Host materialization also passed directly: host file ID `file_0000000025b8821093307c7a9dd642b5` and `/mnt/data/31.ProbabilisticModels1.annotated.pdf` were exposed. No explicit MCP `resources/read` trace was surfaced, and the PDF contents were intentionally not inspected in that turn.

Accepted result:
```text
CLEAN_INTERMEDIATE_RESOURCE_LINK_MATERIALIZATION=PASS
```

Combined with Validation 060, the currently observed clean host boundary lies above 6,954,298 bytes and at or below 8,715,014 bytes for the tested PDFs. This is not yet proof of a pure byte threshold; file-specific or host-state effects remain possible. Additional real-file discriminators near that interval are required.
