# Validation 053: Tiny MCP PDF Resource-Link Host Materialization Passed

**Date:** 2026-09-04
**Status:** PASS / LIVE HOST TINY RESOURCE-LINK MATERIALIZATION QUALIFIED
**Research:** Research 117
**Experiment:** E117-5g
**Live runtime:** `0.1.1-preview.13` / `codexless-public-preview-v2` / 56 tools

## Result

Fresh disposable ChatGPT testing invoked only `codex.document_file_link` on the 2,372-byte two-page `probe.pdf` after the controlled preview.13 restart, tunnel health/readiness 200/200, and ChatGPT app refresh.

Observed host behavior:

```text
codex.document_file_link                                  PASS
original tool result embeds PDF bytes/base64              false
original tool result contains metadata + resource_link     true
ChatGPT host resolves/fetches linked resource              supported by materialization behavior
probe.pdf conversation file/attachment materialized        PASS
same-turn parsed/rendered PDF content exposed to model      false
explicit resources/read trace surfaced to model             false
```

The host response explicitly distinguished direct evidence from inference. It reported no visible `resources/read` execution trace, but the linked resource was nevertheless resolved sufficiently for `probe.pdf` to materialize as a conversation file. This is the key transport discriminator: unlike the embedded-resource route, the original tool result remained small and contained no PDF base64.

The same-turn content-access behavior is consistent with Validation 051: file materialization succeeds first, while actual PDF inspection becomes available on a later user turn. No fallback tool was allowed in this tiny host test.

## Accepted claim

```text
MCP_PDF_RESOURCE_LINK_MATERIALIZATION=PASS
```

This does not yet qualify representative-size PDFs. The decisive next test is the 1.68 MiB `CheatSheet_A4.pdf`, which previously failed through inline embedded-resource transport because its tool-result base64 expanded to roughly 2.24 million characters.

## Next

Use only `codex.document_file_link` on `CheatSheet_A4.pdf` from the authorized `big-data-statistics` workspace. Require: no maximum-chat-length failure, no inline PDF bytes in the original tool result, host file materialization, and then next-turn full-PDF inspection of the materialized attachment.
