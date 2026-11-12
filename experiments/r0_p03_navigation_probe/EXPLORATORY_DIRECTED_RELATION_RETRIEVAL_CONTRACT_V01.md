# Exploratory directed-reference retrieval and negative-evidence control, V01

**Date:** 2026-11-12
**Status:** SOURCE-DERIVED_QUERY_POPULATION_AND_ARM_RULES_FROZEN_BEFORE_FIRST_SCORE / EXPLORATORY_ONLY
**Context:** Execution-first continuation from Checkpoints 905-908. No C01/C02 protected files, source admissions, or official R0-P03 score are authorized.
**Question:** Can explicit directional reference retrieval, and combinations respecting its absence of evidence, satisfy document-reference information needs that lexical, subject or broad mention-expansion ranking may fail?

## 1. Fixed real original source world, task population and provenance

Read the same **65 exact historical Git source documents** at revision `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef`, check the preexisting source fingerprint `01206bdb2fdc3517627a94bdf6587efaa2f5d9ed10ad220f5799c496353c5a09`, and require exact SHA-256 of published Checkpoint 908 hybrid result `e07bcf10e4f04cbde6cbd08b33fb77c02ca17efa03d1a4dbffb73c7a9439334f`. The existing W5 authored subject catalog remains a treatment input to B1, not a freshly qualified authority.

Derive a **directed raw repository-path mention graph**, using the exact historical `references()` extractor already executed at Checkpoints 906-908. An edge A -> B means source file A contains a literal path mention to exact other corpus member B. It does **not** prove governance, true editorial intention, causal dependence, truth, adoption, implementation, authority, execution, or negative real-world events. Verify exactly 110 distinct directed edges, 31 source nodes with outgoing edges and 39 target nodes with incoming edges.

For **every** document, construct **both** of these mechanical title-based questions, giving **130 fixed queries** regardless of whether source mentions exist:

- **FORWARD:** `Which documents does the document titled "<exact first Markdown H1>" explicitly reference by repository path?`
- **REVERSE:** `Which documents explicitly reference the document titled "<exact first Markdown H1>" by repository path?`

The corresponding structural target set is the document's outbound or inbound raw path-mention neighbors, respectively. No direct original target paths are included in the user-facing query. The first-H1 unique exact-title index resolves a query subject. The unmodified graph supplies the target sets **solely for evaluation after rankers finish**. The same graph may also power graph-index treatment arms, making those arms' high structural scores a **construction-aligned capability check**, not out-of-sample validation.

Preflight source-only totals, before scoring:
- Forward positive documents: **31**, reverse positive documents: **39**; negative/empty forward: **34**, empty reverse: **26**.
- **220** directed-relation reference occurrences across the two query directions.
- 2 questions have more than ten structural targets: one source with 21 outbound references and one source with 11 inbound references. With final top-ten results, perfect recall on all instances is mathematically impossible; retain and report those cases and the ceiling **208/220**, not silent exclusion or raised K.
- All 65 titles are distinct; no question omission, editorial selection, post-result mutation or new authoring.

The synthetic question grammar and exact-title index intentionally favor exact typed-reference retrieval. This new family is more relationship-specific than previous 74 tasks, but it is neither independently authored user need nor trustworthy reference answer key.

## 2. Mechanisms and equal final-output budget

All twelve compared strategies see the same question string and the same original source corpus. Every returned list is unique and contains at most ten paths.

**Existing eight exploratory mechanisms, unchanged** from Checkpoint 908, computed from the complete query string and source bytes:
`b0` (FTS5/BM25), `b1` (query-only inferred subject plus authored membership), `b2` (five lexical seed + one-hop literal path-mention expansion), `fusion_b0_b1`, `fusion_b0_b2`, `fusion_b1_b2`, `fusion_all` (unweighted RRF K=60 over each top-ten list), and `router` (exact source-H1 title match -> B0, otherwise B0+B1 RRF). The old `router` is a **negative control**, not relationship-intent aware.

**New actual typed-relation operator:** `relation_index` parses the two exact fixed query templates by source text alone (NOT reference target, graph neighborhood or query-family indicator), resolves the unique source H1 in the same source-title index, and returns direct outgoing or incoming mention neighbors. Rank with BM25 position of candidate among all literal matches, then stable path; absent matches get rank after matched sources. Final limit ten. It must return **zero** for a source with no neighbors; don't manufacture source evidence.

**Two explicit relation/lexical combinations:** `relation_b0_naive_rrf` applies identical RRF K=60 to up to ten relation-index and up to ten B0 candidates, even if no relation exists. `relation_b0_gated_rrf` uses the same RRF if at least one structurally verified relation exists, but emits **no documents** otherwise. This contrast tests negative-evidence handling. Zero output does not prove historical real-world nonoccurrence, only no matching literal path mentions within these 65 pinned bodies.

**Typed-intent router:** `typed_intent_router` uses the exact fixed forward/reverse query grammar to choose the directed relation-index list. For queries not matching the grammar, it delegates unchanged to the existing Checkpoint 908 router. This is deterministic **synthetic query-language routing**, not learned classification or proof of natural language understanding.

An exact-source H1 index and a parsed directed link index incur additional metadata and construction cost. Their advantages over bare text/subject retrieval on this graph-generated reference task **cannot** be sold as independent empirical proof of superior navigation in general. Record the graph-index work and candidate union sizes; no elapsed latency parity or equal source-authoring labor is claimed.

## 3. Scores, negative controls and regression

Evaluate all 130 tasks with:
- number of positive/zero-target queries and two over-budget queries, no exclusions;
- required path-mention target occurrences = 220 and retrieved positive hits@10;
- micro recall@10 over all positive instances; mean per-positive-query recall, not counting empty as vacuous successful recall;
- exact-set success at K=10 requiring all true graph neighbors and no additional outputs (necessarily fails over-budget);
- false-positive returned paths across 60 *structurally empty* questions, plus count of empty queries with any nonempty output;
- returned slots, pre-fusion union candidate count, per-query rankings and raw source-derived reference witnesses;
- per-direction results as separate breakdowns; target files and original paths are public historical source metadata only.

**Scorer and ranker separation:** produce all arm rankings before inspecting their target sets. The relation-index treatment naturally uses the same underlying mention graph used by the oracle. This makes its structural exactness expected by construction, so this experiment measures the implementation/negative-abstention behavior and tradeoffs, not unbiased architecture superiority.

**Backward compatibility:** Feed all earlier 74 queries (nine old topical labels and 65 first-H1 locators) through the unchanged legacy router and new typed-intent router (which must delegate for nonmatching grammar). Verify exact rank-path parity and total cases against the Checkpoint 908 output. Do not rescore or tune old gold; report only parity counts, no new selected scores.

The study is posthoc exploratory, with a task family deliberately derived from path mention edges. Do not call these 130 tasks a preregistered 12-primary P03 experiment; do not claim B2 governed editorial links, B3 governed concern selectors, B4 learned retrieval, real-world authority/recovery, new human generalization or architecture selection.

## 4. No post-result changes

Fix the queries, empty-set semantics, RRF K=60, raw link extractor, source pin, title index, relation sorting, all arm names, K=10, score definitions and output format **before actual execution**. No tuning based on outcomes, dropping zero-target tasks, converting missing body mentions into negative historical claims, changing the two over-budget cases, or updating legacy published result bytes. Exclusive-create one deterministic JSON execution trace and rerun for identity. Any mechanical defect correction must be documented without substantive method change.

    FIXED_HISTORICAL_SOURCE_COUNT=65
    ORIGINAL_DIRECTED_PATH_MENTION_EDGES=110
    FORWARD_QUESTIONS=65
    REVERSE_QUESTIONS=65
    TOTAL_QUESTIONS=130
    EMPTY_QUESTIONS=60
    POSITIVE_QUESTIONS=70
    POSITIVE_INSTANCE_OPPORTUNITIES=220
    K_TRUNCATED_QUESTIONS=2
    MAX_HITS_AT_K10=208
    EXISTING_COMPARATORS=8
    NEW_DIRECT_RELATION_COMBINATIONS_AND_ROUTER=4
    ALL_ARMS=12
    RETRIEVAL_LIMIT=10
    FORMAL_R0_P03_SOURCE_ADMISSION=NONE
    FORMAL_R0_P03_ARCHITECTURE_SELECTION=NONE
