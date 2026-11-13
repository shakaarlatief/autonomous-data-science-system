# Validation 359: Three complete Claude masked-review batches, original Git witness replay and post-review unmasking

**Date:** 2026-11-13
**Status:** ORIGINAL_CLAUDE_MESSAGES_067_069_071_COMMITTED_AND_VERIFIED / 24_EXPOSED_GPT6_ANSWERS_RETROSPECTIVELY_CONSOLIDATED / ORIGINAL_GIT_LINE_VERIFICATION_COMPLETE / FORMAL_R0_P03_UNSCORED
**Research:** Research 660. **Checkpoint:** 923.
**Scope:** Record exact Git and reviewer evidence, per-variant and per-claim identity, original source-line provenance and the scientific limitations of treatment unmasking after all reviewer messages were frozen.

## 1. Original independent-model reviewer messages

Three fresh, separate Claude Code Opus 5.5 reviewer sessions were manually launched by the owner. Exact original file publications, with only the authorized new message in each commit:

| Review | Original commit | Exact file bytes | Original SHA-256 |
| --- | --- | ---: | --- |
| MC-0030 Message 067, P01-P04 | `53570bca8877790988ed960ccc15aae33e99b51b` | 26,561 | `528c386865b311f899e2d41c98e29ccfdb879a01e8b2553433aa7c6524ec336f` |
| MC-0030 Message 069, P05-P08 | `49916716d2bf47ecfd526ba1fa802a856633daaf` | 31,976 | `aac51653f23d85dba319a5bcd8c78410a880a840d5d2b85240edda2bd30eb42c` |
| MC-0030 Message 071, P09-P12 | `5c8916f58c0f094db7a310db73ab5d68a3d11ab2` | 39,129 | `4b3d77528e9aef20ef0e38ad5b3d38990757d4cb9d7796efdc782fc9ea1764c1` |

Original packet SHA-256s are `6f76a9d8cb11beb64e0b8493230bf24e3b6f87920c562368ac14e2cd458bdb3b` (59,983 bytes), `0615031623d83c7bb6aba74588d18fa9fca5877d72828bd735f5f503b1751623` (62,864 bytes), and `e63afe2ebe79fc7e6ec3751d61971c6794d71cc1904057f2ee7aa691f9636804` (62,152 bytes). Exact original pinned source Git SHA `47ed6344a9153dcf366769e95722840fbf1a8f8b`. The Claude reviewers made no changes to those packets, case questions, source lines or answers.

Third Message 071 was observed as Git commit `5c8916f58c0f094db7a310db73ab5d68a3d11ab2`, parent `18f26709b967dce1444a7aeb7997efc0f604c492`, and exactly one added path `docs/model_collaboration/threads/MC-0030/messages/071_claude_r0_p03_masked_b0_b1_p09_p12_claim_review.md`. Original 39,129-byte report and 17 claim rows / eight answer categories were mechanically matched to all four frozen P09-P12 source packet cases and the exact original claim IDs and cited line ranks. Original reviewer output was fast-forward pushed and the runtime reported `PUBLIC_REPOSITORY_INTEGRITY=PASS`; the local branch was clean after push.

## 2. Post-review mechanical unmasking implementation and first exact result

The consolidator was authored only after all original reviewer messages had been committed and pushed. It opens each original packet/report through exact first-published SHA-256 guards, parses each source-masked case's individual claim rows and whole-answer category, verifies original GPT-6 response text and all source/claim references against the Checkpoint922 packet, and **only then** maps variants to B0/B1 using the already frozen alternating assignment. It also verifies each cited original Git source text, source SHA, line ordinal and individual line SHA against original Git at the pinned revision.

    AGGREGATOR=experiments/r0_p03_navigation_probe/route_b_three_claude_masked_review_consolidation_v01.py
    ORIGINAL_RESULT=experiments/r0_p03_navigation_probe/route_b_three_claude_masked_review_consolidation_result_v01.json
    ORIGINAL_RESULT_BYTES=28645
    ORIGINAL_RESULT_SHA256=8a59c63e4fab9e0a86afb7d0b3d3b7e9fc6dc5bbf9539fef228ba97ca0753f69
    ORIGINAL_QUESTIONS=12
    ORIGINAL_MASKED_RESPONSE_PAIRS=12
    UNMASKED_ANSWERS=24
    ORIGINAL_NUMBERED_CLAIMS=47
    ACTUAL_PINNED_GIT_SOURCE_LINE_HASH_RECHECKS=360
    ORIGINAL_OUTCOME_B0=10_FULL/0_PARTIAL/2_PROPER_ABSTENTION
    ORIGINAL_OUTCOME_B1=10_FULL/2_PARTIAL/0_PROPER_ABSTENTION
    TOTAL_CLAIM_VERDICTS=45_SUPPORTED/2_PARTIAL/0_UNSUPPORTED
    FALSE_OPERATIVE_ASSERTIONS_REPORTED_BY_CLAUDE=0
    INDEPENDENT_REFERENCE_TRUTH_GOLD=false
    FORMAL_R0_P03_SCORED=false

The first run exposed one parser anchoring issue in new code: the review-heading detector originally anchored to end-of-input instead of the section heading line. It was corrected in the **new aggregator only** before saving the original consolidated result. No source or review file was changed. The first successful result was exclusively created and frozen at its exact original 28,645 bytes. The dedicated test module's first run reported 5/6 pass due an overly strong *test-only* assumption that **every** explanatory limit sentence must contain the word `not` or `remain`. That assertion was corrected in the test only. The second execution verified **6/6 PASS**, with exact full output replay and all original source witnesses unchanged.

## 3. Observed precommit regressions and repository integrity

The following **95 nonoverlapping selected tests actually executed** with isolated `--basetemp` locations and no pytest cache:

| Source/test family | Verdict |
| --- | ---: |
| New three-Claude original-review consolidation and original Git-source exact replay | **6/6 PASS** (0.26s) |
| Original three treatment-masked packets, source/line identities and absent self-gold | **5/5 PASS** (0.20s) |
| Prior original GPT-6 24-answer source-only authoring and exact citation integrity | **11/11 PASS** (0.22s) |
| Prior 84 deterministic source-cited extractive answer drafts and original Git replay | **12/12 PASS** (0.73s) |
| Previous frozen B0 twelve-question original source baseline | **9/9 PASS** (0.62s) |
| Previous B1/B2/B3 original subject/link/concern retrieval variants | **10/10 PASS** (0.80s) |
| Previous classical LSA16 dense B4 source model and negative result | **10/10 PASS** (1.46s) |
| Model collaboration state and immutable message identity | **32/32 PASS** (0.67s) |
| **Selected nonoverlapping regressions** | **95/95 PASS** |

The actual repository gates also passed:
- `scripts/check_current_routing.py`: PASS with checkpoint **923**, checked branch `v1-source-vault-bootstrap-resume`, boundary `p-three-three-claude-masked-answer-reviews-complete`, original formal R0-P03 outcome **INCOMPLETE**.
- `scripts/check_knowledge_map.py`: PASS, **660** numbered research records, **924** checkpoint number records, 19 topical groups.
- `scripts/check_checkpoint_metadata.py`: PASS, **924/924** numbered checkpoints compliant.
- `git check-attr text`: new original consolidated JSON has `text: unset`, protecting exact bytes under Windows line ending handling.
- Exact original consolidated JSON byte length and SHA-256: **PASS**, 28,645 bytes, `8a59c63e4fab9e0a86afb7d0b3d3b7e9fc6dc5bbf9539fef228ba97ca0753f69`.
- `git diff --check`: exit **0**, with nonfatal routine text LF/CRLF warnings.
- Full `scripts/check_repository_integrity.py --checked-branch v1-source-vault-bootstrap-resume`: **PUBLIC_REPOSITORY_INTEGRITY=PASS**. Family-aware repository contracts, Project Knowledge, checkpoint metadata, Knowledge Map, model-collaboration state and routing each PASS.

**This is a precommit qualification record only.** Guarded commit, remote fast-forward publication, original committed JSON blob and clean local branch must be separately observed after execution.

No original source, question, model answer, masked packet, Claude report, Git branch policy, owner authority or production migration was changed by this stage.

## 4. Non-score interpretation

The aggregator is a **descriptive review-of-reviews**. Claude's excerpt entailment verdicts are not unexamined truth labels and certainly not official Research513 pass criteria. Three sessions of one model family, exposed authored tasks/answers and bounded source excerpts cannot replace independently sourced reference answers, representative hard tasks or the five-arm physical architecture test. Correct abstentions do not count as correct complete answers. No current authority or migration changes are implied.
