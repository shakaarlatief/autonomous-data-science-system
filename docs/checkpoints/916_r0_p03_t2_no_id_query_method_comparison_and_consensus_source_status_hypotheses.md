# Checkpoint 916: Actual no-ID decision retrieval and three-way fusion comparison

**Date:** 2026-11-13
**Status:** REAL_T2_V04_64_CASE_EXECUTION / FOUR_METHODOLOGICAL_RANKINGS_COMPARED / FUSION_NO_GAIN / ORIGINAL_FORMAL_R0_P03_UNSCORED
**Checkpoint class:** EXPERIMENT_VERIFICATION
**Project stage:** R0-P03 execution-first source-referent and recorded-authority semantics testing
**Scope:** Execute 32 manually authored no-ID decision questions over two original source Git revisions, compare matched full-body BM25, heading BM25, sparse character trigram, reciprocal rank fusion, and separate provisional source-status evidence.
**Authority:** Research 653 / Validation 352, exact Git S0 and S1 original decision source, fixed 8668-byte query manifest SHA-256 `d632b334ec39e88f5fcaa2c1761e0b2f7ea2aa4d5b8126df962b092918495d05`, complete 245742-byte original result SHA-256 `327278182a3ea6793ca999be9d5b6e179cdf8bbf89d37bdacdf6f6147773dc1b`. Formal Research 513/559/576 unchanged.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** chatgpt-42
**Conversation title:** 42 - R0-P03 Historical Evidence Qualification and Experimental Readiness
**Primary collaborator:** ChatGPT
**Research:** Research 653
**Validation:** Validation 352

## Executed results and limitations

Actual original Git source sections **35 S0 + 36 S1**. New **32 humanlike but exposed coordinator-authored no-ID question texts**, frozen before method implementation, repeated against both source snapshots (**64** cases). Of those, 51 had a coordinator-intended decision recorded in that snapshot and 13 were absent/unmatched under that coordinator's hypothesis.

Matched source/context retrieval K10: whole-section BM25 **45/51** top1, heading-only BM25 **37/51**, character-trigram TF-IDF **47/51**, three-way RRF **47/51**. The combined RRF **did not improve** top-one/MRR against character ngram alone; both reach 51/51 at top three. The fused method changes which queries miss. Extra character representation requires 2117/2149 features and 11394/11724 document feature weights across snapshots, plus both FTS5 indexes.

A pre-fixed selective source-status evidence gate emitted **29** provisional statuses matching the **exposed author's intended labels**, and abstained on **35** cases, including 13 absent/no-target hypotheses; candidates always remain separately available. A synthetic falsification proves that three rankers can agree on the *wrong referent* and still trigger the gate. Thus this is a **selective and unverified status hypothesis** measure, not proof of real-world accuracy, independent question understanding or operative authority. The previous 65/120 source experiments and this decision ledger are all exposed regression sources; none is suitable for fresh blind architecture scoring.

The actual exclusive-create output is **245742 bytes**, SHA-256 `327278182a3ea6793ca999be9d5b6e179cdf8bbf89d37bdacdf6f6147773dc1b`. First test pass identified one incorrect *test expectation* for a stopword; corrected the test only, saved result unchanged, dedicated **9/9 PASS**. The original formal R0-P03 outcome remains INCOMPLETE, no physical architecture selected or authority/migration changes.

## Next work

Stop trying to turn exposed, self-authored source/query pairs into official independent test gold. Qualify a source- and comparator-separated task authoring path, with independently authored questions and qualified owner/temporal authority evidence, then execute matched capable lexical, metadata, semantic/embedding and hybrid comparisons including operational effort and costs. Until then, use the actual 64-case result as mechanism/falsification regression and treat RRF complexity as a measured tradeoff, not presumed architectural benefit.

    CHECKPOINT_916=REAL_NO_ID_RETRIEVAL_METHOD_AND_SELECTIVE_STATUS
    SOURCE_SNAPSHOTS=35_36_DECISIONS
    QUESTION_CASES=64
    RRF_CORRECT_TOP1=47_OF_51
    NGRAM_CORRECT_TOP1=47_OF_51
    SELECTIVE_ADMISSIONS=29
    SELECTIVE_ABSTENTIONS=35
    EMBEDDING_BASELINE=NOT_EXECUTED
    INDEPENDENT_GOLD=NONE
    FORMAL_R0_P03_SCORE=NONE
    PHYSICAL_TARGET_SELECTED=false
