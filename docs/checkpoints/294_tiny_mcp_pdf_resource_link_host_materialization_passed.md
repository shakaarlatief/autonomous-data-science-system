# Checkpoint 294: Tiny MCP PDF Resource-Link Host Materialization Passed

**Date:** 2026-09-04
**Status:** LIVE HOST PASS / REPRESENTATIVE PDF TEST NEXT
**Checkpoint class:** EXPERIMENT_VERIFICATION
**Project stage:** Research 117 reuse-first multimodal document architecture
**Scope:** Preserves live ChatGPT host qualification that `codex.document_file_link` can materialize a tiny local PDF as a conversation file without embedding the PDF bytes in the original tool-result envelope.
**Authority:** Validation 053 is primary evidence.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-17`
**Conversation title:** `17 - MCP Image Bridge Publication Recovery and Multimodal Document Continuation`
**Primary collaborator:** ChatGPT

## Boundary

Preview.13 / v2 / 56 is live and tunnel health/readiness are both HTTP 200. Preserved `document_read` and `document_render` smokes passed after restart. Fresh disposable ChatGPT then called only `codex.document_file_link` on `probe.pdf`.

Accepted result:

```text
resource_link tool call succeeds                         PASS
tool-result PDF base64 absent                            PASS
host PDF file materialization                            PASS
same-turn PDF content access                             FAIL / expected from prior host behavior
explicit resources/read trace                            not surfaced
MCP_PDF_RESOURCE_LINK_MATERIALIZATION                    PASS
```

## Exact continuation

```text
1. keep preview.13 / 56 live and do not change the candidate;
2. fresh disposable ChatGPT chat;
3. invoke only codex.document_file_link on the representative CheatSheet_A4.pdf in big-data-statistics;
4. require no maximum-chat-length failure and no inline PDF bytes in the original tool result;
5. verify host attachment/file materialization;
6. if materialized, send a second ordinary user turn asking ChatGPT to inspect the complete PDF without another ADS call;
7. if next-turn complete-PDF inspection passes, qualify resource_link as the preferred whole-PDF transport and test the scanned representative PDF next;
8. if representative resource_link fails, move to the ADS Browser upload route before returning to the paused loopback renderer transport.
```
