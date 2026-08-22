# Specification 011: V1 RRF Hybrid Retrieval Comparator

**Version:** 0.1  
**Date:** 2026-08-22  
**Status:** Frozen bounded experiment contract before implementation  
**Scope:** Tests whether the already-validated production lexical channel and the completed exact dense semantic candidate contain enough complementary signal for a simple deterministic hybrid retriever to improve frozen semantic coverage without regressing lexical coverage.  
**Authority:** Governs the first lexical+dense fusion comparator. It does not define the final production retrieval architecture or MethodologicalHorizon ranker.

## 1. Evidence boundary

This specification starts only after independent preservation of:

```text
Checkpoint 135
    production SQLite FTS5 lexical retrieval
    RH-L Recall@3 = 1.00
    RH-L MRR      = 1.00
    RH-S Recall@3 = 0.75
    RH-S MRR      = 0.75

Checkpoint 137 / Specification 010 result
    exact BGE-small dense retrieval
    RH-L semantic Recall@3 = 1.00
    RH-L semantic MRR      = 1.00
    RH-S Recall@3          = 0.75
    RH-S MRR               = 0.75
```

The channels fail different frozen semantic cases:

```text
RH-S01 class-imbalance
    lexical MISS
    dense rank 1

RH-S04 ecdf
    lexical rank 1
    dense MISS
```

No retrieval query or expected target may be changed for this comparator.

---

## 2. Experimental question

Does equal-weight rank fusion of the existing lexical and dense top-three rankings eliminate the complementary semantic omissions while preserving the perfect lexical control?

This is narrower than asking whether hybrid retrieval is universally best.

---

## 3. Frozen inputs

Use unchanged repository fixtures:

```text
tests/fixtures/knowledge/reusable_knowledge_stress_v1.json
tests/fixtures/retrieval/methodological_horizon_v1.json
```

Use the same ten reusable-knowledge assets and the exact same RH-S and RH-L queries/targets as Specifications 009 and 010.

Record fixture identity using canonical JSON:

```text
json.dumps(
    value,
    sort_keys=True,
    separators=(",", ":"),
    ensure_ascii=False,
).encode("utf-8")
```

and SHA-256 over those canonical bytes.

Do not use raw checked-out working-tree bytes as the semantic fixture fingerprint.

---

## 4. Frozen retrieval channels

### 4.1 Lexical channel

Use the actual production implementation:

```text
SqliteFtsKnowledgeRetrieval
```

The benchmark database must be isolated and populated through the normal governed path:

```text
fixture copy
-> CANDIDATE_SET
-> import_candidate_bundle
-> explicit accept_candidate_bundle
-> rebuild production FTS projection
```

For each query retain exactly:

```text
lexical top 3
```

Do not alter FTS weights, tokenizer behavior, BM25 ranking, query normalization, or index projection for this comparator.

### 4.2 Dense channel

Use the exact Specification 010 candidate unchanged:

```text
fastembed==0.8.0
BAAI/bge-small-en-v1.5
384 dimensions
query_embed for queries
passage_embed for documents
CPUExecutionProvider
threads = 1
exact normalized cosine similarity
```

Use the same frozen semantic passage projection implemented for Specification 010.

For each query retain exactly:

```text
dense top 3
```

Do not tune the embedding model, passage projection, query instructions, similarity function, or dense top-k.

FastEmbed remains experiment-only and must not be added to the locked production dependency set by this experiment.

---

## 5. Frozen fusion rule

Use equal-weight Reciprocal Rank Fusion.

For each document `d`:

```text
RRF(d) = sum over channels c of 1 / (60 + rank_c(d))
```

where:

```text
rank starts at 1
candidate absent from a channel's top 3 contributes 0 for that channel
channels = lexical, dense
channel weights = equal
RRF k = 60
```

Sort final candidates by:

```text
1. descending RRF score
2. ascending stable_key as deterministic tie break
```

Return exactly the first three candidates, or fewer if the two channels expose fewer than three unique candidates.

No score normalization, learned weight, fitted alpha, query-specific rule, threshold, reranker, or manual exception is allowed.

---

## 6. Required observability

For every RH-S and RH-L query record:

```text
case_id
query
expected/required target keys
lexical top-3 identities and ranks
dense top-3 identities and ranks
candidate union size
fused top-3 identities
fused RRF scores
target source classification:
    BOTH
    LEXICAL_ONLY
    DENSE_ONLY
    ABSENT
```

Also record:

```text
FastEmbed package version
model name
embedding dimension
Python version
operating system
canonical knowledge-fixture SHA-256
canonical benchmark-fixture SHA-256
indexed lexical document count
dense document count
```

Print the complete result payload before applying acceptance assertions so a failed comparator remains diagnostically useful.

---

## 7. Primary semantic acceptance gate

The fused final top-three output must achieve:

```text
RH-S Recall@3              = 1.00
RH-S critical omissions    = 0 / 4
RH-S MRR                   > 0.75
```

Specific complementarity sentinels must both survive:

```text
RH-S01 contains class-imbalance in fused top 3
RH-S04 contains ecdf in fused top 3
```

A fusion result that merely swaps one omission for another fails.

---

## 8. Lexical no-regression gate

Against the unchanged RH-L cases:

```text
RH-L Recall@3 = 1.00
RH-L MRR      = 1.00
```

All ten required RH-L targets must therefore remain rank 1 in the final fused result.

This is intentionally stricter than only preserving Recall@3 because the production lexical baseline already achieved rank-1 perfection on these cases.

---

## 9. Bounded-output and authority invariants

The experiment must also demonstrate:

```text
final fused output <= 3 candidates per query
lexical projection contains only accepted-current revisions
retrieval/fusion does not mutate authoritative reusable knowledge
all returned lexical identities carry exact accepted revision IDs
candidate benchmark material is not promoted into repository operational authority
```

Dense experiment documents must correspond to the same accepted-current asset set used by lexical retrieval.

---

## 10. Cross-platform gate

Execute on:

```text
Ubuntu latest
Windows latest
Python 3.13
```

Required result stability:

```text
same canonical fixture digests
same ordered lexical identities
same ordered dense identities
same ordered fused identities
same acceptance metrics
```

Small floating-point score differences are acceptable if ordering and metrics remain identical.

The normal locked V1 Python regression suite must also pass without FastEmbed in the production lock.

---

## 11. Interpretation rules

### 11.1 If the RRF comparator passes

The justified conclusion is:

```text
lexical + exact semantic hybrid retrieval earns retention
as the leading V1 retrieval hypothesis for the current benchmark
```

This does not by itself select:

```text
FastEmbed as permanent production package
BGE-small as final embedding model
persistent vector storage
ANN
vector database
RRF k=60 as globally final
RRF itself as final large-scale fusion algorithm
reranking
final MethodologicalHorizon ranking
```

The next step is to define the smallest production hybrid retrieval seam consistent with D-028, then begin RH-R/RH-A MethodologicalHorizon construction.

### 11.2 If the RRF comparator fails

Do not immediately tune `k`, channel depth, channel weights, embedding model, or benchmark cases.

Preserve the failed result first. Consider further retrieval complexity only if the remaining omission is important enough to justify another preregistered comparator.

---

## 12. Explicit non-goals

This specification does not evaluate:

```text
large-corpus retrieval latency
ANN recall
vector database operations
incremental embedding refresh
embedding persistence
cross-encoder reranking
LLM relevance judgment
applicability reasoning
MethodologicalHorizon construction
selective context assembly
recommendation quality
```

Those remain separate evidence gates.

---

## 13. Primary evidence

```text
docs/specifications/009_v1_retrieval_and_methodological_horizon_evaluation_contract.md
docs/specifications/010_v1_exact_semantic_retrieval_comparator.md
docs/research/018_dense_semantic_failure_complementarity_and_rrf_fusion_rationale.md
experiments/retrieval/V1_LEXICAL_RETRIEVAL_RESULT.md
experiments/retrieval/V1_EXACT_SEMANTIC_RETRIEVAL_RESULT.md
docs/checkpoints/135_first_production_lexical_retrieval_baseline_cross_platform_passed.md
docs/checkpoints/137_exact_dense_semantic_retrieval_failed_standalone_but_exposed_complementary_signal.md
```