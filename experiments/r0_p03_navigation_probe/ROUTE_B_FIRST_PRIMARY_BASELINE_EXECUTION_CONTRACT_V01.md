# Route B first actual twelve-primary-task execution: source-grounded answer and B0 baseline contract V01

**Date:** 2026-11-13
**Status:** PROSPECTIVELY_FIXED_BEFORE_FIRST_BASELINE_RESULT / IMMEDIATE_EXECUTION_ATTEMPT / PROVISIONAL_NONINDEPENDENT_EVIDENCE
**Owner direction:** The owner explicitly chose Path B, requested actual progress toward running R0-P03, and expressly permitted ChatGPT to write source-grounded reference answers with proportionate independent validation, provided limits are transparent. This record interprets that decision as authorization for a **pragmatic, exposed preliminary attempt**, not as hidden authorization to discard Research 513/559/576's formal numerical gates or change Specification 028.

## 1. What is frozen and what is deliberately not qualified

Before implementing/running the baseline, a source-answer manifest was exclusive-created at
`experiments/r0_p03_navigation_probe/ROUTE_B_PRIMARY_12_SOURCE_ANSWER_MANIFEST_V01.json`, exact **9,784 bytes**, SHA-256 `c628555ef02f87499007ead3420a513cf43080262c7288cd347dc2479b4b0330`. Its twelve explicit, source-grounded reference answers are divided **3/3/3/3** across the original Research 513 primary categories. Every question/answer/source anchor is visible to the coordinating model and therefore **not blind/independent**. No previous C02 private questions/answers are used or claimed.

The four category names map directly to the Research 513 categories, with tests centered on *one explicitly evidenced source* each. The original `>=10/12` PASS rule, nine separately neutral legacy task slots and `>=8/9` gate, zero false-authority gate, `>=0.80` held-out assignment F1, `<=10%` authored metadata churn, deletion/rebuild, B0-B4 arm definitions and decision/complexity rules remain intact for the **future properly qualified formal attempt**. They are **not** scored, waived or deemed failed by this baseline diagnostic.

## 2. Fixed original world, source closure and prospective draw

Read Git original bytes only at pin `47ed6344a9153dcf366769e95722840fbf1a8f8b`; never the mutable worktree, later checkpoint files, C01/C02 private answers or competing arm output. **Pre-first-result erratum:** the first executable attempt aborted without a saved result because the initial path-strata predicate omitted the two manifest-required root records `docs/CURRENT_STATE.md` and `docs/DECISIONS.md`. These two exact root paths are now eligible **only as frozen primary closure**, never as sampled filler; no question, answer, source evidence pin or quota changed. Search eligible actual Git tracked original paths:
- exactly `docs/CURRENT_STATE.md` and `docs/DECISIONS.md` as required primary closure only;
- `docs/research/*.md` directly;
- `docs/checkpoints/*.md` directly;
- `docs/specifications/*.md` directly;
- `docs/foundations/*.md` directly;
- `tools/**/*.py` recursively.

A file is eligible if it meets the literal path-family rule above. Do not infer authority from its path. Exclude files in P03 trial implementation paths, and do not use source-derived status as a deployment fact. No semantic cherry-picking of retrieved results. Original authored reference sources are fixed in the task manifest. Include exactly those **twelve distinct source paths** in the 60-source **build** corpus before sampling filler.

Fill the build corpus using exclusive, hash-ordered group quotas from all other eligible tracked paths:
- **20 research**, **16 checkpoint**, **4 specification**, **4 foundation**, **4 tool code** = 48 filler.
- Order within each family by SHA-256(`R0_P03_ROUTE_B_BUILD_V01|<stratum>|<path>`), then pathname.
- If a family lacks quota, fail rather than quietly substitute or reuse historical results.

Select **20 held-out/maintenance original files**, disjoint from build, from the remaining eligible paths, using SHA-256(`R0_P03_ROUTE_B_HELDOUT_V01|<stratum>|<path>`) order:
- **8 research, 8 checkpoint, 2 specification, 1 foundation, 1 tool**.
- The holdout is drawn under a rule fixed before B0 results, but not withheld from the exposed coordinator; its maintenance F1 cannot be truthfully scored without independently authored subject/concern annotations.

All **80** carrier paths and original source bytes/SHA-256 are persisted. This 60/20 candidate is **provisional**, not the final role-aware/coverage-qualified official corpus required by Research 559; future sample correction must be a new versioned prospective attempt, not post-result editing.

## 3. Actual baseline execution and scoring boundaries

On exactly the same **60-source build** contents, compare:
- `B0_SUBSTRATE_LEXICAL_BASELINE`: source-native full-text SQLite FTS5 BM25 with Unicode61, original content, no extra subject/source-link/concern/semantic index, returned top ten.
- `TITLE_LEXICAL_DIAGNOSTIC`: identical FTS5 on the first source H1/title, *not an official B1*.
- `CHAR_TRIGRAM_DIAGNOSTIC`: sparse character-trigram TF-IDF cosine of source H1 + first 600 body characters, *not embedding B4*.
- `DIAGNOSTIC_THREE_WAY_RRF`: fixed 60-damping rank fusion of these three top-ten lists. This is **not an official B2/B3/B4** arm and has no qualified authority advantage.

For each of the 12 fixed queries the four rankers receive exactly the same natural-language question text and indexed source world. The evaluation-only intended source path, witness and reference answer must never flow into the rankers. The source body is indexed up to the same fixed **12,000 source characters** in all lexical stages; longer docs retain untruncated original bytes/witnesses for reference auditing but are not granted more retrieval context. Each returned source must be a real path@source SHA-256. Use deterministic query token normalization and a fixed non-task-tuned stopword set from previous V04. Top K = 10, report @1/@3/@5/@10, MRR@10, raw 12x4 rankings and missed original paths.

For each source-grounded answer, check all required quoted source excerpts occur **verbatim as contiguous text inside one original source line** (trim only leading/trailing Markdown whitespace from the excerpt). Preserve the entire original matching witness line, line number/content SHA-256 and source body SHA-256. **Second pre-result correction:** the P02 answer manifest excerpt is a sentence embedded inside a longer source line, not the line's entire content; the first validation halted without output. Matching an exact quoted substring on one original line is the documented intended evidentiary check, not fuzzy semantic verification. All twelve questions and source excerpts remain byte-identical. This proves the coordinator-authored answer has **specific evidence anchors**, not that each answer is independently correct or exhaustive. A source citation is required even for candidate findings; a source's self-authored state is not operative authority.

Score **source discovery** only: correct source@K against the exposed manifest's one required source. Do NOT generate user-visible status assertions based only on retrieved document ranking. No 12-task answer correctness/PASS, no formal B0-B4 conclusion, no official R0-P03 result class, no legacy gate or architecture winner. Rather than delaying this diagnostic for missing formal gold, save the complete actual result and carry the limitations into the true score-ready attempt.

## 4. Non-negotiable execution discipline and next actual work

Freeze this method before its result. First B0 execution is undertaken immediately with the existing Python/SQLite/Git toolchain. If a source excerpt is missing or a Git source cannot be read, fail and report; do not silently replace the task. Any method fix before first observed result must be explicitly recorded. Once output exists, no tuning to green. The complete output is exclusive-create; preserve original JSON bytes via `.gitattributes -text`.

**Next execution step after the baseline** must either develop genuine source-grounded B1/B2/B3 additions under the same source/query boundary (not mislabeled title/links proxies), obtain independent source-review of the twelve reference answers, or freeze a separate formal route B scored attempt. Do not spend a new series of unbounded preparation checkpoints or relabel exposed questions as independent.

    PIN=47ed6344a9153dcf366769e95722840fbf1a8f8b
    TASK_COUNT=12
    TASKS_PER_CATEGORY=3
    BUILD=60
    HELD_OUT=20
    REQUIRED_SOURCE_CLOSURE=12
    LEGACY=9_UNCHANGED_UNSCORED
    B0_BASELINE=EXECUTE
    OTHER_ARMS=NONARM_DIAGNOSTICS
    INDEPENDENT_GOLD=false
    CURRENT_AUTHORITY_ADJUDICATION=false
    FORMAL_R0_P03_SCORING=NONE
