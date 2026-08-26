# Research 016: Production Retrieval and MethodologicalHorizon Benchmark Design

**Date:** 2026-08-22  
**Status:** Current bounded design research for Q-044 and Q-045  
**Scope:** Production reusable-knowledge retrieval, evaluation decomposition, first MethodologicalHorizon benchmark, and selective-context evaluation. This memo does not select an embedding model, reranker, ANN service, vector database, or final ranking architecture.  
**Design session:** 03  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 03 - Project Cockpit & V1 Integration

## 1. Why this track starts with an evaluation contract

The V1 persistence/interchange seam is now governed and cross-backend validated, and D-032 has selected the initial reasoning runtime behind an ADS-owned port. The next unresolved scaling question is therefore no longer where knowledge lives or which generic reasoning runtime executes the loop.

It is:

> Given a large reusable methodological knowledge universe and the current project state, can ADS retrieve the right knowledge with sufficiently low omission and context cost to construct a bounded MethodologicalHorizon without recreating Prototype V0's large always-on context failure?

This track must not begin by selecting embeddings, a vector store, or a reranker. A retrieval technology is useful only insofar as it improves the actual methodological-navigation failure modes.

The benchmark is therefore frozen before the production lexical baseline is implemented.

---

## 2. Repository reconnaissance

The current production package already contains authoritative knowledge/project persistence and governed interchange, but not production retrieval.

### Existing application surface

`src/ads_system/application/ports.py` currently exposes knowledge publication/lookup, governed interchange, project Findings, historical knowledge references, and a UnitOfWork. It has no retrieval port, MethodologicalHorizon builder, or context-assembly service.

### Existing persistence surface

The production SQLAlchemy schema contains the V1 knowledge graph, revisions, governance, components, rules, relations, project state, and project-to-knowledge references. The reusable-knowledge interchange migration adds rich revision extensions, provenance, relation governance, and collections.

There is no production `idx_` lexical table or FTS5 virtual table yet.

This is consistent with Specification 001. That specification selected the architectural seam:

```text
application Retrieval / HorizonBuilder
    -> storage-neutral application contract
    -> SQLite adapter
        -> rebuildable FTS5 lexical projection
        -> rebuildable semantic cache when justified
```

but deliberately did not preselect the production ranking behavior or semantic provider.

### Existing benchmark knowledge

The heterogeneous reusable-knowledge stress fixture already contains ten deliberately different assets:

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

The assets contain more than titles. Depending on the asset, they include:

```text
purpose
retrieval_profile.lexical_terms
retrieval_profile.aliases
retrieval_profile.semantic_cues
applicability
context requirements
semantic checks
narrative facets
components
rules
relations
```

This makes the corpus a useful first retrieval/horizon fixture because it stresses methods, concepts, frameworks, rules, alternatives, prerequisites, and cross-cutting methodological concerns rather than ten near-identical documents.

The corpus is intentionally a `BENCHMARK_FIXTURE`, not accepted methodological authority. Evaluation code may create a test-only `CANDIDATE_SET` copy and explicitly accept it inside an isolated database. The repository fixture itself must not be silently promoted.

---

## 3. The benchmark must separate failure layers

A single retrieval score would hide the failure mode that matters.

The evaluation must preserve at least this chain:

```text
CATALOG COVERAGE
    Was the methodological knowledge represented at all?

RETRIEVAL
    Did a high-recall retrieval channel surface it?

HORIZON CONSTRUCTION
    Did relation/context/applicability processing retain or add the right plausible units?

RELEVANCE / PRIORITIZATION
    Was applicable knowledge ranked appropriately for this project state?

RECOMMENDATION
    Was the right action/concern actually recommended or required?

HUMAN / EXECUTION
    Was a recommendation accepted, deferred, rejected, or skipped?
```

This gives concrete failure labels aligned with Q-045:

```text
ABSENT_FROM_CATALOG
KNOWN_NOT_RETRIEVED
RETRIEVED_INAPPLICABLE
APPLICABLE_RANKED_TOO_LOW
RECOMMENDED_SKIPPED
RECOMMENDED_INCORRECTLY
REQUIRED_CONCERN_OMITTED
```

The first production slice evaluates the second layer while preserving fixtures for the later layers.

---

## 4. Phase-separated benchmark design

The benchmark is divided into five classes so later implementation cannot claim success by solving an easier neighboring problem.

### RH-L: lexical-addressable retrieval

Queries deliberately contain terminology that the accepted knowledge representation says should be retrievable lexically.

Examples include:

```text
missing values / imputation / missing labels
minority class / rare event / class prevalence
rolling origin / chronological split / temporal validation
feature leakage / prediction time / feature eligibility
ECDF / empirical cumulative distribution
histogram / bins
random forest / randomized tree ensemble
gradient boosting / boosted trees
bagging / bootstrap aggregation
scoring time / prediction moment
```

The lexical baseline is expected to solve these without embeddings or LLM query expansion.

### RH-S: semantic/paraphrase retrieval diagnostics

These queries express the same methodological concern with weak or absent direct lexical overlap.

Examples include:

```text
positive cases are scarce and overall correctness hides failures on them

the value is unavailable until after the score has already been produced

evaluate a model as if each forecast were made using only earlier observations

show how a numeric variable accumulates across its range without choosing buckets
```

RH-S is diagnostic for the lexical baseline. It becomes an acceptance comparison only when a semantic candidate exists.

This distinction is important: lexical retrieval should not be deliberately distorted to imitate an embedding model merely to improve semantic-paraphrase cases.

### RH-R: relational horizon expansion

Some knowledge should enter the bounded horizon because a retrieved seed has a semantically relevant relation.

Initial deterministic cases from the stress corpus are:

```text
random-forest
    USES_CONCEPT -> bagging
    ALTERNATIVE_TO -> gradient-boosted-trees

temporal-validation
    REQUIRES_CONCEPT -> prediction-moment

prediction-time-feature-eligibility
    REQUIRES_CONCEPT -> prediction-moment

histogram
    ALTERNATIVE_TO -> ecdf
```

RH-R does not imply that every relation should always expand. Relation family, direction, horizon budget, and current reasoning task remain part of later HorizonBuilder design.

### RH-A: applicability and required-context behavior

Examples already represented by the corpus include:

```text
random-forest
    supervised + supported tabular applicability

class-imbalance
    class-prevalence context required for applicability

temporal-validation
    prediction-moment required for applicability/rule evaluation

prediction-time-feature-eligibility
    prediction-moment required for rule evaluation
```

The benchmark must distinguish:

```text
known false prerequisite -> inapplicable
known true prerequisite -> applicable candidate
unknown required context -> unresolved/clarify/defer according to knowledge semantics
```

Unknown context must not be silently converted to `not applicable`.

### RH-C: selective context construction

Once a bounded horizon exists, the eventual context assembler must be evaluated for:

```text
required knowledge-revision coverage
irrelevant-context rate
serialized context size
stable revision provenance
omission of the full global catalog
```

RH-C is not part of the first lexical implementation gate.

---

## 5. Production lexical projection

The first production retrieval channel should be a rebuildable SQLite FTS5 projection, as already selected architecturally by D-028 / Specification 001.

The index is derived state, never methodological authority.

One search document should represent one **current accepted KnowledgeAsset revision**. Historical, candidate, reviewed, rejected, or superseded revisions must not appear merely because their text still exists in authoritative tables.

The deterministic projection should preserve separate weighted fields for:

```text
stable key
human title
retrieval-profile lexical terms
retrieval-profile aliases
retrieval-profile semantic cues
broader semantic body
```

The broader body may include:

```text
purpose
scope
limitations
reasoning functions
context requirement keys/descriptions
semantic checks
narrative-facet content
accepted component keys/kinds/body/reasoning functions
```

IDs, timestamps, governance event prose, and provenance locators should not dominate retrieval text.

The lexical index can index semantic-cue prose as text. It remains lexical retrieval because matching is token-based rather than embedding-based.

---

## 6. Query behavior for the baseline

The baseline should remain intentionally simple and inspectable.

Recommended first behavior:

```text
raw query
    -> Unicode-safe token extraction
    -> discard empty/common connective tokens
    -> quoted-token OR query
    -> FTS5 MATCH
    -> weighted BM25
    -> deterministic stable-key tie break
    -> bounded top-k results
```

No LLM query rewriting, synonym service, semantic expansion, stemming framework, fusion, or reranking layer should be added to the first baseline.

Malformed punctuation-only input should produce an empty result rather than exposing FTS syntax errors through the application port.

---

## 7. Lexical baseline metrics

The primary metrics are methodological omission metrics rather than latency alone.

For RH-L:

```text
Recall@3 over required asset keys
Critical lexical omission count
Mean reciprocal rank
Top-k candidate count
Determinism across rebuilds
```

For RH-S diagnostic cases:

```text
Recall@3
MRR
per-case retrieved keys
```

Operational invariants:

```text
accepted-current only
exact knowledge revision IDs returned
bounded result count
stable results after deterministic rebuild
no mutation of authoritative semantic tables
blank/punctuation query safety
storage-specific syntax does not leak above the adapter
```

Retrieval latency may be recorded later but is not an acceptance substitute for omission quality in this corpus.

---

## 8. Acceptance philosophy

The lexical baseline should have a deliberately strict gate for lexical-addressable knowledge:

```text
RH-L required-key Recall@3 = 1.00
critical lexical omissions = 0
```

This is feasible because these cases use cues deliberately represented in the reusable knowledge itself.

RH-S is not a lexical-baseline pass/fail requirement. If lexical retrieval also solves some semantic cases, that is useful evidence. If it misses them, the miss provides a clean target for the semantic candidate.

The semantic candidate should only earn adoption if it adds material recall on RH-S or later real project cases without unacceptable irrelevant-candidate/context growth.

Fusion should only be introduced if lexical and semantic channels demonstrate complementary useful retrieval. A reranker should only be introduced if the candidate set is good but ordering is materially inadequate.

---

## 9. Why this avoids the Prototype V0 failure mode

Prototype V0's main scaling failure was not that persistent knowledge existed. It was that too much structured state and support machinery was repeatedly injected into reasoning.

This benchmark instead tests the intended post-V0 scaling path:

```text
large persistent knowledge universe
    !=
per-call LLM context

large persistent knowledge universe
    -> cheap high-recall retrieval
    -> bounded MethodologicalHorizon
    -> applicability/context handling
    -> relevance/prioritization
    -> small task-specific context pack
```

The retrieval benchmark therefore has to measure omissions and candidate growth together. Maximizing recall by returning the whole catalog would be architecturally invalid even if Recall@k looked perfect at a sufficiently large k.

---

## 10. What is deliberately not selected

This research does not select:

```text
embedding model
embedding provider
vector database
ANN library/service
semantic similarity threshold
lexical/semantic fusion algorithm
reranker
LLM relevance judge
final HorizonBuilder relation-expansion policy
final applicability evaluator
final context-pack budget
production knowledge-authoring retrieval-profile UX
```

The next legitimate step is Specification 009, followed by the frozen RH-L production lexical implementation and gate.