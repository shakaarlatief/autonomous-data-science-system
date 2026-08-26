# Checkpoint 141: First MethodologicalHorizon Cross-Platform Gate Passed

**Date:** 2026-08-22  
**Status:** Historical validated implementation checkpoint; Specification 012 v0.1 executed and passed  
**Checkpoint class:** IMPLEMENTATION / VALIDATION  
**Project stage:** Post-V0 V1 bounded implementation and integration  
**Scope:** Preserves the first production-facing accepted-current knowledge-navigation, one-hop relation-expansion, deterministic applicability/context-evaluation, and explained MethodologicalHorizon result.  
**Authority:** Historical validation evidence for Specification 012 v0.1. It promotes the bounded storage-neutral navigation/applicability seam, not final relevance ranking, recommendation policy, recursive graph expansion, final horizon size, context assembly, or production semantic-retrieval technology.  
**Design session:** 03  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 03 - Project Cockpit & V1 Integration  
**Associated branch:** `v1-semantic-retrieval`

## 1. Starting boundary

Checkpoint 140 froze Specification 012 v0.1 before implementation. The implementation then introduced a production-facing seam whose application layer is independent of retrieval-provider details.

The validated slice contains:

```text
KnowledgeNavigationRepository
    accepted-current asset navigation reads
    accepted-current outbound relation reads

deterministic applicability evaluator
    TRUE / FALSE / UNKNOWN internal truth
    POSSIBLY_APPLICABLE / INAPPLICABLE / MISSING_CONTEXT output

MethodologicalHorizon builder
    direct candidates
    one-hop outbound relation expansion
    current accepted revision checks
    duplicate collapse
    explained origin/state
    included vs excluded candidates
```

It does not depend on FTS5, BM25, FastEmbed, BGE, cosine similarity, RRF, or vector-store APIs.

---

## 2. Cross-platform gate

Observable workflow:

```text
V1 first MethodologicalHorizon builder
run 32561727632
PR merge-test commit 6b58245b41167b30f23895a0127ad2c22d44bac4
validated source branch product-code head be18458ba338f7d19094a736846828cb29371339

Ubuntu   PASS
Windows  PASS
```

Frozen benchmark result:

```text
RH-R relational cases       4 / 4 PASS
RH-A applicability cases    5 / 5 PASS
authoritative knowledge     unchanged
```

Locked V1 regression suite:

```text
Ubuntu   39 passed, 2 skipped
Windows  39 passed, 2 skipped
```

The skips are the existing PostgreSQL-dependent tests when `ADS_TEST_POSTGRES_URL` is not configured in this workflow. They are not Horizon failures.

---

## 3. RH-R relation-expansion result

The first builder returns only accepted-current, direct outbound, one-hop relations from direct seeds.

Observed required relations:

```text
RH-R01 random-forest
    USES_CONCEPT   -> bagging
    ALTERNATIVE_TO -> gradient-boosted-trees

RH-R02 temporal-validation
    REQUIRES_CONCEPT -> prediction-moment

RH-R03 prediction-time-feature-eligibility
    REQUIRES_CONCEPT -> prediction-moment

RH-R04 histogram
    ALTERNATIVE_TO -> ecdf
```

Every relation-added asset carries its exact current accepted asset revision ID and the exact accepted relation revision ID that justified expansion.

The gate also compares expansion against the authoritative accepted snapshot's direct outbound edges so an implementation cannot pass merely by returning the four expected keys while also performing accidental recursion or reverse traversal.

---

## 4. RH-A applicability/context result

Observed states:

```text
RH-A01 random-forest
    project.task.is_supervised = true
    data.representation.is_supported_tabular = true
    -> POSSIBLY_APPLICABLE

RH-A02 random-forest
    project.task.is_supervised = false
    data.representation.is_supported_tabular = true
    -> INAPPLICABLE

RH-A03 class-imbalance
    known context = {}
    -> MISSING_CONTEXT
       missing: class-prevalence

RH-A04 temporal-validation
    known context = {}
    -> MISSING_CONTEXT
       missing: prediction-moment

RH-A05 prediction-time-feature-eligibility
    known context = {}
    -> MISSING_CONTEXT
       missing: prediction-moment
```

This validates the key V1 semantic rule:

```text
unknown != false
```

Known negative applicability evidence can exclude an asset, while absent required information remains explicit and visible instead of being converted into false inapplicability.

---

## 5. Additional invariants validated

The implementation gate also validates:

```text
accepted-current asset revision exactness
accepted current relation-governance filtering
one-hop boundedness
no reverse relation inference
duplicate collapse
direct candidate precedence over relation origin
stale/unknown direct revision rejection
explicit rejection of non-boolean values in the frozen predicate subset
unsupported expression shapes fail explicitly
authoritative-state isolation
application/storage isolation
cross-platform deterministic behavior
existing V1 regression compatibility
```

No Horizon build/evaluation mutates reusable-knowledge governance, accepted pointers, relation state, or project state.

---

## 6. Promotion decision

Promote as the current bounded V1 application seam:

```text
storage-neutral KnowledgeNavigationRepository
accepted-current one-hop outbound relation expansion
three-valued applicability evaluation
explicit missing-context preservation
explained MethodologicalHorizon candidate origin/state
included vs excluded applicability partition
```

Do not promote from this checkpoint:

```text
FastEmbed or BGE as production dependency
RRF k=60 as permanent production fusion
embedding persistence
ANN / vector database
recursive relation expansion
relation-type-specific weighting
final relevance ranking
LLM relevance judge
final recommendation policy
final MethodologicalHorizon budget
selective context serialization
final context/token budget
```

The bounded architecture has earned continuation. The exact future ranking/context policy has not.

---

## 7. Next boundary

The next experiment should test the next distinct stage rather than expanding this builder opportunistically:

```text
explained MethodologicalHorizon
    -> relevance / prioritization
    -> selective context assembly
    -> exact revision coverage
    -> irrelevant-context cost
    -> serialized size / token burden
    -> omission of the global catalog
```

That gate must be frozen before implementation and should directly test the Prototype V0 scaling lesson:

```text
what the SYSTEM should remember
    !=
what the LLM should receive on every reasoning call
```

Primary evidence:

```text
docs/specifications/012_v1_first_methodological_horizon_builder.md
docs/checkpoints/140_first_methodological_horizon_builder_contract_frozen.md
experiments/retrieval/V1_METHODOLOGICAL_HORIZON_RESULT.md
.github/workflows/v1-first-methodological-horizon.yml
```
