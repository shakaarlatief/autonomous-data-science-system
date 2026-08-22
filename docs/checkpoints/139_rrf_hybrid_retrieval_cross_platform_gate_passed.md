# Checkpoint 139: RRF Hybrid Retrieval Cross-Platform Gate Passed

**Date:** 2026-08-22  
**Status:** Historical evaluation/promotion checkpoint; Specification 011 v0.1 passed  
**Checkpoint class:** EVALUATION  
**Project stage:** Post-V0 V1 bounded implementation and integration  
**Scope:** Preserves the first successful lexical+dense hybrid retrieval result and promotes only the hybrid-retrieval direction warranted by the frozen benchmark.  
**Authority:** Historical evaluation evidence and current bounded retrieval-direction promotion. It does not freeze a permanent embedding package/model, vector store, ANN strategy, reranker, or final MethodologicalHorizon ranker.  
**Design session:** 03  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 03 - Project Cockpit & V1 Integration

## 1. Starting evidence

Two independently preserved standalone channels each achieved:

```text
RH-S Recall@3 = 0.75
RH-S MRR      = 0.75
```

but with complementary misses:

```text
RH-S01 class-imbalance
    lexical MISS
    dense rank 1

RH-S04 ecdf
    lexical rank 1
    dense MISS
```

Specification 011 froze one deterministic equal-weight RRF comparator before fusion implementation.

---

## 2. Executed comparator

```text
lexical
    production SqliteFtsKnowledgeRetrieval
    top 3

dense
    fastembed==0.8.0
    BAAI/bge-small-en-v1.5
    exact normalized cosine
    top 3

fusion
    Reciprocal Rank Fusion
    equal weights
    k = 60
    final top 3
```

No benchmark query, target, model, FTS configuration, passage projection, channel depth, fusion constant, or channel weight was tuned after Checkpoint 138.

---

## 3. Validation evidence

```text
V1 retrieval fusion comparator
run 32561118325
validated source head 2e6be67d579bd203f449fa732b67c8272be9675f

Ubuntu comparator           PASS
Ubuntu locked V1 regression PASS, 38 passed / 2 skipped

Windows comparator           PASS
Windows locked V1 regression PASS, 38 passed / 2 skipped
```

Canonical fixture digests, ordered channel identities, fused identities, accepted revision IDs, and metrics matched across operating systems.

---

## 4. Frozen gate result

```text
RH-S Recall@3              1.00
RH-S MRR                   0.875
RH-S critical omissions    0 / 4

RH-L Recall@3              1.00
RH-L MRR                   1.00
```

Specific sentinels:

```text
RH-S01 class-imbalance
    DENSE_ONLY signal
    fused rank 1

RH-S04 ecdf
    LEXICAL_ONLY signal
    fused rank 2
```

The fusion therefore removes the complementary omission swap while preserving the lexical control's perfect RH-L ranking.

---

## 5. Candidate-growth result

Internal top-three channel unions remained small on the current corpus:

```text
RH-S union size range 3 to 4
RH-L union size range 3 to 4
final exposed result <= 3
```

This demonstrates bounded output for the current benchmark but is not evidence about large-corpus latency or candidate growth.

---

## 6. Authority and revision safety

The experiment used an isolated migrated database and the normal governed import/acceptance path.

The lexical projection was built from accepted-current knowledge. Dense passages were built from the exported accepted-current snapshot. Cross-channel stable keys agreed on exact accepted revision IDs.

Retrieval and fusion did not mutate authoritative knowledge:

```text
authoritative_knowledge_unchanged = true
```

Benchmark knowledge remains test material rather than repository operational authority.

---

## 7. Promotion decision

Promote now, narrowly:

> **For the current V1 retrieval benchmark, a bounded lexical + exact semantic hybrid candidate path is the leading retrieval hypothesis because it preserves perfect lexical control while closing the measured semantic omission.**

This is enough to carry both channels forward into MethodologicalHorizon evaluation.

It is not enough to accept as permanent architecture:

```text
FastEmbed
BGE-small
persistent embedding storage
ANN
vector database
RRF k=60
RRF as final large-scale fusion
reranking
```

The production boundary should therefore remain replaceable:

```text
bounded retrieval candidates
    independent of
specific lexical / embedding / fusion implementation
```

---

## 8. Exact continuation

Do not spend another cycle optimizing retrieval metrics on the ten-asset corpus.

Proceed into the purpose for which retrieval exists:

```text
retrieval candidates
-> applicability/context evaluation
-> bounded MethodologicalHorizon
-> relevance/prioritization
-> selective context
```

Use the frozen RH-R/RH-A cases from Specification 009 to test whether the system can correctly distinguish retrieved knowledge from applicable/relevant knowledge.

Before implementing the first Horizon builder, define the smallest application-facing candidate contract that keeps provider/model/fusion details below the boundary.

Primary evidence:

```text
experiments/retrieval/V1_RRF_HYBRID_RETRIEVAL_RESULT.md
docs/specifications/011_v1_rrf_hybrid_retrieval_comparator.md
docs/research/018_dense_semantic_failure_complementarity_and_rrf_fusion_rationale.md
docs/checkpoints/137_exact_dense_semantic_retrieval_failed_standalone_but_exposed_complementary_signal.md
docs/checkpoints/138_rrf_hybrid_retrieval_comparator_contract_frozen.md
```