# Validation 358: Executed GPT-6 exposed model reasoning over original B0/B1 top-three source excerpts

**Date:** 2026-11-13
**Status:** GPT6_MODEL_AUTHORED_TWENTY_FOUR_PAIRS_FROZEN / EXACT_SOURCE_PACKET_AND_CITATIONS_VERIFIED / FORMAL_REFERENCE_NOT_QUALIFIED
**Research:** Research 659. **Checkpoint:** 922.
**Scope:** Record the actual source-visible GPT-6 answer authoring, original source evidence, test results and the absence of blind model-level independence or semantic gold.

## First immutable original outputs

Source-visible context exporter created before answer generation:

    PATH=experiments/r0_p03_navigation_probe/route_b_reasoned_b0_b1_gold_free_source_packet_v01.json
    ORIGINAL_SIZE=155794
    SHA256=60ec37969aa3319ce195353a6f9cddb2103640b0e4f748564e0be4a4d839b508
    SOURCE_PARENT=route_b_extractively_cited_answer_evidence_result_v01.json
    ORIGINAL_PARENT_SIZE=995317
    ORIGINAL_PARENT_SHA256=17f5bae16a96530008ea954e7145e3903e25386d83eeee7e69b983de91b908f8
    SOURCE_GIT_PIN=47ed6344a9153dcf366769e95722840fbf1a8f8b
    CASES=12
    METHOD_INPUTS=B0_ORIGINAL;B1_EXPOSED_SUBJECT_B0
    GOLD_FIELDS_IN_EXPORTED_MODEL_PACKET=NONE
    MODEL_HAS_HISTORICAL_REFERENCE_EXPOSURE=true

The same exposed GPT-6 coordinator authored **24** original prose responses from that question/line scope and saved them exclusively. These were actual model-authored language outputs, not generated from a deterministic quote template:

    PATH=experiments/r0_p03_navigation_probe/route_b_reasoned_b0_b1_gpt6_exposed_answers_v01.json
    ORIGINAL_SIZE=56283
    SHA256=5e8848f444fee4234fe885d9350e872393ac20f24a043c2347e615dafccdc388
    EVIDENCED_CLAIMS=47
    CITATION_ENTRIES=78
    DISTINCT_ORIGINAL_GIT_SOURCE_BLOBS_CITED=12
    DISTINCT_ORIGINAL_LINE_POSITIONS_CITED=41
    TOTAL_MODEL_AUTHORED_ANSWER_CHARACTERS=7777
    HUMAN_OR_INDEPENDENT_GOLD=NOT_OBTAINED

Prose self-assessment: B0 9 supported/1 partial/2 abstain; B1 10 supported/2 partial/0 abstain. These are **model self-reports**, *not* verified full-answer correctness or a pass under Research513's formal threshold. P01, P02, P03 and P10 cite explicit original source/line evidence and preserve uncertainty. No external model tool was newly run to independently evaluate the claims.

## Initial actual dedicated test execution

`tests/unit/test_r0_p03_route_b_exposed_gpt6_reasoned_b0_b1_answers_v01.py`: **11/11 PASS** (0.29s). These tests verify original 155794-byte packet and 56283-byte answer file hashes, direct packet reproducibility, absence of evaluator gold in actual question/line payload, 12 × two-arm source/response identity, 24 distinct non-templated prose responses, correct original pinned Git source SHA and exact original line SHA for all 78 citations, no citation outside an arm's top-three lines, P01 proper abstention/recovery, P02 and P03 missing-context caveats, P09/P10 authority/temporal separation, and explicit non-independent non-scored status.

The source context packet can be reexported bit-identically, but the GPT-6 original prose was written by the exposed language model in this conversation. Its exact model generation cannot be independently reexecuted through the Python original-source validator. The file's integrity and cited source lines are replayable; the *truth of its inferred statements* remains unqualified.

## Observed selected regressions and full repository integrity

All test batches were executed with isolated pytest scratch directories, Python `-B` and disabled pytest cache. The test groups are nonoverlapping.

| Actual test scope | Result |
| --- | ---: |
| New source-reasoned GPT-6 B0/B1 original line-citation validation | **11/11 PASS** (0.22s) |
| Prior 84 extractive answer drafts, exact original-source quote replay | **12/12 PASS** (0.64s) |
| Original B0 frozen 12-question source retrieval/result | **9/9 PASS** (0.51s) |
| Original B1/B2/B3 subject/link/concern experimental retrieval | **10/10 PASS** (0.67s) |
| Original B4 corpus-trained LSA16 spectral/embeddings/negative result | **10/10 PASS** (1.43s) |
| Git event and GitHub CI source witness | **7/7 PASS** (3.43s) |
| T2 V04 no-ID retrieval/status comparison | **9/9 PASS** (0.53s) |
| Specification025/028 native source grammar and model-collaboration identity/state | **41/41 PASS** (5.71s) |
| T2 V03 two original-Git decision snapshots | **9/9 PASS** (0.28s) |
| T2 V02 source identity/unsupported authority abstention | **10/10 PASS** (0.67s) |
| Protected C02 independent evidence and HOLD aggregate identity | **15/15 PASS** (0.14s) |
| Earlier T2 V01 three synthetic negative controls | **3/3 PASS** (0.10s) |
| Earlier T2 V01 two original 120-source sample/roster tests | **2/2 PASS** (15.01s) |
| Earlier T2 V01 full Git-source result replay | **1/1 PASS** (14.59s) |
| Earlier T2 V01 two saved actual negative cases | **2/2 PASS** (0.11s) |
| **Total nonoverlapping observed selected tests** | **151/151 PASS** |

Additional original repository validation:
- `scripts/check_current_routing.py`: **PASS**, current checkpoint **922**, original R0-P03 outcome **INCOMPLETE**, boundary `p-three-route-b-exposed-reasoned-answers-executed`.
- `scripts/check_knowledge_map.py`: **PASS**, Research **659**, **923** numbered checkpoint records, 19 topic groups.
- `scripts/check_checkpoint_metadata.py`: **PASS**, **923/923** numbered checkpoints compliant.
- `git check-attr text`: both new immutable source-only packet and model-authored original result are **unset** for text line-ending normalization on Windows.
- `git diff --check`: exit **0**, with routine Git LF/CRLF warnings on other tracked text only.
- Exact source packet and saved model answer hashes: **PASS**, original **155,794 bytes** SHA-256 `60ec37969aa3319ce195353a6f9cddb2103640b0e4f748564e0be4a4d839b508` and original **56,283 bytes** SHA-256 `5e8848f444fee4234fe885d9350e872393ac20f24a043c2347e615dafccdc388`.
- Full `scripts/check_repository_integrity.py --checked-branch v1-source-vault-bootstrap-resume`: **PUBLIC_REPOSITORY_INTEGRITY=PASS**, family-aware repository contracts, project knowledge, checkpoint metadata, Knowledge Map, model collaboration and routing all PASS.

These are **precommit** observations. The eventual published Git commit, remote branch head, clean working tree and committed original source/answer bytes require separate verification. The model's prose is not reproducible from a deterministic Python runner; only its immutable saved text and source citations are independently verifiable. Source authenticity does **not** mechanically establish semantic entailment.

## Formal science limit

The present model had prior source and reference-answer exposure, even though the explicitly exported packet omitted gold. This experiment only adds model-authored prose grounded on originally retrieved source quotes; no independent reference adjudication, complete B0–B4 prose comparison, actual source-owner B1 metadata, score-ready nine-case historical legacy packet, heldout F1, complete V03-native substrate or genuine fresh-model double evaluation was obtained. No status of protected C02 evidence, current owner-selected physical architecture or operational migration changed.
