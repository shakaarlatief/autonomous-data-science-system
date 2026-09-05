# Checkpoint 308: ChatGPT Local-File Access Objective Restored

**Date:** 2026-09-05
**Status:** SCOPE CORRECTION ACCEPTED / SEMANTIC WORKER BRANCH DEACTIVATED / DIRECT CHATGPT LOCAL-FILE ACCESS RESUMED
**Checkpoint class:** ARCHITECTURE / RESEARCH CORRECTION
**Project stage:** Research 117 / Research 119 direct local-file access through Codexless
**Scope:** Preserves the project-owner clarification that the current document/file work is intended to give ordinary ChatGPT chat direct bounded access to authorized local-machine files through Codexless, without requiring manual uploads or a Codex reasoning-model intermediary. Reclassifies the Astra Phase 2 semantic-worker branch as optional future delegated-analysis research, records that prepared semantic Attempt 02 was declined before any model turn, and restores the next research route to direct model-free file/source handoff across file types.
**Authority:** Research 119 is the governing scope correction. Research 118, Validations 065-066 and Checkpoints 306-307 remain historical evidence and are not rewritten as if they had pursued the corrected objective.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-18`
**Conversation title:** `18 - Astra Architecture Review and Multimodal Handoff Continuation`
**Primary collaborator:** ChatGPT

## Corrected objective

```text
user authorizes local workspace
    -> Codexless gets bounded local file access
    -> ordinary ChatGPT chat directly receives the file or faithful source representation
    -> no manual upload required
    -> no Codex model required merely to interpret the file for ChatGPT
```

This work is developed and preserved in the ADS repository, but it is not the same question as the future ADS product's document architecture. ADS may later reuse any useful mechanisms under its own requirements.

## Manual-upload baseline

The user can already manually attach supported files to ChatGPT, including large PDFs. Therefore a pipeline where Codex reads a local file and explains it to ChatGPT is not an acceptable replacement for direct ChatGPT file access. It is a separate delegated-analysis capability.

The desired improvement over manual upload is automatic access from already-authorized local roots.

## Accepted direct-access forms

```text
PREFERRED
    actual local file becomes a ChatGPT conversation/native file input

ACCEPTABLE MODEL-FREE FALLBACK
    deterministic/faithful source representations reach ChatGPT directly
    examples: PDF text, rendered page images, slide images, workbook cells/formulas

NOT THE DEFAULT SOLUTION
    local file -> Codex reasoning model -> semantic summary/evidence -> ChatGPT
```

## Existing useful evidence retained

The correction does not discard the substantial direct-access work already completed:

```text
codex.read_many
    bounded authorized local text -> ChatGPT

codex.image_read
    authorized local PNG/JPEG/WebP -> ChatGPT native vision
    LIVE QUALIFIED

codex.document_read
    authorized local PDF -> deterministic PDF text -> ChatGPT
    LIVE QUALIFIED

codex.document_render
    authorized local PDF pages -> MCP images -> ChatGPT native vision
    LIVE QUALIFIED for the tested ordinary-page envelope

codex.document_file_link
    authorized local PDF -> MCP resource_link -> actual ChatGPT conversation PDF
    LIVE QUALIFIED within the clean host-materialization envelope
```

The clean PDF whole-file host interval remains:

```text
highest confirmed PASS  7,417,428 bytes
lowest confirmed FAIL    7,993,210 bytes
```

The exact enforcing host component is still unresolved.

## Astra work reclassified

Astra Phase 1 retains useful transport, Browser, host, upstream and runtime findings.

Astra Phase 2 produced a rigorous source-bound semantic evidence candidate, preserved privately at:

```text
a5025c2071077f719dcc59c7dfd729ee59ec34eb
```

That candidate is now classified as:

```text
OPTIONAL FUTURE DELEGATED DOCUMENT ANALYSIS / POSSIBLE ADS PRODUCT REUSE
```

not as the active solution for ChatGPT local-file access.

Research 119 identifies the scope drift explicitly: the Phase 2 prompt allowed the original file not to reach ChatGPT if another workflow could satisfy the user's task. That widened criterion changed the problem from direct access to indirect usefulness.

## Pending Astra Attempt 02 cancelled

The prepared task:

```text
requestId
    ads-astra-phase2-pdf-02-reconciled-root-cwd

short task ID
    C-CB7A8B13EB

model
    gpt-6-astra / high
```

was waiting at the Call Codex consent stage and had not started.

It was explicitly declined after the objective correction.

```text
ASTRA_SEMANTIC_ATTEMPT_02 = REJECTED_BEFORE_MODEL_TURN
METERED_MODEL_TURN_STARTED = NO
```

No second semantic qualification should be started merely to complete the obsolete branch.

## Correct next route

The active Research 117/119 question is now:

```text
For each authorized local file type,
how can ChatGPT itself obtain the actual file or a faithful model-free source representation through Codexless?
```

Priority:

```text
1. large PDF direct access beyond the current resource_link host boundary
2. generic/direct whole-file handoff opportunities for DOCX/PPTX/XLSX and other supported ChatGPT files
3. model-free format-faithful fallbacks where whole-file handoff is unavailable
4. Browser upload only as a transport fallback if cleaner supported host mechanisms are insufficient
5. Codex semantic delegation kept separate and optional
```

## Durable category boundary

```text
DIRECT CHATGPT LOCAL-FILE ACCESS
    source reaches ChatGPT directly

DELEGATED DOCUMENT ANALYSIS
    another reasoning model interprets source first

ADS PRODUCT ARCHITECTURE
    separate system-design problem
```

Future research must not silently substitute one category for another.

## Result

```text
CHATGPT_LOCAL_MACHINE_FILE_ACCESS_OBJECTIVE = RESTORED
RESEARCH_118_SEMANTIC_WORKER_AS_ACTIVE_SOLUTION = SUPERSEDED
ASTRA_ATTEMPT_02 = DECLINED_BEFORE_START
MODEL_FREE_SOURCE_HANDOFF = ACTIVE_DIRECTION
ADS_PRODUCT_ARCHITECTURE = SEPARATE_FUTURE_QUESTION
NEXT = DIRECT_CHATGPT_FILE_ACCESS_MATRIX_AND_LARGE_PDF_TRANSPORT_RESEARCH
```
