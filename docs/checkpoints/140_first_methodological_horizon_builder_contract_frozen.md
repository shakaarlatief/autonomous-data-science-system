# Checkpoint 140: First MethodologicalHorizon Builder Contract Frozen

**Date:** 2026-08-22  
**Status:** Historical experiment-design checkpoint; Specification 012 v0.1 frozen before HorizonBuilder implementation  
**Checkpoint class:** DESIGN  
**Project stage:** Post-V0 V1 bounded implementation and integration  
**Scope:** Preserves the successful hybrid retrieval boundary and freezes the first production knowledge-navigation, relation-expansion, and applicability-aware MethodologicalHorizon slice before implementation.  
**Authority:** Historical preregistration provenance. Specification 012 v0.1 governs the first RH-R/RH-A implementation until its result is preserved.  
**Design session:** 03  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 03 - Project Cockpit & V1 Integration

## 1. Starting boundary

Checkpoint 139 passes the first bounded hybrid retrieval comparator:

```text
RH-S Recall@3  1.00
RH-S MRR       0.875
RH-L Recall@3  1.00
RH-L MRR       1.00
```

The immediate next question is no longer whether the ten-asset corpus can be retrieved. It is whether retrieved/seeded knowledge can be transformed into an explained applicability-aware MethodologicalHorizon without conflating retrieval, relation expansion, applicability, and relevance.

---

## 2. Frozen architecture boundary

The first Horizon slice must be independent of retrieval technology.

The application layer receives stable/revision-transparent knowledge identities and reads governed navigation semantics through a storage-neutral port.

It must not depend on:

```text
FTS5
BM25
FastEmbed
BGE
cosine similarity
RRF
vector infrastructure
```

---

## 3. Frozen implementation scope

Implement:

```text
KnowledgeNavigationRepository
    accepted-current asset navigation reads
    accepted-current outbound relation reads

deterministic applicability evaluator
    TRUE / FALSE / UNKNOWN internal truth
    POSSIBLY_APPLICABLE / INAPPLICABLE / MISSING_CONTEXT output

MethodologicalHorizon builder
    direct seeds
    one-hop outbound relation expansion
    no recursive expansion
    explained candidate origins
    included vs excluded states
```

Do not implement relevance ranking or context assembly yet.

---

## 4. Frozen RH-R gate

```text
RH-R01 random-forest
    -> bagging
    -> gradient-boosted-trees

RH-R02 temporal-validation
    -> prediction-moment

RH-R03 prediction-time-feature-eligibility
    -> prediction-moment

RH-R04 histogram
    -> ecdf
```

All returned relation and asset revisions must be current accepted.

---

## 5. Frozen RH-A gate

```text
RH-A01 random-forest + supervised/tabular true
    POSSIBLY_APPLICABLE

RH-A02 random-forest + supervised false
    INAPPLICABLE

RH-A03 class-imbalance + empty context
    MISSING_CONTEXT

RH-A04 temporal-validation + empty context
    MISSING_CONTEXT

RH-A05 prediction-time-feature-eligibility + empty context
    MISSING_CONTEXT
```

Unknown context must not collapse to false.

---

## 6. Promotion audit

Promote now:

```text
Research 019
    current application-seam rationale

Specification 012 v0.1
    frozen first HorizonBuilder contract

Checkpoint 140
    historical preregistration boundary
```

Do not promote:

```text
FastEmbed/BGE as production dependency
RRF as permanent fusion architecture
recursive relation expansion
final relation semantics
LLM relevance ranking
final MethodologicalHorizon size/budget
selective context assembly
```

---

## 7. Exact continuation

Implement Specification 012, then execute RH-R/RH-A and the locked V1 regression suite on Ubuntu and Windows.

Preserve the complete result before adding relevance or selective-context reasoning.

Primary sources:

```text
docs/specifications/012_v1_first_methodological_horizon_builder.md
docs/research/019_first_methodological_horizon_application_seam.md
docs/checkpoints/139_rrf_hybrid_retrieval_cross_platform_gate_passed.md
experiments/retrieval/V1_RRF_HYBRID_RETRIEVAL_RESULT.md
```