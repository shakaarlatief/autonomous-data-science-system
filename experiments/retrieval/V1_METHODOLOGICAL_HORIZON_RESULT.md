# V1 First MethodologicalHorizon Result

**Date:** 2026-08-22  
**Status:** PASS  
**Specification:** `docs/specifications/012_v1_first_methodological_horizon_builder.md` v0.1  
**Validated source head:** `be18458ba338f7d19094a736846828cb29371339`  
**GitHub Actions workflow:** `V1 first MethodologicalHorizon builder`  
**Run:** `32561727632`

## 1. Implemented production-facing seam

The validated slice introduces:

```text
storage-neutral KnowledgeNavigationRepository
    get_current_asset
    get_outbound_related_assets

accepted-current SQLAlchemy navigation adapter

deterministic applicability evaluator
    internal TRUE / FALSE / UNKNOWN
    external POSSIBLY_APPLICABLE / INAPPLICABLE / MISSING_CONTEXT

first MethodologicalHorizon builder
    revision-transparent direct seeds
    one-hop outbound relation expansion
    explicit included / excluded groups
    direct-vs-relation origin
    visible missing-context requirements
```

The application layer does not depend on FTS5, BM25, FastEmbed, BGE, cosine similarity, RRF, or vector infrastructure.

## 2. Cross-platform gate

```text
Ubuntu frozen RH-R/RH-A gate     PASS
Ubuntu locked V1 regression      PASS, 39 passed / 2 skipped

Windows frozen RH-R/RH-A gate    PASS
Windows locked V1 regression     PASS, 39 passed / 2 skipped
```

Both operating systems produced the same stable keys, revision IDs, relation revision IDs, relation types, applicability states, and missing-context keys.

## 3. Relational Horizon gate

All four frozen RH-R cases passed.

### RH-R01: Random Forest

```text
seed
    random-forest
    revision fefb0b89-52b5-4353-9eb0-331670c9211c

one-hop accepted-current relations
    USES_CONCEPT
        bagging
        relation revision 6cad4578-74fc-4781-8ebf-dac78eb8389d
        asset revision f0341774-efbb-48a7-b3c7-94820857c7e8

    ALTERNATIVE_TO
        gradient-boosted-trees
        relation revision f2891407-ec31-4b52-ace3-0eca528f1694
        asset revision 1b9604fc-6cdb-4ff5-b4de-7aafaa157d89
```

Both relation-added assets evaluate as `POSSIBLY_APPLICABLE` under the empty benchmark context because neither has a hard applicability/context blocker in the current accepted revision.

### RH-R02: Temporal Validation

```text
seed temporal-validation
    -> REQUIRES_CONCEPT
    -> prediction-moment

relation revision
    37460b32-740d-4eb6-9501-7ab192a4e65b

target revision
    4a3189bb-b007-4efd-a2bd-04a8cc6a4d5c
```

### RH-R03: Prediction-Time Feature Eligibility

```text
seed prediction-time-feature-eligibility
    -> REQUIRES_CONCEPT
    -> prediction-moment

relation revision
    71d4728a-78e2-4446-a786-b062287fee34

target revision
    4a3189bb-b007-4efd-a2bd-04a8cc6a4d5c
```

### RH-R04: Histogram

```text
seed histogram
    -> ALTERNATIVE_TO
    -> ecdf

relation revision
    c59b7821-745d-48a8-a06c-d427065fc8e0

target revision
    9b6b4a84-526f-4fba-9036-13ad3cc00896
```

For every RH-R case, the relation-added candidate set exactly matched the authoritative accepted snapshot's direct outbound asset relations. This validates one-hop boundedness and rejects accidental reverse or recursive expansion on the frozen graph.

## 4. Applicability/context gate

All five frozen RH-A cases passed exactly.

```text
RH-A01 random-forest
context:
    project.task.is_supervised = true
    data.representation.is_supported_tabular = true
result:
    POSSIBLY_APPLICABLE

RH-A02 random-forest
context:
    project.task.is_supervised = false
    data.representation.is_supported_tabular = true
result:
    INAPPLICABLE

RH-A03 class-imbalance
context: {}
result:
    MISSING_CONTEXT
missing:
    class-prevalence

RH-A04 temporal-validation
context: {}
result:
    MISSING_CONTEXT
missing:
    prediction-moment

RH-A05 prediction-time-feature-eligibility
context: {}
result:
    MISSING_CONTEXT
missing:
    prediction-moment
```

The result demonstrates the intended epistemic distinction:

```text
known false applicability
    !=
missing information
```

Unknown/missing context is not collapsed to false and therefore does not silently remove potentially important methodological knowledge.

## 5. Additional invariants validated

```text
candidate-before-acceptance navigation unavailable          PASS
exact current accepted asset revision identity             PASS
current accepted relation revision identity                PASS
accepted-current target filtering                          PASS
one-hop outbound expansion                                  PASS
duplicate stable-key collapse                               PASS
direct origin wins over relation duplicate                 PASS
stale direct revision rejected explicitly                  PASS
ambiguous non-boolean predicate value rejected explicitly  PASS
known INAPPLICABLE candidate preserved in excluded group    PASS
authoritative knowledge unchanged                          PASS
application/storage separation retained                    PASS
```

## 6. Architectural interpretation

The first downstream stage after retrieval has earned its complexity on the frozen benchmark.

The validated decomposition is now executable:

```text
retrieval / direct seeds
    -> accepted-current identity verification
    -> one-hop governed relation expansion
    -> deterministic applicability/context assessment
    -> explained MethodologicalHorizon
```

The result supports retaining `MISSING_CONTEXT` inside the visible Horizon. This makes unresolved prerequisites available for clarification or later reasoning instead of losing them as though they were irrelevant.

The result does not yet evaluate:

```text
RELEVANT
RECOMMENDED
REQUIRED / BLOCKING
final Horizon budget
LLM relevance reasoning
selective task-specific context
context token/byte cost
recommendation quality
```

## 7. Retrieval technology remains below the boundary

Checkpoint 139 established hybrid lexical+dense retrieval as the leading V1 retrieval hypothesis for the frozen corpus.

This Horizon result deliberately does not make the Horizon depend on that implementation. Therefore the following remain unpromoted:

```text
FastEmbed as production package
BGE-small as final embedding model
RRF as permanent fusion algorithm
vector persistence
ANN/vector database
```

The first application seam can consume candidates from lexical-only, hybrid, fake, or future retrieval providers.

## 8. Next step

The next evidence gate should move one stage further through Foundation 019:

```text
APPLICABLE / MISSING_CONTEXT Horizon
    -> relevance/prioritization
    -> selective context assembly
```

That gate should measure context coverage and cost separately from retrieval and applicability, rather than immediately adding more retrieval machinery.
