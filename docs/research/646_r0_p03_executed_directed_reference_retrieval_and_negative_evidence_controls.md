# Research 646: Actual directed-reference retrieval, negative-evidence abstention, and fusion ablation

**Date:** 2026-11-12
**Status:** ACTUAL_130_QUESTION_DIRECTED_RELATION_TEST_EXECUTED / STRUCTURAL_GRAPH_CEILING_208_OF_220 / NO_FORMAL_ARCHITECTURE_SELECTION
**Scope:** Preserve real historical-source reference navigation across both directions, including 60 legitimate no-reference queries and two over-top-ten cases. Distinguish source-derived functionality from independent historical truth and from authentic B2/B3 authority.
**Authority:** Frozen source-derived V01 contract, actual immutable 130-task result, predecessor Checkpoints 905-908, original Research 513/559/576 still unchanged.
**Checkpoint:** 909. **Specification:** 028 unchanged. **Interaction:** ChatGPT / chatgpt-42.

## 1. Why this was a useful experiment to actually run

The previous 74 exploratory source-navigation questions measured broad subject retrieval and exact document-title location; neither directly tested questions requiring explicit source-to-source relationships. The owner instructed the team to keep executing real experiments, including hybrids, while identifying limitations instead of restarting lengthy historical answer-reference qualification.

This is a complete new **source-derived structural-relation question family**, not a freshly independent human question set:

- Exactly **65** pinned UTF-8 Markdown source documents at `4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef` with source SHA-256 corpus fingerprint `01206bdb2fdc3517627a94bdf6587efaa2f5d9ed10ad220f5799c496353c5a09`.
- **110** exact directed literal repository-path mentions, **31** source documents with outgoing edges and **39** with incoming edges.
- Exactly **130 fixed synthetic title-based questions**: one asks which documents each source explicitly references and another asks which documents explicitly reference that source. Zero manual inclusion/exclusion, no replacement or result-aware query edits.
- **70** positive questions; **60** legitimate structurally empty questions; **220** reference opportunities over both directions; two questions contain more than ten reference targets (21 outbound, 11 inbound), so the absolute maximum observable top-ten reference hits is **208/220**, and maximum exact-set successes **128/130**.
- The complete first-H1 title is used as the request key. No target source path enters the query. A correct answer is **the set of documents explicitly mentioned by repository path within the exact source texts**, not a confirmed source-owned governed relation or an operational event.

The raw link graph is mechanically extracted from actual historical source bodies using the same previously tested literal `docs/...` mention parser. It is not independently source-authority-adjudicated. Crucially, the new `relation_index` treatment and the scoring reference both consume this **same graph**, so near-perfect structural scores are expected by construction. This is a functional implementation/cost/abstention experiment, **not independent evidence** that the graph index will succeed on new user intents, semantic links or authoritative relationship questions.

Frozen before first new score:

    experiments/r0_p03_navigation_probe/EXPLORATORY_DIRECTED_RELATION_RETRIEVAL_CONTRACT_V01.md
    experiments/r0_p03_navigation_probe/exploratory_directed_relation_retrieval_v01.py

Actual exclusive-create saved output:

    experiments/r0_p03_navigation_probe/exploratory_directed_relation_retrieval_result_v01.json
    RESULT_BYTES=1692786
    RESULT_SHA256=99206720df7dfa6deb788f4abd8428137a55f5ee68962e83f08da79a7775c399
    ORIGINAL_CHECKPOINT_908_RESULT_SHA256=e07bcf10e4f04cbde6cbd08b33fb77c02ca17efa03d1a4dbffb73c7a9439334f

All eight existing lexical/subject/citation-proxy/fusion/router alternatives were computed from exactly the same visible question text and common sources, with the same top-ten final output limit. Added four actual new arms:
- `relation_index`: parse exact fixed question grammar, source-H1 title resolution, retrieve outgoing or incoming explicit-path mention neighbors, sort with common BM25 rank then path.
- `relation_b0_naive_rrf`: rank-fuse first ten relation neighbors with ten lexical candidates even if no reference exists.
- `relation_b0_gated_rrf`: same fusion where a reference is observed, but **return no candidates** when the source has no explicit edges.
- `typed_intent_router`: exact known syntactic relation request chooses relation index; other requests delegate to unchanged Checkpoint 908 router. A full regression reran all previous **74 non-relation queries** and verified unchanged result rankings.

This does not constitute an authenticated natural-language intent classifier. The test grammar and graph-index operator intentionally align. Additional title/link index construction and treatment-specific metadata costs have not been equalized with B0/B1.

## 2. Actual results across all 130 questions

| Mechanism | Required explicit path references found @10 / 220 | Correct empty abstentions / 60 | Exact entire structural target set / 130 | Unrelated returned slots on empty questions |
| --- | ---: | ---: | ---: | ---: |
| B0 lexical | 110 | 0 | 0 | 600 |
| B1 inferred subjects | 104 | 0 | 0 | 600 |
| B2 literal citation proxy | 132 | 0 | 0 | 600 |
| B0+B1+B2 RRF | 126 | 0 | 0 | 600 |
| Relation-index + B0 naïve RRF | 186 | 0 | 0 | 600 |
| Relation-index + B0 **gated** RRF | 186 | **60** | 60 | **0** |
| **Typed directed relation index** | **208** | **60** | **128** | **0** |
| Exact grammar typed-intent router | 208 | 60 | 128 | 0 |

These numbers are actual executed retrieval traces, not simulated estimates. Other pairwise fusions are also fully recorded in the result file (B0+B1 RRF 121/220, B0+B2 RRF 130/220, B1+B2 RRF 125/220) and not excluded because unfavorable.

**Forward only:** B0 39/110, B1 45/110, B2 proxy 64/110, indexed 99/110; source-owned zero-result claims 34/34. **Reverse only:** B0 71/110, B1 59/110, B2 proxy 68/110, indexed 109/110; structurally empty reverse 26/26. The 21-outbound and 11-inbound over-budget cases explain 12 missed references out of 220 from the direct index, exactly matching its top-ten mathematical ceiling. Both over-budget cases are reported as structurally incomplete, not silently removed.

The index emits **208 total returned paths** across all 130 queries, all of which are actual indexed structural mention targets, whereas the B0 lexical baseline always fills ten and emits **1300 total source slots**, including **600** across structurally empty requests. This is a functional selectivity effect, not measured latency, token efficiency or automatically a superior user experience.

The naïve index+B0 fusion returns **186/220** references but also generates **600** spurious returned slots across the 60 structurally empty requests. Gating those same fusion outputs based on independently observable index emptiness keeps the same **186/220** positive reference coverage while reducing empty-request false-positive slots to **zero**. It also reduces union candidate instances from **1398 to 798**. This isolates an important engineering policy: a source-grounded absence of the requested *indexed relation* should not be silently overridden by lexical retrieval. Still, no-path-mention is not evidence that an underlying real-world relationship does not exist.

## 3. What the result actually establishes and does not establish

Actual positive engineering evidence:
- A directed source-path index can be implemented against pinned real Git original bytes, traverse outgoing/incoming links, respect a strict top-ten cap, retain cases above cap, and return empty results without fabricating structural witness paths.
- Simple lexical/topic/path-hop retrieval and generic RRF do not automatically implement precise **typed** relationships, and can return unrelated sources to questions whose mechanically defined relation set is empty.
- A hybrid evidence-boundary policy is materially different from naïvely combining the same components, and can be evaluated with ablations and negative controls.
- The unchanged 74-query historical router regression passed, so the new typed experimental operator did not break recorded nonrelation behavior.

**Important limitations:**
- The graph index and the task targets share the same literal parser and historical corpus; 208/220 at K=10 is tautologically expected for a correctly implemented index. It is not blinded independent gold, a generalization score, or causal evidence of superior architecture.
- The synthetic question grammar is known exactly to the typed router. It cannot claim flexible natural language understanding.
- Literal path mentions, including in source prose/code, are *not* verified source-owned governing editorial B2 edges, actual dependency, operative authority or B3 concern obligations. Missing repository-path mentions cannot establish that a real relationship is absent.
- Both positive answers and structural empty requests are only about this bounded historical 65-file source world, not current or later C02 evidence ceiling.
- No independent human question/adjudicator, unseen corpus, equalized annotation effort, wall-clock latency/memory/cost or false-authority scoring exists for this test.
- C01/C02 restricted questions and case reports are neither read nor changed. Research 513/559/576 twelve-primary plus nine independently neutralized legacy scored architectural experiment remains **UNSCORED**, with zero primary qualified gold and no source admission.

**Next bounded technical work:** distinguish literal mentions from **meaningful declared or governed relations** where originals provide actual source-owned semantics, build independent answerable relation/authority query samples without recycling the just-measured 130 synthetic edge questions, and test automatic intent routing with different wording or adverse paraphrases before proposing any physical target. Keep execution-first progress, honest negative controls, and no silent score-driven threshold optimization.

    CHECKPOINT_909=ACTUAL_DIRECTED_130_QUERY_EXECUTION
    SOURCE_DOCUMENTS=65
    RAW_LITERAL_DIRECTED_EDGES=110
    NEW_FORWARD_TASKS=65
    NEW_REVERSE_TASKS=65
    EMPTY_TASKS=60
    GRAPH_INDEX_REQUIRED_INSTANCES=220
    MAX_K10_HITS=208
    DIRECT_GRAPH_INDEX_HITS=208
    DIRECT_GRAPH_INDEX_EXACT_SETS=128
    DIRECT_GRAPH_INDEX_CORRECT_EMPTY=60
    NAIVE_RELATION_LEXICAL_FUSION_HITS=186
    NAIVE_RELATION_LEXICAL_FUSION_EMPTY_FALSE_POSITIVE_SLOTS=600
    GATED_RELATION_LEXICAL_FUSION_HITS=186
    GATED_RELATION_LEXICAL_FUSION_EMPTY_FALSE_POSITIVE_SLOTS=0
    OLD_74_QUERY_ROUTER_REGRESSION=PASS
    FULL_R0_P03_SCORED_OUTCOME=NONE
    ARCHITECTURE_TARGET_SELECTION=NONE
    NEXT=FRESH_SEMANTICALLY_QUALIFIED_RELATION_AND_NATURAL_QUERY_TEST
