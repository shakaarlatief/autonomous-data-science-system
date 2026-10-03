# Research 498: D-1 comparison-runner hash-basis correction

**Date:** 2026-10-03
**Status:** RUNNER HASH BASIS CORRECTED / EXECUTION STILL UNSTARTED
**Parent:** Research 497
**Probe ID:** HYBRID_D1_REAL_EVENT_REPLAY_V01
**Frozen comparison commit:** a90302689dd4d356daa1e3d3cd6a8a981d5da844
**Scope:** Correct Research 497's pre-commit working-tree runner digest to the committed Git-blob digest before executing the D-1 comparison.
**Authority:** Development-integrity correction only. No runner source, evaluator source, fixture, key, threshold, or scoring rule is changed.

## 1. Required stop condition triggered

Research 497 explicitly required execution to stop if the committed runner Git-blob hash did not equal its recorded pre-commit content hash.

Observed:

    Research 497 pre-commit worktree SHA-256
        b3f327271024d645c22f9753e17959ffb5d8b4e63b4710d4593b2504a794e1a4

    committed Git-blob SHA-256
        24483ab0d1a6ee09428c77c21b7e517ff62f2f00e99015950a12585f49fec384

    result.json exists
        false.

The mismatch is another line-ending hash-basis difference between worktree bytes and committed Git-blob bytes.

Execution was not started.

## 2. Authoritative runner identity

For the frozen comparison at commit:

    a90302689dd4d356daa1e3d3cd6a8a981d5da844

the authoritative runner identity is:

    path
        experiments/ao10_hybrid_d1_replay_v01/run_two_model_comparison.py

    hash basis
        GIT_BLOB_BYTES_AT_COMMIT

    SHA-256
        24483ab0d1a6ee09428c77c21b7e517ff62f2f00e99015950a12585f49fec384.

No source edit is made.

## 3. Research 497 correction

Research 497 remains the comparison-harness freeze.

Its pre-commit runner digest is retained as a historical WORKTREE_BYTES observation only.

Its Section 5 execution condition is satisfied by this correction because the exact committed runner is now identified prospectively, before result observation.

## 4. Integrity

At this correction point:

    evaluator A has not been executed by ChatGPT;
    evaluator B has not been executed by ChatGPT;
    result.json is absent;
    runner source is unchanged;
    hidden key is unchanged;
    comparison logic is unchanged.

Therefore no post-result tuning has occurred.

## 5. Current boundary

    RUNNER_GIT_BLOB_SHA256=24483ab0d1a6ee09428c77c21b7e517ff62f2f00e99015950a12585f49fec384
    RESULT_EXISTS=false
    EXECUTION_COUNT=0

    NEXT=EXECUTE_D1_TWO_MODEL_COMPARISON_ONCE
