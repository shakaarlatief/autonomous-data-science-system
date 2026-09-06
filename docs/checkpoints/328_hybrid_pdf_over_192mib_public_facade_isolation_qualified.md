# Checkpoint 328: Hybrid PDF >192 MiB Public Facade Isolation Qualified

**Date:** 2026-09-06
**Status:** PUBLIC PDF ROUTE FAMILY QUALIFIED / RESEARCH 120 PDF LEAF COMPLETE
**Checkpoint class:** LOCAL EXECUTION / DIRECT CHATGPT FILE ACCESS
**Project stage:** Research 120 automatic hybrid PDF direct-source routing
**Scope:** Preserves the successful public-facade qualification of all three >192 MiB page/range-isolation route classes on a valid authorized 211,813,221-byte PDF, including managed-artifact reuse, original source-page provenance and direct ChatGPT text/image consumption.
**Authority:** Validation 086 contains the exact source, route, artifact, hash, warning, provenance and source-cleanliness evidence.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-19`
**Conversation title:** `19 - Hybrid PDF Intent Matrix and Isolation Qualification`
**Primary collaborator:** ChatGPT

The final previously unqualified public PDF route family now passes:

```text
text   -> isolate-then-text
visual -> isolate-then-render
mixed  -> isolate-then-text-plus-render
```

The source was a valid deterministic synthetic PDF of 211,813,221 bytes, above the 201,326,592-byte direct-processing ceiling. Page 1 isolated to one managed 862-byte PDF whose source-page map remained `[1]`. The first text call generated it, then visual and mixed calls visibly reused the same generation key/id and artifact SHA-256.

Text returned the intended 122 characters with `sourcePageNumber:1`. Visual returned a directly inspectable 1275 x 1651 PNG, 48,898 bytes, SHA-256 `aeb0cb98eb4ac5fc31ae099f42882e7c3d0c0bfdae6254b29bb2d865e3514427`, also mapped to source page 1. No PDF resource links were involved.

After the calls the source retained its original SHA-256, and its test directory still contained only the source PDF, directly confirming that the derived artifact did not appear beside the source. After all evidence was captured, the synthetic 211,813,221-byte source and its now-empty dedicated `.tmp` directory were removed by an exact-path, exact-size-guarded cleanup; no user source or tracked repository file was deleted.

The renderer also emitted Node's standard `--allow-addons` security warning. This is preserved as a hardening caveat rather than hidden: functional qualification passes, while the Node permission model is not treated as an OS-grade isolation guarantee when a trusted native addon is enabled.

Research 120 can now close for the accepted PDF direct-source routing scope. The broader AB-005 document work can advance to the next file-type capability matrix rather than adding more PDF size-threshold tests without new evidence.

```text
CHECKPOINT_328 = HYBRID_PDF_PUBLIC_FACADE_ISOLATION_QUALIFIED
```
