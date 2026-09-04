# Validation 051: MCP PDF Resource Materializes Attachment but Not Same-Turn Native PDF

**Date:** 2026-09-04
**Status:** LIVE HOST RESULT / DIRECT SAME-TURN NATIVE PDF PROMOTION FAILED / ATTACHMENT MATERIALIZATION OBSERVED
**Research:** Research 117
**Experiment:** E117-5d
**Live surface:** `0.1.1-preview.12` / `codexless-public-preview-v2` / 55 tools

## Purpose

Test the live `codex.document_file_read` path after guarded publication, controlled restart, and ChatGPT app refresh. Separate three questions that had previously been conflated:

```text
1. can ADS return exact local PDF bytes as standard MCP PDF resource content?
2. does the ChatGPT host materialize that resource as a file/attachment artifact?
3. does the same model turn receive native parsed/visual PDF input automatically?
```

## Large representative-file observation

The first test used `CheatSheet_A4.pdf` (1,679,081 raw bytes). Its inline base64 MCP resource payload is approximately 2.24 million characters before surrounding protocol/context overhead. Multiple fresh chats returned a misleading `maximum chat length is reached` UI error for that prompt while ordinary messages in the same chats still worked immediately afterward.

This is evidence that the conversation itself was not exhausted. The failure is consistent with the representative inline embedded-resource payload exceeding a host/tool-result/context envelope, but the exact host ceiling is not established.

Classification:

```text
representative inline embedded-PDF transport     NOT VIABLE AS TESTED
native PDF promotion for that request             UNDETERMINED
conversation-length exhaustion                    NOT SUPPORTED BY OBSERVATION
```

## Tiny discriminating PDF test

The experiment was repeated in a fresh disposable ChatGPT conversation against the 2,372-byte two-page `probe.pdf`:

```text
cwd          C:\Projects_Data\autonomous-data-science-system
documentPath docs/local_execution/validation/generated/e117_managed_poppler_probe/probe.pdf
```

Only `codex.document_file_read` was permitted.

The live host reported:

```text
codex.document_file_read                          SUCCEEDED
MCP metadata                                      AVAILABLE
application/pdf resource                          RETURNED
host file/attachment materialization              OBSERVED
parsed PDF contents in same model context         NOT AVAILABLE
rendered/native visual representation             NOT AVAILABLE
independent PDF content/layout facts               NOT POSSIBLE
```

The ChatGPT UI visibly showed a `probe.pdf` PDF attachment card associated with the tool result. This is important positive evidence: the MCP PDF resource was not merely discarded or rendered as opaque text. The host materialized a file-like conversation artifact.

However, the same assistant turn explicitly could not inspect the PDF contents or visual layout and correctly classified:

```text
MCP_PDF_RESOURCE_TO_CHATGPT_NATIVE_PDF=FAIL
```

## Correct claim scope

This result rejects the strongest one-step architecture assumption:

```text
ADS local PDF
    -> MCP embedded PDF resource
    -> automatic same-turn native PDF model input
    -> first-party PDF understanding
```

That path does not occur automatically in the exact tested ChatGPT developer-MCP host.

It does **not** yet reject a two-stage first-party reuse path because the host visibly materialized the PDF as an attachment/file artifact. The next highest-value experiment is therefore:

```text
turn N
    ADS codex.document_file_read
    -> host materializes probe.pdf attachment

turn N+1, same conversation
    invoke @PDF / first-party PDF Skill on the materialized probe.pdf attachment
    -> determine whether the Skill can now inspect the actual PDF
```

This experiment requires no ADS code change, no restart, no schema refresh, and no renderer/loopback publication.

If that passes, the architecture question becomes how to materialize representative PDFs without multi-megabyte inline base64. A server-owned MCP `resource_link` + bounded resource-read route is then a stronger candidate than returning the full binary inline. If the first-party PDF Skill cannot consume the materialized attachment in the next turn, the attachment artifact is only UI-level/file-output behavior and does not solve Research 117.

## Current result

```text
LIVE_PREVIEW_12                               PASS
CODEx_DOCUMENT_FILE_READ                     PASS
TINY_INLINE_MCP_PDF_RESOURCE                 PASS
HOST_PDF_ATTACHMENT_MATERIALIZATION          PASS
SAME_TURN_NATIVE_PDF_MODEL_PROMOTION         FAIL
REPRESENTATIVE_INLINE_BASE64_ROUTE            FAIL / SIZE-SENSITIVE HOST LIMIT LIKELY
NEXT                                          same-chat @PDF consumption of materialized probe.pdf attachment
LOOPBACK_RENDER_TRANSPORT                     REMAINS PAUSED
```
