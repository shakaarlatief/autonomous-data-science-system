# Research 486: D-2 pre-score output-contract clarification

**Date:** 2026-10-03
**Status:** PRE-SCORE CLARIFICATION FROZEN / NO D-2 RESULT OBSERVED
**Parent:** Research 482-485 / MC-0029 Message 018
**Fixed evidence base:** cd0cf087a4d0ddb30920a8c753e478da8f92295c
**Probe ID:** HYBRID_D2_LINEAGE_EXTENSION_V01
**Scope:** Resolve one reviewer-facing output-contract under-specification identified independently by Claude before ChatGPT executes either evaluator or scores D-2.
**Authority:** Development-probe scoring clarification only. Fixtures, semantic rules, hidden key, Evaluator A and Evaluator B source are not changed.

## 1. Trigger

Message 018 was authored independently while blind to:

    evaluator_key.json
    evaluator_chatgpt_a.py
    evaluator-A output
    D-2 result/comparison.

Before any D-2 scoring, Claude identified that reason_codes is required by the public output contract but no public vocabulary defines:

    exact reason-code strings;
    whether informational codes are emitted on valid relations.

That makes exact string agreement on reason_codes impossible to interpret as independent semantic agreement.

## 2. Clarification principle

The D-2 test is intended to test:

    relation validity
    current-effect resolution
    realization initialization mode
    carried successor components
    deferral rebound
    review requirement.

reason_codes is diagnostic explanation.

It is not governing lineage truth.

Therefore the frozen D-2 comparison will report two scores.

### 2.1 Full-object diagnostic score

For transparency, compute exact equality against the frozen evaluator key including:

    reason_codes.

This score is diagnostic only.

It preserves visibility into every difference from the originally frozen hidden key.

### 2.2 Semantic pass/fail score

For D-2 outcome classification, compare the frozen semantic output object after removing only:

    reason_codes.

The semantic object still includes exactly:

    fixture_id
    relation_valid
    current_effect_ids
    successor_initialization
        successor_id
        mode
        carried_components
        deferral_rebound
    review_required.

No other field is ignored or normalized away.

Thus:

    disagreement over invalid-relation currentness;
    disagreement over successor initialization timing;
    disagreement over carried component naming/content;
    disagreement over deferral rebound;
    disagreement over review_required

remains a material D-2 disagreement and cannot be hidden by this clarification.

## 3. Outcome clarification

Research 482's D2_LINEAGE_EXTENSION_PLAUSIBLE condition is interpreted prospectively as:

    Evaluator A semantic object matches frozen key semantic object on all fourteen fixtures;
    Evaluator B semantic object matches frozen key semantic object on all fourteen fixtures;
    A and B semantic objects agree exactly on all fourteen fixtures;
    all substantive fixture-specific D-2 conditions remain satisfied.

Exact reason_codes agreement is separately reported but is not pass/fail evidence.

If a non-reason_codes mismatch appears:

    do not massage or normalize it after observation;
    classify D2_AMEND or D2_REDESIGN_REQUIRED under Research 482.

## 4. Other Message 018 ambiguities

Message 018 also documents conventions for:

    invalid-transition outputs;
    carried component names;
    future-effective successor initialization;
    retired/unaffected portion format;
    CARRY_FORWARD edge cases;
    carry-block validity scope.

This clarification does not retroactively choose Claude's conventions.

Any difference in the semantic output fields caused by those conventions remains visible and material.

The only scoring relaxation is exact reason_codes string equality.

## 5. Integrity

At this clarification point:

    ChatGPT has not executed Evaluator A;
    ChatGPT has not materialized/executed Evaluator B;
    no D-2 comparison result exists;
    no fixture or hidden-key value is changed.

Message 018 itself contains no score against the hidden key.

Therefore this is a prospective scoring clarification rather than post-result threshold tuning.

## 6. Current boundary

    REASON_CODES=DIAGNOSTIC_ONLY
    SEMANTIC_FIELDS=UNCHANGED_AND_STRICT
    FIXTURES=UNCHANGED
    HIDDEN_KEY=UNCHANGED
    EVALUATOR_A=UNCHANGED_UNEXECUTED
    EVALUATOR_B=UNCHANGED_UNEXECUTED_BY_CHATGPT
    D2_RESULT_EXISTS=false

    NEXT=MATERIALIZE_AND_FREEZE_CLAUDE_EVALUATOR_B
