# Research 480: D-3 cross-plane dependency proof implementation freeze

**Date:** 2026-10-03
**Status:** IMPLEMENTATION FROZEN / SINGLE PROOF EXECUTION NEXT
**Protocol:** Research 479
**Protocol commit:** b79d842b119b21877bbac28e11b5522d9cea6cb0
**Implementation root:** experiments/ao10_hybrid_d3_dependency_v01
**Manifest SHA-256:** af306ed8b728883221714d9eb971a9c2010524df0ea07ca2b194d538c203d715
**Scope:** Freeze the exact D-3 dependency graph/checker before evaluating the frozen proof obligations.
**Authority:** Development proof implementation only. No production selection, migration, Specification 028 replacement, dependent-DRP resumption, or hidden-R2 exposure.

## 1. Frozen files

The pre-result harness contains:

    graph.json
    predicate_registry.json
    negative_controls.json
    check_dependency.py
    static_validate.py
    manifest.json

The manifest binds the five pre-result proof/business files by exact SHA-256 and byte count.

No result.json exists at freeze time.

## 2. Static preflight

Observed:

    HYBRID_D3_STATIC_VALIDATION=PASS

The static validator checked:

    probe identity
    exact 14-node graph
    exact five negative controls
    checker syntax
    absence of result.json.

It did not execute the dependency proof.

## 3. Frozen proof mechanics

The checker validates:

    same-revision DAG property
    lineage -> active set -> J3 -> orientation precedence
    absence of forbidden same-revision feedback
    detective-output review-only behavior
    shared predicate registry uniqueness
    shared J3/WARRANT-F predicate consumption
    positive next-revision feedback semantics.

Negative controls then deliberately introduce:

    meta-assurance -> same J3
    delivery -> same-revision source facts
    duplicate predicate identity with different digest
    orientation -> lineage
    and one valid next-revision delivery feedback edge.

## 4. Execution rule

Exactly one normal proof execution is authorized.

If the checker or frozen graph fails:

    preserve the result
    do not alter expectations and silently rerun
    reconcile under Research 479.

## 5. Current boundary

    IMPLEMENTATION=FROZEN
    MANIFEST_SHA256=af306ed8b728883221714d9eb971a9c2010524df0ea07ca2b194d538c203d715
    RESULT_EXISTS=false
    OWNER_PARTICIPATION_REQUIRED=false
    HIDDEN_R2_DETAILS=SEALED

    NEXT=EXECUTE_D3_DEPENDENCY_PROOF_ONCE
