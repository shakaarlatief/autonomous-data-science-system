# Validation 041: Codex Native Local Image View Qualified

**Date:** 2026-09-03
**Status:** PASS / NATIVE LOCAL IMAGE VISION QUALIFIED
**Research:** Research 117
**Workspace:** `ads-public`
**Target:** `frontend/e2e/visual.spec.ts-snapshots/overview-light-chromium-linux.png`

## Purpose

Test whether the current installed Codex runtime can inspect an already-authorized local image through its maintained native image path, without ADS implementing a custom image reader, renderer, OCR path, file copy, or conversion step.

## Experiment

A bounded read-only Codex turn used GPT-5.6 Sol with medium reasoning and explicitly required the maintained native `view_image` / local-image capability.

Codex task identity:

```text
shortTaskId  C-98FDD36322
threadId     01a068f4-3169-7fe0-918e-93d4547e5be9
turnId       01a068f4-32e9-7871-b1f5-909ff9b9c943
```

## Result

Codex reported:

```text
native image attachment / inspection    PASS
visual-only understanding               PASS
intermediate file/render/copy required  NO
authority/sandbox blocker               NONE
```

The model inspected the screenshot through the maintained `view_image` path with original detail and identified a visual-only fact: the screenshot contains a `Customer Churn Prediction` dashboard with a right-side `Approval required` panel.

No OCR script, custom parser, image conversion, temporary copy, or intermediate renderer was required.

## Interpretation

This is important positive reuse evidence for Research 117. Current Codex already owns a working local-image-to-model-vision path under ADS's existing project authority. Therefore ADS should not build a separate image-understanding subsystem.

The remaining document problem is now narrower:

```text
PDF/document bytes
    -> safe page/image representation
    -> existing Codex/OpenAI native image input
```

rather than:

```text
PDF/document bytes
    -> ADS custom vision stack
```

Validation 040 showed that the maintained PDF Skill's local renderer dependency is not presently usable on this machine. Validation 041 proves that once an authorized image exists, native model vision works directly. This strongly favors solving or reusing only the rendering/handoff seam.

## Qualification result

```text
CODEX_NATIVE_LOCAL_IMAGE_VIEW=PASS
VISUAL_MODEL_INPUT=PASS
CUSTOM_IMAGE_UNDERSTANDING_REQUIRED=false
INTERMEDIATE_COPY_REQUIRED=false
NO_FILES_MODIFIED=true
```
