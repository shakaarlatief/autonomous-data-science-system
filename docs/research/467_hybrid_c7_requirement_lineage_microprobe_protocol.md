# Research 467: thin-centred hybrid C7 requirement-lineage micro-probe protocol

**Date:** 2026-10-03
**Status:** PROTOCOL FROZEN / IMPLEMENTATION NEXT
**Parent:** Research 466
**Fixed evidence base:** f5b7908d36742c1951be9cbecec4b3e67953e312
**Scope:** Prospectively freeze a bounded development probe for governed N:M requirement lineage across contract evolution.
**Authority:** Development-probe protocol only. This record does not select production architecture, amend Specification 028, expose hidden R2 item material, resume dependent DRPs, migrate repository state, or switch authority.

## 1. Question

Research 463 and Research 466 now provide stable J1 requirement identities and bounded completion semantics.

C7 asks:

> Can those identities evolve across carry-forward, replacement, split, merge and retirement without mutating history, creating competing owners, losing live obligations silently, or asking a future model to infer lineage from prose?

The probe tests only the structural lineage mechanism.

It does not attempt to prove semantic equivalence automatically.

## 2. Shared-substrate compatibility

DRP-01 admitted:

    semantic_identity
    exact_subject_revision_binding
    provenance_descriptor
    governing_lifecycle_reference
    obligation_reference
    governed_relation_reference

The C7 candidate must use those shared concepts without expanding the shared substrate into a universal project type system.

Requirement-lineage details remain a bounded semantic/lifecycle domain contract referenced through the shared substrate.

## 3. Candidate lineage model

### 3.1 Immutable accepted requirement identity

A requirement identity denotes one accepted governing effect.

Its accepted semantic payload is immutable.

Changing governing meaning does not edit the old requirement identity.

Instead, a governed transition either:

    preserves the same identity under exact semantic continuity;
    creates successor requirement identities;
    or retires the predecessor explicitly.

### 3.2 Relation classes

Freeze:

    CARRY_FORWARD
    REPLACE
    SPLIT
    MERGE
    RETIRE

CARRY_FORWARD is continuity, not semantic succession.

It preserves the same requirement identity across a new governing carrier/revision and therefore does not create a graph edge.

All other classes are prospective governed lifecycle relations.

### 3.3 Transition record

Every transition record contains:

    relation_id
    relation_class
    predecessors[]
    successors[]
    governing_authority_ref
    accepted_decision_ref
    effective_from
    source_revision_ref
    target_revision_ref
    provenance[]

For REPLACE, SPLIT and MERGE, each predecessor also receives exactly one machine-visible disposition:

    FULLY_MAPPED
    PARTIAL_WITH_EXPLICIT_RETIREMENT

If PARTIAL_WITH_EXPLICIT_RETIREMENT:

    retirement_ref

is mandatory and must identify an accepted retirement decision for the unmapped remainder.

RETIRE has no successors and requires:

    retirement_ref
    retirement_evidence_ref

CARRY_FORWARD requires:

    predecessors == successors == [same requirement id]
    semantic_digest_before == semantic_digest_after

and is treated as a continuity annotation, not a graph self-loop.

## 4. Cardinality rules

    CARRY_FORWARD
        1 predecessor
        1 identical successor

    REPLACE
        1 predecessor
        1 distinct successor

    SPLIT
        1 predecessor
        >=2 distinct successors

    MERGE
        >=2 distinct predecessors
        1 successor

    RETIRE
        >=1 predecessor
        0 successors

No duplicate endpoint is allowed within one relation.

## 5. Validity rules

A transition is valid only when:

    every endpoint exists in the frozen requirement corpus;
    predecessor identities are active immediately before effective_from;
    successors are valid accepted identities at or after effective_from;
    authority and decision refs are accepted for the exact source/target revisions;
    effective_from is inside the governing decision's effective boundary;
    provenance is non-empty;
    cardinality matches relation class;
    every predecessor has exactly one disposition within the relation;
    every PARTIAL_WITH_EXPLICIT_RETIREMENT predecessor has a valid retirement_ref;
    RETIRE has valid retirement authority/evidence;
    CARRY_FORWARD preserves exact semantic digest.

## 6. Graph rules

Ignoring CARRY_FORWARD continuity annotations:

    lineage graph must be acyclic.

For one effective boundary:

    a predecessor may participate in at most one active outgoing semantic-succession relation.

Therefore two separate REPLACE/SPLIT/RETIRE records cannot compete for the same predecessor at the same boundary.

If one predecessor intentionally maps to several successors:

    encode one SPLIT relation.

If several predecessors intentionally map to one successor:

    encode one MERGE relation.

## 7. Closed live-predecessor accounting

Each fixture declares:

    transition_scope_predecessors[]

representing every live requirement in the governing scope that the accepted change says may be affected.

At postflight each scoped predecessor must resolve to exactly one of:

    CARRIED_FORWARD
    MAPPED_TO_SUCCESSOR_SET
    RETIRED

No scoped predecessor may remain:

    UNMAPPED

unless the change package explicitly declares it:

    UNAFFECTED

with exact source/target revision binding.

For this probe, UNAFFECTED declarations are frozen structured facts, not inferred from prose.

This is the C7 analogue of KA-R52 completeness accounting.

## 8. Frozen fixtures

Freeze twelve cases.

### L1 CARRY_FORWARD_SAME_ID

P1 remains semantically identical in target revision.

Expected:

    valid=true
    current_targets=[P1]
    retired=[]
    review_required=false

### L2 ONE_TO_ONE_REPLACE

P1 is replaced by S1 under accepted authority.

Expected:

    valid=true
    current_targets=[S1]
    retired=[]
    review_required=false

### L3 ONE_TO_MANY_SPLIT

P1 is split into S1 and S2 through one SPLIT relation.

Expected:

    valid=true
    current_targets=[S1,S2]
    retired=[]
    review_required=false

### L4 MANY_TO_ONE_MERGE

P1 and P2 merge into S1 through one MERGE relation.

Expected:

    valid=true
    P1 current_targets=[S1]
    P2 current_targets=[S1]
    review_required=false

### L5 PARTIAL_REPLACE_WITH_RETIREMENT

P1 maps to S1 with predecessor disposition PARTIAL_WITH_EXPLICIT_RETIREMENT and accepted retirement R-REM.

Expected:

    valid=true
    current_targets=[S1]
    retired_remainder_refs=[R-REM]
    review_required=false

### L6 EXPLICIT_RETIRE

P1 is retired with no successor and valid retirement evidence.

Expected:

    valid=true
    current_targets=[]
    retired=[P1]
    review_required=false

### L7 UNMAPPED_LIVE_PREDECESSOR

Scope contains P1 and P2 but transition package accounts only for P1 and does not mark P2 UNAFFECTED.

Expected:

    valid=false
    unmapped=[P2]
    review_required=true

### L8 COMPETING_OUTGOING_RELATIONS

Two separate active REPLACE relations claim P1 at the same boundary.

Expected:

    valid=false
    conflict=true
    review_required=true

### L9 CYCLE

P1 -> S1 and S1 -> P1 are both active succession edges.

Expected:

    valid=false
    cycle=true
    review_required=true

### L10 UNAUTHORIZED_RELATION

P1 -> S1 has a relation authority not accepted for the exact source/target revisions.

Expected:

    valid=false
    authority_valid=false
    review_required=true

### L11 STALE_EFFECTIVE_BOUNDARY

P1 -> S1 is otherwise valid but effective_from lies outside the accepted decision boundary.

Expected:

    valid=false
    effective_boundary_valid=false
    review_required=true

### L12 INVALID_CARRY_FORWARD_DIGEST

CARRY_FORWARD keeps P1 but semantic_digest_before != semantic_digest_after.

Expected:

    valid=false
    continuity_valid=false
    review_required=true

## 9. Two evaluator requirement

Implement two evaluators after this protocol is committed.

Evaluator A:

    procedural transition validation + adjacency traversal.

Evaluator B:

    normalized relation tables + independent topological/closure derivation.

They may share fixture parsing only.

They may not call one another's business-rule functions.

## 10. Derived outputs

Each evaluator must return for each fixture:

    valid
    review_required
    authority_valid
    effective_boundary_valid
    continuity_valid
    conflict
    cycle
    unmapped[]
    current_targets_by_predecessor
    retired[]
    retired_remainder_refs[]

All arrays/maps are deterministically sorted.

No evaluator may consume free-text semantics.

## 11. Outcome classes

### C7_LINEAGE_MECHANISM_PLAUSIBLE

Only if:

    all twelve fixtures match frozen expectations in both evaluators;
    evaluators agree exactly;
    split and merge resolve N:M targets correctly;
    unmapped live predecessor is detected;
    competing outgoing relations are detected;
    cycle is rejected;
    unauthorized/stale relations fail visibly;
    changed semantics cannot pass as CARRY_FORWARD;
    no free-text reinterpretation is used.

### C7_AMEND

Use if the mechanism is sound but a bounded schema/evaluator rule needs local amendment.

### C7_REDESIGN_REQUIRED

Use if N:M lineage cannot be expressed without mutating accepted history, duplicating authority, implementation-bound grouping, or future prose interpretation.

### HARNESS_INVALID

Use if frozen fixtures/expectations or implementation are changed after result observation.

## 12. Limits

A pass will not prove:

    that an owner always chooses the correct semantic successor mapping;
    that all real Specification 028 obligations have already been migrated;
    that DRP-07's full 46-section / 104-MUST audit passes;
    that retirement evidence policy is final;
    that C8 orientation or C9 burden is solved.

It only qualifies the structural N:M lineage mechanism needed before the larger DRP-07 lineage audit can be redesigned.

## 13. Current boundary

    PROBE=HYBRID_C7_LINEAGE_V01
    FIXTURES=12
    IMPLEMENTATIONS_REQUIRED=2
    HIDDEN_R2_DETAILS=SEALED
    OWNER_PARTICIPATION_REQUIRED=false

    NEXT=IMPLEMENT_AND_FREEZE_HYBRID_C7_LINEAGE_V01
