# Research 481: D-3 cross-plane dependency proof result

**Date:** 2026-10-03
**Status:** D3_DEPENDENCY_PROOF_PASSES / D2 LINEAGE EXTENSION NEXT
**Protocol:** Research 479
**Implementation freeze:** Research 480
**Frozen implementation commit:** 33662ea6b1582f6c8a11ebef7da4bf4c95ed4a8d
**Result artifact:** experiments/ao10_hybrid_d3_dependency_v01/result.json
**Result SHA-256:** 797c672bd6d05136638347039b3e67405f51dc540acfec07af9ced26cc6b2e31
**Scope:** Record the single frozen D-3 proof execution and reconcile the cross-plane dependency model in THIN_CENTRED_HYBRID_V02.
**Authority:** Development proof evidence only. No production selection, migration, Specification 028 replacement, dependent-DRP resumption, or hidden-R2 exposure.

## 1. Frozen result

Observed:

    base_valid                      true
    next_revision_feedback_valid   true
    negative_controls_all_match    true
    outcome                         D3_DEPENDENCY_PROOF_PASSES

Every frozen proof check passed:

    P1 same-revision graph is acyclic
    P2 lineage -> active set -> J3 -> orientation precedence holds
    P3 meta-assurance does not feed the same J3 snapshot
    P4 operational feedback increments revision
    P5 shared predicate identities are unique
    P6 J3 and WARRANT-F consume the same shared predicate identities
    P7 generated orientation/control remain downstream
    P8 detective output routes review only.

## 2. Same-revision stratification

The qualified direction is:

    J1 accepted governing meaning
        -> lineage resolution
        -> current active requirement set

    natural-owner source facts
        -> shared evidence/freshness predicates
        -> WARRANT-F base decisions where required

    current active requirement set
        + shared predicates
        + required WARRANT-F base decisions
        -> J3 requirement truth

    J3 requirement truth
        -> generated orientation
        -> review routing

    J3 requirement truth
        -> optional WARRANT-F meta-assurance on exact frozen J3 snapshot
        -> compiled control

    J3 / assurance outputs
        -> compiled control
        -> AO pre-dispatch conformance
        -> delivery execution.

No current-revision evaluator feeds back into its own semantic inputs.

## 3. Temporal feedback

Operational feedback is allowed only through a later immutable snapshot.

Examples:

    delivery execution at r
        -> natural-owner source facts at r+1

    resolved review at r
        -> corrected source facts or accepted governing meaning at r+1.

This preserves feedback and self-improvement without evaluator recursion.

## 4. Shared evidence/freshness semantics

D-3 also closes the duplicate-predicate concern at mechanism level.

WARRANT-F and J3 do not own separate meanings for evidence validity/freshness.

They consume one versioned predicate identity/definition.

A duplicated predicate identity with a different digest failed the frozen negative control.

The production representation of the shared predicate registry remains a later implementation question.

## 5. Meta-assurance

WARRANT-F may evaluate a claim about a J3-derived fact only against an exact J3 snapshot/revision.

That decision is downstream.

It cannot change the same J3 snapshot it evaluated.

A frozen negative control adding:

    WARRANT_F_META_ON_J3_SNAPSHOT
        -> J3_REQUIREMENT_TRUTH

failed because it creates a same-revision cycle.

## 6. Detective boundary

Detective observations may produce:

    REVIEW_ROUTING

but do not directly mutate:

    J1 accepted governing meaning
    natural-owner source facts
    J3 truth.

Any correction requires the appropriate later governed/factual revision.

This preserves detector non-authority.

## 7. Evidence strength

D-3 is a bounded architecture dependency proof over the frozen V0.2 graph.

It does not prove:

    production implementation correctness
    performance
    every future domain extension is acyclic
    D-2 lineage extension
    D-1 integrated real-event execution.

Every future cross-plane dependency extension must revalidate the graph.

## 8. Current disposition

    D3=D3_DEPENDENCY_PROOF_PASSES

    THIN_CENTRED_HYBRID_V02=REMAINS_LEADING_CANDIDATE
    D1=REQUIRED
    D2=REQUIRED

    OWNER_ARCHITECTURE_DECISION_READY=false
    PRODUCTION_TARGET_SELECTED=false
    HIDDEN_R2_DETAILS=SEALED

    NEXT=FREEZE_D2_LINEAGE_EXTENSION_PROTOCOL
