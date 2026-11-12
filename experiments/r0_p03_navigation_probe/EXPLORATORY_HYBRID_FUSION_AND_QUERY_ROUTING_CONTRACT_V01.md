# Exploratory hybrid retrieval, ablation, and query-routing experiment V01

**Date:** 2026-11-12
**Status:** FIXED_PRE_RESULT_HYBRID_METHOD / REAL_SOURCE_RETRIEVAL_ONLY / FORMAL_R0_P03_UNSCORED
**Parent:** Exact executed Checkpoints 905-907 and original Research 513/559/576.
**Purpose:** Actually execute combined navigation methods instead of arguing about architectural combinations in the abstract. Any observed result is an exploratory engineering result, not a newly blind or fully equalized Research 513 B0-B4 selection.

## Frozen input world and questions

The **same 65 real historical source documents** at Git revision `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef`, with the previously published W5 T1 V02 catalog and authored membership annotation, will be read from exact Git objects. No worktree/current-knowledge document is eligible.

Evaluate **two separate, never-pooled query families**:

1. **Nine old subject-oriented navigation queries:** the literal human-readable subject label strings from the existing nine V02 scenarios. Use the original source-target positives and explicitly labeled distractors as a *historical B1-authored, nonneutral, nonblind* evaluation after ranking.
2. **All 65 source-heading document-location queries:** the exact first top-level Markdown heading from every document, with its originating file as a mechanical exact-target label. This is a *source-contained lexical-favoring* query family, not an independent user or source-authority question.

Query text, old source labels and the historical corpus are unchanged. Do not reuse the previously scored nine-scenario B1 *subject ID* as a ranker input: B1 must infer the subject solely from the same visible query string for **both** families. Any B1 route failure must remain a reported failure, never be repaired using the reference label.

## Three common single-mechanism candidates

**B0 lexical:** exact full-text SQLite FTS5 `unicode61` with the preexisting stopword/literal-term OR query and stable BM25 ranking; return at most top ten.

**B1 inferred-subject:** use the existing first-heading experiment's fixed `infer_subject` classifier (catalog label/description token intersections, deterministic thresholds and ties). Where a topic is inferred, rank all annotated matching members by preferred-subject first, shared BM25 rank, stable path, filling to ten from lexical BM25; otherwise use B0 top ten. Authored B1 memberships and their sunk construction cost are *part of the treatment*, not cost-free.

**B2 literal-citation proxy:** preserve B0's top five seeds, one hop of exact explicit `docs/...` references among the same 65 source contents, prioritize citing-seed frequency then BM25 rank then stable path, fill remaining top-ten from B0. This does **not** equal governing/source-owned editorial carrier links (actual Research 513 B2 remains unimplemented).

For each query, compute all three unmodified top-ten ranked lists **before reference labels are read by the scoring step**, independently of their observed success.

## Frozen combinations, controls and ablations

Use **reciprocal rank fusion** (RRF) over the *ten already retrieved candidates* per included mechanism, with `RRF_K=60`, each contributing `1/(60+one_based_rank)`, zero weight for absent candidates. Sort descending fusion score, then ascending position in the B0 full lexical list, then stable path. Do **not** normalize candidate lists by prior observed gold or vary weights after seeing results.

The exact arms are:

- B0, B1, B2 as described above;
- B0+B1 RRF;
- B0+B2 RRF;
- B1+B2 RRF;
- B0+B1+B2 RRF.

**Seven arms total**, including three singles and four fusions. The three two-way fusions are direct one-component removals from the three-way fusion, and the singles document pure mechanism behavior. Every candidate list remains fixed. The fusion pool can contain up to 20 or 30 unique candidates while the *final* returned list contains at most ten. Record candidate-union size per query as a cost/effort proxy; this is not actual wall-clock latency or normalized source read cost.

A separate **query-text-only router**, evaluated alongside the seven arms:

- Normalize query with Unicode NFKC, casefold, and trimming/collapsing whitespace.
- Compare against every one of the same 65 source's *first H1 heading texts*, excluding paths/labels/gold from the routing decision; this is an explicitly available title index, which is a form of additional metadata also derivable from source text.
- If exactly equal to a unique heading, choose B0. Otherwise choose **B0+B1 RRF**, a fixed broad topical fallback. No query-family labels, scenario IDs, historical source target paths, or evaluation outcomes are accessible to this decision.
- Record selected branch and actual route count, and explicitly disclose that exact-heading matching is advantaged by one of the two evaluated families.

A router can merely reproduce a baseline if the task families separate by heading syntax; that observation must not be inflated into evidence of learned intent classification or generalization.

## Scoring and integrity

- On **nine old tasks**: positive source instances in top ten, micro/macro recall@10, explicit known distractor intrusions, strict complete-scenario passes (all positives and zero explicit negatives); actual returned slots and union pool sizes.
- On **65 title-locator tasks**: hit@1, hit@10, MRR@10, actual returned slots and union pool sizes, zero task omissions.
- Never pool these incompatible metric definitions into an overall winning score. Report per-arm and per-family outcomes independently; avoid ranking by cherry-picked primary criterion.
- Preserve per-query lists, input/source hashes, contract and method ID, interpreter/SQLite version, classifier decisions, route switches, and all outcomes in one immutable JSON result.
- Verify previous Checkpoint 905/906/907 baseline trace SHA-256, exact query text/ranks and Git source bytes. If any differs, stop rather than relabeling or revising historical results.
- Exclusive-create output; no results-dependent tuning, changing RRF K, changing title matching, changing benchmark tasks, or replacing source texts after execution. Rerun deterministically and test exact full-file byte identity.

## Interpretation and scope ceiling

This test **adds real combined methods** but is not a fresh source-independent oracle. Both task families were seen in preceding experiments. The nine original labels are B1-authored, the 65 headings contain their own target words, and source membership metadata is inherited. The router and fusion weights are specified after earlier single-mechanism outcomes and cannot be called strictly prospective blind arm selection. B2 remains a weak literal-path proxy; there is **no authentic B3 governed concerns arm or B4 embedding model** here. Equal final top-ten output budgets do not equalize fusion's up to 30 upstream candidates, metadata preparation, authority semantics, implementation effort or retrieval latency. No primary C01/C02 protected source/gold is consulted.

**No Research 513/559/576 thresholds or task count are changed. No R0-P03 scored architecture selection, false-authority qualification, physical target switch, source admission, primary gold, migration or production release is authorized by any pilot outcome.**

    FROZEN_MECHANISM_COUNT=3
    FROZEN_SINGLE_AND_FUSION_ARMS=7
    ADDITIONAL_QUERY_TEXT_ROUTER=1
    LEGACY_TASKS=9_PREVIOUSLY_SCORED
    DOCUMENT_LOCATION_TASKS=65_PREVIOUSLY_SCORED
    SOURCE_SNAPSHOT=4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef
    TOP_K=10
    RRF_K=60
    EVALUATION=EXPLORATORY_ONLY
