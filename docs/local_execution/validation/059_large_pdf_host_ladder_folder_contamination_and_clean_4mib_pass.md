# Validation 059: Large PDF Host Ladder Folder Contamination and Clean 4 MiB Pass

**Date:** 2026-09-04
**Status:** PARTIAL PASS / FOLDER TEST CONTAMINATED / CLEAN 8.31 MiB RETEST REQUIRED
**Research:** Research 117

Two cumulative ChatGPT host tests were run after preview.14 activation. The first test was started inside a ChatGPT folder/project that already contains the Machine Learning files. All four `codex.document_file_link` calls returned success and the conversation reported attachment materialization through 78,874,939 bytes. However, because the surrounding ChatGPT folder already exposes the same Machine Learning source files, that run cannot cleanly attribute host-side file availability/materialization to the MCP resource-link handoff alone. It is therefore useful execution evidence for ADS tool success at all four sizes, but not accepted as a clean end-to-end host-materialization qualification.

A second cumulative test was run in a fresh chat outside that folder. There, `52.Trees.annotated.pdf` (4,435,890 bytes) produced direct host evidence of materialization at `/mnt/data/52.Trees.annotated.pdf`, and no maximum-chat-length/request-size/transport/timeout failure occurred. This is the first clean host PASS above the old 4 MiB ceiling. The same chat then called `codex.document_file_link` successfully on `32.LinearModels2.annotated.pdf` (8,715,014 bytes), with no inline PDF bytes and no explicit transport failure, but the model was not shown sufficient host evidence that the second PDF had materialized. Per the experiment stop rule, the 30.67 MiB and 75.22 MiB files were not attempted in that clean chat.

Accepted classification:
```text
folder/project cumulative run: ADS tool success at 4.23 / 8.31 / 30.67 / 75.22 MiB = DIRECT EVIDENCE
folder/project cumulative run: host materialization attribution = CONTAMINATED / NOT ACCEPTED FOR QUALIFICATION
fresh no-folder 4.23 MiB host materialization = PASS
fresh no-folder 8.31 MiB ADS resource-link tool call = PASS
fresh no-folder 8.31 MiB host materialization = INCONCLUSIVE
30.67 / 75.22 MiB clean-host materialization = UNTESTED
```

The next discriminating experiment is a fresh no-folder chat containing only the 8.31 MiB `32.LinearModels2.annotated.pdf` call. If that passes, continue similarly upward. A single-file clean chat removes both project-folder source contamination and cumulative multi-resource ambiguity.
