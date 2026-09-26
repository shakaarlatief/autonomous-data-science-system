# Research 355: Key Author A P3 Batch 8 Pass and Batch 9 Task-Owner Release

**Date:** 2026-09-26
**Status:** P3 BATCH 8 PASS / PRIVATE FROZEN / SEQUENTIAL EXPOSURE VERIFIED / BATCH 9 RELEASED WITHIN EXISTING P3 AUTHORIZATION
**Parent:** Research 354 / owner-run local Claude Code P3 Batch 8 report
**Scope:** Reconcile the eighth BIRTH held-out classification batch without publishing semantic labels, mechanically validate the private artifact and exact Batch 8 exposure boundary, preserve same-session continuation evidence, freeze Batch 8, and release Batch 9 under the already-granted P3 authorization.
**Authority:** P3 Batch 8 disposition and Batch 9 task-owner continuation release only. This does not authorize BIRTH grouping, attention-consistency reconciliation, LEGACY, canonical Key A assembly, commitment generation, Key Author B, scoring, reviewer execution, production implementation, migration, oracle retirement, or authority switching.

## 1. Executor result

The continuing fresh P3 Claude Code session returned:

    P3_BATCH_RESULT
        PASS

    batch_number
        8

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
        BAT-7dc61c90a939

    presentations expected / completed
        129 / 129

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

The executor noted that effort and permission mode are launch settings not directly displayed in-session. Transcript metadata independently confirms the continuing qualified configuration.

## 2. Private-workspace postflight

Task-owner postflight independently verified:

    current_phase
        P3_BIRTH_HELDOUT_BATCH_08_COMPLETE_AWAITING_REVIEW

    p3_authorized
        true

    frozen_batches
        both P2 development batches
        P3 held-out Batches 1 through 8

    open_batch
        null

    P3 session ID
        a7968d41-028c-4a18-86e9-a9b63f16c3c9

    compaction_events
        0

    restarts
        0

    Batch 8 output
        exists

    P3 held-out output files
        exactly eight

    PRECEDENTS.md
        unchanged from the accepted Batch 7 boundary

    ERRATA.jsonl
        empty

    .claude/settings.local.json
        absent

    controlled settings SHA-256
        8579fdb498a7d8a80b33025aa13d0a6a200e78881fd4e4fc7979e267a1d61eb6
        unchanged

A private Batch 8 digest was recorded for later immutability checking. This public record intentionally does not publish semantic-artifact digests.

## 3. Mechanical artifact validation

The task owner mechanically validated Batch 8:

    top-level fields
        exact

    protocol/component/split/batch/event/part metadata
        exact

    presentation count
        129

    presentation-ID set
        exact match to frozen Batch 8 source

    presentation order
        exact match to frozen Batch 8 source

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

    P3_BATCH8_MECHANICAL_VALIDATION
        PASS

No semantic labels, semantic category counts, semantic excerpts, or precedent content are published.

## 4. Transcript and sequential-exposure verification

The Batch 8 transcript segment contains 14 tool uses.

The held-out event-context Reads are:

    key_author_birth_heldout.json
        offset 9067 / limit 40
        offset 10030 / limit 190
        offset 9107 / limit 923

Taken together, these cover exactly:

    lines 9067 through 10219 inclusive

The held-out classification Reads are:

    birth_heldout_classification_sessions.json
        offset 10286 / limit 650
        offset 10936 / limit 648

Taken together, these cover exactly:

    lines 10286 through 11583 inclusive

No semantic-source Read crosses either Batch 8 boundary.

The segment does not Read:

    prior held-out classification ranges
    prior held-out event-context ranges
    prior frozen held-out semantic artifacts
    P2 development semantic artifacts
    P1 STATE semantic output
    Batch 9 or later source ranges
    BIRTH grouping
    attention provenance
    LEGACY
    repository checkout
    other-key material

All three Grep operations target only the current Batch 8 artifact for internal structural checks.

The one Glob operation checks only for .claude/settings.local.json.

No transcript compaction marker occurs during Batch 8.

Therefore:

    BATCH8_SEQUENTIAL_EXPOSURE
        PASS

    BATCH9_PREMATURE_EXPOSURE
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

    cwd
        Key Author A workspace

The Batch 8 segment invokes no:

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

The controlled settings hash remains unchanged and local settings remain absent.

Therefore:

    P3_BATCH8_SHELL_PROHIBITION
        PASS

    P3_BATCH8_TOOL_BOUNDARY
        PASS

## 6. Batch 8 disposition

All required Batch 8 gates passed.

Therefore:

    P3_BATCH8
        PASS

    BAT-7dc61c90a939
        PRIVATE_FROZEN

    BATCH8_REWRITE
        PROHIBITED_UNLESS_GOVERNED_CORRECTION_IS_OPENED

Earlier held-out batches remain private frozen.

## 7. Batch 9 release

Research 346 records explicit owner authorization for the complete 13-batch P3 phase.

Research 345 established that accepted P3 batches may be followed by task-owner continuation release without additional human authorization.

Batch 8 acceptance is now complete.

Therefore:

    P3_BATCH9
        TASK_OWNER_RELEASED

The same P3 Claude Code session may continue because:

    model/configuration are unchanged
    compaction_events remains 0
    restarts remains 0
    Batch 8 is frozen
    no new precedent or erratum was added
    no future-batch material was exposed

## 8. Batch 9 exposure boundary

Batch 9 begins the first part of split event EVP-ffd3c3f9f874.

Batch 9:

    batch_id
        BAT-903fa5c8a8e6

    packet_event_id
        EVP-ffd3c3f9f874

    part_index
        1

    presentations
        392

Classification-session exposure:

    lines 11584 through 15511 inclusive

Held-out event-context exposure:

    lines 10220 through 14185 inclusive

Batch 10 is the second part of the same event. Its classification range remains forbidden until Batch 9 passes task-owner review. The event context exposed in Batch 9 is prospectively the context to be retained for Batch 10; if the same session continues, Batch 10 must not reread it.

The executor must not:

    reread prior classification ranges
    reread prior event-context ranges
    read prior frozen semantic batch artifacts
    expose Batch 10 classification lines
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
    P3_BATCHES_1_8=PASS_PRIVATE_FROZEN
    P3_BATCH9=TASK_OWNER_RELEASED
    P3_BATCHES_10_13=TASK_OWNER_GATED
    P3_COMPLETE=false

    BIRTH_GROUPING=NOT_STARTED
    LEGACY=NOT_STARTED
    COMPLETE_KEY_A_BYTES=NOT_CREATED

    NEXT=OWNER_CONTINUE_P3_BATCH9
