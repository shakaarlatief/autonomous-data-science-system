# Research 363: Key Author A P4 BIRTH Grouping Phase Design

**Date:** 2026-09-26
**Status:** P4 BIRTH GROUPING DEFINED PROSPECTIVELY / READY FOR OWNER AUTHORIZATION / NO GROUPING EXECUTED
**Parent:** Research 362
**Scope:** Define the complete Key Author A BIRTH grouping phase after all BIRTH classification and the post-freeze attention-quality gate have passed.
**Authority:** Design only. This record does not authorize grouping execution, LEGACY, canonical Key A assembly, commitment generation, Key Author B, scoring, reviewer execution, production implementation, migration, oracle retirement or authority switching.

## 1. Preconditions

P4 becomes eligible only because the following are now true:

    P1 STATE
        PASS / PRIVATE FROZEN

    P2 BIRTH development classification
        PASS / PRIVATE FROZEN

    P3 BIRTH held-out classification
        PASS / PRIVATE FROZEN

    all BIRTH classification
        FROZEN

    Key Author A BIRTH attention-quality gate
        PASS

    quality replacement required
        false

    BIRTH grouping catalog exposure
        now eligible under Research 332 / Research 345

No grouping output exists yet.

## 2. P4 scope

P4 is:

    BIRTH GROUPING

It covers both frozen BIRTH splits:

    development
        2 packet events
        455 unique semantic items

    held-out
        11 packet events
        2254 unique semantic items

P4 does not include:

    classification-label changes
    attention-driven label repair
    LEGACY classification
    LEGACY grouping
    STATE changes
    canonical Key A assembly
    Key A commitment
    Key Author B
    construct-validity comparison
    scoring
    decision reviewers

The grouping stage never authorizes revision of P1/P2/P3 semantic artifacts.

## 3. Why development and held-out grouping are one governed phase

The frozen delivery plan exposes BIRTH grouping after all BIRTH classification freezes and provides two unique grouping catalogs:

    birth_development.json
    birth_heldout.json

P4 therefore owns BIRTH grouping as one semantic phase, while preserving the development/held-out evaluation boundary internally.

Development grouping is completed first.

Held-out grouping begins only after all development grouping artifacts are frozen and task-owner accepted.

A fresh Claude Code session is mandatory at the development-to-held-out grouping boundary.

This permits development grouping to refine reusable append-only grouping interpretations while preventing exact development pair memory from carrying conversationally into held-out grouping.

The owner may authorize the complete P4 phase once. Event batches after the first remain task-owner gated and do not require repeated human authorization.

## 4. Fresh P4 start

P4 must begin in a fresh Claude Code session.

Do not continue or resume any P3 classification session.

Reason:

    P3 conversational state contains presentation-level classification judgments.

Grouping uses stable semantic item IDs from a different unique catalog.

A fresh start prevents incidental presentation-level memory from becoming an implicit presentation-to-item mapping.

The P4 executor remains the same logical Key Author A under Research 334.

## 5. Grouping truth model

P4 does not construct a canonical partition.

The frozen rule remains:

    MUST_JOIN
        store only when both items may share one ObligationUnit and all four realization-boundary conditions are individually confirmed

    MUST_SPLIT
        store only when at least one independent realization/evidence/qualification/failure boundary is individually confirmed

    UNCONSTRAINED
        every unreviewed, uncertain or insufficiently supported pair

The four MUST_JOIN conditions are:

    same realization act or effect would satisfy both
    same evidence event/path is sufficient to demonstrate both
    same qualification/admission decision closes both
    failure of either is the same realization failure rather than independently remediable failure

No absence of a stored pair implies MUST_SPLIT.

No candidate-family rule may promote an unreviewed pair.

No pair may be added merely to satisfy a sample floor.

## 6. Grouping scope

The addendum freezes grouping scope as:

    BIRTH
        within one packet_event_id only

Cross-event pairs are outside the scoring surface and must never be stored.

Within one event, cross-source pairs are allowed because the BIRTH grouping scope is the packet event, not the source.

Every stored pair must satisfy:

    item_id_a < item_id_b
        lexicographically

    item_id_a != item_id_b

    both endpoints exist in the current packet event

    pair appears at most once

    pair appears in exactly one of MUST_JOIN or MUST_SPLIT

    reason is a non-empty item-pair-specific explanation

Pair lists are sorted by:

    (item_id_a, item_id_b, reason)

## 7. Relationship to frozen classifications

The grouping semantic author must not read:

    P2 classification artifacts
    P3 classification artifacts
    attention-provenance mappings

The unique grouping catalog is the semantic source supplied to the grouping author.

The task owner, outside the semantic author session, may mechanically use the frozen attention mapping and frozen classification artifacts to verify that every grouping endpoint corresponds to a semantic item whose frozen primary classification has:

    realization_required = true

This hidden mechanical consistency check does not change labels and does not reveal attention identities or prior classification outputs to the semantic author.

A grouping artifact that contains an endpoint inconsistent with frozen realization_required truth does not authorize label repair.

It is a grouping-phase failure/hold requiring task-owner disposition under the frozen no-repair rule.

## 8. Allowed common sources

A P4 semantic session may read:

    work/PROGRESS.json
    work/CODEBOOK.md
    work/PRECEDENTS.md
    work/ERRATA.jsonl if genuinely needed
    inputs/r2_v03/KEY_AUTHOR_INSTRUCTIONS.md
    inputs/r2_v03/key_author_schema.json
    inputs/addendum/DRP03_R2_KEY_AUTHOR_EXECUTION_ADDENDUM_V01.md
    only the currently released event range from the appropriate unique BIRTH grouping catalog

PRECEDENTS.md remains append-only.

A new precedent may be added only when it is:

    genuinely reusable
    not already represented
    not tied to a specific event ID or item pair
    not a disguised list of pair outcomes

Grouping-specific reusable reasoning may be carried from development into held-out through this append-only mechanism.

## 9. Forbidden sources

The P4 semantic author must not read:

    out/P1_STATE_EXPECTED_OUTPUTS.json
    work/P1_STATE_RULE_TRACE.md
    out/birth_development/**
    out/birth_heldout/**
    any attention-provenance file
    any prior Claude transcript
    inputs/research330/**
    LEGACY packets
    LEGACY provenance
    STATE provenance
    repository checkouts
    other-key material
    unrelated workspace files

After the first grouping event freezes, the semantic author must not reread prior frozen grouping artifacts either.

Only PRECEDENTS.md carries reusable semantic guidance forward.

## 10. Deterministic P4 event sequence

P4 uses one grouping event per task-owner gate.

This avoids quadratic whole-component exposure and matches the frozen within-event scoring scope.

### Development grouping

| Batch | Event | Unique items | Catalog range |
|---:|---|---:|---|
| D01 | EVP-ca475c9a5a9d | 199 | birth_development.json lines 9-1810 |
| D02 | EVP-362b09ec98e9 | 256 | birth_development.json lines 1811-4125 |

After D02 passes task-owner review:

    development grouping
        PRIVATE FROZEN

    current development grouping session
        RETIRE

    held-out grouping
        begin in a fresh sequential P4 session

### Held-out grouping

| Batch | Event | Unique items | Catalog range |
|---:|---|---:|---|
| H01 | EVP-1b6edca704fa | 15 | birth_heldout.json lines 9-154 |
| H02 | EVP-1b53b3b00c6c | 216 | birth_heldout.json lines 155-2109 |
| H03 | EVP-819a9953b12b | 371 | birth_heldout.json lines 2110-5464 |
| H04 | EVP-d8bfe7b48f85 | 65 | birth_heldout.json lines 5465-6060 |
| H05 | EVP-ba08dc62e616 | 63 | birth_heldout.json lines 6061-6638 |
| H06 | EVP-dca0fcb4fb4d | 124 | birth_heldout.json lines 6639-7765 |
| H07 | EVP-838a4c21407b | 124 | birth_heldout.json lines 7766-8892 |
| H08 | EVP-3ad3b2e576e0 | 124 | birth_heldout.json lines 8893-10019 |
| H09 | EVP-ffd3c3f9f874 | 436 | birth_heldout.json lines 10020-13959 |
| H10 | EVP-e9498b2ad950 | 20 | birth_heldout.json lines 13960-14150 |
| H11 | EVP-63516d4b5c63 | 696 | birth_heldout.json lines 14151-20440 |

The event ranges include the event decision token, source identity, headings/context and unique semantic item IDs required for grouping.

No later event range may be exposed before the current event artifact is frozen and task-owner accepted.

## 11. Source-query boundary

For the two multi-event grouping catalogs:

    use only explicitly bounded Read operations
    do not Grep the catalog
    do not search/count the catalog
    do not Glob semantic source
    do not perform unrestricted/full-file Read

Artifact validation may query only the newly created current-event grouping artifact.

If current-event reasoning appears to require a different event, prior frozen output, attention provenance or LEGACY material:

    HOLD

## 12. Working artifact schema

Each event produces exactly one private grouping artifact.

Development path:

    out/birth_grouping/development/<packet_event_id>.json

Held-out path:

    out/birth_grouping/heldout/<packet_event_id>.json

Exact top-level shape:

    {
      "schema_version": 1,
      "protocol_id": "AO10-DRP03-R2-V03",
      "component": "BIRTH",
      "split": "development|heldout",
      "packet_event_id": "...",
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

These are private working semantic artifacts.

They are not yet the canonical Key A bytes.

UNCONSTRAINED pairs are represented by absence from both stored lists and are not enumerated.

## 13. Candidate generation

P4 must remain non-quadratic in semantic review burden.

The author may identify candidate pairs using current-event content and private reasoning attributes such as:

    likely realization owner
    realization act/effect
    evidence boundary
    qualification/admission boundary
    independent failure/remediation boundary
    heading/table context
    source identity within the same event

Candidate generation is only a prioritization device.

For every stored pair, the author must individually reconsider the exact two items and explicitly confirm the stored outcome.

No candidate family, lexical similarity, shared heading, source adjacency or sampling rule may automatically populate pair outcomes.

All unconfirmed pairs remain UNCONSTRAINED.

## 14. Mechanical event acceptance gate

For each frozen event artifact, the task owner independently checks without publishing pair identities:

    exact top-level fields
    exact protocol/component/split/event metadata
    pair object fields exactly item_id_a/item_id_b/reason
    endpoint existence in current event
    endpoints distinct
    lexicographic endpoint order
    no duplicate pairs
    MUST_JOIN / MUST_SPLIT disjointness
    deterministic list order
    non-empty reasons
    no cross-event endpoint
    every endpoint mechanically maps to frozen realization_required=true truth
    no prior frozen grouping artifact mutation
    PRECEDENTS append-only if changed
    ERRATA governed if changed
    source exposure stayed inside current event
    no forbidden source/tool exposure

No pair identities or reasons are published by the task owner during P4.

## 15. Held-out grouping floor

After all eleven held-out grouping event artifacts freeze, the task owner mechanically evaluates the frozen Research 330 held-out floor:

    MUST_JOIN pairs >= 15
    total constrained pairs >= 30

The author must not be told a running pair count for the purpose of reaching the floor.

No padding is allowed.

If either floor fails:

    grouping evidence
        INCONCLUSIVE

The floor failure does not authorize adding pairs after freeze.

## 16. Session / compaction rules

P4 start:

    fresh session required

Development D01-D02:

    same session may continue after each accepted event

Development-to-held-out boundary:

    mandatory fresh session

Held-out H01-H11:

    same session may continue after each accepted event
    fresh replacement may be required or proactively chosen at an accepted event boundary

Compaction:

    while no grouping event is open
        task-owner review before continuation

    while a grouping event is open
        HOLD

Model/configuration change:

    HOLD

Parallel semantic sessions:

    prohibited

Subagent semantic workers:

    prohibited

All session IDs are retained in private progress provenance.

## 17. Tool boundary

P4 semantic grouping requires no shell.

Prohibited:

    Bash
    PowerShell
    Git
    Python
    terminal execution
    repository queries
    external process execution
    WebSearch
    WebFetch
    GitHub
    MCP
    IDE tools
    Agent/subagent semantic workers

The session remains a standalone external Claude Code terminal with model claude-opus-5-5, effort high and permission mode default.

## 18. Progress-state extension

P4 authorization, if granted, adds explicit grouping state without altering prior phase history:

    p4_authorized
        true

    grouping_frozen_events
        []

    open_grouping_event
        null

    grouping_sessions
        []

Initial phase:

    P4_BIRTH_GROUPING_DEVELOPMENT_D01_READY

When an event is open:

    open_grouping_event
        current packet_event_id

When an event freezes:

    append packet_event_id to grouping_frozen_events
    open_grouping_event = null
    current_phase = P4_BIRTH_GROUPING_<DNN_OR_HNN>_COMPLETE_AWAITING_REVIEW

After all 13 grouping events freeze and pass:

    current_phase
        P4_BIRTH_GROUPING_COMPLETE_AWAITING_REVIEW

No P5/later authorization may be introduced by P4 execution.

## 19. Bounded executor report

After each event the executor returns only:

    P4_GROUPING_RESULT=PASS|HOLD|FAIL
    GROUPING_BATCH=D01|D02|H01..H11
    SESSION_ID=<id or NOT_EXPOSED>
    MODEL=<model>
    EFFORT=<effort or NOT_EXPOSED_IN_SESSION>
    PERMISSION_MODE=<mode or NOT_EXPOSED_IN_SESSION>
    EXTERNAL_TERMINAL=PASS|FAIL
    IDE_CONTEXT_ABSENT=PASS|FAIL
    MCP_DISABLED=PASS|FAIL
    WEB_DENIED=PASS|FAIL
    LOCAL_SETTINGS_ABSENT=PASS|FAIL
    PACKET_EVENT_ID=<event>
    UNIQUE_ITEMS_EXPECTED=<count>
    OUTPUT_PATH=<private relative path>
    OUTPUT_SCHEMA_COMPLETE=PASS|FAIL
    PRECEDENTS_ADDED_THIS_BATCH=<count>
    ERRATA_ADDED_THIS_BATCH=<count>
    GROUPING_ARTIFACT_FROZEN=true|false
    NEXT_EVENT_EXPOSED=false
    OUT_OF_SCOPE_SOURCE_QUERY_USED=false
    SHELL_USED=false
    LEGACY_STARTED=false
    CANONICAL_KEY_STARTED=false
    P4_COMPLETE=true|false

Do not return:

    pair identities
    pair reasons
    MUST_JOIN count
    MUST_SPLIT count
    classification labels
    attention identities
    semantic excerpts
    LEGACY information

## 20. Authorization boundary

This research freezes the P4 execution design only.

Current state:

    P4_READY=true
    P4_AUTHORIZED=false

No grouping catalog may be exposed to a semantic author until the project owner explicitly authorizes P4.

If the owner authorizes P4, task-owner release begins with development grouping D01 only.

## 21. Current boundary

    P1_STATE=PASS
    P2_BIRTH_DEVELOPMENT=PASS
    P3_BIRTH_HELDOUT=PASS
    KEY_A_BIRTH_ATTENTION_QUALITY=PASS

    ALL_BIRTH_CLASSIFICATION=PRIVATE_FROZEN

    P4_SCOPE=BIRTH_GROUPING
    P4_EVENT_COUNT=13
    P4_DEVELOPMENT_EVENTS=2
    P4_HELDOUT_EVENTS=11
    P4_FRESH_START_REQUIRED=true
    P4_FRESH_HELDOUT_BOUNDARY_REQUIRED=true
    P4_READY=true
    P4_AUTHORIZED=false

    LEGACY=NOT_STARTED
    COMPLETE_KEY_A_BYTES=NOT_CREATED

    NEXT=OWNER_P4_AUTHORIZATION_DECISION
