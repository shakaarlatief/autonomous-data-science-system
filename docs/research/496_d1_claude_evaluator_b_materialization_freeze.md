# Research 496: D-1 Claude evaluator B materialization freeze

**Date:** 2026-10-03
**Status:** EVALUATOR B MATERIALIZED AND FROZEN / COMPARISON HARNESS FREEZE NEXT
**Parent:** Research 490-495 / MC-0029 Message 020
**Fixed evidence base:** 83d40f35587116008655374032b9a881214c6397
**Probe ID:** HYBRID_D1_REAL_EVENT_REPLAY_V01
**Scope:** Materialize Claude's independently authored Message 020 Python block with no semantic edits and freeze it before any ChatGPT-side D-1 evaluator execution.
**Authority:** Development evaluator freeze only. No D-1 score or result is observed here.

## 1. Source provenance

Claude Message 020 commit:

    e80a007adf9a39c83b2abccbd22fe5f767fdb50e

Message file:

    docs/model_collaboration/threads/MC-0029/messages/020_claude_d1_integrated_replay_evaluator_b.md

Message SHA-256 over current working-tree bytes:

    bc619d962f0b94f2d8792d049b443b9cfbac0eba5a60521627b66d7e42d054eb

Exactly one fenced Python block was present.

It was extracted without semantic edits.

Only Markdown-fence removal and line-ending/final-newline normalization were permitted.

## 2. Materialized evaluator

Materialized path:

    experiments/ao10_hybrid_d1_replay_v01/evaluator_claude_b.py

Observed:

    EVALUATOR_B_SHA256=d6899286ac281b4e26097accfca39e79acdd8253f6f9ab2d3f6f757be05ac463
    EVALUATOR_B_BYTES=15168
    EVALUATOR_B_AST=PASS

No D-1 replay input was passed to Evaluator B during ChatGPT materialization.

No hidden-key comparison was performed.

## 3. Independence state

Evaluator A:

    author = ChatGPT
    SHA-256 = 082e1dce1a1af5504ae51b95e640878c61f4484d2065043e8e80b4470f9e46fd

Evaluator B:

    author = Claude / claude-04
    SHA-256 = d6899286ac281b4e26097accfca39e79acdd8253f6f9ab2d3f6f757be05ac463

Claude Message 020 attests blindness to:

    evaluator_key.json
    evaluator_chatgpt_a.py
    Evaluator A output
    D-1 result/comparison
    hidden R2 item-level material.

The independent-author requirement is satisfied at source-authoring level.

## 4. Recorded reviewer-facing ambiguities

Message 020 records ambiguity in:

    acceptance_binding_valid
    source_fact_contract_valid
    lineage_relation_valid
    review-required/orientation coupling
    review-owner precedence
    fixture-specific currentness generalization.

These are material D-1 fields.

No scoring relaxation is introduced.

Any actual A/B/key disagreement on those fields remains material D-1 evidence and must be reconciled as D1_AMEND or D1_REDESIGN_REQUIRED.

## 5. Current boundary

    EVALUATOR_A=FROZEN_UNEXECUTED
    EVALUATOR_B=FROZEN_UNEXECUTED_BY_CHATGPT
    D1_RESULT_EXISTS=false
    ALL_OUTPUT_FIELDS=MATERIAL
    HASH_BASIS=GIT_BLOB_BYTES_AT_COMMIT
    HIDDEN_R2_DETAILS=SEALED

    NEXT=FREEZE_D1_TWO_MODEL_COMPARISON_HARNESS
