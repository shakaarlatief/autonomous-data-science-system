# T2 V04: No decision-ID questions, matched retrieval mechanisms and selective source-status hypotheses

**Date:** 2026-11-13
**Status:** METHOD_PREDECLARED_BEFORE_V04_EXECUTION / COMPLETELY_EXPOSED_COORDINATOR_QUESTIONS / SOURCE_RECORD_ONLY / NO_INDEPENDENT_GOLD
**Purpose:** Determine which of several complementary retrieval representations actually find the correct *source-defined decision record* when a user-style question contains no `D-NNN` identifier. A separate selective evidence-handling stage tests the trade-off between abstention and mistaken referent-binding. This is not a B0-B4 qualified architecture comparison.

## Immutable question freeze and source frames

Use `EXPLORATORY_T2_NO_ID_MANUAL_QUESTION_MANIFEST_V01.json`, **8668 exact bytes**, SHA-256 `d632b334ec39e88f5fcaa2c1761e0b2f7ea2aa4d5b8126df962b092918495d05`, exclusive-created **before implementing or running any V04 method**. The author (ChatGPT) read all decision record titles, current contents, and previous R0-P03 outcomes before authoring. There are **26** manually paraphrased positive topic questions each assigned one author-intended D-NNN for evaluation only, and **six** author-hypothesized no-matching-decision controls. None of their actual question strings contains an explicit `D-NNN` identifier. Every question runs against both frozen Git original ledger snapshots: S0 `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef` (35 decisions) and S1 `6d484dd5d35884f55a9bb15dd1adf8b1e3afc3d3` (36 decisions). This forms **64** source/question/snapshot instances: 52 positive-topic instances, 12 no-target hypotheses, with one positive topic referencing D-036 that is **not recorded in S0**. No question is dropped after seeing retrieval or status results.

The reference IDs are author-attributed **intent labels**, **not independent ground truth** or semantic proof that another decision cannot also answer. A no-match control is a hypothesis about the bounded source ledger, not a universal proof of absence or any real-world operational truth. Only the source's own recorded status can be cited; a historical `Accepted` status never proves live authority. Original decisions and source snapshots overlap previously exposed tests; these results are regression only.

## Common corpus and equal data access

Use original `parse_sections`, `original_git_blob` from the Checkpoint 915 T2 V03 runner, and insist all section witnesses and exact S0/S1 revision hashes agree. Each comparator is built from the same **section-level 35 or 36 records**. Each is queried with the **same raw question**. The evaluator-only intended ID and intent family never flow into any scoring, ranking, lookup or selective assertion function. There is no hidden exact-ID fallback.

We compare **four actual mechanism families**, each evaluated at K=1,3,5,10:
1. **BODY_FTS5_BM25:** SQLite FTS5 unicode61 over complete original decision section Markdown, OR query from unique normalized question content tokens, with a fixed stopword list and stable ID tie-break.
2. **TITLE_FTS5_BM25:** same SQLite FTS5 over the source-authored decision heading title only, same query normalization and tie-breaking.
3. **CHARACTER_NGRAM_TFIDF:** ordinary pure Python sparse character 3-gram TF-IDF with cosine ranking on title plus at most first 600 characters of the section body (no embedding model or trained semantic reasoning), smoothing IDF `1 + log((N+1)/(df+1))`, stable tie-break.
4. **THREE_WAY_RRF:** simple reciprocal-rank fusion of the **top-ten** rankings above using `score = sum(1/(60+rank))`, tie-break by source ID. No manual selected-document lookup or query-specific method weights. This is a real combined method, not a fair physical B0-B4 arm. It adds maintenance/index and query complexity.

All four rankers share source snapshots and a fixed K10 retrieval budget. Character ngrams and RRF may produce low-score suggestions even when lexical queries have no matches; do not treat presence in an output as proven source relevance. Save all top-ten paths and rank metrics, with the exact method specifications and operations/feature counts; Python standard library and SQLite FTS5 suffice. No local `sentence-transformers`, numpy or sklearn embedding model is installed. **Do not call the ngram stage a semantic embedding model.**

## Separate selective evidence gate

Take *only the RRF top-one suggested section*, not the evaluator's intended D-NNN. A source-status **hypothesis**, explicitly not a confirmed answer, may be returned only if ALL fixed gates pass:
- the same RRF top-one document is rank-one for at least two of BODY_BM25, TITLE_BM25, CHARACTER_NGRAM_TFIDF;
- the remaining method ranks that candidate within its top three;
- the source's actual title overlaps at least two unique query content tokens, with case/punctuation normalized and no synonyms or runtime learned thresholds;
- the exact original Git section/Status source witnesses exist.

If any gate fails, return `REFERENT_NOT_SUFFICIENTLY_VERIFIED`. If all pass, return `PROVISIONAL_SOURCE_STATUS_HYPOTHESIS` with cited source identity, original Git revision/blob hash, source recorded Status and supersession scope. **Never assert operative governance**, including for `Accepted`; the source pointer itself may be wrong. Always return the RRF top ten separately as `NONAUTHORITATIVE_CANDIDATES`, even on abstention.

Count source-specific hypothesis precision against the author-intended source ID only as `author-labelled precision`, track incorrect source-status hypotheses for both positive and no-target question families, and report abstention/coverage. Do not relabel an incorrect source-specific hypothesis as correct merely because some other document might also be related. Do not silently treat absent at snapshot as `NEVER_EXISTED`.

## Evaluation and stopping

For each 64-case item persist query, question class, snapshot, expected target for **evaluation only**, whether that target appears in the original snapshot, every method top-ten IDs, rank@1/3/5/10, reciprocal rank and actual source Status witness for admitted provisional source. Score per-snapshot and per-family, including Q22/D-036 S0 missing-source controls and six no-target questions in both snapshots. Record candidate-count and character-ngram feature/corpus size estimates and distinguish additional query computation from metadata authoring cost (no new human annotations were required for the methods).

No tuning after seeing performance, no cherry-picked queries, no dropping cases and no changing source classifications. If the runner fails before first result, record the failure and any minimal correction. Saved result is exclusive-create, exact bytes preserved via `.gitattributes -text`, verified by rerun and unit tests. Any future independent questions require an external author who has not seen these questions, output scores or retrieval methods. This experimental packet must not be used as such independent gold.

The formal Research 513/559/576 R0-P03 trial remains INCOMPLETE; neither B3 concern vocabulary nor an embedding B4 arm has been fairly evaluated. Do not select a physical knowledge architecture or change the authority of Specification 028 based on this source-derived result.

    SOURCE_S0=4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef
    SOURCE_S1=6d484dd5d35884f55a9bb15dd1adf8b1e3afc3d3
    QUESTIONS_POSITIVE=26
    QUESTIONS_NO_TARGET_HYPOTHESES=6
    SNAPSHOTS=2
    CASES=64
    RANKING_TOP_K=10
    FUSION_RRF_K=60
    QUERY_GOLD_INDEPENDENT=false
    SOURCE_STATUS_IS_OPERATIVE_TRUTH=false
    ORIGINAL_R0_P03_SCORING=NONE
    OUTPUT=EXCLUSIVE_CREATE_NEW_RESULT
