# Validation 341: Actual executed B0-like/B1-like fixed historical navigation retrieval pilot

**Date:** 2026-11-12
**Status:** REAL_TWO_MECHANISM_LEGACY_TEST_EXECUTED / FIXED_INPUTS_AND_REPEATABLE_OUTPUT / NO_ORIGINAL_R0_P03_SCORING
**Scope:** Preserve actual run output and execution-time limitations from a deliberately narrower real retrieval comparison. This is experimental engineering evidence, not a fixture-admission or architecture-selection result.
**Authority:** R0-P03 exploratory pilot code and fixed legacy W5-T1-V02 input fixtures; Research 642, Checkpoint 905.

## Actual execution

`python -B -m experiments.r0_p03_navigation_probe.exploratory_legacy_b0_b1_live_comparison --output`

Completed successfully against original historical Git revision `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef`, with exact 65 source documents. It returned one deterministic JSON artifact:

    FILE=experiments/r0_p03_navigation_probe/exploratory_legacy_b0_b1_live_result_v01.json
    BYTES=18712
    SHA256=498bb12d906639642da943e8366194ec8b0c7f6817d20ae5b8fa89a43f8a2acb
    SCENARIOS=9
    RETRIEVAL_LIMIT=10
    B0_LIKE_STRICT_FULL_PASSES=1
    B1_LIKE_STRICT_FULL_PASSES=9
    B0_LIKE_RELEVANT=28_OF_39
    B1_LIKE_RELEVANT=39_OF_39
    B0_LIKE_NEGATIVE_INTRUSIONS=4
    B1_LIKE_NEGATIVE_INTRUSIONS=0
    B0_LIKE_TOTAL_RETRIEVED=90
    B1_LIKE_TOTAL_RETRIEVED=51

The pilot runner uses the same exact real historical UTF-8 source bytes for both mechanisms and records content digests, per-scenario outputs and full scoring metadata in the persisted JSON. A separate subsequent read-only invocation of the same `run()` function returned the **identical full JSON structure** as the saved output, and its complete-file SHA-256 matched the original run. The nine public legacy scenario gold paths are present in the fixed 65-carrier set; this is not C01/C02 private gold.

W5-T1-V02 preexisting subject annotation author was ChatGPT; independent blind generalization is not established. The previously developed subject index fits those legacy labels by design. Only lexical versus authored-subject navigation mechanics were compared. No B2/B3/B4, real authority/answer scoring, maintenance holdout, currentness, new source release, independent evaluator or protected private artifacts were involved.

## Post-run engineering verification

Actual post-run checks completed:
- Focused executable pilot plus original C02 Phase A/B source-free boundary and prior origination regression suite: **24/24 PASS** (3.42 seconds, isolated scratch and no pytest cache).
- `scripts/check_current_routing.py`: **PASS**, Checkpoint **905**, stable boundary `p-three-exploratory-legacy-comparison-executed`.
- `scripts/check_knowledge_map.py`: **PASS**, **19** topics, latest Research **642**, **906** numbered checkpoint records (000..905).
- `scripts/check_checkpoint_metadata.py`: **PASS**, **906/906** canonical checkpoints compliant, zero warnings or errors.
- `git check-attr text` on fixed 18,712-byte result JSON: **unset**, preserving source JSON exact bytes through Git checkout.
- `git diff --check`: exited **0**, ordinary Windows text line-ending warnings on four tracked documents.
- Full public repository gate `scripts/check_repository_integrity.py --checked-branch v1-source-vault-bootstrap-resume`: **PUBLIC_REPOSITORY_INTEGRITY=PASS**, including family-aware contracts, project knowledge, checkpoint, Knowledge Map, collaboration state and routing.

These observations preceded commit and push; they are not evidence of an independent blind subject-architecture win, a valid twelve-primary experiment or a physical target decision.

    REAL_EXECUTED_PILOT=PASS
    RERUN_IDENTICAL=PASS
    ORIGINAL_R0_P03_SCORE_STATUS=INCOMPLETE
