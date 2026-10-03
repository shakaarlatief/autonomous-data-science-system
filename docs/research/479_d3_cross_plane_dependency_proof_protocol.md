# Research 479: D-3 cross-plane dependency proof protocol

**Date:** 2026-10-03
**Status:** PROTOCOL FROZEN / DEPENDENCY PROOF NEXT
**Parent:** Research 477-478
**Fixed evidence base:** 89c87ab43e00b7ce2da5e8fe720d2da200b8f83e
**Probe ID:** HYBRID_D3_DEPENDENCY_V01
**Scope:** Prospectively freeze the exact cross-plane dependency graph and proof obligations needed to show that THIN_CENTRED_HYBRID_V02 has no same-revision evaluation cycle and no duplicated evidence/freshness semantics.
**Authority:** Development proof protocol only. No production selection, migration, Specification 028 replacement, dependent-DRP resumption, or hidden-R2 exposure.

## 1. Question

D-3 asks:

> Can AO, lineage, natural-owner facts, shared predicates, WARRANT-F, J3, generated orientation and compiled control be ordered so that consequential truth has one deterministic dependency direction, while operational feedback occurs only through a later revision/snapshot?

## 2. Revision model

The proof distinguishes:

    same_revision edges
        must form a directed acyclic graph.

    next_revision feedback edges
        may return operational results to source facts or governing events only by creating a new immutable snapshot/revision.

A next-revision edge is not a same-revision evaluation dependency.

## 3. Frozen same-revision nodes

    J1_ACCEPTED_GOVERNING_MEANING
    LINEAGE_RESOLUTION
    CURRENT_ACTIVE_REQUIREMENT_SET
    NATURAL_OWNER_SOURCE_FACTS
    SHARED_EVIDENCE_FRESHNESS_PREDICATES
    WARRANT_F_BASE_DECISIONS
    J3_REQUIREMENT_TRUTH
    WARRANT_F_META_ON_J3_SNAPSHOT
    GENERATED_ORIENTATION
    CONTROL_COMPILATION
    AO_PRE_DISPATCH_CONFORMANCE
    DELIVERY_EXECUTION
    REVIEW_ROUTING
    DETECTIVE_OBSERVATION

## 4. Frozen same-revision edges

    J1_ACCEPTED_GOVERNING_MEANING
        -> LINEAGE_RESOLUTION

    LINEAGE_RESOLUTION
        -> CURRENT_ACTIVE_REQUIREMENT_SET

    CURRENT_ACTIVE_REQUIREMENT_SET
        -> J3_REQUIREMENT_TRUTH

    NATURAL_OWNER_SOURCE_FACTS
        -> SHARED_EVIDENCE_FRESHNESS_PREDICATES

    SHARED_EVIDENCE_FRESHNESS_PREDICATES
        -> WARRANT_F_BASE_DECISIONS

    SHARED_EVIDENCE_FRESHNESS_PREDICATES
        -> J3_REQUIREMENT_TRUTH

    WARRANT_F_BASE_DECISIONS
        -> J3_REQUIREMENT_TRUTH

    J3_REQUIREMENT_TRUTH
        -> WARRANT_F_META_ON_J3_SNAPSHOT

    J3_REQUIREMENT_TRUTH
        -> GENERATED_ORIENTATION

    J3_REQUIREMENT_TRUTH
        -> CONTROL_COMPILATION

    WARRANT_F_META_ON_J3_SNAPSHOT
        -> CONTROL_COMPILATION

    GENERATED_ORIENTATION
        -> REVIEW_ROUTING

    CONTROL_COMPILATION
        -> AO_PRE_DISPATCH_CONFORMANCE

    AO_PRE_DISPATCH_CONFORMANCE
        -> DELIVERY_EXECUTION

    NATURAL_OWNER_SOURCE_FACTS
        -> DETECTIVE_OBSERVATION

    J1_ACCEPTED_GOVERNING_MEANING
        -> DETECTIVE_OBSERVATION

    DETECTIVE_OBSERVATION
        -> REVIEW_ROUTING

There is no same-revision edge from:

    WARRANT_F_META_ON_J3_SNAPSHOT -> J3_REQUIREMENT_TRUTH
    GENERATED_ORIENTATION -> J3_REQUIREMENT_TRUTH
    CONTROL_COMPILATION -> J3_REQUIREMENT_TRUTH
    DELIVERY_EXECUTION -> NATURAL_OWNER_SOURCE_FACTS
    REVIEW_ROUTING -> J1_ACCEPTED_GOVERNING_MEANING.

Those interactions require a later snapshot/revision.

## 5. Frozen next-revision feedback

    DELIVERY_EXECUTION(r)
        -> NATURAL_OWNER_SOURCE_FACTS(r+1)

    REVIEW_RESOLUTION(r)
        -> J1_ACCEPTED_GOVERNING_MEANING(r+1)
        OR
        -> NATURAL_OWNER_SOURCE_FACTS(r+1)

    ARCHITECTURE_EVOLUTION_DECISION(r)
        -> J1_ACCEPTED_GOVERNING_MEANING(r+1)

These are temporal feedback, not evaluator recursion.

## 6. Shared predicate rule

Evidence validity/freshness is defined once by a versioned shared predicate contract.

Both:

    WARRANT_F_BASE_DECISIONS
    J3_REQUIREMENT_TRUTH

may consume the same predicate result/reference.

They may not implement semantically distinct private versions under the same predicate identity.

The proof artifact must therefore declare for every shared predicate:

    predicate_id
    definition_revision
    executable_definition_digest
    consumers[].

Duplicate predicate_id with different digest/revision is invalid.

## 7. Meta-assurance rule

WARRANT_F_META_ON_J3_SNAPSHOT may evaluate a claim about J3 only when bound to:

    exact J3 snapshot/revision
    exact requirement/effect subject.

Its decision is downstream of that J3 snapshot.

It may affect:

    compiled control
    later admission
    later review.

It may not change the J3 snapshot it evaluated.

## 8. Lineage precedence

For a given revision:

    lineage resolution precedes current-requirement selection;
    current-requirement selection precedes J3;
    J3 precedes orientation.

No orientation state may determine semantic lineage.

No J3 satisfaction result may decide whether semantic identity is carried forward, split, merged, repartitioned, retired or reinstated.

Those are accepted lifecycle decisions.

## 9. Frozen proof checks

The proof must establish:

    P1 same-revision graph is a DAG.
    P2 every topological ordering respects lineage -> active set -> J3 -> orientation.
    P3 no meta-assurance result feeds the same J3 snapshot.
    P4 delivery/review feedback enters only a later revision.
    P5 shared evidence/freshness predicate identities are unique by exact definition revision/digest.
    P6 J3 and WARRANT-F consumers reference the same shared predicate identity rather than duplicating semantics.
    P7 generated orientation and compiled control are downstream only.
    P8 detective output routes review but never mutates current governing truth.

## 10. Frozen negative controls

    N1 add WARRANT_F_META_ON_J3_SNAPSHOT -> J3_REQUIREMENT_TRUTH.
       Expected: cycle / invalid.

    N2 add DELIVERY_EXECUTION -> NATURAL_OWNER_SOURCE_FACTS as same_revision.
       Expected: cycle-risk / invalid.

    N3 duplicate predicate_id EVIDENCE_FRESHNESS_V1 with a different digest.
       Expected: predicate-registry invalid.

    N4 add GENERATED_ORIENTATION -> LINEAGE_RESOLUTION.
       Expected: cycle / precedence invalid.

    N5 represent next-revision DELIVERY -> FACTS feedback with explicit revision increment.
       Expected: valid temporal feedback.

## 11. Outcome classes

D3_DEPENDENCY_PROOF_PASSES only if P1-P8 pass and N1-N4 fail while N5 passes.

D3_AMEND if the architecture remains stratifiable but the exact graph needs a bounded local correction.

D3_REDESIGN_REQUIRED if the required semantics inherently demand a same-revision cycle or duplicated evidence/freshness authority.

HARNESS_INVALID if the graph or expected controls are changed after result observation.

## 12. Limits

A pass proves dependency stratification of the frozen candidate graph.

It does not prove runtime performance, production correctness, or that every future domain extension will remain acyclic.

New cross-plane dependencies require revalidation.

## 13. Current boundary

    PROBE=HYBRID_D3_DEPENDENCY_V01
    SAME_REVISION_NODES=14
    NEGATIVE_CONTROLS=5
    OWNER_PARTICIPATION_REQUIRED=false
    HIDDEN_R2_DETAILS=SEALED

    NEXT=EXECUTE_D3_DEPENDENCY_PROOF
