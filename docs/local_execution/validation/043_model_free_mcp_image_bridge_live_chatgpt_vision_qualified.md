# Validation 043: Model-Free MCP Image Bridge Live ChatGPT Vision Qualified

**Date:** 2026-09-04
**Status:** PASS / LIVE CHATGPT HOST VISION QUALIFIED
**Research:** Research 117
**Experiment:** E117-1
**Workspace:** `ads-public`
**Target:** `frontend/e2e/visual.spec.ts-snapshots/overview-light-chromium-linux.png`

## Purpose

Close the exact host question left open by Research 117 and Validation 042:

```text
authorized local image
    -> codex.image_read
    -> standard MCP image content
    -> ChatGPT developer-MCP host
    -> ChatGPT model vision
```

The discriminating requirement was a fresh disposable ChatGPT conversation that used `codex.image_read` as the only substantive ADS/Codex route and reported visual-only facts that were not supplied in the prompt or metadata.

## Live publication and runtime verification

The guarded host publication completed successfully before this experiment. After the controlled Codexless/tunnel restart and ChatGPT developer-MCP refresh, a model-free local health check on 2026-09-04 returned:

```text
ok              true
service         codexless-public
transport       streamable-http
version         0.1.1-preview.10
surfaceVersion  codexless-public-preview-v2
toolCount       53
defaultCwd      C:\Projects_Data\autonomous-data-science-system
```

The tunnel was independently checked at the same live boundary:

```text
http://127.0.0.1:8080/healthz   HTTP 200 / live
http://127.0.0.1:8080/readyz    HTTP 200 / ready
```

The refreshed ChatGPT projection exposes both `codex.image_read` and the preserved `codex.document_read` action. No Browser repair was needed for E117-1.

## Fresh disposable ChatGPT experiment

The fresh disposable conversation was instructed to call only:

```text
codex.image_read

cwd:
C:\Projects_Data\autonomous-data-science-system

imagePath:
frontend/e2e/visual.spec.ts-snapshots/overview-light-chromium-linux.png
```

It was explicitly forbidden from using a Codex agent/model turn, `codex.document_read`, Browser, OCR, shell/command execution, repository reads, web search, filename inference, metadata inference, or prior knowledge to determine the visual content.

The prompt did **not** provide the expected visual facts.

The fresh conversation reported that it received actual visual image content and could inspect pixels rather than only metadata/text. It then reported concrete visual facts including:

```text
light-themed "Customer Churn Prediction" dashboard
right-side "What matters now" panel
pale-orange "APPROVAL REQUIRED" card
"Missingness pattern investigation"
"Approve & run" and "Reject" buttons
"Runs & activity" states including
    "WAITING FOR APPROVAL"
    "COMPLETED"
    "RUNNING"
```

It classified:

```text
MCP_IMAGE_TO_CHATGPT_VISION=PASS
```

## Independent cross-check

Validation 041 had already inspected the same PNG through Codex's separate native `view_image` path and independently identified the `Customer Churn Prediction` dashboard plus the right-side `Approval required` panel.

The fresh E117-1 facts therefore agree with previously preserved independent visual evidence while adding further pixel-level details that were not supplied in the test prompt.

This materially reduces the possibility that the PASS arose from metadata-only exposure.

## Result

```text
LIVE_CODEXLESS_VERSION                 0.1.1-preview.10
LIVE_PUBLIC_SURFACE                    codexless-public-preview-v2
LIVE_PUBLIC_TOOL_COUNT                 53
TUNNEL_LIVENESS                        PASS
TUNNEL_READINESS                       PASS
CODEX_IMAGE_READ_PROJECTED             PASS
CODEX_DOCUMENT_READ_PRESERVED          PASS
ACTUAL_MCP_IMAGE_CONTENT_TO_CHATGPT    PASS
VISUAL_ONLY_FACT_RECOVERY              PASS
EXTRA_CODEX_MODEL_TURN_REQUIRED        false
BROWSER_REQUIRED                       false
OCR_REQUIRED                           false
CUSTOM_IMAGE_UNDERSTANDING_REQUIRED    false
MCP_IMAGE_TO_CHATGPT_VISION             PASS
```

## Architectural interpretation

Research 117 now has two separately qualified local-image vision routes:

```text
E117-3
authorized local image
    -> Codex native view_image
    -> Codex model vision
    -> PASS

E117-1
authorized local image
    -> Codexless model-free codex.image_read
    -> standard MCP image content
    -> ChatGPT host/model vision
    -> PASS
```

The second route is especially important because the image handoff itself starts no Codex model turn. ADS therefore does not need to pay for a separate Codex reasoning turn merely to make an already-authorized image visually available to ChatGPT.

The remaining multimodal document problem is narrower:

```text
document bytes
    -> safe/reusable page or visual representation
    -> already-qualified native image vision route
```

rather than:

```text
document bytes
    -> custom ADS image-understanding stack
```

## Scope limits

This validation establishes the exact tested ChatGPT developer-MCP path for an authorized local PNG returned by `codex.image_read`.

It does not by itself establish:

```text
all MCP hosts expose image content identically
PDF page rendering/conversion is solved
DOCX/PPTX/XLSX visual conversion is solved
scanned-document OCR is solved
native whole-PDF file-input transport from an authorized local path is solved
```

Those remain separate Research 117 questions.

## Qualification result

```text
MODEL_FREE_MCP_IMAGE_BRIDGE=LIVE_QUALIFIED
MCP_IMAGE_TO_CHATGPT_VISION=PASS
RESEARCH_117_E117_1=PASS
```
