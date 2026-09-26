# Research 351: Key Author A P3 Batch 4 Pass and Batch 5 Task-Owner Release

**Date:** 2026-09-26
**Status:** P3 BATCH 4 PASS / PRIVATE FROZEN / SEQUENTIAL EXPOSURE VERIFIED / BATCH 5 RELEASED WITHIN EXISTING P3 AUTHORIZATION
**Parent:** Research 350 / owner-run local Claude Code P3 Batch 4 report
**Scope:** Reconcile the fourth BIRTH held-out classification batch without publishing semantic labels, mechanically validate the private artifact and exact Batch 4 exposure boundary, preserve same-session continuation evidence, freeze Batch 4, and release Batch 5 under the already-granted P3 authorization.
**Authority:** P3 Batch 4 disposition and Batch 5 task-owner continuation release only. This does not authorize BIRTH grouping, attention-consistency reconciliation, LEGACY, canonical Key A assembly, commitment generation, Key Author B, scoring, reviewer execution, production implementation, migration, oracle retirement, or authority switching.

## 1. Executor result

The continuing fresh P3 Claude Code session returned:

    P3_BATCH_RESULT
        PASS

    batch_number
        4

    session_id
        a7968d41-028c-4a18-86e9-a9b63f16c3c9

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

    batch
        BAT-5b6b88a6e3c6

    presentations expected / completed
        70 / 70

    output schema complete
        PASS

    precedents added
        0

    errata added
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

The executor noted that effort and permission mode are launch settings not directly shown in-session. Transcript metadata independently confirms the continuing qualified configuration.

## 2. Private-workspace postflight

Task-owner postflight independently verified:

    current_phase
        P3_BIRTH_HELDOUT_BATCH_04_COMPLETE_AWAITING_REVIEW

    p3_authorized
        true

    frozen_batches
        both P2 development batches
        P3 held-out Batches 1 through 4

    open_batch
        null

    P3 session ID
        a7968d41-028c-4a18-86e9-a9b63f16c3c9

    compaction_events
        0

    restarts
        0

    Batch 4 output
        exists

    P3 held-out output files
        exactly four

    PRECEDENTS.md bytes
        unchanged from the accepted Batch 3 boundary

    ERRATA.jsonl
        empty

    .claude/settings.local.json
        absent

    controlled settings SHA-256
        8579fdb498a7d8a80b33025aa13d0a6a200e78881fd4e4fc7979e267a1d61eb6
        unchanged

A private Batch 4 digest was recorded for later immutability checking. This public record intentionally does not publish semantic-artifact digests.

## 3. Mechanical artifact validation

The task owner mechanically validated Batch 4:

    protocol/component/split/batch/event/part metadata
        exact

    presentation count
        70

    presentation-ID set
        exact match to frozen Batch 4 source

    presentation order
        exact match to frozen Batch 4 source

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

    P3_BATCH4_MECHANICAL_VALIDATION
        PASS

No semantic labels, semantic category counts, semantic excerpts, or precedent content are published.

## 4. Transcript and sequential-exposure verification

The Batch 4 transcript segment contains 11 tool uses.

The only semantic source Reads are:

    key_author_birth_heldout.json
        offset 5520
        limit 622

    birth_heldout_classification_sessions.json
        offset 6294
        limit 708

Therefore the exact exposed ranges are:

    event context
        lines 5520 through 6141 inclusive

    classification source
        lines 6294 through 7001 inclusive

No semantic-source Read crosses either Batch 4 boundary.

The segment does not Read:

    prior held-out classification ranges
    prior held-out event-context ranges
    prior frozen held-out semantic artifacts
    P2 development semantic artifacts
    P1 STATE semantic output
    Batch 5 or later source ranges
    BIRTH grouping
    attention provenance
    LEGACY
    repository checkout
    other-key material

All three Grep operations reference the current Batch 4 artifact; none references a prior held-out batch or development semantic artifact.

The one Glob operation checks for the local settings file.

No transcript compaction marker occurs during Batch 4.

Therefore:

    BATCH4_SEQUENTIAL_EXPOSURE
        PASS

    BATCH5_PREMATURE_EXPOSURE
        NONE

    PRIOR_FROZEN_BATCH_SEMANTIC_ACCESS
        NONE

## 5. Execution configuration verification

Transcript metadata records:

    model
        claude-opus-5-5

    effort
        high

    permissionMode
        default

The Batch 4 segment invokes no:

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

The controlled settings hash is unchanged and local settings remain absent.

Therefore:

    P3_BATCH4_SHELL_PROHIBITION
        PASS

    P3_BATCH4_TOOL_BOUNDARY
        PASS

## 6. Batch 4 disposition

All required Batch 4 gates passed.

Therefore:

    P3_BATCH4
        PASS

    BAT-5b6b88a6e3c6
        PRIVATE_FROZEN

    BATCH4_REWRITE
        PROHIBITED_UNLESS_GOVERNED_CORRECTION_IS_OPENED

Earlier held-out batches remain private frozen.

## 7. Batch 5 release

Research 346 records explicit owner authorization for the complete 13-batch P3 phase.

Research 345 established that accepted P3 batches may be followed by task-owner continuation release without additional human authorization.

Batch 4 acceptance is now complete.

Therefore:

    P3_BATCH5
        TASK_OWNER_RELEASED

The same P3 Claude Code session may continue because:

    model/configuration are unchanged
    compaction_events remains 0
    restarts remains 0
    Batch 4 is frozen
    no new precedent or erratum was added
    no future-batch material was exposed

## 8. Batch 5 exposure boundary

Batch 5:

    batch_id
        BAT-ba93d18c7368

    packet_event_id
        EVP-ba08dc62e616

    part_index
        1

    presentations
        68

Classification-session exposure:

    lines 7002 through 7689 inclusive

Held-out event-context exposure:

    lines 6142 through 6745 inclusive

The executor must not:

    reread prior classification ranges
    reread prior event-context ranges
    read prior frozen semantic batch artifacts
    expose Batch 6
    access attention provenance
    access BIRTH grouping
    access LEGACY
    use shell/external tools

## 9. Repository operating constraint

Research 348 remains active:

    ADS repository operations
        Codexless Runtime Bridge only

    native GitHub connector
        prohibited for ADS repository operations

## 10. Current boundary

    P1_STATE=PASS
    P2_BIRTH_DEVELOPMENT=PASS

    P3_AUTHORIZED=true
    P3_BATCH1=PASS_PRIVATE_FROZEN
    P3_BATCH2=PASS_PRIVATE_FROZEN
    P3_BATCH3=PASS_PRIVATE_FROZEN
    P3_BATCH4=PASS_PRIVATE_FROZEN
    P3_BATCH5=TASK_OWNER_RELEASED
    P3_BATCHES_6_13=TASK_OWNER_GATED
    P3_COMPLETE=false

    BIRTH_GROUPING=NOT_STARTED
    LEGACY=NOT_STARTED
    COMPLETE_KEY_A_BYTES=NOT_CREATED

    NEXT=OWNER_CONTINUE_P3_BATCH5
