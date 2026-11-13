# Research 660: Three frozen Claude masked reviews completed and 24 original B0/B1 answers unmasked

**Date:** 2026-11-13
**Status:** ALL_THREE_CLAUDE_FRESH_SESSION_REVIEWS_COMPLETED / TWELVE_ORIGINAL_QUESTIONS_TWENTY_FOUR_ANSWERS_VERIFIED / DESCRIPTIVE_UNMASKED_ANALYSIS_ONLY / FORMAL_R0_P03_INCOMPLETE
**Scope:** Mechanically and scientifically reconcile the three independently sessioned, treatment-masked Claude Opus 5.5 source-line critiques of previously frozen GPT-6 B0/B1 natural-language answers, without changing questions, source evidence, original answers, reviewer reports or the Research 513 scored protocol.
**Authority:** Original Git source revision `47ed6344a9153dcf366769e95722840fbf1a8f8b`, Checkpoints 918-922 and the original frozen GPT-6 answer packet. Reviewer original messages MC-0030 **067**, **069**, **071**, all written and single-file committed before treatment unmasking.
**Checkpoint:** 923. **Validation:** 359.
**Scientific class:** RETROSPECTIVE_SEPARATE_MODEL_SOURCE_ENTAILMENT_AUDIT / NOT INDEPENDENT ORIGINAL REFERENCE GOLD / NOT ORIGINAL FORMAL R0-P03 SCORING.

## 1. Observed review executions and frozen-source controls

A separate new Claude Code CLI session using Claude Opus 5.5 was run manually by the owner for each of the three pre-frozen source-only packets. Each reviewer explicitly reported reading only its assigned instruction and the assigned treatment-masked packet; the ChatGPT-author original answers' self-scores, evaluator-source labels, prior Claude review contents and unmasked B0/B1 identities were withheld. The Claude sessions did receive limited local environment details, including the branch name and recent Git commit subjects, and all three used **the same Claude model family**. Session freshness and separate-model authorship therefore do not establish independent reference-answer origin, no prior semantic exposure, or inter-rater model diversity.

| Case subset | Original review message | Exact original report bytes / SHA-256 | Reviewer claims | Whole-answer grades |
| --- | --- | --- | ---: | --- |
| P01-P04 | Message **067**, original commit `53570bca8877790988ed960ccc15aae33e99b51b` | 26,561 / `528c386865b311f899e2d41c98e29ccfdb879a01e8b2553433aa7c6524ec336f` | 13 supported; 1 partial | 5 full; 1 partial; 2 appropriate abstentions |
| P05-P08 | Message **069**, original commit `49916716d2bf47ecfd526ba1fa802a856633daaf` | 31,976 / `aac51653f23d85dba319a5bcd8c78410a880a840d5d2b85240edda2bd30eb42c` | 16 supported | 8 full |
| P09-P12 | Message **071**, original commit `5c8916f58c0f094db7a310db73ab5d68a3d11ab2` | 39,129 / `4b3d77528e9aef20ef0e38ad5b3d38990757d4cb9d7796efdc782fc9ea1764c1` | 16 supported; 1 partial | 7 full; 1 partial |

All three original reviewer reports were exact Git committed and then fast-forward pushed, with reviewer original bytes preserved. The third reviewer directly checked all 120 source-line textual hashes in its packet; **our follow-up independent-of-reviewer mechanical aggregation further checked all 360 cited original Git-line occurrences across all three packets**, including original Git source SHA-256, original line ordinal, exact original full text and line SHA. This controls citation provenance but does **not** establish semantic entailment by machine or source-author truth.

### The retrospective consolidator

The following deterministic code and saved result were written **only after all three reviews existed**:

    RUNNER=experiments/r0_p03_navigation_probe/route_b_three_claude_masked_review_consolidation_v01.py
    RESULT=experiments/r0_p03_navigation_probe/route_b_three_claude_masked_review_consolidation_result_v01.json
    ORIGINAL_RESULT_BYTES=28645
    ORIGINAL_RESULT_SHA256=8a59c63e4fab9e0a86afb7d0b3d3b7e9fc6dc5bbf9539fef228ba97ca0753f69
    ORIGINAL_GIT_PIN=47ed6344a9153dcf366769e95722840fbf1a8f8b
    IMMUTABLE_REVIEW_MESSAGES=067;069;071
    IMMUTABLE_SOURCE_PACKETS=P01-P04;P05-P08;P09-P12
    MASKED_ANSWERS_RECONCILED=24
    ORIGINAL_SOURCE_LINE_WITNESSES_RECHECKED=360

For each original question and masked variant, the consolidator verifies the exact frozen review packet and report file SHA, parses the numbered claim verdicts and whole-answer grades from the **reviewer's original variant section**, aligns all original claim IDs and text with the previously frozen GPT-6 output, verifies source/line identity against original Git, and then unmasks treatment using the prospectively frozen alternating A/B assignment. It performs **no regrading**, semantic rewriting, additional text retrieval, or output conditioning on the expected grade. Any source drift, missing review, malformed claimed grade, altered source line or missing case fails closed.

This is a descriptive **post-review** analysis, not a new prospective or formally blinded experiment. Neither the runner nor the original GPT-6 author has independent claim-truth authority.

## 2. Unmasked comparison: substantial, but limited, answer evidence

Across 24 GPT-6-authored natural-language responses and 47 explicit claims, Claude graded:

| Outcome | Original B0 lexical | Exposed B1 subject+B0 | Total |
| --- | ---: | ---: | ---: |
| `FULLY_SUPPORTED` whole answers | **10/12** | **10/12** | **20/24** |
| `PARTIALLY_SUPPORTED` whole answers | 0/12 | 2/12 | 2/24 |
| `PROPER_ABSTENTION` | 2/12 | 0/12 | 2/24 |
| `MISLEADING_OR_UNSUPPORTED` | 0/12 | 0/12 | 0/24 |
| Explicit claims graded `SUPPORTED` | 23 | 22 | **45/47** |
| Explicit claims graded `PARTIAL` | 0 | 2 | **2/47** |
| Explicit claims graded `UNSUPPORTED` | 0 | 0 | 0 |

**These are not the formal Research 513 full-answer 10/12 acceptance scores.** They measure Claude's single-pass judgment that a prior exposed author's claims follow from a short set of source excerpts preselected by the exposed author's retrieval/quote pipeline. A cautious abstention is not a fully answered question. The same external reviewer family can miss errors, and the original source/answer selection is not independent.

### Case-level outcomes and why the distinction matters

- **P01, archived current-state checkpoint and branch:** B0 appropriately abstained because its top-three excerpts lacked the required archived `docs/CURRENT_STATE.md` values. B1 retrieved that original source and gave a fully supported historical answer. This supports a **source discovery benefit** of exposed B1 subject navigation for that one task, without proving its annotation process was independently grounded or generally better.
- **P02, decisions register and revision:** both whole prose answers were graded fully supported. However, B1's second **numbered claim** strengthened the source's softer `should` into a stronger `requires` and omitted part of the "what changed and why" qualifier. Claude graded that specific claim `PARTIAL`; a strong whole-answer grade does **not** imply every auxiliary claim is exact.
- **P03, exact Specification 028 implementation status:** B0 appropriately abstained; B1 provided only a partially supported adjacent migration-progress answer. Neither arm actually supplied the exact specification status header in its model-facing excerpt. The reviewer noted B1's use of historical W1 progress did not settle the question and its occasional "still" could suggest unwarranted present-day status.
- **P05-P08:** both arms obtained the decisive original-source record and produced fully supported prose. This is a **ceiling effect**, not evidence that their navigation mechanisms are equivalent. Claude disclosed mild modality, status-currentness and inferred-authority qualifiers, notably P07 "migration authority" and P08 inferred "owner physical architecture".
- **P09-P10:** both arms faithfully kept a frozen AO-10 candidate distinct from production authority, and separated historical R0-P02 PASS/R0-P01 next sequencing from later prospective gate supersession. The "later" relative order and the identity of the superseded mandatory gate are partly inferred from checkpoint numbering and source context, not explicitly dated in every claim citation.
- **P11, owner-authentication deferral:** B0 gave a fully supported historical answer. B1 gave a partially supported answer because its claim widened the source's specific `no production ledger admission` negation into a broader `production authority not completed` statement and asserted what the entire checkpoint did not claim, beyond available excerpts. The reviewer noted moderate uncertainty and that the error was conservative-direction overreach, **not** a false claim that authority existed.
- **P12, historical reference-capacity HOLD:** both arms correctly distinguished completed witness review plus insufficient verified reference capacity from a passed or failed architecture experiment. One arm added the then-open question of a fresh independent reference route or deferral, supported by an original source line.

Across all 24 reviewed answers Claude found **zero** promotions of a historical status/candidate/archived decision to currently operative physical implementation, migration, deployment or governing authority. This is important positive evidence on the reviewed scope, but **not** the independent-gold formal Research 513 zero-false-authority gate.

## 3. Why the results do not establish an architectural winner

The initial B0/B1/B2/B3/classical LSA tests used only twelve exposed coordinator-authored primary questions with a single designated original source and its excerpt witnesses. The twelve-question source answerers were the **same exposed GPT-6 coordinator**; B1 subject memberships and other metadata were **coordinator-authored with exposure to earlier rankings and reference content**. The three Claude reviewers are separate sessions of **one model family**, judging only source snippets selected by the same exposed system. They did **not** examine whole original source cases, independently author a reference answer, verify source-owner metadata origination, perform original nine-case neutral legacy scoring, assess heldout maintenance F1, or execute the complete five-arm original V03-native physical architecture trial.

The `10/12` and `10/12` fully supported whole-answer counts are **descriptively tied** under the known, incomplete source context. B0's two abstentions were **appropriate**, not unsupported hallucinations; B1's two attempts lacked full support. Differences in source discovery and willingness to abstain must be separately represented, not collapsed into one numeric winner.

A specific genuine technical implication is that **answerability and abstention need their own graded dimension**. Source retrieval top-k, excerpt recall, answer truth, grounded attribution, temporal scope and authority safety are not interchangeable. A method that retrieves a related document can increase apparent answer coverage without securing the exact requested fact. Similarly a baseline can look unhelpful on a task while behaving safely by declining to assert what it cannot verify.

Because source selection, metadata, reference answers and task construction were not independently controlled, the observed descriptive tie cannot establish equivalent expected performance. No implementation cost, scalability, source-owner ergonomics, neural pretrained B4 comparison or maintenance fairness conclusion follows.

## 4. Decision boundary and efficient next action

We should **not initiate another cycle of coordinator-generated easy questions or tune B1 metadata on these exposed twelve cases**. The most valuable missing qualification is now specifically **independent source-grounded reference truth**, including hard cases where the answer is a documented, properly bounded unknown. That needs an authorized fresh source-reading/reference-author process, with independent eligibility and neutral source scope, before scored answers are generated. Reuse actual Git evidence, already built B0-B4 navigation and existing Claude collaboration rather than rebuilding infrastructure.

The owner's approval of prospective Path B redesign stands. The original Research 513/559/576 formal score remains `INCOMPLETE` and its acceptance thresholds, source-authority false-claim gates, five-arm cost comparisons, common V03-native semantics, original neutral nine-case legacy cohort and heldout F1 are still unqualified. The project remains free to redesign **all** physical and organizational levels: file structure, semantic owners, branches, CI/CD, source authority, collaboration and experimental protocols. This review creates no owner physical target, source migration or operative-policy change.

A productive next step is a **bounded fresh-source reference authoring and verification pilot on a prospective cohort**, then a true source-to-answer trial. Limit this to real problem-sized evidence and a fixed completion window rather than indefinite prerequisites. Where a fresh writer cannot access the needed source files or source authority, record the scope limitation and proceed with honestly classified engineering evidence instead of inventing gold.

    ALL_THREE_MASKED_CLAUDE_REVIEWS_COMPLETE=true
    ORIGINAL_QUESTION_COUNT=12
    ORIGINAL_GPT6_PROSE_RESPONSES=24
    ORIGINAL_SOURCE_LINES_MECHANICALLY_VERIFIED=360
    CLAUDE_WHOLE_FULLY_SUPPORTED_B0=10_OF_12
    CLAUDE_WHOLE_FULLY_SUPPORTED_B1=10_OF_12
    CLAUDE_PROPER_ABSTENTION_B0=2_OF_12
    CLAUDE_PARTIAL_B1=2_OF_12
    CLAUDE_EXPLICIT_CLAIMS_SUPPORTED=45_OF_47
    CLAUDE_EXPLICIT_CLAIMS_PARTIAL=2_OF_47
    CLAUDE_FALSE_OPERATIVE_ASSERTIONS=0_OF_24
    INDEPENDENT_REFERENCE_GOLD_CREATED=false
    FORMAL_R0_P03_SCORED=false
    PHYSICAL_ARCHITECTURE_SELECTED=false
