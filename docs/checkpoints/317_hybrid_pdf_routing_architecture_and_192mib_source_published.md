# Checkpoint 317: Hybrid PDF Routing Architecture and 192 MiB Source Published

**Date:** 2026-09-06
**Status:** ARCHITECTURE ACCEPTED / POLICY PASS / 192 MiB SOURCE PUBLISHED / RESTART PENDING
**Checkpoint class:** LOCAL EXECUTION / DIRECT CHATGPT FILE ACCESS
**Project stage:** Research 120 automatic hybrid PDF direct-source routing
**Scope:** Preserves the accepted automatic route hierarchy, the managed content-addressed cache decision for generated split PDFs, the first deterministic route-policy candidate, and the guarded installed-source increase of `document_read` / `document_render` from 96 MiB to 192 MiB.
**Authority:** Research 120 defines the architecture. Validation 075 contains the detailed implementation/publication evidence.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-18`
**Conversation title:** `18 - Astra Architecture Review and Multimodal Handoff Continuation`
**Primary collaborator:** ChatGPT

The architecture now distinguishes four things explicitly:

```text
native whole-file host handoff
    conservative target 7,000,000 bytes

native PDF splitting
    deterministic contiguous parts <= 7,000,000 bytes

large-source direct text/render
    bounded direct-processing envelope 192 MiB

very large sources above direct-processing envelope
    isolate bounded page/range first, then text/render
```

Generated split PDFs will not be written into source folders and will not be regenerated unconditionally on every request. They are transport artifacts managed by a Codexless-owned content-addressed cache:

```text
small durable manifest
reusable cached part bytes
source SHA + workspace authority binding
source-drift invalidation
deterministic regeneration after eviction
```

This preserves the original PDF as the sole source of truth while avoiding repeated expensive splitting.

The first private routing-policy implementation is statically qualified 8/8. It does not yet change the public MCP surface.

The installed direct text/render source envelope is now published as 192 MiB. A valid 134,218,421-byte PDF passed installed `pdfjs-dist@5.4.624` embedded-text extraction with the new 384 MiB parser-child heap. The renderer path separately passed >96 MiB maintained-runtime feasibility.

The private implementation complement is synchronized at `fde55f1db3191086431f5a7d56fc416c1beebfa1` with `RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS` and `postflightOk=true`. The temporary runtime publication admission was removed; the durable workspace registry is revision 14 with the normal four workspaces only.

The currently running Codexless process predates this publication. One controlled Codexless/tunnel restart remains required. No Plugin refresh is required because no public schema or tool count changed.

After restart, do not return to ad-hoc size-limit research. The next implementation seam is the managed artifact manager plus deterministic native splitter/page-range isolator required by Research 120.

```text
CHECKPOINT_317 = HYBRID_PDF_ROUTING_ARCHITECTURE_AND_192MIB_SOURCE_PUBLISHED
```
