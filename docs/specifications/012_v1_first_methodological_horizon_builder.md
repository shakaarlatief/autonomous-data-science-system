# Specification 012: V1 First MethodologicalHorizon Builder

**Version:** 0.1  
**Date:** 2026-08-22  
**Status:** Frozen bounded implementation/evaluation contract before HorizonBuilder code  
**Scope:** First production application seam for accepted-current knowledge navigation, one-hop relation expansion, deterministic applicability/context assessment, and an explained bounded MethodologicalHorizon.  
**Authority:** Governs the first RH-R/RH-A implementation. It does not define final relevance ranking, recommendation policy, recursive graph expansion, final horizon size, context assembly, or production semantic retrieval technology.

## 1. Starting boundary

This specification begins after:

```text
Checkpoint 135
    production lexical retrieval validated

Checkpoint 137
    dense-only semantic comparator preserved

Checkpoint 139
    lexical+dense RRF comparator PASS
    RH-S Recall@3 1.00
    RH-S MRR 0.875
    RH-L Recall@3 1.00
    RH-L MRR 1.00
```

Retrieval has therefore earned advancement into the first downstream methodological-navigation stage.

---

## 2. Core architecture rule

The Horizon layer must depend on stable/revision-transparent methodological candidates and governed knowledge reads, not on retrieval implementation details.

Application/domain code must not import or reference:

```text
SQLite FTS5 MATCH syntax
BM25
FastEmbed
BAAI/bge-small-en-v1.5
cosine similarity
RRF formula
vector-store APIs
```

The first Horizon implementation must remain usable with lexical-only, hybrid, fake, or future retrieval providers.

---

## 3. Storage-neutral knowledge-navigation port

Introduce a targeted application read contract capable of:

```text
get_current_asset(stable_key)
    -> accepted-current navigable asset projection or None

get_outbound_related_assets(stable_key)
    -> accepted-current one-hop relation projections
```

### 3.1 Navigable asset projection

Expose at least:

```text
stable_key
revision_id
title
applicability
context_requirements
```

### 3.2 Related asset projection

Expose at least:

```text
relation_revision_id
relation_type
stable_key
revision_id
title
```

No SQLite row IDs, JSON storage encoding, SQLAlchemy types, or persistence table names may escape the adapter.

---

## 4. Accepted-current relation rule

Relation expansion may use only a current relation revision whose governance state is `ACCEPTED` and whose target asset has a current accepted revision.

The first builder traverses only:

```text
outbound
one hop
from direct seed candidates
```

It does not recursively expand newly relation-added assets.

It does not silently invert directional relations.

---

## 5. Horizon seed contract

The builder accepts storage-neutral direct candidates containing at least:

```text
stable_key
revision_id
title
retrieval_origin / provenance labels when available
```

The builder must verify that a direct candidate revision is still the current accepted revision before treating it as active methodological knowledge.

A stale or unknown candidate must not silently enter the Horizon.

For the frozen RH-R benchmark, a seed may be constructed from the current accepted asset directly because the cases start from a named seed rather than a query.

---

## 6. Applicability truth model

The deterministic evaluator uses internal three-valued condition truth:

```text
TRUE
FALSE
UNKNOWN
```

The externally visible first-slice applicability states are:

```text
POSSIBLY_APPLICABLE
INAPPLICABLE
MISSING_CONTEXT
```

### 6.1 Meaning

`POSSIBLY_APPLICABLE`:
- no known applicability condition rejects the asset;
- all context explicitly required for `APPLICABILITY` or `RULE_EVALUATION` is present;
- this does not assert relevance or recommendation.

`INAPPLICABLE`:
- known context makes the asset's applicability expression false.

`MISSING_CONTEXT`:
- an applicability predicate cannot be resolved from known context; or
- an explicit context requirement needed for `APPLICABILITY` or `RULE_EVALUATION` is absent.

Unknown must never be collapsed to false.

---

## 7. Frozen expression subset

Support only the expression structures needed by the current governed fixture:

```text
{"predicate": "context.key", "arguments": {}}
{"all": [expr, ...]}
{"any": [expr, ...]}
{"not": expr}
```

For a direct predicate:

```text
known_context[predicate] is True  -> TRUE
known_context[predicate] is False -> FALSE
predicate absent                  -> UNKNOWN
```

A present non-boolean value for this frozen direct-boolean predicate subset must raise an explicit evaluation error rather than using Python truthiness.

Unsupported expression shapes must also raise an explicit evaluation error.

Do not silently invent generic predicate semantics from predicate names.

---

## 8. Context requirement rule

For each asset, inspect accepted-current context requirements whose `required_for` includes:

```text
APPLICABILITY
RULE_EVALUATION
```

If the requirement key is absent from `known_context`, record it in `missing_context_keys`.

The first slice treats presence as the context-availability signal. It does not attempt to validate the semantic quality of an arbitrary supplied value.

---

## 9. Applicability resolution order

For an asset:

```text
1. evaluate applicability expression if present
2. if expression is FALSE -> INAPPLICABLE
3. collect UNKNOWN predicate keys
4. collect missing explicit context-requirement keys
5. if any unknown/missing key remains -> MISSING_CONTEXT
6. otherwise -> POSSIBLY_APPLICABLE
```

Known negative applicability evidence therefore takes precedence over unrelated missing context.

---

## 10. Horizon candidate representation

Each candidate must preserve:

```text
stable_key
revision_id
title
origin
    DIRECT
    RELATION
relation_type if relation-added
relation_revision_id if relation-added
applicability_state
missing_context_keys
```

Optional retrieval provenance may also be retained, but provider-specific score semantics are not required by this first builder.

---

## 11. First MethodologicalHorizon representation

The result must preserve two explicit groups:

```text
included
    POSSIBLY_APPLICABLE
    MISSING_CONTEXT

excluded
    INAPPLICABLE
```

`MISSING_CONTEXT` remains visible inside `included` because the first Horizon is also a navigation/clarification surface. It must not disappear as though the knowledge were irrelevant.

Candidates must be deterministically ordered:

```text
DIRECT before RELATION
then stable_key ascending
```

No final relevance score is introduced in this slice.

---

## 12. Frozen RH-R gate

Use unchanged cases from `methodological_horizon_v1.json`.

Required one-hop related keys:

```text
RH-R01 random-forest
    bagging
    gradient-boosted-trees

RH-R02 temporal-validation
    prediction-moment

RH-R03 prediction-time-feature-eligibility
    prediction-moment

RH-R04 histogram
    ecdf
```

Gate:

```text
all expected related keys present
0 missing expected relations
all related revisions are current accepted
all relation revisions are current accepted
no recursive second-hop expansion
```

Unexpected additional direct outbound accepted relations may be recorded, but the benchmark must preserve the exact related set returned so candidate growth remains visible.

---

## 13. Frozen RH-A gate

Required states:

```text
RH-A01 random-forest
context:
    project.task.is_supervised = true
    data.representation.is_supported_tabular = true
expected:
    POSSIBLY_APPLICABLE

RH-A02 random-forest
context:
    project.task.is_supervised = false
    data.representation.is_supported_tabular = true
expected:
    INAPPLICABLE

RH-A03 class-imbalance
context: {}
expected:
    MISSING_CONTEXT

RH-A04 temporal-validation
context: {}
expected:
    MISSING_CONTEXT

RH-A05 prediction-time-feature-eligibility
context: {}
expected:
    MISSING_CONTEXT
```

Gate:

```text
5 / 5 applicability states exact
missing context keys preserved for every MISSING_CONTEXT result
known false not converted to MISSING_CONTEXT
```

---

## 14. Additional invariants

### HB-01 Revision exactness
Every navigation asset and relation-added target carries its exact current accepted revision ID.

### HB-02 Governance filtering
Non-accepted relation revisions and non-current/non-accepted target asset revisions do not enter relation expansion.

### HB-03 One-hop boundedness
Relation-added candidates are not recursively expanded in v0.1.

### HB-04 Duplicate collapse
A stable key already present as a direct candidate is not duplicated when reached by a relation.

### HB-05 Direct authority over origin
If an asset is both direct and relation-reachable, its candidate origin remains `DIRECT` while relation provenance may be retained separately later.

### HB-06 Unknown is not false
Missing predicate/context data never produces `INAPPLICABLE` solely because it is missing.

### HB-07 Authoritative-state isolation
Building/evaluating a Horizon does not mutate reusable-knowledge governance, current pointers, relation state, or project state.

### HB-08 Storage isolation
Application/domain modules contain no SQLAlchemy, SQLite, FTS, or persistence schema imports.

### HB-09 Existing regression compatibility
The locked existing V1 Python suite remains green.

### HB-10 Cross-platform execution
The RH-R/RH-A gate passes on Ubuntu and Windows.

---

## 15. Result observability

Persist/print enough evidence to diagnose failures:

```text
benchmark case
seed/asset key
known context
current revision ID
applicability expression summary
missing context keys
applicability state
outbound relation type/revision
related stable key/revision
included horizon keys
excluded horizon keys
```

The result artifact must distinguish:

```text
DIRECT
RELATION
POSSIBLY_APPLICABLE
MISSING_CONTEXT
INAPPLICABLE
```

---

## 16. Explicit non-goals

Do not add in this slice:

```text
production FastEmbed/BGE integration
RRF production implementation
embedding persistence
ANN/vector database
relation recursion
relation-type-specific weights
LLM relevance judgment
heuristic relevance score
recommendation state
required/blocking state
final horizon budget
selective context serialization
runtime/model calls
```

---

## 17. Advancement rule

If RH-R/RH-A pass:

1. preserve the result;
2. promote the storage-neutral navigation/applicability seam if it remains appropriately bounded;
3. then define a separate relevance/selective-context gate over the explained Horizon;
4. integrate the leading hybrid retriever only when a real production retrieval provider is needed by that vertical slice.

If RH-R or RH-A fail, repair the navigation/applicability layer before introducing relevance reasoning.

---

## 18. Primary evidence

```text
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
docs/specifications/009_v1_retrieval_and_methodological_horizon_benchmark.md
docs/research/019_first_methodological_horizon_application_seam.md
docs/checkpoints/139_rrf_hybrid_retrieval_cross_platform_gate_passed.md
experiments/retrieval/V1_RRF_HYBRID_RETRIEVAL_RESULT.md
```