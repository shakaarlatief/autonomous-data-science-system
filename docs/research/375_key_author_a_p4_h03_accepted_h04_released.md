# Research 375: Key Author A P4 H03 Accepted and H04 Released

**Date:** 2026-09-27
**Status:** H03 ATTEMPT 001 ACCEPTED / H04 PREPARATION PASS / H04 SEMANTIC EXECUTION RELEASED
**Parent:** Research 374 / fresh H03 execution
**Scope:** Preserve successful H03 execution and acceptance, H04 preparation, and fresh-session H04 release under the verifier-compatible per-event held-out session policy.
**Authority:** H04 attempt-001 semantic execution only. H05-H11, runtime-verifier redesign, classification repair, LEGACY, canonical Key A assembly, commitment generation, Key Author B, scoring, production implementation, migration, oracle retirement and authority switching remain unauthorized.

## 1. H03 execution

H03 attempt 001 executed in a fresh standalone held-out Claude Code session:

    session
        717cbd8a-f992-426c-bb04-a8b95228f850

    packet event
        EVP-819a9953b12b

    unique semantic items
        371

The executor returned bounded PASS and froze the H03 artifact.

## 2. Independent bounded postflight

Independent task-owner postflight returned:

    overallPostflight
        PASS

Every published check passed, including progress and authorization, accepted predecessors and target state, exact frozen eligibility, artifact and pair mechanics, transcript identity, source and tool boundaries, write-once behavior, and append-only shared state.

No hidden semantic detail was exposed.

The task owner then accepted H03 attempt 001 through the qualified bounded private-operation capability.

Disposition:

    H03 attempt 001
        ACCEPTED

## 3. H04 preparation

The bounded private-operation capability prepared:

    batch
        H04

    packet event
        EVP-d8bfe7b48f85

    unique semantic items
        65

    catalog range
        birth_heldout.json lines 5465-6060 inclusive

Preparation returned:

    preparation
        PASS

    projectionExactFrozenEligibility
        true

    hiddenSemanticDetailsExposed
        false

## 4. H04 semantic release

H04 is released only to a fresh standalone held-out Claude Code session.

The temporary verifier-compatible policy remains one fresh semantic session per held-out event unless the bounded verifier is separately requalified at a clean event boundary.

H05-H11 remain task-owner gated.

## 5. Current boundary

    P4_AUTHORIZED=true
    P4_ELIGIBILITY_INTERFACE=V0.1_FROZEN

    H01_ATTEMPT_002=ACCEPTED
    H02_ATTEMPT_002=ACCEPTED
    H03_ATTEMPT_001=ACCEPTED

    H04_PROJECTION_PREPARATION=PASS
    H04_SEMANTIC_EXECUTION=RELEASED_FRESH_SESSION

    REMAINING_HELDOUT_SESSION_POLICY=FRESH_PER_EVENT_UNLESS_VERIFIER_REQUALIFIED

    H05_H11_RELEASED=false

    CLASSIFICATION_REPAIR_AUTHORIZED=false
    LEGACY_AUTHORIZED=false
    CANONICAL_KEY_A_ASSEMBLY_AUTHORIZED=false
    MIGRATION_AUTHORIZED=false

    NEXT=OWNER_LAUNCH_FRESH_P4_HELDOUT_H04_ATTEMPT001
