# Validation 357: Executed twelve-question, seven-method source-only extractive answer evidence

**Date:** 2026-11-13
**Status:** ORIGINAL_SOURCE_EIGHTY_FOUR_ANSWER_DRAFTS_ACTUALLY_GENERATED / ALL_1260_CITATIONS_VERIFIED / EXACT_RESULT_SAVED / PRECOMMIT_INTEGRITY_AND_POSTFLIGHT_PENDING
**Research:** Research 658. **Checkpoint:** 921.
**Scope:** Actual original-Git extractive answer generation, citation verification, retrospective frozen-answer excerpt coverage and no unsupported governing authority. Model-free passages only, not independently judged complete LLM answers.

## Actual method freeze and original execution

The contract `ROUTE_B_PRIMARY_EXTRACTIVE_ANSWER_EVIDENCE_CONTRACT_V01.md` was exclusive-created **before the executable and first result**. Its seven arm rankings, original Git source and query SHA freezes, top-three source reading budget, 12,000-character source prefix, maximum five selected quote lines per source, first 35 unfenced eligible source line scan and token/field score are fixed.

The generator reads only source carrier bytes and the original question/ranking paths. A separate second phase loads the exact frozen 12-question reference manifest **after** all drafts and original citations have been verified. This is a **dataflow discipline in one exposed model-runner process**, not cryptographic blindness, separate reviewer, full factual answer adjudication or permission to score original Research513.

The first execution succeeded and exclusively saved:

    RESULT=experiments/r0_p03_navigation_probe/route_b_extractively_cited_answer_evidence_result_v01.json
    EXACT_BYTES=995317
    SHA256=17f5bae16a96530008ea954e7145e3903e25386d83eeee7e69b983de91b908f8
    QUESTIONS=12
    FROZEN_COMPARATIVE_METHODS=7
    CANDIDATE_SOURCE_TOP_K=3
    EXTRACTIVE_DRAFTS=84
    DISTINCT_SOURCE_RECORD_READS_WITH_MULTIPLICITY=252
    CITE_ORIGINAL_LINE_VALIDATIONS=1260
    DRAFT_TEXT_CHARACTERS=251190
    SOURCE_GIT_PIN=47ed6344a9153dcf366769e95722840fbf1a8f8b
    ORIGINAL_CONTEXT_CHARACTER_BUDGET_PER_SOURCE=12000
    EVALUATOR_SOURCE_GOLD_IN_RENDERER=false
    INDEPENDENT_SEMANTIC_ANSWER_TRUTH_SCORE=NONE

Each of the 1,260 quoted original lines was rechecked against a Git-archive source byte digest, line position, exact full original line and SHA-256. All source-scoped quotes carry direct path@SHA attribution. Every rendered output includes a historical/nonoperative qualifier. The 20 heldouts never entered answer generation.

### Observed evidence-completeness counts

| Method | Reference original source consumed top 3 | Every required source excerpt quoted |
| --- | ---: | ---: |
| B0 original | 10 | **9** |
| B1 exposed subject+B0 | 11 | **10** |
| B2 original link+B0 | 10 | **9** |
| B3 exposed concern+B0 | 9 | **8** |
| B4 classical LSA only | 7 | **7** |
| B4 classical LSA+B0 | 9 | **9** |
| B4 classical LSA+B2 | 9 | **9** |

P01 is an actual B1 evidence recovery despite B0 not retrieving the original current-state record. P02 is an actual quote-selection failure despite B0 retrieving the correct original decision register as rank one: a full answer needs both register identity and decision-revision support. P03 is absent from B0 top three but recovered by B3. These are full original outputs; no results were edited or post-result tuned.

## Regression and integrity controls

The first candidate test module had a local test-file syntax error and then three incorrect test assumptions (a source-prefix length off-by-one, a precise disclaimer phrase and an output attribute name). Each was repaired in **the test module only**, without changing the frozen contract, core executable, 84 outputs, original Git world or saved result. The final dedicated `tests/unit/test_r0_p03_route_b_extractively_cited_answer_evidence_v01.py` actually passed **12/12** (0.77s), including exact frozen source/arm hash, source prefix/fence/truncation exclusion, source-only ranker input dataflow, negative gold-context controls, all 1,260 original line verification, all twelve actual per-arm evidence grades, full 995,317-byte deterministic end-to-end rerun and explicit non-governing/no-scored-PASS boundaries.

## Actual full selected regressions and repository integrity

Each of the following test groups **actually executed**, with independent `--basetemp` and no pytest caching. The selected batches do not overlap in test cases:

| Test family | Actual result |
| --- | --- |
| New original-source extractive answer, citation, passage budget and full JSON replay | **12/12 PASS** (0.68s latest) |
| Checkpoint918 B0 twelve-task source baseline and original source exact replay | **9/9 PASS** (0.52s) |
| Checkpoint919 B1/B2/B3 distinct source metadata and original authored link comparisons | **10/10 PASS** (0.71s) |
| Checkpoint920 B4 classical LSA16 real original-model spectral/projection/source-vector replay | **10/10 PASS** (1.40s) |
| Checkpoint917 Git and GitHub CI original evidence / source witness test | **7/7 PASS** (3.43s) |
| Previous T2 V04 no-ID four-method source retrieval | **9/9 PASS** (0.51s) |
| Native Specification025/028 source-reference grammar + model collaboration identity/state | **41/41 PASS** (6.29s) |
| Previous T2 V03 two-original-Git-snapshot decisions/status scope and authority checks | **9/9 PASS** (0.30s) |
| Previous T2 V02 source-identity and unsupported governing assertion abstention | **10/10 PASS** (0.72s) |
| Protected C02 source-free aggregate identity / reviewer evidence boundary | **15/15 PASS** (0.15s) |
| Previous T2 V01 heading/status semantic negative controls | **3/3 PASS** (0.10s) |
| Previous T2 V01 120-document original-Git roster/source rebuild | **2/2 PASS** (18.93s) |
| Previous T2 V01 full 24-case result replay from original Git | **1/1 PASS** (16.58s) |
| Previous T2 V01 saved original T2 negative failures | **2/2 PASS** (0.16s) |
| **Actual selected nonoverlapping tests** | **140/140 PASS** |

Actual other repo controls:
- `scripts/check_current_routing.py`: **PASS**, checkpoint **921**, boundary `p-three-route-b-cited-answer-evidence-executed`, formal original P03 outcome `INCOMPLETE`.
- `scripts/check_knowledge_map.py`: **PASS**, Research **658**, **922** numbered checkpoints and 19 topic groups.
- `scripts/check_checkpoint_metadata.py`: **PASS**, **922/922** canonical checkpoint metadata records compliant.
- `git check-attr text` for the original exact **995,317-byte** output: **unset**, preserving byte identity on Windows.
- Original result checksum check: **PASS**, SHA-256 `17f5bae16a96530008ea954e7145e3903e25386d83eeee7e69b983de91b908f8`. The dedicated twelve-case tests independently replay the full JSON and compare all original quoted source lines.
- `git diff --check`: **PASS** with routine tracked-text LF/CRLF warnings.
- Initial full `scripts/check_repository_integrity.py` run correctly caught one document contract omission: Research658's metadata lacked an explicitly named nonempty `**Scope:**` field (although its boundary prose contained scope information). Added only the proper Scope metadata field to Research658, **without changing any original source, question, ranking, extractive runner, saved 84 drafts or results**. The immediate subsequent full identical branch integrity check returned **`PUBLIC_REPOSITORY_INTEGRITY=PASS`** with all family-aware contracts, Project Knowledge, checkpoint, Knowledge Map, model collaboration and routing components PASS.

These are **prepublication** gates. Guarded commit exact paths, remote fast-forward push, GitHub remote exact HEAD, clean working tree and committed source-result blob identity must be separately verified after execution.

## Scientific conclusion

The new renderer produces source-cited quotations and measures whether every earlier coordinator-author source excerpt survives top-three retrieval + passage selection. It cannot judge independent semantic entailment, actual accepted authority, current deployment or complete answer correctness. The observed P02 case demonstrates a real *retrieved correct source but incomplete quoted evidence* failure. The original C02 protected cohort, its answer HOLD and nine legacy scenarios remain unchanged; owner physical architecture/production migration is not selected.

## Authority and validity

An exact quote does not establish the source is true/current/accepted. The retrospective original answer draft author was exposed, and all primary tasks had one designated source, not independently adjudicated exhaustive gold. The renderer does not perform semantic entailment or status reasoning. A no-tools Claude CLI readiness attempt timed out, and no independent Claude review can be claimed. The protected original C02 case data, nine independently neutralized W5 legacy cases, heldout F1 and original Research513 formal scored level remain unchanged and unqualified. No architecture target is selected.
