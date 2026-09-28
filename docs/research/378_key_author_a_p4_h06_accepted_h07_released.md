# Research 378: Key Author A P4 H06 Accepted and H07 Released

**Date:** 2026-09-28
**Status:** H06 ATTEMPT 001 ACCEPTED / H07 PREPARATION PASS / H07 SEMANTIC EXECUTION RELEASED
**Parent:** Research 377 / fresh H06 execution
**Scope:** Preserve successful H06 execution and acceptance, H07 preparation, and fresh-session H07 release under the verifier-compatible per-event held-out session policy.
**Authority:** H07 attempt-001 semantic execution only. H08-H11, runtime-verifier redesign, classification repair, LEGACY, canonical Key A assembly, commitment generation, Key Author B, scoring, production implementation, migration, oracle retirement and authority switching remain unauthorized.

## 1. H06 execution

H06 attempt 001 executed in a fresh standalone held-out Claude Code session:

    session
        738b37a3-1527-41bd-8244-38d12b58255c

    packet event
        EVP-dca0fcb4fb4d

    unique semantic items
        124

The executor returned bounded PASS and froze the H06 artifact.

## 2. Independent bounded postflight

Independent task-owner postflight returned:

    overallPostflight
        PASS

Every published check passed, including progress and authorization, accepted predecessors and target state, exact frozen eligibility, artifact and pair mechanics, transcript identity, source and tool boundaries, write-once behavior, and append-only shared state.

No hidden semantic detail was exposed.

The task owner then accepted H06 attempt 001 through the qualified bounded private-operation capability.

Disposition:

    H06 attempt 001
        ACCEPTED

## 3. H07 preparation

The bounded private-operation capability prepared:

    batch
        H07

    packet event
        EVP-838a4c21407b

    unique semantic items
        124

    catalog range
        birth_heldout.json lines 7766-8892 inclusive

Preparation returned:

    preparation
        PASS

    projectionExactFrozenEligibility
        true

    hiddenSemanticDetailsExposed
        false

## 4. H07 semantic release

H07 is released only to a fresh standalone held-out Claude Code session.

The temporary verifier-compatible policy remains one fresh semantic session per held-out event unless the bounded verifier is separately requalified at a clean event boundary.

H08-H11 remain task-owner gated.

## 5. Current boundary

    P4_AUTHORIZED=true
    P4_ELIGIBILITY_INTERFACE=V0.1_FROZEN

    H01_ATTEMPT_002=ACCEPTED
    H02_ATTEMPT_002=ACCEPTED
    H03_ATTEMPT_001=ACCEPTED
    H04_ATTEMPT_001=ACCEPTED
    H05_ATTEMPT_001=ACCEPTED
    H06_ATTEMPT_001=ACCEPTED

    H07_PROJECTION_PREPARATION=PASS
    H07_SEMANTIC_EXECUTION=RELEASED_FRESH_SESSION

    REMAINING_HELDOUT_SESSION_POLICY=FRESH_PER_EVENT_UNLESS_VERIFIER_REQUALIFIED

    H08_H11_RELEASED=false

    CLASSIFICATION_REPAIR_AUTHORIZED=false
    LEGACY_AUTHORIZED=false
    CANONICAL_KEY_A_ASSEMBLY_AUTHORIZED=false
    MIGRATION_AUTHORIZED=false

    NEXT=OWNER_LAUNCH_FRESH_P4_HELDOUT_H07_ATTEMPT001
