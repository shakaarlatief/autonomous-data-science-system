# Research 493: D-1 ChatGPT evaluator A freeze

**Date:** 2026-10-03
**Status:** EVALUATOR A FROZEN / CLAUDE EVALUATOR B HANDOFF NEXT
**Parent:** Research 492
**Probe ID:** HYBRID_D1_REAL_EVENT_REPLAY_V01
**Evaluator A:** experiments/ao10_hybrid_d1_replay_v01/evaluator_chatgpt_a.py
**Evaluator A SHA-256:** 082e1dce1a1af5504ae51b95e640878c61f4484d2065043e8e80b4470f9e46fd
**Scope:** Freeze ChatGPT's D-1 evaluator before any Claude evaluator source or D-1 result exists.
**Authority:** Development evaluator freeze only. No D-1 result is observed or inferred here.

## 1. Frozen authoring boundary

Evaluator A was authored against the frozen public D-1 replay inputs:

    accepted_j1.json
    source_facts.json
    definitions.json
    evaluator_contract.json

The hidden evaluator key was already frozen by Research 492.

Evaluator A implements:

    evaluate(accepted_j1, source_facts) -> dict

and derives the material D-1 fields mechanically from the accepted J1 package and actual J2 source facts.

## 2. Pre-execution validation

Observed:

    EVALUATOR_A_AST=PASS
    EVALUATOR_A_SHA256=082e1dce1a1af5504ae51b95e640878c61f4484d2065043e8e80b4470f9e46fd
    EVALUATOR_A_BYTES=9512

Evaluator A has not been executed against the D-1 source facts.

No D-1 comparison result exists.

## 3. Claude independence requirement

Claude Evaluator B must be authored independently from only:

    experiments/ao10_hybrid_d1_replay_v01/accepted_j1.json
    experiments/ao10_hybrid_d1_replay_v01/source_facts.json
    experiments/ao10_hybrid_d1_replay_v01/definitions.json
    experiments/ao10_hybrid_d1_replay_v01/evaluator_contract.json
    Research 490-492 as reviewer-facing explanation where useful
    current routing/state needed for task authorization.

Before committing its evaluator source, Claude must not inspect:

    experiments/ao10_hybrid_d1_replay_v01/evaluator_key.json
    experiments/ao10_hybrid_d1_replay_v01/evaluator_chatgpt_a.py
    any Evaluator A output
    any D-1 comparison/result.

Claude's bounded write surface remains MC-0029 collaboration messages.

## 4. Current boundary

    EVALUATOR_A=FROZEN
    EVALUATOR_A_EXECUTED=false
    EVALUATOR_B_EXISTS=false
    D1_RESULT_EXISTS=false

    NEXT=FREEZE_D1_CLAUDE_EVALUATOR_B_HANDOFF
