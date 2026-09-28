# Research 381: Key Author A P4 H09 Accepted and H10 Released

**Date:** 2026-09-28
**Status:** H09 ATTEMPT 001 ACCEPTED / H10 PREPARATION PASS / H10 SEMANTIC EXECUTION RELEASED
**Parent:** Research 380 / fresh H09 execution
**Scope:** Preserve successful H09 execution and acceptance, H10 preparation, and fresh-session H10 release under the verifier-compatible per-event held-out session policy.
**Authority:** H10 attempt-001 semantic execution only. H11, runtime-verifier redesign, classification repair, LEGACY, canonical Key A assembly, commitment generation, Key Author B, scoring, production implementation, migration, oracle retirement and authority switching remain unauthorized.

## 1. H09 execution

H09 attempt 001 executed in a fresh standalone held-out Claude Code session:

    session
        18bdf4fe-07e5-47e2-bfd5-d46336f979b7

    packet event
        EVP-ffd3c3f9f874

    unique semantic items
        436

The executor returned bounded PASS and froze the H09 artifact.

## 2. Independent bounded postflight

Independent task-owner postflight returned:

    overallPostflight
        PASS

Every published check passed, including progress and authorization, accepted predecessors and target state, exact frozen eligibility, artifact and pair mechanics, transcript identity, source and tool boundaries, write-once behavior, and append-only shared state.

No hidden semantic detail was exposed.

The task owner then accepted H09 attempt 001 through the qualified bounded private-operation capability.

Disposition:

    H09 attempt 001
        ACCEPTED

## 3. H10 preparation

The bounded private-operation capability prepared:

    batch
        H10

    packet event
        EVP-e9498b2ad950

    unique semantic items
        20

    catalog range
        birth_heldout.json lines 13960-14150 inclusive

Preparation returned:

    preparation
        PASS

    projectionExactFrozenEligibility
        true

    hiddenSemanticDetailsExposed
        false

## 4. H10 semantic release

H10 is released only to a fresh standalone held-out Claude Code session.

The temporary verifier-compatible policy remains one fresh semantic session per held-out event unless the bounded verifier is separately requalified at a clean event boundary.

H11 remains task-owner gated.

## 5. Current boundary

    P4_AUTHORIZED=true
    P4_ELIGIBILITY_INTERFACE=V0.1_FROZEN

    H01_ATTEMPT_002=ACCEPTED
    H02_ATTEMPT_002=ACCEPTED
    H03_ATTEMPT_001=ACCEPTED
    H04_ATTEMPT_001=ACCEPTED
    H05_ATTEMPT_001=ACCEPTED
    H06_ATTEMPT_001=ACCEPTED
    H07_ATTEMPT_001=ACCEPTED
    H08_ATTEMPT_001=ACCEPTED
    H09_ATTEMPT_001=ACCEPTED

    H10_PROJECTION_PREPARATION=PASS
    H10_SEMANTIC_EXECUTION=RELEASED_FRESH_SESSION

    REMAINING_HELDOUT_SESSION_POLICY=FRESH_PER_EVENT_UNLESS_VERIFIER_REQUALIFIED

    H11_RELEASED=false

    CLASSIFICATION_REPAIR_AUTHORIZED=false
    LEGACY_AUTHORIZED=false
    CANONICAL_KEY_A_ASSEMBLY_AUTHORIZED=false
    MIGRATION_AUTHORIZED=false

    NEXT=OWNER_LAUNCH_FRESH_P4_HELDOUT_H10_ATTEMPT001
