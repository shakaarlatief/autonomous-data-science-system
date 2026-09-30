# Research 417: Key Author A P6A PASS and P6B Add-Dir Prompt-Parsing HOLD Remediation

**Date:** 2026-09-30
**Status:** P6A PASS / P6B HOLD BEFORE ACCEPTED SOURCE / CLI PROMPT-PARSING REMEDIATION FROZEN
**Parent:** Research 416
**Scope:** Preserve successful P6A completion, the first P6B fail-closed HOLD, mechanical CLI diagnosis, and the minimal P6B invocation remediation before any replacement evidence-authoring attempt.
**Authority:** P6A phase completion and mechanical P6B runner remediation only. Research 410 semantic scope and owner acceptance remain unchanged. This record does not alter evidence semantics, evidence horizon, candidate-gap outputs, grouping semantics, witness/control floors, canonical Key A assembly, Key A commitment, Key Author B, scoring, successor implementation, migration, or authority switching.

## 1. P6A completed and froze successfully

After Research 416 activated the StructuredOutput postflight remediation and resumed P6A, bounded status reached:

    currentSubphase = P6A
    runnerStatus = COMPLETE
    boundaryReady = true
    hold = false
    errorCode = null

The purpose-specific control plane was invoked with exactly:

    action = finalize_subphase

and returned:

    ok = true
    finalizedSubphase = P6A
    subphaseResult = PASS
    nextSubphase = P6B
    hiddenSemanticDetailsExposed = false
    next = RUN_UNTIL_BOUNDARY

P6A is therefore frozen as PASS.

The task owner did not inspect candidate-gap values or per-item semantic output.

## 2. First P6B run stopped before acceptance

The bounded control plane then invoked:

    action = run_until_boundary

for P6B.

It started successfully, then stopped fail closed with:

    currentSubphase = P6B
    runnerStatus = HOLD
    errorCode = P6_CLAUDE_EXIT

Mechanical private-runner metadata shows:

    accepted source count = 0
    accepted record count = 0
    failed source = first frozen LEGACY source

The P6B job workspace contains all required staged inputs:

    SOURCE.json
    ELIGIBLE_ITEM_IDS.json
    KEY_AUTHOR_INSTRUCTIONS.md
    EXECUTION_ADDENDUM.md
    PRECEDENTS.md
    mcp.json

No Claude project transcript directory was created for the failed P6B attempt.

Therefore Claude Code exited before beginning the semantic session.

No P6B semantic output was accepted or inspected.

## 3. Mechanical CLI diagnosis

P6B differs from P6A by adding the fixed frozen evidence checkout through:

    --add-dir <evidenceRoot>

Claude Code help defines this option as variadic:

    --add-dir <directories...>

The qualified P6 invocation builder currently constructs the P6B tail as:

    --add-dir
    <fixedEvidenceRoot>
    <prompt>

Because `--add-dir` is variadic, the positional prompt is consumed as an additional directory value.

A synthetic non-semantic CLI probe reproduced the exact immediate failure:

    exit status = 1
    stderr =
        Error: Input must be provided either through stdin or as a prompt argument when using --print

This probe used only temporary synthetic files and did not access Key Author A semantic data.

A second synthetic probe inserted the standard option terminator:

    --add-dir
    <syntheticEvidenceRoot>
    --
    <syntheticPrompt>

The immediate missing-input failure disappeared and the process entered normal model execution until the deliberately short probe timeout.

This isolates the defect to CLI argument parsing.

## 4. Frozen minimal remediation

The successor P6 runner must change only P6B prompt separation.

For P6B, construct:

    --add-dir
    <fixedEvidenceRoot>
    --
    <prompt>

P6A and P6C invocation structure remains unchanged.

The fixed evidence root remains exactly:

    LOCALAPPDATA/ADS-R2-KeyAuthor-A/legacy_search/ads_legacy_0a68787a

The evidence revision remains exactly:

    0a68787aee5f2c6332d6ee1fb6adbf0efe92a41d

No caller-selectable path or prompt is introduced.

No semantic tool permission changes.

No model or effort changes.

No evidence rule changes.

## 5. Strengthened qualification requirements

Before P6B resumption, the successor release must prove at minimum:

    Claude CLI help still declares --add-dir as variadic
    P6B invocation contains exactly one --add-dir
    fixed evidence root immediately follows --add-dir
    literal -- immediately follows the evidence root
    semantic prompt follows the literal -- separator
    no prompt is consumed into add-dir values
    P6A invocation remains unchanged
    P6C invocation remains unchanged
    P6B semantic tools remain Read / Glob / Grep only
    P6A/P6C semantic tools remain Read only
    StructuredOutput postflight remediation remains PASS
    transcript-slug remediation remains PASS
    stop-on-HOLD remains PASS
    resume-after-HOLD remains PASS
    headless runner smoke remains PASS
    retained P5 regression remains PASS
    retained P4 regression remains PASS
    full managed release regressions pass
    release verification mismatchCount = 0

No live P6B replacement semantic attempt may start before qualification, publication and activation complete.

## 6. Replacement-attempt rule

The first P6B attempt remains HOLD and is not accepted.

Because accepted P6B prefix is zero, governed:

    resume_after_hold

may start the first source again only after the fix is activated.

The replacement must use:

    a new orchestration UUID
    a new Claude Code session UUID
    no --resume
    no --continue
    no prior semantic response context

P6A remains frozen and must not be rerun.

## 7. Current boundary

    P6A=PASS_FROZEN
    P6B=HOLD
    P6B_ACCEPTED_PREFIX=0
    P6B_HOLD_ERROR=P6_CLAUDE_EXIT
    P6B_HOLD_ROOT_CAUSE=VARIADIC_ADD_DIR_CONSUMED_POSITIONAL_PROMPT
    P6B_SEMANTIC_OUTPUT_ACCEPTED=false
    P6B_SEMANTIC_OUTPUT_INSPECTED_BY_TASK_OWNER=false
    P6C=NOT_STARTED
    REMEDIATION=FROZEN
    NEXT=IMPLEMENT_QUALIFY_PUBLISH_ACTIVATE_P6B_PROMPT_SEPARATOR_REMEDIATION
