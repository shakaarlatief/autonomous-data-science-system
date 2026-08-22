# Specification 010: V1 Exact Semantic Retrieval Comparator

**Date:** 2026-08-22  
**Status:** Frozen bounded experiment contract v0.1  
**Scope:** First dense semantic retrieval comparator against the preserved Specification 009 lexical control and frozen RH-S/RH-L cases  
**Authority:** Governs this semantic comparator experiment only. It does not select a production embedding model, semantic adapter, vector database, ANN index, fusion method, or reranker.  
**Design session:** 03  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 03 - Project Cockpit & V1 Integration

## 1. Purpose

Checkpoint 135 established the production lexical control:

```text
RH-L Recall@3 = 1.00
RH-L MRR      = 1.00
RH-S Recall@3 = 0.75
RH-S MRR      = 0.75
```

The first semantic comparator tests one narrow question:

> Can a small local dense embedding channel recover the frozen semantic miss and improve semantic retrieval materially without introducing vector-store or ANN infrastructure?

The experiment is frozen before semantic implementation.

---

## 2. Candidate configuration

The comparator must use:

```text
fastembed==0.8.0
BAAI/bge-small-en-v1.5
384-dimensional dense embeddings
TextEmbedding.query_embed for queries
TextEmbedding.passage_embed for documents
exact cosine similarity across the complete corpus
top_k = 3
CPU/local inference in CI
```

The experiment must not use:

```text
Qdrant
another vector database
ANN
LLM query rewriting
lexical score fusion
cross-encoder reranking
hosted embedding APIs
```

FastEmbed remains an experiment-only dependency until later evidence justifies production adoption.

---

## 3. Frozen corpus and cases

Use the unchanged fixtures already preserved by Specification 009:

```text
tests/fixtures/knowledge/reusable_knowledge_stress_v1.json
tests/fixtures/retrieval/methodological_horizon_v1.json
```

No RH-L or RH-S query may be modified in this comparator.

No target key may be modified after seeing semantic results.

---

## 4. Frozen semantic document projection

Construct one deterministic text passage per asset using the existing fixture only.

Allowed content:

```text
stable_key
title
purpose
scope
limitations
retrieval_profile.lexical_terms
retrieval_profile.aliases
retrieval_profile.semantic_cues
reasoning_functions
context requirement keys/descriptions/required_for
semantic checks
narrative facet kind/body
component key/kind/body/reasoning_functions
```

Do not include:

```text
benchmark queries
target labels beyond the asset's own stable identity
relation target names solely to inflate similarity
provenance locators
governance event prose
timestamps
random IDs
```

Asset iteration order must be deterministic by `stable_key` before embedding.

---

## 5. Exact similarity

Let query embedding `q` and document embedding `d_i` be vectors returned by FastEmbed.

Use exact cosine similarity:

```text
cos(q, d_i) = (q · d_i) / (||q|| ||d_i||)
```

If the model outputs normalized vectors, the implementation may use the dot product only after explicitly verifying or normalizing vectors in the comparator. Prefer explicit normalization in experiment code so the similarity semantics are not implicit.

Rank by:

```text
cosine score descending
stable_key ascending as deterministic tie break
```

Return at most three results.

---

## 6. Primary RH-S gate

The semantic comparator must execute all four frozen RH-S cases.

Acceptance requires:

```text
RH-S Recall@3              = 1.00
RH-S critical omissions    = 0 / 4
RH-S MRR                   > 0.75
```

The critical incremental case is RH-S01:

```text
positive cases are scarce and overall correctness hides failures on them
    -> class-imbalance
```

A semantic candidate that does not retrieve `class-imbalance` in the top three does not close the measured lexical gap and therefore does not earn promotion merely because it is an embedding model.

---

## 7. RH-L diagnostic gate

Execute all ten frozen RH-L cases through the semantic channel and record:

```text
RH-L semantic Recall@3
RH-L semantic MRR
per-case rank/results
```

This is diagnostic rather than a replacement criterion because the semantic channel is being evaluated as a complement to a lexical channel that already has perfect RH-L performance.

However, if semantic RH-L Recall@3 is below `0.80`, classify that as a material weakness requiring consideration before fusion/adoption.

---

## 8. Operational and reproducibility checks

### SR-01 Package identity

Record and assert `fastembed==0.8.0` in the comparator environment.

### SR-02 Model identity

Record `BAAI/bge-small-en-v1.5` and assert embedding dimension `384`.

### SR-03 No production dependency promotion

The root `pyproject.toml` / `uv.lock` must not gain FastEmbed merely to run the candidate.

### SR-04 Exact search only

No vector database, ANN library, or remote search service participates.

### SR-05 Cross-platform

Run the comparator on Ubuntu and Windows under Python 3.13.

### SR-06 Deterministic identity/order

Given the same returned scores, tie handling must be deterministic by stable key. Record ordered top-three keys for every case on both platforms.

Exact floating-point scores need not be bit-identical across operating systems, but target inclusion/rank must satisfy the same gate.

### SR-07 Bounded candidate count

Every query returns at most three semantic candidates.

### SR-08 External model acquisition is visible

The CI/result record must make clear that the model artifact is downloaded/cached externally by FastEmbed and is not committed to the ADS repository.

### SR-09 No benchmark mutation

The comparator must read the existing frozen fixture files without changing them.

### SR-10 Existing production regression

The existing V1 Python suite remains green without FastEmbed becoming a required production dependency.

---

## 9. Descriptive operational telemetry

Record, but do not gate on:

```text
model initialization seconds
corpus embedding seconds
total RH-S query seconds
total RH-L query seconds
```

Hosted CI timing is too noisy for a stable pass/fail latency threshold.

---

## 10. Result interpretation

### If primary RH-S gate fails

Preserve the result. Do not adjust queries or silently change the model.

Then decide whether another lightweight candidate such as Model2Vec is decision-relevant or whether semantic retrieval is not yet justified by this corpus.

### If primary RH-S gate passes

Do not automatically add FastEmbed to production.

First preserve the exact result, then evaluate whether semantic results are complementary to lexical results by measuring:

```text
lexical top-3 set
semantic top-3 set
union size
new relevant target contributed by semantic
additional irrelevant candidates contributed by semantic
```

Only then decide whether a semantic channel and/or lexical-semantic fusion earns a production slice.

---

## 11. Stop rule

This comparator answers only whether the selected dense local candidate adds useful semantic retrieval evidence.

It does not justify:

```text
production vector persistence
ANN
vector database
semantic threshold selection
cross-encoder reranking
production embedding refresh policy
production model download policy
final MethodologicalHorizon ranking
```

If exact dense search is sufficient at current scale, do not add ANN/vector infrastructure.

---

## 12. Required execution order

```text
1. preserve this frozen contract
2. implement experiment-only exact semantic comparator
3. run unchanged RH-S + RH-L cases
4. run Ubuntu + Windows gates
5. preserve complete result before any fusion code
6. decide whether semantic retrieval earns further integration
```

Research basis:

```text
docs/research/017_exact_semantic_retrieval_comparator_selection.md
```
