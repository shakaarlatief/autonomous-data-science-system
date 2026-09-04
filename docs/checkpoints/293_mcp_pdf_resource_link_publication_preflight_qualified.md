# Checkpoint 293: MCP PDF Resource-Link Publication Preflight Qualified

**Date:** 2026-09-04
**Status:** CANDIDATE QUALIFIED / HOST PUBLICATION PENDING
**Checkpoint class:** EXPERIMENT_VERIFICATION
**Project stage:** Research 117 reuse-first multimodal document architecture
**Scope:** Preserves preflight qualification of `codex.document_file_link`, a bounded local-PDF handoff candidate that returns a small standard MCP `resource_link` and serves PDF bytes separately through `resources/read`, avoiding PDF base64 in the original tool-result envelope.
**Authority:** Validation 052 is primary evidence. This checkpoint does not claim preview.13 is live or that ChatGPT follows/materializes the resource link.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-17`
**Conversation title:** `17 - MCP Image Bridge Publication Recovery and Multimodal Document Continuation`
**Primary collaborator:** ChatGPT

## Boundary

Checkpoint 292 established the key whole-PDF behavior:

```text
embedded MCP PDF -> ChatGPT file materialization       PASS
same-turn native PDF access                            FAIL
next-turn full PDF inspection                          PASS
representative inline base64 tool-result transport     FAIL AS TESTED
```

The next smallest transport substitution is now qualified:

```text
authorized local PDF
    -> existing DocumentFileReader authority/provenance
    -> server-owned ephemeral resource
    -> small MCP resource_link tool result
    -> separate resources/read PDF blob
    -> ChatGPT host materialization experiment
```

Target public surface:

```text
version        0.1.1-preview.13
surface        codexless-public-preview-v2
tool count     56
new action     codex.document_file_link
```

The existing `codex.document_file_read` embedded-resource experiment remains preserved for direct A/B evidence.

## Qualification

```text
DOCUMENT_RESOURCE_LINK_REGRESSION=PASS tests=8
DOCUMENT_FILE_READ_REGRESSION=PASS tests=5
BOUNDED_GIT_FETCH_ORIGIN=PASS tools=56
BOUNDED_GIT_PULL_FF_ONLY=PASS tools=56
PUBLIC_SURFACE_REGISTRATION=PASS tools=56
IMAGE_READ_REGRESSION=PASS tests=7
DOCUMENT_RENDER_REGRESSION=PASS tests=10
DOCUMENT_RESOURCE_LINK_PUBLICATION_PREFLIGHT=PASS
TOOL_RESULT_EMBEDS_PDF_BYTES=false
BROWSER_REQUIRED=false
NEW_EXTERNAL_DEPENDENCY=false
PAUSED_LOOPBACK_RENDER_TRANSPORT_OVERLAID=false
NO_LIVE_FILES_MODIFIED=true
```

## Exact continuation

```text
1. preserve Checkpoint 293 / Validation 052 in public authority;
2. run `.ads-private/codexless/activate-document-resource-link-publication.ps1 -Publish` from ordinary PowerShell and approve only its exact ShouldProcess target;
3. verify DOCUMENT_RESOURCE_LINK_PUBLICATION_RESULT=PASS, PAUSED_LOOPBACK_RENDER_TRANSPORT_MODIFIED=false and RESTART_PERFORMED=false;
4. do not restart until the publication output is reviewed;
5. then follow docs/local_execution/OPERATIONS.md controlled restart order;
6. verify preview.13 / v2 / 56 tools and existing document/image/render smokes;
7. refresh the ChatGPT developer-MCP app schema;
8. fresh disposable chat: call only codex.document_file_link on the tiny probe.pdf and determine whether the host follows resources/read/materializes the PDF;
9. if tiny PASS, test CheatSheet_A4.pdf and require no maximum-chat-length failure plus next-turn full-PDF inspection;
10. if resource-link handling fails or remains materially inferior, move next to the already-existing ADS Browser upload route; keep Checkpoint 289 loopback renderer unpublished until the whole-PDF routes are resolved.
```

Primary evidence:

```text
docs/local_execution/validation/052_mcp_pdf_resource_link_publication_preflight_qualified.md
docs/local_execution/validation/051_mcp_pdf_resource_materializes_attachment_but_not_same_turn_native_pdf.md
docs/research/117_reuse_first_multimodal_document_architecture_and_local_media_handoff.md
```
