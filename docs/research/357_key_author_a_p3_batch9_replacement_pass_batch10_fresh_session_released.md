# Research 357: Key Author A P3 Batch 9 Replacement Pass with Bounded Count-Query Deviation and Batch 10 Fresh-Session Release

**Date:** 2026-09-26
**Status:** P3 BATCH 9 PASS / PRIVATE FROZEN / BOUNDED NON-SEMANTIC TOOL-SCOPE DEVIATION RECORDED / BATCH 10 FRESH SESSION RELEASED
**Parent:** Research 356 / owner-run fresh replacement Claude Code P3 Batch 9 report
**Scope:** Reconcile the fresh replacement execution of BIRTH held-out Batch 9, mechanically validate the frozen private artifact, adjudicate one disclosed whole-source count-only Grep after all Batch 9 labels were already written, preserve the sequential-exposure construct, retire the replacement session after the deviation, and release Batch 10 to a fresh sequential P3 session under the existing P3 authorization.
**Authority:** P3 Batch 9 acceptance and Batch 10 fresh-session continuation release only. This does not authorize Batch 11, BIRTH grouping, attention-consistency reconciliation, LEGACY, canonical Key A assembly, commitment generation, Key Author B, scoring, reviewer execution, production implementation, migration, oracle retirement, or authority switching.

## 1. Executor result

The fresh replacement P3 Claude Code session returned:

    P3_BATCH_RESULT
        PASS

    batch_number
        9

    replacement_session
        true

    session_id
        af653639-44b6-4300-a2dc-9fab30973b96

    model
        claude-opus-5-5

    effort
        high launch setting

    permission mode
        default launch setting

    external terminal
        PASS

    IDE context absent
        PASS

    MCP disabled
        PASS

    web denied
        PASS

    local settings absent
        PASS

    compaction_events recorded
        1

    restarts recorded
        1

    open_batch_corrections
        0

    batch
        BAT-903fa5c8a8e6

    presentations expected / completed
        392 / 392

    output schema complete
        PASS

    precedents added this replacement
        0

    errata added this replacement
        0

    batch frozen
        true

    next batch exposed
        false

    shell used
        false

    grouping started
        false

    LEGACY started
        false

    P3 complete
        false

The executor separately disclosed one deviation for task-owner review: after all 392 Batch 9 labels had been written, but before the formal progress-state freeze, it ran a count-only Grep over the complete held-out classification-session source rather than restricting the operation to the Batch 9 line range.

## 2. Private-workspace postflight

Task-owner postflight independently verifies:

    current_phase
        P3_BIRTH_HELDOUT_BATCH_09_COMPLETE_AWAITING_REVIEW

    p3_authorized
        true

    frozen_batches
        both P2 development batches
        P3 held-out Batches 1 through 9

    open_batch
        null

    compaction_events
        1

    restarts
        1

    open_batch_corrections
        0

    errata_count
        0

    replacement P3 session ID
        af653639-44b6-4300-a2dc-9fab30973b96

    Batch 9 output
        exists

    P3 held-out output files
        exactly nine

    PRECEDENTS.md
        unchanged from the Research 356 recovery boundary

    ERRATA.jsonl
        empty

    .claude/settings.local.json
        absent

    controlled settings SHA-256
        8579fdb498a7d8a80b33025aa13d0a6a200e78881fd4e4fc7979e267a1d61eb6
        unchanged

A private Batch 9 digest and byte length were recorded for later immutability checking. They are intentionally not published.

## 3. Mechanical artifact validation

Task-owner mechanical validation returns:

    top-level fields
        exact

    protocol/component/split/batch/event/part metadata
        exact

    presentation count
        392

    presentation-ID set
        exact match to the frozen Batch 9 source

    presentation order
        exact match to the frozen Batch 9 source

    duplicate presentation IDs
        none

    per-presentation fields
        exact

    boolean field types
        exact

    normative_kind enum
        valid

    normative / normative_kind null consistency
        valid

Therefore:

    P3_BATCH9_MECHANICAL_VALIDATION
        PASS

No semantic labels, semantic category counts, semantic excerpts, or private precedent content are published.

## 4. Authorized semantic-source Reads

The replacement session uses bounded Read operations for Batch 9 event context only within:

    key_author_birth_heldout.json
        lines 10220 through 14185 inclusive

The replacement session uses bounded Read operations for Batch 9 classification material only within:

    birth_heldout_classification_sessions.json
        lines 11584 through 15511 inclusive

No bounded semantic Read crosses either authorized Batch 9 boundary.

The replacement session does not Read:

    prior frozen held-out semantic artifacts
    P2 development semantic artifacts
    P1 STATE semantic output
    Batch 10 classification content
    BIRTH grouping
    attention provenance
    LEGACY
    repository checkout
    other-key material

No transcript compaction occurs in the replacement session.

## 5. Count-only whole-source Grep deviation

After the final Batch 9 artifact mutation, the executor invoked one Grep on:

    inputs/r2_v03/packets/birth_heldout_classification_sessions.json

with:

    output_mode
        count

    pattern
        a generic presentation_id prefix

The tool result exposed only:

    total occurrences
        2347

No matched line text, presentation IDs, event text, semantic labels, or other content from Batch 10 or later entered the model-visible tool result.

The value 2347 was already prospectively published as the complete P3 presentation count in Research 345 and Research 346 before Batch 9 execution.

Transcript ordering independently proves:

    final Batch 9 semantic artifact mutation
        occurs before the whole-source Grep

    whole-source count-only Grep
        occurs after all 392 Batch 9 labels are written

    Batch 9 semantic artifact mutation after Grep
        none

After the Grep, the only artifact Read is a small bounded Read of the current Batch 9 output itself, followed by progress-state edits that freeze the already-written artifact.

Therefore the operation is a literal tool-scope/procedural deviation from the intended source-boundary discipline, but it did not expose any new future-batch semantic information to the author and could not influence any Batch 9 label because all labels were already written and none were changed afterward.

Task-owner classification:

    WHOLE_SOURCE_COUNT_GREP
        TECHNICAL_PROTOCOL_DEVIATION

    FUTURE_BATCH_SEMANTIC_CONTENT_EXPOSED
        NO

    NEW_FUTURE_BATCH_INFORMATION_EXPOSED
        NO

    BATCH9_LABELS_MUTATED_AFTER_DEVIATION
        NO

    DETECTABLE_CONSTRUCT_VALIDITY_EFFECT
        NONE

The deviation is preserved in provenance rather than silently normalized away.

## 6. Execution configuration verification

Transcript metadata records:

    model
        claude-opus-5-5

    effort
        high

    permissionMode
        default

    cwd
        Key Author A workspace

The replacement segment invokes no:

    Bash
    PowerShell
    shell / terminal execution
    Git
    Python
    WebSearch
    WebFetch
    Agent
    MCP
    IDE tool

No compaction occurs.

Therefore:

    P3_BATCH9_SHELL_PROHIBITION
        PASS

    P3_BATCH9_EXECUTION_CONFIGURATION
        PASS

## 7. Batch 9 disposition

Because the artifact is mechanically exact, all semantic-source Reads remained inside the authorized Batch 9 ranges, the only out-of-scope operation returned only a previously published aggregate count, and every Batch 9 semantic label was already written before that operation with no later mutation:

    P3_BATCH9
        PASS_WITH_RECORDED_NON_SEMANTIC_TOOL_SCOPE_DEVIATION

    BAT-903fa5c8a8e6
        PRIVATE_FROZEN

The frozen Batch 9 artifact must not be revised unless a separately governed correction is opened.

The Research 356 compaction/restart provenance remains part of the Key Author A record.

## 8. Session disposition

Although the deviation did not contaminate Batch 9 labels, the replacement session is retired after Batch 9 rather than carried into Batch 10.

Retired session:

    af653639-44b6-4300-a2dc-9fab30973b96

Reason:

    preserve the strongest possible prospective tool-boundary discipline after a recorded source-scope deviation

Research 345 explicitly permits a fresh sequential P3 session at a batch boundary.

Because Batch 9 and Batch 10 are parts of the same event, Research 345 also explicitly permits a fresh Batch 10 session to reread the already-authorized same-event context.

The new session remains the same logical Key Author A under Research 334.

## 9. Batch 10 release

Batch 10:

    batch_id
        BAT-ece1bc9728dc

    packet_event_id
        EVP-ffd3c3f9f874

    part_index
        2

    presentations
        61

Classification-session exposure:

    lines 15512 through 16129 inclusive

Because a fresh sequential session is required, the already-authorized split-event context may be reread:

    key_author_birth_heldout.json
        lines 10220 through 14185 inclusive

No other held-out event context is authorized.

Batch 11 remains gated.

Before semantic work, the fresh Batch 10 session must preserve the existing recovery provenance and record the additional session replacement:

    compaction_events
        1

    restarts
        2

It must append its exact Batch 10 session ID if exposed without shell use.

## 10. Repository operating constraint

Research 348 remains active:

    ADS repository operations
        Codexless Runtime Bridge only

    native GitHub connector
        prohibited for ADS repository operations

## 11. Current boundary

    P1_STATE=PASS
    P2_BIRTH_DEVELOPMENT=PASS

    P3_AUTHORIZED=true
    P3_BATCHES_1_8=PASS_PRIVATE_FROZEN
    P3_BATCH9=PASS_PRIVATE_FROZEN_WITH_RECORDED_NON_SEMANTIC_TOOL_SCOPE_DEVIATION

    P3_BATCH10=TASK_OWNER_RELEASED_FRESH_SESSION
    P3_BATCHES_11_13=TASK_OWNER_GATED
    P3_COMPLETE=false

    BIRTH_GROUPING=NOT_STARTED
    LEGACY=NOT_STARTED
    COMPLETE_KEY_A_BYTES=NOT_CREATED

    NEXT=OWNER_LAUNCH_FRESH_P3_BATCH10_SESSION
