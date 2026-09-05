# Research 118: Astra Phase 2 Browser-Free PDF Evidence Architecture Reconciliation

**Date:** 2026-09-05
**Status:** COMPLETE / PHASE 2 ARCHITECTURE RECONCILIATION / LIVE SEMANTIC QUALIFICATION PENDING
**Scope:** Reconcile the independent GPT-6 Astra Phase 1 architecture challenge with the frozen GPT-5.6 Sol Browser implementation, current ADS document requirements, current installed Codex/App Server mechanisms, and current public Codexless evidence. Select the smallest supported next architecture and preserve the non-live source-bound PDF evidence candidate without claiming live semantic qualification.
**Authority:** Level-2 architecture research under Research 113/117. The public ADS repository remains the sole project-development authority. The private local-runtime candidate is implementation evidence only and is not a live Codexless publication or accepted production surface.
**Declared references:** `research:113`, `research:117`, `checkpoint:305`, `path:docs/local_execution/validation/064_gpt56_browser_compatibility_baseline_blocked_direct_call_cleanup.md`, `path:docs/local_execution/LOCAL_RUNTIME_REPOSITORY.md`, `path:docs/OPEN_ARCHITECTURE_BACKLOG.md`

## 1. Why Phase 2 was run

Checkpoint 305 intentionally froze the GPT-5.6 Sol Browser baseline before giving GPT-6 Astra access to the private implementation. Astra Phase 1 therefore reviewed the public architecture and current upstream mechanisms independently. Only after that independent pass was complete was the private local-runtime repository added to the same Astra project/thread for Phase 2.

The purpose was not to make either model "win". The design was:

```text
independent Astra architecture challenge
-> expose the actual frozen Sol implementation
-> compare both against current upstream and ADS evidence
-> retain the strongest supported mechanisms
-> remove or defer unsupported complexity
-> implement only a candidate whose assumptions can be tested non-live
```

The frozen Sol comparison boundary remained:

```text
private repository commit
e45a5de7ddae7f8158445b4b71d9c5f70cab8a2c

public checkpoint
305
```

The completed Phase 2 candidate and review are now preserved in the private local-runtime repository at:

```text
a5025c2071077f719dcc59c7dfd729ee59ec34eb

.ads-private/codexless/astra-phase2-pdf-evidence-candidate/
```

That private preservation passed the runtime repository's bounded push integrity gate:

```text
RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
postflightOk=true
retried=false
local HEAD == origin/main
```

## 2. Browser lifecycle reconciliation

Astra confirmed that Sol had already implemented substantial Browser safety work that Phase 1 could not see:

```text
current installed Browser/Chrome plugin discovery
exact action preparation and single-use references
runtime-generation invalidation
source path/size/SHA-256 binding for uploads
pre/post source revalidation
uncertain mutation classification
no blind replay
new-tab creation through browser.tabs.new()
markDeliverable handling
confirmation-policy integration
```

Those mechanisms remain valuable evidence and several invariants should be reused if Browser returns later.

Phase 2 also narrowed what the frozen Browser qualification established.

### Existing user tabs

The current direct Browser executor recognizes that finalize-absent current Browser runtimes do not expose an explicit release/unclaim primitive. It can report cleanup as unavailable / turn-cleanup-unproven. However, the defined release-availability guard is not enforced before every path that calls `browser.user.claimTab()`.

Therefore the safe public interpretation is stronger than "cleanup is reported honestly":

```text
model-free direct existing-tab Browser operations
    BLOCKED

reason
    no supported explicit release/unclaim
    + no genuine Codex turn lifecycle
    + pre-claim enforcement gap in the frozen candidate
```

No historical result is rewritten. Validation 064 remains a valid 7/7 compatibility qualification for the exact discovery contract it tested, not a live claimed-tab safety qualification.

### Agent-created new tabs

Sol already implemented a prepared new-tab route using `browser.tabs.new()`, navigation, and `markDeliverable()`. This means the idea itself was not new in Astra Phase 1.

Phase 2 nevertheless rejects publishing a separate model-free new-tab lifecycle now. Creating a new tab avoids claiming an existing user tab, but it still creates externally visible state whose ownership, interruption, crash, transport-loss, marking, and reconciliation semantics must be supported. Individual availability of `tabs.new()` and `markDeliverable()` does not prove a complete lifecycle outside a genuine Codex turn.

Accepted disposition:

```text
MODEL_FREE_EXISTING_TAB_BROWSER = BLOCKED
MODEL_FREE_NEW_TAB_BROWSER = DEFER_UNPROVEN_DIRECT_CALL_LIFECYCLE
GENUINE_TURN_BROWSER = SUPPORTED_NORMAL_LIFECYCLE_ADS_INTEGRATION_UNQUALIFIED
```

If Browser mutation becomes necessary later, one genuine-turn lifecycle is preferred over maintaining a second direct-call mutation lifecycle.

## 3. Two additional frozen Sol discovery weaknesses

Phase 2 added two synthetic regression reproductions against the frozen Browser discovery implementation:

1. a version-root junction outside the resolved bundled plugin root can still be accepted;
2. changing Browser service bytes at the same path does not change the compatibility result because the current binding hashes the client but not the service bytes.

These tests deliberately pass when they reproduce the weakness. They are not Browser safety passes.

The correct historical interpretation is:

```text
Validation 064 focused compatibility suite       7 / 7 PASS
new frozen defect reproductions                  2 / 2 REPRODUCED
historical Validation 064 rewritten              NO
future reuse requires containment/binding repair YES
```

## 4. Document architecture changed from transport-first to evidence-first

The most important Phase 2 conclusion is that ADS should not make Browser upload or original-file materialization the universal requirement for large documents.

The preferred architecture is now:

```text
within clean-qualified host materialization range
    -> codex.document_file_link
    -> next-turn native ChatGPT PDF handling

outside that qualified range or when host materialization fails
    -> one genuine formal Codex document task
    -> maintained extraction/rendering/native local-image vision
    -> explicit source-bound coverage and evidence report
    -> independent ChatGPT-side review of cited evidence/supporting pages

Browser upload
    -> optional deferred fallback only if a real downstream requirement needs it
```

This preserves exact source identity and inspectability without requiring every original PDF to become a ChatGPT attachment.

It does not claim that semantic evidence can replace an original file for every downstream use. If the requirement is file portability, exact PDF interactions/forms, or third-party processing, a native full-file path may still be required.

## 5. Resource-link boundary interpretation

The clean host materialization evidence remains unchanged:

```text
highest confirmed clean PASS  7,417,428 bytes
lowest confirmed clean FAIL    7,993,210 bytes
```

This remains an observed interval, not a universal ChatGPT or MCP maximum.

The private DocumentFileReader can prepare and locally read/decode a synthetic 11,825,407-byte PDF with identical SHA-256. Its base64 representation is 15,767,212 bytes. Therefore the observed 7-8 MB failure is downstream of the tested source preparation/read layer for that fixture.

The historical boundary also maps to base64 sizes of approximately:

```text
7,417,428 raw bytes -> 9,889,904 base64 bytes
7,993,210 raw bytes -> 10,657,616 base64 bytes
```

A decimal 10 MB and a 10 MiB serialized-envelope threshold both fall inside that interval, making a serialized/buffered downstream boundary plausible. No host trace identifies the enforcing component. Candidate locations include MCP HTTP response buffering, gateway handling, ChatGPT MCP host processing, attachment ingestion, or another hidden materialization layer.

Do not transfer ordinary ChatGPT upload limits or another Codex MCP path's limits to this route by inference.

## 6. Non-live PDF evidence candidate

Astra implemented one deliberately small internal seam in the private repository:

```text
src/pdf-evidence.mjs
```

It does not implement a new parser, renderer, OCR engine, model executor, Browser route, public MCP action, upload path, or task ledger.

The candidate composes the existing authority-bound `DocumentFileReader.prepareResource()` around a worker-reported evidence contract. It records and validates:

```text
source workspace/path/size/SHA-256 identity
fresh read authorization at record time
question identity
reported page count and method references
text-inspected pages
rendered pages and hashes
visually inspected pages
evidence rows with page references
cross-page evidence requirements
answered/unanswered questions
missing page coverage
supporting-page request metadata
bounded report/output size
```

It deliberately keeps:

```text
understandingVerified = false
observationAssurance = WORKER_REPORTED_NOT_INDEPENDENTLY_VERIFIED
```

The receipt is an integrity/coverage object, not a semantic truth certificate. Actual cited extraction/render/vision evidence must still be inspected independently.

## 7. Verification completed before live qualification

Astra's Phase 2 report records 61 behavioral checks across the new receipt candidate and reused frozen regressions. ChatGPT independently reran the new candidate suite after review and reproduced:

```text
34 / 34 PDF evidence receipt tests PASS
2 / 2 frozen Sol discovery defect reproductions PASS
36 / 36 combined new-candidate checks PASS
```

The broader Phase 2 record also preserves:

```text
existing Browser compatibility     7 / 7 PASS
existing flexible authority        7 / 7 PASS
existing document-read            11 / 11 PASS in owned dependency layout
```

The validation is non-live. No real Browser tab was claimed, no PDF was uploaded, no installed runtime was published/restarted, and no formal document-understanding worker was run.

## 8. Exact next experiment

The next discriminating experiment is one genuine formal Codex task on a held-out synthetic mixed PDF above the observed resource-link failure interval.

Fixture preserved outside Git payloads:

```text
size       11,825,407 bytes
pages      8
SHA-256    be09c6065c36a9beaa32e812382b7fee7d8366dcb23f99a49e88f7306c99bc7f
```

The worker must not receive the evaluator key or prior visual QA. It must independently:

```text
hash the source
establish page count with a parser
extract page text with explicit coverage/truncation
render every page
inspect every page through native local-image vision
answer one first-vs-last cross-page question
answer one chart question
answer one raster/scanned visual question
return real evidence references and render hashes
report limitations and incomplete coverage honestly
rehash/revalidate the source
```

The reviewing ChatGPT-side workflow then compares the worker's answers against the held-out key and independently inspects the cited evidence.

Classification rules:

```text
PASS
    correct held-out answers + real supporting evidence + eight-page visual coverage
    + matching source identity + bounded valid receipt

FAIL
    authorized completed run with available tools produces wrong answers,
    silent coverage omissions, or unusable evidence

AMBIGUOUS
    authority/consent/tool/environment/transport/task-state failure before
    a clean semantic judgment can be made
```

One logical task only. An uncertain or timed-out task must be reconciled, not blindly replayed.

## 9. Current disposition

```text
KEEP
    codex.document_file_link within exact clean-qualified range/context
    codex.document_read
    codex.document_render
    codex.image_read
    authority-bound source hashing/revalidation
    pagewise supporting evidence
    Browser confirmation policy for any future supported Browser executor

NARROW
    embedded codex.document_file_read
    Browser plugin discovery before future reuse
    Browser repair Skill
    direct mcpServer/tool/call Browser work to non-claiming discovery/inventory only

REPLACE
    direct existing-tab Browser mutation with genuine-turn ownership if Browser is needed

DEFER
    resource-link large-file scaling beyond observed host qualification
    model-free new-tab Browser mutation
    Browser upload
    PDF-part packaging
    external connector file plane

TEST NEXT
    local formal Codex PDF semantic workflow with source-bound evidence receipt

REJECT
    custom OCR merely to solve this boundary
    custom renderer merely to evade outer transport behavior
    fake turn completion/release workarounds
```

## 10. Claim boundary

Phase 2 closes the architecture-review obligation AB-028, but does not close Research 117.

Accepted now:

```text
ASTRA_PHASE2_ARCHITECTURE_REVIEW = COMPLETE_WITH_NONLIVE_CANDIDATE
PREFERRED_DOCUMENT_ARCHITECTURE = BROWSER_FREE_QUALIFIED_PRIMITIVES_WITH_SOURCE_BOUND_EVIDENCE
MODEL_FREE_EXISTING_TAB_BROWSER = BLOCKED
MODEL_FREE_NEW_TAB_BROWSER = DEFER_UNPROVEN_DIRECT_CALL_LIFECYCLE
LOCAL_CODEX_PDF_WORKFLOW = TEST_NEXT_WITH_COVERAGE_AND_EVIDENCE_RECEIPT
```

Not accepted yet:

```text
large-PDF semantic worker workflow       LIVE QUALIFIED
receipt                                  semantic verification
Browser upload                            necessary or supported fallback
resource-link hidden component/threshold exactly identified
new Browser candidate                    publishable
```

The next project boundary is empirical: run the single held-out 11.8 MB semantic document experiment before integrating the receipt into live Codexless or reopening Browser mutation work.
