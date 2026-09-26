# Research 346: Key Author A P3 Explicit Owner Authorization and Held-Out Batch-1 Launch Boundary

**Date:** 2026-09-26
**Status:** P3 EXPLICITLY AUTHORIZED / BIRTH HELD-OUT ONLY / FRESH CLAUDE SESSION REQUIRED / BATCH 1 OWNER LAUNCH NEXT / BATCHES 2-13 TASK-OWNER GATED
**Parent:** Research 345 / project-owner explicit authorization
**Scope:** Preserve the owner's explicit authorization for the prospectively defined P3 BIRTH held-out classification phase, bind the mandatory fresh-session launch boundary, authorize Batch 1 execution, and retain task-owner gates before every later held-out batch is exposed.
**Authority:** Key Author A P3 authorization only. This authorizes the 13-batch BIRTH held-out classification phase defined by Research 345. It does not authorize BIRTH grouping, attention-consistency reconciliation, LEGACY, canonical Key A assembly, commitment generation, Key Author B, scoring, reviewer execution, production implementation, migration, oracle retirement, or authority switching.

## 1. Owner decision

The project owner explicitly stated:

    I authorize P3

This authorizes the complete prospectively defined P3 scope:

    P3 = BIRTH HELD-OUT CLASSIFICATION

with:

    11 opaque packet events
    2254 unique semantic items
    2347 classification presentations
    13 sequential batches

The authorization does not waive any sequential-exposure gate.

Only Batch 1 is immediately executable.

Batches 2 through 13 remain inaccessible until the ChatGPT task owner accepts the currently frozen batch and releases the next one.

No additional human authorization is required between P3 batches after this P3 authorization.

## 2. Mandatory fresh-session launch

P3 must start in a new Claude Code session.

The P2 Claude Code session:

    ae1c2ab7-0ae8-4263-8606-0b54de84e2ed

must not be continued or resumed for P3.

Launch must not use:

    --continue
    --resume

Reason:

    the P2 conversational context contains exact BIRTH development presentation labels

The only semantic carry-forward into P3 is the controlled private file state:

    work/CODEBOOK.md
    work/PRECEDENTS.md
    work/ERRATA.jsonl if needed
    frozen Key Author instructions/schema/addendum

P2 batch artifacts and P2 transcript/context remain forbidden.

## 3. Immediate Batch 1 scope

Batch 1:

    batch_id
        BAT-373ed51c1abb

    packet_event_id
        EVP-1b6edca704fa

    part_index
        1

    presentations
        20

Classification source:

    inputs/r2_v03/packets/birth_heldout_classification_sessions.json

Allowed Batch-1 range:

    lines 1 through 217 inclusive

Forbidden before Batch-1 acceptance:

    line 218 and later

Held-out key-author context:

    inputs/r2_v03/packets/key_author_birth_heldout.json

Allowed Batch-1 range:

    lines 1 through 157 inclusive

Forbidden before Batch-1 acceptance:

    line 158 and later

The executor must use bounded Read operations on both multi-batch/multi-event files.

## 4. Common allowed P3 sources

The fresh P3 session may read:

    work/PROGRESS.json
    work/CODEBOOK.md
    work/PRECEDENTS.md
    work/ERRATA.jsonl if needed

    inputs/r2_v03/KEY_AUTHOR_INSTRUCTIONS.md
    inputs/r2_v03/key_author_schema.json
    inputs/addendum/DRP03_R2_KEY_AUTHOR_EXECUTION_ADDENDUM_V01.md

The six P2 append-only precedents are valid carry-forward guidance.

The P3 session must not read:

    out/P1_STATE_EXPECTED_OUTPUTS.json
    work/P1_STATE_RULE_TRACE.md
    out/birth_development/**
    P2 transcript/context
    inputs/research330/**
    BIRTH grouping packets
    attention-provenance mappings
    LEGACY files
    repository checkouts
    other-key material
    unrelated workspace files

## 5. Execution configuration

P3 preserves the qualified Key Author A environment:

    model
        claude-opus-5-5

    effort
        high

    permission mode
        default / INTERACTIVE_APPROVAL

    launch surface
        standalone external Windows Terminal / PowerShell

    IDE attachment
        prohibited

    Chrome
        disabled

    MCP / web / GitHub
        disabled / denied

    .claude/settings.local.json
        absent

    parallel semantic workers
        prohibited

    subagent semantic workers
        prohibited

P3 classification requires no shell.

Therefore:

    Bash
    PowerShell
    Git
    Python
    terminal execution
    external process execution
    repository queries
        PROHIBITED

If shell use appears necessary:

    STOP / HOLD

## 6. Private progress transition

Before the first P3 semantic judgment, the fresh session must confirm:

    current_phase
        P2_BIRTH_DEVELOPMENT_COMPLETE_AWAITING_REVIEW

    p2_authorized
        true

    semantic_labels_created
        true

    frozen_batches
        includes BAT-2d0805e6c619
        includes BAT-904613dd8a4e

    open_batch
        null

Then record:

    p3_authorized
        true

    current_phase
        P3_BIRTH_HELDOUT_BATCH_01_IN_PROGRESS

    open_batch
        BAT-373ed51c1abb

If the fresh P3 session ID is available without shell use, append one P3 session record.

Do not introduce P4 or later authorization.

## 7. Batch-1 semantic task

Independently classify all 20 presentations in:

    BAT-373ed51c1abb

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

The semantic executor must not use:

    repeated text
    text hashes
    presentation similarity
    remembered development labels

as a mechanism for enforcing duplicate consistency.

No attention mapping is visible.

## 8. Batch-1 private artifact

Write exactly one P3 semantic artifact:

    out/birth_heldout/BAT-373ed51c1abb.json

with logical shape:

    {
      "schema_version": 1,
      "protocol_id": "AO10-DRP03-R2-V03",
      "component": "BIRTH",
      "split": "heldout",
      "batch_id": "BAT-373ed51c1abb",
      "packet_event_id": "EVP-1b6edca704fa",
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

No additional semantic output file is authorized during Batch 1.

PRECEDENTS.md remains append-only.

ERRATA.jsonl may be appended only if a genuine frozen-input issue is discovered.

## 9. Batch-1 freeze transition

After all 20 presentations are complete and internally reviewed:

    freeze out/birth_heldout/BAT-373ed51c1abb.json

Then update progress:

    append BAT-373ed51c1abb to frozen_batches

    open_batch
        null

    current_phase
        P3_BIRTH_HELDOUT_BATCH_01_COMPLETE_AWAITING_REVIEW

    p3_authorized
        true

Do not expose Batch 2.

Do not rewrite the frozen Batch-1 artifact after freeze.

If a post-freeze issue is discovered, report it to the task owner.

## 10. Return boundary

Return only:

    P3_BATCH_RESULT=PASS|HOLD|FAIL
    BATCH_NUMBER=1
    SESSION_ID=<id or NOT_EXPOSED>
    MODEL=<exact model>
    EFFORT=<exact effort>
    PERMISSION_MODE=<exact mode>
    EXTERNAL_TERMINAL=PASS|FAIL
    IDE_CONTEXT_ABSENT=PASS|FAIL
    MCP_DISABLED=PASS|FAIL
    WEB_DENIED=PASS|FAIL
    LOCAL_SETTINGS_ABSENT=PASS|FAIL
    BATCH_ID=BAT-373ed51c1abb
    PRESENTATIONS_EXPECTED=20
    PRESENTATIONS_COMPLETED=<count>
    OUTPUT_PATH=out/birth_heldout/BAT-373ed51c1abb.json
    OUTPUT_SCHEMA_COMPLETE=PASS|FAIL
    PRECEDENTS_ADDED_THIS_BATCH=<count>
    ERRATA_ADDED_THIS_BATCH=<count>
    BATCH_FROZEN=true|false
    NEXT_BATCH_EXPOSED=false
    SHELL_USED=false
    GROUPING_STARTED=false
    LEGACY_STARTED=false
    P3_COMPLETE=false

The executor must not return:

    presentation labels
    semantic category counts
    attention identities
    semantic precedents
    semantic excerpts
    grouping information

The human owner must paste only the bounded final report back to ChatGPT.

## 11. Authorization state

    P1_STATE=PASS
    P2_BIRTH_DEVELOPMENT=PASS

    P3_READY=true
    P3_AUTHORIZED=true
    P3_SCOPE=BIRTH_HELDOUT_CLASSIFICATION

    P3_BATCH1=AUTHORIZED_FOR_EXECUTION
    P3_BATCHES_2_13=AUTHORIZED_IN_PRINCIPLE_BUT_TASK_OWNER_GATED

    BIRTH_GROUPING_AUTHORIZED=false
    LEGACY_AUTHORIZED=false
    COMPLETE_KEY_A_BYTES=NOT_CREATED

    NEXT=OWNER_LAUNCH_FRESH_P3_BATCH1_SESSION
