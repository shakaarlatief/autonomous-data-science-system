# Validation 065: Astra Phase 2 PDF Evidence Candidate Reviewed and Preserved

**Date:** 2026-09-05
**Status:** PASS / NON-LIVE ARCHITECTURE CANDIDATE REVIEWED / LIVE SEMANTIC QUALIFICATION PENDING
**Research:** Research 118 under Research 117

## Purpose

Preserve the independent review of GPT-6 Astra Phase 2 after the frozen GPT-5.6 Sol implementation was exposed, verify the new private source-bound PDF evidence candidate without publishing it, and establish the exact next live semantic discriminator.

This validation does not claim that a formal Codex worker can already understand arbitrary large PDFs correctly. It validates the architecture review, candidate integrity/coverage seam, and preservation boundary only.

## Starting boundaries

Public ADS authority before this transition:

```text
branch      v1-source-vault-bootstrap-resume
HEAD        f16612a0bf799e4e3b64644b44c37dba2c7d82ee
checkpoint  305
```

Frozen private Sol comparison boundary:

```text
repository  autonomous-data-science-system-local-runtime
branch      main
HEAD        e45a5de7ddae7f8158445b4b71d9c5f70cab8a2c
```

Astra Phase 1 was completed before the private repository was added to the Codex Desktop project. Phase 2 then used the same Astra thread with both repositories visible, preserving the intended independent-first comparison sequence.

## Phase 2 candidate preserved privately

The reviewed candidate contains ten files under:

```text
.ads-private/codexless/astra-phase2-pdf-evidence-candidate/
```

The private runtime manifest was reconciled to public Checkpoint 305 / `f16612a0...`, and the candidate was committed through the registered `ads-local-runtime` semantic Git surface.

Private preservation result:

```text
commit
    a5025c2071077f719dcc59c7dfd729ee59ec34eb

message
    Preserve Astra Phase 2 PDF evidence candidate

commit postflight
    indexCleanAfter=true
    postflightOk=true
```

The bounded private push then returned:

```text
RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
retried=false
postflightOk=true
local HEAD == origin/main
```

A pre-commit candidate sensitivity scan found no matches for the bounded credential/secret patterns checked across the ten new candidate files. This does not turn private Git into a secrets manager; the repository's normal exclusion boundary remains unchanged.

## Candidate behavior

The new `pdf-evidence.mjs` seam composes the existing authority-bound DocumentFileReader and records a bounded evidence receipt. It adds no parser, renderer, OCR, Browser, model executor, public MCP action, write authority, or upload path.

Important invariants include:

```text
fresh read authorization at prepare/record boundaries
source workspace/path/size/hash binding
question identity binding
bounded report and final receipt
page coverage accounting
render/visual consistency checks
cross-page answers require evidence from multiple pages
returned/input state is detached from internal session state
source drift is fail-closed
no automatic model/action retry
understandingVerified=false
```

The receipt validates consistency and provenance. It does not independently verify the worker's semantic understanding or authenticate inert evidence-reference strings.

## Independent ChatGPT rerun

ChatGPT independently reran the preserved candidate's new focused test suite after Astra completed Phase 2.

The first attempt used `codex.command_exec` with `access=readOnly`. It could not create the test suite's temporary fixture directories and therefore was not accepted as candidate evidence. The same exact tests were then rerun under the already-authorized `ads-local-runtime` workspace profile, without widening authority.

Accepted result:

```text
node --test test/pdf-evidence.test.mjs test/sol-browser-audit.test.mjs

tests   36
pass    36
fail    0
skip    0
```

Composition of the 36 tests:

```text
PDF evidence/receipt candidate              34 PASS
frozen Sol discovery weakness reproductions 2 PASS
```

The two Browser audit tests intentionally reproduce defects. Their PASS result means the weakness was reproduced, not that the Browser implementation is safe.

Astra's broader non-live validation record separately preserves:

```text
existing Browser compatibility  7 / 7 PASS
existing flexible authority     7 / 7 PASS
existing document-read         11 / 11 PASS
```

Those broader results were not rerun again by ChatGPT in this preservation step and are not mislabeled as fresh independent evidence.

## Frozen Browser findings

The reviewed Phase 2 evidence preserves the GPT-5.6 Sol strengths:

```text
prepared exact actions
single-use refs
runtime generation invalidation
uncertain-result/no-blind-replay behavior
authority-bound upload path/size/SHA source checks
pre/post source revalidation
current Browser/Chrome discovery
new-tab creation and markDeliverable support
```

It also adds two concrete frozen-discovery limitations:

```text
version-root junction may escape resolved bundle root
service bytes are not independently bound by the compatibility receipt
```

And it sharpens the existing lifecycle boundary:

```text
current direct existing-tab Browser paths can claim tabs
while explicit release remains unsupported outside a genuine turn;
the defined release guard is not enforced before every claim path.
```

Therefore no Browser candidate is published by this transition.

## Document architecture result

The preferred current document direction is Browser-free:

```text
qualified small/medium whole PDF
    -> codex.document_file_link
    -> next-turn native ChatGPT PDF handling

materialization-blocked larger PDF
    -> one formal Codex document task
    -> maintained extraction/render/native image vision
    -> source-bound coverage/evidence report
    -> independent evidence review
```

Browser upload remains optional/deferred rather than part of the document critical path.

## Resource-link boundary evidence

Historical clean host interval is unchanged:

```text
highest confirmed PASS  7,417,428 bytes
lowest confirmed FAIL    7,993,210 bytes
```

The candidate's synthetic held-out fixture is:

```text
size       11,825,407 bytes
pages      8
SHA-256    be09c6065c36a9beaa32e812382b7fee7d8366dcb23f99a49e88f7306c99bc7f
base64     15,767,212 bytes
```

The frozen DocumentFileReader prepared and locally read/base64-decoded that fixture with identical SHA-256. This establishes source-reader behavior for the fixture, not ChatGPT host ingestion. It supports only the bounded conclusion that the observed historical materialization failure occurs downstream of the tested local source reader for this fixture.

## Live actions deliberately not performed

This validation did not:

```text
publish or restart Codexless
claim or mutate a Browser tab
upload a PDF
change Chrome/Browser plugin files
widen workspace authority
start the formal held-out PDF worker
publish the receipt as a public MCP action
identify the hidden resource-link host component by assertion
```

## Exact next live experiment

Run one formal Codex task against the held-out 11,825,407-byte eight-page mixed PDF using the prepared private `WORKFLOW.md` contract.

The worker must not receive the evaluator key. It must inspect all pages with maintained parsing/rendering/native local-image vision, answer the three held-out questions, and return actual page/evidence/render references.

The reviewing composition must then independently compare those answers with the hidden key and validate the source-bound receipt.

Outcome classes:

```text
PASS
    correct held-out answers + real evidence + all eight pages visually inspected
    + stable source identity + valid bounded receipt

FAIL
    completed authorized run with available tools gives wrong semantic answers,
    silently omits coverage, or cannot return inspectable evidence

AMBIGUOUS
    authority/consent/tool/environment/transport/task-state failure prevents
    a clean semantic judgment
```

No blind replacement task after uncertainty.

## Result

```text
ASTRA_PHASE2_REVIEW = PASS
ASTRA_PHASE2_NONLIVE_CANDIDATE = PASS
CHATGPT_INDEPENDENT_CANDIDATE_RERUN = PASS_36_OF_36
PRIVATE_PHASE2_PRESERVATION = PASS
a5025c2071077f719dcc59c7dfd729ee59ec34eb
RUNTIME_PRIVATE_BOOTSTRAP_SAFETY = PASS
MODEL_FREE_EXISTING_TAB_BROWSER = BLOCKED
MODEL_FREE_NEW_TAB_BROWSER = DEFER_UNPROVEN_LIFECYCLE
LOCAL_CODEX_PDF_WORKFLOW = TEST_NEXT
LIVE_SEMANTIC_PDF_QUALIFICATION = NOT_RUN
```
