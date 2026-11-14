# Research 664: Two frozen four-need source-limited answer sets and the case-local evidence boundary

**Date:** 2026-11-14
**Status:** TWO_AUTHOR_ANSWER_OUTPUTS_FROZEN / ONE_B_N03_CROSS_CASE_SOURCE_REFERENCE / UNSCORED_DESCRIPTIVE_FEASIBILITY_ONLY / FORMAL_R0_P03_INCOMPLETE
**Scope:** Reconcile the two actual independently sessioned Claude author outputs from identical four-need questions under distinct, fixed retrieval packets, including the correct later-author HOLD and a retrospective source-only case-local reference audit, without accessing protected historical reference gold.
**Authority:** Research 663, Validation 362, Checkpoint 926, MC-0030 Messages 078–080, Validation 363, Checkpoint 927; original historical source pin `47ed6344a9153dcf366769e95722840fbf1a8f8b`; Research 513/559/576 original formal controls unchanged.

## 1. What actually happened and what the later HOLD means

Message 078 prospectively instructed two fresh Claude Opus 5.5 source-answer sessions: A to use only the immutable V02 Packet A, then B in a separate session to use only V02 Packet B. Both outputs have now been committed independently, without overwriting any original input.

| Author | Original answer commit | Parent | One original changed file | Published answer SHA-256 |
| --- | --- | --- | --- | --- |
| Packet A | `d521fefc53375bbbc29b184b7ab56cef576d90ea` | `e403a0cdb5de0747eface94c4b998c53ae66cdc4` | Message 079 | `618767905efe5c3f4ff67088a45b579a41b7b420679e20b7ec5870e6cd501b05` |
| Packet B | `193cd6d56d24b2facdc8efb11b536e22051f71a7` | `d521fefc53375bbbc29b184b7ab56cef576d90ea` | Message 080 | `171a000daa1bd569ecac3cc5227c9239d9b513684b5ce35b04edc2db39584905` |

Source-free owner relay describes a **later** Claude session that was asked to produce Message 080 after Message 080 already existed. It properly halted: actual HEAD `193cd6d5...` was one commit later than its expected `d521fefc...` and the output slot was already occupied. It read neither alternate answers nor the source packets' contents and created no file or commit. This was a **correct protocol HOLD for that attempted duplicate**, not a failure or missing output in the original Packet B authoring trial. We selected the existing validly originated single-file Message 080 as the frozen B response and did not re-run, replace, cherry-pick, or write a new Message 081.

Both actual author reports identify genuinely fresh Claude Code sessions, correct packet byte/hash input checks, four original questions with four source excerpts each, and no reported access to the other treatment's contents, historical Git source bodies, or private reference answers. Both received automatically injected recent Git commit subjects and the common Message 078 handoff, which itself disclosed earlier N01–N04 reference-review dispositions. Role separation is therefore real as reported but is **not independently established OS isolation, provider diversity or formally blinded scoring**.

## 2. Fixed source-only conditions and author self-labels

Both authors answered the same original N01–N04 needs against the original Git source horizon. Packet A was body FTS5 BM25, **92,552 bytes** SHA-256 `3876a30dabc022c67483ea0de5c3ddfcbb75c43ed054f5e4668345df53fe9a37`; Packet B was body/heading RRF diagnostic, **91,531 bytes** SHA-256 `a7ec96918330aa75b2ead92fcf6ad60b4324abc9d5f90ed1f82d1422fc6499d0`. The earlier source retrievers used the **same 2,258 historical documents**, same query text and excerpt budgets, and top-four source overlaps **[2,2,2,3]**. The heading diagnostic is **NOT** official B1/B2/B3/B4.

| Frozen need | A author self-description | B author self-description |
| --- | --- | --- |
| N01, historical orientation | ABSTAIN_INSUFFICIENT_EXCERPTS | PARTIAL_FROM_SUPPLIED_EXCERPTS |
| N02, document/file handoffs | PARTIAL_FROM_SUPPLIED_EXCERPTS | PARTIAL_FROM_SUPPLIED_EXCERPTS |
| N03, persistence-change impact | PARTIAL_FROM_SUPPLIED_EXCERPTS | PARTIAL_FROM_SUPPLIED_EXCERPTS; **case-boundary defect** |
| N04, historical foundation authority | PARTIAL_FROM_SUPPLIED_EXCERPTS | PARTIAL_FROM_SUPPLIED_EXCERPTS |

Both authors self-reported **zero** completely answered questions. A reports **3 partial + 1 full abstention**, and B reports **4 partial + 0 full abstentions**. These are **author self-labels** and not truth-tested answer grades. N01 illustrates a plausible document-discovery difference: A could not establish any dated source/decision record sufficient for even a bounded orientation answer; B's retrieved validation records permitted a qualified partial answer about project activity, but **B still could not determine the latest authorized next action or reconcile the state/decision/checkpoint authority**. Therefore B's N01 is not a complete answer or demonstrated formal improvement.

## 3. Retrospective per-case evidence boundary audit

Only *after* Messages 079 and 080 were originally committed did the coordinator construct a deterministic case-local source-reference audit. The checker opens the two frozen answer files and their respective source-only packets, verifies exact SHA-256 identities, partitions answers by the original N01–N04 sections, and checks that every **fully specified** `path@blob-SHA1` source reference within a question is among that question's four original retrieved source carriers. It does **not** inspect any private reference answer, historical Git source body or semantic source truth.

Actual output:

| Structural observation | Packet A | Packet B |
| --- | ---: | ---: |
| Fully specified source-reference occurrences | 16 | 17 |
| References assigned to the same question | **16** | **16** |
| References to a source assigned only to a different question in the same packet | **0** | **1** |
| References absent from the entire assigned packet | 0 | 0 |
| Explicit `same@blob` shorthand occurrences | 27 | 0 |

The **one B cross-case source reference occurs in N03**: the B author used evidence belonging to N04's source set while answering N03. That reference and the claims depending on it **are not admissible as a clean N03 answer from the frozen N03 Packet B excerpts**. The citation can be source-real and historically correct, but the *per-question* evidence boundary was violated. This is a substantive experimental validity qualification, not automatically a false factual claim and not evidence of exposure to another treatment's answer. A author expressly reported noticing related content in another case and not using it; B did use such cross-case evidence. The original messages and packets remain entirely unchanged.

The check intentionally does **not** assert that all 16+16 case-local source references contain the claimed quoted lines or that those lines semantically entail all assertions. The authors use shorthand, abbreviated paths and cross-paragraph aliases; these require a separate original answer-support review. Not all abbreviations are self-contained original path@blob/line citations. A source-within-packet pass is **necessary but insufficient** for evidence support.

**Preregistered versus retrospective:** the per-case evidence restriction was already frozen in Message 078, but this particular deterministic validator and its implementation were written after seeing both responses. It is a *transparent non-scored protocol check*, not a new pre-registered performance metric and not a reason to change answer inputs to obtain greener results.

The public source-free audit result `four_need_source_only_answer_case_boundary_audit_v01.json` is immutable under exact-byte Git handling. It preserves per-case counts but no document paths, original quote strings or private source mappings.

## 4. Why we preserve B rather than commission a replacement immediately

A later fresh Claude session correctly refused to overwrite Message 080 because both the expected HEAD and output exclusivity were violated. The coordinator chose to **retain the actual existing Message 080**, not create a second answer at Message 081. Repeating the answer after seeing the B N03 result would be a post-result intervention with its own bias. The narrow correction is to flag B N03 as **contaminated by cross-case source use** in the unscored interpretation.

A possible future **new versioned, prospectively controlled** test can supply each question as a distinct model-facing packet, so no answerer ever sees other questions' source contexts. This should be applied symmetrically to both methods, not only to B N03 as an outcome-guided repair. However, that new trial is not authorized simply by discovering an imperfection; its expected information gain and fair evaluation plan should be justified before more cost.

## 5. Evidence-based continuation and architectural freedom

We have now obtained actual natural-language answers from both source-only navigation diagnostics, which is more decision-relevant than source-path rank comparison alone. The results also demonstrate constraints: hard multi-plane questions remain mostly partial; one method can recover a little context another misses; bare citation pointers do not guarantee authoritative answer truth; and per-case source context must be isolated where the experimental rule requires it.

A bounded **post-hoc citation/claim support assessment** of both frozen answers, with exact in-packet original line checks and explicit handling of the B N03 cross-case item, is warranted before making any qualitative comparison. If the original protected reference report is needed, use a separate custody plan rather than exposing source-specific protected gold to the coordinator or answer models. Under the current evidence, neither treatment has an independently audited full-answer score, and no official B0–B4 experiment or architecture selection follows.

The architecture remains revisable at **every level**: information structures, substrate semantics, repository design, implementations, tests, CI/CD, development workflow, branching and collaboration. This pilot tests two cheap retrieval mechanisms, not the full proposed future knowledge architecture. No physical migration, operative authority change or production cutover is authorized.

    PACKET_A_ANSWER_ORIGINAL_COMMIT=d521fefc53375bbbc29b184b7ab56cef576d90ea
    PACKET_B_ANSWER_ORIGINAL_COMMIT=193cd6d56d24b2facdc8efb11b536e22051f71a7
    FROZEN_A_SELF_REPORTED=0_FULL_3_PARTIAL_1_ABSTAIN
    FROZEN_B_SELF_REPORTED=0_FULL_4_PARTIAL_0_ABSTAIN
    A_CASE_LOCAL_EXPLICIT_REFERENCES=16_OF_16
    B_CASE_LOCAL_EXPLICIT_REFERENCES=16_OF_17
    B_N03_CROSS_CASE_SOURCE_REFERENCE=1
    DUPLICATE_LATER_B_AUTHOR_HOLD_CORRECT=true
    AUTHORS_ANSWERS_MODIFIED=false
    INDEPENDENT_ANSWER_GOLD_QUALIFIED=false
    FORMAL_R0_P03_RESULT=INCOMPLETE
    PHYSICAL_ARCHITECTURE_SELECTED=false
