# Research 119: ChatGPT Local-Machine File Access Objective Restoration

**Date:** 2026-09-05
**Status:** ACTIVE / SCOPE CORRECTION ACCEPTED / DIRECT CHATGPT LOCAL-FILE ACCESS RESTORED AS THE RESEARCH OBJECTIVE
**Scope:** Restore the actual purpose of the current Codexless document/file work after Research 118 drifted from direct ChatGPT local-file access into Codex semantic delegation. Define what counts as success, preserve the useful transport/runtime evidence, reclassify the semantic-worker branch as optional future delegation research rather than the solution to the current problem, and establish the next direct-access research route across file types.
**Authority:** Level-2 local-capability research. The public ADS repository is being used to build, preserve and test this capability, but the capability under investigation is not the ADS product's own document-analysis architecture. Findings may later be reused by ADS if useful. The current target is ordinary ChatGPT chat gaining authorized local-machine file access through Codexless.
**Declared references:** `research:117`, `research:118`, `checkpoint:307`, `path:docs/local_execution/validation/066_astra_large_pdf_semantic_worker_ambiguous_runtime_cwd_reconciled.md`, `path:docs/OPEN_ARCHITECTURE_BACKLOG.md`

## 1. The actual objective

The project owner clarified the governing intent explicitly on 2026-09-05.

The goal of this work is:

```text
user authorizes a local folder/workspace
    -> Codexless can reach files inside that authorized local root
    -> this ordinary ChatGPT conversation can directly use those files
    -> no manual upload should be required for normal use
```

This is analogous to a capability Codex already has in its own local execution environment, but the target here is **ChatGPT chat itself**, not Codex.

The important distinction is:

```text
Codex already has authorized local-machine file access
ChatGPT normally does not
Codexless is being extended so ChatGPT can gain bounded authorized local-file access too
```

The public ADS repository is the development and preservation authority for this engineering work. That does not mean the target architecture being designed is automatically the future ADS product architecture.

The eventual ADS system has its own UI, runtime and architecture questions. ADS may choose Codex workers, direct model inputs, parsers, specialized services, or any combination that is best for the ADS product. That is a separate design problem.

## 2. Manual ChatGPT upload is the baseline comparator, not the target workflow

The user can already take a PDF or another supported file and manually attach it to ChatGPT. That gives ChatGPT direct access to the source through normal product file handling.

Therefore the current problem is not:

```text
How can any model on the machine understand this file?
```

Codex already makes that possible.

It is also not:

```text
How can the user somehow get this file into ChatGPT?
```

Manual upload already makes that possible.

The problem is specifically:

```text
How can ChatGPT gain the same practical access automatically through the user's existing local authorization,
without requiring the user to locate and upload the file manually each time?
```

A proposed solution must therefore be compared against ordinary manual attachment. If it gives ChatGPT a weaker derived interpretation when the user could simply attach the source, it is not solving the intended access problem.

## 3. What counts as direct ChatGPT access

Two forms of access can legitimately satisfy the current objective.

### A. Whole-file/native host access

Preferred when the ChatGPT host supports it:

```text
authorized local file
    -> Codexless model-free transport
    -> actual file becomes a ChatGPT conversation file/input
    -> ChatGPT can inspect it using normal native file handling
```

This is the strongest form because ChatGPT retains the source itself and can answer later questions that were not anticipated at handoff time.

`codex.document_file_link` is the clearest existing example for PDF within its currently qualified host envelope.

### B. Faithful model-free source representations delivered directly to ChatGPT

When whole-file materialization is unavailable or inefficient, a direct source representation can still satisfy the objective if no intermediary model interprets the content first.

Examples:

```text
PDF
    -> deterministic page text -> ChatGPT
    -> rendered page image -> ChatGPT vision

image
    -> exact image bytes/content -> ChatGPT vision

spreadsheet
    -> sheets/cells/formulas/metadata -> ChatGPT
    -> rendered ranges/charts -> ChatGPT vision when needed

presentation
    -> slide text/structure -> ChatGPT
    -> rendered slides -> ChatGPT vision

word-processing document
    -> structured text/tables/media -> ChatGPT
    -> rendered pages -> ChatGPT vision when layout matters
```

The reasoning remains in ChatGPT. Codexless may parse, render, package or transport the source, but it should not require a second reasoning model merely because the file is local.

## 4. What does NOT solve this objective

The following architecture is not the solution to the current local-file-access problem:

```text
local file
    -> formal Codex model task
    -> Codex reads/interprets the file
    -> Codex returns summary/evidence/findings
    -> ChatGPT reasons from Codex's interpretation
```

That is **delegated document analysis**, not direct ChatGPT local-file access.

It may be useful later for other purposes, including:

```text
parallel analysis of many documents
large batch work
specialized bounded workers
ADS product workflows
expensive local tasks intentionally delegated away from the initiating chat
```

But it must remain a separate capability and must not be presented as a replacement for source access in ordinary ChatGPT chat.

The distinction is fundamental because a semantic worker chooses what to preserve. If the user later asks about an unanticipated figure, equation, table, footnote, slide, cell or page relationship, ChatGPT may need to invoke the worker again. Direct source access avoids that unnecessary intermediary.

## 5. How the scope drift happened

Research 117 initially tracked the correct problem. It built and qualified several direct model-free paths from local authorized files into ChatGPT:

```text
codex.document_read
codex.image_read
codex.document_render
codex.document_file_read
codex.document_file_link
```

The critical whole-file finding was that MCP `resource_link` can materialize a local PDF into the ChatGPT conversation and make it fully inspectable on the next turn.

A clean host boundary was then observed:

```text
highest confirmed PASS  7,417,428 bytes
lowest confirmed FAIL    7,993,210 bytes
```

The exact hidden enforcing component remains unknown.

At that point the research question should have remained:

```text
How do we extend or complement direct ChatGPT access beyond this host-materialization boundary?
```

Instead, the Astra review was allowed to broaden the success criterion. The Phase 2 prompt explicitly allowed a solution where the original PDF did not become available to the initiating ChatGPT conversation if the user's task could be satisfied another way.

That instruction changed the objective from:

```text
ChatGPT directly gains local-file access
```

to:

```text
ChatGPT can obtain useful information from the local file somehow
```

Those goals are not equivalent.

Research 118 then produced a technically rigorous source-bound semantic-evidence worker design. The engineering quality of that candidate does not change the fact that it addresses a different problem.

The orchestration error is therefore preserved explicitly rather than attributed only to Astra:

```text
ROOT_CAUSE_OF_SCOPE_DRIFT
    the research/prompt success criterion permitted semantic substitution for direct source access

NOT_THE_ROOT_CAUSE
    Astra merely failing to follow a correct local-file-access objective
```

This distinction is important for future model collaboration. A strong model can optimize the wrong objective extremely well if the objective itself is widened incorrectly.

## 6. Disposition of Astra Phase 1 and Phase 2 work

The Astra work is not deleted or treated as worthless.

### Retain as directly useful to the real objective

Phase 1 and Phase 2 produced or reinforced useful evidence about:

```text
MCP resource_link behavior
hidden ChatGPT host materialization boundary
binary/base64 envelope hypotheses
current OpenAI/Codex file-input mechanisms
current Codexless PDF/image mechanisms
Browser upload as a possible transport fallback
Browser lifecycle constraints
current maintained PDF runtimes/renderers
large local page-image handling
source authority, hashing and revalidation invariants
```

Those findings remain relevant to direct local-file access.

### Reclassify as optional future delegation research

The following Phase 2 material is no longer the active solution path:

```text
formal Codex large-PDF semantic worker
source-bound semantic evidence receipt as a substitute for direct access
held-out semantic worker qualification as the next Research 117 discriminator
```

The private candidate at:

```text
a5025c2071077f719dcc59c7dfd729ee59ec34eb
```

remains preserved as implementation/research evidence. It may later inform intentional document-worker or ADS product architecture, but it is not required for ChatGPT to access local files.

The first formal held-out worker remains historically `AMBIGUOUS`. No second semantic worker is needed for the current objective.

## 7. Attempt 02 was explicitly cancelled before execution

A second GPT-6 Astra semantic-worker task had been prepared after Checkpoint 307 but had not started because it was awaiting the normal Call Codex consent stage.

After the objective correction, that prepared task was explicitly declined through the task decision surface.

Result:

```text
ASTRA_SEMANTIC_ATTEMPT_02
    REJECTED_BEFORE_MODEL_TURN

model turn started
    NO

metered Astra work consumed by Attempt 02
    NO
```

This prevents the obsolete semantic-delegation branch from continuing accidentally.

## 8. Existing direct-access capabilities that remain accepted

The active direct-access baseline is already substantial.

### Plain text and repository text

`codex.read_many` provides bounded model-free UTF-8 file reads inside authorized local roots.

### Images

`codex.image_read` is live-qualified:

```text
authorized local PNG/JPEG/WebP
    -> standard MCP image content
    -> ChatGPT native vision
    -> no Codex model turn
```

This directly satisfies the current goal for supported image files.

### PDF embedded text

`codex.document_read` is live-qualified:

```text
authorized local PDF
    -> deterministic bounded PDF.js extraction
    -> ChatGPT text context
    -> no Codex model turn
```

### PDF page vision

`codex.document_render` is live-qualified for its tested ordinary-page envelope:

```text
authorized local PDF page(s)
    -> maintained PDF.js + canvas rendering
    -> standard MCP image content
    -> ChatGPT native vision
    -> no Codex model turn
```

Representative image-heavy pages exposed a serialized command-output limit in this implementation. That is a transport/representation engineering problem, not a reason to insert a reasoning model.

### Whole PDF

`codex.document_file_link` is live-qualified within the clean host-materialization envelope:

```text
authorized local PDF
    -> small MCP resource_link tool result
    -> ChatGPT host materializes actual PDF
    -> next-turn normal ChatGPT full-PDF inspection
```

This is exactly the desired whole-file behavior.

The remaining problem is extending the same experience to larger PDFs and to other useful local file types.

## 9. Correct active architecture principle

The active architecture principle is now:

```text
AUTHORIZED LOCAL SOURCE
        |
        v
    CODEXLESS
        |
        +-> exact/native file handoff ------------> ChatGPT native file handling
        |
        +-> deterministic text/structure ---------> ChatGPT reasoning
        |
        +-> faithful rendered media --------------> ChatGPT native vision
        |
        +-> format-specific source representation -> ChatGPT

NO INTERMEDIARY REASONING MODEL REQUIRED BY DEFAULT
```

Codex remains useful in two separate roles:

```text
1. development tool
   Codex can help implement/test/debug Codexless itself.

2. optional delegated worker
   A future workflow may intentionally ask Codex to analyze files.
```

Neither role makes Codex part of the default file-access data path.

## 10. Separation from ADS product architecture

This distinction must survive future reconstruction.

The current work is happening in the Autonomous Data Science System development repository because Codexless and the local execution bridge are developed and preserved here.

The capability under test is nevertheless:

```text
ChatGPT chat <-> authorized local machine files
```

It is **not automatically**:

```text
future ADS application document architecture
```

For the future ADS product, the best design may use Codex, direct OpenAI file inputs, specialized document services, multiple workers, deterministic parsers, or another composition. That decision should be made from ADS product requirements at the appropriate time.

Knowledge and infrastructure produced here may be reused by ADS, but current ChatGPT-local-file research must not be distorted merely to make it look like an ADS product subsystem.

## 11. Correct next research route

Research 117 now returns to direct, model-free ChatGPT access.

The next work should build a format/capability matrix from the user-facing perspective:

```text
Can ChatGPT directly access this authorized local file through Codexless?
If yes, through what representation?
If no, what exact transport/format seam is missing?
```

Priority order:

```text
1. PDF
   preserve whole-file resource_link where qualified
   solve or bypass the >7.4-8.0 MB host-materialization gap without a reasoning-model intermediary
   retain direct text/page-image access as complementary source access

2. Images
   already direct-qualified for PNG/JPEG/WebP
   audit other practically relevant image formats only when needed

3. DOCX / other word-processing documents
   determine whether actual file materialization through a generic resource-link route can feed normal ChatGPT document handling
   otherwise expose faithful model-free structure/text/media/page renderings

4. PPTX
   prefer actual file handoff when possible
   otherwise direct slide structure/text + rendered slide images to ChatGPT

5. XLSX / spreadsheet formats
   prefer actual file handoff when possible
   otherwise direct workbook/sheet/cell/formula semantics plus visual chart/range representations

6. other local file families
   classify from real user need rather than building generic adapters speculatively
```

The research should first look for reusable native OpenAI/ChatGPT/MCP mechanisms before adding custom format implementations.

## 12. Large-PDF question restated correctly

The 7.4-8.0 MB materialization boundary remains a real direct-access problem.

The relevant questions are now:

```text
Can the hidden resource_link host boundary be avoided through another supported file/resource transport?
Can a large local PDF be split into native ChatGPT-consumable source parts without semantic interpretation?
Can rendered page images be exposed directly to ChatGPT without the current stdout/base64 bottleneck?
Can a generic ChatGPT file-attachment/resource mechanism accept local authorized bytes beyond the current MCP resource-link path?
Can Browser upload safely automate the same ordinary ChatGPT file control only as a transport fallback, if no cleaner host primitive exists?
```

The wrong question for this workstream is:

```text
Can Codex understand the large PDF well enough that ChatGPT no longer needs access to it?
```

That question belongs to optional delegated-document-analysis research.

## 13. Acceptance criteria for the overall local-file capability

A professional end state should let the user do something like:

```text
"Read the PDF in my authorized Machine Learning folder."
"Compare this local spreadsheet with that local report."
"Look at slide 14 of the presentation in my authorized folder."
```

without manually attaching the files first.

ChatGPT should then be able to obtain the source itself or faithful source representations through bounded Codexless tools.

The user should not need to care whether the internal direct representation is:

```text
native conversation file
bounded text
page image
slide image
sheet/cell structure
another format-faithful representation
```

as long as ChatGPT itself receives the source information directly and the bridge preserves authority, provenance, fidelity and fail-closed behavior.

## 14. Durable guardrail

Future collaborators must preserve this distinction:

```text
DIRECT CHATGPT LOCAL-FILE ACCESS
    source or faithful source representation reaches ChatGPT model context directly
    no intermediary reasoning model required

DELEGATED FILE ANALYSIS
    another model reads the source and returns an interpretation
    useful separate capability, but not a substitute for direct access

ADS PRODUCT ARCHITECTURE
    separate future system-design question
    may reuse either or both depending on ADS requirements
```

If a proposed solution changes categories, that must be stated explicitly before it becomes the active architecture.

## 15. Current classification

```text
CHATGPT_LOCAL_MACHINE_FILE_ACCESS_OBJECTIVE = RESTORED
MANUAL_UPLOAD = BASELINE_COMPARATOR_NOT_TARGET_WORKFLOW
CODEX_MODEL_AS_DEFAULT_FILE_INTERMEDIARY = REJECT_FOR_THIS_OBJECTIVE
MODEL_FREE_SOURCE_HANDOFF = PREFERRED
NATIVE_WHOLE_FILE_HANDOFF = PREFERRED_WHEN_SUPPORTED
MODEL_FREE_FAITHFUL_SOURCE_REPRESENTATION = ACCEPTABLE_FALLBACK
ASTRA_PHASE2_SEMANTIC_RECEIPT = PRESERVE_AS_OPTIONAL_FUTURE_DELEGATION_RESEARCH
ASTRA_SEMANTIC_ATTEMPT_02 = DECLINED_BEFORE_START
ADS_PRODUCT_DOCUMENT_ARCHITECTURE = SEPARATE_FUTURE_QUESTION
NEXT_RESEARCH = DIRECT_CHATGPT_FILE_ACCESS_MATRIX_AND_LARGE_PDF_TRANSPORT_GAP
```

## 16. Checkpoint 309 direct-host capability discriminator

A corrected-objective Astra review subsequently converged on the same category boundary: actual/native file handoff is preferred, deterministic model-free source representations are valid fallbacks, and semantic model delegation is separate. Before running its proposed multi-native-PDF split experiment, ChatGPT identified one narrower supported-host question that should be resolved first.

Current MCP Apps protocol surfaces allow a host to advertise `updateModelContext` modalities, including `resourceLink`. Current OpenAI Plugin documentation also acknowledges files returned by tool file references, but no general custom-MCP mechanism has been established for minting a ChatGPT-managed file ID from arbitrary local bytes. The distinction is therefore:

```text
protocol / product surface exists
    !=
this exact ChatGPT MCP host advertises and accepts it
```

To avoid inferring support from documentation alone, a temporary read-only MCP Apps host-capability probe was implemented and qualified. It performs only the standard `ui/initialize` handshake and records a narrow whitelist of advertised host capability metadata. It reads no local document bytes, invokes no Browser, calls no file picker/upload helper, and does not invoke `ui/update-model-context` during discovery.

The probe was live-published as:

```text
Codexless version
    0.1.1-preview.15-host-capability-probe

source tool count
    59
```

Direct post-restart evidence returned that exact version/tool count and Secure MCP Tunnel `/readyz = ready`. The one-time exact-root runtime workspace admission used for publication was removed again immediately afterward; the durable workspace registry returned to its normal four-workspace shape.

The user then refreshed `ADS Codexless Local Bridge` in the same persistent ChatGPT conversation. ChatGPT-side tool rediscovery still exposed the older callable projection and did not show the three newly published probe tools. This is classified as another same-conversation projection-staleness reproduction, not a live-server publication failure.

The exact next experiment is therefore a fresh disposable ChatGPT conversation:

```text
fresh chat
    -> verify codex.host_capability_probe is projected
    -> run the read-only MCP App probe
    -> read codex.host_capability_probe_result
    -> classify updateModelContext.resourceLink
```

Decision rule:

```text
ADVERTISED
    -> qualify one tiny known PDF resourceLink through ui/update-model-context
    -> this remains direct source access
    -> do not infer large-file success merely from capability advertisement

NOT_ADVERTISED
    -> stop this host-model-context route for the current ChatGPT host
    -> proceed to the deterministic multi-native-PDF document_file_link experiment
```

Primary evidence: Validation 067 and Checkpoint 309.

Updated classification:

```text
HOST_CAPABILITY_PROBE = LIVE
SAME_CHAT_TOOL_PROJECTION = STALE
UPDATE_MODEL_CONTEXT_RESOURCE_LINK = NOT_YET_OBSERVED
NEXT_RESEARCH = FRESH_CHAT_HOST_CAPABILITY_HANDSHAKE
```

## 17. Checkpoint 310 fresh-host discriminator resolved

The fresh disposable ChatGPT conversation projected the newly published probe tools successfully and mounted the MCP App. The widget visibly completed the standard `ui/initialize` handshake and displayed the current ChatGPT host capability object.

Observed host capability core:

```text
updateModelContext = {}
message = {}
downloadFile = absent/null
serverResources = advertised
serverTools = advertised
logging = advertised
openLinks = advertised
```

The MCP Apps capability contract models `updateModelContext` as a set of independently optional supported content modalities. `resourceLink?: {}` is the explicit indicator that resource-link content blocks are supported. The current host advertised `updateModelContext` itself but no `resourceLink` property.

Accepted result:

```text
UPDATE_MODEL_CONTEXT = ADVERTISED
UPDATE_MODEL_CONTEXT_RESOURCE_LINK = NOT_ADVERTISED
```

The proposed tiny-PDF `resourceLink -> ui/update-model-context` qualification is therefore not run on this host. Protocol availability remains useful upstream evidence, but the current ChatGPT host advertisement does not expose the required modality.

The later model-visible result tool returned `{ "status": "not_recorded" }` twice even though the widget visibly reported a recorded host snapshot. Source review and a new focused regression localize that discrepancy to the diagnostic itself: the HTTP runtime constructs a fresh `McpServer` per request, while the probe's default store is created inside each server registration. Two independent registrations therefore receive isolated stores. The raw `ui/initialize` snapshot remains valid host evidence; only the convenience persistence/readback path was defective.

The Checkpoint 309 branch now resolves to:

```text
NOT_ADVERTISED
    -> close the resourceLink update-model-context candidate for the current host
    -> return to deterministic multi-native-PDF document_file_link qualification
```

The next experiment must preserve direct-source semantics:

```text
large authorized PDF
    -> deterministic valid PDF parts
    -> each part below the known clean materialization PASS envelope
    -> codex.document_file_link for all ordered parts
    -> one ordinary ChatGPT conversation receives the native parts
    -> ChatGPT verifies access across the complete ordered page set
```

A PASS proves multi-part native source access. It does not prove unchanged whole-file materialization above the current host boundary.

Primary evidence: Validation 068 and Checkpoint 310.

Updated classification:

```text
HOST_CAPABILITY_PROBE = QUALIFICATION_COMPLETE
FRESH_CHAT_TOOL_PROJECTION = PASS
UPDATE_MODEL_CONTEXT = ADVERTISED
UPDATE_MODEL_CONTEXT_RESOURCE_LINK = NOT_ADVERTISED
PROBE_RESULT_STORE = REQUEST_LOCAL_BUG
NEXT_RESEARCH = DETERMINISTIC_MULTI_NATIVE_PDF_DOCUMENT_FILE_LINK
```

## 18. Checkpoint 311 multi-native-PDF direct-access qualification passed

The deterministic multi-native-PDF fallback has now been tested end to end on the established 11,825,407-byte eight-page source.

A naive two-part split was deliberately rejected because pages 1-4 alone produced approximately 7.87 MiB, above the highest clean whole-file host PASS of 7,417,428 bytes. A deterministic contiguous-range size search under that conservative ceiling selected the minimum three-part partition:

```text
source pages 1-3    3,936,427 bytes
source page 4       3,935,151 bytes
source pages 5-8    3,955,281 bytes
```

The model-free splitter reproduced all output hashes exactly across reruns. Model-free Poppler rendering of the original and split parts produced exact image-hash equality for all eight pages.

Each part was then handed off through the already-qualified `codex.document_file_link` mechanism in the same ordinary ChatGPT conversation. All three resource-link calls succeeded and the ChatGPT host materialized all three as actual PDF files in the conversation file layer. Ordinary ChatGPT-side PDF Skill inspection reported the expected 3 + 1 + 4 page structure and ChatGPT directly inspected source content across all parts.

Cross-part source reasoning was also verified. Page 1 contains opening inventory 137 units and page 8 contains closing inventory 219 units, allowing ChatGPT itself to compute the source-supported +82 unit change even though those pages reside in different materialized PDF parts.

Accepted result:

```text
MULTI_NATIVE_PDF_DIRECT_ACCESS = PASS
PART_GENERATION_DETERMINISTIC = PASS
PAGE_RENDER_FIDELITY = 8/8 EXACT
CHATGPT_HOST_MATERIALIZATION = 3/3 PASS
CHATGPT_NATIVE_PDF_INSPECTION = PASS
CROSS_PART_REASONING = PASS
SEMANTIC_INTERMEDIARY = NONE
UNCHANGED_OVERSIZED_WHOLE_FILE_MATERIALIZATION = NOT_ESTABLISHED
```

This changes the architecture status materially. Deterministic native PDF splitting is no longer speculative; it is a proven direct-source fallback for this oversized fixture.

It should remain subordinate to unchanged whole-file handoff because splitting can weaken document-wide semantics such as signatures, outlines, links, forms, attachments, and the user's single-file experience. The next decision is therefore whether to productize this fallback now or first compare its UX/document-container trade-offs against the heavier Browser-upload fallback and any newly available supported native host primitive.

Primary evidence: Validation 069 and Checkpoint 311.

Updated classification:

```text
OVERSIZED_PDF_DIRECT_SOURCE_FALLBACK = QUALIFIED
PREFERRED_WITHIN_HOST_ENVELOPE = UNCHANGED_NATIVE_WHOLE_FILE_RESOURCE_LINK
FALLBACK_BEYOND_HOST_ENVELOPE = DETERMINISTIC_NATIVE_PDF_PARTS
BROWSER_UPLOAD = LATER_HEAVIER_FALLBACK / NOT_YET_REQUIRED
NEXT_RESEARCH = PRODUCTIZATION_DECISION_AND_FILE_TYPE_EXTENSION
```

## 19. Checkpoint 312 Machine Learning generalization narrows native splitting

The Checkpoint 311 fallback was then tested conceptually and model-free against the larger PDFs in the authorized read-only `machine-learning` workspace.

Fifteen PDFs exceed the 7,417,428-byte highest clean whole-file PASS. Several are much larger, including approximately 75.2 MiB `51.Deep Learning2.annotated.pdf` and 55.7 MiB `11.Introduction.annotated.pdf`.

The important new result is that page-range splitting alone is not universal. Model-free single-page serialization found individual source pages whose native one-page PDFs already exceed a 7,000,000-byte planning target:

```text
11.Introduction.annotated.pdf page 12    17,597,874 bytes
51.Deep Learning2.annotated.pdf page 16  15,944,609 bytes
71.Reinforcement Learning.annotated.pdf page 18  14,059,747 bytes
41.DeepLearning1.annotated.pdf page 39   14,048,969 bytes
21.Methodology1.annotated.pdf page 27    10,025,200 bytes
Transformers.annotated.pdf page 32       9,422,430 bytes
```

Basic pypdf content-stream compression/deduplication did not materially shrink the worst Deep Learning 2 page. Inspection showed many embedded image resources, so the page payload itself is genuinely large.

The current `codex.document_read` and `codex.document_render` tools also reject whole source PDFs above 33,554,432 bytes before page selection. Therefore those tools cannot currently serve as the oversized-single-page fallback for a 40-75 MiB source without first isolating the page internally.

The direct-source hierarchy is now:

```text
unchanged native whole file
    -> preferred when host-qualified

native PDF page-range parts
    -> proven when all resulting parts fit

single native page still oversized
    -> hybrid faithful model-free representation required
    -> isolate exact page internally
    -> deliver page text plus high-fidelity visual/source representation directly to ChatGPT
    -> no reasoning-model intermediary

Browser upload
    -> remains heavier fallback/comparison route
```

The production mechanism should not require writing split files back into the source workspace. `machine-learning` intentionally has read-only authority. Generated parts/renders should be Codexless-owned ephemeral resources or deterministically regenerated from verified source identity.

Primary evidence: Validation 070 and Checkpoint 312.

Updated classification:

```text
NATIVE_PDF_SPLITTER = QUALIFIED_BUT_NOT_UNIVERSAL
OVERSIZED_SINGLE_NATIVE_PAGE = CONFIRMED_REAL_CASE
READ_ONLY_SOURCE_WORKSPACE = MUST_REMAIN_SUPPORTED
NEXT_RESEARCH = HYBRID_OVERSIZED_SINGLE_PAGE_DIRECT_SOURCE_ROUTE
```

## 20. Checkpoint 313 renderer-only large-source route published

The first bounded oversized-single-page route is now implemented and source-published for live qualification. The representative source remains `51.Deep Learning2.annotated.pdf` at 78,874,939 bytes, where page 16 alone serializes to a 15,944,609-byte native one-page PDF.

A model-free feasibility run using the same maintained PDF.js + `@napi-rs/canvas` stack as `codex.document_render` succeeded directly against the read-only 78,874,939-byte source:

```text
page 16 render at 150 DPI
    dimensions    1240 x 1755
    PNG bytes     583,130
    PNG SHA-256   aca9cfadbfcb99382e22a2472495f26d1ab097922ce9406d66a8121810a56023

page 16 embedded text
    characters    17,999
    SHA-256       6829039204ef86c6204e3ca2d8c3b74e77b94c07ec8d7fc885c5a3e15ae52ba2
```

The combined render/text probe also passed under a 256 MiB Node heap. This shows that the existing 32 MiB failure was a source-admission-policy limitation rather than a fundamental inability of the maintained runtime to process the page.

The chosen implementation is deliberately narrow. `codex.document_read` remains unchanged at its current 32 MiB source ceiling. Only `document-renderer.mjs` receives a separate 96 MiB source ceiling. The renderer parent no longer retains the entire source twice for identity verification; it validates the PDF header from the first 1,024 bytes and computes SHA-256 in bounded 1 MiB chunks before and after the existing sandboxed render. Canonical path, size, mtime, dev/inode and SHA drift checks remain in force, while existing per-page and aggregate PNG ceilings remain 4 MiB and 8 MiB respectively.

Static candidate tests passed, the reviewed source was published to the installed Codexless tree with a hash-verified backup, and the installed document-render regression is 10/10 PASS. The temporary exact-root runtime publication admission was removed again after verification; the normal Machine Learning workspace remains read-only.

The currently running Codexless process still has the pre-publication module loaded. Therefore no end-to-end host claim is made yet. The exact next experiment is the canonical controlled Codexless/tunnel restart followed by the unchanged existing `codex.document_render` tool on Machine Learning page 16 in the same ChatGPT conversation. No Plugin refresh is required because the tool schema and tool count did not change.

Primary evidence: Validation 071 and Checkpoint 313.

Updated classification:

```text
LARGE_PDF_PAGE_RENDER_FEASIBILITY = PASS
RENDERER_96MIB_SOURCE_CANDIDATE = STATIC_PASS
LIVE_SOURCE_PUBLICATION = PASS
SOURCE_WORKSPACE_WRITE = NONE
TOOL_SCHEMA_CHANGE = NONE
END_TO_END_CHATGPT_PAGE16_RENDER = PENDING_RESTART
NEXT_RESEARCH = RESTART_THEN_DOCUMENT_RENDER_PAGE16
```

## 21. Checkpoint 314 oversized-page direct vision qualifies end to end

After the canonical controlled restart, ordinary ChatGPT invoked the unchanged existing `codex.document_render` tool on page 16 of the real 78,874,939-byte `51.Deep Learning2.annotated.pdf` source in the read-only Machine Learning workspace.

The call succeeded and returned:

```text
source SHA-256
    3872d5b3957d4313ab154a8405222d47098dda50657b660330ea0eecdce24110

page 16
    media type    image/png
    dimensions    1240 x 1755
    bytes         583,130
    SHA-256       aca9cfadbfcb99382e22a2472495f26d1ab097922ce9406d66a8121810a56023
```

The live returned image hash exactly matched the pre-restart feasibility render. More importantly, the standard MCP image content reached ChatGPT itself and was directly inspected with native vision. Visible content included the StyleGAN architecture diagram, `latent vector` and `per-layer noise` labels, generated-face examples, and the lower `changing the latent vector` section. This is direct image evidence, not a semantic receipt and not reconstructed from earlier extracted text.

The successful live path is therefore:

```text
78,874,939-byte authorized local PDF
    -> read-only Machine Learning authority
    -> model-free PDF.js + canvas page render
    -> 583,130-byte standard MCP PNG
    -> ordinary ChatGPT native vision
```

No manual upload, Browser, OCR, source-workspace write, semantic worker, or Codex reasoning-model turn was used.

This closes the exact oversized-single-page visual question raised by Checkpoint 312 for sources within the 96 MiB renderer ceiling. It does not yet solve every large-PDF concern. In particular, `codex.document_read` still has the separate 32 MiB source ceiling, and no automatic hybrid dispatcher yet chooses among unchanged whole-file handoff, native PDF splitting and rendered-page fallback.

Primary evidence: Validation 072 and Checkpoint 314.

Updated classification:

```text
OVERSIZED_SINGLE_PAGE_DIRECT_VISION = QUALIFIED
LARGE_PDF_PAGE16_DIRECT_RENDER = PASS
SOURCE_BYTES = 78874939
PAGE16_NATIVE_PDF_BYTES = 15944609
PAGE16_RENDER_BYTES = 583130
CHATGPT_NATIVE_VISUAL_INSPECTION = PASS
READ_ONLY_SOURCE_WORKSPACE = PASS
MANUAL_UPLOAD = NONE
BROWSER = NONE
REASONING_MODEL_INTERMEDIARY = NONE
NEXT_RESEARCH = GENERALIZE_HYBRID_POLICY_AND_LARGE_SOURCE_TEXT_PATH
```

## 22. Checkpoint 315 large-source embedded-text route published

The corresponding large-source `codex.document_read` gap is now addressed in source and awaiting only a controlled runtime restart plus the real page-16 qualification.

Before publication, the live first-class tool was called on page 16 of the 78,874,939-byte `51.Deep Learning2.annotated.pdf` source and failed before page selection:

```text
DOCUMENT_SIZE_LIMIT
limitBytes  33,554,432
sizeBytes   78,874,939
```

This proves the old restriction was the whole-source admission ceiling, not the selected page size.

The candidate keeps the existing public `codex.document_read` contract and read-only authority but raises its bounded source ceiling from 32 MiB to 96 MiB. The isolated PDF.js child was also tightened for large inputs: the server-owned source size is passed through private protocol metadata, the child allocates one exact bounded input buffer, rejects length mismatch, and gives PDF.js a zero-copy `Uint8Array` view over that buffer.

Pre-restart evidence:

```text
candidate syntax                         PASS
focused >32 MiB source tests             3/3 PASS
live source publication                  PASS
installed valid source bytes             36,700,855
installed parser                          pdfjs-dist 5.4.624
installed >32 MiB text extraction smoke  PASS
public tool schema/count change          NONE
source-workspace write                    NONE
reasoning-model intermediary              NONE
```

The temporary installed-runtime workspace admission was removed after publication/testing. The normal Machine Learning workspace remains strictly read-only.

The running Codexless process still has the old module loaded, so no real 78.9 MB end-to-end claim is made yet. The exact next experiment is the canonical controlled restart followed by same-chat `codex.document_read` on page 16 with `maxCharacters=25000`. No Plugin refresh is required.

Primary evidence: Validation 073 and Checkpoint 315.

Updated classification:

```text
LARGE_SOURCE_TEXT_ADMISSION_96MIB = SOURCE_PUBLISHED
INSTALLED_GT32MIB_PDFJS_TEXT_SMOKE = PASS
REAL_78MB_PAGE16_DIRECT_TEXT = PENDING_RESTART
NEXT_RESEARCH = RESTART_THEN_DOCUMENT_READ_PAGE16
```
