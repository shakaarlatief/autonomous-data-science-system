# Research 488: D-2 two-model comparison implementation freeze

**Date:** 2026-10-03
**Status:** COMPARISON HARNESS FROZEN / SINGLE EXECUTION NEXT
**Parent:** Research 482-487
**Probe ID:** HYBRID_D2_LINEAGE_EXTENSION_V01
**Comparison manifest SHA-256:** b5519a885a9d9b00b7627c8bc799d644666cb386a861fea791529708e5779200
**Scope:** Freeze the exact two-model comparison runner and all bound D-2 inputs before the first ChatGPT-side evaluator execution.
**Authority:** Development comparison freeze only. No D-2 result is observed here.

## 1. Frozen comparison inputs

The comparison manifest binds:

    reviewer_fixtures.json
    evaluator_contract.json
    evaluator_key.json
    evaluator_chatgpt_a.py
    evaluator_claude_b.py
    run_two_model_comparison.py
    static_validate_comparison.py

Static validation passed.

No result.json exists at freeze time.

## 2. Frozen scoring behavior

The runner computes:

    full-object diagnostic equality
        includes reason_codes

and:

    semantic equality
        removes reason_codes only.

Every other output field remains strict.

Outcome classification follows Research 486.

## 3. Independence

Evaluator A:

    author = ChatGPT

Evaluator B:

    author = Claude / claude-04

Claude authored Evaluator B before seeing:

    evaluator_key.json
    evaluator_chatgpt_a.py
    evaluator-A output
    any D-2 result.

Both evaluator source files are now immutable for this run.

## 4. Execution rule

Exactly one normal comparison execution is authorized.

If semantic mismatches appear:

    preserve them;
    do not edit evaluators, fixtures, key or runner and rerun;
    reconcile as D2_AMEND or D2_REDESIGN_REQUIRED.

## 5. Current boundary

    COMPARISON_MANIFEST_SHA256=b5519a885a9d9b00b7627c8bc799d644666cb386a861fea791529708e5779200
    RESULT_EXISTS=false
    EXECUTION_COUNT=0

    NEXT=EXECUTE_D2_TWO_MODEL_COMPARISON_ONCE
