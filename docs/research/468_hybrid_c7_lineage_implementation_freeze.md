# Research 468: HYBRID C7 lineage implementation freeze

**Date:** 2026-10-03
**Status:** IMPLEMENTATION FROZEN / SINGLE EXECUTION NEXT
**Protocol:** Research 467
**Protocol commit:** be1dd3763d06af11bd2e1aeccd50b9e1da529230
**Implementation root:** experiments/ao10_hybrid_c7_lineage_v01
**Manifest SHA-256:** 9a3f4df5be021bd3cf8c3d3d37a77eea78776796026c4e129d6b8ee4cbe4ebed
**Scope:** Freeze the exact C7 lineage harness before business-rule execution.
**Authority:** Development implementation freeze only. This record does not select production architecture, amend Specification 028, expose hidden R2 material, resume dependent DRPs, migrate repository state, or switch authority.

## 1. Frozen implementation

The pre-result implementation contains:

    definitions.json
    fixtures.json
    evaluator_a.py
    evaluator_b.py
    run_comparison.py
    static_validate.py
    manifest.json

The manifest binds the six pre-result business/fixture files by exact SHA-256 and byte count.

The manifest itself hashes to:

    9a3f4df5be021bd3cf8c3d3d37a77eea78776796026c4e129d6b8ee4cbe4ebed

No result.json exists at freeze time.

## 2. Frozen fixture count

    lineage fixtures           12
    evaluators                  2

The expected outputs are embedded in fixtures.json and may not change after execution.

## 3. Evaluator separation

Evaluator A uses procedural transition validation, explicit outgoing-relation checks, depth-first cycle detection and terminal-target traversal.

Evaluator B normalizes relation tables, uses independent cardinality/retirement validation, topological cycle detection and normalized reachability closure.

They share fixture parsing only.

They do not call one another's business-rule functions.

This is code-path independence, not independent-author confirmation.

## 4. Static-only preflight

Observed before freeze:

    HYBRID_C7_STATIC_VALIDATION=PASS

The static validator checked:

    probe identity
    exact fixture count
    fixture-ID uniqueness
    Python syntax for both evaluators and the runner
    absence of result.json

It did not import or execute either evaluator.

## 5. Frozen semantics

The implementation treats:

    CARRY_FORWARD
        as same-identity continuity only when the exact semantic digest is unchanged;

    REPLACE
        as 1:1 semantic succession;

    SPLIT
        as 1:N semantic succession in one governed relation;

    MERGE
        as N:1 semantic succession in one governed relation;

    RETIRE
        as explicit no-successor closure backed by retirement authority/evidence.

Every live predecessor in transition scope must be accounted for by one governed relation or an explicit UNAFFECTED declaration.

Competing active outgoing semantic-succession relations are invalid.

Non-continuity succession must remain acyclic.

## 6. Execution rule

Exactly one normal business-rule execution is authorized against these frozen files.

If execution reveals a defect:

    preserve the result;
    do not change fixtures or evaluators and silently rerun;
    classify under Research 467 outcome rules.

## 7. Current boundary

    IMPLEMENTATION=FROZEN
    MANIFEST_SHA256=9a3f4df5be021bd3cf8c3d3d37a77eea78776796026c4e129d6b8ee4cbe4ebed
    RESULT_EXISTS=false
    HIDDEN_R2_DETAILS=SEALED
    OWNER_PARTICIPATION_REQUIRED=false

    NEXT=EXECUTE_HYBRID_C7_LINEAGE_V01_ONCE
