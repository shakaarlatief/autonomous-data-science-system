# Validation 354: Actual Route B twelve-primary-task B0 execution with original Git source witnesses

**Date:** 2026-11-13
**Status:** ACTUAL_B0_12_TASK_SOURCE_RETRIEVAL_EXECUTED / EXACT_RESULT_REPLAY_TESTED / FORMAL_GOLD_UNQUALIFIED
**Research:** Research 655. **Checkpoint:** 918.
**Scope:** Verify prospective source-grounded coordinator reference manifest, first bounded 60/20 original Git draw, real twelve-question B0 vs diagnostic retrieval results, exact source witness positions, reproducibility and repository contracts.

## Actual execution

The source-answer manifest was exclusive-created *before* the baseline implementation:

    MANIFEST=experiments/r0_p03_navigation_probe/ROUTE_B_PRIMARY_12_SOURCE_ANSWER_MANIFEST_V01.json
    MANIFEST_BYTES=9784
    MANIFEST_SHA256=c628555ef02f87499007ead3420a513cf43080262c7288cd347dc2479b4b0330

It contains twelve complete coordinator-authored question/answer pairs, three per Research 513 family, with one explicitly required original source and verbatim source excerpts. All original citations were validated directly from public Git at `47ed6344a9153dcf366769e95722840fbf1a8f8b`; preserved complete original source line, line index, SHA-256 and original source byte digest.

The pre-result execution first stopped due to an omission of the two root documents from the source-path eligibility family. It stopped a second time because a valid source quotation was a subsection of a longer original Markdown line. Both failures were openly reconciled in the method contract/code **before any result file existed**, without changing original question/answer/anchor manifest bytes.

On the third attempt, the method produced the complete exclusive-create output:

    RESULT=experiments/r0_p03_navigation_probe/route_b_primary_b0_baseline_result_v01.json
    RESULT_BYTES=122682
    RESULT_SHA256=59ab36aef96046f71e2ccacbcc2105918ab19ed4bbc1f013e9bb78539a9bd4ab
    BUILD_DOCUMENTS=60
    HELDOUT_DOCUMENTS=20
    SOURCE_WORLD_ELIGIBLE_PATHS=1659
    ORIGINAL_GIT_REVISION=47ed6344a9153dcf366769e95722840fbf1a8f8b
    REQUIRED_ORIGINAL_SOURCE_CLOSURE=12
    B0_REQUIRED_SOURCE_HIT_AT_1=8
    B0_REQUIRED_SOURCE_HIT_AT_10=11
    B0_REFERENCE_SOURCE_MISS=P01
    TITLE_DIAGNOSTIC_HIT_AT_1=10
    TITLE_DIAGNOSTIC_REFERENCE_MISS=P02
    CHARACTER_TRIGRAM_DIAGNOSTIC_HIT_AT_1=12
    RRF_DIAGNOSTIC_HIT_AT_1=12
    FORMAL_R0_P03_SCORING=NONE

This trace preserves complete original source roster/digests, question/answer witness positions, returned candidate paths per query, exact source rank, index statistics and explicit non-independence flags. A source reference is never promoted into verified real-world operative authority by this execution.

## Dedicated tests

Actual `tests/unit/test_r0_p03_route_b_primary_b0_baseline_execution_v01.py`: **9/9 PASS** (0.63s). Tests cover pinned exact 9,784-byte question/answer fixture, exact four-category distribution, 60/20 sample re-selection against historical Git, 80 actual source blob SHA-256s, each original answer witness, bitwise identical complete 122,682-byte full rerun, actual negative retrieval failures, comparator labeling and a synthetic fabricated-excerpt rejection.

## Full observed precommit verification

Every selected test below actually completed under an isolated scratch directory, with Python `-B` and pytest cache disabled:

| Test scope | Actual verdict |
| --- | ---: |
| New Route B original-Git 60/20 twelve-task B0/diagnostic execution and complete output replay | **9/9 PASS** (0.58s latest) |
| Earlier objective Git and external GitHub Actions source event/witness evidence | **7/7 PASS** (4.04s) |
| Earlier T2 V04 no-ID, four-method ranking and source-status answers | **9/9 PASS** (0.55s) |
| Native Specification 025/028 source-reference grammar V03 and model-collaboration identity/state | **41/41 PASS** (6.92s) |
| Earlier T2 V03 exact two-Git-snapshot decision scope/authority analysis | **9/9 PASS** (0.35s) |
| Earlier T2 V02 118-request original-source subject-identity regression | **10/10 PASS** (0.76s) |
| Protected C02 source-free evidence-aggregate identity and original HOLD boundary | **15/15 PASS** (0.18s) |
| Earlier T2 V01 synthetic checks | **3/3 PASS** (0.11s) |
| Earlier T2 V01 exact 120-original-source Git sample/roster reconstruction | **2/2 PASS** (17.52s) |
| Earlier T2 V01 full source result deterministic replay | **1/1 PASS** (16.39s) |
| Earlier T2 V01 saved negative controls | **2/2 PASS** (0.11s) |
| **Non-overlapping selected tests across the actual batches** | **108/108 PASS** |

Additional actual repository checks:

- `scripts/check_current_routing.py`: **PASS**, checkpoint **918**, boundary `p-three-route-b-first-primary-lexical-executed`, original formal R0-P03 outcome `INCOMPLETE`.
- `scripts/check_knowledge_map.py`: **PASS**, Research **655**, **919** numbered checkpoint records, 19 topic categories.
- `scripts/check_checkpoint_metadata.py`: **PASS**, **919/919** canonical numbered checkpoints compliant.
- `git check-attr text` on both reference manifest and result JSON: **unset**; exact original bytes cannot be altered by Git text line-endings on Windows.
- `git diff --check`: exit **0**, with only expected Windows LF/CRLF warnings on existing tracked text files.
- `scripts/check_repository_integrity.py --checked-branch v1-source-vault-bootstrap-resume`: **PUBLIC_REPOSITORY_INTEGRITY=PASS**, including repository family, Project Knowledge, checkpoint metadata, Knowledge Map, model collaboration and routing validators.

The first routing check failed because a draft boundary identifier contained the digit `0`, which violates the repository's letter-only slug grammar. Only `docs/current_routing.json` was corrected to a valid descriptive boundary; no reference case, original source, ranking method, original result or threshold was changed.

This evidence is **precommit only**. Committed Git blob hashes, published branch SHA, clean local working tree and exact remote head require separate direct postcommit verification and must not be inferred from the precommit results.

## Scientific limitations

This is a twelve-task **exposed** source-discovery and answer-evidence baseline, not an independent qualified primary gold evaluation, full fresh-agent answer correctness, nine-case neutral legacy evaluation or B0-B4 arm contest. The 60/20 candidate source frame is path-stratified rather than source-role adjudicated. B0 indexes source text only, lacking a proven complete V03-native common substrate; three diagnostics are not true B1/B2/B3/B4. No R0-P03 viability threshold, architecture choice, production migration or governing authority may be inferred.
