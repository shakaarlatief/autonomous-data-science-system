# Research 019: First MethodologicalHorizon Application Seam

**Date:** 2026-08-22  
**Status:** Current bounded application-architecture research  
**Scope:** Defines the smallest production-facing seam needed to execute Specification 009 RH-R/RH-A after the successful hybrid retrieval comparator. It does not select the final Horizon ranking/budget algorithm, LLM relevance judge, embedding implementation, or context assembler.  
**Design session:** 03  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 03 - Project Cockpit & V1 Integration

## 1. Evidence boundary

Retrieval now has three preserved result boundaries:

```text
Checkpoint 135
    production lexical retrieval
    RH-L Recall@3 1.00 / MRR 1.00
    RH-S Recall@3 0.75

Checkpoint 137
    exact dense-only comparator
    RH-S Recall@3 0.75
    complementary miss pattern

Checkpoint 139
    lexical+dense RRF comparator
    RH-S Recall@3 1.00 / MRR 0.875
    RH-L Recall@3 1.00 / MRR 1.00
```

The retrieval stage has therefore earned enough evidence to advance into the purpose for which it exists: a bounded project-specific methodological candidate set.

---

## 2. Do not make the Horizon depend on retrieval technology

The successful comparator used:

```text
SQLite FTS5
FastEmbed
BAAI/bge-small-en-v1.5
RRF(k=60)
```

None of those concepts belong in MethodologicalHorizon semantics.

The application boundary should receive only stable/revision-transparent candidate identities plus retrieval provenance such as channel/rank when useful.

Therefore:

```text
MethodologicalHorizon
    must not import FastEmbed
    must not know cosine similarity
    must not know FTS MATCH syntax
    must not know BM25
    must not know RRF formula
```

This keeps the successful hybrid result replaceable and preserves D-028's application/infrastructure separation.

---

## 3. The current persistence API is insufficient for RH-R/RH-A

The existing `KnowledgeRepository` can publish/read asset revisions and write relations/rules, but the application lacks targeted read operations for:

```text
accepted-current applicability metadata
accepted-current context requirements
accepted-current one-hop relations
related accepted-current asset identity
```

Using full accepted-snapshot export inside every Horizon construction would technically expose the information, but would recreate an undesirable pattern:

```text
load the global knowledge universe
-> filter in application memory every time
```

That contradicts the scaling direction established after V0.

The first Horizon slice should therefore add a targeted storage-neutral navigation read port instead of treating interchange export as the operational query API.

---

## 4. Minimal navigation read model

The application needs a revision-transparent projection for one accepted-current asset:

```text
NavigableKnowledgeAsset
    stable_key
    revision_id
    title
    applicability expression or null
    context requirements
```

and a one-hop related projection:

```text
RelatedKnowledgeAsset
    relation_revision_id
    relation_type
    stable_key
    revision_id
    title
```

These are read projections over governed knowledge. They are not new authoritative KnowledgeAsset or KnowledgeRelation identities.

The adapter must resolve only current accepted target asset revisions.

---

## 5. First relation-expansion semantics

Specification 009 freezes four RH-R cases whose expected relations are represented explicitly in the governed fixture:

```text
random-forest
    -> gradient-boosted-trees through ALTERNATIVE_TO
    -> bagging through USES_CONCEPT

temporal-validation
    -> prediction-moment through REQUIRES_CONCEPT

prediction-time-feature-eligibility
    -> prediction-moment through REQUIRES_CONCEPT

histogram
    -> ecdf through an explicit fixture relation
```

The first Horizon builder should use only:

```text
one-hop
outbound
current accepted relations
from direct seed candidates
```

Do not recursively expand relation-of-relation paths in this slice.

Why outbound only:

- the frozen RH-R cases are expressed as seed -> expected related concept;
- direction carries semantics for `REQUIRES_CONCEPT` and `USES_CONCEPT`;
- automatic bidirectional traversal could silently turn directional dependencies into symmetric associations;
- later evidence can introduce relation-type-specific symmetric traversal if needed.

---

## 6. Applicability is tri-state-plus, not a boolean filter

RH-A explicitly requires distinguishing negative evidence from unknown context.

The first application assessment states should be:

```text
POSSIBLY_APPLICABLE
INAPPLICABLE
MISSING_CONTEXT
```

Interpretation:

### POSSIBLY_APPLICABLE

Known hard applicability predicates do not reject the asset and required applicability/rule-evaluation context is available.

This does not mean `RELEVANT` or `RECOMMENDED`. It means the deterministic applicability layer has not excluded the asset.

### INAPPLICABLE

Known context makes a frozen applicability condition false.

This is stronger than low relevance. The asset should not remain in the active Horizon merely because retrieval ranked it highly.

### MISSING_CONTEXT

The asset cannot yet be safely classified because:

```text
an applicability predicate is unknown
or
an explicit context requirement needed for APPLICABILITY/RULE_EVALUATION is absent
```

The asset remains visible as deferred/clarification-needed rather than being converted into false inapplicability.

---

## 7. Initial expression evaluator scope

The reusable-knowledge interchange already represents applicability structurally.

For the first RH-A gate, deterministic evaluation may support the expression family actually present in the governed fixture:

```text
predicate
all
any
not
```

Predicate resolution rule for the first slice:

```text
predicate name -> known_context key
```

A missing predicate key produces UNKNOWN, not FALSE.

A boolean false produces FALSE.

A boolean true produces TRUE.

If a later knowledge revision introduces richer predicate arguments or comparison semantics, those require an explicit evaluator extension rather than accidental truthiness.

---

## 8. Context requirements participate separately from applicability expressions

A reusable asset may have `applicability = null` and still require context before a rule or applicability decision can be completed.

For the first Horizon gate, unresolved requirements whose `required_for` contains either:

```text
APPLICABILITY
RULE_EVALUATION
```

produce `MISSING_CONTEXT`.

This is needed for the frozen cases:

```text
class-imbalance
    missing class-prevalence

temporal-validation
    missing prediction-moment

prediction-time-feature-eligibility
    missing prediction-moment
```

---

## 9. First Horizon representation

A minimal candidate should explain why it is present:

```text
HorizonCandidate
    stable_key
    revision_id
    title
    origin
        DIRECT
        RELATION
    relation_type when relation-added
    applicability_state
    missing_context_keys
```

A first `MethodologicalHorizon` should preserve two sets:

```text
included
    POSSIBLY_APPLICABLE
    MISSING_CONTEXT

excluded
    INAPPLICABLE
```

Keeping `MISSING_CONTEXT` inside the visible Horizon is deliberate. It allows the system/human to see what must be clarified instead of losing a potentially important concern.

---

## 10. Why relevance/ranking is not included yet

Foundation 019 separates:

```text
KNOWN -> APPLICABLE -> RELEVANT -> RECOMMENDED
```

The current frozen RH-R/RH-A cases test relation expansion and applicability/context handling only.

Adding a heuristic or LLM relevance ranker now would make it harder to diagnose whether a failure came from:

```text
retrieval
relation expansion
applicability
relevance reasoning
```

The first builder should therefore stop after a bounded, explained applicability-aware Horizon.

A later RH-C/relevance gate can evaluate selective context and prioritization separately.

---

## 11. Production seam decision

Implement now:

```text
storage-neutral KnowledgeNavigationRepository
accepted-current asset navigation projection
accepted-current outbound relation projection
deterministic applicability evaluator
one-hop MethodologicalHorizon builder
```

Do not implement now:

```text
production FastEmbed adapter
persistent embedding cache
vector database
ANN
final hybrid retriever
recursive graph expansion
LLM relevance judge
final horizon budget
context assembler
```

This lets the system validate the methodological architecture downstream of retrieval while keeping the successful hybrid channel an independently replaceable retrieval hypothesis.

---

## 12. Exact next test

Execute the unchanged RH-R/RH-A cases from:

```text
tests/fixtures/retrieval/methodological_horizon_v1.json
```

Required behavior:

```text
RH-R01 random-forest
    includes bagging and gradient-boosted-trees by relation expansion

RH-R02 temporal-validation
    includes prediction-moment

RH-R03 prediction-time-feature-eligibility
    includes prediction-moment

RH-R04 histogram
    includes ecdf

RH-A01 random-forest + supervised/tabular true
    POSSIBLY_APPLICABLE

RH-A02 random-forest + supervised false
    INAPPLICABLE

RH-A03 class-imbalance + no context
    MISSING_CONTEXT

RH-A04 temporal-validation + no context
    MISSING_CONTEXT

RH-A05 prediction-time-feature-eligibility + no context
    MISSING_CONTEXT
```

The gate should also prove exact revision identity, accepted-current relation filtering, one-hop boundedness, and authoritative-state isolation.
