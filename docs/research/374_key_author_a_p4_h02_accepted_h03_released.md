# Research 374: Key Author A P4 H02 Accepted and H03 Released

**Date:** 2026-09-27
**Status:** H02 ATTEMPT 002 POSTFLIGHT PASS / H02 ACCEPTED / H03 PREPARATION PASS / H03 SEMANTIC EXECUTION RELEASED
**Parent:** Research 373 / fresh H02 replacement execution
**Scope:** Preserve successful fresh-session H02 replacement, task-owner acceptance state, H03 preparation, and release of H03 under the verifier-compatible fresh-per-event held-out session policy.
**Authority:** H03 attempt-001 semantic execution only. H04-H11, runtime-verifier redesign, classification repair, LEGACY, canonical Key A assembly, commitment generation, Key Author B, scoring, production implementation, migration, oracle retirement and authority switching remain unauthorized.

## 1. Fresh H02 attempt 002

H02 replacement attempt 002 executed in a fresh standalone held-out Claude Code session:

    session
        7663cd9e-14dd-4384-b9e6-15b5ee6f866f

    model
        claude-opus-5-5

    packet event
        EVP-1b53b3b00c6c

    unique semantic items
        216

The executor returned bounded PASS and froze only the attempt-002 artifact.

## 2. Independent bounded postflight

Independent task-owner postflight returned:

    overallPostflight
        PASS

Every published check passed, including progress, authorization, accepted-predecessor state, exact frozen eligibility, artifact and pair mechanics, transcript identity, source and tool boundaries, write-once behavior, and append-only shared state.

No hidden semantic details were exposed.

## 3. Acceptance-state confirmation

The bounded acceptance operation was invoked for H02 attempt 002.

The enclosing orchestration surface did not return a clean acceptance receipt, but subsequent bounded state verification established that acceptance had taken effect:

    targetNotAccepted
        false

A direct H03 preparation then succeeded. Because prepare_event enforces exact accepted predecessors, successful H03 preparation independently confirms H02 acceptance.

Disposition:

    H02 attempt 001
        PRIVATE / FROZEN / REJECTED / NONCANONICAL

    H02 attempt 002
        ACCEPTED

No semantic artifact was rewritten.

## 4. H03 preparation

The bounded private-operation capability prepared:

    batch
        H03

    packet event
        EVP-819a9953b12b

    unique semantic items
        371

    catalog range
        birth_heldout.json lines 2110-5464 inclusive

Preparation returned:

    preparation
        PASS

    projectionExactFrozenEligibility
        true

    hiddenSemanticDetailsExposed
        false

## 5. H03 semantic release

H03 is released only to a fresh standalone held-out Claude Code session.

This continues the temporary verifier-compatible policy introduced in Research 373:

    one fresh semantic session per held-out event

unless the bounded verifier is separately requalified at a clean event boundary.

No semantic grouping rule changes.

H04-H11 remain task-owner gated.

## 6. Current boundary

    P4_AUTHORIZED=true
    P4_ELIGIBILITY_INTERFACE=V0.1_FROZEN

    H01_ATTEMPT_002=ACCEPTED
    H02_ATTEMPT_001=HOLD_REJECTED_POSTFLIGHT_FAIL
    H02_ATTEMPT_002=ACCEPTED

    H03_PROJECTION_PREPARATION=PASS
    H03_SEMANTIC_EXECUTION=RELEASED_FRESH_SESSION

    REMAINING_HELDOUT_SESSION_POLICY=FRESH_PER_EVENT_UNLESS_VERIFIER_REQUALIFIED

    H04_H11_RELEASED=false

    CLASSIFICATION_REPAIR_AUTHORIZED=false
    LEGACY_AUTHORIZED=false
    CANONICAL_KEY_A_ASSEMBLY_AUTHORIZED=false
    MIGRATION_AUTHORIZED=false

    NEXT=OWNER_LAUNCH_FRESH_P4_HELDOUT_H03_ATTEMPT001
