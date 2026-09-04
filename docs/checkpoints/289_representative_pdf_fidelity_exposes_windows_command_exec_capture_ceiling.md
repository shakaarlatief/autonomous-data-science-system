# Checkpoint 289: Representative PDF Fidelity Exposes Windows Command/Exec Capture Ceiling

**Date:** 2026-09-04
**Status:** REPRESENTATIVE GAP LOCALIZED / TRANSPORT CORRECTION OPEN
**Checkpoint class:** EXPERIMENT_VERIFICATION
**Project stage:** Research 117 reuse-first multimodal document architecture
**Scope:** Preserves the first representative PDF fidelity matrix after live `codex.document_render` qualification and localizes a Windows App Server buffered `command/exec` capture ceiling that blocks image-heavy pages below the semantic 4 MiB PNG limit.
**Authority:** Validation 048 is primary evidence. Checkpoint 288 remains valid for its exact simple/ordinary page claim. This checkpoint does not authorize a new runtime publication or broaden workspace authority.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-17`
**Conversation title:** `17 - MCP Image Bridge Publication Recovery and Multimodal Document Continuation`
**Primary collaborator:** ChatGPT

## Boundary

Representative real-document testing began immediately after Checkpoint 288.

Ordinary mathematical/text pages passed. A dense full-width cheat-sheet page exceeding the semantic 4 MiB PNG ceiling failed closed correctly with `DOCUMENT_RENDER_IMAGE_SIZE_LIMIT`.

More importantly, multiple real pages whose PNGs were between roughly 1.16 and 1.23 MiB failed with `DOCUMENT_RENDER_PROTOCOL_ERROR / invalid JSON` even though they were below the 4 MiB page limit. Direct maintained PDF.js + canvas probes successfully rendered those same pages.

The affected examples include an image-only cheat sheet, a scanned/handwritten page, and another dense theory sheet. A 425 KiB PNG ordinary assignment page succeeds, while representative pages whose previous base64 stdout payload would exceed one MiB fail.

## Root cause

Current official Codex App Server documentation defines buffered `command/exec` output with a default 1 MiB per-stream capture ceiling. Current upstream Windows restricted-token implementation requires that default cap and does not support custom `outputBytesCap` or streamed `command/exec` in that sandbox.

The preview.11 candidate mistakenly treated a larger local post-response truncation allowance as though it enlarged the upstream App Server capture. It does not. The test fake did not reproduce that Windows upstream constraint.

Therefore:

```text
renderer fidelity on sampled failing pages     not disproven
semantic 4 MiB PNG guard                       working
buffered stdout as binary-page transport       inadequate on Windows
Checkpoint 288 simple-case qualification       preserved
representative PDF qualification               incomplete
```

## Experimental correction candidate

The ignored local candidate now explores a bounded parent-owned loopback binary transport. The renderer remains inside `:read-only`; stdout carries only compact control JSON; page bytes use a random parent-generated 256-bit token, ephemeral `127.0.0.1` destination, bounded packet/header limits, and parent-side hash/signature/dimension validation.

Focused candidate unit regression currently passes:

```text
DOCUMENT_RENDER_REGRESSION=PASS tests=10
```

This candidate is not live-qualified. The first nested staging harness could not bootstrap another runtime provider from inside the already-sandboxed outer command because user-local runtime preference access was denied. That result does not prove or disprove the actual cross-boundary loopback transfer.

## Exact continuation

```text
1. keep the live preview.11 / 54-tool runtime unchanged;
2. preserve Checkpoint 288 as simple-case PASS and Checkpoint 289 as representative transport-gap boundary;
3. qualify or reject the authenticated parent-owned loopback channel across the actual Windows :read-only sandbox;
4. do not use unsandboxed process/spawn for untrusted PDF parsing;
5. do not lower DPI merely to fit buffered stdout;
6. if loopback passes, rerun the same image-only and scanned pages;
7. only after transport succeeds evaluate OCR/fidelity gaps and decide whether any fallback stack is justified.
```

The broader `%LOCALAPPDATA%` authority architecture remains separate under AB-002 / AB-017.

Primary evidence:

```text
docs/local_execution/validation/048_representative_pdf_fidelity_exposes_windows_command_exec_capture_ceiling.md
docs/local_execution/validation/047_document_render_live_chatgpt_vision_qualified.md
docs/checkpoints/288_document_render_live_chatgpt_vision_qualified.md
docs/research/117_reuse_first_multimodal_document_architecture_and_local_media_handoff.md
```
