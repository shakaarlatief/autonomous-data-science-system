# Research 390: Key Author A P5 L03 Accepted and L04 Released

**Date:** 2026-09-28
**Status:** L03 POSTFLIGHT PASS / L03 ACCEPTED / L04 PREPARATION PASS / FRESH L04 ATTEMPT 001 RELEASED
**Parent:** Research 389
**Scope:** Accept frozen L03 after bounded postflight, prepare exact next batch L04, and release only L04 attempt 001.
**Authority:** L03 acceptance and L04 semantic execution only. L05-L18 and all later LEGACY phases remain gated.

## L03 result and bounded postflight

The owner returned:

    P5_BATCH_RESULT=PASS
    BATCH_KEY=L03
    ATTEMPT=1
    SESSION_ID=79a1e003-a733-4147-ad21-f323789ec3e4
    MODEL=claude-opus-5-5
    EFFORT=high
    PERMISSION_MODE=default
    BATCH_ID=LBAT-c8da030cfb5d
    PRESENTATIONS_EXPECTED=279
    PRESENTATIONS_COMPLETED=279
    OUTPUT_PATH=out/legacy_classification/LBAT-c8da030cfb5d.json
    OUTPUT_SCHEMA_COMPLETE=PASS
    BATCH_FROZEN=true
    NEXT_BATCH_EXPOSED=false
    SHELL_USED=false
    MCP_USED=false
    WEB_USED=false
    COMPACTION_OCCURRED=false
    CANDIDATE_GAP_STARTED=false
    EVIDENCE_STARTED=false
    GROUPING_STARTED=false

The task owner called bounded postflight for L03 attempt 001 and that exact session. overallPostflight=PASS and hiddenSemanticDetailsExposed=false.

Every bounded verifier check passed, including authorization/interface state, predecessor acceptance/freeze validity, fresh-session uniqueness, artifact schema and exact presentation order, field/invariant checks, transcript identity/configuration/cwd, bounded source reads, absence of forbidden tool/source use, no compaction, required common-source reads, ERRATA-before-PRECEDENTS ordering, one-write artifact freeze, append-only precedents/errata, and absence of local settings override.

## L03 acceptance

Bounded acceptance returned:

    accepted=true
    nextBatchKey=L04
    allClassificationBatchesAccepted=false
    hiddenSemanticDetailsExposed=false

Therefore:

    KEY_A_P5_L03=ACCEPTED_PRIVATE_FROZEN
    KEY_A_P5_ACCEPTED_BATCH_COUNT=3

The accepted prefix is exactly L01-L03.

## L04 preparation and release

Bounded preparation returned:

    batch key
        L04
    batch ID
        LBAT-2a2a2c500d59
    packet source ID
        LSP-816d7caf56ea
    part index
        1
    presentations expected
        63
    frozen source lines
        7349-7985 inclusive
    preparation
        PASS
    hidden semantic details exposed
        false

The task owner releases exactly P5 L04 attempt 001 to one fresh standalone Key Author A Claude Code session. Research 384 requires a fresh session for every P5 batch.

The only authorized batch source range is:

    inputs/r2_v03/packets/legacy_classification_sessions.json
        lines 7349-7985 inclusive

L04 must not read lines 1-7348 or line 7986 and later, and it must not read frozen L01-L03 semantic artifacts.

The executor independently classifies all 63 presentations with exactly:

    presentation_id
    normative
    normative_kind
    material
    realization_required

Allowed normative_kind values remain OBLIGATION, CONSTRAINT, DISPOSITION, SEQUENCING, PRINCIPLE, or null, with normative=false implying normative_kind=null.

The one-write output artifact is:

    out/legacy_classification/LBAT-2a2a2c500d59.json

with batch ID LBAT-2a2a2c500d59, packet source ID LSP-816d7caf56ea, part index 1, and the standard P5 classification schema.

At successful freeze:

    open_p5_batch=null
    current_phase=P5_LEGACY_CLASSIFICATION_L04_ATTEMPT_001_COMPLETE_AWAITING_REVIEW

L05 must not be exposed or prepared by the semantic executor.

## Current boundary

    KEY_A_P5_L01=ACCEPTED_PRIVATE_FROZEN
    KEY_A_P5_L02=ACCEPTED_PRIVATE_FROZEN
    KEY_A_P5_L03=ACCEPTED_PRIVATE_FROZEN
    KEY_A_P5_ACCEPTED_BATCH_COUNT=3
    KEY_A_P5_L04_PREPARATION=PASS
    KEY_A_P5_L04_BATCH_ID=LBAT-2a2a2c500d59
    KEY_A_P5_L04_PRESENTATIONS=63
    KEY_A_P5_L04_SOURCE_LINES=7349-7985
    KEY_A_P5_L04_ATTEMPT=001
    KEY_A_P5_L04_RELEASED=true
    KEY_A_P5_L05_RELEASED=false
    LEGACY_CANDIDATE_GAP=NOT_STARTED
    LEGACY_EVIDENCE=NOT_STARTED
    LEGACY_GROUPING=NOT_STARTED
    CANONICAL_KEY_A_ASSEMBLY=NOT_AUTHORIZED
    COMMITMENT_GENERATION=NOT_AUTHORIZED
    KEY_AUTHOR_B=NOT_AUTHORIZED
    MIGRATION=NOT_AUTHORIZED
    NEXT=OWNER_LAUNCH_FRESH_P5_L04_ATTEMPT001
