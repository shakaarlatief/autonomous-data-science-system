# Research 658: Actual source-cited extractive answer reconstruction and evidence-completeness comparison

**Date:** 2026-11-13
**Status:** TWELVE_PRIMARY_TASKS_SEVEN_ARMS_EIGHTY_FOUR_EXTRACTIVE_DRAFTS_ACTUALLY_GENERATED / ALL_ORIGINAL_CITATIONS_VERIFIED / EVIDENCE_COMPLETENESS_DISCRIMINATED / COMPLETE_SEMANTIC_ANSWER_GOLD_NOT_QUALIFIED
**Scope:** Owner-approved pragmatic Route B continuation of actual R0-P03 navigation experiments, testing original-source line-cited extractive answers across seven previously executed retrieval routes on twelve frozen primary tasks.
**Research boundary:** Owner-approved pragmatic Route B continued actual R0-P03 navigation experiments. This is a real, bounded *source-to-answer* mechanism run, **not** a fresh-model whole-answer adjudication and **not** original Research 513/559/576 formally scored B0–B4.
**Source/authority:** Frozen Checkpoints 918–920 and exact source revision `47ed6344a9153dcf366769e95722840fbf1a8f8b`; fixed twelve coordinator-authored source-grounded questions, sixty actual original Git build carriers, twenty excluded heldouts, immutable original B0/B1/B2/B3/classical LSA outputs, before-result extractive method contract.
**Checkpoint:** 921. **Validation:** 357. **Session:** chatgpt-42.
**Safety:** No source status is promoted to owner-signed or current operative authority. The protected C01/C02 cohort and historical nine-case reference packet are not accessed.

## 1. Why source retrieval accuracy is not yet enough

Checkpoints 918–920 executed the original twelve exposed primary questions against a fixed source world, implementing actual B0 lexical retrieval, B1 historical subject vocabulary with exposed source-adjacent membership, B2 original source-written link navigation, B3 exposed selective concerns, and a true classical word-distributional LSA embedding. These experiments established which candidate documents were retrieved, but did **not** establish whether an agent could quote the correct original evidence or avoid adding unsupported claims when attempting an answer.

An answerable query such as "Where is the accepted decisions register and can decisions be revised?" has at least two substantive pieces. A top-one correct file is necessary but not sufficient if the assembled answer drops the original statement that project decisions may be revised. Conversely, a retrieved source with an `**Status:** Accepted` header is a *historical source statement* and does not prove current deployment.

This checkpoint therefore executes a **deterministic source-bound extractive answer generator** over the existing frozen rank lists. It is deliberately more stringent than required-source@3 retrieval and deliberately weaker than full answer correctness. It is *not* a simulated ChatGPT/Claude answer. Its text is a quote-forward answer draft that can support later independent review, with citations that can be mechanically reproduced from original Git.

## 2. Prospectively frozen and original-source-equal answer contexts

The method was committed as `ROUTE_B_PRIMARY_EXTRACTIVE_ANSWER_EVIDENCE_CONTRACT_V01.md` in the working source corpus **before the first comparative output** and first runner execution. The four existing inputs are exact original immutable records:

| Input | Exact bytes | SHA-256 |
| --- | ---: | --- |
| Twelve questions / coordinator draft reference answers | 9,784 | `c628555ef02f87499007ead3420a513cf43080262c7288cd347dc2479b4b0330` |
| First B0 source ranking and original Git 60/20 roster | 122,682 | `59ab36aef96046f71e2ccacbcc2105918ab19ed4bbc1f013e9bb78539a9bd4ab` |
| Distinct B1/B2/B3 original source ranking experiment | 92,547 | `6a2b656432a5b8fbb963b0e8c14220411ed57bbad6127b8a550c05cf93ee0fa2` |
| Classical corpus-trained LSA16 B4 candidate ranks | 154,662 | `59fd12cc78892bf6f97cde88e44fc692729582560011bf81a55f1fc62af0b00f` |

For **each query and method**, the generator receives exactly the method's **three highest-ranked original source carriers**. Each source is visible only up to its first **12,000 original characters**; truncated final source lines are excluded to prevent misquoting. The generator examines the first **35** whole, nonempty, out-of-fence candidate lines; picks the first original H1 plus at most **four** other source lines using the same question-token overlap and frozen field bonuses across every arm; and cites every original complete line with exact path, blob SHA, line ordinal and line SHA. A source's quote line may be at most **550** characters. No answer text, intended source ID, gold witness snippet or retroactive relevance label enters the renderer.

The resulting attributed draft lists original text of up to three retrieved carriers and explicitly says these are not independently verified complete answers or proof of current operative authority. Contradictory sources remain separately attributed rather than silently merged. There is no task-specific status hardcoding, per-arm intervention or post-result quote tuning.

Only **after all 84 draft texts have been generated and source SHA/line checks verified**, a second evaluation-only phase reads the previously frozen exposed reference manifest. It checks whether the one source expected by the previous coordinating model is present in the top three, whether its exact reference quotations were available in the 12,000-character source window, and whether **all** those source-specific excerpts were actually selected/cited in the generated draft. The prior reference answer text is not compared for semantic entailment or promoted to independently correct gold.

## 3. Actual frozen observed results

The first comparative execution succeeded and exclusively created the complete original result:

    FILE=experiments/r0_p03_navigation_probe/route_b_extractively_cited_answer_evidence_result_v01.json
    ORIGINAL_BYTES=995317
    ORIGINAL_SHA256=17f5bae16a96530008ea954e7145e3903e25386d83eeee7e69b983de91b908f8
    FIXED_PRIMARY_QUERIES=12
    PREVIOUSLY_EXECUTED_METHODS=7
    ORIGINAL_EXTRACTIVE_DRAFTS=84
    SOURCE_RECORDS_CITED=252
    ORIGINAL_LINES_SHA256_REVERIFIED=1260
    DRAFT_CHARACTERS=251190
    SOURCE_BUILD=60
    SOURCE_HELDOUT=20_EXCLUDED
    REFERENCE_AUTHOR_IS_INDEPENDENT=false
    SEMANTIC_ANSWER_CORRECTNESS_SCORED=false

| Actual frozen method | Required original source among top 3 | Every required excerpt available in permitted source context | Every required reference excerpt actually quoted |
| --- | ---: | ---: | ---: |
| **B0 original whole-body BM25** | **10/12** | 10/12 | **9/12** |
| B1 exposed source-subject + B0 | **11/12** | 11/12 | **10/12** |
| B2 source-written-link + B0 | 10/12 | 10/12 | 9/12 |
| B3 exposed selective concerns + B0 | 9/12 | 9/12 | 8/12 |
| B4 true classical LSA16 dense only | 7/12 | 7/12 | 7/12 |
| B4 classical LSA16 + B0 RRF | 9/12 | 9/12 | 9/12 |
| B4 classical LSA16 + B2 RRF | 9/12 | 9/12 | 9/12 |

These are **exposed, retrospective quote-evidence-completeness metrics**, not full natural-language answer PASS rates. They are more demanding than source@3 because even when the source is retrieved, the answer renderer must actually select all reference-supporting original lines. Source identity and reference excerpts were authored by the same exposed coordinating model, so no independent truth or universal architecture efficacy follows.

## 4. Actual discriminating failures and improvements

**P01, historical state/branch:** B0 does not retrieve `docs/CURRENT_STATE.md` in its top three; B1 restores it and quotes both the archived Checkpoint 899 and the active development branch correctly. B3 and classical LSA alone do not recover it in the same budget. This is a *genuine provenance-backed B1 evidence-reconstruction benefit* on an exposed case, not proof that every source should have the new subject annotation.

**P02, owner decisions register:** The correct `docs/DECISIONS.md` is B0 **rank one**, and both source-backed reference statements fit within the 12,000-character context. The generic lexical evidence selector nevertheless includes the source's H1 and the paragraph describing possible revision but **drops the opening declaration establishing that the file is the project decisions register**. This is the clearest evidence that correct document retrieval is not sufficient to reconstruct a complete answer. The experiment records **`REFERENCES_ACCESSIBLE_NOT_ALL_QUOTED`**, not a false PASS. Changing its four-line quote budget after seeing this failure would invalidate the already fixed comparison.

**P03, implementation status of Specification 028:** B0 and B1 do not retrieve the required original specification within their first three source candidates. B3 does and quotes the original `FROZEN / IMPLEMENTATION PENDING` evidence. This illustrates that alternative metadata can help some source cases even while reducing aggregate performance. We do not tune source labels or rerank P03 after observing it.

**P05 and P08:** B0 quotes the original full reference evidence, while some structured metadata variants displace the actual source. For P08, the retrieved Research 512 source includes both the reconciled `GOVERNED_LEDGER_KERNEL_V02` candidate and its original historical `OWNER DECISION NOT READY`/candidate-only status; there is no claim of an accepted physical target.

**Classical B4:** LSA-alone has required source in top three for seven of the twelve exposed questions, and all seven selected original reference excerpts happened to be quoted. The combined LSA+B0 and LSA+B2 routes reach nine, below B1's ten. This is about the specific classical corpus-trained LSA16 model, not a modern pretrained neural embedding; no claim about the unavailable neural B4 is supported.

## 5. Evidence construct and strictly limited authority claims

The pipeline validates every emitted quotation against the exact original Git bytes and original line hash. It does **not** validate that those lines are true in the world, that the proposed reference answer includes every applicable historical source, that different original records are reconciled in the correct temporal order or that a historical source's wording is an operative owner acceptance.

There are three distinct necessary conditions:

1. **Discovery:** the source whose contents support an answer must be retrieved within the common source budget.
2. **Evidence extraction:** the relevant original witness lines must survive the context restriction and be selected for the attributed answer draft.
3. **Semantic interpretation and authority:** a genuine reasoning agent must determine what those witnesses establish, handle conflict and supersession and refrain from unsupported present-day status assertions.

This checkpoint actually tests the first **two**, including source-byte integrity and exact original line citations. It does **not** score the third. Claiming "9/12 full answers correct" would be scientifically false. The source-only deterministic renderer is a conservative quoted evidence supplier, and must not be mislabeled a fresh-agent LLM answer.

The locally installed Claude Code CLI (`2.1.283`) was probed with a no-tools, no-session-persistence, prompt-only readiness request. The bounded Windows bridge call **timed out** before a valid Claude result; thus this run did **not** complete a separate independent reference answer review. No extra instructions, credentials or sandbox escape were used. The absence of that reviewer is recorded rather than hidden.

The previous C02 independent cohort remains **unresolved and protected**. The separately neutral nine-case historical W5 primary legacy method remains unexecuted, and Research 513 original `>=10/12`, `>=8/9`, zero false-authority and metadata-maintenance/fairness gates are **not waived or scored**.

## 6. Next efficient advance

The executed comparisons now expose the next exact problem: **source evidence is not the same as answer entailment**. The next bounded advance should be a source-limited *actual reasoning-model* reconstruction and proportionate fresh answer review, if a model endpoint can be accessed through authorized channels without granting hidden answers to the author. A qualified reference reviewer should assess which parts of each full coordinator draft answer are truly supported by original source scope (especially multi-clause answers), not simply repeat the existing reference excerpts.

Until such an agent/reviewer can be run, the sixty original source/answer drafts provide a reproducible mechanical answer-extraction basis. Repeating more exposed keyword questions or adjusting quote-budget hyperparameters on the current twelve would primarily tune to disclosed test cases and would not improve scientific independence.

No physical architecture, current repository workflows, source file layout, source authority or migration plan is selected or fixed by this method. All architecture levels remain open to evidence-based change.

    ORIGINAL_R0_P03_FORMAL_OUTCOME=INCOMPLETE
    ORIGINAL_GIT_PIN=47ed6344a9153dcf366769e95722840fbf1a8f8b
    ACTUAL_EXTRACTIVE_ANSWER_DRAFTS=84
    VERIFIED_ORIGINAL_CITED_LINES=1260
    B0_ALL_REFERENCES_QUOTED=9_OF_12
    B1_ALL_REFERENCES_QUOTED=10_OF_12
    B2_ALL_REFERENCES_QUOTED=9_OF_12
    B3_ALL_REFERENCES_QUOTED=8_OF_12
    B4_CLASSICAL_LSA_ALL_REFERENCES_QUOTED=7_OF_12
    B4_CLASSICAL_LSA_PLUS_B0_ALL_REFERENCES_QUOTED=9_OF_12
    REAL_INDEPENDENT_SEMANTIC_ANSWER_REVIEW=false
    FULL_NATURAL_LANGUAGE_CORRECTNESS_SCORE=NONE
    ARCHITECTURE_SELECTED=false
