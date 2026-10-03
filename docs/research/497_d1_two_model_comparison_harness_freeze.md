# Research 497: D-1 two-model comparison harness freeze

**Date:** 2026-10-03
**Status:** COMPARISON HARNESS FROZEN / SINGLE EXECUTION NEXT
**Parent:** Research 490-496
**Probe ID:** HYBRID_D1_REAL_EVENT_REPLAY_V01
**Fixed base commit:** cd8b712c67fd624cb0624cd0349fccaef75e31d1
**Runner:** experiments/ao10_hybrid_d1_replay_v01/run_two_model_comparison.py
**Runner pre-commit content SHA-256:** b3f327271024d645c22f9753e17959ffb5d8b4e63b4710d4593b2504a794e1a4
**Hash basis for existing frozen inputs:** GIT_BLOB_BYTES_AT_COMMIT
**Scope:** Freeze the exact D-1 two-model comparison semantics before the first ChatGPT-side execution of either evaluator.
**Authority:** Development comparison freeze only. No D-1 result is observed here.

## 1. Frozen inputs

The comparison consumes the already-frozen D-1 artifacts:

    accepted_j1.json
        cffbeffc45e0adeda0adbb6b240b4b9968f461f3af4ce3f89af716776742ebe4

    source_facts.json
        3b5ceaa50765297c34d8d1cfa2f6230ba1d3263f457aa3f6f71dd51f39b6ded3

    definitions.json
        b1852c008fe9f61026cc44b24e5f936c8ec22d129989cb09019ae004805d98ac

    evaluator_contract.json
        01acbd0a3d4e9f497cf27bba6472a4265e1fe585aa9ca04122da8a38efa5cccf

    evaluator_key.json
        f555dbc603294f3a618a38cb2f6c1f5e11f0cd6f2406c688e620888028cc23a8

    evaluator_chatgpt_a.py
        082e1dce1a1af5504ae51b95e640878c61f4484d2065043e8e80b4470f9e46fd

    evaluator_claude_b.py
        d6899286ac281b4e26097accfca39e79acdd8253f6f9ab2d3f6f757be05ac463.

## 2. Frozen comparison

The runner executes exactly once:

    ChatGPT Evaluator A
    Claude Evaluator B

against:

    accepted_j1.json
    source_facts.json.

It compares:

    A to frozen key
    B to frozen key
    A to B

over every required material output field.

It also checks:

    exact whole-object equality
    required output field order
    lexical current_effect_ids ordering.

No field is diagnostic-only in D-1.

## 3. Outcome

Raw comparison outcome is:

    D1_INTEGRATED_MICROREPLAY_PLAUSIBLE

only if:

    A == key exactly
    B == key exactly
    A == B exactly
    output field order matches the frozen contract
    current-effect ordering is valid
    there are zero material field differences.

Otherwise:

    D1_MISMATCH_REQUIRES_RECONCILIATION.

Any mismatch must be preserved and reconciled under Research 490 as D1_AMEND or D1_REDESIGN_REQUIRED.

No post-result normalization, field dropping, evaluator editing, or hidden-key editing is permitted.

## 4. Independence

Evaluator A was authored by ChatGPT before Claude B existed.

Evaluator B was authored by Claude while blind to:

    evaluator_key.json
    Evaluator A source
    Evaluator A output
    D-1 result.

Both are frozen.

## 5. Pre-execution integrity

At freeze time:

    result.json does not exist.

The runner content hash is recorded before commit.

Before execution, its committed Git-blob SHA-256 must be verified to equal:

    b3f327271024d645c22f9753e17959ffb5d8b4e63b4710d4593b2504a794e1a4.

If it differs, execution must stop for hash-basis reconciliation.

## 6. Current boundary

    EVALUATOR_A=FROZEN_UNEXECUTED
    EVALUATOR_B=FROZEN_UNEXECUTED_BY_CHATGPT
    RESULT_EXISTS=false
    EXECUTION_COUNT=0
    ALL_OUTPUT_FIELDS=MATERIAL
    HIDDEN_R2_DETAILS=SEALED

    NEXT=EXECUTE_D1_TWO_MODEL_COMPARISON_ONCE
