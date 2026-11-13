# Research 650: T2 actual new-source owner-status retrieval and evidence-guard pilot

**Date:** 2026-11-13
**Status:** ACTUAL_24_QUESTION_120_NEW_SOURCE_T2_V01_EXECUTED / TWO_REAL_TOP1_FAILURES_PRESERVED / FORMAL_R0_P03_UNSCORED
**Scope:** Directly execute a bounded part of Claude Message 064's proposed T2 governing-currentness and false-authority investigation over a source population outside the previously exposed 65 historical navigation documents, using actual archived Git bytes and source-status provenance.
**Authority:** Exact fixed prospective exploratory contract, fixed Git `e8ae867392f818f43dc8b76984f164e277d5cc87`, executable T2 V01 code, exclusive-create complete result JSON, directly executed full-source replay tests. Research 513/559/576 remain formally unscored. Checkpoint 913 / Validation 349.
**Interaction:** chatgpt-42; exposed task author and implementation coordinator, NOT independent question author or scorer.

## Executive experimental finding

**We ran an actual new-source T2 investigation, not another preparation exercise.** The frozen 120-source archive yields 24 title-derived status questions, 8 in each of three explicit source-header categories. SQLite FTS5 over exactly these 120 new documents returns the correct target in the top position for **22/24**, within five for **24/24**, and gives **MRR@10 = 0.9513888889**. The source-Status-only guarded interpretation is exact-target-and-status correct for **22/24** at rank one. It never asserts real operative governance, and does not misstate owner acceptance for a nonaccepted target under this limited status key. Both rank-one errors remain recorded unchanged.

**This does NOT establish live governing currentness or an architecture-choice advantage.** The question content derives mechanically from each document's own title, and the reference status comes from the **same first-100-lines header grammar** that the guarded arm reads. The only independent evidence is that actual source bytes and machine execution/reproducibility agree. These are source-grammar behavior checks, not independent user/gold adjudication, and none can be entered into Research 513's official B0–B4 score.

## 1. Why this experiment was chosen

Claude Message 064 found that the previous 65-document path graph omitted typed declared references and that a missing link must not imply a missing real relationship. Research 649/Checkpoint 912 repaired the parser basis and recommended a new-source T2 currentness/false-authority question.

The broad T2 question "what currently governs X?" cannot be answered from an arbitrary Markdown `Status` header. The corpus contains many historical statuses that describe only experiments, earlier decisions, paused workstreams or superseded *sections* rather than whole-source operative authority. Using `HISTORICAL`, `FROZEN` or `ACCEPTED` as unconditional currentness truth would produce invalid gold. We therefore narrowed **this first executable step** to a real, measurable question: *What owner-decision status does this particular document's own `Status` metadata record, and will candidate retrieval be kept non-assertive?*

This explicitly deliberately weakens the first run's construct relative to full T2. It is a safety/retrieval pilot and a way to obtain real behavior now, not a hidden replacement for the full preregistered T2 or original R0-P03.

## 2. Exact source world, source-independent selection rule and query procedure

The input is a single `git archive --format=tar` over `docs/research`, `docs/checkpoints`, `docs/specifications` from exact public commit `e8ae867392f818f43dc8b76984f164e277d5cc87`. The archive contains **1,680 Markdown files**. Every one of the old 65 historical source paths used in Checkpoints 905–912 is excluded from source selection and distractor selection. No private C01/C02 corpus/capsule is read.

Using the repository's actual `scripts.repository_integrity.read_header_fields` in isolated scratch on the Git original source bytes, assign at most one class from its `Status` field:
- **OWNER_ACCEPTANCE_RECORDED:** bounded source header says `OWNER ACCEPTED` or `OWNER-ACCEPTED`; it says that approval was recorded, *not* that the document currently governs.
- **OWNER_DECISION_REQUIRED_RECORDED:** bounded `OWNER DECISION REQUIRED`. It wins over other candidate language.
- **CANDIDATE_RECORDED:** bounded `CANDIDATE`, without `ACCEPTED` or an owner-decision marker; this is deliberately broad, and candidate-qualified is not accepted.

Candidate class populations after historical exclusions and title eligibility: **10**, **15**, **84**, respectively. The pre-output method specified a fixed SHA-256 per-class path sort with seed `T2-V01-NOV13-STATUS-FIXED` and took eight per class. A second fixed SHA-256 sort with `T2-V01-DISTRACTOR-FIXED` chose **96 distinct other source files**. The common test world has **120 documents**, 24 target sources and 96 distractors, with exact per-file Git bytes/SHA-256 and aggregate digest `a547e798677f424660592c9cf428af159fb3d4af47db98e5ed92c3d3bb5e5ef4`.

Each target provides one query template using its original first H1 after removing several owner/status category trigger words. The fixed query asks whether the topic has been owner-accepted, needs a decision or remains a candidate, and requests cited status evidence with separate useful documents. These are **not independent natural-language paraphrases**. No hidden target ID or expected source path is passed to the lexical ranker. All source selection and all 24 question strings are constructed *before* candidate retrieval.

## 3. Actual compared behaviors

All variants have access to the same 120 exact original body texts and the same source question. Shared retrieval is SQLite FTS5 Unicode61/BM25, literal OR query from the topic, stable path-tie ordering and at most ten returned documents.

| Actual execution variant | Assertion behavior | Candidate behavior | Claim scope |
| --- | --- | --- | --- |
| Lexical-only | No owner-status assertion | Top-ten FTS documents | Candidate discovery only |
| Body-keyword heuristic | Priority-matched `OWNER DECISION REQUIRED`, `OWNER ACCEPTED`, `CANDIDATE` anywhere in top document body | Top-ten FTS documents | Explicitly weak diagnostic, not governed |
| Native governed-header assertion | Parses `Status` of top lexical source using incumbent parser; emits source/line citation or open-world abstention | No separate assertion support from unrelated lexical documents | Source-header self-description only |
| Two-channel guarded answer | Same evidence-gated assertion with `NOT_FOUND_IN_COVERED_SCOPE` where no supported header value exists | **Always** retains separate non-authoritative top-ten FTS candidates | Source header evidence and candidate navigation are not fused |

The last two methods share the same assertion rule and therefore have **no distinct retrieval ranking performance**. Their distinct behavior is the answer contract: candidate suggestions remain available without becoming asserted governing facts. No candidate can be silently promoted to real governance. No supervised/embedding model was run; no B4 or B3 proxy claim is made.

A prediction counts correct only when the top-ranked document is the **exact expected original source** and its read status is the matching bounded source-header category. A fact about a *different* document, even if accurately cited, is **not** a correct answer to the user's intended target. This prevents source accuracy from being confused with answer relevance. None of these metrics verifies real-life owner action/currentness.

## 4. Observed results, including failed cases

| Actual measure | Observed result |
| --- | ---: |
| New Git-pinned source documents | 120 |
| Questions, class-balanced | 24 = 8 + 8 + 8 |
| Correct document at rank one | **22/24** |
| Correct document within ranks 1–5 | **24/24** |
| Correct document within ranks 1–10 | **24/24** |
| MRR@10 | **0.951389** |
| Correct top source AND header status | **22/24** |
| Correct top source AND naive body-keyword status | **22/24** |
| Naive body keyword disagreed with top source's native header | **1** |
| Top document other than intended target but asserted a source status | **1** |
| False owner-acceptance claims for a nonaccepted target, relative to the three class labels | **0** for both keyword and native header |
| Guarded assertions claiming operative governing authority | **0**, by design |
| Cases retaining nonassertive lexical candidates separately | **24/24**, by design |

The two **unrepaired** top-position failures:
- **T2-08, owner acceptance:** target `docs/research/PROJECT_KNOWLEDGE_ARCHITECTURE_REQUIREMENTS_V02.md` was ranked **third**. First ranked source was `docs/research/140_real_ads_relationship_corpus_v01_machine_freeze.md` with no recognized native status in the three categories. The guarded assertion correctly abstained, while the naive whole-body keyword parser hallucinated a `CANDIDATE_RECORDED` classification from non-header content.
- **T2-24, candidate:** target `docs/research/476_integrated_thin_centred_hybrid_successor_candidate_v01.md` was ranked **second**. The first-ranked different candidate document, `docs/checkpoints/812_integrated_thin_centred_hybrid_candidate_frozen.md`, does have a source-owned candidate Status. So the guarded policy correctly cited the **wrong source's own status**, but **did not answer the correct target**. This is an important counterexample: *verifiably sourced* is not equivalent to *subject-correct*. The future assertion channel must bind the question's referent to the correct source identity independently of a high lexical score.

None of the raw negative results was removed, replaced or tuned away. Both cases and all returned candidate paths are persisted in the complete 24-case trace.

## 5. Interpretation and what this falsifies

**Supported**: A separate relation/status assertion channel with explicit evidence and an independent candidate list is implementable. Source-body keyword heuristics can conflict with source-header metadata in actual data. Pure lexical title/subject retrieval can miss top-one source selection even when the target is in top five. Governing source parsing needs a referent-binding check; a correct fact attached to the wrong carrier does not satisfy the query.

**Not supported**: Present-day governance correctness, genuine B2 natural-owner metadata, B3 concern navigation, B4 semantic paraphrase value, operator-independent question wording, zero real-world false authority, B0–B4 physical-target choice or neutral metadata cost/recall comparison. A safety contract that structurally never asserts operative governance cannot count zero false-governance outputs as a semantic generalization score. The record of owner acceptance may be historical, scope-limited, or superseded by later decisions.

The pilot has no intended effective blinding: selection criteria and questions are deterministic and visible. Status reference labels are sourced from the same Status grammar used by the guarded method. Further 65/120 source-relative experiments should be counted as exposed regression unless a new independent question/answer origin and an arm-neutral source-authority gold method are provided.

## 6. Next scientifically discriminating direction

1. Retain and regression-test both T2-08/T2-24 failures. For the next T2 slice establish an explicit subject/identity binding gate before asserting source-specific status and treat a candidate's own cited status separately from a response about the user's target.
2. Source new *currentness* tasks from actual accepted decision/authority records and explicit lifecycle transitions, not a general `Status` keyword heuristic. Require time/scope and provenance evidence; unknown/not-adjudicated must be a legitimate class.
3. Ask a fresh, unexposed author to phrase natural user questions from neutral topic fact cards **after** the exact task population and comparator policies are fixed. Include non-current distractors and open-owner-decision cases, with retrieval-first and governed-metadata cases on the same source world and budgets. Only then can false-authority outcomes discriminate representation designs. The original R0-P03 twelve-primary and independent neutralized nine-legacy Research 513/559/576 protocol remains a separate, incomplete experiment.

    CONTRACT=experiments/r0_p03_navigation_probe/EXPLORATORY_T2_OWNER_STATUS_GUARDED_RETRIEVAL_CONTRACT_V01.md
    EXECUTABLE=experiments/r0_p03_navigation_probe/exploratory_t2_owner_status_guarded_retrieval_v01.py
    RESULT=experiments/r0_p03_navigation_probe/exploratory_t2_owner_status_guarded_retrieval_result_v01.json
    EXACT_RESULT_BYTES=224009
    EXACT_RESULT_SHA256=b56b2f173cb69f34e5d6a009421ce738fab5640c47b615796a51a3005b77e843
    ACTUAL_NEW_SOURCE_WORLD=120
    TITLE_DERIVED_QUERY_CASES=24
    CORRECT_SOURCE_AT_1=22
    CORRECT_SOURCE_AT_5=24
    STRICT_HEADER_SOURCE_AND_STATUS_CORRECT=22
    WRONG_SOURCE_ASSERTION=1
    NATIVE_GOVERNING_AUTHORITY_GOLD=NONE
    ORIGINAL_FORMAL_R0_P03_SCORE=NONE
