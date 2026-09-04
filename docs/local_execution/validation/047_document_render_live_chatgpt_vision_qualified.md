# Validation 047: Document Render Live ChatGPT Vision Qualified

**Date:** 2026-09-04
**Status:** PASS / LIVE CHATGPT PAGE-VISION QUALIFIED
**Research:** Research 117
**Experiment:** E117-4d
**Workspace:** `ads-public`
**Live runtime:** `0.1.1-preview.11` / `codexless-public-preview-v2` / 54 tools

## Live infrastructure

Post-restart verification returned Codexless `0.1.1-preview.11`, surface `codexless-public-preview-v2`, 54 tools, expected ADS `defaultCwd`, tunnel `/healthz` HTTP 200 and `/readyz` HTTP 200.

The pre-existing `codex.document_read` smoke also passed after restart on `docs/local_execution/validation/generated/e117_sandbox_render_tiny.pdf`:

```text
embedded text      SANDBOX
parser             pdfjs-dist
parser version     5.4.624
selected pages     [1]
OCR performed      false
```

## Fresh disposable ChatGPT visual qualification

A fresh disposable ChatGPT conversation invoked only `codex.document_render` on the authorized two-page probe PDF. The prompt prohibited alternate document/image routes, Browser, OCR, shell commands, direct Poppler, Codex Agent/model turns, filename/repository inference, metadata inference, and prior-knowledge substitution.

The fresh conversation explicitly reported receiving actual rendered PNG content for both pages and directly inspecting the pixels. It reported visual-only facts not supplied in the prompt:

```text
page 1
    heading "MANAGED POPPLER PROBE"
    three stacked horizontal rectangles colored orange, green and light blue
    dark diagonal line sloping downward left-to-right

page 2
    heading "SECOND PAGE CHECK"
    five blue vertical bars increasing left-to-right
    "PAGE 2" beneath and to the right of the bars
```

Renderer metadata reported by the fresh conversation:

```text
engine            pdfjs-dist+@napi-rs/canvas
PDF.js version    5.6.205
canvas version    0.1.100
isolation         codex-command-exec-read-only
DPI               150
selected pages    [1, 2]
OCR performed     false
returned PNG      1275 x 1651 per page
```

Fresh-chat classification:

```text
MCP_DOCUMENT_RENDER_TO_CHATGPT_VISION=PASS
```

## Independent project-session reproduction

The continuing Chat 17 session independently rechecked current infrastructure and directly invoked `codex.document_render` on the same PDF. The live call returned the same renderer/isolation/version metadata, `warnings=[]`, two PNG images at 1275 x 1651, and no OCR. The MCP response included both actual images, and direct vision again confirmed the same headings, rectangles, diagonal line, increasing bars and page labels.

## Architectural result

The live-qualified path is now:

```text
workspace-authorized local PDF
    -> canonical read authority
    -> bounded source preflight
    -> Codex command/exec :read-only sandbox
    -> maintained primary-runtime pdfjs-dist + @napi-rs/canvas
    -> in-memory PNG page(s)
    -> validated standard MCP image content
    -> ChatGPT native vision
    -> PASS
```

No workspace image file, OCR, Browser, extra `codex.image_read` hop, external dependency, or Codex model turn is required for the tested PDF page-vision path.

## Result

```text
CODEXLESS_LIVE_VERSION                    0.1.1-preview.11
PUBLIC_TOOL_COUNT                         54
TUNNEL_HEALTH                             PASS
TUNNEL_READY                              PASS
DOCUMENT_READ_POST_RESTART                PASS
DOCUMENT_RENDER_PROJECTED                 PASS
DOCUMENT_RENDER_CALL                      PASS
ACTUAL_MCP_PAGE_IMAGES                    PASS
CHATGPT_VISUAL_PAGE_INSPECTION            PASS
READ_ONLY_RENDER_ISOLATION                PASS
OCR_REQUIRED                              false
BROWSER_REQUIRED                          false
CODEX_MODEL_TURN_REQUIRED                 false
WORKSPACE_WRITE_REQUIRED                  false
NEW_EXTERNAL_DEPENDENCY                   false
MCP_DOCUMENT_RENDER_TO_CHATGPT_VISION     PASS
```

## Scope limits and next step

This closes the semantic transport and host-vision question for the exact tested configuration. Representative fidelity for mathematical notation, annotations, complex tables, multi-column layouts, unusual embedded fonts, scanned/image-only PDFs, and large-document bounds remains open.

```text
RESEARCH_117_E117_4D=PASS
DOCUMENT_RENDER_LIVE=QUALIFIED
NEXT=representative PDF fidelity qualification before considering broader adapters or fallback stacks
```
