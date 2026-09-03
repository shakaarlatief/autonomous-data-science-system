# Validation 040: Codex PDF Skill Visual-Read Reuse Experiment

**Date:** 2026-09-03
**Status:** PARTIAL PASS / VISUAL RENDER BLOCKED BY LOCAL DEPENDENCY
**Research:** Research 117
**Workspace:** `big-data-statistics`
**Target:** `BDS-exam-24-25-solutions.pdf`, page 1 only

## Purpose

Test whether the maintained OpenAI Codex PDF Skill can replace a custom ADS `document_render` path for visual inspection of an already authorized local PDF.

## Authority change

The workspace registry was intentionally widened only from:

```text
read
```

to:

```text
read
agent
```

No `write`, `browser`, or Git capability was added. Registry revision advanced from `3` to `4`; content hash became `2960f0b113550301a692470b0f2ff527317812550b6d3ae7cd2e519c94ad9e80`.

## Experiment

A bounded Codex turn used GPT-5.6 Sol with medium reasoning. The task required the maintained OpenAI PDF Skill, page 1 only, no file modification, and an explicit report of whether visual rendering actually occurred.

Codex task identity:

```text
shortTaskId  C-7F17A2A8B7
threadId     01a068e9-0d78-7222-a543-3d678a9842d4
turnId       01a068e9-0ebd-7fd0-a62e-3add8204eb60
```

## Result

```text
PDF Skill routed/used             PASS
rendered page visually inspected  FAIL / NOT COMPLETED
files modified                    NO
```

Codex reported that the maintained PDF Skill was loaded and followed, but visual inspection did not complete. The blocker was local rendering infrastructure: the available Poppler command resolved to an uninitialized MiKTeX stub and no alternative PDF-rendering backend was available under the bounded read-only task. Completing MiKTeX setup, installing a renderer, or writing an intermediate image would have exceeded the experiment's no-modification constraint.

Therefore no visual/layout fact was claimed.

## Interpretation

This is useful negative evidence. The installed PDF Skill is real and routable, but its current local visual path is not self-sufficient on this machine. The failure does **not** establish that a custom ADS renderer is required. It establishes only that the current maintained Skill's renderer dependency is not presently usable in this environment under the tested constraints.

Research 117 should continue with reuse-first alternatives before custom implementation:

```text
1. exact App Server/localImage semantics
2. standard MCP image-result visibility in ChatGPT
3. native OpenAI PDF file-input handoff from an authorized local file
4. maintained renderer/runtime dependency resolution if it can remain upstream-owned
5. third-party render/conversion fallback only if needed
```

## Qualification result

```text
CODEX_PDF_SKILL_ROUTE=PASS
CODEX_PDF_VISUAL_RENDER=BLOCKED_LOCAL_DEPENDENCY
NO_FILES_MODIFIED=true
CUSTOM_DOCUMENT_RENDER_JUSTIFICATION=NOT_ESTABLISHED
```
