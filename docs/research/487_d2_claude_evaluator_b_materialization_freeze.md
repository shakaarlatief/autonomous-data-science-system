# Research 487: D-2 Claude evaluator B materialization freeze

**Date:** 2026-10-03
**Status:** EVALUATOR B MATERIALIZED AND FROZEN / TWO-EVALUATOR EXECUTION NEXT
**Parent:** Research 482-486 / MC-0029 Message 018
**Fixed evidence base:** 36b1a6f28a431adb700085d64d2646cce5dfee16
**Probe ID:** HYBRID_D2_LINEAGE_EXTENSION_V01
**Scope:** Materialize Claude's independently authored Message 018 Python block byte-for-byte apart from normalized line endings, syntax-check it, and freeze it before any ChatGPT-side D-2 evaluator execution.
**Authority:** Development evaluator freeze only. No D-2 score or result is observed here.

## 1. Source provenance

Claude Message 018 commit:

    cd0cf087a4d0ddb30920a8c753e478da8f92295c

Message file:

    docs/model_collaboration/threads/MC-0029/messages/018_claude_d2_lineage_evaluator_b.md

Message SHA-256:

    9d23abafee8ae8e3bcc2d9a3ac7d9d9b0e80118032b1d38661ad5cfd2f472348

Exactly one fenced Python block was found.

That block was extracted without semantic edits.

Only line-ending normalization and one final newline normalization were permitted.

## 2. Materialized evaluator

Materialized path:

    experiments/ao10_hybrid_d2_lineage_v01/evaluator_claude_b.py

Observed:

    EVALUATOR_B_SHA256=b4c8ff134ce51f7c833600a8e87849205cf1f2554102314f5ff1ea30aba3ee3b
    EVALUATOR_B_BYTES=14472
    EVALUATOR_B_AST=PASS

No fixture was passed to Evaluator B during ChatGPT materialization.

No hidden-key comparison was performed.

## 3. Independence state

Evaluator A:

    author = ChatGPT
    SHA-256 = 26b63dcc0968b73927145bdd495865091a5ef1847feb28213549d7eb6c914e6f

Evaluator B:

    author = Claude / claude-04
    SHA-256 = b4c8ff134ce51f7c833600a8e87849205cf1f2554102314f5ff1ea30aba3ee3b

Claude's Message 018 attests that it remained blind to:

    evaluator_key.json
    evaluator_chatgpt_a.py
    evaluator-A output
    D-2 result/comparison
    hidden R2 item-level material.

The independent-author requirement is therefore satisfied at source-authoring level.

## 4. Scoring rule

Research 486 remains authoritative for comparison:

    semantic pass/fail score
        all output fields except reason_codes

    full-object diagnostic score
        includes reason_codes.

No evaluator source, fixture, hidden-key value, or semantic scoring field may now change before execution.

## 5. Execution rule

The next step is one frozen comparison run that:

    loads all 14 reviewer fixtures;
    executes Evaluator A and Evaluator B;
    compares each output to the frozen evaluator key;
    records semantic equality with reason_codes removed;
    records full-object exact equality separately;
    records A/B semantic and full-object agreement separately.

No post-result normalization is permitted.

## 6. Current boundary

    EVALUATOR_A=FROZEN
    EVALUATOR_B=FROZEN
    EVALUATOR_A_EXECUTED_BY_CHATGPT=false
    EVALUATOR_B_EXECUTED_BY_CHATGPT=false
    D2_RESULT_EXISTS=false
    SEMANTIC_SCORING=STRICT_EXCEPT_REASON_CODES
    HIDDEN_R2_DETAILS=SEALED

    NEXT=EXECUTE_D2_TWO_MODEL_COMPARISON_ONCE
