# Research 364: Key Author A P4 Explicit Owner Authorization and BIRTH Grouping D01 Launch Boundary

**Date:** 2026-09-27
**Status:** P4 EXPLICITLY AUTHORIZED / BIRTH GROUPING ONLY / FRESH CLAUDE SESSION REQUIRED / DEVELOPMENT D01 OWNER LAUNCH NEXT / ALL LATER EVENTS TASK-OWNER GATED
**Parent:** Research 363 / project-owner explicit authorization
**Scope:** Preserve the owner's explicit authorization for the prospectively defined P4 BIRTH grouping phase, bind the mandatory fresh-session launch boundary, authorize development grouping D01 execution, and retain task-owner gates before every later grouping event is exposed.
**Authority:** Key Author A P4 authorization only. This authorizes the 13-event BIRTH grouping phase defined by Research 363. It does not authorize classification-label repair, LEGACY, canonical Key A assembly, commitment generation, Key Author B, construct-validity comparison, scoring, reviewer execution, production implementation, migration, oracle retirement, or authority switching.

## 1. Owner decision

The project owner explicitly stated:

    I authorize P4. Proceed.

This authorizes the complete prospectively defined P4 scope:

    P4 = BIRTH GROUPING

with:

    development grouping
        2 packet events
        455 unique semantic items

    held-out grouping
        11 packet events
        2254 unique semantic items

The authorization does not waive any event-level exposure gate.

Only development grouping D01 is immediately executable.

D02 and held-out H01-H11 remain inaccessible until the ChatGPT task owner accepts the currently frozen grouping event and releases the next one.

No additional human authorization is required between P4 events after this P4 authorization.

## 2. Mandatory fresh-session launch

P4 must start in a new Claude Code session.

No P3 classification session may be continued or resumed for P4.

Launch must not use:

    --continue
    --resume

Reason:

    P3 conversational state contains presentation-level classification judgments

Grouping uses the unique semantic-item catalog and must not inherit an implicit presentation-to-item mapping from classification conversation state.

The only semantic carry-forward into P4 is controlled private file state:

    work/CODEBOOK.md
    work/PRECEDENTS.md
    work/ERRATA.jsonl if genuinely needed
    frozen Key Author instructions/schema/addendum

Frozen P1/P2/P3 semantic artifacts and prior Claude transcripts remain forbidden.

## 3. Immediate D01 scope

Grouping batch:

    D01

Packet event:

    EVP-ca475c9a5a9d

Unique semantic items:

    199

Grouping source:

    inputs/r2_v03/packets/birth_development.json

Allowed D01 range:

    lines 9 through 1810 inclusive

Forbidden before D01 acceptance:

    line 1811 and later

The executor must use bounded Read operations on the multi-event grouping catalog.

## 4. Common allowed P4 sources

The fresh P4 session may read:

    work/PROGRESS.json
    work/CODEBOOK.md
    work/PRECEDENTS.md
    work/ERRATA.jsonl if genuinely needed

    inputs/r2_v03/KEY_AUTHOR_INSTRUCTIONS.md
    inputs/r2_v03/key_author_schema.json
    inputs/addendum/DRP03_R2_KEY_AUTHOR_EXECUTION_ADDENDUM_V01.md

and only the currently released event range from the appropriate unique BIRTH grouping catalog.

PRECEDENTS.md remains append-only.

A new grouping precedent may be added only if it is genuinely reusable, not already represented, not tied to a specific event/item pair, and not a disguised pair-result list.

The fresh P4 session must not read:

    out/P1_STATE_EXPECTED_OUTPUTS.json
    work/P1_STATE_RULE_TRACE.md
    out/birth_development/**
    out/birth_heldout/**
    any attention-provenance file
    any prior Claude transcript
    inputs/research330/**
    any prior grouping artifact
    LEGACY packets
    LEGACY provenance
    STATE provenance
    repository checkouts
    other-key material
    unrelated workspace files

## 5. Execution configuration

P4 preserves the qualified Key Author A environment:

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

P4 grouping requires no shell.

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

Before the first P4 semantic judgment, the fresh session must confirm the accepted P3 boundary:

    current_phase
        P3_BIRTH_HELDOUT_COMPLETE_AWAITING_REVIEW

    p3_authorized
        true

    semantic_labels_created
        true

    frozen_batches
        contains both P2 development batches
        contains all thirteen P3 held-out batches

    frozen batch count
        15

    open_batch
        null

    compaction_events
        1

    restarts
        4

    open_batch_corrections
        0

    errata_count
        0

P4 grouping state does not yet exist in the private progress file.

Before semantic work, add exactly these P4 fields without altering prior history:

    p4_authorized
        true

    grouping_frozen_events
        []

    open_grouping_event
        EVP-ca475c9a5a9d

    grouping_sessions
        []

Set:

    current_phase
        P4_BIRTH_GROUPING_DEVELOPMENT_D01_IN_PROGRESS

If the fresh P4 session ID is available without shell use, append one grouping-session record for D01.

Do not remove or rewrite any prior classification session record.

Do not introduce P5 or later authorization.

## 7. D01 grouping task

Review the 199 unique semantic items in the released D01 event.

P4 does not construct a canonical partition.

For any pair actually stored, use exactly one of:

    MUST_JOIN
    MUST_SPLIT

Every other pair remains:

    UNCONSTRAINED

and is represented by absence from both stored lists.

MUST_JOIN may be stored only when the exact pair is individually reviewed and all four conditions are confirmed:

    same realization act/effect would satisfy both
    same evidence event/path is sufficient to demonstrate both
    same qualification/admission decision closes both
    failure of either is the same realization failure rather than independently remediable failure

MUST_SPLIT may be stored only when the exact pair is individually reviewed and at least one independent realization/evidence/qualification/failure boundary is confirmed.

Do not infer pair outcomes automatically from:

    lexical similarity
    repeated wording
    shared heading
    adjacency
    source identity
    candidate family membership
    thematic similarity

Candidate generation may prioritize review only.

Every stored pair must be individually reconsidered before it is written.

Do not add pairs to satisfy a sample floor.

Do not attempt to count toward the later held-out floor.

## 8. Pair rules

Grouping scope is:

    within current packet_event_id only

Cross-event pairs are prohibited.

Within the current event, cross-source pairs are allowed.

For every stored pair:

    item_id_a < item_id_b
        lexicographically

    item_id_a != item_id_b

    both endpoints exist in EVP-ca475c9a5a9d

    pair appears at most once

    pair appears in exactly one of must_join_pairs or must_split_pairs

    reason is non-empty and specific to the exact pair

Sort each pair list by:

    (item_id_a, item_id_b, reason)

## 9. D01 private artifact

Write exactly one new semantic grouping artifact:

    out/birth_grouping/development/EVP-ca475c9a5a9d.json

with exact top-level shape:

    {
      "schema_version": 1,
      "protocol_id": "AO10-DRP03-R2-V03",
      "component": "BIRTH",
      "split": "development",
      "packet_event_id": "EVP-ca475c9a5a9d",
      "must_join_pairs": [
        {
          "item_id_a": "...",
          "item_id_b": "...",
          "reason": "..."
        }
      ],
      "must_split_pairs": [
        {
          "item_id_a": "...",
          "item_id_b": "...",
          "reason": "..."
        }
      ]
    }

No additional semantic output file is authorized during D01.

Do not enumerate UNCONSTRAINED pairs.

## 10. Source-query boundary

For:

    inputs/r2_v03/packets/birth_development.json

use only explicitly bounded Read operations entirely within lines 9-1810 inclusive.

Do not use:

    Grep
    search
    count
    Glob
    pattern matching
    unrestricted/full-file Read

against the grouping catalog.

Mechanical artifact validation may query only the newly created D01 artifact.

If reasoning appears to require D02, held-out grouping, prior classification outputs, attention provenance, LEGACY or another event:

    HOLD

## 11. D01 freeze transition

After D01 grouping is complete and internally reviewed:

    freeze
        out/birth_grouping/development/EVP-ca475c9a5a9d.json

Then update progress:

    append EVP-ca475c9a5a9d
        to grouping_frozen_events

    open_grouping_event
        null

    current_phase
        P4_BIRTH_GROUPING_D01_COMPLETE_AWAITING_REVIEW

    p4_authorized
        true

Retain:

    all prior classification state
    compaction_events = 1
    restarts = 4
    open_batch_corrections = 0
    existing errata count unless a genuine governed erratum was appended

Do not expose D02.

Do not reread or revise the frozen D01 artifact after freeze.

If a post-freeze issue is discovered, report it rather than silently editing a frozen artifact.

## 12. Compaction rule

If compaction occurs while D01 is open:

    STOP IMMEDIATELY WITH HOLD

Do not issue another semantic Read after detecting the compaction boundary.

If a model/configuration mismatch is detected while D01 is open:

    HOLD

## 13. Return boundary

Return only:

    P4_GROUPING_RESULT=PASS|HOLD|FAIL
    GROUPING_BATCH=D01
    SESSION_ID=<id or NOT_EXPOSED>
    MODEL=<exact model>
    EFFORT=<exact effort or NOT_EXPOSED_IN_SESSION>
    PERMISSION_MODE=<exact mode or NOT_EXPOSED_IN_SESSION>
    EXTERNAL_TERMINAL=PASS|FAIL
    IDE_CONTEXT_ABSENT=PASS|FAIL
    MCP_DISABLED=PASS|FAIL
    WEB_DENIED=PASS|FAIL
    LOCAL_SETTINGS_ABSENT=PASS|FAIL
    PACKET_EVENT_ID=EVP-ca475c9a5a9d
    UNIQUE_ITEMS_EXPECTED=199
    OUTPUT_PATH=out/birth_grouping/development/EVP-ca475c9a5a9d.json
    OUTPUT_SCHEMA_COMPLETE=PASS|FAIL
    PRECEDENTS_ADDED_THIS_BATCH=<count>
    ERRATA_ADDED_THIS_BATCH=<count>
    GROUPING_ARTIFACT_FROZEN=true|false
    NEXT_EVENT_EXPOSED=false
    OUT_OF_SCOPE_SOURCE_QUERY_USED=false
    SHELL_USED=false
    LEGACY_STARTED=false
    CANONICAL_KEY_STARTED=false
    P4_COMPLETE=false

Do not return:

    pair identities
    pair reasons
    MUST_JOIN count
    MUST_SPLIT count
    classification labels
    attention identities
    semantic excerpts
    LEGACY information

## 14. Authorization state

    P1_STATE=PASS
    P2_BIRTH_DEVELOPMENT=PASS
    P3_BIRTH_HELDOUT=PASS
    KEY_A_BIRTH_ATTENTION_QUALITY=PASS

    P4_READY=true
    P4_AUTHORIZED=true
    P4_SCOPE=BIRTH_GROUPING

    P4_D01=AUTHORIZED_FOR_EXECUTION
    P4_D02_AND_H01_H11=AUTHORIZED_IN_PRINCIPLE_BUT_TASK_OWNER_GATED

    LEGACY_AUTHORIZED=false
    CANONICAL_KEY_A_ASSEMBLY_AUTHORIZED=false
    COMPLETE_KEY_A_BYTES=NOT_CREATED

    NEXT=OWNER_LAUNCH_FRESH_P4_D01_SESSION
