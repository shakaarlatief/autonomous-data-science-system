# Research 371: Key Author A P4 Development Grouping Accepted and H01 Released

**Date:** 2026-09-27
**Status:** D02 ATTEMPTS 001-002 REJECTED / ATTEMPT 003 ACCEPTED / DEVELOPMENT GROUPING COMPLETE / H01 PREPARATION PASS / H01 SEMANTIC EXECUTION RELEASED
**Parent:** Research 370 / bounded D02 task-owner postflight and recovery sequence
**Scope:** Preserve the complete D02 attempt sequence, accept the first D02 attempt that passes the full bounded postflight, close the P4 development-grouping segment, prepare the first held-out event through the qualified bounded private-operation capability, and release H01 only across the mandatory fresh-session boundary.
**Authority:** D02 acceptance and H01 semantic execution only. H02-H11, classification repair, LEGACY, canonical Key A assembly, commitment generation, Key Author B, scoring, production implementation, migration, oracle retirement and authority switching remain unauthorized.

## 1. D02 attempt 001

The development-grouping session returned a bounded PASS report for D02 attempt 001, but independent task-owner postflight did not accept that self-report.

Bounded postflight result:

    overallPostflight
        FAIL

The material failing controls were:

    catalogReadsBounded
        false

    noForbiddenSourceRead
        false

All hidden semantic details remained undisclosed.

Disposition:

    D02 attempt 001
        PRIVATE / FROZEN / REJECTED / NONCANONICAL

    reason
        SOURCE_BOUNDARY

No semantic repair or artifact rewrite was authorized.

The bounded capability then re-prepared D02 and again verified the frozen eligibility projection exactly.

## 2. D02 attempt 002

A fresh standalone development-grouping session executed replacement attempt 002.

Its source/tool boundary corrected the attempt-001 defect:

    catalogReadsBounded
        true

    eligibilityProjectionRead
        true

    noForbiddenSourceRead
        true

    noForbiddenTool
        true

Independent postflight nevertheless failed the complete acceptance gate. The bounded receipt reported, among other dependent mechanical failures:

    progressPhaseOk
        false

    pairShapeOk
        false

    errataReadBeforePrecedents
        false

The attempt therefore remained unacceptable despite the executor's bounded PASS report.

Disposition:

    D02 attempt 002
        PRIVATE / FROZEN / REJECTED / NONCANONICAL

    reason
        ARTIFACT_INVALID

No frozen artifact was edited.

The bounded capability then re-prepared D02 and again verified the frozen eligibility projection exactly.

## 3. D02 attempt 003

A second fresh standalone replacement session executed D02 attempt 003:

    session
        c418e325-b7c2-46b4-be9d-fbcf4a057b2e

    model
        claude-opus-5-5

Independent bounded postflight returned:

    overallPostflight
        PASS

Every published check passed:

    progress boundary
    P4 authorization
    interface version
    event closure
    accepted predecessors
    target not already accepted
    projection provenance
    projection schema
    projection uniqueness/order/event scope
    exact projection equality to frozen same-key eligibility truth
    artifact schema
    pair shape
    endpoint event scope
    endpoint eligibility-projection membership
    endpoint distinctness
    lexical order
    pair reasons
    duplicate absence
    join/split disjointness
    deterministic pair ordering
    local-settings absence
    transcript session/model/permission identity
    no compaction
    no prohibited tool
    bounded catalog reads
    eligibility-projection use
    no forbidden source read
    ERRATA-before-PRECEDENTS ordering
    write-once artifact behavior
    append-only precedent behavior
    append-only errata behavior

No hidden semantic detail was exposed.

The bounded acceptance operation reran the complete postflight and accepted attempt 003.

Result:

    D02 attempt 003
        ACCEPTED

Only attempt 003 is accepted for downstream Key A construction.

## 4. Development-grouping closure

D01 attempt 003 and D02 attempt 003 are now accepted.

Therefore:

    P4 BIRTH development grouping
        COMPLETE / PRIVATE FROZEN

All development-grouping Claude Code sessions now retire.

No development session may continue into held-out grouping.

This preserves the mandatory development-to-held-out session separation frozen in Research 363 and Research 367.

## 5. H01 preparation

The bounded private-operation capability prepared the first held-out grouping event:

    batch
        H01

    packet event
        EVP-1b6edca704fa

    unique semantic items
        15

    catalog range
        birth_heldout.json lines 9-154 inclusive

Preparation returned:

    preparation
        PASS

    projectionExactFrozenEligibility
        true

    hiddenSemanticDetailsExposed
        false

No eligible IDs, counts, pair identities, classifications, attention mappings or private digests were exposed.

## 6. H01 semantic release

H01 is now released only to a mandatory fresh standalone Claude Code session.

The fresh held-out session must preserve:

    eligibility projection V0.1
    classification immutability
    event-local grouping only
    pairwise individual review
    MUST_JOIN all-four-condition rule
    MUST_SPLIT independent-boundary rule
    UNCONSTRAINED by absence
    no padding
    bounded H01 source only
    no development grouping artifact reads
    no prior grouping transcript reads
    no classification/attention reads
    no shell/web/MCP/IDE/Agent semantic worker

No later held-out event may be exposed before H01 freezes and passes task-owner review.

## 7. Current boundary

    P4_AUTHORIZED=true
    P4_ELIGIBILITY_INTERFACE=V0.1_FROZEN

    D01_ATTEMPT_003=ACCEPTED

    D02_ATTEMPT_001=HOLD_REJECTED_SOURCE_BOUNDARY
    D02_ATTEMPT_002=HOLD_REJECTED_ARTIFACT_INVALID
    D02_ATTEMPT_003=ACCEPTED

    P4_DEVELOPMENT_GROUPING=COMPLETE
    DEVELOPMENT_GROUPING_SESSIONS=RETIRED

    H01_PROJECTION_PREPARATION=PASS
    H01_SEMANTIC_EXECUTION=RELEASED
    H01_FRESH_SESSION_REQUIRED=true

    H02_H11_RELEASED=false

    CLASSIFICATION_REPAIR_AUTHORIZED=false
    LEGACY_AUTHORIZED=false
    CANONICAL_KEY_A_ASSEMBLY_AUTHORIZED=false
    MIGRATION_AUTHORIZED=false

    NEXT=OWNER_LAUNCH_FRESH_P4_HELDOUT_H01
