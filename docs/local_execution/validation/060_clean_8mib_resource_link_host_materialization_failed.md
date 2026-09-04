# Validation 060: Clean 8 MiB Resource-Link Host Materialization Failed

**Date:** 2026-09-04
**Status:** FAIL / RESOURCE PREPARATION PASS / HOST FILE MATERIALIZATION FAIL
**Research:** Research 117

A fresh no-folder single-file qualification tested `32.LinearModels2.annotated.pdf` at exactly 8,715,014 bytes through only `codex.document_file_link`. The ADS tool succeeded and returned only the small `codexless.document-resource-link.v1` metadata result. No inline PDF bytes/base64, request-size error, timeout, maximum-chat-length failure, or other explicit transport/context failure was exposed in that tool turn.

The same conversation was then tested on the following ordinary user turn without another ADS/Codexless/Browser/web reacquisition. ChatGPT-side evidence showed: conversation file listing total 0; filename-specific conversation file search returned no result; `/mnt/data` contained no files; no PDF rendering or extraction could run because the PDF was absent. Therefore the previous 8.31 MiB resource link did not produce a ChatGPT-accessible conversation file on this host.

Accepted classification:
```text
codex.document_file_link preparation at 8,715,014 bytes = PASS
original tool result contains inline PDF/base64          = NO
explicit tool/host transport error                      = NONE SURFACED
host materialization receipt in first turn              = NONE
next-turn conversation file availability                = FAIL
next-turn /mnt/data PDF availability                     = FAIL
CLEAN_8MIB_NEXT_TURN_FULL_PDF_ACCESS                     = FAIL
```

This localizes the failure beyond ADS resource preparation but does not yet identify the hidden host layer. Possible layers still include host decision not to resolve the resource link, hidden `resources/read` failure/limit, tunnel/HTTP response handling, or host attachment-materialization limits. No exact size ceiling or causal layer is claimed yet.

The clean 4,435,890-byte `52.Trees.annotated.pdf` host materialization remains PASS. Therefore the current observed materialization boundary lies somewhere above 4,435,890 bytes and at or below 8,715,014 bytes for these tested files. The next smallest real lecture discriminator is `31.ProbabilisticModels1.annotated.pdf` at approximately 6.63 MiB.
