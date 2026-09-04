# Validation 058: Large PDF Resource-Link Preview.14 Live Smokes Passed

**Date:** 2026-09-04
**Status:** PASS / PREVIEW.14 LIVE / LARGE-HOST LADDER NEXT
**Research:** Research 117

After the controlled restart, Codexless reported `0.1.1-preview.14` / `codexless-public-preview-v2` / 56 tools. The tunnel returned HTTP 200 for both `/healthz` (`live`) and `/readyz` (`ready`).

Preserved document smokes were rerun against the restarted runtime. `codex.document_read` on the two-page probe returned the expected embedded text through `pdfjs-dist 5.4.624`, pageCount 2, and `ocrPerformed=false`. `codex.document_render` on the same probe returned both expected PNG pages at 1275 x 1651 through `pdfjs-dist 5.6.205` + `@napi-rs/canvas 0.1.100`, with the same source and page hashes as the prior qualified baseline. Visual inspection confirmed the three stacked rectangles + diagonal line on page 1 and five increasing bars on page 2.

Accepted result:
```text
PREVIEW14_LARGE_PDF_RESOURCE_LINK_RUNTIME=LIVE
CODEXLESS_HEALTH=PASS
TUNNEL_HEALTH=PASS
TUNNEL_READY=PASS
PRESERVED_DOCUMENT_READ_SMOKE=PASS
PRESERVED_DOCUMENT_RENDER_SMOKE=PASS
```

The next unresolved claim is host materialization of real PDFs above the former 4 MiB ceiling. Continue with fresh disposable chats using only `codex.document_file_link`, starting at 4.23 MiB and stopping at the first failed tier.
