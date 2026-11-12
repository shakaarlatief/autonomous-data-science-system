# Checkpoint 905: Executed real historical navigation pilot, B0-like versus B1-like

**Date:** 2026-11-12
**Status:** EXPLORATORY_LEGACY_B0_B1_ACTUALLY_EXECUTED / B0_1_OF_9_B1_9_OF_9 / FORMAL_R0_P03_UNSCORED
**Checkpoint class:** EXPERIMENT_VERIFICATION
**Project stage:** R0-P03 execution-first exploratory navigation pilot alongside formal source/reference qualification
**Scope:** Record actual executed real-document comparative retrieval metrics with clear limits, preserving the formal preregistered architecture-scoring hold.
**Authority:** Executed pilot fixed source/read-only retrieval and output artifact; Research 642, Validation 341; existing R0-P03 Research 513/559/576 and W5 Research 217 remain unchanged.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** chatgpt-42
**Conversation title:** 42 - R0-P03 Historical Evidence Qualification and Experimental Readiness
**Primary collaborator:** ChatGPT
**Research:** Research 642
**Validation:** Validation 341

## Actual test result

Ran an execution-first, nonblind, previously used public W5-V02 legacy fixture: nine fixed navigation scenarios and 65 real historical Git documents at revision `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef`. Compared common-source text-only FTS5 BM25 versus existing authored subject memberships with preferred-subject and common lexical ordering. At top 10, **B0-like 1/9 strict scenario PASS, B1-like 9/9**; micro relevant-source recall **28/39 versus 39/39**; explicitly negative document intrusions **4 versus 0**; total returned carrier slots **90 versus 51**.

Full persisted executed trace is 18,712 bytes, SHA-256 `498bb12d906639642da943e8366194ec8b0c7f6817d20ae5b8fa89a43f8a2acb`. An actual second run recomputed identical data. B1's previous membership construction and prior use of the same scenario labels make the pilot nonblind and authoring-unequal. Do not treat this as scientific proof of out-of-sample dominance, actual Project/Product answer correctness or R0-P03 B0–B4 architecture selection.

## What is now open for a clear owner decision

There is real executed comparator behavior to inspect. The original C01/C02 twelve-primary reference packet remains unadmitted; no fully equalized B0–B4 arms have run. The owner explicitly prefers moving toward actual executable comparisons rather than indefinite research gating.

The immediate bounded continuation is to choose whether to broaden a **real small exploratory comparison** with independent, withheld evidence-verified queries and implemented B2/B3 features, while continuing prospective protocol qualification before formal scored architectural selection. Do not represent exploratory results as fully preregistered primary outcomes, and do not silently weaken Research 513's acceptance thresholds.

    CHECKPOINT_905=EXPLORATORY_REAL_RETRIEVAL_COMPARISON_EXECUTED
    ACTUAL_HISTORICAL_SOURCE_COUNT=65
    ACTUAL_LEGACY_TASK_COUNT=9
    B0_LIKE_FULL_SCENARIO_PASSES=1
    B1_LIKE_FULL_SCENARIO_PASSES=9
    RESULT_BYTES=18712
    ORIGINAL_R0_P03_PRIMARY_SOURCE_ADMISSIONS=0
    ORIGINAL_R0_P03_ARCHITECTURE_DECISION=NONE
    NEXT=EXECUTION_FIRST_FOLLOW_UP_SCOPE
