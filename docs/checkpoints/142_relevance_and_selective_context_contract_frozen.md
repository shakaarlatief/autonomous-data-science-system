# Checkpoint 142: Relevance and Selective Context Contract Frozen

**Date:** 2026-08-22  
**Status:** Historical experiment-design checkpoint; Specification 013 v0.1 and RH-C fixture frozen before implementation  
**Checkpoint class:** DESIGN  
**Project stage:** Post-V0 V1 bounded implementation and integration  
**Scope:** Preserves the first task-profile relevance and selective methodological-context experiment before selector/context code exists.  
**Authority:** Historical preregistration provenance. Specification 013 v0.1 and `selective_context_v1.json` govern the first RH-C implementation until its result is preserved.  
**Design session:** 03  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 03 - Project Cockpit & V1 Integration  
**Associated branch:** `v1-relevance-selective-context`

## 1. Promoted starting boundary

PR #10 was merged into `v1-frontend-spike` at:

```text
9319ed9b0a401efa1be85c27a9ce4424a8ce5e1e
```

The current branch starts exactly from that merge commit:

```text
v1-relevance-selective-context
```

The promoted prerequisite seam already provides:

```text
production lexical retrieval
measured dense semantic complementarity
bounded hybrid retrieval evidence
accepted-current one-hop relation expansion
three-valued applicability/context evaluation
explained MethodologicalHorizon
```

---

## 2. Frozen first relevance hypothesis

Do not introduce an LLM relevance judge first.

The first hypothesis is:

```text
explicit task reasoning functions
    -> primary function matches inside Horizon
    -> bounded REQUIRES_CONCEPT support closure
    -> hard max_assets budget
    -> exact compact reasoning projection
    -> selective MethodologicalContextPack
```

System omission decisions remain outside the model-facing pack.

---

## 3. Frozen wide-Horizon stress fixture

New fixture:

```text
tests/fixtures/retrieval/selective_context_v1.json
```

The original accepted knowledge and retrieval benchmark fixtures are unchanged.

All four RH-C cases use six direct seeds:

```text
class-imbalance
histogram
missing-data
prediction-time-feature-eligibility
random-forest
temporal-validation
```

Expected one-hop expansion adds:

```text
bagging
ecdf
gradient-boosted-trees
prediction-moment
```

Expected included wide Horizon:

```text
10 assets
```

This is an adversarial context-selection stress harness, not a claim that normal retrieval should return the catalog.

---

## 4. Frozen RH-C target sets

```text
RH-C01 MODEL_OPTION
    gradient-boosted-trees
    random-forest

RH-C02 EVIDENCE_OPTION
    ecdf
    histogram

RH-C03 VALIDITY_CONSTRAINT
    prediction-time-feature-eligibility
    temporal-validation
    prediction-moment via REQUIRED_CONCEPT_SUPPORT

RH-C04 DECISION_FRAMEWORK
    class-imbalance
    missing-data
```

Every case has:

```text
max_assets = 3
```

Frozen aggregate unresolved context:

```text
RH-C01  []
RH-C02  []
RH-C03  [prediction-moment]
RH-C04  [class-prevalence, production-missingness]
```

---

## 5. Frozen acceptance gate

Across all cases:

```text
exact required stable-key coverage          = 1.00
exact required revision coverage            = 1.00
irrelevant selected assets                  = 0
selected assets                             <= 3
omitted candidates without system reason    = 0
```

Per case:

```text
selective bytes < full-Horizon control bytes
selective/full-Horizon byte ratio <= 0.65
selective bytes < global-catalog control bytes
```

Primary size metric is deterministic canonical UTF-8 bytes. Exact provider token counts are not claimed in this gate because no final model/tokenizer is selected.

---

## 6. Frozen architecture boundaries

The first implementation must add:

```text
relation_source_key provenance on relation Horizon candidates
exact current-accepted context read by stable_key + revision_id
compact reasoning-only knowledge projection
ContextSelectionResult with selected/omitted decisions
MethodologicalContextPack with selected knowledge only
canonical deterministic serialization + digest
```

The context projection must exclude retrieval cues/scores and operational audit metadata.

No application-level global accepted-snapshot scan may be used for production selection.

---

## 7. Non-selections

Do not promote or introduce merely to pass this gate:

```text
LLM relevance judge
embedding relevance reranker
learned ranker
opaque numeric relevance score
natural-language task classifier
recommendation policy
REQUIRED/BLOCKING policy
final Horizon budget
final provider token budget
production FastEmbed/BGE dependency
permanent production RRF implementation
ANN/vector database
recursive relation expansion
```

---

## 8. Exact continuation

```text
1. implement the storage-neutral exact context projection/read
2. implement deterministic task-profile selection
3. implement system selection report and model-facing pack separation
4. add canonical serializer
5. run frozen RH-C01..RH-C04 plus budget/staleness/invariant coverage
6. run Ubuntu + Windows
7. preserve the complete result before any threshold/policy tuning
8. only then decide whether the bounded selector earns promotion
```

Primary sources:

```text
docs/research/020_first_horizon_relevance_and_selective_context_gate_design.md
docs/specifications/013_v1_horizon_relevance_and_selective_context.md
tests/fixtures/retrieval/selective_context_v1.json
docs/checkpoints/141_first_methodological_horizon_cross_platform_gate_passed.md
```
