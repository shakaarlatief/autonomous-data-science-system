# Execution-first 65-heading mechanical query generalization stress test, V01

**Date:** 2026-11-12
**Status:** METHOD_FIXED_BEFORE_EXECUTION / REAL_HISTORICAL_DOCUMENT_LOCATOR_TEST / NOT_PRIMARY_R0_P03_GOLD
**Purpose:** Improve on the prior nine W5-T1 B1-authored scenario labels without repeating unbounded private historical witness review. This is a second exploratory query family with mechanically generated answer targets from source-local text.

## Fixed source world and query generation

Same exact 65 authored-annotation corpus paths and real historical Git commit `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef` as prior pilot, with source bytes read from pinned Git objects, not current working files. This is not a representative whole-ADS source-world release.

For **every** one of the 65 source documents, extract the **first nonempty Markdown level-one heading** matching a literal `# ` prefix and strip surrounding whitespace. Use the complete heading as one natural-language document-location query. The correct target is **that same exact historical source document**. No manual source selection, query editing, task exclusion, paraphrase invention, tie-breaking against results, alternative source matching or omission. First-heading uniqueness and existence are verified; failure stops the pilot. The query generator cannot see the legacy nine gold sets or their B1 subject IDs.

This is a **known-content document-location query test**, NOT a source-independent user question about history, execution, authority, recovery or context reasoning. Because headings occur verbatim in source documents, it may favor lexical text retrieval, and the correct target is mechanically known without independent reference adjudication. All three mechanisms use the same complete heading text and same exact document corpus. No original C01/C02 restricted file enters this test.

## Three executable retrieval mechanisms, no oracle/topic hint

- **B0-like full text:** FTS5 `unicode61` with existing B0 literal OR query tokenization and BM25 ordering on the full 65-document text corpus; output the first up to **ten** matched documents. If fewer than ten documents match, do not fabricate nonmatching results.
- **B1-like human-language subject routing:** derive candidate subject from the **same query text only**, using the existing W5 subject catalog. For each assignable subject calculate number of unique content tokens overlapping its human-readable label and its `description`. Choose the unique tie-broken subject with the most label overlaps, then description overlaps and lexical ID; route only when at least one label term and at least two total label+description overlaps occur. Otherwise fall back to B0. With a chosen subject, rank its authored subject-member carriers by preferred-subject membership, shared BM25 ranking, then stable path and fill unused slots from B0 matches, maximum ten. No scenario ID, target path, gold label or manually assigned query subject provided to B1.
- **B2-like literal-citation proxy:** same extraction and one-hop reference rule as the previous executed V01 citation proxy: start with up to five B0 matches, follow exact directed `docs/` path mentions within the 65-carrier corpus, sort by citing-seed frequency then shared BM25 match rank then stable path, append link targets up to ten, fill remaining slots from subsequent B0 matches. Do not promote path references into governed editorial or source-authority links.

B1 and B2 differ in added information: B1 has prior human-authored subject metadata and catalog; B2 only extracts path mentions from source bodies. Both have the exact same heading query and lexical FTS5 engine. They are not complete Research 513 B1/B2 arms. B3 governed concern facets and B4 semantic retrieval remain unimplemented.

## Fixed metrics and interpretation

For each of 65 heading queries, evaluate exact source path of the target document at ranks one to ten, reciprocal rank@10 and returned count. Aggregate hit@1, hit@10, MRR@10, returned slots, selected/fallback B1 topic routes, citation edges. Record all source headings and ranked path traces in a versioned public exploratory JSON.

As a negative/robustness control, compare the new query family to the already observed nine-topic scenario results without changing the latter. No model-generated answer scoring or architecture selection. No manual adjustment after scores. Rerun exact full output for deterministic parity.

Limitations to disclose: these headings are not independent human tasks; the 65 source files and B1 annotations are the same nonblind research corpus, and B2 is only a literal-mention proxy. An exact document-locator test is not historical semantic answerability or verified authority. Its value is testing the sensitivity of compared retrieval mechanisms to a fundamentally different, mechanically generated query family, including potential B1 over-specialization to known subject labels.

    SOURCE_SET=EXACT_W5_T1_V02_HISTORICAL_65
    QUERIES=65_COMPLETE_FIRST_H1_HEADINGS
    QUERY_TARGET=SELF_EXACT_HISTORICAL_SOURCE_PATH
    TOP_K=10
    GOLD_FROM_B1_AUTHOR=NO
    SUBJECT_ID_SUPPLIED_TO_B1=NO
    REAL_B2_EDITORIAL_SEMANTICS=NO
    ORIGINAL_R0_P03_PRIMARY_GOLD=NONE
    SCORING=EXPLORATORY_DOCUMENT_LOCATION_ONLY
