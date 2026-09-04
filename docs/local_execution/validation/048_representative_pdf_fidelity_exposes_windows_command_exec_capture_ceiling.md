# Validation 048: Representative PDF Fidelity Exposes Windows Command/Exec Capture Ceiling

**Date:** 2026-09-04
**Status:** PASS / REPRESENTATIVE GAP LOCALIZED / LIVE SIMPLE-CASE QUALIFICATION PRESERVED
**Research:** Research 117
**Experiment:** E117-5a
**Workspace:** `big-data-statistics` plus `ads-public`
**Live runtime:** `0.1.1-preview.11` / `codexless-public-preview-v2` / 54 tools

## Purpose

Begin representative PDF fidelity qualification immediately after Checkpoint 288 closed the simple two-page host-vision transport question. The goal was to test real authorized documents spanning mathematical notation, text-heavy pages, dense cheat sheets, and scanned/image-heavy material before adding OCR or broader document adapters.

## Representative observations

`BDS-exam-24-25-solutions.pdf`, page 1, passed both embedded-text extraction and page rendering. The rendered 1275 x 1651 PNG was 293,677 bytes and visibly preserved equations, Greek symbols, nested exponentials, fractions, summations and ordinary prose.

`Data-Assignment-24-25.pdf`, page 1, also passed. Its 1275 x 1651 PNG was 425,135 bytes, corresponding to roughly 566,848 base64 characters in the prior stdout transport.

`CheatSheet_A4_FullWidth.pdf`, page 1, directly rendered through the maintained PDF.js + canvas stack to 5167 x 7309 and 6,900,744 PNG bytes. Public `codex.document_render` correctly failed closed with `DOCUMENT_RENDER_IMAGE_SIZE_LIMIT` because this exceeds the accepted 4 MiB per-page semantic ceiling. That is intentional safety-bound behavior.

Three representative pages below the 4 MiB PNG ceiling exposed a different failure:

```text
CheatSheet_A4.pdf page 1
    document_read text        empty
    direct render             5167 x 7309
    PNG bytes                 1,208,281
    base64 chars              1,611,044
    document_render           DOCUMENT_RENDER_PROTOCOL_ERROR / invalid JSON

Adobe Scan BDS_Exercises_Misha.pdf page 1
    document_read             sparse/noisy embedded text layer
    direct render             1240 x 1753
    PNG bytes                 1,233,793
    base64 chars              1,645,060
    document_render           DOCUMENT_RENDER_PROTOCOL_ERROR / invalid JSON

theorieSheet.pdf page 1
    direct render             1651 x 1275
    PNG bytes                 1,160,847
    base64 chars              1,547,796
    document_render           DOCUMENT_RENDER_PROTOCOL_ERROR / invalid JSON
```

The pattern is discriminating: pages whose sandboxed renderer JSON remains comfortably below approximately one MiB succeed, while pages requiring more than one MiB of stdout capture fail as truncated/invalid JSON even when the PNG itself remains below the semantic 4 MiB ceiling.

## Root cause

Current official Codex App Server documentation defines buffered `command/exec` stdout/stderr capture with a default 1 MiB per-stream cap. Current upstream source additionally states that the Windows restricted-token sandbox does not support custom `outputBytesCap` or streaming `command/exec`; Windows buffered sandbox execution requires the default output cap.

Primary upstream sources:

```text
https://github.com/openai/codex/blob/main/codex-rs/app-server/README.md
https://github.com/openai/codex/blob/main/codex-rs/app-server/src/command_exec.rs
https://github.com/openai/codex/blob/main/codex-rs/app-server-protocol/src/protocol/v2/command_exec.rs
```

Inspection of the preview.11 candidate found a local design mistake: `DocumentRenderer` requested an internal 11,750,000-byte ceiling from `CodexAuthorityExecutor.exec`, but `CodexAuthorityExecutor.exec` did not forward that value into `CodexAppServerClient.exec`. It only applied a larger truncation allowance after the App Server response had already been captured. The regression suite used a fake executor and therefore did not reproduce the real Windows App Server 1 MiB capture ceiling.

This explains why Checkpoint 288's smaller synthetic pages passed while representative image-heavy pages expose invalid JSON.

## Claim correction

Checkpoint 288 remains valid for its exact tested claim:

```text
bounded ordinary PDF pages
    -> read-only sandboxed PDF.js + canvas render
    -> standard MCP image content
    -> ChatGPT native vision
    -> PASS
```

Validation 048 narrows coverage:

```text
simple/ordinary page transport                         QUALIFIED
representative high-detail page transport              NOT YET QUALIFIED
4 MiB semantic page ceiling enforcement                WORKING / FAIL-CLOSED
>1 MiB buffered Windows command/exec payload transport UNSUITABLE
```

No claim is made that PDF.js/canvas fidelity itself failed on the image-only/scanned samples. Direct maintained-render probes successfully created the PNGs. The failing layer is sandbox-to-parent byte transport through buffered `command/exec` stdout.

## Candidate correction under investigation

A private ignored candidate has been changed experimentally so page PNG bytes are no longer base64-embedded in buffered stdout. Instead, the sandboxed renderer keeps stdout as compact control JSON and sends a bounded authenticated binary packet to an ephemeral parent-owned `127.0.0.1` listener:

```text
sandboxed PDF.js + canvas child
    -> compact stdout control receipt under App Server cap
    -> random 256-bit parent-generated transfer token
    -> ephemeral loopback-only binary channel
    -> bounded header + maximum 8 MiB aggregate PNG bytes
    -> parent hash/signature/dimension validation
```

The candidate exposes no caller-selected port/token/network destination and keeps external network blocked by the existing read-only sandbox. Unit regression for this candidate transport currently passes:

```text
DOCUMENT_RENDER_REGRESSION=PASS tests=10
```

This candidate is **not live-qualified and must not be published yet**. A first nested staging attempt could not instantiate another Codex runtime provider from inside the outer read-only sandbox because access to the user-local runtime-install preference was denied. That is a staging-harness limitation, not evidence that the loopback transport itself works across the real Codex Windows sandbox boundary.

## Result

```text
REPRESENTATIVE_MATH_PAGE_RENDER            PASS
REPRESENTATIVE_TEXT_PAGE_RENDER            PASS
DENSE_PAGE_SEMANTIC_SIZE_GUARD             PASS / FAIL-CLOSED
IMAGE_ONLY_PAGE_WITHIN_4_MIB               TRANSPORT FAIL
SCANNED_PAGE_WITHIN_4_MIB                  TRANSPORT FAIL
WINDOWS_COMMAND_EXEC_1_MIB_ROOT_CAUSE      LOCALIZED
CHECKPOINT_288_SIMPLE_CASE                 PRESERVED
REPRESENTATIVE_PDF_FIDELITY                INCOMPLETE
OCR_REQUIRED                               NOT ESTABLISHED
THIRD_PARTY_FALLBACK_REQUIRED              NOT ESTABLISHED
LOOPBACK_BINARY_CANDIDATE                  UNIT-QUALIFIED ONLY
LIVE_PUBLICATION                           NOT AUTHORIZED / NOT ATTEMPTED
```

## Exact next step

Research 117 should qualify the smallest supported sandbox-to-parent binary transport before any renderer or OCR replacement. Do not widen workspace authority, use unsandboxed `process/spawn` for untrusted PDF parsing, or lower DPI merely to hide the transport defect. First prove whether the parent-owned authenticated loopback channel works across the actual Windows `:read-only` sandbox; if it does, rerun the same image-only/scanned representative pages before making any OCR or fallback-stack decision.
