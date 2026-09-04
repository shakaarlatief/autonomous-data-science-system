# Validation 049: Official PDF Skill Local ADS Handoff Research Prioritized

**Date:** 2026-09-04
**Status:** PASS / REUSE-FIRST ROUTE REPRIORITIZED / IMPLEMENTATION NOT YET AUTHORIZED
**Research:** Research 117
**Experiment:** E117-5b

## Purpose

Re-evaluate Checkpoint 289 after the project owner surfaced the first-party ChatGPT PDF plugin/skill. Determine whether ADS can hand an already-authorized local Windows PDF into standard MCP file/resource semantics that ChatGPT may promote into the first-party PDF capability, instead of continuing custom page-image transport work prematurely.

## Mobile/tunnel clarification

The earlier `tunnel_active_organization_required` result occurred while the user had messaged from the phone. That device/context behavior is already a separate deferred architecture topic and is not evidence that enabling the PDF plugin caused an ADS/plugin conflict. No causal link is accepted.

## First-party PDF capability

The ChatGPT PDF plugin router identifies the capability as a Skill and points Chat to `/home/oai/skills/pdfs/SKILL.md` as its fallback. That skill was read directly and provides render-first PDF review plus extraction, OCR, preflight, editing, renderer comparison, conversion and verification.

The installed Codex primary runtime separately exposes the maintained `pdf:pdf` Skill for local-machine PDFs. OpenAI therefore already maintains PDF-specific workflows on both Chat and Codex sides.

## Local-file seam

The Chat PDF Skill does not itself have arbitrary access to a Windows path. ADS already owns the missing local authority side:

```text
registered Windows workspace
    -> Codexless read authority
    -> canonical containment
    -> exact local PDF bytes
```

The unresolved question is whether those authorized bytes can be returned through standard MCP file/resource semantics and then treated by the ChatGPT host as a genuine PDF/file input for the first-party PDF capability.

## MCP protocol evidence

The exact installed MCP SDK used by live Codexless was inspected. Its current `CallToolResultSchema` accepts both:

```text
EmbeddedResource
    type: resource
    resource: { uri, mimeType, blob|text }

ResourceLink
    type: resource_link
    uri, name, mimeType, optional size/metadata
```

A model-free local schema probe validated both an embedded `application/pdf` blob and an `application/pdf` resource link as legal tool-result content.

This proves protocol feasibility only. It does not prove ChatGPT promotes an MCP-returned PDF into the same native file-input path used for user attachments.

## OpenAI documentation evidence

Current OpenAI documentation confirms that ChatGPT custom apps are MCP-based, Responses supports native `input_file` content, and app/file-output documentation recognizes file references and MCP `resource_link` outputs. It does not clearly document the exact inbound promotion we need:

```text
MCP tool returns application/pdf resource/blob
    -> ChatGPT native PDF/file input
    -> first-party PDF Skill / model processing
```

That exact host behavior remains an empirical question.

## Existing Browser upload fallback

ADS already exposes an authority-bounded local-file Browser upload path. `codex.browser_prepare_upload` binds canonical path, byte length and SHA-256, and `codex.browser_upload` uses Chrome's official filechooser/setFiles flow.

This is a useful fallback/diagnostic, not the preferred document architecture, because it depends on ChatGPT web UI state and effectively automates manual upload.

## Reuse-first decision

Checkpoint 289's authenticated loopback page-image transport candidate is paused before publication. The next preferred experiment is smaller:

```text
authorized local PDF
    -> thin ADS bounded file reader
    -> standard MCP PDF resource/file content
    -> ChatGPT host
    -> native PDF/file interpretation if supported
    -> first-party PDF capability
```

The ADS side should own only authority/provenance, not PDF interpretation.

## Required host experiment

The candidate must require existing workspace read authority, accept one bounded workspace-relative PDF, reject traversal/symlink escape, cap bytes, hash the source, perform no model turn/Browser/OCR/render/write/Git/external API call, and return standard MCP `application/pdf` content. Embedded resource should be tested first; `resource_link` should be tested only if host behavior requires it.

Fresh disposable ChatGPT qualification must distinguish actual PDF/file ingestion from metadata/base64 exposure and then test the same difficult PDFs that exposed Checkpoint 289's render-transport ceiling.

## Result

```text
FIRST_PARTY_CHAT_PDF_SKILL                 PRESENT
FIRST_PARTY_CODEX_PDF_SKILL                PRESENT
ADS_LOCAL_WINDOWS_FILE_AUTHORITY           PRESENT
MCP_EMBEDDED_PDF_RESOURCE_SCHEMA           SUPPORTED
MCP_PDF_RESOURCE_LINK_SCHEMA               SUPPORTED
CHATGPT_MCP_PDF_TO_NATIVE_FILE_PROMOTION   UNPROVEN
BROWSER_LOCAL_FILE_UPLOAD_FALLBACK         AVAILABLE
LOOPBACK_RENDER_TRANSPORT_PUBLICATION       PAUSED
NEXT                                        bounded PDF-resource handoff host experiment
```
