# Checkpoint 292: MCP PDF Resource Attachment Materialized, Same-Turn Native PDF Failed

**Date:** 2026-09-04
**Status:** LIVE HOST DISCRIMINATION COMPLETE / TWO-STAGE PDF-SKILL TEST NEXT
**Checkpoint class:** EXPERIMENT_VERIFICATION
**Project stage:** Research 117 reuse-first multimodal document architecture
**Scope:** Preserves the live preview.12 result that `codex.document_file_read` successfully returns an MCP PDF resource and ChatGPT materializes it as a PDF attachment/file artifact, but the same model turn does not automatically receive parsed or visual native PDF input.
**Authority:** Validation 051 is primary evidence.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-17`
**Conversation title:** `17 - MCP Image Bridge Publication Recovery and Multimodal Document Continuation`
**Primary collaborator:** ChatGPT

## Boundary

Live publication/restart/schema refresh succeeded to:

```text
version        0.1.1-preview.12
surface        codexless-public-preview-v2
tool count     55
```

The existing document-read smoke passed. The earlier document-render smoke failure was traced to an incorrect test path; the corrected live render on `e117_managed_poppler_probe/probe.pdf` succeeded and returned both expected page images, so preview.12 did not regress the qualified smaller-page render path.

The new file-handoff experiment then established:

```text
codex.document_file_read                  live and callable
small PDF MCP resource                    succeeds
ChatGPT PDF attachment/file card          materialized
same-turn model PDF parsing/vision        absent
MCP_PDF_RESOURCE_TO_CHATGPT_NATIVE_PDF    FAIL
```

A representative 1.68 MiB PDF produced repeated `maximum chat length is reached` errors in otherwise fresh/usable chats, consistent with the 2.24M-character inline base64 tool payload being an unsuitable representative transport. Exact host size limits are not claimed.

## Architectural consequence

Do not resume custom loopback page-image transport yet. The observed attachment materialization opens a smaller zero-code-change experiment first:

```text
same chat, next user turn
    -> invoke first-party @PDF Skill
    -> target the already-materialized probe.pdf attachment
    -> ask for visual/content facts
```

If the PDF Skill can consume that file artifact, the local-authority seam is closer to solved than same-turn promotion suggested. The remaining transport optimization would be to avoid inline base64, likely by testing a server-owned `resource_link`/resource-read path.

If the PDF Skill cannot consume it, then MCP resource materialization is not a usable bridge into first-party PDF understanding and the project should return to the remaining supported candidates.

## Exact continuation

```text
1. in the same disposable chat that now shows the probe.pdf attachment card, invoke @PDF in the next user message;
2. ask @PDF to inspect exactly that already-materialized attachment and report visual facts from both pages;
3. prohibit ADS/document_render/document_read/Codex/Browser/OCR fallback so the result discriminates PDF-Skill attachment consumption;
4. if PASS, test whether a resource_link/resource-read design can materialize a representative local PDF without inline multi-megabyte base64;
5. if FAIL, preserve the failure and reassess loopback/native-Codex/third-party routes;
6. keep Checkpoint 289 loopback implementation unpublished until this reuse-first branch closes.
```

Primary evidence:

```text
docs/local_execution/validation/051_mcp_pdf_resource_materializes_attachment_but_not_same_turn_native_pdf.md
docs/checkpoints/291_document_file_handoff_publication_preflight_qualified.md
docs/local_execution/validation/050_document_file_handoff_publication_preflight_qualified.md
docs/research/117_reuse_first_multimodal_document_architecture_and_local_media_handoff.md
```
