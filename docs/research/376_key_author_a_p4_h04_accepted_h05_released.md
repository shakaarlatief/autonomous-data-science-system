# Research 376: Key Author A P4 H04 Accepted and H05 Released

**Date:** 2026-09-27
**Status:** H04 ATTEMPT 001 ACCEPTED / H05 PREPARATION PASS / H05 SEMANTIC EXECUTION RELEASED
**Parent:** Research 375 / fresh H04 execution
**Scope:** Preserve successful H04 execution and acceptance, H05 preparation, and fresh-session H05 release under the verifier-compatible per-event held-out session policy.
**Authority:** H05 attempt-001 semantic execution only. H06-H11, runtime-verifier redesign, classification repair, LEGACY, canonical Key A assembly, commitment generation, Key Author B, scoring, production implementation, migration, oracle retirement and authority switching remain unauthorized.

## 1. H04 execution

H04 attempt 001 executed in a fresh standalone held-out Claude Code session:

    session
        d3586e39-d4db-478c-8e33-0adef84e6af3

    packet event
        EVP-d8bfe7b48f85

    unique semantic items
        65

The executor returned bounded PASS and froze the H04 artifact.

## 2. Independent bounded postflight

Independent task-owner postflight returned:

    overallPostflight
        PASS

Every published check passed, including progress and authorization, accepted predecessors and target state, exact frozen eligibility, artifact and pair mechanics, transcript identity, source and tool boundaries, write-once behavior, and append-only shared state.

No hidden semantic detail was exposed.

The task owner then accepted H04 attempt 001 through the qualified bounded private-operation capability.

Disposition:

    H04 attempt 001
        ACCEPTED

## 3. H05 preparation

The bounded private-operation capability prepared:

    batch
        H05

    packet event
        EVP-ba08dc62e616

    unique semantic items
        63

    catalog range
        birth_heldout.json lines 6061-6638 inclusive

Preparation returned:

    preparation
        PASS

    projectionExactFrozenEligibility
        true

    hiddenSemanticDetailsExposed
        false

## 4. H05 semantic release

H05 is released only to a fresh standalone held-out Claude Code session.

The temporary verifier-compatible policy remains one fresh semantic session per held-out event unless the bounded verifier is separately requalified at a clean event boundary.

H06-H11 remain task-owner gated.

## 5. Current boundary

    P4_AUTHORIZED=true
    P4_ELIGIBILITY_INTERFACE=V0.1_FROZEN

    H01_ATTEMPT_002=ACCEPTED
    H02_ATTEMPT_002=ACCEPTED
    H03_ATTEMPT_001=ACCEPTED
    H04_ATTEMPT_001=ACCEPTED

    H05_PROJECTION_PREPARATION=PASS
    H05_SEMANTIC_EXECUTION=RELEASED_FRESH_SESSION

    REMAINING_HELDOUT_SESSION_POLICY=FRESH_PER_EVENT_UNLESS_VERIFIER_REQUALIFIED

    H06_H11_RELEASED=false

    CLASSIFICATION_REPAIR_AUTHORIZED=false
    LEGACY_AUTHORIZED=false
    CANONICAL_KEY_A_ASSEMBLY_AUTHORIZED=false
    MIGRATION_AUTHORIZED=false

    NEXT=OWNER_LAUNCH_FRESH_P4_HELDOUT_H05_ATTEMPT001
