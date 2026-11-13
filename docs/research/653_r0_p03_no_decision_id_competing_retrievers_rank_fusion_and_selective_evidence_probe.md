# Research 653: Real no-ID decision queries, competing retrieval mechanisms, fusion and selective evidence

**Date:** 2026-11-13
**Status:** ACTUAL_64_CASE_NO_ID_SOURCE_RETRIEVAL_EXECUTED / COMBINED_METHOD_NO_AGGREGATE_GAIN / EXPOSED_AUTHOR_LABELS_ONLY
**Scope:** Real no-ID question retrieval against two original decision-ledger Git snapshots, with matched FTS5/body, FTS5/title, sparse character-ngram retrieval, and reciprocal-rank fusion. Separate source-status interpretation from mere candidate relevance, while retaining measurable nonassertive navigation under abstention.
**Authority:** Before-result frozen Q-manifest SHA-256 `d632b334ec39e88f5fcaa2c1761e0b2f7ea2aa4d5b8126df962b092918495d05`, fixed T2 V04 contract and executable, original source Git revisions S0 `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef`, S1 `6d484dd5d35884f55a9bb15dd1adf8b1e3afc3d3`, actual exclusive-create trace SHA-256 `327278182a3ea6793ca999be9d5b6e179cdf8bbf89d37bdacdf6f6147773dc1b`.
**Checkpoint:** 916. **Validation:** 352. **Prerequisite:** Research 652 / Checkpoint 915.
**Independence:** The question author (ChatGPT/chatgpt-42) had already inspected the decision ledger and earlier results. Author-intended source pointers are NOT independent source-owner or relevance gold. The original R0-P03 Research 513/559/576 remains unscored.

## 1. What was actually executed

We did not stop at another planning artifact. **32 manually authored no-ID questions** were frozen as an exact exclusive-created manifest **before** the V04 comparison code was written or evaluated. They include 26 source-topic questions and six negative controls hypothesized to lack an answer among the numbered decisions in `docs/DECISIONS.md`. None of the question texts contains a `D-NNN` identifier. The target IDs appear in a separate `expected_id_for_evaluation_only` manifest field and are accessed by code only **after** method ranking and source-status behavior have been computed for a question.

The same 32 questions were applied without alteration to two original Git source revisions. S0 contains 35 numbered decision sections, S1 contains 36. **Q22**, intended to discuss D-036, points to a decision not yet recorded in S0; this is a source-snapshot absence, not an inference that the decision could never have existed. Six no-match questions repeated at each snapshot are **author hypotheses**, not independently exhaustive statements about repository or world facts.

The result comprises **64** question/snapshot cases, **51** source-present positive cases, and **13** source-absent/unmatched cases. The source originals, Git blob SHA-1s, exact section/Status/scope line evidence and content SHA-256s remain pinned. Everything is a transparent regression fixture: this ledger was already exposed to the method author in previous checkpoints.

## 2. Matched retrieval and actual combined method

All comparators see the same 35 or 36 source-owned original decision-section contents at the selected revision, the same raw question and identical K10 output limits:

1. **BODY_FTS5_BM25:** SQLite FTS5 `unicode61` over the entire Markdown decision section, OR of a fixed set of non-stopword query tokens and stable decision-ID tie break.
2. **TITLE_FTS5_BM25:** the same FTS5 scoring over decision heading title text only.
3. **CHARACTER_NGRAM_TFIDF:** pure Python sparse character trigram TF-IDF cosine matching against original title plus the first 600 section-text characters. This is lexical representation, **NOT a semantic embedding model**.
4. **THREE_WAY_RRF:** actual rank fusion using the top-ten lists from the first three methods, reciprocal-rank fusion with fixed parameter `60`. This genuinely combines retrieval mechanisms, but it also requires both FTS5 indexes and the additional character-ngram representation. No metadata label/gold or source target ID is used in scoring any query.

The source section semantics are then handled **separately**: a frozen selective evidence gate may return a `PROVISIONAL_SOURCE_STATUS_HYPOTHESIS` only if the RRF top-one is also rank-one for at least two underlying rankers, is in the third ranker's top three, and the source heading shares two distinct content tokens with the question. Otherwise it returns `REFERENT_NOT_SUFFICIENTLY_VERIFIED`. Either way, the RRF candidates remain available in a separate nonauthoritative list. Even a provisional output explicitly denies independent referent verification and never asserts operative governing authority.

## 3. Actual complete results

| Matched ranking | Correct target@1 / 51 | Correct target@3 / 51 | Correct target@10 / 51 | MRR@10 |
| --- | ---: | ---: | ---: | ---: |
| Whole-section FTS5 BM25 | 45 | 49 | 51 | 0.929412 |
| Heading-only FTS5 BM25 | 37 | 45 | 47 | 0.802288 |
| Sparse character trigram TF-IDF | **47** | **51** | **51** | **0.960784** |
| Three-way reciprocal-rank fusion | **47** | **51** | **51** | **0.960784** |

**The combined method does not improve aggregate retrieval scores over the single character-ngram stage on this population.** This is an important negative result. It does shift errors: the character method misses at top one on Q10 (checkpoint responsibility) and Q25 (project-relative objective), whereas the fused method misses Q24 (knowledge reconciliation) and Q25 across both revisions. Ranking methods are not interchangeable even when aggregate performance ties. Q24 and Q25 each have the intended source at rank two under RRF in both snapshots. All raw queries, per-method top-ten candidates and target ranks are persisted; none were dropped or tuned away after results.

The separate assertion gate admitted **29/64** provisional source-status hypotheses and withheld **35/64**. All 29 matched the same **exposed author's intended source pointers**. No hypothesis was admitted for the **13** absent/unmatched cases; the gate's correct admitted coverage among the 51 source-present cases was **29/51 = 56.86%**. No output asserts operative governance. This is an **author-label precision and coverage result**, not an externally validated reliability score. The gate was designed to be conservative and cannot in general authenticate query referents.

A dedicated synthetic falsification test constructs a query where all three retrieval mechanisms unanimously place an irrelevant but heading-overlapping decision first. The same gate admits a provisional Status for that wrong document. Thus its apparent 29/29 within the hand-authored regression offers **no guarantee** of accuracy on unseen questions. Agreement between multiple index representations derived from the **same source bytes** is correlated, not independent authority evidence.

## 4. Representation and maintenance costs

The combined method builds **two separate FTS5 search indexes**, a separate character-ngram index, and computes/merges three ranked lists per query. Character-index source statistics are deliberately recorded, not described as free:

| Index property | Earlier snapshot S0 | Later snapshot S1 |
| --- | ---: | ---: |
| Numbered source sections | 35 | 36 |
| Distinct character-trigram features | 2,117 | 2,149 |
| Nonzero document-trigram weights | 11,394 | 11,724 |
| Original section text bytes indexed | 50,835 | 54,975 |

These are actual original-source representation counts. They are **not** measured wall-clock latency, production memory use or human annotation effort, and a production semantic/embedding baseline remains unexecuted. RRF's lack of performance gain here is evidence against assuming all feature fusion is warranted, but it does not globally falsify combination methods.

## 5. Scientific interpretation and next decision

**Supported mechanism findings:** no-ID retrieval works to a meaningful extent on real project topics. Character similarity and body BM25 have complementary error patterns. Naive lexical retrieval cannot by itself authorize a source-specific Status or its operative authority. A selective two-channel answer can abstain on uncertain referents while retaining navigation candidates. Multiple retrieval methods can still agree on an incorrect referent, and combined methods can add engineering cost without a measured ranking gain.

**Not supported:** independent semantic query understanding, a vector/embedding model, neutral B2/B3/B4 comparison, independent source-owner adjudication, correct operative currentness, evidence that 29/29 is generalizable, or accepted target architecture. Question authoring was intentionally exposed and the same authored decisions supply evaluation pointers and source-status snippets. The two snapshots are genuine Git originals but **not new blind source material**.

The next qualified leap is not another self-generated paraphrase pass over the same 36 decisions. Instead freeze a **prospective, independently originated** source/question/answer packet, with task creation blind to comparator scores and genuine source-owner/lifecycle/activation evidence. A reviewer who knows previous R0 designs can still provide adversarial critique, but does not automatically become a blind author. Only then compare sufficiently capable lexical, metadata, semantic embedding and fusion methods with matched source and cost budgets, scoring wrong-source assertions, false governing authority, temporal scope, candidate utility and maintenance burden. If embeddings are unavailable locally, qualify acquisition/compute cost before claiming any B4 result.

This report makes no owner decision about changing files/folders, databases, CI/CD, branch practices, work processes, or the physical knowledge architecture; all levels remain revisable based on evidence.

    MANIFEST=experiments/r0_p03_navigation_probe/EXPLORATORY_T2_NO_ID_MANUAL_QUESTION_MANIFEST_V01.json
    MANIFEST_SHA256=d632b334ec39e88f5fcaa2c1761e0b2f7ea2aa4d5b8126df962b092918495d05
    CONTRACT=experiments/r0_p03_navigation_probe/EXPLORATORY_T2_NO_ID_RETRIEVAL_AND_SELECTIVE_EVIDENCE_CONTRACT_V04.md
    RUNNER=experiments/r0_p03_navigation_probe/exploratory_t2_no_id_retrieval_and_selective_evidence_v04.py
    RESULT=experiments/r0_p03_navigation_probe/exploratory_t2_no_id_retrieval_and_selective_evidence_result_v04.json
    RESULT_BYTES=245742
    RESULT_SHA256=327278182a3ea6793ca999be9d5b6e179cdf8bbf89d37bdacdf6f6147773dc1b
    ORIGINAL_SOURCE_REVISIONS=S0_4b94ffe_S1_6d484dd
    POSITIVE_SOURCE_PRESENT=51
    NO_SOURCE_OR_MANUAL_NEGATIVE=13
    RRF_TOP_ONE_CORRECT=47_OF_51
    CHAR_NGRAM_TOP_ONE_CORRECT=47_OF_51
    PROVISIONAL_SOURCE_STATUS_ADMITTED=29
    PROVISIONAL_SOURCE_STATUS_AUTHOR_MATCH=29
    INDEPENDENT_GOLD=false
    EMBEDDING_RETRIEVAL_RUN=false
    FORMAL_R0_P03_SCORING=NONE
