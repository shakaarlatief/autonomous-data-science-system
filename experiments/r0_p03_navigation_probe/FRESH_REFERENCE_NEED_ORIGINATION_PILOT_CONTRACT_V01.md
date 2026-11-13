# R0-P03 unscored independent need-to-reference pilot V0.1

**Date:** 2026-11-13
**Source world:** original Git commit `47ed6344a9153dcf366769e95722840fbf1a8f8b`, independent of current branch mutations.
**Status:** ONE_SMALL_PATH_INDEX_FROZEN / FRESH_NEED_ORIGINATION_PENDING / FULL_SOURCE_REFERENCE_VERIFICATION_NOT_STARTED / FORMAL_R0_P03_INCOMPLETE
**Scientific role:** source-index-informed, question-first **feasibility pilot**, not the scored primary cohort, not a substitute for the twelve genuinely independent tasks required by Research 513, 559 or 576, and not a candidate selection.
**Owner governance:** no amendment to the owner's accepted formal R0-P03 study, private reviewer authorization, source publication policy or source/physical architecture is implied.

## Purpose and explicit failure mode

We already have three independent-session Claude source-excerpt critiques of twelve **coordinator-authored** questions and 24 exposed GPT-6 answers. That result is helpful evidence about answer grounding, not independent reference truth. Historical independently originated C02 needs, when checked against limited available original evidence, previously produced **zero fully closed source-supported cases** (Research 641). An unqualified new question writer without source-world orientation would risk repeating unanswerable cases, while a writer who first reads full answer-bearing source texts could cherry-pick trivial questions. This small experiment deliberately tests a middle path: **path-only neutral source orientation, then question origination, then separately qualified full-source reference review, without replacing difficult or unanswerable cases**.

The path-only orientation index is constructed with a fixed, deterministic SHA-256 order over path and immutable Git blob identity. It contains **ten original source paths per family** for Foundation, Specification, Research, Checkpoint and Validation, plus two historical `CURRENT_STATE`/`DECISIONS` orientation anchors, **52 source paths total**, from original Git. It contains **no source body**, original answer, previous model answer, rubric truth, branch-head live source, reviewer score or B0/B1 mapping. Historical filename/path meanings are only source *hints*, not verified authority.

**This index is not a representative sample of actual user questions, not a source closure, and not an arm-equivalent source corpus.** It is a bounded prompt context for an unscored feasibility check. The separate subsequent adjudicator may need full original Git evidence well beyond those 52 index paths; failing to find complete original evidence must be recorded as HOLD.

## Sequence and source-exposure contract

**Step 1, next action: new independent NEED_ORIGINATOR session.** Start Claude Code with a new conversation. Show it only this contract, MC-0030 Message 072 and the exact frozen path-only index. Do not expose previous twelve questions/answers, Claude Messages 067/069/071, the original R0-P03 model results, selected original source bodies, project memory or model-authored reference answers. Acknowledge and record auto-injected runtime information (repository branch/commit subjects may appear). The author must not execute Git source reads, searches, or web browsing. It authors **exactly four provisional needs**, one per each of Research 513's four primary task families, in fixed order:

    N01: COLD_START_CURRENT_ORIENTATION
    N02: CROSS_PLANE_DISCOVERY
    N03: IMPACT_ANALYSIS_ARCHITECTURE_EVOLUTION
    N04: EXACT_SOURCE_AUTHORITY_RECOVERY

Each needs an actionable, answer-seeking question (not merely the name of a file, a status-header trivia lookup, or a variant of an existing known answer), a realistic user purpose, the evidence that would have to be seen to justify a full answer, a concrete authority/time risk, and a declared `EVIDENCE_UNASSESSED` state. Do not write answers, source-body quotations, fabricated sources, inferred outcomes or an invented complete evidentiary chain. If a meaningful source-index-grounded question cannot be constructed for any category, keep its fixed slot and report `ORIGINATION_HOLD` plus a reason. Do not substitute an easier category or compensate later.

**Step 2, only after Step 1 original bytes and SHA are frozen: separate fresh REFERENCE_ADJUDICATOR session.** The need author must not review, grade or resolve its own four questions. That reviewer receives the same four frozen questions and a **read-only original Git source view** of the entire admissible historical source world, not B0/B1 answer excerpts. Reviewer must provide exact path@original-blob ID, original line witnesses and evidence lineage and distinguish a source's *own claims* from verified implemented/owner/CI evidence. Record `SUPPORTED`, `PARTIAL`, `HOLD_INSUFFICIENT_ORIGINAL_EVIDENCE` or `NOT_IN_SCOPE` as justified, preserving failure. Bound original-document reads and source-search scope before reference inspection in a separate explicit handoff, so the reviewer cannot indefinitely search to make every case appear answerable. Keep any source-specific completed reference answers in a protected or local-only output outside shared/public arm-visible Git, with exact custody disclosure. If this cannot be done, stop at an unscored source-feasibility classification rather than claim independent gold.

**Step 3, after both roles conclude:** independently verify complete source-line provenance, classify source reliability/answerability and compare only as a **pilot**, not as official Research 513 scores. Do not tune existing B1/B2/B3, change exposed twelve model answers, or score official B0-B4 arms against a reference that their authors can see. Separate a properly verified `UNKNOWN` answer from a source search that simply gave up.

## Predeclared success and stopping criteria

The pilot's useful output is the **number and reason** of four candidate needs that produce objectively checkable, historically time-scoped original-source reference answers under the same prescribed source-review budget. An honest `0/4`, including why original evidence is missing, is a complete pilot observation. Do not swap a HOLD for a trivially supported question or claim the pilot's completion satisfies the formal independent 12-case primary / neutral nine-case legacy / heldout maintenance and parity gates. No score on any architecture is authorized by this contract.

    FIRST_ROLE=FRESH_QUESTION_ORIGINATOR
    PILOT_NEED_SLOTS=4
    ELIGIBLE_SOURCE_INDEX_PATHS=52
    INDEX_CONTAINS_SOURCE_TEXT=false
    INDEX_CONTAINS_REFERENCE_ANSWERS=false
    PRIOR_R0_P03_ANSWER_RESULTS_AVAILABLE_TO_AUTHOR=false
    SECOND_ROLE=SEPARATE_FULL_ORIGINAL_SOURCE_ADJUDICATOR_PENDING
    ANSWERABLE_REFERENCE_CASES=UNKNOWN
    FORMAL_R0_P03_SCORING_ALLOWED=false
    OWNER_PHYSICAL_ARCHITECTURE_SELECTION=false
