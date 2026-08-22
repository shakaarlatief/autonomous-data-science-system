# Checkpoint 137: Exact Dense Semantic Retrieval Failed Standalone but Exposed Complementary Signal

**Date:** 2026-08-22  
**Status:** Historical evaluation checkpoint; Specification 010 executed and primary dense-only gate failed  
**Checkpoint class:** EVALUATION  
**Project stage:** Post-V0 V1 bounded implementation and integration  
**Scope:** Preserves the completed exact dense semantic comparator, its cross-platform failure pattern, regression non-impact, and the evidence-based transition to one bounded fusion experiment.  
**Authority:** Historical evaluation evidence. The dense-only comparator result is final for Specification 010 v0.1 unless a separately preregistered future experiment explicitly reopens it.  
**Design session:** 03  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 03 - Project Cockpit & V1 Integration

## 1. Starting boundary

Checkpoint 136 froze the first dense comparator before implementation:

```text
fastembed==0.8.0
BAAI/bge-small-en-v1.5
384 dimensions
query_embed / passage_embed
exact normalized cosine
ten-document corpus
top_k = 3
```

The lexical control from Checkpoint 135 remained unchanged.

---

## 2. Final observable run

The first comparator execution revealed the substantive dense-only miss but initially asserted before emitting the complete result and skipped the broad regression step after failure.

Those were observability/gating defects only. The follow-up changed only:

```text
emit complete JSON before frozen acceptance assertions
run locked V1 regression with if: always()
```

No frozen query, target, model, passage projection, similarity calculation, top-k, or acceptance threshold changed.

Final observable evidence:

```text
V1 semantic retrieval comparator
run 32560811584
validated source head 47e4913d159aa365aad74dbdcf94281055d7d5ba

Ubuntu dense comparator       FAIL primary RH-S gate
Ubuntu locked V1 regression  PASS, 38 passed / 2 skipped

Windows dense comparator      FAIL primary RH-S gate
Windows locked V1 regression PASS, 38 passed / 2 skipped
```

Both operating systems produced the same ordered retrieval identities and the same metrics.

---

## 3. Dense-only result

```text
RH-L semantic Recall@3     1.00
RH-L semantic MRR          1.00

RH-S Recall@3              0.75
RH-S MRR                   0.75
RH-S critical omissions    1 / 4
```

Specification 010 required:

```text
RH-S Recall@3              = 1.00
RH-S critical omissions    = 0 / 4
RH-S MRR                   > 0.75
```

The dense-only candidate therefore fails its primary gate.

---

## 4. Per-case result

```text
RH-S01 -> class-imbalance
    dense rank 1
    lexical baseline MISS

RH-S02 -> prediction-time-feature-eligibility
    dense rank 1
    lexical rank 1

RH-S03 -> temporal-validation
    dense rank 1
    lexical rank 1

RH-S04 -> ecdf
    dense MISS from top 3
    dense top 3 = random-forest, bagging, histogram
    lexical rank 1
```

The dense channel closes the lexical baseline's only RH-S miss but introduces a different miss on a case the lexical channel solved.

---

## 5. Architectural interpretation

The evidence rejects replacing lexical retrieval with dense retrieval:

```text
lexical RH-S Recall@3 = 0.75
dense   RH-S Recall@3 = 0.75
```

But aggregate equality hides a useful error structure:

```text
lexical and dense fail different semantic cases
```

Therefore semantic retrieval has demonstrated incremental signal without demonstrating standalone superiority.

This is exactly the condition under which Specification 009 allowed a bounded fusion experiment to become decision-relevant.

---

## 6. Production-dependency boundary remained intact

FastEmbed was provided ephemerally to the comparator workflow. The normal locked V1 suite passed independently without FastEmbed on both operating systems.

Therefore this checkpoint does not promote:

```text
FastEmbed
BGE-small
embeddings as mandatory production infrastructure
vector persistence
ANN
vector database
reranking
```

---

## 7. Reproducibility finding

Raw SHA-256 over checked-out fixture bytes differed between Ubuntu and Windows despite identical parsed JSON semantics and identical retrieval identities.

The likely source is working-tree line-ending normalization.

Future retrieval experiment identity should therefore use canonical JSON bytes or Git blob identity rather than raw working-tree bytes.

This did not invalidate the result because:

```text
case IDs and expected targets were unchanged
parsed knowledge content was equivalent
ordered results matched
metrics matched exactly
```

---

## 8. Promotion audit

Promote/preserve now:

```text
experiments/retrieval/V1_EXACT_SEMANTIC_RETRIEVAL_RESULT.md
    final dense-only result

docs/research/018_dense_semantic_failure_complementarity_and_rrf_fusion_rationale.md
    current rationale for the next bounded experiment

Checkpoint 137
    historical dense-only evaluation boundary
```

Do not promote:

```text
FastEmbed as production dependency
BGE-small as final model
dense retrieval as lexical replacement
RRF as architecture before execution
vector database / ANN / reranker
```

---

## 9. Exact continuation

Freeze one score-scale-independent fusion comparator before implementation:

```text
production lexical top 3
+ exact dense top 3
-> equal-weight Reciprocal Rank Fusion
-> final top 3
```

The fusion experiment must preserve both complementarity sentinels:

```text
RH-S01 class-imbalance
RH-S04 ecdf
```

and must not regress the perfect RH-L lexical control.

Primary sources:

```text
docs/specifications/010_v1_exact_semantic_retrieval_comparator.md
docs/research/018_dense_semantic_failure_complementarity_and_rrf_fusion_rationale.md
experiments/retrieval/V1_EXACT_SEMANTIC_RETRIEVAL_RESULT.md
docs/checkpoints/135_first_production_lexical_retrieval_baseline_cross_platform_passed.md
```