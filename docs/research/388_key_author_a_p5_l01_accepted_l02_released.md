# Research 388: Key Author A P5 L01 Accepted and L02 Released

**Date:** 2026-09-28
**Status:** L01 POSTFLIGHT PASS / L01 ACCEPTED / L02 PREPARATION PASS / FRESH L02 ATTEMPT 001 RELEASED
**Parent:** Research 387 / bounded P5 private-operation receipts
**Scope:** Reconcile the first P5 LEGACY classification batch after task-owner mechanical postflight, accept the frozen L01 artifact, prepare the exact next frozen batch, and release only L02 attempt 001 to a fresh Key Author A semantic session.
**Authority:** L01 acceptance and L02 attempt-001 semantic execution only. L03-L18 remain task-owner gated. candidate_gap, evidence_refs, witness/control selection, attention/provenance exposure, LEGACY grouping, canonical Key A assembly, commitment generation, Key Author B, scoring, production implementation, migration and authority switching remain unauthorized.

## 1. L01 executor return

The project owner returned the bounded L01 report:

    P5_BATCH_RESULT
        PASS

    batch key
        L01

    attempt
        1

    session ID
        0c45e7c2-c448-46d7-9811-fe222d3d1925

    model
        claude-opus-5-5

    effort
        high

    permission mode
        default

    batch ID
        LBAT-93e997b85fbc

    presentations
        297 / 297

    output
        out/legacy_classification/LBAT-93e997b85fbc.json

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
        L01

    attempt
        1

    sessionId
        0c45e7c2-c448-46d7-9811-fe222d3d1925

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
    predecessor acceptance/freeze surface
    fresh session
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

No semantic label, semantic-category count, attention identity, grouping identity, provenance mapping, or private digest was returned to the task owner.

## 3. L01 acceptance

The task owner then called the bounded acceptance operation for the same batch, attempt and session.

The receipt returned:

    accepted
        true

    nextBatchKey
        L02

    allClassificationBatchesAccepted
        false

    hiddenSemanticDetailsExposed
        false

Therefore:

    KEY_A_P5_L01=ACCEPTED_PRIVATE_FROZEN

The accepted L01 artifact is now part of the private predecessor surface that every later P5 batch must revalidate.

## 4. L02 deterministic preparation

The task owner then called:

    prepare_batch
        L02

The bounded preparation result was:

    preparation
        PASS

    batch key
        L02

    batch ID
        LBAT-9186ac12caec

    packet source ID
        LSP-4f1bc6ce3068

    part index
        1

    presentations expected
        156

    frozen source lines
        2985-4551 inclusive

    hidden semantic details exposed
        false

    next
        SEMANTIC_RELEASE_REQUIRES_TASK_OWNER

The preparation operation revalidated the accepted L01 predecessor surface before opening L02.

No later batch was prepared or exposed.

## 5. Task-owner L02 release

The task owner now releases exactly:

    P5 L02
    attempt 001

to one fresh standalone Key Author A Claude Code session.

Research 384 requires a fresh Claude Code session for every P5 batch. The accepted L01 session must not be continued or resumed.

Required execution configuration:

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

## 6. Authorized L02 semantic sources

The fresh L02 session may read the common P5 sources:

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

    lines 2985-4551 inclusive

The session must not read line 1-2984 or line 4552 and later.

It must not read the frozen L01 semantic artifact.

All prior P5 and pre-P5 confidentiality/source restrictions remain in force.

## 7. L02 semantic task

The executor independently classifies all 156 L02 presentations.

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

L02 attempt 001 writes exactly one semantic artifact:

    out/legacy_classification/LBAT-9186ac12caec.json

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
        LBAT-9186ac12caec

    packet_source_id
        LSP-4f1bc6ce3068

    part_index
        1

Presentation IDs must preserve the exact frozen L02 order.

## 9. Freeze and return boundary

After all 156 presentations are complete and internally reviewed:

    open_p5_batch
        null

    current_phase
        P5_LEGACY_CLASSIFICATION_L02_ATTEMPT_001_COMPLETE_AWAITING_REVIEW

L03 must not be exposed or prepared by the semantic executor.

The executor returns only the bounded non-secret report required by the P5 protocol, including the exact new Claude Code session UUID.

The task owner will use that UUID for bounded postflight before L02 can be accepted.

## 10. Current boundary

    KEY_A_P5_L01=ACCEPTED_PRIVATE_FROZEN
    KEY_A_P5_ACCEPTED_BATCH_COUNT=1

    KEY_A_P5_L02_PREPARATION=PASS
    KEY_A_P5_L02_BATCH_ID=LBAT-9186ac12caec
    KEY_A_P5_L02_PRESENTATIONS=156
    KEY_A_P5_L02_SOURCE_LINES=2985-4551
    KEY_A_P5_L02_ATTEMPT=001
    KEY_A_P5_L02_RELEASED=true

    KEY_A_P5_L03_RELEASED=false

    LEGACY_CANDIDATE_GAP=NOT_STARTED
    LEGACY_EVIDENCE=NOT_STARTED
    LEGACY_GROUPING=NOT_STARTED
    CANONICAL_KEY_A_ASSEMBLY=NOT_AUTHORIZED
    COMMITMENT_GENERATION=NOT_AUTHORIZED
    KEY_AUTHOR_B=NOT_AUTHORIZED
    MIGRATION=NOT_AUTHORIZED

    NEXT=OWNER_LAUNCH_FRESH_P5_L02_ATTEMPT001
