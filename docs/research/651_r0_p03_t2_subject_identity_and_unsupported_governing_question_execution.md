# Research 651: T2 subject binding, source-referent recovery and unsupported-authority challenge execution

**Date:** 2026-11-13
**Status:** REAL_118_REQUEST_T2_V02_EXECUTED / ORIGINAL_V01_FAILURES_RECOVERED / SYNTHETIC_AUTHORITY_CONTROLS_ABSTAIN / NO_FORMAL_R0_P03_SCORE
**Scope:** Evaluate whether source-specific assertions can remain bound to the requested document, rather than to the top lexical hit, and whether unsupported current-governance questions and intentionally contradictory identifiers are withheld without suppressing useful document candidates.
**Authority:** Existing Checkpoint 913 exact source universe at Git pin `e8ae867392f818f43dc8b76984f164e277d5cc87`, immutable V01 result, before-result V02 contract, real executable, complete exclusive-create outcome trace, unit/synthetic and original-Git replay tests.
**Checkpoint:** 914. **Validation:** 350. **Collaboration:** MC-0030 Message 065. **Specification:** 028 unchanged.

## Summary and scientific qualification

A real 118-request executable regression compared the earlier **top-one source-header assertion** to a new **complete-title source-identity binding rule** over precisely the same Git-pinned **120 documents** and FTS5 top-ten rankings. Previously, exact source/status correctness was **22/24** and a source-backed wrong-document assertion occurred once. The V02 identity-bound rule produced **24/24 exact target+Status interpretations** and **zero wrong-source assertions** for the original 24 source-status questions.

For 94 additional source-derived synthetic controls, the rule emitted no recorded-status assertion: **23/23** conflicting numbered ID/title requests, **23/23** nonexistent numbered-ID requests, **24/24** abbreviated partial subjects and **24/24** operative-governing questions. Every answer retains the independently produced top-ten lexical candidates separately, never as governing or source-status evidence.

**This is a mechanism-level regression, not a general-purpose subject identity solution.** The exact normalized first-H1 rule is advantaged because the questions were constructed from those same first-H1s, and the corpus, test methods and two original failures have already been inspected by the implementation author. All negative controls are likewise generated deterministically from those same exposed source titles. No independently authored natural questions, paraphrase robustness, real lifecycle/accepted decision oracle or independent scoring exists. The original Research 513/559/576 R0-P03 protocol remains unscored.

## 1. Exact input and method freeze

Use the exact Checkpoint 913 JSON `exploratory_t2_owner_status_guarded_retrieval_result_v01.json` (224,009 bytes, SHA-256 `b56b2f173cb69f34e5d6a009421ce738fab5640c47b615796a51a3005b77e843`) and exact historical Git archive commit `e8ae867392f818f43dc8b76984f164e277d5cc87`. Validate all 120 individual original source bytes against the V01 SHA-256 roster. The earlier 65 historical source paths are still absent. The 24 original task labels and query topics were not changed.

The new experimental contract `EXPLORATORY_T2_SUBJECT_BINDING_AND_UNSUPPORTED_AUTHORITY_CONTRACT_V02.md` was written **before** the first saved V02 result. Its first execution stopped without output because some non-target distractor documents lack first-H1 headings. That is a legitimate original-corpus condition. Before any result existed the contract and code were explicitly corrected to treat such a candidate as **unable to establish document identity**, not to invent its name or discard that distractor. There was no post-result task or label change.

The V02 engine receives only typed request topic/intent and the same top-ten SQLite FTS5/BM25 candidate rankings as before. It does **not** receive the target source path, intended label or case type. For each returned candidate with a first H1, it applies the previous T2 `topic_from_heading` transformation, normalizes punctuation, whitespace and case, and accepts exactly one **complete** normalized subject-title match. Two matches cause `AMBIGUOUS_SOURCE_IDENTITY`, none causes `IDENTITY_NOT_VERIFIED`. A candidate without an H1 cannot match. Verified source self-status is then read from its existing V01 native-parsed `Status` field with an exact original source line and SHA witness, returning `ASSERTED_SOURCE_STATUS_ONLY`; missing/unclassified status returns `NOT_FOUND_IN_COVERED_SCOPE`.

The distinct `OPERATIVE_GOVERNANCE` intent always returns `UNSUPPORTED_OPERATIVE_GOVERNANCE` because this sample provides **no trustworthy source-lifecycle/owner-authentication/currentness oracle**. All responses retain a `candidate_documents_not_authority` array holding the exact top-ten retrieved candidate paths. Candidates are discovery aids, not evidence of governing status.

This is a typed structured request experiment, not an executed natural-language intent parser or an architecture-neutral semantic retrieval arm.

## 2. Complete challenge matrix and executed outputs

The task matrix was fully generated before index/ranking execution from the unchanged 24 original first-H1 topic requests.

| Challenge family | Requests | Recorded-status assertions | Other outcome |
| --- | ---: | ---: | --- |
| Original recorded-source-status topics | 24 | **24** | All 24 exact target document and recorded Status |
| Contradictory numbered record ID with original other title | 23 | **0** | 23 `IDENTITY_NOT_VERIFIED` |
| Unknown record number `999999` with existing topic title | 23 | **0** | 23 `IDENTITY_NOT_VERIFIED` |
| Partial topic (two title tokens plus `overview`) | 24 | **0** | 24 `IDENTITY_NOT_VERIFIED` |
| Question asking whether source currently governs | 24 | **0** | 24 `UNSUPPORTED_OPERATIVE_GOVERNANCE` |
| **Total** | **118** | **24** | **94 intentionally unsupported/ambiguous requests withheld** |

The 23-numbered subset is all prior V01 topic requests with a numeric `Research N:` or `Checkpoint N:` identifier. One non-numbered title does not qualify for a number-substitution control. Each contradictory numeral was deterministically substituted from another source title in the same family; no after-output case curation.

**The two actual original top-rank failures were recovered:**
- `T2-08`: target `docs/research/PROJECT_KNOWLEDGE_ARCHITECTURE_REQUIREMENTS_V02.md`, lexical rank **3**. V02 finds its exact title-topic identity among the same top ten and binds the source-header status to the target rather than the unrelated rank-one corpus result.
- `T2-24`: target `docs/research/476_integrated_thin_centred_hybrid_successor_candidate_v01.md`, lexical rank **2** behind `docs/checkpoints/812_integrated_thin_centred_hybrid_candidate_frozen.md`. Both are relevant but only the requested **Research 476** title matches. V02 correctly avoids asserting Checkpoint 812's recorded status as an answer about Research 476.

These recoveries do not imply that the top-ranked retrieval algorithm improved: **all 24 original candidate rankings are exactly unchanged**. The actual improvement is the assertion gate's explicit referent-binding behavior in one deliberately structured and title-derived task family.

## 3. Negative controls, expected limitations and falsification interpretation

The new gate prevents a *specific verified engineering failure*: a candidate's perfectly authentic own-source status was previously allowed to masquerade as evidence about another source. It also makes unsupported, mismatched and incomplete subjects fail closed without hiding potentially relevant documents.

However, the test **does not establish** that the method solves realistic semantic reference: complete-title equality would reject abbreviated document names, project-wide topics, natural paraphrases, cross-source editorial aliases, renamed carriers, semantically equivalent terms, and many legitimate multi-document questions. Detecting an operative-governance intent is supplied as a typed test-field, not inferred from raw natural language. The 24 empty operative-governance assertions are **policy-by-construction**, not an observed true-negative correctness rate against real authority gold.

A further dangerous failure remains possible: two documents may have the same normalized H1, in which case the rule must abstain rather than select a preferred carrier; a regression synthetic tests this. A document with no H1 is unbindable by this method even if there is other legitimate identity evidence. Requiring exact title identity is an unacceptable general navigation design by itself and is **not** being promoted as the optimal architectural representation.

## 4. What should be tested next, on genuinely qualified tasks

The next meaningful comparison must join **actual source-owned identity and lifecycle semantics** to independently originated questions about current vs superseded vs proposed decisions, with explicit time/scope and real authority provenance. Compare a retrieval-first no-assertion baseline, title/identity aliasing, validated metadata/lifecycle links, hybrid evidence-aware assertions and a fair semantic candidate stage, including authoring and computation burden. Questions not supported by the examined sources must remain answerable as **unknown** rather than fabricated absent/accepted facts.

Do not repeatedly score newly invented variants on these same 120 exposed documents and call that external generalization. Retain Checkpoints 905–914 fixtures as regression; the original R0-P03 primary/legacy independent gold and B0–B4 equality-of-context criteria remain distinct and incomplete. This experiment does not create any Specification 028 source admission, owner authorization, physical architecture selection, production migration or user approval of revised preregistration.

    CONTRACT=experiments/r0_p03_navigation_probe/EXPLORATORY_T2_SUBJECT_BINDING_AND_UNSUPPORTED_AUTHORITY_CONTRACT_V02.md
    EXECUTABLE=experiments/r0_p03_navigation_probe/exploratory_t2_subject_binding_and_unsupported_authority_v02.py
    RESULT=experiments/r0_p03_navigation_probe/exploratory_t2_subject_binding_and_unsupported_authority_result_v02.json
    RESULT_BYTES=465797
    RESULT_SHA256=3648c2a0d6c75cd566a75a09453466a86697d530a88bca5bd91b74e2c849271f
    ORIGINAL_T2_CASES=24
    ORIGINAL_SOURCE_RETRIEVAL_RANKINGS=UNCHANGED
    ORIGINAL_CORRECT_SOURCE_AND_STATUS=22_TO_24
    ORIGINAL_WRONG_SOURCE_ASSERTIONS=1_TO_0
    ADDITIONAL_CONTROL_REQUESTS=94
    UNSUPPORTED_CONTROLS_ABSTAINED=94
    SOURCE_CURRENTNESS_GOLD=NONE
    INDEPENDENT_USER_QUESTIONS=NONE
    FORMAL_R0_P03_SCORE=NONE
