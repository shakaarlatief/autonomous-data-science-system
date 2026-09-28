# Research 389: Key Author A P5 L02 Accepted and L03 Released

**Date:** 2026-09-28
**Status:** L02 POSTFLIGHT PASS / L02 ACCEPTED / L03 PREPARATION PASS / FRESH L03 ATTEMPT 001 RELEASED
**Parent:** Research 388 / bounded P5 private-operation receipts
**Scope:** Reconcile the second P5 LEGACY classification batch after task-owner mechanical postflight, accept the frozen L02 artifact, prepare the exact next frozen batch, and release only L03 attempt 001 to a fresh Key Author A semantic session.
**Authority:** L02 acceptance and L03 attempt-001 semantic execution only. L04-L18 remain task-owner gated. candidate_gap, evidence_refs, witness/control selection, attention/provenance exposure, LEGACY grouping, canonical Key A assembly, commitment generation, Key Author B, scoring, production implementation, migration and authority switching remain unauthorized.

## 1. L02 executor return

The project owner returned the bounded L02 report:

    P5_BATCH_RESULT
        PASS

    batch key
        L02

    attempt
        1

    session ID
        70c761c0-fc90-449c-abe8-8a2f90426e93

    model
        claude-opus-5-5

    effort
        high

    permission mode
        default

    batch ID
        LBAT-9186ac12caec

    presentations
        156 / 156

    output
        out/legacy_classification/LBAT-9186ac12caec.json

    output schema
        PASS

    batch frozen
        true

    next batch exposed
        false

    shell / MCP / web
        false / false / false

    compaction
        false

    candidate_gap / evidence / grouping
        not started

The bounded return did not expose semantic labels or hidden semantic counts.

## 2. Task-owner bounded postflight

The task owner ran the qualified purpose-specific P5 postflight against:

    batchKey
        L02

    attempt
        1

    sessionId
        70c761c0-fc90-449c-abe8-8a2f90426e93

The result was:

    overallPostflight
        PASS

    hiddenSemanticDetailsExposed
        false

Every bounded verifier check passed, including:

    progress phase
    P5 authorization/interface version
    predecessor state
    batch closure
    target not previously accepted
    accepted predecessor order/records
    predecessor artifact freeze and schema validity
    predecessor session uniqueness
    fresh current session
    exact artifact schema
    exact presentation count
    exact presentation ID set/order
    presentation uniqueness
    exact presentation object shape
    field types
    normative-kind enum
    normative-kind implication
    transcript session/model/permission/cwd
    no compaction
    no forbidden tool
    required current-batch source read
    bounded catalog reads
    required common-source reads
    no forbidden source read
    ERRATA-before-PRECEDENTS ordering
    one-write artifact freeze
    append-only precedents
    append-only errata
    absence of local settings override

No hidden semantic detail was returned to the task owner.

## 3. L02 acceptance

The task owner called bounded acceptance for L02 attempt 001 and the exact fresh session.

The receipt returned:

    accepted
        true

    nextBatchKey
        L03

    allClassificationBatchesAccepted
        false

    hiddenSemanticDetailsExposed
        false

Therefore:

    KEY_A_P5_L02=ACCEPTED_PRIVATE_FROZEN

The accepted P5 predecessor prefix is now exactly L01, L02.

## 4. L03 deterministic preparation

The task owner then called:

    prepare_batch
        L03

The bounded preparation result was:

    preparation
        PASS

    batch key
        L03

    batch ID
        LBAT-c8da030cfb5d

    packet source ID
        LSP-8b58f8ed9f58

    part index
        1

    presentations expected
        279

    frozen source lines
        4552-7348 inclusive

    hidden semantic details exposed
        false

    next
        SEMANTIC_RELEASE_REQUIRES_TASK_OWNER

The bounded operation revalidated the accepted L01-L02 predecessor surface before opening L03.

No later batch was prepared or exposed.

## 5. Task-owner L03 release

The task owner now releases exactly:

    P5 L03
    attempt 001

to one fresh standalone Key Author A Claude Code session.

Research 384 requires a fresh Claude Code session for every P5 batch. Neither L01 nor L02 may be continued or resumed.

Required execution configuration remains:

    model
        claude-opus-5-5

    effort
        high

    permission mode
        default / interactive approval

    standalone external terminal
        required

    IDE context
        absent

    Chrome
        absent

    MCP
        disabled

    web
        denied

    shell / terminal execution inside Claude Code
        prohibited

    Git / repository queries
        prohibited

    Agent / subagent / parallel semantic workers
        prohibited

## 6. Authorized L03 semantic sources

The fresh L03 session may read the common P5 sources:

    work/PROGRESS.json
    work/CODEBOOK.md
    work/ERRATA.jsonl
    work/PRECEDENTS.md

    inputs/r2_v03/KEY_AUTHOR_INSTRUCTIONS.md
    inputs/r2_v03/key_author_schema.json
    inputs/addendum/DRP03_R2_KEY_AUTHOR_EXECUTION_ADDENDUM_V01.md

ERRATA must be read before PRECEDENTS.

The only authorized batch source is:

    inputs/r2_v03/packets/legacy_classification_sessions.json

with the exact line boundary:

    lines 4552-7348 inclusive

The session must not read lines 1-4551 or line 7349 and later.

It must not read the frozen L01 or L02 semantic artifacts.

All earlier confidentiality/source restrictions remain in force.

## 7. L03 semantic task

The executor independently classifies all 279 L03 presentations.

Each presentation receives exactly:

    presentation_id
    normative
    normative_kind
    material
    realization_required

Allowed normative_kind values remain:

    OBLIGATION
    CONSTRAINT
    DISPOSITION
    SEQUENCING
    PRINCIPLE
    null

Invariant:

    normative=false
        -> normative_kind=null

    normative=true
        -> normative_kind is one of the five non-null frozen kinds

P5 still does not author:

    candidate_gap
    evidence_refs
    witness/control identity
    grouping
    attention mappings
    source provenance
    negative-control identity

## 8. Attempt-001 private artifact

L03 attempt 001 writes exactly one semantic artifact:

    out/legacy_classification/LBAT-c8da030cfb5d.json

The artifact is written once and is not edited after the write.

Top-level fields remain exactly:

    schema_version
    protocol_id
    component
    phase
    batch_id
    packet_source_id
    part_index
    presentations

with:

    schema_version
        1

    protocol_id
        AO10-DRP03-R2-V03

    component
        LEGACY

    phase
        classification

    batch_id
        LBAT-c8da030cfb5d

    packet_source_id
        LSP-8b58f8ed9f58

    part_index
        1

Presentation IDs must preserve the exact frozen L03 order.

## 9. Freeze and return boundary

After all 279 presentations are complete and internally reviewed:

    open_p5_batch
        null

    current_phase
        P5_LEGACY_CLASSIFICATION_L03_ATTEMPT_001_COMPLETE_AWAITING_REVIEW

L04 must not be exposed or prepared by the semantic executor.

The executor returns only the bounded non-secret report required by the P5 protocol, including the exact new Claude Code session UUID.

The task owner will use that UUID for bounded postflight before L03 can be accepted.

## 10. Current boundary

    KEY_A_P5_L01=ACCEPTED_PRIVATE_FROZEN
    KEY_A_P5_L02=ACCEPTED_PRIVATE_FROZEN
    KEY_A_P5_ACCEPTED_BATCH_COUNT=2

    KEY_A_P5_L03_PREPARATION=PASS
    KEY_A_P5_L03_BATCH_ID=LBAT-c8da030cfb5d
    KEY_A_P5_L03_PRESENTATIONS=279
    KEY_A_P5_L03_SOURCE_LINES=4552-7348
    KEY_A_P5_L03_ATTEMPT=001
    KEY_A_P5_L03_RELEASED=true

    KEY_A_P5_L04_RELEASED=false

    LEGACY_CANDIDATE_GAP=NOT_STARTED
    LEGACY_EVIDENCE=NOT_STARTED
    LEGACY_GROUPING=NOT_STARTED
    CANONICAL_KEY_A_ASSEMBLY=NOT_AUTHORIZED
    COMMITMENT_GENERATION=NOT_AUTHORIZED
    KEY_AUTHOR_B=NOT_AUTHORIZED
    MIGRATION=NOT_AUTHORIZED

    NEXT=OWNER_LAUNCH_FRESH_P5_L03_ATTEMPT001
