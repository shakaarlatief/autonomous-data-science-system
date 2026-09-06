# Checkpoint 321: Hybrid PDF Access Fresh-Chat Native Hybrid Qualified

**Date:** 2026-09-06
**Status:** END-TO-END NATIVE + TEXT + VISION PASS / PUBLIC INTENT MATRIX NEXT
**Checkpoint class:** LOCAL EXECUTION / DIRECT CHATGPT FILE ACCESS
**Project stage:** Research 120 automatic hybrid PDF direct-source routing
**Scope:** Preserves the first fresh-chat end-to-end qualification of the live `codex.pdf_access` native hybrid route on a large PDF whose deterministic native partition contains individually oversized pages. The one high-level call returned fourteen bounded native PDF resources plus embedded-text and rendered-image fallback for source pages 16 and 49; ChatGPT directly inspected both returned images, materialized all fourteen native PDF resources as conversation files, and independently inspected one materialized native part using ordinary ChatGPT-side PDF tooling.
**Authority:** Research 120 defines the architecture. Validation 079 contains the detailed evidence.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-18`
**Conversation title:** `18 - Astra Architecture Review and Multimodal Handoff Continuation`
**Primary collaborator:** ChatGPT

Checkpoint 320 established the fresh-host native-split route. This checkpoint closes the more demanding large-PDF hybrid-native route against:

```text
C:\School\Machine Learning\51.Deep Learning2.annotated.pdf
```

The fresh disposable ChatGPT conversation invoked exactly one ADS tool:

```text
codex.pdf_access
```

with:

```text
intent         native
maxCharacters  50000
```

The facade reported:

```text
facade schema      codexless.pdf-access-orchestrator.v1
policy schema      codexless.pdf-access-policy.v1
requested intent   native
effective intent   native
primary route      native-parts-plus-page-fallback
native mode        parts-plus-page-fallback
split generation   reused
native target      7,000,000 bytes
```

Source identity:

```text
filename    51.Deep Learning2.annotated.pdf
bytes       78,874,939
SHA-256     3872d5b3957d4313ab154a8405222d47098dda50657b660330ea0eecdce24110
page count  56
```

The route returned fourteen native PDF resource links covering all non-oversized pages:

```text
1-7
8-11
12-14
15
17-19
20
21
22-27
28-36
37
38-41
42
43-48
50-56
```

All fourteen managed native PDFs remained below the 7,000,000-byte native-part target.

Pages 16 and 49 were independently too large for native preservation inside the host-qualified per-part envelope and were therefore routed to the accepted faithful direct-source fallback:

```text
page 16
    fallback mode      direct
    text returned      17,999 chars
    text truncated     false
    rendered PNG       1240 x 1755
    PNG bytes          583,130
    PNG SHA-256        aca9cfadbfcb99382e22a2472495f26d1ab097922ce9406d66a8121810a56023

page 49
    fallback mode      direct
    text returned      1,345 chars
    text truncated     false
    rendered PNG       1240 x 1755
    PNG bytes          535,152
    PNG SHA-256        2eaaa5f2ffaae9b3d1e171d200d412dc1c545425d5f539e48513ac25c4e5e927
```

Direct page-16 text and image evidence included StyleGAN, latent-vector injection, per-layer noise, coarse/middle/fine style manipulation, generated faces, and source/destination latent-vector controls.

Direct page-49 text and image evidence included correlation versus causation, the statements `Correlation does not imply causation.` and `No correlation without causation.`, and the predictive-versus-intervention burned-toast/smoke example.

Facade projection counts:

```text
resourceLinkCount  14
imageCount         2
```

The structured/text metadata contained neither PDF payload bytes/base64 nor rendered-image base64. PDF content traveled through separate MCP `resource_link` items and rendered pages traveled through separate MCP image content items. Literal `sha1_base64` strings observed in page-16 extracted text belonged to the PDF's embedded LaTeX/accessibility content and were not transport payloads.

The fresh ChatGPT host materialized all fourteen native PDF resources as actual conversation files under `/mnt/data`. This establishes:

```text
HOST_NATIVE_PART_MATERIALIZATION = PASS 14/14
```

The same ChatGPT response directly inspected both image content items returned by the single facade call without another ADS operation. It then used only normal ChatGPT-side PDF capabilities to inspect the materialized pages-1-7 PDF, reporting seven pages, 595 x 842 pt page size, no encryption, four annotations, and concrete first-page content including `Deep generative models`, `Part 1: Generator networks`, generated human faces, Karras et al., and the `visual shorthand` slide.

Evidence classes remain separated:

```text
A. direct codex.pdf_access evidence
    source identity
    routing decision
    native split plan
    fallback text metadata
    rendered PNG metadata
    projection counts

B. ChatGPT host evidence
    14 host file IDs
    14 exact /mnt/data paths
    successful materialization of every native part

C. direct image-content inspection
    concrete page-16 and page-49 visual observations
    no additional ADS call

D. ordinary ChatGPT-side materialized-PDF inspection
    pages-1-7 part inspected with normal PDF tooling
```

No OCR, Browser, Agent, source-workspace write, manual source-PDF upload, web search, or reasoning-model intermediary inside the PDF facade was used.

The resulting proven high-level route is:

```text
authorized large local PDF
    -> one codex.pdf_access call
    -> deterministic native split reuse
    -> bounded native PDF resource links for ordinary pages
    -> embedded text + rendered-image fallback for individually oversized pages
    -> direct ChatGPT vision over returned images
    -> ChatGPT host materialization of all native PDF parts
    -> ordinary ChatGPT PDF inspection
```

This closes the core `intent=native` hybrid architecture at the host boundary. Remaining Research 120 public qualification should now move to the explicit high-level intent matrix and isolation path rather than repeating native routing:

```text
text
visual
mixed
auto
>192 MiB page/range isolation through codex.pdf_access
```

```text
CHECKPOINT_321 = HYBRID_PDF_ACCESS_FRESH_CHAT_NATIVE_HYBRID_QUALIFIED
```