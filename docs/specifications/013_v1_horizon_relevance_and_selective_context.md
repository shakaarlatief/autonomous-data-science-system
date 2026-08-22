# Specification 013: V1 Horizon Relevance and Selective Context

**Version:** 0.1  
**Date:** 2026-08-22  
**Status:** Frozen bounded implementation/evaluation contract before relevance/context code  
**Scope:** First deterministic task-profile relevance filter, bounded required-concept support closure, exact-revision methodological context projection, system-facing omission observability, and RH-C context-size/coverage evaluation.  
**Authority:** Governs the first RH-C implementation until its result is preserved. It does not define final semantic relevance judgment, recommendation policy, required/blocking policy, final Horizon budget, final LLM context budget, or production semantic-retrieval infrastructure.

## 1. Starting boundary

This specification begins from the promoted PR #10 merge boundary:

```text
v1-frontend-spike
9319ed9b0a401efa1be85c27a9ce4424a8ce5e1e
```

The active implementation branch is:

```text
v1-relevance-selective-context
```

Prerequisite evidence:

```text
Checkpoint 135
    production lexical retrieval PASS

Checkpoint 137
    dense-only semantic comparator preserved

Checkpoint 139
    complementary lexical+dense RRF comparator PASS

Checkpoint 141
    first storage-neutral one-hop/applicability-aware MethodologicalHorizon PASS
```

The next frozen question is:

> Can an explicit task profile reduce a deliberately wide explained Horizon to a small exact-revision methodological context pack without losing required knowledge or leaking the whole Horizon/catalog into the model-facing payload?

---

## 2. Governing architectural constraints

Preserve Foundations 019-020 and the Prototype V0 scaling lesson:

```text
what the SYSTEM should remember
    !=
what the LLM should receive on every reasoning call
```

The implementation must preserve these separations:

```text
retrieval != applicability
applicability != relevance
relevance != recommendation
system observability != model-facing context
knowledge storage != context serialization
```

No LLM call participates in the frozen first selector.

---

## 3. Input contract

The first selector consumes:

```text
MethodologicalHorizon
MethodologicalContextRequest
```

The request contains exactly:

```text
task_id: str
requested_reasoning_functions: tuple[str, ...]
max_assets: int
```

Requirements:

```text
task_id non-empty
requested_reasoning_functions non-empty
function names non-empty and deduplicated
max_assets > 0
```

The caller supplying reasoning functions is part of this frozen slice. How a future system derives those functions from natural-language/project semantics remains outside this specification.

---

## 4. Horizon provenance extension

Add one storage-neutral field to `HorizonCandidate`:

```text
relation_source_key: str | None
```

Rules:

```text
DIRECT candidate
    relation_source_key = None

RELATION candidate
    relation_source_key = stable key of the direct Horizon seed
                          whose accepted outbound relation introduced it
```

This is an explainability extension only. Specification 012's one-hop/outbound/accepted-current traversal remains unchanged.

When multiple direct sources reach the same related stable key, the existing deterministic first-reached relation provenance remains the first-slice behavior. Multi-edge provenance is not introduced here.

---

## 5. Exact accepted-current context read contract

Extend the storage-neutral knowledge-navigation boundary with an exact context read conceptually equivalent to:

```text
get_context_asset(stable_key: str, revision_id: str)
    -> ContextKnowledgeAsset | None
```

The adapter must return content only when:

```text
stable_key exists
revision_id is exactly the current accepted asset revision
```

A stale/historical revision must not be silently substituted with current content.

The application layer must not use global accepted-snapshot export as its operational context API.

---

## 6. Compact reasoning projection

`ContextKnowledgeAsset` must expose only reasoning-relevant, revision-transparent content needed by the first pack.

Required fields:

```text
stable_key
revision_id
title
intrinsic_kind
purpose
scope
reasoning_functions
context_requirements
semantic_checks
limitations
narrative_facets
accepted components
rules
```

### 6.1 Component projection

For accepted components belonging to the exact selected parent asset revision:

```text
component_key
revision_id
component_kind
body
reasoning_functions
```

Only components with accepted governance may be serialized.

### 6.2 Narrative facet projection

```text
facet_kind
body
position
```

### 6.3 Rule projection

```text
rule_spec_id
rule_key
condition
consequence_type
consequence_payload
force
unknown_behavior
rationale
```

### 6.4 Explicit exclusions from model-facing projection

Do not serialize merely because the data exists:

```text
retrieval lexical terms
aliases
semantic retrieval cues
negative retrieval cues
retrieval scores
asset UUID when stable/revision identity suffices
component UUID when component key/revision identity suffices
provenance source lists / locators
governance event prose
timestamps
collection membership
SQLite / SQLAlchemy implementation details
```

Retrieval metadata is not reasoning context.

---

## 7. Frozen relevance policy

### 7.1 Candidate universe

Only `horizon.included` participates in relevance selection.

`horizon.excluded` candidates remain available to system observability but cannot enter the model-facing pack in this first policy.

### 7.2 Primary match

A candidate is a primary task match when:

```text
set(asset.reasoning_functions)
    intersects
set(request.requested_reasoning_functions)
```

Selection reason:

```text
PRIMARY_FUNCTION_MATCH
```

### 7.3 Required-concept support closure

After primary matches are identified, a relation-added Horizon candidate is a support match only when:

```text
candidate.relation_type == "REQUIRES_CONCEPT"
and
candidate.relation_source_key is in the primary selected stable keys
```

Selection reason:

```text
REQUIRED_CONCEPT_SUPPORT
```

Do not automatically include `USES_CONCEPT`, `ALTERNATIVE_TO`, `COMPLEMENTS`, or other relation types.

A candidate that independently matches the requested reasoning functions remains a primary match regardless of relation type.

### 7.4 No recursion

Support closure does not traverse relations again. It only selects already-present one-hop Horizon candidates.

---

## 8. Frozen deterministic ordering and budget

Candidate priority:

```text
1. PRIMARY_FUNCTION_MATCH
2. REQUIRED_CONCEPT_SUPPORT
```

Within the same priority:

```text
DIRECT before RELATION
stable_key ascending
```

Then apply:

```text
request.max_assets
```

Candidates that are relevant under the policy but fall outside the hard limit receive system-facing omission reason:

```text
BUDGET_LIMIT
```

No numeric relevance score is introduced.

---

## 9. System-facing selection result

The first application result is conceptually:

```text
ContextSelectionResult
    request
    pack
    decisions
```

Every Horizon candidate receives an inspectable decision.

Required decision reasons include:

Selected:

```text
PRIMARY_FUNCTION_MATCH
REQUIRED_CONCEPT_SUPPORT
```

Omitted:

```text
NO_REASONING_FUNCTION_MATCH
BUDGET_LIMIT
INAPPLICABLE
```

For candidates in `horizon.excluded`, use `INAPPLICABLE`.

The result may preserve Horizon origin/applicability/missing-context state for observability.

---

## 10. Model-facing MethodologicalContextPack

The model-facing pack contains selected knowledge only.

Required envelope:

```text
schema_version = 1
task_id
requested_reasoning_functions
selected knowledge items
aggregate missing_context_keys
```

Each selected knowledge item includes:

```text
compact exact ContextKnowledgeAsset projection
Horizon origin
applicability_state
missing_context_keys
relation_source_key / relation_type / relation_revision_id when relation-added
selection_reason
```

The pack must not include omission decisions or names/content of omitted Horizon candidates.

This is a deliberate system/model boundary:

```text
system remembers why 8 candidates were omitted
model receives only the 2 selected candidates
```

---

## 11. Canonical serialization

Provide deterministic serialization for the pack:

```text
UTF-8 JSON
sorted mapping keys
compact separators
stable list ordering from the selection policy
ensure_ascii = false
newline not required
```

Record:

```text
UTF-8 byte count
Unicode character count
SHA-256 digest
```

Do not add a provider tokenizer dependency in this gate.

A model-specific exact token count is deferred to the first real runtime/model vertical slice.

---

## 12. Frozen wide-Horizon stress setup

Use the unchanged accepted knowledge fixture:

```text
tests/fixtures/knowledge/reusable_knowledge_stress_v1.json
```

Do not edit that fixture for RH-C.

Use a new scenario fixture:

```text
tests/fixtures/retrieval/selective_context_v1.json
```

Every RH-C case builds the same wide Horizon from six direct accepted-current seeds:

```text
class-imbalance
histogram
missing-data
prediction-time-feature-eligibility
random-forest
temporal-validation
```

The accepted one-hop graph should add:

```text
bagging
ecdf
gradient-boosted-trees
prediction-moment
```

Expected wide-Horizon included count:

```text
10
```

Common known context contains only:

```text
project.task.is_supervised = true
data.representation.is_supported_tabular = true
```

This resolves Random Forest's frozen applicability predicate while deliberately leaving class-prevalence, production-missingness, and prediction-moment context unresolved.

The setup is a context-selection stress case, not an expected production retrieval pattern.

---

## 13. Frozen RH-C cases

All cases use:

```text
max_assets = 3
```

### RH-C01 model-option reasoning

```text
requested_reasoning_functions:
    MODEL_OPTION

required selected keys:
    gradient-boosted-trees
    random-forest

required aggregate missing_context_keys:
    []
```

### RH-C02 empirical-distribution evidence

```text
requested_reasoning_functions:
    EVIDENCE_OPTION

required selected keys:
    ecdf
    histogram

required aggregate missing_context_keys:
    []
```

### RH-C03 predictive-validity constraints

```text
requested_reasoning_functions:
    VALIDITY_CONSTRAINT

required selected keys:
    prediction-moment
    prediction-time-feature-eligibility
    temporal-validation

selection expectation:
    prediction-time-feature-eligibility  PRIMARY_FUNCTION_MATCH
    temporal-validation                  PRIMARY_FUNCTION_MATCH
    prediction-moment                    REQUIRED_CONCEPT_SUPPORT

required aggregate missing_context_keys:
    prediction-moment
```

### RH-C04 data-quality decision frameworks

```text
requested_reasoning_functions:
    DECISION_FRAMEWORK

required selected keys:
    class-imbalance
    missing-data

required aggregate missing_context_keys:
    class-prevalence
    production-missingness
```

Expected key sets are frozen before running the implementation.

---

## 14. Frozen quality gates

Across RH-C01 through RH-C04:

```text
exact required stable-key coverage          = 1.00
exact required revision coverage            = 1.00
irrelevant selected asset count             = 0
selected asset count per case               <= 3
omitted Horizon candidates missing a reason = 0
```

For every case:

```text
selective serialized bytes < full-Horizon control bytes
selective/full-Horizon byte ratio <= 0.65
selective serialized bytes < global-catalog control bytes
```

The full-Horizon and global controls use the same compact reasoning projection and same task envelope so the size comparison is not distorted by different schemas.

The deliberately wide benchmark currently expects the full included Horizon and accepted catalog both to contain ten assets, but they remain distinct conceptual controls in the harness.

---

## 15. Non-quality invariants

### RC-01 Exact revision identity
Every selected item uses the exact revision in its Horizon candidate and that revision is still current accepted when context is read.

### RC-02 Stale context fail-closed
A stale or unavailable exact revision raises an explicit error. The assembler never silently substitutes another revision.

### RC-03 No global scan in production selection
The production selector obtains context only through exact candidate reads. It has no application-level list-all/global-export dependency.

### RC-04 Omitted knowledge absent from model pack
System omission decisions do not leak omitted candidates into serialized model-facing context.

### RC-05 Missing context preserved
Selected `MISSING_CONTEXT` candidates retain their missing keys, and the pack exposes the sorted unique aggregate.

### RC-06 Inapplicable excluded
No `INAPPLICABLE` Horizon candidate enters the first pack.

### RC-07 Required-concept closure bounded
Only already-present relation candidates of type `REQUIRES_CONCEPT` whose recorded source is a primary match are auto-included.

### RC-08 Deterministic serialization
Repeated assembly from unchanged inputs yields identical serialized bytes and SHA-256 digest.

### RC-09 Retrieval metadata omitted
The context pack contains no lexical terms, aliases, semantic retrieval cues, retrieval scores, or provider-specific ranking metadata.

### RC-10 Authoritative-state isolation
Selection/context assembly performs no authoritative knowledge/project writes.

### RC-11 Storage isolation
Application modules contain no SQLAlchemy/persistence-schema imports.

### RC-12 Regression compatibility
The existing locked V1 Python suite remains green.

### RC-13 Cross-platform
The RH-C gate passes on Ubuntu and Windows under Python 3.13.

### RC-14 Budget overflow explicit
Separate unit coverage proves a relevant candidate beyond `max_assets` is omitted as `BUDGET_LIMIT`, not silently dropped.

---

## 16. Benchmark observability

The RH-C result must record per case:

```text
case_id
task_id
wide Horizon keys/revisions
requested reasoning functions
selected keys/revisions
selection reasons
omitted keys and system-facing reasons
aggregate missing-context keys
selected asset count
full Horizon asset count
global accepted asset count
selective UTF-8 bytes
full-Horizon control UTF-8 bytes
global-control UTF-8 bytes
selective/full-Horizon ratio
canonical SHA-256 digest
```

Do not print/serialize omitted full knowledge content as part of the model-facing pack merely for benchmark logging.

---

## 17. Explicit non-goals

Do not implement in this slice:

```text
LLM relevance judgment
semantic embedding reranking
learned ranking
opaque relevance score
natural-language task -> reasoning-function inference
recommendation state
required/blocking state
final project-wide Horizon budget
provider-specific model token budget
production semantic retriever integration
FastEmbed/BGE production dependency
permanent RRF production implementation
ANN/vector database
recursive relation expansion
open-world concern discovery
runtime/model calls
```

---

## 18. Advancement rule

If all frozen RH-C gates pass:

```text
1. preserve the complete result
2. promote the bounded task-profile ContextSelectionResult / MethodologicalContextPack seam
3. reconcile Q-044/Q-045/Q-029
4. connect one real reasoning vertical slice through the ADS-owned ReasoningRuntime
5. evaluate selective context versus a strong simple context control under one concrete model
6. measure exact provider tokens only in that model-specific experiment
```

If RH-C fails:

```text
1. preserve the failed result before tuning
2. classify metadata, task-profile, relation-support, budget, or serialization failure
3. repair the smallest demonstrated defect
4. consider LLM relevance only if deterministic task semantics prove insufficient
```

---

## 19. Primary sources

```text
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
docs/specifications/009_v1_retrieval_and_methodological_horizon_benchmark.md
docs/specifications/012_v1_first_methodological_horizon_builder.md
docs/checkpoints/141_first_methodological_horizon_cross_platform_gate_passed.md
docs/research/020_first_horizon_relevance_and_selective_context_gate_design.md
```
