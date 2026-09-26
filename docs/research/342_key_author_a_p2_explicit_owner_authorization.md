# Research 342: Key Author A P2 Explicit Owner Authorization and Batch-1 Launch Boundary

**Date:** 2026-09-26
**Status:** P2 EXPLICITLY AUTHORIZED / BIRTH DEVELOPMENT ONLY / BATCH 1 OWNER LAUNCH NEXT / BATCH 2 HELD BEHIND TASK-OWNER GATE
**Parent:** Research 341 / project-owner explicit authorization
**Scope:** Preserve the owner's explicit authorization for the prospectively defined P2 BIRTH development phase, bind the batch-1 execution contract, and preserve the mandatory task-owner review gate before batch 2 exposure.
**Authority:** Key Author A P2 authorization only. This authorizes the two-batch BIRTH development classification phase defined by Research 341, but does not authorize BIRTH held-out classification, BIRTH grouping, LEGACY, canonical Key A assembly, commitment generation, Key Author B, scoring, reviewer execution, production implementation, migration, oracle retirement, or authority switching.

## 1. Owner decision

The project owner explicitly stated:

    I authorize P2

This authorizes the complete prospectively defined P2 scope from Research 341:

    P2 = BIRTH DEVELOPMENT CLASSIFICATION

with exactly:

    batch 1
        BAT-2d0805e6c619
        205 presentations

    batch 2
        BAT-904613dd8a4e
        264 presentations

    total
        469 presentations

This authorization does not waive the frozen sequential-exposure control.

Batch 2 remains operationally inaccessible until the task owner accepts frozen batch 1.

## 2. Current launch scope

The immediate executable scope is:

    P2 / batch 1 only

The executor may not expose batch 2 during the first run segment.

The mandatory batch-1 stop gate from Research 341 remains in force.

After batch-1 semantic output is frozen, the executor must stop and return a bounded non-secret report.

Only the ChatGPT task owner may release batch 2 after mechanical artifact, transcript, configuration and host-isolation review.

No second human semantic authorization is required for batch 2 because the owner has already authorized the entire prospectively frozen P2 scope.

## 3. Batch-1 frozen evidence ranges

Classification-session source:

    inputs/r2_v03/packets/birth_development_classification_sessions.json

Allowed during batch 1:

    lines 1 through 2067 inclusive

Forbidden during batch 1:

    line 2068 and later

Key-author development context:

    inputs/r2_v03/packets/key_author_birth_development.json

Allowed during batch 1:

    lines 1 through 1831 inclusive

Forbidden during batch 1:

    line 1832 and later

The semantic executor must use bounded Read operations.

If one bounded read is too large for the tool, it may use multiple smaller Read calls, but the union of read ranges must remain entirely inside the authorized bounds.

No unrestricted/full-file Read is permitted on either multi-batch file.

## 4. Common allowed P2 sources

The executor may read:

    work/PROGRESS.json
    work/CODEBOOK.md
    work/PRECEDENTS.md
    work/ERRATA.jsonl if genuinely needed

    inputs/r2_v03/KEY_AUTHOR_INSTRUCTIONS.md
    inputs/r2_v03/key_author_schema.json
    inputs/addendum/DRP03_R2_KEY_AUTHOR_EXECUTION_ADDENDUM_V01.md

It must not read:

    out/P1_STATE_EXPECTED_OUTPUTS.json
    work/P1_STATE_RULE_TRACE.md
    inputs/research330/**
    BIRTH held-out files
    BIRTH grouping packets
    LEGACY files
    attention-provenance mappings
    Claude transcripts
    repository checkouts
    other-key material
    unrelated workspace files

## 5. P2 execution configuration

P2 preserves the qualified Key Author A environment:

    model
        claude-opus-5-5

    effort
        high

    permission mode
        default / INTERACTIVE_APPROVAL

    terminal
        standalone external Windows Terminal / PowerShell

    IDE attachment
        prohibited

    Chrome
        disabled

    MCP / web / GitHub
        disabled / denied

    .claude/settings.local.json
        absent

    subagents / parallel semantic workers
        prohibited

P2 batch classification requires no shell.

Therefore:

    Bash / PowerShell / terminal / Git / Python / external process use
        PROHIBITED

If shell execution appears necessary:

    STOP / HOLD

## 6. Private progress transition

Before the first batch-1 semantic judgment, the executor must mechanically verify:

    current_phase
        P1_STATE_COMPLETE_AWAITING_REVIEW

    p1_authorized
        true

    semantic_labels_created
        true

    frozen_batches
        []

    open_batch
        null

Then record:

    p2_authorized
        true

    current_phase
        P2_BIRTH_DEVELOPMENT_BATCH1_IN_PROGRESS

    open_batch
        BAT-2d0805e6c619

If the current session ID is available without shell execution, append a P2 session record.

No P3 or later authorization field may be introduced.

## 7. Batch-1 semantic task

Classify all 205 presentations in:

    BAT-2d0805e6c619

independently.

Each presentation receives exactly:

    presentation_id
    normative
    normative_kind
    material
    realization_required
    restated
    decision_time_delta
    ambiguity

Allowed normative_kind values:

    OBLIGATION
    CONSTRAINT
    DISPOSITION
    SEQUENCING
    PRINCIPLE
    null

The author must not use repeated text, text hashes, cross-presentation similarity or remembered prior labels as a mechanism to enforce duplicate consistency.

No attention mapping is visible during P2 classification.

## 8. Batch-1 private artifact

Write exactly one semantic batch artifact:

    out/birth_development/BAT-2d0805e6c619.json

with logical shape:

    {
      "schema_version": 1,
      "protocol_id": "AO10-DRP03-R2-V03",
      "component": "BIRTH",
      "split": "development",
      "batch_id": "BAT-2d0805e6c619",
      "packet_event_id": "EVP-ca475c9a5a9d",
      "part_index": 1,
      "presentations": [
        {
          "presentation_id": "...",
          "normative": true | false,
          "normative_kind": "OBLIGATION" | "CONSTRAINT" | "DISPOSITION" | "SEQUENCING" | "PRINCIPLE" | null,
          "material": true | false,
          "realization_required": true | false,
          "restated": true | false,
          "decision_time_delta": true | false,
          "ambiguity": true | false
        }
      ]
    }

No additional semantic output file is authorized in batch 1.

Reusable semantic interpretations may be appended to PRECEDENTS.md only when genuinely necessary.

Existing precedents are append-only and may not be edited or deleted.

ERRATA.jsonl may be appended only if an actual frozen-input issue is discovered.

## 9. Batch-1 freeze transition

After all 205 presentation labels are complete and internally reviewed:

    treat the batch artifact as frozen

Then update progress mechanically:

    frozen_batches
        append BAT-2d0805e6c619

    open_batch
        null

    current_phase
        P2_BIRTH_DEVELOPMENT_BATCH1_COMPLETE_AWAITING_REVIEW

    p2_authorized
        true

Do not expose batch 2.

Do not reopen or revise the frozen batch-1 artifact during the same session after declaring it frozen.

If an issue is discovered after freeze, report it to the task owner rather than silently rewriting the batch.

## 10. Return boundary

Return only a bounded non-secret report.

Allowed report fields:

    P2_BATCH1_RESULT=PASS|HOLD|FAIL
    SESSION_ID=<id or NOT_EXPOSED>
    MODEL=<exact model>
    EFFORT=<exact effort>
    PERMISSION_MODE=<exact mode>
    EXTERNAL_TERMINAL=PASS|FAIL
    IDE_CONTEXT_ABSENT=PASS|FAIL
    MCP_DISABLED=PASS|FAIL
    WEB_DENIED=PASS|FAIL
    LOCAL_SETTINGS_ABSENT=PASS|FAIL
    BATCH_ID=BAT-2d0805e6c619
    PRESENTATIONS_EXPECTED=205
    PRESENTATIONS_COMPLETED=<count>
    OUTPUT_PATH=out/birth_development/BAT-2d0805e6c619.json
    OUTPUT_SCHEMA_COMPLETE=PASS|FAIL
    PRECEDENTS_ADDED=<count>
    ERRATA_ADDED=<count>
    BATCH_FROZEN=true|false
    BATCH2_EXPOSED=false
    SHELL_USED=false
    P2_COMPLETE=false

The executor must not return:

    presentation-level labels
    normative-kind counts
    material counts
    realization-required counts
    restated counts or identities
    decision-time-delta counts or identities
    ambiguity counts or identities
    semantic precedents
    semantic excerpts from the batch artifact

The human owner must paste only this bounded final report back to ChatGPT, not Claude Code tool previews.

## 11. Authorization state

    P1_STATE=PASS
    P1_STATE_OUTPUT=PRIVATE_FROZEN

    P2_READY=true
    P2_AUTHORIZED=true
    P2_SCOPE=BIRTH_DEVELOPMENT_CLASSIFICATION

    P2_BATCH1=AUTHORIZED_FOR_EXECUTION
    P2_BATCH2=AUTHORIZED_IN_PRINCIPLE_BUT_NOT_YET_EXPOSABLE

    BIRTH_HELDOUT_AUTHORIZED=false
    BIRTH_GROUPING_AUTHORIZED=false
    LEGACY_AUTHORIZED=false

    COMPLETE_KEY_A_BYTES=NOT_CREATED

    NEXT=OWNER_LAUNCH_P2_BATCH1
