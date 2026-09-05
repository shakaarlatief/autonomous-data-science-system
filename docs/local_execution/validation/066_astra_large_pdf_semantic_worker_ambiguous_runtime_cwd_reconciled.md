# Validation 066: Astra Large-PDF Semantic Worker Ambiguous, Runtime/CWD Boundary Reconciled

**Date:** 2026-09-05
**Status:** AMBIGUOUS / FIRST LIVE SEMANTIC RUN TERMINAL / ENVIRONMENT CAUSE LOCALIZED / CONTROLLED SECOND RUN READY
**Research:** Research 118 under Research 117
**Scope:** Preserve the first held-out 11.8 MB formal Codex PDF semantic-worker attempt, classify it without semantic overclaim, localize the execution/runtime ambiguity through model-free evidence, and define the smallest non-blind follow-up experiment.

## Purpose

Checkpoint 306 made one held-out formal Codex document task the exact next discriminator for the Browser-free evidence-first PDF architecture. This validation records that first real task and the subsequent environment reconciliation.

The first task did not produce a semantic PASS or FAIL. It terminated cleanly without parsing, rendering, or answering because the worker could not establish a maintained PDF execution path with enough certainty. Under the preregistered Research 118 classification rules, that outcome is `AMBIGUOUS`.

The ambiguity was then investigated model-free before considering any second task. The investigation localized a concrete execution-context problem and established an exact maintained runtime route that was not available to the first worker from its chosen nested working directory.

## Starting authority

Public repository before the live attempt:

```text
branch      v1-source-vault-bootstrap-resume
HEAD        3d2f487a9e7140aa14d055b60c8c50c10f04d0f7
checkpoint  306
```

Private Phase 2 candidate/evaluator workflow:

```text
private commit
    a5025c2071077f719dcc59c7dfd729ee59ec34eb

workflow
    .ads-private/codexless/astra-phase2-pdf-evidence-candidate/WORKFLOW.md
```

Held-out source identity:

```text
path in worker scratch
    .tmp/astra-phase2-pdf-worker-01/source.pdf

bytes
    11,825,407

SHA-256
    be09c6065c36a9beaa32e812382b7fee7d8366dcb23f99a49e88f7306c99bc7f

pages expected by evaluator
    8
```

Before the worker began, the scratch directory contained exactly one file: `source.pdf`. The evaluator key and fixture generator remained outside the worker workspace.

## Formal worker attempt 01

Task identity:

```text
requestId
    ads-astra-phase2-pdf-01

agentRef
    agent_a92fe6f3-0dcf-4f96-9b9d-96fb58ee9b0f

threadId
    01a072e7-6582-7b71-881d-5f003bf7a544

turnId
    01a072e7-666f-78a1-b4fd-30ac3433a5b7

model
    gpt-6-astra

reasoning effort
    high

cwd
    C:\Projects_Data\autonomous-data-science-system\.tmp\astra-phase2-pdf-worker-01
```

The worker was explicitly forbidden from reading repository reports, private candidate implementation, evaluator material, answer keys, or prior visual QA. It was also forbidden from Browser/upload/external storage/custom OCR/dependency installation and was told to stop rather than fabricate evidence when a maintained capability could not be established.

The turn completed normally after approximately 103 seconds. It did not enter an uncertain task state, did not require a replacement turn, and did not mutate Browser or external state.

## Worker result

The worker returned a bounded JSON result with:

```text
sourceSha256
    be09c6065c36a9beaa32e812382b7fee7d8366dcb23f99a49e88f7306c99bc7f

pageCount
    0 / explicitly unknown

pageCount parser
    not-run

text extraction
    not-run

rendering
    not-run

local-image vision
    not-run

textInspectedPages
    []

renders
    []

visuallyInspectedPages
    []

inventory
    unanswered

chart
    unanswered

scan
    unanswered
```

Its limitations explicitly stated that the maintained PDF execution runtime could not be established with certainty. The worker reported that the default execution route failed before execution with `helper_unknown_error: setup refresh had errors`; a maintained command bridge subsequently worked for preliminary checks, but the worker did not treat repository-virtualenv Python or a discovered MiKTeX Poppler executable as proven maintained runtime. It rehashed the source before and after those preliminary checks and reported no source drift.

This behavior is a useful fail-closed result. The worker did not claim visual inspection merely because a PDF Skill existed, did not infer semantic answers from the question wording, and did not silently substitute an unverified dependency.

## Preregistered classification

Research 118 defined:

```text
AMBIGUOUS
    authority / consent / tool / environment / transport / task-state failure
    before a clean semantic judgment can be made
```

Therefore:

```text
ASTRA_PDF_SEMANTIC_ATTEMPT_01 = AMBIGUOUS
SEMANTIC_CORRECTNESS = NOT_EVALUATED
SEMANTIC_FAILURE = NOT_ESTABLISHED
SOURCE_DRIFT = NOT_OBSERVED
BLIND_RETRY = NOT_PERFORMED
```

The held-out evaluator answers were not supplied to the worker. ChatGPT retained them only on the evaluator side for later independent comparison.

## Model-free runtime reconciliation

No second model task was started while the cause remained unclear.

### 1. Exact project/runtime context

`codex.project_context` against the nested scratch directory established:

```text
Codex CLI
    0.153.0

active permission profile
    ads-direct-git

approval policy
    on-request

nested runtime workspace root
    ...\.tmp\astra-phase2-pdf-worker-01

sandbox projection
    workspaceWrite

reported writableRoots
    ...\.tmp\astra-phase2-pdf-worker-01\.git

implicit Skill-routing probe
    unavailable / IMPLICIT_SKILLS_STRUCTURE_MISMATCH
```

The unavailable implicit-routing diagnostic does not mean the PDF Skill itself was absent. `codex.skill_read` independently resolved the maintained `pdf:pdf` Skill successfully.

### 2. Maintained PDF Skill contract

The exact installed Skill is:

```text
name
    pdf:pdf

bundle/version path
    openai-primary-runtime/pdf/26.904.11930/skills/pdf/SKILL.md
```

Its read workflow explicitly permits:

```text
pdftoppm from the bundled runtime
or system Poppler when available

pdfplumber or pypdf for extraction

visual review of rendered PNGs
```

No dependency installation is required when the maintained bundle already contains the needed tools.

### 3. Exact primary-runtime bundle exists and is functional

Model-free inspection found the maintained primary runtime at:

```text
C:\Users\shaka\.cache\codex-runtimes\codex-primary-runtime
```

Its `runtime.json` records:

```text
bundleFormatVersion  2
bundleVersion        26.904.11930
targetPlatform       win32
targetArch           x64
pythonVersion        3.12.14
nativeDependencies   includes poppler
```

Manifest SHA-256:

```text
83abea4f54dc8295a6ba4422131b72e71c4b3d557ce316349501b511bd6b0423
```

Exact maintained executables/dependencies were verified:

```text
primary-runtime Python
    dependencies\python\python.exe
    Python 3.12.14
    pdfplumber 0.11.9
    pypdf 6.10.0

primary-runtime Poppler
    dependencies\native\poppler\Library\bin\pdfinfo.exe
    pdfinfo 26.07.0

primary-runtime Poppler renderer
    dependencies\native\poppler\Library\bin\pdftoppm.exe
```

This bundle identity matches the maintained PDF Skill's `26.904.11930` bundle/version boundary.

### 4. Read-only parsing/extraction succeeds on the exact 11.8 MB source

Using the maintained runtime from the nested scratch context:

```text
pdfinfo source.pdf
    exit 0
    Pages: 8
    File size: 11825407 bytes

primary-runtime Python + pdfplumber
    exit 0
    pages: 8
    page-by-page extraction returned all eight pages
    source SHA-256 remained exact
```

The already-qualified first-class ADS parser independently returned:

```text
codex.document_read
    parser pdfjs-dist 5.4.624
    pageCount 8
    returnedPages 1-8
    truncation false
    source SHA-256 exact
```

Therefore the source PDF and maintained parsing/extraction dependencies are not the cause of Attempt 01's ambiguity.

### 5. Write-capable nested cwd reproduces the worker setup failure

The exact maintained `pdftoppm` renderer was then invoked model-free with `access=inherit` while the command cwd was the nested scratch directory.

Result:

```text
helper_unknown_error: setup refresh had errors
```

No rendering occurred.

This reproduces the worker's environment symptom without a model turn and localizes it to the write-capable command/sandbox setup for that nested cwd rather than to PDF validity or runtime absence.

### 6. Same maintained renderer succeeds from the registered repository root

Without changing workspace authority, the same exact maintained `pdftoppm.exe` was invoked with:

```text
cwd
    C:\Projects_Data\autonomous-data-science-system

input/output
    only .tmp\astra-phase2-pdf-worker-01\...
```

A one-page page-2 render succeeded. `codex.image_read` then returned that PNG through native ChatGPT vision, proving the scratch-file image route end to end.

A full eight-page render from the repository root also succeeded in one command. Resulting PNG sizes ranged from approximately 30 KB to 3.36 MB; image-heavy pages 3-5 were each about 3.35 MB. All eight output files were hashed successfully and then removed. The scratch directory was restored to exactly one file, `source.pdf`.

### 7. Why scratch-file rendering is preferable for this fixture

The already-qualified `codex.document_render` path still provides useful evidence:

```text
page 1 single-page render  PASS
page 2 single-page render  PASS
page 6 single-page render  PASS
```

Its receipt identifies the maintained render bundle precisely:

```text
bundleVersion        26.904.11930
runtimeManifestSha256
    83abea4f54dc8295a6ba4422131b72e71c4b3d557ce316349501b511bd6b0423
engine
    pdfjs-dist + @napi-rs/canvas
isolation
    codex-command-exec-read-only
```

However, one image-heavy page and a multi-page request reproduced `DOCUMENT_RENDER_PROTOCOL_ERROR: sandboxed renderer returned invalid JSON`. The current `document_render` implementation transports rendered PNG bytes as base64 inside the sandbox command stdout protocol. The successful Poppler scratch-file route avoids that large serialized command-output path and is therefore the more appropriate discriminator for this 11.8 MB image-heavy fixture.

This does not invalidate prior `document_render` qualification. It narrows the fixture-specific transport behavior and reinforces the Phase 2 decision to keep large rendered image bytes local rather than stream them through a large JSON/stdout envelope.

## Reconciled cause

The evidence supports the bounded diagnosis:

```text
source corruption                         NO
maintained PDF Skill absent               NO
maintained primary runtime absent         NO
maintained Poppler absent                 NO
maintained Python extraction absent       NO
read-only parsing from scratch cwd        WORKS
write-capable nested scratch cwd setup    REPRODUCES helper_unknown_error
same write from registered repo root      WORKS
all-page local scratch rendering          WORKS
native image-read of local render         WORKS
```

Therefore Attempt 01's ambiguity is best localized to the selected nested working-directory / write-capable sandbox setup, compounded by the worker not being given or discovering the exact primary-runtime bundle path. It is not evidence that the Browser-free semantic architecture itself failed.

## Controlled follow-up is not a blind retry

Research 118 forbids blindly replaying an uncertain or environment-blocked task. That rule has been followed.

A second formal worker is justified only because the blocking environment has now been independently reconciled and the next run changes the discriminating condition deliberately:

```text
Attempt 01
    formal task cwd = nested scratch directory
    maintained write-capable command setup fails

Attempt 02
    formal task cwd = registered ADS repository root
    worker remains explicitly confined by instruction to the one scratch subtree
    exact maintained primary-runtime paths and bundle identity are supplied
    no evaluator key is supplied
    no dependency install / Browser / upload is allowed
```

This is a new controlled experiment after cause localization, not an automatic replay of an uncertain model action.

## Result

```text
ASTRA_PDF_SEMANTIC_ATTEMPT_01 = AMBIGUOUS
ATTEMPT_01_TASK_STATE = TERMINAL_CLEAN
ATTEMPT_01_SOURCE_IDENTITY = STABLE
ATTEMPT_01_SEMANTIC_ANSWERS = NOT_PRODUCED
NESTED_WRITE_CWD_SETUP_FAILURE = REPRODUCED_MODEL_FREE
PRIMARY_RUNTIME_BUNDLE = QUALIFIED_FOR_CONTROLLED_FOLLOWUP
PRIMARY_RUNTIME_BUNDLE_VERSION = 26.904.11930
PRIMARY_RUNTIME_POPPLER = 26.07.0
PRIMARY_RUNTIME_PYTHON = 3.12.14
ALL_EIGHT_PAGE_SCRATCH_RENDER = PASS_MODEL_FREE
SCRATCH_IMAGE_TO_NATIVE_VISION = PASS
BLIND_RETRY = NO
CONTROLLED_SECOND_RUN = READY
```

No Browser tab was claimed, no PDF was uploaded, no external storage was used, no evaluator answer was disclosed to the worker, no runtime was published/restarted, and no dependency was installed.
