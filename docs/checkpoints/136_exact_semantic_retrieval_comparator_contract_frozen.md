# Checkpoint 136: Exact Semantic Retrieval Comparator Contract Frozen

**Date:** 2026-08-22  
**Status:** Historical experiment-design checkpoint; Specification 010 v0.1 frozen before semantic implementation  
**Checkpoint class:** DESIGN  
**Project stage:** Post-V0 V1 bounded implementation and integration  
**Scope:** Preserves the post-lexical semantic-retrieval option audit and freezes the first dense exact semantic comparator before implementation.  
**Authority:** Historical preregistration provenance. Specification 010 v0.1 governs the first semantic comparator until its result is preserved.  
**Design session:** 03  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 03 - Project Cockpit & V1 Integration

## 1. Starting boundary

PR #9 merged the validated production lexical retrieval slice into `v1-frontend-spike` at:

```text
73a78d00b8edf440e7fef8c5334b3edb52246d50
```

The semantic comparator branch is:

```text
v1-semantic-retrieval
```

and begins exactly from that promoted lexical boundary.

The lexical control remains unchanged:

```text
RH-L Recall@3            1.00
RH-L MRR                 1.00
RH-S Recall@3            0.75
RH-S MRR                 0.75
```

---

## 2. Candidate selected for experiment, not production

Research 017 compares hosted embeddings, SentenceTransformers, Model2Vec, and FastEmbed for the first bounded semantic comparator.

The frozen experiment candidate is:

```text
fastembed==0.8.0
BAAI/bge-small-en-v1.5
384 dimensions
query_embed for queries
passage_embed for documents
exact cosine over the full ten-document corpus
top_k = 3
```

No vector database, ANN index, hosted embedding API, fusion, or reranker participates.

FastEmbed is not added to the production dependency lock for this comparator.

---

## 3. Why this is the first comparator

The candidate brackets the semantic question with a relatively small local dense model and ONNX inference while avoiding the substantially larger general SentenceTransformers/PyTorch surface.

Model2Vec remains a credible lighter fallback if the dense ONNX candidate is operationally too expensive or fails to add semantic value.

The goal is not to prove that one embedding package is best. The goal is to test whether a real dense semantic channel adds useful retrieval coverage beyond the already-strong lexical baseline.

---

## 4. Frozen gate

The unchanged Specification 009 RH-S cases are primary.

Acceptance requires:

```text
RH-S Recall@3           = 1.00
RH-S critical omissions = 0 / 4
RH-S MRR                > 0.75
```

The critical case remains:

```text
RH-S01
positive cases are scarce and overall correctness hides failures on them
    -> class-imbalance
```

RH-L is also executed as a semantic-channel diagnostic, with `< 0.80 Recall@3` classified as a material weakness.

---

## 5. Reproducibility and operational boundary

The comparator must record:

```text
package version
model name
embedding dimension
Python version
operating system
ordered top-three results
frozen fixture identity
model initialization time
corpus embedding time
query timing
```

The model artifact is downloaded/cached externally by FastEmbed and is not committed to the ADS repository.

If external acquisition or cross-platform execution is unstable, that is real operational evidence against the candidate rather than something to hide through vendoring model weights.

---

## 6. Promotion audit

Promote now:

```text
Research 017
    current semantic-comparator option audit

Specification 010 v0.1
    frozen first exact dense semantic comparator contract
```

Do not promote:

```text
FastEmbed as production infrastructure
BGE-small as final embedding model
semantic retrieval as mandatory
vector persistence
ANN
vector database
fusion
reranking
```

No new Foundation or project-level Decision is justified at this preregistration boundary.

---

## 7. Exact continuation

Implement the experiment-only comparator without changing Specification 009 RH-S/RH-L queries.

Then:

```text
1. run Ubuntu + Windows
2. preserve the exact semantic result
3. compare useful incremental coverage against the lexical control
4. decide whether semantic retrieval earns production integration
5. only then consider fusion
```

Primary sources:

```text
docs/research/017_exact_semantic_retrieval_comparator_selection.md
docs/specifications/010_v1_exact_semantic_retrieval_comparator.md
experiments/retrieval/V1_LEXICAL_RETRIEVAL_RESULT.md
```