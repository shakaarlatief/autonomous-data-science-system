# Research 343: Key Author A P2 Batch 1 Pass and Batch 2 Task-Owner Release

**Date:** 2026-09-26
**Status:** P2 BATCH 1 PASS / SEQUENTIAL-EXPOSURE CONTROL VERIFIED / PRIVATE BATCH FROZEN / BATCH 2 RELEASED WITHIN EXISTING P2 AUTHORIZATION
**Parent:** Research 342 / owner-run local Claude Code P2 Batch 1 report
**Scope:** Reconcile the first BIRTH-development classification batch without publishing semantic labels, verify the private batch artifact and transcript/exposure boundary mechanically, preserve the private frozen-batch commitment point, and release Batch 2 under the already-granted P2 authorization.
**Authority:** P2 Batch 1 disposition and Batch 2 task-owner continuation release only. This does not authorize BIRTH held-out classification, BIRTH grouping, LEGACY, canonical Key A assembly, commitment generation, Key Author B, scoring, reviewer execution, production implementation, migration, oracle retirement, or authority switching.

## 1. Executor result

The owner-run local Claude Code P2 Batch 1 session returned:

    P2_BATCH1_RESULT
        PASS

    session_id
        ae1c2ab7-0ae8-4263-8606-0b54de84e2ed

    model
        claude-opus-5-5

    effort
        high

    permission mode
        default

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
        BAT-2d0805e6c619

    presentations expected
        205

    presentations completed
        205

    output schema complete
        PASS

    precedents added
        3

    errata added
        0

    batch frozen
        true

    batch 2 exposed
        false

    shell used
        false

    P2 complete
        false

## 2. Private-workspace postflight

Task-owner postflight independently verified:

    current_phase
        P2_BIRTH_DEVELOPMENT_BATCH1_COMPLETE_AWAITING_REVIEW

    p1_authorized
        true

    p2_authorized
        true

    semantic_labels_created
        true

    frozen_batches
        exactly BAT-2d0805e6c619

    open_batch
        null

    P2 session count
        1

    P2 session ID
        ae1c2ab7-0ae8-4263-8606-0b54de84e2ed

    .claude/settings.local.json
        absent

    out/ semantic files
        P1 STATE output
        P2 Batch 1 output
        no Batch 2 output

    errata bytes
        0

    compaction_events
        0

    restarts
        0

    open_batch_corrections
        0

The task owner observed a private SHA-256 digest and byte length for the frozen Batch 1 artifact for later change detection. This public record intentionally does not publish that digest.

## 3. Mechanical Batch 1 artifact validation

The task owner validated the private Batch 1 JSON without publishing semantic values.

Checks passed:

    top-level fields
        exact

    metadata
        exact protocol/component/split/batch/event/part binding

    presentation count
        205

    presentation-ID set
        exact match to the frozen Batch 1 source

    presentation order
        exact match to the frozen Batch 1 source

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

    P2_BATCH1_MECHANICAL_VALIDATION
        PASS

This is a structural/integrity check only. The task owner did not reclassify or evaluate the semantic labels.

## 4. Sequential-exposure transcript verification

The exact Claude Code transcript was located uniquely by session ID.

Actual tool-use counts were:

    Read
        14

    Write
        3

    Edit
        1

    Grep
        4

    Glob
        1

No actual tool-use block invoked:

    Bash
    PowerShell
    shell / terminal execution
    Git
    Python
    WebSearch
    WebFetch
    Agent
    MCP
    IDE tools

The common Read targets were all P2-authorized sources.

The frozen multi-batch classification-session file was read only in these bounded ranges:

    offset 1, limit 500
    offset 500, limit 520
    offset 1020, limit 520
    offset 1540, limit 528

The final authorized line reached is therefore:

    2067

The prohibited Batch 2 boundary begins at:

    2068

The frozen multi-event key-author development packet was read only in these bounded ranges:

    offset 1, limit 450
    offset 450, limit 460
    offset 910, limit 460
    offset 1370, limit 462

The final authorized line reached is therefore:

    1831

The prohibited Batch 2 event boundary begins at:

    1832

Therefore:

    BATCH2_CLASSIFICATION_EXPOSURE
        NONE

    BATCH2_EVENT_CONTEXT_EXPOSURE
        NONE

    SEQUENTIAL_EXPOSURE_CONTROL
        PASS

The Grep operations targeted only the just-created Batch 1 private artifact for internal validation and did not access future-batch material.

## 5. Precedent append-only verification

The only PRECEDENTS.md mutation was one Edit operation.

Mechanically:

    original text preserved as exact prefix
        PASS

    appended section count
        3 level-2 entries

This matches the executor report:

    PRECEDENTS_ADDED
        3

No existing precedent was edited or deleted.

No erratum was added.

The semantic contents of the precedents remain private and are not reproduced in this record.

## 6. Configuration and host isolation

Transcript metadata independently records:

    permissionMode
        default

    model
        claude-opus-5-5

    effort
        high

    cwd
        KEYA_WORK

Host postflight observed the active P2 Claude CLI process started at approximately 10:54 local time.

The P2 process had no connection to the active VS Code IDE listener.

A separate older Claude CLI process remained connected to VS Code, which is permitted by Research 336.

Therefore:

    P2_BATCH1_IDE_ISOLATION
        PASS

The owner reported the expected standalone external PowerShell launch. Host WMI ancestry inspection was unavailable under the Runtime Bridge read-only process permissions, so the task-owner evidence for the exact parent chain remains the owner report plus the already-qualified launch procedure. No IDE attachment or contradictory runtime evidence was observed.

## 7. Batch 1 freeze disposition

All Batch 1 acceptance gates passed.

Therefore:

    P2_BATCH1
        PASS

    BAT-2d0805e6c619
        PRIVATE_FROZEN

    SEMANTIC_LABELS
        PRIVATE

    BATCH1_REWRITE
        PROHIBITED_UNLESS_GOVERNED_CORRECTION_IS_OPENED

Before final P2 completion, the task owner must verify that Batch 1 bytes remain unchanged from this reviewed boundary.

## 8. Batch 2 continuation authority

Research 342 already records explicit owner authorization for the complete two-batch P2 phase.

Research 341 prospectively established that no second human authorization is required for Batch 2 after task-owner acceptance of Batch 1.

That acceptance is now complete.

Therefore:

    P2_BATCH2
        TASK_OWNER_RELEASED

The current Claude Code session may continue as the same logical Key Author A session because:

    model/configuration are unchanged
    no compaction occurred
    no restart occurred
    Batch 1 is frozen
    the same codebook/addendum/precedents remain in force

A replacement sequential session would also remain permissible under Research 334, but is not required.

## 9. Batch 2 exposure boundary

Batch 2 is:

    batch_id
        BAT-904613dd8a4e

    packet_event_id
        EVP-362b09ec98e9

    presentations
        264

Classification-session exposure is now limited to:

    lines 2068 through 4716 inclusive

Key-author development-event exposure is now limited to:

    lines 1832 through 4168 inclusive

The executor must not re-read Batch 1 semantic output or any attention-provenance mapping.

The frozen Batch 1 artifact must remain untouched.

## 10. Still-prohibited work

Batch 2 release does not authorize:

    BIRTH held-out classification
    BIRTH grouping
    LEGACY
    P1 STATE semantic output access
    attention-provenance access
    shell / Git / Python / web / repository queries
    canonical Key A assembly
    commitment generation

## 11. Current boundary

    P1_STATE=PASS
    P1_STATE_OUTPUT=PRIVATE_FROZEN

    P2_AUTHORIZED=true

    P2_BATCH1=PASS_PRIVATE_FROZEN
    P2_BATCH2=TASK_OWNER_RELEASED
    P2_COMPLETE=false

    BIRTH_HELDOUT_LABELS=NONE
    LEGACY_LABELS=NONE
    GROUPING_PAIRS=NONE
    COMPLETE_KEY_A_BYTES=NOT_CREATED

    NEXT=OWNER_CONTINUE_P2_BATCH2
