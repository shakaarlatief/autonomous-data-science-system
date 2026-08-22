# Specification 013: V1 Horizon Relevance and Selective Context

**Version:** 1.0  
**Date:** 2026-08-22  
**Status:** Accepted bounded V1 application seam after successful RH-C validation  
**Scope:** Deterministic task-profile relevance filtering, bounded required-concept support closure, exact-revision methodological context projection, system-facing omission observability, hard context budgeting, and canonical model-facing context serialization.  
**Authority:** Governs the accepted first V1 `MethodologicalHorizon -> ContextSelectionResult -> MethodologicalContextPack` seam. It does not define final semantic relevance judgment, natural-language task interpretation, recommendation policy, REQUIRED/BLOCKING policy, universal Horizon/context budgets, final LLM provider/model, or production semantic-retrieval infrastructure.  
**Promoted by:** Checkpoint 143 after the frozen v0.1 RH-C contract passed without target or threshold changes.

## 1. Accepted boundary

This specification began from the promoted retrieval/Horizon boundary:

```text
v1-frontend-spike
9319ed9b0a401efa1be85c27a9ce4424a8ce5e1e
```

The implementation and promotion branch is:

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

Checkpoint 142
    this selector/context contract frozen as v0.1 before implementation

Checkpoint 143
    frozen RH-C gate passed and bounded promotion authorized
```

Accepted question answered by this specification:

> Given an already-built explained `MethodologicalHorizon` and an explicit task profile naming the reasoning functions needed for the current reasoning step, can ADS construct a small exact-revision methodological context pack while retaining system-side omission evidence and avoiding serialization of the whole Horizon/catalog into the model-facing payload?

For the frozen RH-C corpus, the answer is yes.

---

## 2. Governing architectural constraints

Preserve Foundations 019-020 and Prototype V0's strongest scaling lesson:

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
methodological knowledge != runtime/provider state
```

No LLM call participates in this accepted first selector.

The accepted seam is deliberately minimum-complexity. A future semantic relevance stage may be added only when downstream evidence demonstrates that explicit task semantics are insufficient.

---

## 3. Input contract

The selector consumes:

```text
MethodologicalHorizon
MethodologicalContextRequest
```

The request contains:

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

The caller supplying reasoning functions is part of this bounded seam.

Still outside scope:

```text
natural-language task -> reasoning-function inference
project-object state -> reasoning-function inference
LLM task interpretation
learned task classifiers
```

Those mechanisms require separate evidence rather than being hidden inside context selection.

---

## 4. Horizon provenance contract

`HorizonCandidate` includes:

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

This field exists so the selector can distinguish relation-added conceptual support from independent primary matches.

Specification 012's accepted traversal remains unchanged:

```text
accepted-current
outbound
one-hop
relation-bounded
```

No recursive graph expansion is introduced by this specification.

When multiple direct sources reach the same related stable key, the existing deterministic first-reached provenance remains the accepted first-slice behavior. Multi-edge provenance remains open.

---

## 5. Exact accepted-current context read

The storage-neutral navigation boundary supports an exact context read conceptually equivalent to:

```text
get_context_asset(stable_key: str, revision_id: str)
    -> ContextKnowledgeAsset | None
```

Content is returned only when:

```text
stable_key exists
revision_id is exactly the current accepted revision
```

A stale, historical, missing, or mismatched revision must fail closed. The assembler must never silently substitute a newer revision.

The application layer must not operationally assemble context by scanning a global accepted-snapshot export.

The accepted ordering is:

```text
Horizon identities
    -> relevance/budget selection
    -> exact context reads for selected candidates only
```

This ensures a candidate omitted by budget does not have full reasoning content materialized merely to be discarded.

---

## 6. Compact reasoning projection

`ContextKnowledgeAsset` exposes reasoning-relevant, revision-transparent content for selected knowledge.

Required asset fields:

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

### 6.1 Accepted component projection

For accepted components belonging to the exact selected parent revision:

```text
component_key
revision_id
component_kind
body
reasoning_functions
```

Only accepted-governance components may be serialized.

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

### 6.4 Explicit exclusions

The model-facing projection must not serialize merely because data exists:

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
provider-specific ranking metadata
```

Retrieval and operational audit metadata are not reasoning context.

---

## 7. Accepted deterministic relevance policy

### 7.1 Candidate universe

Only:

```text
horizon.included
```

participates in relevance selection.

`horizon.excluded` remains system-observable but cannot enter this first model-facing pack.

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

### 7.3 Required-concept support

After primary matches are identified, an already-present relation-added Horizon candidate is a support match only when:

```text
candidate.relation_type == "REQUIRES_CONCEPT"
and
candidate.relation_source_key is in the primary selected stable keys
```

Selection reason:

```text
REQUIRED_CONCEPT_SUPPORT
```

Do not automatically include relation candidates only because they are connected through:

```text
USES_CONCEPT
ALTERNATIVE_TO
COMPLEMENTS
```

or any other relation type.

A relation-added candidate that independently matches a requested reasoning function remains a primary match.

### 7.4 No recursion

Support closure selects only already-present one-hop Horizon candidates. It does not traverse relations again.

### 7.5 Interpretation limit

Selected means:

```text
task-relevant under this bounded explicit policy
```

It does **not** mean:

```text
RECOMMENDED
REQUIRED
BLOCKING
universally most important
```

Those are later Foundation 019 stages.

---

## 8. Deterministic ordering and hard budget

Priority:

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

A relevant candidate beyond the hard limit receives system-facing omission reason:

```text
BUDGET_LIMIT
```

It must not be silently dropped.

The validated benchmark used `max_assets = 3`, but this value is an experiment constant, not a universal product budget.

No numeric relevance score is introduced by this seam.

---

## 9. System-facing selection result

The accepted application result is conceptually:

```text
ContextSelectionResult
    request
    pack
    decisions
```

Every Horizon candidate receives an inspectable system-side decision.

Required selected reasons:

```text
PRIMARY_FUNCTION_MATCH
REQUIRED_CONCEPT_SUPPORT
```

Required omission reasons include:

```text
NO_REASONING_FUNCTION_MATCH
BUDGET_LIMIT
INAPPLICABLE
```

For `horizon.excluded`, use `INAPPLICABLE` in this first seam.

The result may preserve:

```text
Horizon origin
applicability state
missing-context state
relation provenance
budget diagnostics
size diagnostics
```

for observability and future UI use.

These system decisions must not be copied wholesale into the model-facing pack.

---

## 10. Model-facing MethodologicalContextPack

The model-facing pack contains selected methodological knowledge only.

Required envelope:

```text
schema_version = 1
task_id
requested_reasoning_functions
selected knowledge items
aggregate missing_context_keys
```

Each selected item includes:

```text
compact exact ContextKnowledgeAsset projection
Horizon origin
applicability_state
missing_context_keys
relation_source_key / relation_type / relation_revision_id when relation-added
selection_reason
```

The pack must not include:

```text
omission decisions
names of omitted Horizon candidates
omitted knowledge content
global catalog inventory
retrieval ranking traces
```

Accepted boundary:

```text
SYSTEM
    may retain a ten-asset Horizon and eight omission decisions

MODEL-FACING PACK
    may receive only the two selected exact revisions
```

---

## 11. Missing-context preservation

A selected `MISSING_CONTEXT` candidate remains selected when it is relevant under the task profile.

Its unresolved context keys must remain visible on the item and in the pack's sorted unique aggregate.

Methodological concept support does not imply the project fact itself is known.

Example validated by RH-C03:

```text
prediction-moment concept selected as REQUIRED_CONCEPT_SUPPORT
    while
project prediction-moment context remains unresolved
```

This preserves the executable semantic invariant inherited from Specification 012:

```text
unknown != false
```

---

## 12. Canonical serialization

The pack has deterministic canonical serialization:

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

Provider-specific tokenizer dependencies remain outside this seam.

Exact model token counts belong in a later experiment that fixes one concrete model/runtime configuration.

---

## 13. Frozen RH-C evidence that earned promotion

The v0.1 contract used the unchanged accepted knowledge fixture and a deliberately wide ten-asset Horizon.

All four cases used:

```text
max_assets = 3
```

Observed selected sets:

```text
RH-C01 MODEL_OPTION
    random-forest
    gradient-boosted-trees

RH-C02 EVIDENCE_OPTION
    histogram
    ecdf

RH-C03 VALIDITY_CONSTRAINT
    prediction-time-feature-eligibility
    temporal-validation
    prediction-moment as REQUIRED_CONCEPT_SUPPORT

RH-C04 DECISION_FRAMEWORK
    class-imbalance
    missing-data
```

Observed context ratios:

```text
RH-C01  0.20020477
RH-C02  0.16462054
RH-C03  0.34635417
RH-C04  0.28222057
```

Equivalent canonical-context reductions were approximately:

```text
79.98%
83.54%
65.36%
71.78%
```

Across every frozen case:

```text
required stable-key coverage          1.00
required exact-revision coverage      1.00
irrelevant selected assets            0
selected assets                       <= 3
omitted candidates without reason     0
selective/full-Horizon byte ratio     <= 0.65
```

The frozen target sets, threshold, task profiles, budget, relation-support rule, and accepted knowledge fixture were not changed after observing the implementation result.

Primary result:

```text
experiments/retrieval/V1_SELECTIVE_CONTEXT_RESULT.md
```

---

## 14. Accepted non-quality invariants

### RC-01 Exact revision identity
Every selected item uses the exact revision carried by its Horizon candidate and that revision is still accepted-current when context is read.

### RC-02 Stale context fail-closed
A stale or unavailable exact revision raises an explicit error. The assembler never silently substitutes another revision.

### RC-03 No global scan in production selection
Production selection obtains full context only through exact selected-candidate reads. It has no application-level list-all/global-export dependency.

### RC-04 Omitted knowledge absent from model pack
System omission decisions do not leak omitted candidates into serialized model-facing context.

### RC-05 Missing context preserved
Selected unresolved candidates retain missing keys and the pack exposes the sorted unique aggregate.

### RC-06 Inapplicable excluded
No `INAPPLICABLE` Horizon candidate enters this first model-facing pack.

### RC-07 Required-concept closure bounded
Only already-present `REQUIRES_CONCEPT` relation candidates whose recorded source is a primary match are auto-included.

### RC-08 Deterministic serialization
Repeated assembly from unchanged inputs yields identical canonical bytes and SHA-256 digest.

### RC-09 Retrieval metadata omitted
The pack contains no lexical terms, aliases, semantic retrieval cues, retrieval scores, or provider ranking metadata.

### RC-10 Authoritative-state isolation
Selection/context assembly performs no authoritative knowledge/project writes.

### RC-11 Storage isolation
Application modules remain free of SQLAlchemy/persistence-schema imports.

### RC-12 Regression compatibility
The locked V1 Python suite remains green.

### RC-13 Cross-platform
The validated RH-C gate passes on Ubuntu and Windows under the frozen workflow environment.

### RC-14 Budget overflow explicit
A relevant candidate beyond `max_assets` is reported as `BUDGET_LIMIT`, not silently dropped.

### RC-15 Post-budget materialization
Full context content is fetched only after the hard selection budget has been applied.

---

## 15. Explicit non-goals and non-selections

This accepted bounded seam does not select or solve:

```text
LLM relevance judgment
semantic embedding relevance reranking
learned ranking
opaque relevance scores
natural-language task -> reasoning-function inference
final recommendation state
final REQUIRED/BLOCKING state
final project-wide Horizon budget
final per-call context budget
provider-specific token budget
production semantic retriever integration
FastEmbed/BGE production dependency
permanent RRF production implementation
ANN/vector database
recursive relation expansion
open-world concern discovery
final LLM provider/model
multi-agent architecture
runtime/model reasoning quality
```

The frozen `max_assets = 3` and ten-asset stress Horizon remain benchmark parameters only.

---

## 16. Promotion interpretation

Specification 013 v1.0 promotes the **seam**, not every benchmark constant.

Accepted:

```text
explicit task-profile request
exact Horizon identity handling
deterministic primary reasoning-function selection
bounded REQUIRES_CONCEPT support
hard budget with explicit overflow reason
exact accepted-current context reads
compact reasoning projection
system/model-facing separation
missing-context preservation
canonical deterministic serialization
```

Still hypothesis/open:

```text
how task profiles are derived in production
whether semantic/LLM relevance is later necessary
how relevance becomes recommendation
how REQUIRED/BLOCKING is decided
what final budgets should be
whether selective context improves real reasoning
```

This status is intentionally narrower than a claim that general methodological relevance is solved.

---

## 17. Next evidence boundary

The next justified experiment is a real reasoning vertical slice, preregistered before model calls:

```text
same frozen project/task evidence
    -> selective MethodologicalContextPack
    -> ADS-owned ReasoningRuntime
    -> one concrete model configuration

versus

same frozen project/task evidence
    -> strong full-Horizon/simple context control
    -> same ADS-owned ReasoningRuntime
    -> same concrete model configuration
```

Measure at least:

```text
reasoning-output quality against frozen obligations
critical methodological omissions
exact knowledge revisions supplied
exact provider/model tokens
latency and cost where observable
whether selective omission causes real quality loss
whether full-Horizon context creates distraction or unnecessary burden
```

Do not tune retrieval or add an LLM relevance judge merely because those mechanisms are available. Reopen them when the reasoning vertical slice demonstrates a concrete deficiency.

---

## 18. Primary sources

```text
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md

docs/research/020_first_horizon_relevance_and_selective_context_gate_design.md

docs/specifications/009_v1_retrieval_and_methodological_horizon_benchmark.md
docs/specifications/012_v1_first_methodological_horizon_builder.md

docs/checkpoints/141_first_methodological_horizon_cross_platform_gate_passed.md
docs/checkpoints/142_relevance_and_selective_context_contract_frozen.md
docs/checkpoints/143_selective_methodological_context_gate_passed_and_promotion_authorized.md

experiments/retrieval/V1_SELECTIVE_CONTEXT_RESULT.md
```
