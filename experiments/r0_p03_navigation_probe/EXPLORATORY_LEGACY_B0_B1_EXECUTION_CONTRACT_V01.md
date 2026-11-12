# R0-P03 execution-first exploratory legacy retrieval comparison, V01

**Date:** 2026-11-12
**Purpose:** Respond to the owner's explicit decision to perform a real test now, despite incomplete prospective source/reference qualification, by running a bounded real retrieval comparison rather than extending historical source review.
**Status:** PREEXECUTION_METHOD_FIXED / LEGACY_PILOT_ONLY / ORIGINAL_R0_P03_SCORED_EXPERIMENT_STILL_HOLD
**Authority boundary:** This is not an amendment to Research 513, 559 or 576, Specification 028, C01/C02 original questions, original reference freeze or scored B0–B4 architecture selection. Do not present any pilot number as a preregistered architecture result.

## Fixed executable comparison

Use real, frozen W5 T1 V0.2 legacy fixtures under `experiments/project_knowledge_subject_navigation_t1_v02/`. Nine existing published research navigation scenarios and sixty-five historical original text carriers, all read from the fixture's exact pinned source commit, are compared. The previous W5 report already used these scenarios and this subject index, so this is a **known, nonblind, nonfresh** pilot. It is meaningful as executed engineering behavior, but does not replace a blind primary experiment.

Two actually implemented retrieval mechanisms:
- `B0-like`: same-carrier full-text SQLite FTS5/BM25, literal OR terms from the human-readable subject label; no access to subject memberships.
- `B1-like`: uses the existing authored semantic-subject memberships; eligible member carriers are ordered by preferred-subject match then by the same label-query FTS5 relevance ranking, then stable path. Exact subject membership is the explicit treatment difference; metadata authoring cost is **not equal** or benchmarked here.

Both use the same human-readable label query, same exact sixty-five original bytes and maximum returned carriers of **ten per scenario**. The authored subject ID is available to B1's semantic lookup and is part of the treatment. Query tokens, ranking, stopwords, frozen source paths, and score definitions are fixed in `exploratory_legacy_b0_b1_live_comparison.py`. No subsequent tuning, hand-written query simplification, dropped cases or B1 membership edits in response to pilot outcomes.

Only after both outputs are produced does the scorer consult each frozen scenario's preexisting `must_retrieve` and `must_not_retrieve` path sets. Report strict complete scenario pass, micro/macro recall@10, explicit negative intrusions, and total returned carriers. These are **retrieval**, not answer correctness, false-authority claims, lifecycle correctness or source admission. This is a genuine measured B0-like/B1-like comparison, **not** actual fully equalized B0–B4 and not full Research 513 nine-legacy score admission.

There is no B2, B3 or B4 trial in this run. They must not be represented as tested. The old C01/C02 protected questions, old held source-specific reports, and reference gold are outside all inputs. No external web, connected apps, new source admission, independent adjudicator, private owner ZIP or trial results from future revisions.

## Execution rule

Exactly one complete run on the fixed fixture; preserve a deterministic JSON trace with per-scenario retrieved carrier paths (all public legacy fixture data), results, source revision, input content fingerprint, method labels and limitations. Validate the script and result without tuning. Report **actual** results, including if the lexical baseline or metadata intervention performs poorly. If execution fails, report the failure, repair only a mechanical runtime defect and document it.

A successful run demonstrates an implemented, reproducible, limited navigation comparison. It **does not** unfreeze the prospective primary source/answer cohort, fulfill the 12-primary/3-per-category or nine-legacy preregistration, or authorize physical architecture target selection.

    OWNER_INTENT=ACTUAL_TEST_NOW
    LEGACY_PILOT_B0_LIKE_VS_B1_LIKE=EXECUTE
    ORIGINAL_R0_P03_RESEARCH_513=UNSCORED_HOLD
    PRIMARY_ADMISSIONS=ZERO
    PRIVATE_C01_C02_CASES_ACCESSED=FALSE
    SCORED_ARCHITECTURE_SELECTION=NONE
