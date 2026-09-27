# Research 373: Key Author A P4 H02 Attempt 001 Verifier-Scope HOLD and Fresh Replacement Release

**Date:** 2026-09-27
**Status:** H02 ATTEMPT 001 REJECTED / VERIFIER SESSION-SCOPE INCOMPATIBILITY IDENTIFIED / H02 REPREPARATION PASS / FRESH ATTEMPT 002 RELEASED
**Parent:** Research 372 / H02 attempt-001 bounded task-owner postflight
**Scope:** Reconcile the first H02 held-out grouping attempt, identify why the already-qualified P4 verifier cannot accept same-session continuation across event-local source boundaries, preserve the frozen attempt without semantic repair, and release a fresh H02 replacement under an execution pattern already permitted by the frozen P4 design.
**Authority:** H02 attempt-002 semantic execution only. H03-H11, runtime-verifier redesign, classification repair, LEGACY, canonical Key A assembly, commitment generation, Key Author B, scoring, production implementation, migration, oracle retirement and authority switching remain unauthorized.

## 1. H02 attempt 001 report

The accepted H01 held-out Claude Code session continued into H02, as permitted by Research 363.

The executor returned bounded PASS for:

    grouping batch
        H02

    attempt
        1

    session
        38294db9-d218-4797-86bc-0dc7e0b52e6a

    packet event
        EVP-1b53b3b00c6c

    unique semantic items
        216

    artifact frozen
        true

    next event exposed
        false

## 2. Independent bounded postflight

Independent task-owner postflight did not accept the executor self-report.

The following controls passed:

    progressPhaseOk
    p4Authorized
    interfaceVersionOk
    eventClosed
    acceptedPredecessorsOk
    targetNotAccepted
    projection provenance/schema/uniqueness/order/event scope
    projectionExactFrozenEligibility
    artifactSchemaOk
    pairShapeOk
    endpointEventScopeOk
    endpointEligibilityProjectionOk
    endpointDistinctOk
    lexicalOrderOk
    pairReasonsOk
    noDuplicatePairs
    joinSplitDisjoint
    pairSortOk
    localSettingsAbsent
    transcriptSessionOk
    transcriptModelOk
    transcriptPermissionOk
    noCompaction
    noForbiddenTool
    eligibilityProjectionRead
    errataReadBeforePrecedents
    artifactWrittenOnce
    precedentsAppendOnly
    errataAppendOnly

Two checks failed:

    catalogReadsBounded
        false

    noForbiddenSourceRead
        false

No hidden semantic details were exposed.

## 3. Verifier-scope diagnosis

The already-qualified p4-private-ops-v2 implementation was inspected as runtime evidence.

Its transcript verifier reads the complete Claude Code session transcript supplied by session ID.

For an event, it then evaluates every catalog read in that complete transcript against only the current event's permitted line range and treats every prior grouping-artifact access other than the current artifact as forbidden.

Therefore, when one held-out session is reused from accepted H01 into H02:

    H01 catalog reads
        are re-evaluated against H02 lines 155-2109

    H01 grouping-artifact activity
        is re-evaluated as a non-H02 grouping-artifact access

The two H02 failures are consequently induced by historical H01 activity that was itself authorized and already accepted.

The current verifier does not possess an event-local transcript boundary for a reused semantic session.

## 4. Interpretation

This is a verifier/session-scope incompatibility.

It is not evidence that H02 attempt 001 itself performed a semantically prohibited H02 source query.

However, the qualified acceptance gate is fail-closed. A frozen attempt that does not pass that gate cannot be accepted.

Disposition:

    H02 attempt 001
        PRIVATE / FROZEN / REJECTED / NONCANONICAL

    reason
        POSTFLIGHT_FAIL

No grouping artifact is repaired, filtered, rewritten or promoted.

## 5. Relationship to earlier D02 attempt 001

D02 attempt 001 also used a session that already contained accepted D01 activity and failed the same two published source-boundary checks.

Research 373 records that the same whole-session verifier property can account for that pattern.

The historical D02 disposition is not reopened:

    D02 attempt 001
        remains rejected / noncanonical

    D02 attempt 003
        remains the accepted development result

No accepted artifact or key state is changed retrospectively.

## 6. Selected bounded recovery

The frozen P4 design already permits a fresh replacement session at an accepted-event boundary.

Therefore no semantic P4 amendment is required.

The task owner rejected H02 attempt 001 and reran bounded H02 preparation.

Preparation returned:

    PASS

    projectionExactFrozenEligibility
        true

No hidden semantic detail was exposed.

H02 attempt 002 is released to a fresh standalone held-out Claude Code session.

## 7. Remaining held-out session policy

To avoid repeating the known whole-session verifier incompatibility during the active key-author program:

    H02-H11
        use fresh per-event Claude Code sessions

unless the bounded verifier is separately requalified before a later clean event boundary.

This is a stricter operational isolation choice already permitted by Research 363. It does not alter grouping semantics, event ordering, eligibility truth, held-out blindness, pair truth rules, or task-owner gates.

The broader verifier architecture may be reconsidered later. Mid-key runtime redesign is not required to continue safely.

## 8. Current boundary

    P4_AUTHORIZED=true
    P4_ELIGIBILITY_INTERFACE=V0.1_FROZEN

    H01_ATTEMPT_002=ACCEPTED

    H02_ATTEMPT_001=HOLD_REJECTED_POSTFLIGHT_FAIL
    H02_VERIFIER_SESSION_SCOPE_INCOMPATIBILITY=IDENTIFIED
    H02_REPREPARATION=PASS
    H02_ATTEMPT_002=RELEASED_FRESH_SESSION

    REMAINING_HELDOUT_SESSION_POLICY=FRESH_PER_EVENT_UNLESS_VERIFIER_REQUALIFIED

    H03_H11_RELEASED=false

    CLASSIFICATION_REPAIR_AUTHORIZED=false
    LEGACY_AUTHORIZED=false
    CANONICAL_KEY_A_ASSEMBLY_AUTHORIZED=false
    MIGRATION_AUTHORIZED=false

    NEXT=OWNER_LAUNCH_FRESH_P4_HELDOUT_H02_ATTEMPT002
