# Checkpoint 329: Non-PDF Office Handoff Reuse-First Research Opened

**Date:** 2026-09-06
**Status:** RESEARCH 121 OPEN / GENERIC FILE-LINK CANDIDATE NEXT
**Checkpoint class:** LOCAL EXECUTION / DIRECT CHATGPT FILE ACCESS
**Project stage:** AB-005 non-PDF file capability matrix
**Scope:** Opens the next reuse-first direct-file work after Research 120 closes, grounded in current OpenAI file-upload support, generic MCP resource-link semantics and the existing PDF resource lifecycle's reusable authority/binding machinery.
**Authority:** Research 121 owns the architecture; Validation 087 preserves the evidence baseline.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-19`
**Conversation title:** `19 - Hybrid PDF Intent Matrix and Isolation Qualification`
**Primary collaborator:** ChatGPT

Current official evidence establishes that DOCX, PPTX and XLSX are supported ordinary ChatGPT upload types and that MCP resource links are MIME-generic. Local source inspection establishes that the existing PDF-only whole-file path is transport-generic except for its PDF media validation.

The accepted next move is therefore not to build three new parsers. It is to reuse the proven resource lifecycle in one narrow `codex.file_link` candidate, allowlist the three OOXML MIME types, then qualify tiny deterministic files through a fresh ChatGPT host and measure materialization, structure/text/data access and visual fidelity separately.

Only formats that fail or lose material information should receive a model-free fallback later.

```text
CHECKPOINT_329 = NON_PDF_OFFICE_HANDOFF_REUSE_FIRST_RESEARCH_OPENED
```
