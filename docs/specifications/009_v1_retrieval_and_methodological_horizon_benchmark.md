# Specification 009: V1 Retrieval and MethodologicalHorizon Benchmark

**Date:** 2026-08-22  
**Status:** Frozen V1 evaluation contract v0.1 for the first production lexical baseline  
**Scope:** Q-044/Q-045 production reusable-knowledge retrieval, benchmark fixtures, lexical baseline acceptance, and later semantic/Horizon comparison boundaries  
**Authority:** Governs the first production lexical retrieval implementation and its evaluation. It does not promote a semantic retrieval technology, final HorizonBuilder policy, or final context-assembly architecture.  
**Design session:** 03  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 03 - Project Cockpit & V1 Integration

## 1. Purpose

This specification freezes the evaluation boundary before implementing production retrieval.

The target is not generic document search. The target is the first measurable production step in:

```text
global reusable methodological knowledge
    -> high-recall retrieval
    -> bounded MethodologicalHorizon
    -> applicability/context handling
    -> relevance/prioritization
    -> selective task-specific LLM context
```

The specification is designed to preserve the Prototype V0 lesson:

```text
what the system remembers
    !=
what the LLM receives on every reasoning call
```

The first gate therefore evaluates omission quality and bounded candidate retrieval rather than rewarding a system for returning the full catalog.

---

## 2. Governing architecture constraints

The implementation must preserve D-028 / Specification 001 and Foundations 019-020.

### 2.1 Application/storage separation

Application code must depend on a storage-neutral knowledge-retrieval contract.

SQLite FTS5 syntax, BM25 invocation, virtual-table creation, tokenization details, and rebuild mechanics must remain inside the SQLite retrieval adapter.

### 2.2 Retrieval output is derived, not authoritative

A retrieval hit is an application projection over accepted reusable knowledge. It is not a new fundamental domain object and does not change governance state.

### 2.3 Accepted-current boundary

The production lexical index must contain only current accepted `KnowledgeAsset` revisions.

The index must not surface a revision merely because it remains present historically in authoritative persistence.

### 2.4 Rebuildability

The lexical index is derived state. It must be possible to delete/rebuild it deterministically from authoritative accepted-current knowledge.

No retrieval index row may become the sole source of semantic knowledge.

### 2.5 Revision transparency

Every returned hit must include the exact accepted knowledge revision ID that produced the indexed document.

---

## 3. Benchmark knowledge corpus

The first benchmark uses:

```text
tests/fixtures/knowledge/reusable_knowledge_stress_v1.json
```

The fixture contains ten heterogeneous assets:

```text
bagging
class-imbalance
ecdf
gradient-boosted-trees
histogram
missing-data
prediction-moment
prediction-time-feature-eligibility
random-forest
temporal-validation
```

The source fixture remains `bundle_kind=BENCHMARK_FIXTURE` and must not be silently promoted.

For an isolated retrieval test database, the benchmark harness may deep-copy the validated bundle, change only `bundle_kind` to `CANDIDATE_SET`, import it through the normal governed candidate path, and explicitly accept that test-only copy. Content identities and semantic payloads must remain unchanged.

---

## 4. Frozen benchmark scenarios

The benchmark fixture for this specification must encode the following case classes and expected keys.

### 4.1 RH-L lexical-addressable cases

These are acceptance-gating for the lexical baseline.

| Case | Query | Required asset key |
|---|---|---|
| RH-L01 | `missing values imputation missing labels` | `missing-data` |
| RH-L02 | `minority class rare event class prevalence` | `class-imbalance` |
| RH-L03 | `rolling origin chronological split temporal validation` | `temporal-validation` |
| RH-L04 | `feature leakage prediction time feature eligibility` | `prediction-time-feature-eligibility` |
| RH-L05 | `empirical cumulative distribution ECDF without bins` | `ecdf` |
| RH-L06 | `histogram bins quantitative distribution` | `histogram` |
| RH-L07 | `random forest randomized tree ensemble` | `random-forest` |
| RH-L08 | `gradient boosting boosted trees sequential` | `gradient-boosted-trees` |
| RH-L09 | `bootstrap aggregation bagging learners` | `bagging` |
| RH-L10 | `scoring time prediction moment cutoff` | `prediction-moment` |

### 4.2 RH-S semantic/paraphrase diagnostics

These are recorded but are not lexical-baseline pass/fail gates.

| Case | Query | Target asset key |
|---|---|---|
| RH-S01 | `positive cases are scarce and overall correctness hides failures on them` | `class-imbalance` |
| RH-S02 | `the value is unavailable until after the score has already been produced` | `prediction-time-feature-eligibility` |
| RH-S03 | `evaluate a model as if each forecast were made using only earlier observations` | `temporal-validation` |
| RH-S04 | `show how a numeric variable accumulates across its range without choosing buckets` | `ecdf` |

The semantic candidate must later be evaluated on the same frozen cases. The lexical implementation must not change these queries after seeing results.

### 4.3 RH-R relational Horizon cases

These are frozen for the later HorizonBuilder phase and are not part of the first lexical gate.

```text
seed random-forest
    expected related candidates include bagging and gradient-boosted-trees

seed temporal-validation
    expected required concept includes prediction-moment

seed prediction-time-feature-eligibility
    expected required concept includes prediction-moment

seed histogram
    expected alternative candidate includes ecdf
```

### 4.4 RH-A applicability/context cases

Frozen later-stage expectations:

```text
random-forest
    known supervised + supported tabular -> may remain applicable
    known non-supervised -> must not be treated as applicable merely because retrieved

class-imbalance
    missing class-prevalence context -> unresolved/defer/clarify state, not false inapplicability

temporal-validation
    missing prediction-moment -> required context remains visible

prediction-time-feature-eligibility
    missing prediction-moment -> rule evaluation cannot be silently completed
```

### 4.5 RH-C selective context cases

A later context-assembly gate must measure exact revision coverage, irrelevant context, serialized size, and omission of the global catalog. No RH-C acceptance threshold is frozen in v0.1 because the first real Horizon representation does not yet exist.

---

## 5. Application retrieval contract

The first production slice must introduce a storage-neutral application port conceptually equivalent to:

```text
search(query: str, limit: int) -> tuple[KnowledgeRetrievalHit, ...]
```

A hit must expose at least:

```text
stable_key
revision_id
title
score
channel
```

For this baseline:

```text
channel = LEXICAL
```

The application contract must not expose SQLite rowids, FTS rank expressions, MATCH syntax, or raw index-table fields.

---

## 6. Frozen lexical document projection

The SQLite adapter must build one FTS5 row per current accepted asset revision.

Searchable fields are:

```text
stable_key
title
lexical_terms
aliases
semantic_cues
body
```

`revision_id` is retained as unindexed metadata.

The deterministic `body` projection may contain:

```text
purpose
scope
limitations
reasoning_functions
context-requirement key / description / required_for
semantic checks
narrative facets
accepted component key / kind / body / reasoning functions
```

The projection must not include governance-event prose, source locators, random IDs, timestamps, or unrelated audit text merely to increase token overlap.

Only accepted components belonging to the current accepted asset revision may contribute component text.

---

## 7. Frozen lexical query and ranking baseline

The first implementation must use a simple deterministic lexical pipeline:

```text
raw user/project query
    -> extract alphanumeric/underscore Unicode-compatible tokens
    -> normalize case
    -> remove a small implementation-owned connective stopword set
    -> quote each remaining token
    -> combine with OR
    -> FTS5 MATCH
    -> weighted BM25
    -> deterministic stable_key tie break
    -> top-k
```

No LLM query rewriting or semantic expansion is permitted in the lexical baseline.

The initial BM25 column weights are frozen as:

```text
stable_key      8.0
title           6.0
lexical_terms   5.0
aliases         3.0
semantic_cues   2.0
body            1.0
revision_id     0.0 / unindexed
```

If an implementation detail makes FTS5 require the equivalent weights in a different positional order, the semantic weighting above remains authoritative.

A blank query or a query that contains no usable token must return no hits without raising an FTS syntax error.

`limit <= 0` must return no hits.

---

## 8. RH-L acceptance metrics

For the ten RH-L cases, evaluate top 3 results.

Required gate:

```text
required-key Recall@3 = 1.00
critical lexical omissions = 0 / 10
```

Also record:

```text
MRR over the required keys
per-case rank
retrieved stable keys
retrieval scores
```

No lower MRR threshold is frozen for v0.1 because all ten required assets only need to be reliably surfaced within the bounded high-recall top-three candidate set.

---

## 9. Non-quality invariants

The lexical gate must also prove:

### RL-01 Accepted-current only

Candidate, reviewed, rejected, and superseded revisions do not appear unless they are the current accepted revision of an asset, which by definition they should not be.

### RL-02 Revision exactness

Every hit's `revision_id` equals the indexed current accepted revision.

### RL-03 Deterministic rebuild

Rebuilding the FTS index from unchanged authoritative knowledge produces identical ordered hit keys and revision IDs for the frozen benchmark queries.

### RL-04 Bounded output

The requested positive `limit` is honored.

### RL-05 Query safety

Blank, whitespace-only, and punctuation-only queries return an empty tuple rather than leaking SQLite/FTS parser errors.

### RL-06 Authoritative-state isolation

Index rebuild/search does not modify reusable-knowledge governance, current accepted pointers, project state, or historical revisions.

### RL-07 Storage isolation

Application/domain modules do not import SQLite FTS APIs or depend on FTS5 syntax.

### RL-08 Existing persistence compatibility

The existing Python persistence/interchange/migration suite remains green.

### RL-09 Cross-platform execution

The lexical benchmark and relevant existing suite must pass on Ubuntu and Windows under the repository's supported Python baseline.

### RL-10 Semantic diagnostic preservation

All four RH-S cases are executed and their results persisted in the benchmark result artifact even though they are not lexical-baseline gates.

---

## 10. Result artifact

The implementation gate must generate or preserve a deterministic human-readable result artifact containing at least:

```text
implementation name/version
benchmark specification version
knowledge fixture identity
RH-L per-case top-3 results
RH-L Recall@3
RH-L MRR
RH-L critical omission count
RH-S per-case top-3 results and diagnostic recall
invariant test results
operating-system gate results when CI is complete
```

The result must not claim that RH-S failures imply a specific embedding solution. They establish only that the lexical channel has a measurable semantic-retrieval gap on the frozen cases.

---

## 11. Semantic-candidate advancement rule

After the lexical gate:

1. preserve the lexical result before adding semantic code;
2. inspect RH-S misses and false-positive candidate growth;
3. implement a semantic candidate only against the same frozen corpus/cases;
4. compare incremental useful recall and candidate growth;
5. add lexical/semantic fusion only if the channels are materially complementary;
6. add reranking only if candidate coverage is good but ordering remains materially weak.

Do not select a vector database or ANN service merely because a semantic candidate uses vectors. Exact in-process semantic search remains a valid first semantic comparator for the current corpus size.

---

## 12. HorizonBuilder advancement rule

Do not conflate retrieval with applicability or relation expansion.

The first HorizonBuilder implementation should begin only after at least one high-recall retrieval channel has a preserved result boundary.

It must then evaluate RH-R and RH-A separately and preserve explanations for:

```text
retrieved directly
added by relation expansion
retained as applicable
removed as inapplicable
deferred because required context is unknown
```

The final horizon budget/ranking algorithm remains open.

---

## 13. Stop conditions and non-selections

The current specification does not select:

```text
embedding model/provider
vector store
ANN index
semantic threshold
fusion algorithm
reranker
LLM relevance judge
relation-expansion depth
final applicability engine
final horizon size
final context budget
```

If RH-L fails, repair the lexical projection/query baseline first rather than adding semantic infrastructure to hide a lexical defect.

If RH-L passes and RH-S is already unexpectedly strong, semantic retrieval still requires evidence of incremental value before adoption.

If a semantic candidate materially improves RH-S but explodes candidate/context volume, it has not yet earned promotion.

---

## 14. Required execution order

```text
1. preserve this frozen v0.1 contract
2. add the benchmark scenario fixture
3. introduce storage-neutral KnowledgeRetrievalPort / hit DTO
4. implement rebuildable SQLite FTS5 accepted-current projection
5. execute RH-L + RH-S diagnostics and RL-01..RL-10
6. preserve the complete lexical result
7. only then evaluate semantic retrieval
8. only after retrieval evidence, begin RH-R/RH-A HorizonBuilder work
```

Research basis:

```text
docs/research/016_production_retrieval_and_methodological_horizon_benchmark_design.md
```
