# Research 372: Key Author A P4 H01 Accepted and H02 Released

**Date:** 2026-09-27
**Status:** H01 ATTEMPT 001 REJECTED / ATTEMPT 002 ACCEPTED / H02 PREPARATION PASS / H02 SEMANTIC EXECUTION RELEASED
**Parent:** Research 371 / bounded H01 task-owner postflight and exact progress-state reconciliation
**Scope:** Preserve the H01 held-out grouping attempt sequence, reconcile the exact attempt-aware postflight phase expected by the already-qualified bounded P4 runtime, accept H01 only after a complete PASS, prepare H02, and release H02 to the accepted held-out grouping session.
**Authority:** H01 acceptance and H02 semantic execution only. H03-H11, classification repair, LEGACY, canonical Key A assembly, commitment generation, Key Author B, scoring, production implementation, migration, oracle retirement and authority switching remain unauthorized.

## 1. H01 attempt 001

The mandatory fresh held-out grouping session returned a bounded PASS report for H01 attempt 001.

Independent task-owner postflight did not accept the self-report.

Exactly one bounded check failed:

    progressPhaseOk
        false

Every other published check passed, including:

    P4 authorization
    interface version
    event closure
    accepted predecessors
    target not already accepted
    projection provenance/schema/uniqueness/order/event scope
    exact projection equality to frozen same-key eligibility truth
    artifact schema and pair shape
    endpoint event scope and eligibility membership
    endpoint distinctness and lexical order
    pair reasons
    duplicate absence
    join/split disjointness
    deterministic pair ordering
    local settings
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

Disposition:

    H01 attempt 001
        PRIVATE / FROZEN / REJECTED / NONCANONICAL

    reason
        POSTFLIGHT_FAIL

The bounded capability re-prepared H01 and again verified the frozen eligibility projection exactly.

## 2. H01 attempt 002 initial postflight

A fresh replacement held-out session executed H01 attempt 002.

Its grouping artifact and all semantic/source/tool controls passed the bounded gate.

The initial postflight again had exactly one failing check:

    progressPhaseOk
        false

No semantic, artifact, eligibility, transcript, source-boundary, tool-boundary, write-once or append-only defect was present.

Attempt 002 was therefore not rejected immediately while the exact mechanical phase expectation was resolved.

## 3. Exact qualified runtime expectation

The already-qualified p4-private-ops-v2 implementation was inspected as runtime evidence.

Its frozen postflight contract requires the attempt-aware completion phase:

    P4_BIRTH_GROUPING_<EVENT>_ATTEMPT_<NNN>_COMPLETE_AWAITING_REVIEW

For H01 attempt 002 the exact value is:

    P4_BIRTH_GROUPING_H01_ATTEMPT_002_COMPLETE_AWAITING_REVIEW

The older public P4 design wording used a non-attempt-qualified completion label. The observed failure was therefore an operational state-label mismatch, not a semantic grouping failure.

No P4 semantic rule was changed.

## 4. Non-semantic progress correction

The same H01 attempt-002 session performed one bounded progress-only correction.

The returned correction receipt states:

    PROGRESS_CORRECTION
        PASS

    current phase
        P4_BIRTH_GROUPING_H01_ATTEMPT_002_COMPLETE_AWAITING_REVIEW

    grouping artifact modified
        false

    semantic source read
        false

    next event exposed
        false

No grouping artifact, eligibility projection, classification artifact, PRECEDENTS, ERRATA or semantic source was changed or reopened.

## 5. H01 attempt 002 acceptance

Independent bounded postflight was rerun after the progress-only correction.

Result:

    overallPostflight
        PASS

Every published check passed.

The bounded acceptance operation reran the complete postflight and accepted H01 attempt 002.

Result:

    H01 attempt 002
        ACCEPTED

Only attempt 002 is accepted for downstream Key A construction.

## 6. H02 preparation

The bounded private-operation capability prepared:

    batch
        H02

    packet event
        EVP-1b53b3b00c6c

    unique semantic items
        216

    catalog range
        birth_heldout.json lines 155-2109 inclusive

Preparation returned:

    preparation
        PASS

    projectionExactFrozenEligibility
        true

    hiddenSemanticDetailsExposed
        false

No eligible IDs/counts, pair identities/counts/reasons, classifications, attention mappings or private digests were exposed.

## 7. H02 semantic release

H02 is released to the accepted held-out grouping session.

The frozen P4 design permits H01-H11 to continue in the same held-out session after each accepted event. A fresh replacement session remains permitted or required only at a clean accepted-event boundary when operationally necessary.

H02 must preserve:

    eligibility projection V0.1
    classification immutability
    event-local grouping only
    pairwise individual review
    MUST_JOIN all-four-condition rule
    MUST_SPLIT independent-boundary rule
    UNCONSTRAINED by absence
    no padding
    bounded H02 source only
    no prior frozen grouping-artifact reads
    no classification/attention reads
    no shell/web/MCP/IDE/Agent semantic worker
    exact attempt-aware completion phase required by the qualified runtime

No H03 or later source may be exposed before H02 freezes and passes task-owner review.

## 8. Current boundary

    P4_AUTHORIZED=true
    P4_ELIGIBILITY_INTERFACE=V0.1_FROZEN

    P4_DEVELOPMENT_GROUPING=COMPLETE

    H01_ATTEMPT_001=HOLD_REJECTED_POSTFLIGHT_FAIL
    H01_ATTEMPT_002=ACCEPTED

    H02_PROJECTION_PREPARATION=PASS
    H02_SEMANTIC_EXECUTION=RELEASED

    H03_H11_RELEASED=false

    CLASSIFICATION_REPAIR_AUTHORIZED=false
    LEGACY_AUTHORIZED=false
    CANONICAL_KEY_A_ASSEMBLY_AUTHORIZED=false
    MIGRATION_AUTHORIZED=false

    NEXT=OWNER_CONTINUE_P4_HELDOUT_H02
