# Route B: masked, source-only independent model critique of frozen GPT-6 prose, V01

**Date:** 2026-11-13
**Status:** FROZEN_BEFORE_FIRST_REVIEWER_MODEL_RESPONSE / CLAIM_SUPPORT_EVIDENCE_ONLY / FORMAL_R0_P03_REMAINS_UNSCORED
**Purpose:** Test the actual original-source entailment of the 24 GPT-6 B0/B1 prose answers saved at Checkpoint 922 without showing their original answer author's own self-classifications or known question/reference gold. This is an independent *review of an exposed author's outputs*, not fresh reference-author task origination.

## 1. Source, reviewer exposure and source world

The author output was first frozen at Checkpoint 922:
- Original Git source horizon `47ed6344a9153dcf366769e95722840fbf1a8f8b`.
- Original gold-free source packet `route_b_reasoned_b0_b1_gold_free_source_packet_v01.json`, **155794 bytes**, SHA-256 `60ec37969aa3319ce195353a6f9cddb2103640b0e4f748564e0be4a4d839b508`.
- Original 24 GPT-6 answer texts `route_b_reasoned_b0_b1_gpt6_exposed_answers_v01.json`, **56283 bytes**, SHA-256 `5e8848f444fee4234fe885d9350e872393ac20f24a043c2347e615dafccdc388`.
- Source-limited original quoted evidence parent `route_b_extractively_cited_answer_evidence_result_v01.json`, **995317 bytes**, SHA-256 `17f5bae16a96530008ea954e7145e3903e25386d83eeee7e69b983de91b908f8`.

A deterministic source-only exporter creates **three** prospective non-overlapping review packets, P01-P04, P05-P08 and P09-P12. Each contains 4 original frozen questions and 8 prose answers, their individual explicit claims and original 3-or-fewer source carriers with line numbers, original Git source SHA and original line SHA. Per-question paired answers are **counterbalanced** in display order. The reviewer sees only `VARIANT_A`/`VARIANT_B`, **not** B0/B1 labels, earlier hit@k, previous author `SUPPORTED/PARTIAL/ABSTAIN`, original reference answer text, target source or retrospective quoted-evidence grades. The mapping to B0/B1 remains in the already frozen source-packet exporter code, which the reviewer is **not** allowed to inspect.

Independent means **fresh distinct model invocation without direct prior author narrative or scoring** and reviewer-only packet input. It cannot mean the entire model vendor or installation has scientifically certified no prior repository knowledge. A Codex reviewer shares account and repository runtime context; default project runtime instructions may exist. The review must not claim stronger independence or full blind neutral source-authority knowledge than the physically observed model environment supports.

## 2. Input and strict assessment rubric

Read **only** the exact assigned `route_b_treatment_masked_claim_review_pXX_to_pYY_v01.json` file; do not open any other repository file, worktree artifact, prior comparison, model-authored result, test, README, `AGENTS.md`, reference answer key or web source; do not call an external website. If the runtime requires reading project instructions or has injected them automatically, disclose this and identify a source-exposure limitation. Source text supplied in the packet is the **whole authorized evidence universe** for this review.

For each question and each masked variant:
1. Evaluate each individually listed claim `C01,C02,...` solely against the exact cited original line refs from that variant's own `available_evidence`. Use `SUPPORTED` only if the line words directly establish the full claim (including temporal scope); `PARTIAL` if some but not all material clauses are supported; `UNSUPPORTED` if missing, contradicted, or reliant on unseen context. Include an evidence-grounded short rationale and specific exact source rank/line identifiers that support or refute it.
2. Evaluate whether the full natural-language `answer` actually answers all aspects of the original question, even when the cited claims are true. Use `FULLY_SUPPORTED`, `PARTIALLY_SUPPORTED`, `PROPER_ABSTENTION`, `MISLEADING_OR_UNSUPPORTED`. Do not count a cautious, necessary abstention as a fabricated successful complete answer. Differentiate an unsupported claim from honest lack of source evidence.
3. Identify **any unlisted substantive answer assertion** absent from the numbered claims and whether it is supported or is an ungrounded addition, so the original author cannot omit bad clauses from self-written claim lists.
4. Assign independent `false_operative_authority_assertion` true only if the answer asserts current governing/deployment/migration permission from archived `Status`, candidate or unqualified source. Identify any later historical supersession or known source scope conflict **only if its cited line is in that variant's packet**.
5. For every variant record `critical_missing_evidence` as an explicit list of clauses the original question asks that this variant's cited lines cannot establish. Do not import full source data or reference answers, even if recognized from the title.
6. Include an `adjudicator_uncertainty` note explaining genuinely uncertain entailment, if present.
7. Explicitly say no claim about source-currentness beyond the original Git horizon and no formal architecture winner or authoritative migration.
8. **Do not read prior model self-grades** and do not change source quotes/questions. Evaluate both variants even when they appear similar.

## 3. Reviewer response schema and saved evidence

Reviewer should produce **one raw UTF-8 JSON file** per four-case assigned packet, e.g. `.venv/.r0_p03_independent_review/work/p01_p04_reviewer_response_v01.json`, with no source corpus mutations, no test/branch/git mutations, and the following fully specified top-level fields:
- `review_protocol`: `ROUTE_B_TREATMENT_MASKED_CLAIM_REVIEW_CONTRACT_V01.md`
- `input_packet_sha256`: exact input SHA-256 supplied by caller
- `reviewer`: model name, invocation mechanism, fresh-thread/isolated-context claim **as actually observed**, plus any unrequested pre-exposure
- `review_scope`: source-only claim support on 4 cases, 8 answers; original official R0-P03 *not scored*
- `cases`: 4 objects preserving exact packet `case_id`. Each contains 2 `variants` preserving `VARIANT_A/B`; each variant contains `claim_assessments`, exactly one assessment for each original `claim_id`; and `whole_answer_grade`, `false_operative_authority_assertion`, `unlisted_substantive_claims`, `critical_missing_evidence`, `adjudicator_uncertainty`.
- Each `claim_assessments`: `claim_id`, `verdict`, `rationale`, `cited_line_refs_used` (list of source rank + original line).
- `summary`: per-variant grade counts, number of claim judgments, number of unsafe authority assertions; these are independently reviewer-reported and separately verified mechanically.
- `limitations`: cite source-only packet, author exposed, reviewer blind to model self-grades, not independent scored Research513 gold, not a full B0–B4 fair test.

No numerical architecture decision from reviewer alone. Retain original reviewer output **before** seeing the original self-grade or re-identifying B0/B1 treatment. Its exact bytes/hash must be frozen unmodified. Perform mechanical schema checks against original packet for every claim and original cited line. If a reviewer is not available, record the authorization/runtime hold and do not manufacture a response.

## 4. Execution and controls

A local Claude CLI preflight using `--restricted --bare --strict-mcp-config --tools "" --no-session-persistence --model haiku` returned **`Not logged in · Please run /login`** with zero model tokens, while its normal no-tools route timed out after fifteen seconds. No Claude reviewer result exists. No credentials, network/security policy or setting was changed to bypass that.

The connected Codex account preflight confirms an authenticated Plus account and the live catalog has `gpt-6-astra` with `high` reasoning. The existing user-authored Codex Call Profile explicitly requires **per-turn approval**. Call Codex only through the formal consent mechanism, with a fresh short bounded reviewer task per 4-case packet, model/effort selected according to profile and task complexity; keep supervising if approved, do not silently spend quota before approval. If the user defers or the model cannot run, freeze the source-only packet and report this dependency.

The first stage's goal is to complete **one** four-question reviewer packet and verify exact original reviewer evidence before proceeding to the other two. Avoid turning a three-batch reviewer attempt into weeks of credential/protocol preparation.

    REVIEWER_SOURCE_COHORT=ORIGINAL_12_X_B0_B1
    MODELS_TO_BE_CRITIQUED=EXPOSED_GPT6_PROSE_24
    REVIEW_BATCH_SIZE=4_ORIGINAL_QUESTIONS_8_VARIANTS
    REVIEWER_INPUT_MASKS_TREATMENT_LABELS=true
    REVIEWER_INPUT_EXCLUDES_REFERENCE_GOLD=true
    REVIEWER_INPUT_EXCLUDES_AUTHOR_SELF_GRADES=true
    UNAUTHORIZED_CODEX_CALLS=ZERO
    CLAUDE_INDEPENDENT_REVIEW_EXECUTED=false
    RESEARCH513_FORMAL_SCORE=NONE
