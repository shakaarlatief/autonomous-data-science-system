# Research 415: Key Author A P6A Structured-Output Postflight Remediation

**Date:** 2026-09-30
**Status:** P6A HOLD / STRUCTURED-OUTPUT POSTFLIGHT MISMATCH DIAGNOSED / REMEDIATION FROZEN
**Parent:** Research 414
**Scope:** Preserve the second live P6A HOLD after transcript-slug remediation, diagnose the verifier mismatch without inspecting semantic output, and freeze the minimal postflight remediation before another replacement attempt.
**Authority:** Mechanical transcript-verifier remediation only. This record does not alter Research 410 semantic scope, candidate-gap criteria, model configuration, source order, evidence rules, grouping rules, witness/control floors, canonical assembly, Key Author B, scoring, successor implementation, migration, or authority switching.

## 1. Post-remediation P6A stopped correctly

After P6 V3 was qualified, published, activated, and the held orchestration was resumed with a fresh Claude Code session, bounded status initially reported:

    currentSubphase = P6A
    runnerStatus = RUNNING
    hold = false

The replacement attempt then stopped with:

    runnerStatus = HOLD
    errorCode = P6_TRANSCRIPT_POSTFLIGHT_FAILED

The private runner state still reported:

    accepted source count = 0
    accepted record count = 0

Therefore no P6A source was accepted before this second HOLD.

## 2. Semantic boundary remained intact

The task owner did not inspect:

    candidate_gap values
    Claude semantic response text
    StructuredOutput values
    transcript prose
    hidden source/control roles

The failed session transcript remains preserved.

No canonical P6A artifact was accepted.

No P6B or P6C work started.

Diagnosis was restricted to non-semantic transcript metadata.

## 3. Mechanical diagnosis

The failed transcript satisfied all of the following:

    transcript filename/session agreement = true
    distinct session count = 1
    transcript cwd equals job workspace = true
    permission mode = dontAsk
    model = claude-opus-5-5
    compact-boundary events = none
    malformed JSON lines = 0
    tool paths outside the job workspace = 0

Observed tool names were exactly:

    Read
    StructuredOutput

Counts were:

    Read = 7
    StructuredOutput = 1

The `StructuredOutput` invocation exposed only the schema-level keys:

    schema_version
    protocol_id
    component
    phase
    packet_source_id
    items

No values were inspected.

## 4. Root cause

P6 uses Claude Code's:

    --json-schema

structured-output mode.

Claude Code records its schema-constrained final answer in the transcript as a built-in tool-use entry named:

    StructuredOutput

The V2/V3 verifier allowed only the semantic read/search tool set:

    P6A
        Read

    P6B
        Read / Glob / Grep

    P6C
        Read

and therefore treated the required built-in StructuredOutput event as a forbidden semantic tool.

This is a verifier-model mismatch, not a semantic-author boundary violation.

The headless smoke did not detect the mismatch because its synthetic transcript stub emitted only a Read tool event rather than the real Claude Code StructuredOutput event.

## 5. Frozen remediation

The verifier must distinguish:

    semantic capability tools

from:

    the schema-bound final-output carrier

The semantic tool allowlist remains unchanged:

    P6A
        Read

    P6B
        Read / Glob / Grep

    P6C
        Read

The verifier may additionally accept exactly:

    StructuredOutput

under all of these conditions:

    exactly one StructuredOutput tool-use event exists
    it is not treated as a filesystem/network/process capability
    it carries no path that can expand semantic read scope
    its input object has exactly the phase schema's top-level keys
    no other previously forbidden tool becomes permitted

For P6A, expected StructuredOutput top-level keys are exactly:

    schema_version
    protocol_id
    component
    phase
    packet_source_id
    items

For P6B, expected keys are exactly:

    schema_version
    protocol_id
    component
    phase
    packet_source_id
    items

For P6C, expected keys are exactly:

    schema_version
    protocol_id
    component
    phase
    packet_source_id
    must_join_pairs
    must_split_pairs

The semantic artifact remains independently validated after Claude returns.

Therefore allowing StructuredOutput in transcript postflight does not authorize any new semantic capability.

## 6. Strengthened qualification requirement

Before live resumption, the successor release must prove:

    real-style transcript fixture includes one StructuredOutput event
    exactly one StructuredOutput is accepted
    missing StructuredOutput fails closed
    duplicate StructuredOutput fails closed
    wrong StructuredOutput key set fails closed
    Bash remains rejected
    MCP tool remains rejected
    P6A Read-only capability remains unchanged
    P6B Read/Glob/Grep capability remains unchanged
    P6C Read-only capability remains unchanged
    underscore transcript-slug regression remains PASS
    headless smoke emits and verifies StructuredOutput
    stop-on-HOLD remains PASS
    resume-after-HOLD remains PASS
    retained P5 regression remains PASS
    retained P4 regression remains PASS
    full managed release regressions pass
    release verification mismatchCount = 0

No live replacement semantic attempt may start before this qualification and activation complete.

## 7. Replacement-attempt rule

The second failed attempt is not accepted.

The transcript is preserved.

After the verifier fix is qualified and activated:

    resume_after_hold

may archive the held orchestration and start another fresh orchestration/session.

Because the accepted prefix remains zero:

    acceptedPrefix = 0

the first source is again the first unfinished semantic job.

Neither prior failed transcript is supplied through:

    --continue
    --resume
    prompt context
    precedent context

No prior candidate-gap answer is read or used to steer the next attempt.

## 8. Exact next step

Create the successor managed runtime release from P6 V3, implement only the StructuredOutput postflight distinction, strengthen synthetic and headless tests to reproduce real Claude Code transcript behavior, qualify/publish/verify/activate it, then invoke:

    resume_after_hold

No new owner semantic authorization is required because Research 410 remains accepted and the semantic capability boundary is unchanged.

    P6A_SECOND_RUN=HOLD
    P6A_ACCEPTED_PREFIX=0
    HOLD_ERROR=P6_TRANSCRIPT_POSTFLIGHT_FAILED
    ROOT_CAUSE=STRUCTURED_OUTPUT_NOT_DISTINGUISHED_FROM_SEMANTIC_TOOLS
    FAILED_TRANSCRIPT_PRESERVED=true
    FAILED_SEMANTIC_OUTPUT_ACCEPTED=false
    FAILED_SEMANTIC_OUTPUT_OBSERVED_BY_TASK_OWNER=false
    REMEDIATION=FROZEN
    NEXT=IMPLEMENT_QUALIFY_PUBLISH_ACTIVATE_STRUCTURED_OUTPUT_POSTFLIGHT_REMEDIATION
