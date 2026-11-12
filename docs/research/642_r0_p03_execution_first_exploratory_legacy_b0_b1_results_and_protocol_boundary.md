# Research 642: Actual execution-first B0-like vs B1-like historical navigation pilot

**Date:** 2026-11-12
**Status:** REAL_EXPLORATORY_LEGACY_COMPARISON_EXECUTED / B0_LIKE_1_OF_9_B1_LIKE_9_OF_9 / ORIGINAL_R0_P03_SCORE_GATE_UNCHANGED
**Scope:** Record an actual reproducible historical source-retrieval comparison requested by the owner and distinguish it from the original preregistered R0-P03 architecture-selection experiment.
**Authority:** Owner explicitly prioritized an actual test even at reduced methodological robustness; actual executed pinned-source legacy experiment output. Research 513, 559, 576, 641 and prior W5 Research 217 remain unchanged.
**Checkpoint:** 905. **Specification:** 028 unchanged. **Interaction:** ChatGPT / chatgpt-42.

## 1. What was actually executed

The project has now run a real **engineering comparison**, not just another corpus sufficiency audit. The fixed contract and executable implementation were authored before the first recorded result:

    experiments/r0_p03_navigation_probe/EXPLORATORY_LEGACY_B0_B1_EXECUTION_CONTRACT_V01.md
    experiments/r0_p03_navigation_probe/exploratory_legacy_b0_b1_live_comparison.py

The actual immutable output is:

    experiments/r0_p03_navigation_probe/exploratory_legacy_b0_b1_live_result_v01.json
    EXACT_BYTES=18712
    SHA256=498bb12d906639642da943e8366194ec8b0c7f6817d20ae5b8fa89a43f8a2acb

**Real source data:** 65 real UTF-8 historical repository documents read from Git revision `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef`, not mutable current working copies. The exact 65-carrier set comes from original W5-T1-V02 annotated research fixture. All nine existing legacy research scenarios have pre-recorded must-retrieve and explicit must-not-retrieve examples inside those 65 carriers. All original question/gold files from C01/C02 remain inaccessible to this pilot, unmodified and unused.

**Both retrieval approaches receive** the same real 65 historical documents, the same natural-language human subject-label query for each scenario and the same limit of ten returned carriers. The treatment difference is deliberate:

- **B0-like:** in-memory SQLite FTS5 lexical full text; Unicode tokenization with literal-term OR query; BM25 ranking; no subject memberships.
- **B1-like:** existing authored V0.2 semantic-subject memberships limit the eligible carriers; previously authored preferred subject gives priority, followed by shared full-text BM25 relevance and stable path order. This explicitly relies on pre-authored metadata, not automatically inferred semantics.

The scorer then evaluates the two retrieved lists against the unchanged known W5 legacy `must_retrieve` and `must_not_retrieve` paths. Passing a scenario requires **all** positives in the top ten and **none** of its explicit negative examples. Additional independent relevance or lifecycle labels do not exist in this fixture. Repeated execution of the fixed script produced exactly the same result JSON without mutating source files or scores.

## 2. Observed experimental numbers

| Actual metric | B0-like lexical | B1-like authored subject navigation |
| --- | ---: | ---: |
| Strict complete-scenario PASS (9 scenarios) | **1/9** | **9/9** |
| Relevant source instances retrieved at top-10 (39 opportunities) | 28/39 | 39/39 |
| Micro recall@10 | 0.717949 | 1.000000 |
| Macro recall@10 | 0.738889 | 1.000000 |
| Explicit negative example intrusions | 4 | 0 |
| Source carrier slots returned across nine scenarios | 90 | 51 |

The result demonstrates genuine deterministic retrieval behavior: on this fixture, source-authored subject memberships and preferred routes substantially improve finding the previously labeled relevant sources, with fewer irrelevant explicit examples and fewer returned carrier slots.

**Interpretation limits are material:** these nine scenarios were originally developed and previously evaluated against the authored W5 subject arrangement (Research 217 already reported 9/9 candidate scenario passes and 4/9 legacy topic passes). The new test adds an actual same-source BM25 lexical comparator, but is neither blind nor fresh. B1's annotations have sunk human authoring effort, while B0 has no equivalent semantic enrichment. The B1 query additionally accesses the frozen subject ID as its treatment. The published labels are not independently adjudicated new user queries and may favor B1. Full recall of 39 labels is not proof of factual answers, source authority, provenance, decision correctness or repeatable improvement on unseen queries.

B0-like and B1-like are **deliberately not** complete Research 513 arms with all nine shared capability contracts. They have no real-equalized B2 editorial-links arm, no B3 concern-routing arm, no B4 learned/embedding arm, no protected novel 12-primary gold, no held-out maintenance scoring, no authority reasoning and no architectural selection. Do not upgrade these nine exploratory scenario passes into the original R0-P03 `>=10/12` primary viability or `>=8/9` independently qualified legacy PASS gate.

## 3. What the owner's execution-first decision changes

The owner is right that indefinite C01/C02 original-source reviews were delaying observable engineering evidence. This pilot ends a literal **zero empirical comparisons executed** state in the narrower exploratory sense: at least one real pinned-source, multi-mechanism navigation measurement and a repeat pass have now occurred.

It does not end the original scored-test hold. The issue is not that there is no task *of any kind* to test: the legacy 9 tasks demonstrably run, and the project has many stable historical, mechanically checkable source witnesses. The problem is the *particular* prospective historical C01/C02 12-task **full as-stated answer/authority reference closure** requirement, which remains unqualified. A scientifically honest project should run bounded exploratory pilot comparisons earlier while separately deciding what independent evidence suffices for architectural selection.

**Recommended execution-first continuation:** Use a small, strictly defined comparability and reference package that can be executed, explicitly preserving limits. Prioritize broadening the runnable pilot beyond reused W5 labels with independent withheld or mechanically constructed tasks and genuine B2/B3 features *only when actually implemented*, rather than claiming B2/B3 performance from imagined designs. Separately, qualify or prospectively amend Research 513's primary task/source-world rules before representing any result as final R0-P03 architectural-selection evidence. A methods design must have a concrete run exit condition and a fixed stop decision; no repeated indefinite cohort origination.

Do not mutate original C01/C02 questions, source ceilings or dispositions. Never give scored treatment arms the protected original adjudicator reports or gold. No physical migration/authority switch is authorized by these pilot scores.

    PILOT_STATUS=ACTUAL_EXECUTED_AND_DETERMINISTICALLY_RERUN
    PILOT_SCENARIOS=9_LEGACY_PREVIOUSLY_USED
    PILOT_HISTORICAL_CARRIERS=65
    B0_LIKE_STRICT_PASSES=1
    B1_LIKE_STRICT_PASSES=9
    B0_LIKE_MICRO_RECALL=0.717949
    B1_LIKE_MICRO_RECALL=1.000000
    PILOT_GENERALIZATION=NOT_ESTABLISHED
    ORIGINAL_R0_P03_12_PRIMARY_ADMISSIONS=0
    SOURCE_ADMISSIONS=0
    REFERENCE_GOLD=NONE
    COMPLETE_B0_B4_COMPARISON=NOT_EXECUTED
    NEXT=EXECUTION_FIRST_BOUNDED_PROSPECTIVE_COMPARISON_METHOD_AND_ARM_SCOPE_DECISION
