# Research 017: Exact Semantic Retrieval Comparator Selection

**Date:** 2026-08-22  
**Status:** Current bounded retrieval research; selects one experiment candidate, not production semantic architecture  
**Scope:** First semantic-retrieval comparator after the preserved lexical baseline. This memo does not select a production embedding provider, vector database, ANN index, fusion method, or reranker.  
**Design session:** 03  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 03 - Project Cockpit & V1 Integration

## 1. Evidence boundary

Checkpoint 135 preserves a strong production lexical control:

```text
RH-L Recall@3            1.00
RH-L MRR                 1.00
RH-L omissions           0 / 10
RH-S diagnostic Recall@3 0.75
```

The frozen semantic miss is:

```text
RH-S01
positive cases are scarce and overall correctness hides failures on them
    -> class-imbalance
    -> lexical result: no hits
```

The other three RH-S targets are already rank 1 lexically.

The semantic comparator therefore has a very specific job. It should test whether genuine dense semantic similarity can close the frozen paraphrase gap without forcing ADS to adopt vector infrastructure prematurely.

---

## 2. Comparator requirements

The first semantic experiment should be:

```text
real semantic embeddings
local/in-process inference
exact similarity over the complete tiny corpus
cross-platform executable
small enough for CI experimentation
separate from production dependency lock until it earns adoption
independent of a vector database
independent of ANN
independent of an LLM provider/API key
```

This deliberately distinguishes:

```text
semantic model value
    from
vector-store / ANN infrastructure value
```

At ten documents, approximate nearest-neighbor infrastructure would add no useful retrieval capability and would confound the experiment with unnecessary operational complexity.

---

## 3. Options considered

### A. Hosted embedding API

Advantages:

```text
strong modern models
minimal local inference burden
```

Disadvantages for the first comparator:

```text
provider/network dependency
API credentials required
less deterministic CI
cost/rate-limit variability
provider choice becomes entangled with semantic-retrieval value
```

Conclusion: not the first comparator.

### B. SentenceTransformers

Current SentenceTransformers is a mature, feature-rich semantic-search stack with explicit query/document encoding and exact semantic-search utilities.

Advantages:

```text
strong standard ecosystem
large model catalog
retrieval-specific models
well-established semantic-search semantics
```

Disadvantages for this bounded experiment:

```text
large framework/dependency surface relative to ten documents
PyTorch-oriented stack is unnecessary for a first CPU comparator
would make dependency cost harder to separate from embedding quality
```

Conclusion: credible future comparator, but larger than necessary for the first experiment.

### C. Model2Vec

Current `model2vec` offers lightweight static embedding models and a small base package. The project advertises models from roughly 2M to 32M parameters, including retrieval-oriented variants.

Advantages:

```text
very small/fast inference
attractive local-first operational profile
no full transformer inference at query time
```

Disadvantages for the first comparator:

```text
package currently labels itself Beta
static-distillation approach is a less conventional first semantic-retrieval control
retrieval-specific flagship is larger than the smallest general models
```

Conclusion: strong lightweight fallback/comparator if the first dense ONNX candidate proves operationally too heavy or if later evidence suggests static embeddings are sufficient.

### D. FastEmbed 0.8.0 + BAAI/bge-small-en-v1.5

FastEmbed 0.8.0 is the current released package at this design boundary. Its documentation exposes dedicated `query_embed` and `passage_embed` methods and uses ONNX-based local inference. The supported-model registry lists `BAAI/bge-small-en-v1.5` as a 384-dimensional English model at approximately 0.067 GB.

Advantages:

```text
real dense retrieval embedding model
CPU/local ONNX inference
no PyTorch requirement for this path
current package supports Python 3.10+
small model relative to full transformer stacks
query/passages retrieval API is explicit
exact cosine search can be implemented with NumPy only
no Qdrant server/client required
```

Costs:

```text
model download/cache is still external operational state
roughly 67 MB model artifact
ONNX Runtime dependency
model/package reproducibility must be recorded carefully
```

Conclusion: best first semantic comparator.

---

## 4. Selected experiment candidate

Freeze for the first semantic comparator:

```text
package
    fastembed==0.8.0

model
    BAAI/bge-small-en-v1.5

embedding dimension
    384

query encoding
    TextEmbedding.query_embed

document encoding
    TextEmbedding.passage_embed

retrieval
    exact cosine similarity over all accepted-current benchmark documents

top-k
    3
```

The package/model are experiment dependencies only at this stage.

Do not add FastEmbed to the root production dependency lock merely to run the comparator. The CI experiment should use an isolated `uv run --with fastembed==0.8.0` environment or an equivalent bounded experiment environment.

---

## 5. Semantic document projection

The comparator should use the same methodological meaning that made the lexical baseline fair, not a different hand-authored answer key.

For each current accepted asset, construct one deterministic passage from fields equivalent to the lexical projection:

```text
stable key
title
purpose
scope
limitations
retrieval-profile lexical terms
retrieval-profile aliases
retrieval-profile semantic cues
reasoning functions
context requirements
semantic checks
narrative facets
accepted component key/kind/body/reasoning functions
```

Do not inject the benchmark query or target label into document text.

The first experiment may construct these documents directly from the frozen validated knowledge fixture because this is a semantic-model comparator, not yet a production adapter. Production integration is a separate decision after candidate value is known.

---

## 6. Frozen semantic acceptance rule

The lexical control remains:

```text
RH-S Recall@3 = 0.75
RH-S MRR      = 0.75
```

The semantic candidate earns further consideration only if:

```text
RH-S Recall@3 = 1.00
RH-S critical omissions = 0 / 4
RH-S MRR > 0.75
```

The comparator must also execute RH-L as a diagnostic. Semantic retrieval does not need to replace the lexical channel, but catastrophic inability to retrieve the obvious lexical cases would be important evidence against adoption.

Record:

```text
RH-S per-case top 3 + scores
RH-S Recall@3
RH-S MRR
RH-L semantic-channel Recall@3 and MRR
mean returned candidate count
model initialization time
corpus embedding time
query retrieval time as descriptive CI telemetry only
```

Latency is not a pass/fail threshold because hosted CI timing is too noisy for a stable architecture gate.

---

## 7. Candidate-growth interpretation

For the exact semantic comparator, top-k remains hard-bounded at three. The semantic channel will therefore not be judged by absolute corpus recall alone.

The next fusion question, if the semantic candidate passes, should explicitly measure:

```text
lexical top-3 set
semantic top-3 set
union size
new relevant targets contributed by semantic
new irrelevant candidates contributed by semantic
```

Fusion is justified only if the semantic channel contributes useful coverage that the lexical channel lacks.

For the current frozen corpus, RH-S01 is the primary useful-increment test.

---

## 8. Reproducibility boundary

The experiment must record:

```text
fastembed package version
model name
embedding dimension
Python version
operating system
frozen knowledge fixture identity
frozen Specification 009 benchmark identity
```

The model artifact is downloaded/cached by FastEmbed rather than committed to this repository. No model file should be added to Git.

If external model download proves too unstable for repeatable CI, that is operational evidence against this candidate shape and should not be hidden by silently vendoring model weights.

---

## 9. Non-selections

This research does not select:

```text
FastEmbed as a production dependency
BAAI/bge-small-en-v1.5 as the final embedding model
semantic retrieval as mandatory architecture
embedding persistence schema
vector database
ANN
Qdrant
fusion algorithm
reranker
semantic similarity threshold
final MethodologicalHorizon ranking
```

The next step is to freeze a bounded executable semantic-comparator contract before implementation, then run it unchanged against the preserved lexical control.

## External capability sources consulted

```text
FastEmbed PyPI 0.8.0
https://pypi.org/project/fastembed/

FastEmbed supported models
https://qdrant.github.io/fastembed/examples/Supported_Models/

FastEmbed retrieval/query-passage API
https://qdrant.github.io/fastembed/qdrant/Retrieval_with_FastEmbed/
https://github.com/qdrant/fastembed/blob/main/fastembed/text/text_embedding.py

SentenceTransformers semantic search
https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html

Model2Vec
https://pypi.org/project/model2vec/
https://github.com/MinishLab/model2vec
```