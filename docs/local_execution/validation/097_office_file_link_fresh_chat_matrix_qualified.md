# Validation 097: Office File-Link Fresh-Chat Matrix Qualified

**Date:** 2026-09-07
**Status:** PASS / RESEARCH 121 HOST MATRIX QUALIFIED / FORMAT FALLBACKS NOT REQUIRED FOR ACCEPTED SCOPE
**Research:** Research 121
**Scope:** Preserve the fresh disposable ChatGPT qualification of the live `codex.file_link` whole-file handoff for deterministic DOCX, PPTX and XLSX sources, including tool discovery, resource-link execution, host materialization, exact source identity, native structure/content inspection, embedded visual access and fallback disposition.

## Fresh-chat execution boundary

After preview.17 was live at 61 tools and the ADS developer MCP app had been refreshed, a fresh disposable ChatGPT conversation exposed `codex.file_link`. Exactly three ADS calls were made, one per deterministic Office fixture, and no compensating ADS/file/parser/render/Browser/Agent/OCR/shell/web call was used.

```text
DOCX  codex.file_link  PASS
PPTX  codex.file_link  PASS
XLSX  codex.file_link  PASS
```

The fresh-chat terminal classification was:

```text
OFFICE_FILE_LINK_FRESH_CHAT_MATRIX=PASS
```

## DOCX result

Direct ADS evidence reported:

```text
filename  office-handoff.docx
MIME      application/vnd.openxmlformats-officedocument.wordprocessingml.document
bytes     1,985
SHA-256   3bf55d3b8eb7ddcf260282224f409a2d27f00514fc61d444986630548c2bb65d
schema    codexless.file-resource-link.v1
inline source bytes/base64  NO
```

The ChatGPT host materialized the original file into its conversation/file layer. Independent ChatGPT-side hashing reproduced the exact 1,985 bytes and SHA-256. Ordinary ChatGPT-side inspection of that materialized DOCX confirmed:

```text
ADS Office Handoff DOCX Qualification
DOCX_MARKER_ALPHA
one 2x2 table: Metric | Value ; Rows | 2
DOCX_IMAGE_MARKER
one embedded 64x64 PNG
four distinct equal 32x32 image quadrants
```

Therefore native text, Word/table structure and embedded image content were directly accessible.

## PPTX result

Direct ADS evidence reported:

```text
filename  office-handoff.pptx
MIME      application/vnd.openxmlformats-officedocument.presentationml.presentation
bytes     3,046
SHA-256   575f00d083c925f6bae9a76019ccc9095e82f2a85b7295c43502b38c6815b8c7
inline source bytes/base64  NO
```

The host materialized the original presentation and ChatGPT-side hashing reproduced the exact identity. Native presentation inspection confirmed:

```text
2 slides
slide 1: ADS Office Handoff PPTX Qualification
slide 1: PPTX_MARKER_BETA
slide 2: Second slide: structure check
slide 2: PPTX_MARKER_GAMMA
slide 1 contains an actual embedded 64x64 PNG picture
picture shape position/dimensions are accessible
the embedded PNG contains the expected four equal colored quadrants
```

Therefore slide ordering, text, picture-object structure, embedded image bytes and placement metadata were directly accessible.

## XLSX result

Direct ADS evidence reported:

```text
filename  office-handoff.xlsx
MIME      application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
bytes     2,585
SHA-256   7fe060a575346a2844940bd4eb14fd27dc9795f1b8ea1ee59ad3fd202f7aa731
inline source bytes/base64  NO
```

The host materialized the original workbook and ChatGPT-side hashing reproduced the exact identity. Direct inspection of the intact materialized OOXML workbook confirmed:

```text
2 sheets: Metrics, Notes
XLSX_MARKER_DELTA
XLSX_MARKER_EPSILON
Metrics!B2 = 21
Metrics!B3 = 7
Metrics!C2 formula B2*2 with cached value 42
Metrics!C3 formula SUM(B2:B3) with cached value 28
header cells use a distinct style index
header style references a separate font and fill and applies both
```

The ordinary spreadsheet artifact importer timed out during daemon startup in that fresh chat and was explicitly excluded from the evidence. The successful qualification came from direct inspection of the intact materialized OOXML source.

## Accepted architectural conclusion

For all three formats, the fresh host result establishes:

```text
resource_link execution                     PASS
host materialization                        PASS
byte-for-byte source identity               PASS
text/data access                            PASS
native structure access                     PASS
embedded visual access where applicable     PASS
style/layout metadata access                PASS
format-specific fallback required now       NO
```

The accepted default is therefore the original-file `codex.file_link` route for allowlisted DOCX, PPTX and XLSX. Do not insert a custom parser/renderer merely because the source is an Office file.

The qualification does **not** claim pixel-identical rendering against Microsoft Word, PowerPoint or Excel. If a future task explicitly requires final rendered-page/slide/workbook visual fidelity rather than source content/structure/assets, that requirement may justify a separate model-free rendering experiment. It is a trigger-based future capability, not unfinished Research 121 work.

## Cleanup

After the matrix result was preserved, the completed AB-020/Office protected-scratch directories and deterministic qualification fixtures were removed from the private runtime repository's `.tmp` area. The durable candidate remains preserved in private Git and the public repository preserves the full evidence chain.

```text
RESEARCH_121=COMPLETE
OFFICE_NATIVE_WHOLE_FILE_ROUTE=ACCEPTED
DOCX_FORMAT_FALLBACK=NOT_REQUIRED
PPTX_FORMAT_FALLBACK=NOT_REQUIRED
XLSX_FORMAT_FALLBACK=NOT_REQUIRED
PIXEL_IDENTICAL_OFFICE_RENDERING=NOT_CLAIMED
```
