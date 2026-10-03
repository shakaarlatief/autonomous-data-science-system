# Research 482: D-2 extended lineage and realization-succession protocol

**Date:** 2026-10-03
**Status:** PROTOCOL + FIXTURES FROZEN / CHATGPT EVALUATOR A NEXT
**Parent:** Research 477-478
**Fixed evidence base:** b3f29505ea5e0c59c68b4b1f2115634898c48f07
**Probe ID:** HYBRID_D2_LINEAGE_EXTENSION_V01
**Scope:** Prospectively freeze the exact lineage-extension semantics, blinded fixtures and output contract for crossing repartition, effective boundaries, reinstatement and realization succession before either independent model evaluator is executed.
**Authority:** Development mechanism protocol only. No production selection, migration, Specification 028 replacement, dependent-DRP resumption, or hidden-R2 exposure.

## 1. Question

D-2 asks:

> Can THIN_CENTRED_HYBRID_V02 represent true crossing semantic repartition, staged effective boundaries, reinstatement and realization carry/reset deterministically without prose adjudication or silently carrying obsolete realization state?

## 2. Independence design

Two evaluator paths are required:

    Evaluator A
        authored by ChatGPT after this protocol/fixture freeze.

    Evaluator B
        authored independently by Claude from only the reviewer-facing protocol, fixture inputs and output schema.

Before committing Evaluator B, Claude must not inspect:

    evaluator_key.json
    evaluator_chatgpt_a.py
    any ChatGPT D-2 result/output
    any future D-2 comparison result.

Claude's permitted repository write surface remains collaboration messages only. Therefore Claude will place the complete source of Evaluator B in Message 018. ChatGPT may later materialize that source verbatim for execution, preserving Claude authorship.

## 3. Semantic units

A lineage transition is evaluated over accepted effect identities.

For REPARTITION fixtures, each predecessor declares an accepted semantic-portion inventory.

A semantic portion is not an implementation component.

It is a bounded accepted mapping unit used only to state which part of predecessor meaning becomes which successor meaning.

Every source portion in the transition scope must be exactly one of:

    mapped once to a successor target portion
    explicitly retired
    explicitly unaffected.

No source portion may silently disappear or be mapped twice.

Every declared successor target portion must be supplied by at least one mapping row.

## 4. Relation forms under D-2

D-2 exercises:

    CARRY_FORWARD
    REPLACE
    REPARTITION
    REINSTATE.

SPLIT / MERGE remain covered by C7 and are not re-probed separately here.

### REPARTITION

REPARTITION permits:

    N predecessors -> M successors

with:

    N >= 2
    M >= 2

and an explicit mapping matrix.

True crossing repartition is supported when at least one predecessor contributes to more than one successor and at least one successor receives meaning from more than one predecessor.

### REINSTATE

REINSTATE:

    starts from a RETIRED predecessor;
    creates a new accepted effect identity;
    does not erase retirement history;
    does not reuse the retired identity.

## 5. Atomic predecessor and effective-boundary rule

An accepted effect identity is atomic for lifecycle currentness.

Therefore a single predecessor may not be partly superseded at one time and partly superseded at another unless those parts were already separate accepted effect identities.

Operational rule:

    for each predecessor,
    collect the effective boundaries of every successor to which any of its mapped source portions contribute.

    if that predecessor contributes to more than one successor,
    all those successor boundaries must be equal.

This permits:

    true crossing repartition at one synchronized boundary;

    a batched disjoint N:M relation whose independent predecessors move to independent successors at different boundaries.

It rejects:

    one atomic predecessor split across staggered successor boundaries.

This prospectively narrows the broad V0.2 phrase "per-target effective boundaries" into a rule compatible with atomic accepted-effect identity.

## 6. Current-effect resolution

At an evaluation boundary:

    a successor is current when its effective boundary <= evaluation boundary.

For each predecessor:

    if all mapped/retired portions have taken effect and no unaffected portion remains,
        predecessor is no longer current;

    otherwise,
        predecessor remains current.

Because the atomic-boundary rule forbids staggered partial supersession of one predecessor, this does not produce a partly-current predecessor.

REINSTATE predecessor remains historical/retired; the new identity becomes current when effective.

CARRY_FORWARD keeps the same accepted effect identity current.

## 7. Realization-succession rule

Semantic lineage runs before J3.

D-2 does not directly declare a successor SATISFIED.

Instead it emits initialization facts for later J3 re-derivation.

Initialization modes:

    CONTINUITY
        CARRY_FORWARD only; same semantic identity.

    OPEN_RESET
        default for REPLACE / REPARTITION / REINSTATE.

    CARRY_FACTS_FOR_REVALIDATION
        only when an explicit governed realization-carry mapping is valid.

For semantic succession, no prior realization fact carries automatically.

## 8. Governed realization carry

A carry mapping is valid only when all are true:

    carry_present
    carry_authority_valid
    carry_effective_boundary_valid
    source_realization_facts_current
    source_realization_facts_fresh
    every carried predecessor component is mapped to an exact successor required component
    no carried source component maps twice
    every requested successor carried component exists
    if successor qualification is required:
        qualification_rechecked = true.

A valid carry exports only the mapped component facts to J3.

It does not itself set SATISFIED.

If a carry mapping is present but invalid:

    semantic relation may remain valid;
    carry is rejected;
    successor initialization falls back to OPEN_RESET;
    review_required = true.

## 9. CARRY_FORWARD realization

CARRY_FORWARD preserves the same identity and may preserve compatible realization facts only when:

    semantic_digest_unchanged = true
    carrier/revision validity = true
    source realization facts remain current/fresh.

Changed semantic digest invalidates CARRY_FORWARD as a lineage relation.

## 10. Deferral succession

A predecessor deferral does not automatically carry across:

    REPLACE
    REPARTITION
    REINSTATE.

For a semantic successor:

    deferral_rebound = true

only when the governing transition explicitly reaccepts the deferral for that exact successor and effective boundary.

CARRY_FORWARD may preserve the same deferral when its exact authority/scope remains valid because semantic identity is unchanged.

## 11. Frozen fixture package

The reviewer-facing package contains fourteen fixtures:

    F01 valid true crossing REPARTITION at synchronized boundary
    F02 crossing REPARTITION with staggered target boundaries -> invalid
    F03 disjoint batched REPARTITION with independent target boundaries -> valid
    F04 source portion omitted without retirement/unaffected -> invalid
    F05 source portion mapped twice -> invalid
    F06 valid REINSTATE creates new identity and OPEN_RESET
    F07 REINSTATE reuses retired identity -> invalid
    F08 REPLACE with no carry -> OPEN_RESET
    F09 REPLACE with valid governed realization carry -> CARRY_FACTS_FOR_REVALIDATION
    F10 stale carry facts -> relation valid, carry rejected, review required
    F11 invalid carry authority -> relation valid, carry rejected, review required
    F12 predecessor deferral without successor reacceptance -> no deferral rebound
    F13 explicit successor deferral reacceptance -> deferral rebound
    F14 CARRY_FORWARD unchanged meaning -> CONTINUITY; the fixture includes the valid unchanged case.

The hidden evaluator key contains exact expected outputs.

## 12. Output contract

For each fixture emit exactly:

    fixture_id
    relation_valid
    current_effect_ids
    successor_initialization[]
        successor_id
        mode
        carried_components
        deferral_rebound
    review_required
    reason_codes

Ordering rules:

    current_effect_ids sorted lexically
    successor_initialization sorted by successor_id
    carried_components sorted lexically
    reason_codes sorted lexically.

Allowed initialization modes:

    CONTINUITY
    OPEN_RESET
    CARRY_FACTS_FOR_REVALIDATION.

## 13. Outcome classes

D2_LINEAGE_EXTENSION_PLAUSIBLE only if:

    Evaluator A matches the frozen key on all fourteen fixtures;
    independently authored Evaluator B matches the frozen key on all fourteen fixtures;
    A and B agree exactly;
    F01 proves true crossing repartition;
    F02 rejects atomic staggered supersession;
    F03 preserves valid independent staged transition;
    F06/F07 enforce reinstatement identity semantics;
    F08-F11 enforce default reset and bounded carry;
    F12/F13 enforce no automatic deferral carry;
    no evaluator uses free-text semantic adjudication.

D2_AMEND if the mechanism remains coherent but one bounded lineage/carry rule needs correction.

D2_REDESIGN_REQUIRED if true repartition or realization succession cannot be represented without hidden prose adjudication, partial identity currentness, duplicate authority, or automatic stale carry.

HARNESS_INVALID if fixtures/key/protocol change after either evaluator has seen results.

## 14. Limits

A D-2 pass is mechanism evidence.

It does not establish:

    production lineage scale
    full Specification 028 migration lineage
    long-run churn cost
    arbitrary semantic mapping quality
    owner review efficacy.

The mapping matrix is an accepted governing artifact. The probe tests its deterministic mechanics, not whether a model can infer the correct matrix from arbitrary prose.

## 15. Current boundary

    PROBE=HYBRID_D2_LINEAGE_EXTENSION_V01
    FIXTURES=14
    EVALUATORS_REQUIRED=2_DIFFERENT_MODELS
    CLAUDE_BLIND_TO_KEY_AND_EVALUATOR_A=true
    OWNER_PARTICIPATION_REQUIRED=false
    HIDDEN_R2_DETAILS=SEALED

    NEXT=AUTHOR_AND_FREEZE_CHATGPT_EVALUATOR_A
