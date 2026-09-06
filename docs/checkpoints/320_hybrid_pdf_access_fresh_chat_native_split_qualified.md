# Checkpoint 320: Hybrid PDF Access Fresh-Chat Native Split Qualified

**Date:** 2026-09-06
**Status:** END-TO-END NATIVE SPLIT PASS / TEXT-VISION QUALIFICATION NEXT
**Checkpoint class:** LOCAL EXECUTION / DIRECT CHATGPT FILE ACCESS
**Project stage:** Research 120 automatic hybrid PDF direct-source routing
**Scope:** Preserves the first fresh-chat end-to-end qualification of the live `codex.pdf_access` public facade after preview.16 activation, including fresh tool discovery, automatic native split routing, managed PDF resource-link delivery, ChatGPT host materialization into actual conversation files, and ordinary ChatGPT-side inspection of a materialized split part.
**Authority:** Research 120 defines the architecture. Validation 078 contains the detailed evidence.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-18`
**Conversation title:** `18 - Astra Architecture Review and Multimodal Handoff Continuation`
**Primary collaborator:** ChatGPT

Checkpoint 319's activation boundary is now closed for the native split route. After the controlled restart and tunnel reconnect, independent local verification shows:

```text
Codexless ok       true
version            0.1.1-preview.16-hybrid-pdf-access
surfaceVersion     codexless-public-preview-v2
toolCount          60
tunnel /healthz    HTTP 200
tunnel /readyz     HTTP 200
```

The user refreshed the existing ChatGPT developer MCP app and opened a fresh disposable conversation. In that fresh chat, `codex.pdf_access` was available and executed successfully with exactly:

```text
cwd           C:\School\Machine Learning
documentPath  32.LinearModels2.annotated.pdf
intent        native
```

No other ADS tool was used for the qualification call.

The facade returned:

```text
facade schema      codexless.pdf-access-orchestrator.v1
policy schema      codexless.pdf-access-policy.v1
requested intent   native
effective intent   native
primary route      native-parts
native mode        parts
source bytes       8,715,014
source SHA-256     9b4bb8efa6f1adfc27f1cacbfc7b77e1c4335d1629962235f64121ad2768f3e9
source pages       38 by returned page coverage
resource links     2
```

The two deterministic managed native parts matched the previously qualified split plan exactly:

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

The original `codex.pdf_access` result contained metadata plus MCP `resource_link` references. It did not embed the PDF payloads as PDF bytes or base64 in the structured tool result.

The ChatGPT host then materialized both managed PDF resources as actual conversation files:

```text
file_000000001b9c8210a818fc8685769c2d
    /mnt/data/32.LinearModels2.annotated.pages-1-34.pdf

file_00000000fc9881f49b114f21e201ba92
    /mnt/data/32.LinearModels2.annotated.pages-35-38.pdf
```

Ordinary ChatGPT-side PDF inspection of the first materialized part established:

```text
part page count  34
page size        595 x 842 pt
```

Concrete first-page inspection reported:

```text
portrait A4-style page
three lecture-slide panels stacked vertically on the left
corresponding prose/notes on the right
orange title area: "Beyond Linear Models" / "Part 1: Neural networks"
section label for Neural networks and a Surfdrive video/download link
middle slide: "making linear models more powerful"
numeric table plus red/blue nonlinear classification-region plots
notes about expanding features to obtain nonlinear decision boundaries
lower slide: "from linear to nonlinear models"
neural networks contrasted with SVMs
learned feature extractor contrasted with kernel-based feature expansion
notes discuss neural networks, support vector machines, a two-layer feedforward network and a kernel function
```

The fresh chat explicitly separated evidence classes:

```text
direct codex.pdf_access evidence
    facade/policy versions
    source identity/size
    route decision
    split ranges
    per-part sizes
    resource names/URIs
    two resource links

ChatGPT host evidence
    two host file IDs
    exact /mnt/data paths
    successful materialization of both managed PDF resources

ordinary ChatGPT-side PDF evidence
    first part has 34 pages
    concrete first-page visual/content inspection
```

No OCR, Browser, Agent, shell recovery, web search, source-workspace write, manual source-PDF upload or reasoning-model intermediary was used in the qualification path.

This proves the new automatic high-level path end to end for a source that is too large for conservative whole-PDF native handoff but whose deterministic split parts fit the host-qualified native envelope:

```text
authorized local PDF
    -> codex.pdf_access
    -> automatic native-parts route
    -> managed deterministic split PDFs
    -> MCP resource_link content
    -> ChatGPT host materialization
    -> ordinary ChatGPT PDF inspection
```

The next Research 120 qualification should target the mixed text/vision behavior on the 78,874,939-byte `51.Deep Learning2.annotated.pdf`, especially the representative individually oversized native pages 16 and 49, while preserving the one-tool-call constraint for the high-level facade.

```text
CHECKPOINT_320 = HYBRID_PDF_ACCESS_FRESH_CHAT_NATIVE_SPLIT_QUALIFIED
```
