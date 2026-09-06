# Checkpoint 318: Hybrid PDF Routing Core Qualified, Public Facade Next

**Date:** 2026-09-06
**Status:** CORE QUALIFIED / PUBLIC FACADE NEXT
**Checkpoint class:** LOCAL EXECUTION / DIRECT CHATGPT FILE ACCESS
**Project stage:** Research 120 automatic hybrid PDF direct-source routing
**Scope:** Preserves the live post-restart 192 MiB direct-processing qualification and the completed private implementation/qualification of the managed PDF artifact cache, deterministic native splitter/page-range isolator, cached text/render/resource adapters and high-level model-free routing orchestrator.
**Authority:** Research 120 defines the architecture. Validation 076 contains the detailed evidence.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-18`
**Conversation title:** `18 - Astra Architecture Review and Multimodal Handoff Continuation`
**Primary collaborator:** ChatGPT

Checkpoint 317's restart-pending boundary is closed. After the controlled restart, both existing public direct-processing routes passed on the same valid 134,218,426-byte PDF:

```text
document_read    PASS
document_render  PASS
```

The Research 120 internal architecture is no longer policy-only. The private candidate now implements and qualifies:

```text
PdfSourceProfiler
PdfAccessPolicy
PdfNativeSplitter
PageRangeIsolator
PdfArtifactManager
PdfArtifactTextReader
PdfArtifactRenderer
PdfArtifactResourceStore
PdfAccessOrchestrator
```

The content-addressed cache remains outside all source workspaces. Every reusable derivative remains subordinate to the original authorized source and is revalidated against source authority and identity before use. Source drift creates a new generation. Cached artifacts cannot become a hidden authority bypass.

The candidate regression suite passes:

```text
42 / 42 PASS
```

It includes reuse after manager reconstruction, deterministic regeneration after eviction, atomic failed-generation cleanup, active-lease eviction protection, rendered-page equality between original pages and their native split copies, cached PDF embedded text, cached PDF vision and a valid >192 MiB source isolated into a bounded artifact for both text and render.

Real read-only Machine Learning corpus planning also matches the intended architecture. `32.LinearModels2.annotated.pdf` splits into two bounded native parts with no oversized page. `51.Deep Learning2.annotated.pdf` produces bounded native parts plus oversized pages 16 and 49, so the correct route is native parts plus embedded-text/rendered-page fallback for those two pages.

Private implementation preservation is synchronized at:

```text
3cf995e358425c4db970337f0413a8862bb5a564
RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
postflightOk=true
```

No new public MCP tool is exposed at this checkpoint. The next implementation seam is now the public high-level facade itself:

```text
qualified PdfAccessOrchestrator
    -> one bounded MCP PDF-access action
    -> normal MCP resource_link content for native PDFs/parts
    -> normal text structured content for embedded text
    -> normal MCP image content for rendered pages
    -> existing low-level PDF tools retained for debugging/qualification
```

That facade must be schema/content-projection tested and fully regressed before live publication. Because adding it changes the public tool surface, its eventual live activation will require the normal restart and ChatGPT tool-projection refresh/fresh-chat handling appropriate to AB-008.

```text
CHECKPOINT_318 = HYBRID_PDF_ROUTING_CORE_QUALIFIED_PUBLIC_FACADE_NEXT
```
