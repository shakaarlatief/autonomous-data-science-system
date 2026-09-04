# Checkpoint 285: Managed Primary Runtime Poppler Page Rendering Probe Qualified

**Date:** 2026-09-04
**Status:** REUSE PATH QUALIFIED / E117-4A PASS
**Checkpoint class:** EXPERIMENT_VERIFICATION
**Project stage:** Research 117 reuse-first multimodal document architecture
**Scope:** Preserves discovery and bounded end-to-end qualification of the maintained Codex primary-runtime Poppler PDF-to-PNG path feeding the already-qualified `codex.image_read` ChatGPT-vision route.
**Authority:** Historical experiment boundary. Validation 044 is the primary evidence; Research 117 governs continuing architecture interpretation and remaining representative-document qualification.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-17`
**Conversation title:** `17 - MCP Image Bridge Publication Recovery and Multimodal Document Continuation`
**Primary collaborator:** ChatGPT

## Boundary

Checkpoint 284 closed the direct MCP-image-to-ChatGPT-vision question. The next Research 117 question was whether ADS still lacked a maintained PDF renderer for producing the page images required by that now-qualified vision seam.

The answer is narrower than E117-2 originally suggested.

The installed OpenAI primary-runtime Skills document a managed dependency tree. Direct read-only inspection of that documented tree found Poppler `26.07.0` under the managed native dependency location even though `pdftoppm` was absent from ordinary PATH and from `dependencies/bin/override`.

A two-page temporary authorized PDF was rendered successfully with that exact managed binary, producing two PNGs. Both PNGs were then visually inspected through `codex.image_read` and showed the expected text and vector geometry.

Therefore:

```text
managed OpenAI/Codex Poppler exists                YES
model-free PDF -> PNG with managed renderer        PASS
PNG -> ChatGPT vision                              PASS
separate system Poppler installation needed        NO
custom PDF rendering engine justified              NO
thin semantic authority/provenance wrapper needed  LIKELY / DESIGN NEXT
complex representative PDF fidelity                STILL OPEN
```

## Important correction to prior interpretation

Validation 040 remains valid as an execution result, but its renderer blocker must now be interpreted precisely:

```text
E117-2 observed
    Codex PDF Skill routed
    ordinary discovered pdftoppm path was an unusable MiKTeX stub
    no alternative renderer was found by that turn

Checkpoint 285 adds
    maintained Codex primary runtime actually contains Poppler
    the managed native path was not surfaced to that turn
```

So the project should not treat E117-2 as evidence that Poppler installation is required.

## Exact continuation

Before publishing a new document-render MCP surface:

```text
1. define a supported runtime-resolution contract using the upstream dependency loader when available and the documented runtime manifest/fallback root otherwise;
2. design the smallest model-free semantic page-render seam around maintained Poppler;
3. preserve read-only workspace authority for the caller and use bounded temporary output internally;
4. return selected rendered page images as standard MCP image content with source/render provenance;
5. test representative annotated/math/table/multi-column/scanned PDFs and characterize font/OCR/fidelity gaps;
6. only benchmark MarkItDown/Docling/PyMuPDF4LLM if concrete gaps remain.
```

Research 117 remains active. The broader Research 113 upstream-ecosystem program remains active above it, and the Source Vault continuation remains paused until that selected Level-2 research path closes.

Primary evidence:

```text
docs/local_execution/validation/044_managed_primary_runtime_poppler_page_rendering_probe_qualified.md
docs/research/117_reuse_first_multimodal_document_architecture_and_local_media_handoff.md
docs/local_execution/validation/043_model_free_mcp_image_bridge_live_chatgpt_vision_qualified.md
docs/local_execution/validation/040_codex_pdf_skill_visual_read_reuse_experiment.md
```
