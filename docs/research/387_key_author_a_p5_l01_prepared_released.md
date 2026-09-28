# Research 387: Key Author A P5 L01 Prepared and Released

**Date:** 2026-09-28
**Status:** P5 TOOL SURFACE REFRESHED / L01 PREPARATION PASS / L01 ATTEMPT 001 RELEASED / NO LEGACY LABEL CREATED YET
**Parent:** Research 386 / fresh ChatGPT interaction chatgpt-33
**Scope:** Reconcile the fresh interaction-level Runtime Bridge surface required by Research 386, invoke the bounded P5 activation/preparation controls without generic private-workspace access, and release only the first frozen LEGACY classification batch to a fresh Key Author A semantic session.
**Authority:** L01 attempt-001 semantic execution only. L02-L18 remain task-owner gated. candidate_gap, evidence_refs, witness/control selection, LEGACY grouping, attention/provenance exposure, canonical Key A assembly, commitment generation, Key Author B, scoring, production implementation, migration and authority switching remain unauthorized.

## 1. Fresh interaction and tool-surface reconciliation

The new persistent ChatGPT interaction is:

    interaction session
        chatgpt-33

    conversation title
        33 - Semantic Qualification and Architecture Evolution

The public interaction provenance was reconciled before new semantic work at commit:

    8cc3f2ad1e5ea8fc832a50d1c566147b68cc7952

Unlike chatgpt-32, this interaction exposes the purpose-specific bounded Runtime Bridge capability:

    codex.p5_private_operation

with the qualified action set:

    activate_phase
    prepare_batch
    postflight_attempt
    accept_attempt
    reject_attempt

Generic private-workspace shell access was not substituted.

## 2. Bounded activation observation

The task owner called:

    activate_phase

The bounded receipt returned:

    ok
        true

    activation
        ALREADY_ACTIVE

    p5Authorized
        true

    batchCount
        18

    presentationsTotal
        3210

    acceptedBatchCount
        0

    nextBatchKey
        L01

    hiddenSemanticDetailsExposed
        false

This receipt establishes that the private P5 control state was already active when chatgpt-33 first exercised the qualified interface. It does not establish when that private activation first occurred and does not imply any earlier semantic release.

The safety-relevant facts are unchanged:

    accepted P5 batches
        0

    next batch
        L01

    hidden semantic details exposed
        false

    LEGACY labels created by this task-owner action
        none

The earlier public statement that the interaction-local tool refresh was still required is therefore superseded by this observed bounded receipt.

## 3. L01 bounded preparation result

The task owner then called:

    prepare_batch
        L01

The bounded receipt returned:

    preparation
        PASS

    batch key
        L01

    batch ID
        LBAT-93e997b85fbc

    packet source ID
        LSP-157dfb537436

    part index
        1

    presentations expected
        297

    frozen source lines
        1-2984 inclusive

    hidden semantic details exposed
        false

    next
        SEMANTIC_RELEASE_REQUIRES_TASK_OWNER

No later batch was prepared or exposed.

## 4. Task-owner L01 release

The task owner now releases exactly:

    P5 L01
    attempt 001

to one fresh standalone Key Author A Claude Code session.

This release does not expose or authorize L02.

The semantic executor must use:

    model
        claude-opus-5-5

    effort
        high

    permission mode
        default / interactive approval

    launch surface
        fresh standalone external Windows Terminal / PowerShell

    IDE context
        absent

    Chrome
        absent

    MCP
        disabled

    web
        denied

    shell / terminal execution from inside Claude Code
        prohibited

    Git / repository queries
        prohibited

    Agent / subagent / parallel semantic workers
        prohibited

The L01 session must not continue or resume any P1-P4 semantic session.

## 5. Allowed L01 semantic sources

The fresh L01 session may read only the common P5 sources:

    work/PROGRESS.json
    work/CODEBOOK.md
    work/ERRATA.jsonl
    work/PRECEDENTS.md

    inputs/r2_v03/KEY_AUTHOR_INSTRUCTIONS.md
    inputs/r2_v03/key_author_schema.json
    inputs/addendum/DRP03_R2_KEY_AUTHOR_EXECUTION_ADDENDUM_V01.md

plus exactly the current batch range from:

    inputs/r2_v03/packets/legacy_classification_sessions.json
        lines 1-2984 inclusive

ERRATA must be read before PRECEDENTS.

The session must not read any later range of the multi-batch LEGACY classification file.

The session must not read:

    prior P1 STATE semantic output
    frozen P2/P3 BIRTH classification artifacts
    P4 BIRTH grouping artifacts
    BIRTH attention provenance
    LEGACY attention provenance
    LEGACY unique grouping catalog
    LEGACY provenance
    LEGACY corpus manifest
    frozen LEGACY evidence checkout
    any live ADS repository checkout
    another key author's material
    reviewer annotations
    scoring artifacts
    unrelated local files
    web or connector sources

## 6. L01 semantic scope

The executor independently classifies all 297 L01 presentations.

Each presentation receives exactly:

    presentation_id
    normative
    normative_kind
    material
    realization_required

Allowed normative_kind values are:

    OBLIGATION
    CONSTRAINT
    DISPOSITION
    SEQUENCING
    PRINCIPLE
    null

The invariant is:

    normative=false
        -> normative_kind=null

    normative=true
        -> normative_kind is non-null and in the frozen enum

The semantic author must not derive or inspect:

    candidate_gap
    evidence_refs
    witness/control identities
    grouping
    attention mappings
    source provenance
    negative-control identity

## 7. Attempt-001 private artifact

Attempt 001 writes exactly one new semantic artifact:

    out/legacy_classification/LBAT-93e997b85fbc.json

The artifact must be written once and must not be edited after that write.

Its exact top-level fields are:

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
        LBAT-93e997b85fbc

    packet_source_id
        LSP-157dfb537436

    part_index
        1

The presentations must preserve the exact frozen L01 presentation-ID order.

## 8. Progress and freeze boundary

The prepared private state owns L01 as the currently open batch.

During execution the semantic session may update only the authorized private progress state plus the append-only precedent/errata surfaces and the one L01 artifact.

At successful freeze the final private progress boundary must be:

    current_phase
        P5_LEGACY_CLASSIFICATION_L01_ATTEMPT_001_COMPLETE_AWAITING_REVIEW

    open_p5_batch
        null

The task owner will then call the bounded postflight operation using the exact returned Claude session UUID.

L02 remains inaccessible until L01 postflight passes and L01 is explicitly accepted through the bounded control plane.

## 9. Bounded executor return

The semantic executor returns only a bounded non-secret report containing at least:

    P5_BATCH_RESULT=PASS|HOLD|FAIL
    BATCH_KEY=L01
    ATTEMPT=1
    SESSION_ID=<uuid>
    MODEL=claude-opus-5-5
    EFFORT=high
    PERMISSION_MODE=default
    BATCH_ID=LBAT-93e997b85fbc
    PRESENTATIONS_EXPECTED=297
    PRESENTATIONS_COMPLETED=<count>
    OUTPUT_PATH=out/legacy_classification/LBAT-93e997b85fbc.json
    OUTPUT_SCHEMA_COMPLETE=PASS|FAIL
    BATCH_FROZEN=true|false
    NEXT_BATCH_EXPOSED=false
    SHELL_USED=false
    MCP_USED=false
    WEB_USED=false
    COMPACTION_OCCURRED=false
    CANDIDATE_GAP_STARTED=false
    EVIDENCE_STARTED=false
    GROUPING_STARTED=false

The executor must not return:

    presentation labels
    normative-kind counts
    material counts
    realization-required counts
    duplicate or attention identities
    negative-control identities
    semantic precedents
    semantic rationales
    candidate-gap identities
    evidence results

## 10. Current boundary

    KEY_A_P5_DESIGN=ACCEPTED
    KEY_A_P5_AUTHORIZED=true
    KEY_A_P5_PRIVATE_OPS_RUNTIME_READY=true
    KEY_A_P5_CURRENT_CHAT_TOOL_EXPOSED=true
    KEY_A_P5_ACTIVATION_OBSERVATION=ALREADY_ACTIVE
    KEY_A_P5_ACCEPTED_BATCHES=0

    KEY_A_P5_L01_PREPARATION=PASS
    KEY_A_P5_L01_RELEASED=true
    KEY_A_P5_L01_ATTEMPT=1
    KEY_A_P5_L01_LABELS_CREATED=false
    KEY_A_P5_L02_RELEASED=false

    LEGACY_CANDIDATE_GAP=NOT_STARTED
    LEGACY_EVIDENCE=NOT_STARTED
    LEGACY_GROUPING=NOT_STARTED
    CANONICAL_KEY_A_ASSEMBLY=NOT_AUTHORIZED
    COMMITMENT_GENERATION=NOT_AUTHORIZED
    KEY_AUTHOR_B=NOT_AUTHORIZED
    MIGRATION=NOT_AUTHORIZED

    NEXT=OWNER_LAUNCH_FRESH_P5_L01_ATTEMPT001
