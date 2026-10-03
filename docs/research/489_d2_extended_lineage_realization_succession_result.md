# Research 489: D-2 extended lineage and realization-succession result

**Date:** 2026-10-03
**Status:** D2_LINEAGE_EXTENSION_PLAUSIBLE / D1 INTEGRATED MICRO-REPLAY NEXT
**Protocol:** Research 482
**Pre-score clarification:** Research 486
**Comparison freeze:** Research 488
**Frozen comparison commit:** bebe8db0607c09eb2521e3c27155f7802a942584
**Result artifact:** experiments/ao10_hybrid_d2_lineage_v01/result.json
**Result SHA-256:** 79ee18e844a7fc3c8ff1d0132c0a04af4ebcd1ecc030db11f84e4c43965eef35
**Scope:** Record the single frozen two-model D-2 comparison and reconcile lineage-extension mechanics for THIN_CENTRED_HYBRID_V02.
**Authority:** Development mechanism evidence only. No production selection, migration, Specification 028 replacement, dependent-DRP resumption, or hidden-R2 exposure.

## 1. Frozen result

Observed across fourteen frozen fixtures:

    semantic A -> key       14 / 14
    semantic B -> key       14 / 14
    semantic A <-> B        14 / 14
    semantic_all_match      true
    substantive conditions  pass

Therefore:

    D2_LINEAGE_EXTENSION_PLAUSIBLE

The semantic score removes only reason_codes under the prospectively frozen Research 486 clarification.

## 2. Independent-author result

Evaluator A was authored by ChatGPT.

Evaluator B was authored independently by Claude while blind to:

    evaluator_key.json
    evaluator_chatgpt_a.py
    evaluator-A output
    D-2 result/comparison.

The two independently authored evaluators agreed exactly on every material semantic field for all fourteen cases.

This is stronger independence than the earlier same-author C4-C8 mechanism probes.

## 3. Full-object diagnostic result

Full-object exact agreement including reason_codes was:

    Evaluator A -> key      14 / 14
    Evaluator B -> key       6 / 14
    Evaluator A <-> B        6 / 14

Every B mismatch was confined to reason_codes.

No material semantic field differed.

The eight diagnostic differences were exactly the under-specification class Claude identified before scoring:

    F02
        key: ATOMIC_PREDECESSOR_STAGGER
        B:   ATOMIC_PREDECESSOR_STAGGERED_BOUNDARY

    F04
        key: UNACCOUNTED_SOURCE_PORTION
        B:   SOURCE_PORTION_UNACCOUNTED

    F05
        key: SOURCE_PORTION_DOUBLE_MAPPED
        B:   SOURCE_PORTION_MAPPED_TWICE

    F07
        key: REINSTATE_REUSES_RETIRED_ID
        B:   REINSTATE_REUSES_RETIRED_IDENTITY

    F10
        key: CARRY_STALE_FACTS
        B:   CARRY_REJECTED + CARRY_SOURCE_FACTS_STALE

    F11
        key: CARRY_AUTHORITY_INVALID
        B:   CARRY_AUTHORITY_INVALID + CARRY_REJECTED

    F12
        key: no informational code
        B:   DEFERRAL_NOT_CARRIED

    F13
        key: no informational code
        B:   DEFERRAL_REBOUND

This validates the reason for Research 486 rather than weakening the semantic result.

The production design should eventually freeze a public diagnostic vocabulary if reason codes become interoperable machine contracts.

## 4. REPARTITION

F01 established mechanism plausibility for true crossing repartition:

    multiple predecessors
    -> multiple successors

with explicit semantic-portion mapping and synchronized effective boundaries for every atomic predecessor that contributes to multiple successors.

F02 rejected a single atomic predecessor whose mapped meaning would become effective at staggered successor boundaries.

F03 preserved a valid disjoint batched N:M transition in which independent predecessor identities move at different boundaries.

Therefore the amended rule is:

    per-target effective boundaries are valid only when they do not make one accepted atomic predecessor partly current and partly superseded.

## 5. Reinstatement

F06 supports:

    retired predecessor
    -> new accepted identity
    -> OPEN_RESET.

F07 rejects reuse of the retired identity.

Thus reinstatement preserves historical retirement and creates a new semantic identity rather than erasing lifecycle history.

## 6. Realization succession

F08 confirms the default:

    semantic successor
        -> OPEN_RESET.

F09 confirms that an explicit governed realization-carry mapping may export exact successor component facts for:

    CARRY_FACTS_FOR_REVALIDATION

without directly asserting successor satisfaction.

F10 and F11 show that stale realization facts or invalid carry authority reject carry, fall back to OPEN_RESET and require review while the semantic relation itself may remain valid.

Therefore semantic succession and realization succession remain distinct.

## 7. Deferral

F12 confirms:

    predecessor deferral
        does not automatically carry to semantic successor.

F13 confirms:

    exact successor deferral may be rebound only through explicit reacceptance.

## 8. Carry-forward

F14 confirms same-identity continuity under unchanged meaning:

    CARRY_FORWARD
        -> CONTINUITY

with compatible realization facts preserved for later J3 use.

Changed meaning remains outside carry-forward and requires semantic succession.

## 9. Candidate consequence

The V0.2 lineage section is now strengthened to development mechanism evidence for:

    1:1 REPLACE
    1:N SPLIT
    N:1 MERGE
    crossing N:M REPARTITION
    RETIRE
    REINSTATE
    same-identity CARRY_FORWARD
    explicit realization carry/reset
    deferral rebinding
    atomic effective-boundary currentness.

D-2 is therefore closed at development-mechanism level.

## 10. Remaining pre-owner-decision work

After D-3 and D-2:

    D3 = PASSED
    D2 = LINEAGE_EXTENSION_PLAUSIBLE
    D1 = REQUIRED

D-1 is the only remaining discriminator from Research 477 before the owner architecture decision.

D-1 must exercise the integrated V0.2 path on a real recent governing act with:

    source meaning + proposed J1 package;
    ordinary owner ACCEPT / AMEND / REJECT;
    standing/effect accounting;
    exact package/decision binding;
    natural-owner J2 declarations;
    shared-predicate/J3 derivation;
    generated orientation;
    one governed lineage transition;
    realization succession;
    independently authored evaluators from ChatGPT and Claude.

## 11. Current disposition

    D2=D2_LINEAGE_EXTENSION_PLAUSIBLE
    D3=D3_DEPENDENCY_PROOF_PASSES
    D1=REQUIRED

    THIN_CENTRED_HYBRID_V02=REMAINS_LEADING_CANDIDATE
    OWNER_ARCHITECTURE_DECISION_READY=false
    PRODUCTION_TARGET_SELECTED=false
    HIDDEN_R2_DETAILS=SEALED

    NEXT=FREEZE_D1_INTEGRATED_REAL_EVENT_MICROREPLAY_PROTOCOL
