# V1 RRF Hybrid Retrieval Comparator Result

**Date:** 2026-08-22  
**Status:** PASS  
**Specification:** `docs/specifications/011_v1_rrf_hybrid_retrieval_comparator.md` v0.1  
**Validated source head:** `2e6be67d579bd203f449fa732b67c8272be9675f`  
**GitHub Actions workflow:** `V1 retrieval fusion comparator`  
**Run:** `32561118325`

## 1. Frozen comparator

```text
lexical
    production SqliteFtsKnowledgeRetrieval
    top 3

dense
    fastembed==0.8.0
    BAAI/bge-small-en-v1.5
    384 dimensions
    exact normalized cosine
    top 3

fusion
    equal-weight Reciprocal Rank Fusion
    k = 60
    final top 3
```

No query, expected target, FTS weight, dense model, passage projection, channel depth, fusion weight, or RRF constant was tuned after the contract was frozen.

## 2. Cross-platform gate

```text
Ubuntu RRF comparator          PASS
Ubuntu locked V1 regression    PASS, 38 passed / 2 skipped

Windows RRF comparator         PASS
Windows locked V1 regression   PASS, 38 passed / 2 skipped
```

Both platforms produced:

```text
same canonical fixture digests
same lexical ordering
same dense ordering
same fused ordering
same accepted revision identities
same evaluation metrics
```

Canonical fixture identities:

```text
knowledge  1b7c22745246c1c0a8c9ca5457b81513aaa3b7981a9ec791cbcb7ca76ada2f24
benchmark  dadc68a506eb6dd57512711f8dccbe0b21ae6ec7bef1a9f6c36f048bb9690790
```

This resolves the raw-working-tree-byte portability issue exposed by Specification 010.

## 3. Primary result

```text
RH-S Recall@3              1.00
RH-S MRR                   0.875
RH-S critical omissions    0 / 4

RH-L Recall@3              1.00
RH-L MRR                   1.00
```

The hybrid result therefore passes both the primary semantic gate and the lexical no-regression gate.

## 4. Complementarity sentinels

### RH-S01

```text
query
    positive cases are scarce and overall correctness hides failures on them

target
    class-imbalance

lexical
    no candidates

dense
    class-imbalance rank 1

fused
    class-imbalance rank 1
```

Target source classification:

```text
DENSE_ONLY
```

The semantic channel contributes unique useful signal and fusion preserves it.

### RH-S04

```text
query
    show how a numeric variable accumulates across its range without choosing buckets

target
    ecdf

lexical
    ecdf rank 1

dense
    ecdf absent from top 3

fused
    histogram rank 1
    ecdf rank 2
    random-forest rank 3
```

Target source classification:

```text
LEXICAL_ONLY
```

The lexical channel contributes unique useful signal and fusion preserves it.

The result therefore eliminates the omission swap seen in the two standalone channels.

## 5. Other RH-S cases

```text
RH-S02 prediction-time-feature-eligibility
    source BOTH
    fused rank 1

RH-S03 temporal-validation
    source BOTH
    fused rank 1
```

Combined reciprocal ranks:

```text
1.0 + 1.0 + 1.0 + 0.5
--------------------- = 0.875
          4
```

## 6. RH-L no-regression result

All ten frozen lexical targets remain rank 1 after fusion:

```text
missing-data
class-imbalance
temporal-validation
prediction-time-feature-eligibility
ecdf
histogram
random-forest
gradient-boosted-trees
bagging
prediction-moment
```

This preserves the lexical baseline's perfect RH-L ranking while adding the missing RH-S01 semantic coverage.

## 7. Candidate-union growth

The retained channel depth was three per channel, while the final fused output remained bounded to three.

Observed union sizes on RH-S:

```text
RH-S01  3
RH-S02  4
RH-S03  4
RH-S04  4
```

Observed RH-L union sizes were three or four.

So the hybrid approach increased the internal candidate pool modestly on this ten-asset corpus while keeping the exposed retrieval output hard-bounded.

This is useful evidence but not a large-corpus cost result.

## 8. Authority and revision invariants

The experiment populated an isolated database through the governed path:

```text
BENCHMARK_FIXTURE copy
-> CANDIDATE_SET
-> import_candidate_bundle
-> accept_candidate_bundle
-> production FTS rebuild
```

Dense passages were built from the exported accepted-current snapshot, not directly trusted as operational authority from the fixture file.

Every cross-channel identity agreed on the exact accepted revision ID.

The accepted snapshot and semantic digest were unchanged before versus after retrieval/fusion:

```text
authoritative_knowledge_unchanged = true
```

## 9. Production-dependency boundary

FastEmbed was still supplied ephemerally to the experiment process.

The normal locked V1 regression suite passed independently without FastEmbed on both operating systems.

Therefore this result does not silently promote an experiment package into the production dependency graph.

## 10. Interpretation

The evidence supports the narrow conclusion:

> Lexical plus exact semantic hybrid retrieval earns retention as the leading V1 retrieval hypothesis for the current frozen benchmark.

The evidence does not yet justify freezing:

```text
FastEmbed as permanent production library
BAAI/bge-small-en-v1.5 as final embedding model
persistent vector storage
ANN
vector database
RRF k=60 as globally final
RRF as final large-scale fusion algorithm
cross-encoder reranking
final MethodologicalHorizon ranking
```

The next production step should preserve a replaceable semantic/fusion boundary while keeping the already accepted production lexical retriever intact.

## 11. Next step

Proceed to the first real RH-R/RH-A MethodologicalHorizon construction experiment using the smallest production-facing retrieval abstraction that can consume a bounded hybrid candidate set without making the embedding implementation part of methodological/domain semantics.

Primary evidence:

```text
docs/specifications/011_v1_rrf_hybrid_retrieval_comparator.md
docs/research/018_dense_semantic_failure_complementarity_and_rrf_fusion_rationale.md
docs/checkpoints/135_first_production_lexical_retrieval_baseline_cross_platform_passed.md
docs/checkpoints/137_exact_dense_semantic_retrieval_failed_standalone_but_exposed_complementary_signal.md
docs/checkpoints/138_rrf_hybrid_retrieval_comparator_contract_frozen.md
experiments/retrieval/V1_EXACT_SEMANTIC_RETRIEVAL_RESULT.md
