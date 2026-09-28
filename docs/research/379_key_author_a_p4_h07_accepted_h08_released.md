# Research 379: Key Author A P4 H07 Accepted and H08 Released

**Date:** 2026-09-28
**Status:** H07 ATTEMPT 001 ACCEPTED / H08 PREPARATION PASS / H08 SEMANTIC EXECUTION RELEASED
**Parent:** Research 378 / fresh H07 execution
**Scope:** Preserve successful H07 execution and acceptance, H08 preparation, and fresh-session H08 release under the verifier-compatible per-event held-out session policy.
**Authority:** H08 attempt-001 semantic execution only. H09-H11, runtime-verifier redesign, classification repair, LEGACY, canonical Key A assembly, commitment generation, Key Author B, scoring, production implementation, migration, oracle retirement and authority switching remain unauthorized.

## 1. H07 execution

H07 attempt 001 executed in a fresh standalone held-out Claude Code session:

    session
        3f1af83a-7233-4bfd-87f9-3a8148f2b84f

    packet event
        EVP-838a4c21407b

    unique semantic items
        124

The executor returned bounded PASS and froze the H07 artifact.

## 2. Independent bounded postflight

Independent task-owner postflight returned:

    overallPostflight
        PASS

Every published check passed, including progress and authorization, accepted predecessors and target state, exact frozen eligibility, artifact and pair mechanics, transcript identity, source and tool boundaries, write-once behavior, and append-only shared state.

No hidden semantic detail was exposed.

The task owner then accepted H07 attempt 001 through the qualified bounded private-operation capability.

Disposition:

    H07 attempt 001
        ACCEPTED

## 3. H08 preparation

The bounded private-operation capability prepared:

    batch
        H08

    packet event
        EVP-3ad3b2e576e0

    unique semantic items
        124

    catalog range
        birth_heldout.json lines 8893-10019 inclusive

Preparation returned:

    preparation
        PASS

    projectionExactFrozenEligibility
        true

    hiddenSemanticDetailsExposed
        false

## 4. H08 semantic release

H08 is released only to a fresh standalone held-out Claude Code session.

The temporary verifier-compatible policy remains one fresh semantic session per held-out event unless the bounded verifier is separately requalified at a clean event boundary.

H09-H11 remain task-owner gated.

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

    H08_PROJECTION_PREPARATION=PASS
    H08_SEMANTIC_EXECUTION=RELEASED_FRESH_SESSION

    REMAINING_HELDOUT_SESSION_POLICY=FRESH_PER_EVENT_UNLESS_VERIFIER_REQUALIFIED

    H09_H11_RELEASED=false

    CLASSIFICATION_REPAIR_AUTHORIZED=false
    LEGACY_AUTHORIZED=false
    CANONICAL_KEY_A_ASSEMBLY_AUTHORIZED=false
    MIGRATION_AUTHORIZED=false

    NEXT=OWNER_LAUNCH_FRESH_P4_HELDOUT_H08_ATTEMPT001
