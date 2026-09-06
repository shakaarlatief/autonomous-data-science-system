# Validation 078: Hybrid PDF Access Fresh-Chat Native Split Qualified

**Date:** 2026-09-06
**Status:** PASS / END-TO-END NATIVE SPLIT HOST MATERIALIZATION QUALIFIED
**Research:** Research 120
**Scope:** Verify that the refreshed ChatGPT host discovers the newly activated `codex.pdf_access` tool in a fresh conversation, that the facade automatically selects deterministic native splitting for an 8,715,014-byte authorized PDF, that both managed PDF parts are delivered as MCP resource links without inline PDF bytes/base64, and that the ChatGPT host materializes and can inspect the returned PDFs using ordinary ChatGPT-side PDF capabilities.

## 1. Live activation state

Independent local verification after controlled restart/reconnect:

```text
Codexless ok       true
version            0.1.1-preview.16-hybrid-pdf-access
surfaceVersion     codexless-public-preview-v2
toolCount          60
tunnel /healthz    HTTP 200
tunnel /readyz     HTTP 200
```

The user refreshed the existing ChatGPT developer MCP app after those local gates were healthy.

## 2. Fresh-chat discovery

A fresh disposable ChatGPT conversation was opened specifically to avoid the stale callable-tool projection previously observed in long-running chats.

Fresh-chat result:

```text
codex.pdf_access availability  AVAILABLE
call result                    SUCCEEDED
```

Exactly one ADS tool was called:

```text
codex.pdf_access
```

with:

```text
cwd           C:\School\Machine Learning
documentPath  32.LinearModels2.annotated.pdf
intent        native
```

The qualification explicitly forbade `codex.document_read`, `codex.document_render`, `codex.document_file_link`, `codex.document_file_read`, Browser, Agent, OCR, shell commands, web search and any other ADS tool.

## 3. Direct facade evidence

The successful facade result reported:

```text
facade schema      codexless.pdf-access-orchestrator.v1
routing schema     codexless.pdf-access-policy.v1
requested intent   native
effective intent   native
primary route      native-parts
native mode        parts
source filename    32.LinearModels2.annotated.pdf
source bytes       8,715,014
source SHA-256     9b4bb8efa6f1adfc27f1cacbfc7b77e1c4335d1629962235f64121ad2768f3e9
source page span   1-38
resource links     2
```

The two native managed artifacts were:

```text
part 1
    source pages   1-34
    bytes          6,851,116
    resource name  32.LinearModels2.annotated.pages-1-34.pdf
    artifact file  part-0001-p0001-p0034.pdf

part 2
    source pages   35-38
    bytes          1,646,076
    resource name  32.LinearModels2.annotated.pages-35-38.pdf
    artifact file  part-0002-p0035-p0038.pdf
```

The returned split ranges and sizes exactly match the earlier read-only `pypdf 6.10.0` planning evidence for this source.

## 4. Tool-result transport evidence

The original `codex.pdf_access` result contained metadata plus two MCP `resource_link` references.

It did **not** contain the PDF payloads as PDF bytes or base64 inside the structured tool result.

Result:

```text
INLINE_PDF_BYTES_IN_TOOL_RESULT = NONE
INLINE_PDF_BASE64_IN_TOOL_RESULT = NONE
RESOURCE_LINK_COUNT              = 2
```

## 5. ChatGPT host materialization

The host subsequently exposed both returned resources as actual conversation files:

```text
file_000000001b9c8210a818fc8685769c2d
    /mnt/data/32.LinearModels2.annotated.pages-1-34.pdf

file_00000000fc9881f49b114f21e201ba92
    /mnt/data/32.LinearModels2.annotated.pages-35-38.pdf
```

This is separate host-side evidence from the `codex.pdf_access` tool result itself.

Result:

```text
MANAGED_PART_1_HOST_MATERIALIZATION = PASS
MANAGED_PART_2_HOST_MATERIALIZATION = PASS
```

## 6. Ordinary ChatGPT-side PDF inspection

The fresh chat then used only normal ChatGPT-side PDF capabilities on the first host-materialized part.

Reported tooling:

```text
ChatGPT PDF Skill
pdf_inspect.py
render_pdf.py
direct inspection of rendered first-page PNG
OCR not used
```

First part:

```text
total pages  34
page size    595 x 842 pt throughout
```

Concrete page-1 observations included:

```text
portrait A4-style page
three lecture-slide panels stacked vertically on the left
corresponding prose/notes on the right
large orange title area: "Beyond Linear Models" / "Part 1: Neural networks"
upper-right section text for Neural networks plus Surfdrive link
middle slide: "making linear models more powerful"
numeric table plus red/blue nonlinear classification-region plots
notes explain feature expansion for nonlinear decision boundaries
lower slide: "from linear to nonlinear models"
neural networks contrasted with SVMs
learned feature extractor contrasted with kernel-based feature expansion
right-side notes mention neural networks, support vector machines, a two-layer feedforward network and a kernel function
```

This proves the materialized part is not merely an opaque attachment reference; ordinary ChatGPT file/PDF handling can consume it after host resolution.

## 7. Evidence-class separation

Direct `codex.pdf_access` evidence:

```text
facade/policy schema versions
source filename / byte size / SHA-256
native-parts route and mode
source page coverage
part source-page ranges
part byte sizes
resource names / artifact names
resource-link count
```

ChatGPT host evidence:

```text
host file IDs
exact /mnt/data paths
successful materialization of both returned resources
```

Ordinary ChatGPT-side inspection evidence:

```text
first part page count
page dimensions
concrete first-page visual/content features
```

The qualification does not use prior chat memory as substitute evidence for any of those fresh-host claims.

## 8. Architecture result

The representative route now passes end to end:

```text
authorized source PDF > 7,000,000-byte native target
    -> one codex.pdf_access call
    -> deterministic managed native split
    -> two bounded PDF resource links
    -> no inline PDF payload in tool result
    -> host resolves both resources
    -> two actual conversation PDF files
    -> ordinary ChatGPT PDF inspection succeeds
```

No manual source upload, source-workspace write, OCR, Browser, Agent, web search or reasoning-model intermediary was required.

## 9. Result

```text
FRESH_CHAT_TOOL_DISCOVERY                 = PASS
CODEX_PDF_ACCESS_CALL                     = PASS
AUTOMATIC_NATIVE_PARTS_ROUTE              = PASS
SOURCE_IDENTITY_PROVENANCE                = PASS
DETERMINISTIC_PART_RANGES                 = PASS
INLINE_PDF_PAYLOAD                        = NONE
MCP_RESOURCE_LINK_PROJECTION              = PASS
MANAGED_PART_1_HOST_MATERIALIZATION       = PASS
MANAGED_PART_2_HOST_MATERIALIZATION       = PASS
CHATGPT_SIDE_PART_PDF_INSPECTION          = PASS
OCR                                        = NONE
SOURCE_WORKSPACE_WRITE                     = NONE
REASONING_MODEL_INTERMEDIARY               = NONE
NEXT                                       = MIXED_TEXT_VISION_OVERSIZED_PAGE_QUALIFICATION
```

Fresh-chat terminal marker:

```text
HYBRID_PDF_ACCESS_FRESH_CHAT_NATIVE_SPLIT=PASS
```

The next bounded qualification should exercise the facade's mixed native/text/vision behavior against the 78,874,939-byte `51.Deep Learning2.annotated.pdf`, whose deterministic native partition contains individually oversized pages 16 and 49.
