# Current State

**Checkpoint:** 141  
**Date:** 2026-08-22  
**Active development branch:** `v1-semantic-retrieval`  
**Active promotion PR:** #10 into `v1-frontend-spike`  
**Promoted V1 integration branch before PR #10:** `v1-frontend-spike` at the independently merged lexical boundary `73a78d00b8edf440e7fef8c5334b3edb52246d50`  
**Development stage:** Prototype V0 complete; bounded V1 implementation advancing across methodological knowledge, governed persistence/interchange, retrieval and MethodologicalHorizon construction, selected reasoning-runtime infrastructure, and the promoted Project Cockpit interaction architecture  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate project priority:** finish final reconciliation and green validation of PR #10, merge the validated retrieval/Horizon slice, then freeze and execute the first relevance/selective-context gate over the explained MethodologicalHorizon.

## Active ChatGPT development context

```text
Design session: 03
ChatGPT project: Autonomous Data Science System
Session title: 03 - Project Cockpit & V1 Integration
```

Repository artifacts remain authoritative across chats. The default `main` branch intentionally trails current V1 work until explicit later promotion.

---

## 1. Durable system constraint from V0

ADS is intended to be a professional interactive data-science operating environment in which the system carries methodological memory, project memory, process navigation, evidence discipline, provenance, execution coordination, and reporting burden while the LLM remains one flexible reasoning component inside the wider system.

Prototype V0 strongly falsified the P0 strategy of repeatedly carrying large structured state and frontier machinery through reasoning calls.

The strongest scaling lesson remains:

```text
what the SYSTEM should remember
    !=
what the LLM should receive on every reasoning call
```

Do not restore P0's large always-on context/state, path-sensitive activation, generic recursive reopening, or full frontier representation unchanged.

---

## 2. Governing methodological architecture

Foundation 018 separates:

```text
OBJECTS
RELATIONS
EVENTS
VIEWS
```

Important distinctions include:

```text
Investigation != Run
Evidence != Finding
Finding != Claim
Claim != Decision
current state != event history
persisted object != derived recommendation
workspace section != fundamental object
```

Foundation 019 governs methodological navigation through:

```text
KNOWN
    -> APPLICABLE
    -> RELEVANT
    -> RECOMMENDED
    -> REQUIRED / BLOCKING
```

The current scaling path is:

```text
large global methodological knowledge universe
    -> high-recall retrieval
    -> bounded explained MethodologicalHorizon
    -> applicability / missing-context handling
    -> relevance / prioritization
    -> selective task-specific LLM context
```

Foundation 020 governs reusable methodological knowledge around `KnowledgeAsset`, `KnowledgeComponent`, `NarrativeFacet`, `KnowledgeRelation`, conditional `KnowledgeRule`, `KnowledgeCollection`, exact revisions, and `ExecutionCapability`.

---

## 3. Accepted persistence, interchange, and runtime boundaries

Accepted V1 decisions include:

```text
D-028 + Specification 001
    SQLite-centered local-first operational architecture
    rebuildable lexical/semantic retrieval projections
    application-level rule evaluation
    selective context assembly

D-029 + Specification 002 v1.1
    SQLAlchemy Core 2.0 + Alembic 1.x

D-030 + Specification 003
    pyproject.toml + uv + committed uv.lock + uv_build
    Python >=3.12

D-031 + Specification 004
    JSON + JSON Schema Draft 2020-12
    semantic validation
    deterministic reusable-knowledge normalization/serialization

D-032 + completed Specification 005
    OpenAI Agents SDK behind an ADS-owned ReasoningRuntime port
    validated starting package openai-agents==0.19.4
```

Checkpoint 127 closes the governed reusable-knowledge persistence/interchange seam across SQLite/Linux, SQLite/Windows, and PostgreSQL 18.

Checkpoint 133 closes the initial runtime bakeoff. Direct model calls remain the fallback/reference path. LangGraph remains a future stronger-durability escalation path. No final LLM provider/model or multi-agent architecture is selected.

---

## 4. Project Cockpit interaction architecture

Specification 008 is the promoted V1 Project Cockpit interaction contract.

Promoted principles include:

```text
Project Cockpit as primary immersive active-work model
meaningful work units rather than every persisted object
spatial focus into real reusable specialist workspaces
reachability != simultaneous mounting
FiniteNavigableGridWorld != SemanticProjectPlane
2D project navigation and recovery
bounded geometric zoom and native laptop pinch capability
viewport-aware semantic stage orientation
scalable Jump/search project location
compact/fold-away immersive chrome
collision-safe floating surfaces
true fullscreen with graceful fallback
URL-addressable focus/deep-work state
keyboard accessibility and reduced-motion support
world-owned restrained ambient depth
```

The later normal-window/pinch repair is accepted as good enough to continue. The tiny occasional pinch hitch remains deferred non-blocking polish.

---

## 5. Retrieval evidence is now three-stage rather than hypothetical

Research 016 and Specification 009 define:

```text
RH-L    lexical-addressable retrieval
RH-S    semantic/paraphrase retrieval
RH-R    relational Horizon expansion
RH-A    applicability / required-context behavior
RH-C    selective context construction
```

### 5.1 Production lexical baseline

Checkpoint 135 validates the first production lexical retriever:

```text
KnowledgeRetrievalPort
KnowledgeRetrievalHit
    -> SqliteFtsKnowledgeRetrieval
    -> rebuildable accepted-current FTS5 projection
```

Observed quality:

```text
RH-L Recall@3            1.00
RH-L MRR                 1.00
RH-S Recall@3            0.75
```

The lexical miss is RH-S01 `class-imbalance`.

### 5.2 Exact dense semantic comparator

Specification 010 / Checkpoint 137 preserve the experiment-only FastEmbed 0.8.0 + `BAAI/bge-small-en-v1.5` comparator.

Dense retrieval also achieved:

```text
RH-L Recall@3            1.00
RH-L MRR                 1.00
RH-S Recall@3            0.75
RH-S MRR                 0.75
```

It recovered `class-imbalance` at rank 1 but lost `ecdf` from the semantic top 3. Dense-only therefore did not earn replacement of lexical retrieval.

### 5.3 Bounded RRF fusion comparator

Specification 011 / Checkpoint 139 validate the measured complementarity of the two channels using the frozen rank-only RRF comparator:

```text
workflow run 32561118325
Ubuntu PASS
Windows PASS

RH-S Recall@3            1.00
RH-S MRR                 0.875
RH-S omissions           0 / 4
RH-L Recall@3            1.00
RH-L MRR                 1.00
```

`class-imbalance` survives as dense-only signal and `ecdf` survives as lexical-only signal.

This promotes hybrid lexical + exact semantic retrieval as the leading V1 retrieval hypothesis for this benchmark. It does **not** promote FastEmbed, BGE, RRF `k=60`, vector persistence, ANN, or a vector database as permanent production architecture.

Primary result:

```text
experiments/retrieval/V1_RRF_HYBRID_RETRIEVAL_RESULT.md
```

---

## 6. First real MethodologicalHorizon is validated

Specification 012 v1.0 and Checkpoint 141 now validate the first production-facing Horizon seam.

Accepted application boundary:

```text
storage-neutral direct candidate identities
    -> accepted-current KnowledgeNavigationRepository reads
    -> outbound one-hop accepted relation expansion
    -> deterministic TRUE / FALSE / UNKNOWN condition evaluation
    -> POSSIBLY_APPLICABLE / INAPPLICABLE / MISSING_CONTEXT
    -> explained included/excluded MethodologicalHorizon
```

The application layer is independent of FTS5, BM25, FastEmbed, BGE, cosine similarity, RRF, and vector-store APIs.

Cross-platform gate:

```text
V1 first MethodologicalHorizon builder
run 32561727632
Ubuntu PASS
Windows PASS

RH-R relation cases       4 / 4 PASS
RH-A applicability cases  5 / 5 PASS
authoritative knowledge   unchanged
full V1 suite              39 passed, 2 skipped on each OS
```

Validated relation expansion:

```text
random-forest
    -> bagging
    -> gradient-boosted-trees

temporal-validation
    -> prediction-moment

prediction-time-feature-eligibility
    -> prediction-moment

histogram
    -> ecdf
```

Validated applicability distinction:

```text
known negative supervision context
    random-forest -> INAPPLICABLE

missing class prevalence
    class-imbalance -> MISSING_CONTEXT

missing prediction moment
    temporal-validation -> MISSING_CONTEXT
    prediction-time-feature-eligibility -> MISSING_CONTEXT
```

The semantic invariant is executable:

```text
unknown != false
```

Primary result:

```text
experiments/retrieval/V1_METHODOLOGICAL_HORIZON_RESULT.md
```

---

## 7. What remains open in Q-044 / Q-045

The following are no longer open as first-slice questions:

```text
production lexical accepted-current retrieval
whether dense semantic signal is complementary on the frozen corpus
whether simple rank fusion can preserve both measured semantic signals
one-hop accepted-current relation expansion
first three-valued applicability / missing-context behavior
first explained MethodologicalHorizon representation
```

Still open and now next:

```text
relevance / prioritization over an explained Horizon
bounded Horizon budget policy
RH-C selective context construction
exact revision coverage after context selection
irrelevant-context burden
serialized size / token burden
omission quality
recommendation-quality evaluation downstream of relevance
production semantic-provider / fusion integration only when a vertical slice requires it
```

Do not optimize the RRF comparator or add vector infrastructure before those downstream questions demonstrate a need.

---

## 8. Current major non-selections

Still deliberately unselected:

```text
final LLM provider/model
number of agents beyond single-principal-reasoner first
multi-agent collaboration architecture
production durable runtime-state persistence schema
MCP production server/tool catalog
A2A
AG-UI final role
frontend final stack promotion
chart library
Cockpit graph/canvas library
Cockpit gesture library
Cockpit auto-layout algorithm
Cockpit minimap implementation
Cockpit semantic-zoom algorithm
final native-pinch constants/range
production project-search backend
Cockpit final stage taxonomy/layout
Cockpit final public URL contract
Cockpit final visual identity
canonical Cockpit screenshot baseline
backend HTTP/API framework
production embedding model/provider
vector database / ANN infrastructure
permanent production fusion implementation
reranker
final MethodologicalHorizon relevance/budget policy
final broad predicate/rule language
final selective context budget
complete Foundation 018 production schema
artifact-storage backend
job queue/cloud deployment
```

---

## 9. Exact next execution order

### A. CLOSE PR #10 PROMOTION

```text
1. preserve Checkpoint 141 and Specification 012 execution result
2. reconcile current routing/status documents
3. update PR #10 with dense, fusion, and Horizon evidence
4. verify final PR-head workflows are green
5. merge exactly that tested head into v1-frontend-spike
```

### B. FREEZE RELEVANCE / SELECTIVE-CONTEXT GATE

On a new branch from the promoted boundary:

```text
1. define the smallest real Horizon relevance/prioritization input/output contract
2. freeze RH-C scenarios before implementation
3. measure exact required revision coverage
4. measure irrelevant candidate/context inclusion
5. measure serialized size / token burden
6. verify the global catalog is not serialized by default
7. preserve explicit omissions and reasons
```

The first gate should prefer deterministic or simple bounded policy where sufficient. Do not introduce an LLM relevance judge merely because relevance is semantically rich.

### C. ONLY THEN CONNECT A REAL REASONING VERTICAL SLICE

If selective context passes:

```text
explained Horizon
    -> selective MethodologicalContextPack
    -> ADS-owned ReasoningRuntime port
    -> selected OpenAI Agents SDK adapter when needed
    -> trace exact knowledge revisions supplied to the reasoner
```

The retrieval/provider implementation should remain replaceable below that application boundary.

---

## 10. Minimum reading for continuation

```text
README.md
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/OPEN_QUESTIONS.md
docs/DECISIONS.md
docs/PRINCIPLES.md

docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md

docs/specifications/008_v1_project_cockpit_interaction_architecture.md
docs/specifications/009_v1_retrieval_and_methodological_horizon_benchmark.md
docs/specifications/010_v1_exact_semantic_retrieval_comparator.md
docs/specifications/011_v1_rrf_hybrid_retrieval_comparator.md
docs/specifications/012_v1_first_methodological_horizon_builder.md

docs/research/016_production_retrieval_and_methodological_horizon_benchmark_design.md
docs/research/017_exact_semantic_retrieval_comparator_selection.md
docs/research/018_dense_semantic_failure_complementarity_and_rrf_fusion_rationale.md
docs/research/019_first_methodological_horizon_application_seam.md

experiments/retrieval/V1_LEXICAL_RETRIEVAL_RESULT.md
experiments/retrieval/V1_RRF_HYBRID_RETRIEVAL_RESULT.md
experiments/retrieval/V1_METHODOLOGICAL_HORIZON_RESULT.md

docs/checkpoints/135_first_production_lexical_retrieval_baseline_cross_platform_passed.md
docs/checkpoints/137_dense_semantic_retrieval_comparator_cross_platform_result_preserved.md
docs/checkpoints/139_rrf_hybrid_retrieval_cross_platform_gate_passed.md
docs/checkpoints/140_first_methodological_horizon_builder_contract_frozen.md
docs/checkpoints/141_first_methodological_horizon_cross_platform_gate_passed.md
```
