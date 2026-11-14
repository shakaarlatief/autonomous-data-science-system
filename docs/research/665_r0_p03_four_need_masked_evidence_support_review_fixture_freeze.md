# Research 665: Freeze masked, case-local original-excerpt claim support review for two original R0-P03 answer sets

**Date:** 2026-11-14
**Status:** MASKED_EIGHT_ANSWER_SOURCE_ONLY_REVIEW_FIXTURE_FROZEN / QUALITATIVE_SUPPORT_ASSESSMENT_PENDING / ORIGINAL_R0_P03_INCOMPLETE
**Scope:** Prepare one bounded independent-session original-evidence support assessment of eight already frozen source-limited answers, guarding the previously observed cross-question evidence boundary and preserving the difference between source support and historical operative authority.
**Authority:** Research 664; Validation 364 and Checkpoint 928; MC-0030 Messages 079/080 and 081; original historical Git horizon `47ed6344a9153dcf366769e95722840fbf1a8f8b`. The formal Research 513/559/576 gates remain unchanged.

## 1. Why this is the next justified experiment, not another source-retrieval run

Two actual source-only Claude Code authors already returned answers for independently originated N01-N04. Their self-described outcomes were A: 0 complete, 3 partial, 1 abstain; B: 0 complete, 4 partial, 0 abstain. Body BM25 and body+heading RRF diagnostic share an objective 2,258-file original Git source world and fixed evidence budgets. Their retrieval results differ, but self-descriptions are not answer truth, source-line relevance or model-independent scores.

A retrospective model-free case-boundary check found that A has 16/16 fully specified in-case source identities and B 16/17, with the one out-of-question B reference used in its N03 answer from its N04 packet context. This is a **violation of the original per-question evidence-use rule**, not demonstration that the historical fact is wrong or that the model read another *treatment*. Both original messages and both original source-only packets remain unchanged. The later attempted duplicate B author correctly held and produced no new answer.

The outstanding decision-relevant distinction is **whether the extra assertions in either answer are actually supported by its own displayed evidence**, and whether its abstentions accurately reflect missing usable evidence. Re-running only B after observing this defect would bias the experiment. A bounded claim-support review of the existing pair can answer this directly without creating a pseudo-independent reference key.

## 2. Method fixed before the reviewer sees the evidence

The source-only reviewer contract was frozen before constructing the actual masked packet:

`experiments/r0_p03_navigation_probe/FOUR_NEED_MASKED_SOURCE_ONLY_CLAIM_SUPPORT_REVIEW_CONTRACT_V01.md`

**Contract SHA-256:** `0e832f0d1a87f8f119f7d146f918e669f0942d3db5292d7261dd3be1597d7ac1`.

The implementation `four_need_masked_source_excerpt_claim_review_v01.py` verifies exact original SHA-256 identities of the two answer files and the two V02 source packets. It then assembles original N01-N04 question wording, two original answer sections and only the **four sources assigned to that same question and answer**. For each answer it strips precisely one author-provided `Self-description` status line and neutralizes any explicit `Packet A`/`Packet B` phrase. It preserves substantive assertions, literal and abbreviated citations, abstentions, line numbers, original blob identities, quoted evidence content and any source/context defect.

The deterministic P/Q aliases are balanced so P and Q do not always represent the same method. The mapping is reproducible from the source-generator algorithm, not cryptographically blinded or independent of the author. Therefore the reviewer is instructed to read **only** the packet and Message 081, not generator code or original A/B source documents. Original content could also reveal origins. This is **partial masking, never official blinded gold**.

## 3. Actual immutable packet and evidence custody

| Output | Original committed-intended bytes | SHA-256 |
| --- | ---: | --- |
| Masked source-only eight-answer reviewer packet V01 | **234,990** | `e53544ac31eacaf6fd64e74b67c920d9a2b0ec96bafb1a0951c5fdc43c3453a2` |
| Source-free original-lineage manifest V01 | **1,446** | `afd02851a2795be8442b1d8e859fbcf7456c3038256ebb67bddd3306f9fbda62` |

The packet represents exactly **four fixed questions, eight original source-conditioned answers, 32 source contexts and 64 original excerpt windows**. **Eight** self-disposition labels were removed, and **two** treatment-name occurrences were neutralized. All substantive claim/citation text and context selection remain identical to the original frozen answers and source packets. A proof by construction and accompanying synthetic tests verify that all 32 case-local source contexts equal the original individual packet contexts and that the B N03 cross-question citation remains present but its N04 source is not silently added to N03.

The original author messages are unchanged, SHA-256 `618767905efe5c3f4ff67088a45b579a41b7b420679e20b7ec5870e6cd501b05` and `171a000daa1bd569ecac3cc5227c9239d9b513684b5ce35b04edc2db39584905`, respectively. Original Packet A V02 and B V02 remain SHA-256 `3876a30dabc022c67483ea0de5c3ddfcbb75c43ed054f5e4668345df53fe9a37` and `a7ec96918330aa75b2ead92fcf6ad60b4324abc9d5f90ed1f82d1422fc6499d0`.

No Git-history source body, protected original-reference report, original reviewer item-level receipt, private gold mapping or scored answer is opened by the packet builder. The source excerpts in the fixture were previously proven to be the **original Git lines displayed to the authors**; however, that mechanical fact does not by itself establish that the reported history is true.

## 4. Frozen next reviewer contract and necessary restraint

Message 081 specifies **one new, separate Claude Code reviewer session**, not the original A or B author. That reviewer should analyze the eight source-conditioned answers claim by claim, using **only the four allowed source contexts per response**. Claim categories are `SUPPORTED_BY_VISIBLE_LINES`, `PARTIAL_OR_OVERBROAD`, `UNSUPPORTED_OR_OUT_OF_CASE`, `CONTRADICTED_BY_VISIBLE_LINES`, and `INSUFFICIENT_VISIBLE_EVIDENCE`. The reviewer also evaluates proper unsupported-subpart abstention, ambiguous shorthand citations, source-reported versus operative authority claims and cautious within-question paired supported coverage.

Complete exact source-specific per-claim reasoning is confined to a new Git-ignored local report. Public Message 082 must be an **aggregate-only**, source-free result and sole-file local commit; no push by the reviewer. The reviewer must disclose same-provider/model-family biases, accidental commit metadata, custody limitations or source packet deviations. Its labels remain a **post-hoc interpretive assessment**, not formal reference gold or independent experimental treatment scoring.

Important limits persist: four broad questions are not the governed 12+9 formal Research 513 cohort; the heading method is not actual B1/B2/B3/B4; no maintenance F1, authoring churn or independent owner-act truth is measured. A future architecture decision must consider entire project knowledge design, correctness, complexity, lifecycle, CI/CD, collaboration and change triggers rather than privileging a convenient retrieval win. If this reviewer cannot produce useful grounded distinctions, stop the preliminary loop rather than commission arbitrary further reviews.

## 5. Completion and decision gate

The immediate next operation is to receive and check the source-free masked claim support review, not to change source packets or re-author answers. Afterward synthesize supported coverage, meaningful retrieval differences and the risk from case-boundary breaches. Decide explicitly whether additional retrieval experiments have positive marginal architectural information value; do not allow an indefinite series of unscored evaluations to substitute for broader architecture evidence.

    EIGHT_ORIGINAL_FROZEN_ANSWERS=true
    AUTHOR_A_B_UNCHANGED=true
    ORIGINAL_GIT_PIN=47ed6344a9153dcf366769e95722840fbf1a8f8b
    MASKED_SOURCE_ONLY_FIXTURE_FROZEN=true
    SOURCE_CONTEXTS=32
    CASE_LOCAL_EXCERPTS_ONLY=true
    ORIGINAL_REFERENCE_GOLD_READ=false
    REVIEW_RESULT_PENDING=true
    FORMAL_R0_P03_RESULT=INCOMPLETE
    PHYSICAL_ARCHITECTURE_SELECTED=false
