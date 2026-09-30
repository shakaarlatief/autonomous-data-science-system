# Research 413: Key Author A P6A First-Run HOLD and Transcript-Slug Remediation

**Date:** 2026-09-30
**Status:** P6A HOLD / MECHANICAL TRANSCRIPT-RESOLUTION DEFECT DIAGNOSED / REMEDIATION FROZEN BEFORE RESUMPTION
**Parent:** Research 412
**Scope:** Preserve the first live P6A HOLD, diagnose the mechanical failure without inspecting semantic output, and prospectively freeze the minimal remediation before any replacement semantic attempt.
**Authority:** Mechanical runner remediation only. This record does not alter Research 410 semantics, P6A candidate-gap criteria, P6B evidence criteria, P6C grouping criteria, evidence floors, hidden controls, Key A canonical assembly, Key Author B, scoring, successor implementation, migration, or authority switching.

## 1. First live P6A run stopped correctly

After the owner accepted Research 410, the bounded control plane authorized P6 and launched:

    currentSubphase = P6A
    runnerStatus = RUNNING

The automated runner then stopped on the first source with:

    runnerStatus = HOLD
    errorCode = ENOENT

Bounded and mechanical diagnosis established:

    accepted source count = 0
    accepted record count = 0
    current subphase = P6A
    orchestration state/plan IDs agree

Therefore no P6A source was accepted before the HOLD.

## 2. Semantic boundary remained intact

The task owner did not inspect:

    candidate_gap output
    semantic labels
    Claude response text
    transcript content
    hidden source/control roles

The failed semantic attempt transcript was preserved by Claude Code, but its contents were not read.

No canonical P6A artifact was accepted.

No P6B or P6C work started.

The HOLD therefore remains a mechanical execution-integrity event rather than a semantic result.

## 3. Mechanical diagnosis

The first P6A job workspace exists and contains every required staged input:

    SOURCE.json
    ELIGIBLE_ITEM_IDS.json
    KEY_AUTHOR_INSTRUCTIONS.md
    EXECUTION_ADDENDUM.md
    PRECEDENTS.md
    mcp.json

The local Claude Code executable is also available:

    claude
    2.1.283

Claude Code created the expected project transcript directory and a session JSONL transcript.

The actual Claude project slug for the P6A job normalizes the private cwd component:

    p6_jobs

to:

    p6-jobs

The qualified V2 verifier computed the transcript path using only:

    colon -> hyphen
    path separator -> hyphen

and did not normalize underscore to hyphen.

The verifier therefore searched a non-existent transcript directory even though Claude Code had created the transcript successfully.

The resulting `realpath(...)` failure surfaced as:

    ENOENT

This defect is localized to transcript-path reconstruction.

## 4. Frozen remediation

The successor runner must change only the transcript project-slug derivation.

Current rule:

    cwd.replace(/:/g, "-").replace(/[\\/]/g, "-")

Frozen corrected rule:

    cwd.replace(/:/g, "-").replace(/[\\/]/g, "-").replace(/_/g, "-")

No semantic prompt, model, effort, source order, tool allowlist, schema, evidence rule, phase transition, threshold, witness/control rule or retry policy may change as part of this remediation.

The failed transcript remains preserved.

The failed semantic output remains unaccepted and unread by the task owner.

## 5. Replacement-attempt rule

This is not retry-to-green.

The first attempt failed because the verifier could not resolve the already-created transcript path.

After the remediation is independently qualified and activated:

    resume_after_hold

may archive the held orchestration and start a new orchestration UUID.

Because the accepted prefix is empty:

    acceptedPrefix = 0

the first source is rerun in a new Claude Code process with a fresh session UUID.

The previous failed transcript is not supplied through `--continue`, `--resume`, or any semantic prompt.

No prior semantic answer is used to steer the replacement attempt.

## 6. Qualification requirements

Before live resumption, the successor release must prove at minimum:

    transcript slug converts underscore to hyphen
    prior colon/slash normalization remains unchanged
    transcript verifier resolves a synthetic P6-style cwd containing p6_jobs
    transcript verifier still rejects wrong session / wrong cwd / compaction / forbidden tools
    P6A schema regression remains PASS
    P6B evidence regression remains PASS
    P6C grouping regression remains PASS
    stop-on-HOLD remains PASS
    resume-after-HOLD accepted-prefix preservation remains PASS
    headless runner smoke remains PASS
    retained P5 regression remains PASS
    retained P4 regression remains PASS
    public-surface registration remains PASS
    managed release verification mismatchCount = 0

No live P6 semantic attempt may resume before those checks pass and the successor runtime is activated.

## 7. Exact next step

Create the successor managed runtime release from P6 V2, apply only the transcript-slug remediation, expand the synthetic regression to cover the real P6 cwd naming pattern, qualify/publish/verify/activate the release, then invoke the already-governed:

    resume_after_hold

action.

No new owner semantic authorization is required because Research 410 remains accepted and this remediation does not alter semantic scope.

    P6A_FIRST_RUN=HOLD
    P6A_ACCEPTED_PREFIX=0
    HOLD_ERROR=ENOENT
    ROOT_CAUSE=TRANSCRIPT_PROJECT_SLUG_UNDERSCORE_NORMALIZATION
    FAILED_TRANSCRIPT_PRESERVED=true
    FAILED_SEMANTIC_OUTPUT_ACCEPTED=false
    FAILED_SEMANTIC_OUTPUT_OBSERVED_BY_TASK_OWNER=false
    REMEDIATION=FROZEN
    NEXT=IMPLEMENT_QUALIFY_PUBLISH_ACTIVATE_TRANSCRIPT_SLUG_REMEDIATION
