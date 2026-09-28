# Research 380: Key Author A P4 H08 Accepted and H09 Released

**Date:** 2026-09-28
**Status:** H08 ATTEMPT 001 ACCEPTED / H09 PREPARATION PASS / H09 SEMANTIC EXECUTION RELEASED
**Parent:** Research 379 / fresh H08 execution
**Scope:** Preserve successful H08 execution and acceptance, H09 preparation, and fresh-session H09 release under the verifier-compatible per-event held-out session policy.
**Authority:** H09 attempt-001 semantic execution only. H10-H11, runtime-verifier redesign, classification repair, LEGACY, canonical Key A assembly, commitment generation, Key Author B, scoring, production implementation, migration, oracle retirement and authority switching remain unauthorized.

## 1. H08 execution

H08 attempt 001 executed in a fresh standalone held-out Claude Code session:

    session
        92630696-6316-4a83-a779-bbc3689a6fa8

    packet event
        EVP-3ad3b2e576e0

    unique semantic items
        124

The executor returned bounded PASS and froze the H08 artifact.

## 2. Independent bounded postflight

Independent task-owner postflight returned:

    overallPostflight
        PASS

Every published check passed, including progress and authorization, accepted predecessors and target state, exact frozen eligibility, artifact and pair mechanics, transcript identity, source and tool boundaries, write-once behavior, and append-only shared state.

No hidden semantic detail was exposed.

The task owner then accepted H08 attempt 001 through the qualified bounded private-operation capability.

Disposition:

    H08 attempt 001
        ACCEPTED

## 3. H09 preparation

The bounded private-operation capability prepared:

    batch
        H09

    packet event
        EVP-ffd3c3f9f874

    unique semantic items
        436

    catalog range
        birth_heldout.json lines 10020-13959 inclusive

Preparation returned:

    preparation
        PASS

    projectionExactFrozenEligibility
        true

    hiddenSemanticDetailsExposed
        false

## 4. H09 semantic release

H09 is released only to a fresh standalone held-out Claude Code session.

The temporary verifier-compatible policy remains one fresh semantic session per held-out event unless the bounded verifier is separately requalified at a clean event boundary.

H10-H11 remain task-owner gated.

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

    H09_PROJECTION_PREPARATION=PASS
    H09_SEMANTIC_EXECUTION=RELEASED_FRESH_SESSION

    REMAINING_HELDOUT_SESSION_POLICY=FRESH_PER_EVENT_UNLESS_VERIFIER_REQUALIFIED

    H10_H11_RELEASED=false

    CLASSIFICATION_REPAIR_AUTHORIZED=false
    LEGACY_AUTHORIZED=false
    CANONICAL_KEY_A_ASSEMBLY_AUTHORIZED=false
    MIGRATION_AUTHORIZED=false

    NEXT=OWNER_LAUNCH_FRESH_P4_HELDOUT_H09_ATTEMPT001
