# Research 368: Key Author A P4 D01 Eligibility Projection Preparation PASS and Attempt 003 Release

**Date:** 2026-09-27
**Status:** D01 ELIGIBILITY PROJECTION PREPARATION PASS / AMENDED INTERFACE ACTIVE / FRESH ATTEMPT 003 RELEASED / D02 STILL GATED
**Parent:** Research 367 / owner-run deterministic private preparation receipt
**Scope:** Record successful preparation of the first amended P4 event-scoped frozen eligibility projection, preserve the rejected attempt-002 disposition, and release a fresh D01 attempt 003 under the owner-amended P4 interface.
**Authority:** D01 attempt-003 semantic execution only. D02 and held-out grouping remain task-owner gated. This does not authorize classification repair, LEGACY, canonical Key A assembly, Key Author B, scoring, production implementation, migration, oracle retirement, or authority switching.

## 1. Owner-run preparation result

The project owner executed the deterministic private preparation required by Research 367.

Every published preparation check passed:

    accepted-events state                 PASS
    attempt-002 completion boundary       PASS
    attempt-002 rejection provenance      PASS
    attempt-002 artifact presence         PASS
    frozen-classification completeness    PASS
    frozen-presentation uniqueness        PASS
    errata count                          PASS
    event closed                          PASS
    event item IDs unique                 PASS
    event unique                          PASS
    primary mapping complete              PASS
    primary mapping unique                PASS
    projection event scope                PASS
    projection exact frozen eligibility   PASS
    projection fields exact               PASS
    projection IDs unique                 PASS
    projection provenance recorded        PASS
    projection reload exact               PASS
    projection sorted                     PASS
    restart count unchanged               PASS
    attempt-003 prepared phase            PASS

Overall:

    OVERALL_PREPARATION=PASS

No eligible item IDs or eligibility count were exposed in the owner-visible receipt.

## 2. Prepared private state

The private Key Author A workspace now records:

    current_phase
        P4_BIRTH_GROUPING_D01_ATTEMPT_003_PREPARED_AWAITING_RELEASE

    open_grouping_event
        null

    restarts
        5

    grouping_accepted_events
        empty

    D01 attempt 002
        recorded rejected

    P4 grouping interface
        ELIGIBILITY_PROJECTION_V01

The D01 eligibility projection exists at the private path defined by Research 367 and has been mechanically verified exact against frozen Key-A primary realization-required truth.

The task owner does not publish:

    eligible item IDs
    eligibility count
    projection digest
    frozen label identities
    attention mappings

## 3. Attempt 003 release

A fresh D01 attempt 003 semantic session is now released.

Attempt 003 must use:

    fresh standalone Claude Code session
    model claude-opus-5-5
    effort high
    permission mode default
    no IDE context
    no Chrome
    no MCP
    no web
    no shell
    no Agent/subagent
    no parallel semantic worker

The session must not continue or resume either rejected D01 attempt.

## 4. Attempt 003 semantic source boundary

Attempt 003 may read:

    work/PROGRESS.json
    work/CODEBOOK.md
    work/ERRATA.jsonl
    work/PRECEDENTS.md
    inputs/r2_v03/KEY_AUTHOR_INSTRUCTIONS.md
    inputs/r2_v03/key_author_schema.json
    inputs/addendum/DRP03_R2_KEY_AUTHOR_EXECUTION_ADDENDUM_V01.md
    work/grouping_eligibility/development/EVP-ca475c9a5a9d.json
    birth_development.json lines 9-1810 only

The session must not read:

    any P2/P3 classification artifact
    attention provenance
    attempt-001 grouping artifact
    attempt-002 grouping artifact
    prior Claude transcript
    D02 source range
    held-out grouping source
    LEGACY
    repository checkout
    other-key material

## 5. Endpoint authority

For attempt 003:

    endpoint eligibility is owned by the frozen projection

The semantic author must not independently reclassify endpoint eligibility.

A pair may be stored only when:

    both endpoint IDs appear in eligible_item_ids

The author then applies the already-frozen pairwise grouping semantics.

The projection provides no pair candidate or pair result.

## 6. Pairwise truth model unchanged

For eligible endpoints:

    MUST_JOIN
        only when all four frozen realization-boundary conditions are individually confirmed

    MUST_SPLIT
        only when at least one independent realization/evidence/qualification/failure boundary is individually confirmed

    UNCONSTRAINED
        all unreviewed, uncertain or insufficiently supported pairs

No candidate-generation rule may automatically create a pair outcome.

No padding is allowed.

Every stored pair remains individually reviewed.

## 7. Attempt-003 artifact

Attempt 003 writes exactly one new private semantic artifact:

    out/birth_grouping/development/EVP-ca475c9a5a9d.attempt003.json

The rejected attempt-001 and attempt-002 artifacts remain immutable and forbidden to the semantic session.

The semantic schema remains unchanged.

## 8. Progress transition

At attempt-003 start:

    increment restarts
        5 -> 6

    set open_grouping_event
        EVP-ca475c9a5a9d

    set current_phase
        P4_BIRTH_GROUPING_DEVELOPMENT_D01_ATTEMPT_003_IN_PROGRESS

    append fresh grouping-session provenance if session ID is available without shell use

At successful semantic freeze:

    open_grouping_event
        null

    current_phase
        P4_BIRTH_GROUPING_D01_ATTEMPT_003_COMPLETE_AWAITING_REVIEW

    grouping_accepted_events
        remains empty until task-owner review

Do not add duplicate D01 event values to grouping_frozen_events.

## 9. Current boundary

    P4_AUTHORIZED=true
    P4_ELIGIBILITY_INTERFACE=V0.1_FROZEN
    D01_PROJECTION_PREPARATION=PASS

    D01_ATTEMPT_001=HOLD_REJECTED
    D01_ATTEMPT_002=HOLD_REJECTED
    D01_ATTEMPT_003=RELEASED

    D02_RELEASED=false
    HELDOUT_GROUPING_RELEASED=false

    CLASSIFICATION_REPAIR_AUTHORIZED=false
    LEGACY_AUTHORIZED=false
    CANONICAL_KEY_A_ASSEMBLY_AUTHORIZED=false
    MIGRATION_AUTHORIZED=false

    NEXT=OWNER_LAUNCH_FRESH_P4_D01_ATTEMPT_003
