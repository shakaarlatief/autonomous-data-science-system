# Research 356: Key Author A P3 Batch 9 Compaction HOLD and Fresh Replacement Authorization

**Date:** 2026-09-26
**Status:** P3 BATCH 9 HOLD / OPEN-BATCH COMPACTION CONFIRMED / PRIOR ATTEMPT ABANDONED / FRESH REPLACEMENT SESSION AUTHORIZED
**Parent:** Research 355 / owner-run local Claude Code P3 Batch 9 HOLD report
**Scope:** Reconcile the Batch 9 open-batch compaction event, verify what was and was not exposed or persisted, preserve the authorized append-only precedent addition, retire the compacted session from further semantic execution, and authorize a fresh replacement P3 session to restart Batch 9 from scratch under the existing P3 authorization.
**Authority:** Batch 9 HOLD disposition and fresh replacement execution only. Batch 10 remains task-owner gated. This does not authorize BIRTH grouping, attention-consistency reconciliation, LEGACY, canonical Key A assembly, commitment generation, Key Author B, scoring, reviewer execution, production implementation, migration, oracle retirement, or authority switching.

## 1. Executor HOLD

The continuing P3 Claude Code session returned:

    P3_BATCH_RESULT
        HOLD

    batch_number
        9

    batch_id
        BAT-903fa5c8a8e6

    session_id
        a7968d41-028c-4a18-86e9-a9b63f16c3c9

    hold_reason
        COMPACTION_DETECTED_WHILE_BATCH_OPEN

    presentations expected
        392

    presentations written
        0

    Batch 9 output artifact
        not created

    batch frozen
        false

    precedents added
        1

    errata added
        0

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

The HOLD is required by the prospectively frozen Research 345 compaction rule:

    compaction while a batch is open
        HOLD

## 2. Independent compaction verification

Task-owner transcript review independently confirms an actual Claude Code compaction boundary while Batch 9 remained open.

The transcript contains:

    system subtype
        compact_boundary

    compact summary record
        present

The compact boundary is timestamped after the second Batch 9 classification-source read.

Therefore the executor's statement that one bounded classification read occurred after compaction is not supported by the durable transcript ordering.

The durable transcript instead establishes:

    all tool use occurred before the compact_boundary
    no tool call occurred after compaction
    the executor then stopped and returned HOLD

This discrepancy does not weaken the HOLD. Compaction itself occurred while Batch 9 was open, which is sufficient for HOLD under Research 345.

## 3. Exposure before HOLD

Before compaction, the session read the complete authorized Batch 9 event context:

    key_author_birth_heldout.json
        lines 10220 through 14185 inclusive

Before compaction, it read only the first portion of the authorized Batch 9 classification source:

    birth_heldout_classification_sessions.json
        lines 11584 through 12893 inclusive

It did not read:

    classification line 12894 or later
    Batch 10 classification range 15512-16129
    event-context line 14186 or later
    prior frozen held-out semantic artifacts
    P2 development semantic artifacts
    P1 STATE semantic output
    BIRTH grouping
    attention provenance
    LEGACY
    repository checkout
    other-key material

Therefore:

    BATCH10_PREMATURE_EXPOSURE
        NONE

    FORBIDDEN_SOURCE_ACCESS
        NONE

## 4. No Batch 9 semantic artifact exists

Task-owner private-workspace inspection confirms:

    out/birth_heldout/BAT-903fa5c8a8e6.json
        absent

    frozen held-out output count
        8

    frozen Batch 9 entry
        absent

    open_batch
        BAT-903fa5c8a8e6

    current_phase
        P3_BIRTH_HELDOUT_BATCH_09_IN_PROGRESS

No presentation-level Batch 9 labels were persisted.

Any labels held only in pre-compaction conversational working context are abandoned and have no evidentiary or semantic status.

## 5. Append-only precedent disposition

Before compaction, the executor made exactly one Edit to:

    work/PRECEDENTS.md

Task-owner transcript inspection mechanically verifies that the edit was append-only:

    replacement new_string starts with old_string
        true

    append delta
        non-zero

The precedent carrier therefore changed through the authorized append-only mechanism before the compaction event.

The precedent is preserved.

It must not be deleted, rewritten or rolled back merely because the batch attempt later entered HOLD.

Reason:

    Research 334 defines sequential sessions as one logical Key Author A only when the append-only precedent record is preserved.

The precedent content remains private and is not reproduced publicly.

No erratum was added.

## 6. Progress provenance correction

The private PROGRESS state has not yet recorded the compaction.

Before the replacement session makes any semantic judgment, it must mechanically record:

    compaction_events
        1

When the fresh replacement session begins, it must mechanically record:

    restarts
        1

The replacement session must append its own P3 Batch 9 session record if the session ID is exposed without shell use.

The batch remains:

    current_phase
        P3_BIRTH_HELDOUT_BATCH_09_IN_PROGRESS

    open_batch
        BAT-903fa5c8a8e6

    frozen_batches
        unchanged

    p3_authorized
        true

    open_batch_corrections
        unchanged

No open-batch semantic correction is counted because no Batch 9 semantic artifact was written or revised. The recovery is tracked by compaction_events and restarts.

## 7. Recovery disposition

The compacted session:

    a7968d41-028c-4a18-86e9-a9b63f16c3c9

is retired from further semantic execution.

It must not be continued or resumed.

Research 334 permits multiple sequential local Claude Code sessions to remain one logical Key Author A when:

    model selection is unchanged
    frozen inputs are unchanged
    addendum is unchanged
    codebook is unchanged
    append-only precedents are preserved
    no parallel semantic worker exists
    all session IDs are recorded

Research 345 further states that a replacement session reconstructs only from:

    common sources
    append-only precedents
    newly released current-batch source/context

Therefore:

    BATCH9_RETRY
        AUTHORIZED

    EXECUTION_MODE
        FRESH REPLACEMENT P3 SESSION

    BATCH9_RESTART
        FROM SCRATCH

The replacement must not use --continue or --resume.

The replacement is not a new independent key author. It remains the same logical Key Author A.

## 8. Replacement Batch 9 exposure

The fresh replacement session may reread the complete current Batch 9 ranges because it must reconstruct the current batch from scratch:

    classification source
        lines 11584 through 15511 inclusive

    event context
        lines 10220 through 14185 inclusive

It must not read prior frozen semantic artifacts.

It must not read Batch 10 classification lines 15512-16129.

Batch 10 remains gated.

Because Batch 9 and Batch 10 share split event EVP-ffd3c3f9f874, the replacement Batch 9 session should retain the Batch 9 event context for possible Batch 10 continuation if Batch 9 later passes.

## 9. Execution configuration

The fresh replacement must preserve:

    model
        claude-opus-5-5

    effort
        high

    permissionMode
        default

    standalone external terminal
        required

    IDE context
        absent

    MCP
        disabled

    web
        denied

    shell during semantic execution
        prohibited

    parallel semantic workers
        prohibited

    subagent semantic workers
        prohibited

The controlled settings file remains unchanged and .claude/settings.local.json remains absent at HOLD review.

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

    P3_BATCH9=HOLD_OPEN_BATCH_COMPACTION
    P3_BATCH9_PRIOR_ATTEMPT=ABANDONED_NO_ARTIFACT
    P3_BATCH9_REPLACEMENT=TASK_OWNER_AUTHORIZED

    P3_BATCHES_10_13=TASK_OWNER_GATED
    P3_COMPLETE=false

    BIRTH_GROUPING=NOT_STARTED
    LEGACY=NOT_STARTED
    COMPLETE_KEY_A_BYTES=NOT_CREATED

    NEXT=OWNER_LAUNCH_FRESH_P3_BATCH9_REPLACEMENT
