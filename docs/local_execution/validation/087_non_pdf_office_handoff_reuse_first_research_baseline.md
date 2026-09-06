# Validation 087: Non-PDF Office Handoff Reuse-First Research Baseline

**Date:** 2026-09-06
**Status:** PASS / REUSE-FIRST ARCHITECTURE BASELINE ESTABLISHED / GENERIC FILE-LINK CANDIDATE NEXT
**Research:** Research 121
**Scope:** Preserve the official OpenAI/MCP evidence and local implementation inspection that determine the next direct-file-access experiment after Research 120 closes.

## Evidence summary

Current OpenAI documentation explicitly supports DOCX, PPTX and XLSX as ordinary ChatGPT file-upload types. The File Uploads FAQ establishes a broad manual-upload product capability and limits, but those limits are not transferred to MCP resource links by assumption. Enterprise guidance further suggests that DOCX/PPTX are commonly text-retrieval inputs and XLSX commonly receives spreadsheet/code analysis, so materialization and multimodal fidelity must be tested separately.

The maintained MCP protocol makes `resource_link` MIME-generic and allows binary resource bytes to be resolved by `resources/read`. Local implementation inspection shows that the current PDF resource path already owns authority binding, canonical containment, size/hash/identity checks, expiring opaque resources and no-inline-byte transport. The PDF restriction is confined to the reader/store media validation.

## Accepted next experiment

Build a private, allowlisted `codex.file_link` candidate for DOCX/PPTX/XLSX by reusing the current resource lifecycle rather than building parsers first. Then use tiny deterministic OOXML fixtures in a fresh host to measure:

```text
materialization
text/data/structure access
visual/layout access
format-specific need for fallback
```

No Office parser, renderer or conversion pipeline is accepted merely from this research baseline.

## Primary sources

```text
https://help.openai.com/en/articles/8983675-what-types-of-files-are-supported
https://help.openai.com/en/articles/8555545-file-uploads-faq
https://help.openai.com/en/articles/10029836
https://modelcontextprotocol.io/specification/2025-11-25/server/tools
https://modelcontextprotocol.io/specification/2025-11-25/server/resources
```

```text
OFFICE_HANDOFF_REUSE_FIRST_BASELINE=PASS
NEXT=GENERIC_FILE_LINK_PRIVATE_CANDIDATE
```
