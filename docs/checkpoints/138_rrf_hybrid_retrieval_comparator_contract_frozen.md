# Checkpoint 138: RRF Hybrid Retrieval Comparator Contract Frozen

**Date:** 2026-08-22  
**Status:** Historical experiment-design checkpoint; Specification 011 v0.1 frozen before fusion implementation  
**Checkpoint class:** DESIGN  
**Project stage:** Post-V0 V1 bounded implementation and integration  
**Scope:** Preserves the completed dense-only failure interpretation and freezes one deterministic lexical+dense Reciprocal Rank Fusion comparator before fusion code is written.  
**Authority:** Historical preregistration provenance. Specification 011 v0.1 governs the first hybrid retrieval comparator until its result is preserved.  
**Design session:** 03  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 03 - Project Cockpit & V1 Integration

## 1. Evidence boundary

Checkpoint 135 established the production lexical control:

```text
RH-L Recall@3  1.00
RH-L MRR       1.00
RH-S Recall@3  0.75
RH-S MRR       0.75
```

Checkpoint 137 establishes the exact dense-only result:

```text
RH-L semantic Recall@3  1.00
RH-L semantic MRR       1.00
RH-S Recall@3           0.75
RH-S MRR                0.75
```

The critical per-case pattern is complementary:

```text
RH-S01 class-imbalance
    lexical MISS
    dense rank 1

RH-S04 ecdf
    lexical rank 1
    dense MISS
```

No query, expected target, lexical implementation, or dense model is changed for the fusion experiment.

---

## 2. Frozen fusion comparator

Specification 011 freezes:

```text
lexical channel
    production SqliteFtsKnowledgeRetrieval
    top 3

dense channel
    fastembed==0.8.0
    BAAI/bge-small-en-v1.5
    exact normalized cosine
    top 3

fusion
    equal-weight Reciprocal Rank Fusion
    RRF k = 60
    final top 3
    stable_key ascending deterministic tie break
```

No learned weights, score interpolation, threshold tuning, query-specific exceptions, reranking, or model change is permitted.

---

## 3. Frozen gate

Primary semantic gate:

```text
RH-S Recall@3              = 1.00
RH-S critical omissions    = 0 / 4
RH-S MRR                   > 0.75
RH-S01 retains class-imbalance
RH-S04 retains ecdf
```

Lexical no-regression gate:

```text
RH-L Recall@3 = 1.00
RH-L MRR      = 1.00
```

All ten frozen RH-L targets must remain rank 1 after fusion.

---

## 4. Candidate-growth observability

For every query the experiment must preserve:

```text
lexical top 3
dense top 3
candidate union size
fused top 3
target source classification
```

The final retrieval surface stays bounded to top 3 even if the internal candidate union is larger.

---

## 5. Reproducibility correction

The dense-only run showed that raw checked-out fixture byte hashes can differ across operating systems because of line-ending normalization.

This comparator therefore freezes canonical JSON SHA-256 as semantic fixture identity.

Cross-platform success requires identical canonical digests and ordered retrieval identities, not identical platform-dependent raw file bytes.

---

## 6. Promotion audit

Promote now:

```text
Specification 011 v0.1
    frozen RRF comparator contract

Checkpoint 138
    historical preregistration boundary
```

Do not promote:

```text
RRF as accepted production architecture
FastEmbed as production dependency
BGE-small as final model
vector persistence
ANN
vector database
reranking
final MethodologicalHorizon ranking
```

No new project-level Decision or Foundation is justified before execution.

---

## 7. Exact continuation

Implement the comparator exactly as frozen:

```text
1. create isolated migrated SQLite database
2. import/accept benchmark knowledge through governed path
3. rebuild actual production lexical index
4. embed the same accepted-current ten assets with the unchanged dense projection
5. execute frozen RH-S and RH-L queries
6. fuse top-three channel ranks with RRF(k=60)
7. print complete evidence before assertions
8. run on Ubuntu and Windows
9. run locked V1 regression without FastEmbed production dependency
10. preserve result before any retrieval architecture promotion
```

Primary sources:

```text
docs/specifications/011_v1_rrf_hybrid_retrieval_comparator.md
docs/research/018_dense_semantic_failure_complementarity_and_rrf_fusion_rationale.md
docs/checkpoints/137_exact_dense_semantic_retrieval_failed_standalone_but_exposed_complementary_signal.md
```