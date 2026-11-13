# Research 659: Actual GPT-6 reasoned source-answer comparison, B0 versus exposed B1

**Date:** 2026-11-13
**Status:** ACTUAL_MODEL_AUTHORED_24_REASONED_SOURCE_CONSTRAINED_RESPONSES / ORIGINALLY_CITED_EVIDENCE_VERIFIED / SELF_ASSESSED_NOT_INDEPENDENT_OR_FORMALLY_SCORED
**Scope:** Continue owner-approved pragmatic R0-P03 Route B beyond source retrieval and mechanical quotation by having GPT-6 actually interpret the same previously frozen original top-three source-line evidence for all twelve primary questions under B0 and B1, with precise source citations and explicit abstention.
**Authority and original source:** Research 513/559/576 unchanged. Original Git source revision `47ed6344a9153dcf366769e95722840fbf1a8f8b`, original frozen Checkpoints 918–921 result/world, owner-approved Path B and this checkpoint's prospectively fixed source-only answer contract. Existing C01/C02 protected source cohort and nine-case legacy evidence untouched.
**Checkpoint:** 922. **Validation:** 358. **Interaction session:** chatgpt-42.

## 1. A genuine model-language interpretation step, with an explicit source-exposure limitation

The original twelve-answer manifest, B0 retrieval and B1/B2/B3/classical-LSA navigation comparator, and 84 previous model-free citation drafts are already fixed. Checkpoint 921 demonstrated that retrieving a relevant document is different from selecting the exact evidence that supports an answer. It did not test whether an actual reasoning model could interpret a claim, recognize historical versus current authority, or abstain on a missing premise.

This checkpoint therefore exercises **GPT-6 as a prose answer author**. For every question, the model writes one natural-language answer using only B0's selected excerpts and one using B1's excerpts, explicitly citing the source rank and exact original line. The author also records whether the available evidence is `SUPPORTED`, `PARTIAL` or `ABSTAIN` and why.

This is a **real model-authored prose output**, not a Python template substituting status keywords into canned text and not the deterministic extractor's own quotes. However, the present ChatGPT model **has already read the reference answer manifest and prior retrieval outcomes** and knows this repository historically. No mechanism can retrospectively remove that exposure. Consequently this is an **exposed coordinator experiment**, *not a blind model run*, independent answer reference, neutral scientific evaluator, or formal Research513 B0–B4 result. The source packet contains no answer key, but this does not prove model-level blindness. All three limitations are important and persisted directly in original result metadata.

## 2. Prospective source-context and author contract

Before writing any of the 24 model prose answers, we exclusive-created:

    CONTRACT=experiments/r0_p03_navigation_probe/ROUTE_B_EXPOSED_MODEL_REASONED_B0_B1_CONTRACT_V01.md
    SOURCE_ONLY_EXPORTER=experiments/r0_p03_navigation_probe/route_b_reasoned_b0_b1_source_packet_export_v01.py
    MODEL_INPUT_PACKET=experiments/r0_p03_navigation_probe/route_b_reasoned_b0_b1_gold_free_source_packet_v01.json
    INPUT_ORIGINAL_BYTES=155794
    INPUT_SHA256=60ec37969aa3319ce195353a6f9cddb2103640b0e4f748564e0be4a4d839b508

The exporter consumes only the immutable Checkpoint921 original output **995,317 bytes** SHA-256 `17f5bae16a96530008ea954e7145e3903e25386d83eeee7e69b983de91b908f8`, selecting the same twelve questions and two existing ranked methods, `B0_ORIGINAL` and `B1_EXPOSED_SUBJECT_B0`. For each of the original top-three retrieved carriers, it preserves exactly the previously supplied up-to-five source lines, original line ordinal, source SHA and line SHA. It **excludes** reference answer text, expected source identity, old reference excerpts and previous source-coverage grades. The exporter itself is a reproducible standard-library function, and its original 155,794-byte output is hash-verified.

The method contract requires short prose answers with explicit source-scoped citations to **already available lines only**, distinguishing proposed, design-frozen, source-accepted, operative and implemented statuses. Unanswered questions must be explicitly bounded; the source writer must not infer any current branch/status from later historical memory. No source outside an arm's actual three retrieved records, no line beyond the selected exact Checkpoint921 quote set, and no new answer references are allowed.

Only **B0 versus B1** is exercised in this manual GPT-6-authored prose pass, not all seven navigation methods. This is a deliberately bounded *first* model reasoning comparison: it tests the differential value of source-semantic subject membership in readable answers. The other original B2/B3/LSA methods remain in the exact Checkpoints919–921 mechanical evidence experiments. They must not be retroactively credited with a GPT-6 prose evaluation that did not happen.

## 3. Actual original saved model-author responses

The model explicitly wrote all **24 distinct answer texts** in this conversation, one for each original twelve questions × two arms, before saving the final immutable original JSON:

    OUTPUT=experiments/r0_p03_navigation_probe/route_b_reasoned_b0_b1_gpt6_exposed_answers_v01.json
    ORIGINAL_BYTES=56283
    OUTPUT_SHA256=5e8848f444fee4234fe885d9350e872393ac20f24a043c2347e615dafccdc388
    MODEL=GPT-6
    MODEL_IS_FRESH_INDEPENDENT=false
    MODEL_HAS_PRIOR_REFERENCE_EXPOSURE=true
    QUESTIONS=12
    ARMS=2
    MODEL_AUTHORED_PROSE_RESPONSES=24
    EXPLICIT_EVIDENCED_CLAIMS=47
    ORIGINAL_CITATION_ENTRIES=78
    UNIQUE_SOURCE_BLOBS_ACTUALLY_CITED=12
    UNIQUE_ORIGINAL_SOURCE_LINE_REFERENCES=41
    EXACT_ORIGINAL_GIT_SOURCE=47ed6344a9153dcf366769e95722840fbf1a8f8b
    ORIGINAL_SCORE=NONE

The file carries each actual answer text, source-exposure/abstention caveats, individually authored evidenced claims, original source-rank and line references, exact source and source-line SHA hashes and a separate self-classification.

**Original model-author self-classification, NOT independent correctness:**

| Model-author source-evidence disposition | B0 original | B1 subject+B0 |
| --- | ---: | ---: |
| `SUPPORTED` by the excerpts the model could cite | **9/12** | **10/12** |
| `PARTIAL` support with explicitly qualified missing aspect | 1/12 | 2/12 |
| `ABSTAIN` because specific information was absent | 2/12 | 0/12 |

These categories are **not** the Research513 `>=10/12` criterion. They are the prior-exposed answering model's own report of whether its sentence claims follow from its available quoted evidence, and the same model lacks neutral reference truth. Numeric coincidence between B1's `SUPPORTED=10` and the original formal threshold is neither qualification nor threshold attainment.

## 4. Paired case-level evidence and substantive reasoning

| Case | B0 | B1 | What the model actually did |
| --- | --- | --- | --- |
| **P01, archived checkpoint and branch** | `ABSTAIN` | `SUPPORTED` | B0's retrieved sources did not include an actual current-state record with both requested values. B1's third carrier is original `docs/CURRENT_STATE.md`, recording Checkpoint **899** and `v1-source-vault-bootstrap-resume` on original lines 3 and 5; the model cited these and explicitly limited the answer to the archived state. |
| **P02, decisions register and revision** | `PARTIAL` | `PARTIAL` | Both arms retrieved `docs/DECISIONS.md` line 1 `# Decisions` and line 5 expressly permitting revision with preserved history. The exact word *project-wide* was not established separately by the selected short excerpts. Rather than silently importing the known but *not selected* opening line of the full source, GPT-6 gave the file and revision rule but marked the scope qualifier. |
| **P03, Specification 028 implementation-status header** | `ABSTAIN` | `PARTIAL` | Neither arm included Specification 028's source header. B0 found a different comparative candidate which did not authorize the migration; B1 found Checkpoint 550's original W1 semantic-migration progress and subordinate-continuity language. The model did not paste in the previously seen `FROZEN / IMPLEMENTATION PENDING` specification header from memory. It reported what could actually be said and did not manufacture the requested exact status. |
| **P04–P09, source foundations / selected candidates / authority** | `SUPPORTED` | `SUPPORTED` | Both arms supported Foundation 022 original-artifact/provenance design, Specification 025 `FROZEN / IMPLEMENTATION PENDING`, accepted historical W5 T1 design without production activation, Research 503 charter without physical target, `GOVERNED_LEDGER_KERNEL_V02` candidate with owner decision not ready, and AO-10's explicit absence of implementation/migration authorization. |
| **P10, R0-P02 pass and probe sequencing** | `SUPPORTED` | `SUPPORTED` | Both identified the historical Checkpoint 853 `R0-P02 PASS / R0-P01 NEXT`, while separately citing later Checkpoint 891's prospective supersession of R0-P01's mandatory preselection gate. This distinguishes a historically true next-step statement from a later effective gate rule. |
| **P11–P12, deferral and unscored evidence** | `SUPPORTED` | `SUPPORTED` | Both cited Checkpoint 891's owner-directed authentication deferral and P03 fixture continuation without implying a real owner-auth ceremony, and Checkpoint 899's insufficient independently verified reference capacity without calling the unscored experiment a formal failure. |

The P02/P03 qualified outputs are arguably more useful than an unjustified certainty score because they explicitly expose the missing evidence. But whether any full natural-language inference is semantically valid is still **not independently evaluated**. A question sourced from an archived record also does not prove current operational authorization or acceptance just because the source itself includes `Status: Accepted`.

## 5. Executable integrity and explicit model limitation

This stage adds a dedicated `tests/unit/test_r0_p03_route_b_exposed_gpt6_reasoned_b0_b1_answers_v01.py` source witness test module. It verifies immutable input/output sizes and hashes, reruns the **model-facing source-packet exporter** byte identically, checks the 12 × 2 source/answer pairing and absence of gold fields, verifies all **78 original line citations** against actual Git source blob SHA and original line ordinal/SHA in the provided packet, and checks specific P01/P02/P03/P09/P10 abstention/supersession boundaries. It verifies that the same model did not cite a source outside the original B0/B1 top three or quote a line unavailable to that arm.

It does **not** reexecute the original GPT-6 authoring deterministically. Claiming a bitwise rerun of a manual model answer would be a category error; only packet export and source citations are mechanically replayable. Moreover, original-source match does not mechanically prove natural-language entailment. The report preserves this distinction instead of treating a model's self-assessment as independent gold.

The previously attempted Claude CLI readiness call timed out under the bound. Codex's user-authored Call Profile currently requires specific approval before a paid model turn; this stage did not initiate an unapproved Codex model session. No fresh reviewer was obtained, and neither model/tool unavailability was hidden.

## 6. Decision-relevant lessons and next work

We have now observed both **mechanical answer-evidence availability** (Checkpoint921) and **actual model-authored source interpretation** (this checkpoint). The same historical source limit can lead to supported prose, partial prose or a principled abstention. One source may appear in the retrieved top three but the exact scoped answer still require lines not selected (P02); a model must be able to say so.

There is no scientific evidence here for a blanket B1 promotion. The metadata was coordinator-authored *after seeing earlier answers*, and was not requalified as truly original source-owned metadata. The present answerer was previously exposed. A formal head-to-head B0–B4 physical architecture decision still requires independent answer references, a complete equal V03-native substrate, a qualified semantic B4 if appropriate, neutral historical nine-case gold and heldout source-annotation/maintenance checks. Those constraints remain original Research513/559/576 requirements and cannot be erased by an exploratory 10/12 self-disposition count.

**Next most informative bounded step** is an independently authorized source-limited model/reviewer critique of the now-fixed 24 responses, or controlled Level B model-author/evaluator admission if an actual fresh context/model becomes accessible. The exact frozen source/answer packet is now available, so that review need not restart task origination or expose protected C02 reference material. Repeating more self-scored variants on the same exposed questions is unlikely to improve the independence basis.

The project owner's unrestricted ability to rethink architecture, files, Git/CI process and collaboration remains fully preserved. This checkpoint selects no architecture, migration, operational authority or working-procedure lock.

    CHECKPOINT_922=ACTUAL_GPT6_EXPOSED_MODEL_SOURCE_REASONED_B0_B1
    PRIMARY_CASES=12
    MODEL_AUTHORED_ANSWERS=24
    VERIFIED_SOURCE_LINE_CITATIONS=78
    MODEL_SELF_SUPPORTED_B0=9_OF_12
    MODEL_SELF_SUPPORTED_B1=10_OF_12
    INDEPENDENT_SEMANTIC_EVALUATION=NONE
    FORMAL_R0_P03_OUTCOME=INCOMPLETE
    ARCHITECTURE_SELECTED=false
