# Current State

**Checkpoint:** 143  
**Date:** 2026-08-22  
**Active development branch:** `v1-relevance-selective-context`  
**Active promotion PR:** #11 into `v1-frontend-spike`  
**Promoted V1 integration branch before PR #11:** `v1-frontend-spike` at PR #10 merge commit `9319ed9b0a401efa1be85c27a9ce4424a8ce5e1e`  
**Development stage:** Prototype V0 complete; bounded V1 implementation advancing across governed methodological knowledge, retrieval and MethodologicalHorizon construction, selective model-facing methodological context, selected reasoning-runtime infrastructure, and the promoted Project Cockpit interaction architecture  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate project priority:** finish the reconciled PR #11 promotion, validate its exact final head, merge that head into `v1-frontend-spike`, then preregister the first real reasoning vertical slice comparing selective methodological context with a strong full-Horizon/simple control under one concrete model configuration.

## Active ChatGPT development context

```text
Design session: 04
ChatGPT project: Autonomous Data Science System
Session title: 04 - Selective Context Promotion & Reasoning Vertical Slice
```

Repository artifacts remain authoritative across chats. The default `main` branch intentionally trails current V1 work until explicit later promotion.

---

## 1. Durable system constraint from Prototype V0

ADS is intended to be a professional interactive data-science operating environment in which the system carries methodological memory, project memory, process navigation, evidence discipline, provenance, execution coordination, and reporting burden while the LLM remains one flexible reasoning component inside the wider system.

Prototype V0 strongly falsified the tested P0 pattern of repeatedly carrying large structured state and frontier machinery through reasoning calls.

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
    -> selective task-specific reasoning context
    -> runtime reasoning
```

Foundation 020 governs reusable methodological knowledge around `KnowledgeAsset`, `KnowledgeComponent`, `NarrativeFacet`, `KnowledgeRelation`, conditional `KnowledgeRule`, `KnowledgeCollection`, exact revisions, and `ExecutionCapability`.

---

## 3. Accepted V1 persistence, interchange, and runtime boundaries

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

The post-promotion normal-window/pinch repair at Checkpoint 130 remains accepted as good enough to continue. The tiny occasional pinch hitch remains deferred non-blocking polish.

---

## 5. Retrieval and MethodologicalHorizon evidence is closed for the first bounded slice

Research 016 and Specification 009 decompose the retrieval/Horizon program as:

```text
RH-L    lexical-addressable retrieval
RH-S    semantic/paraphrase retrieval
RH-R    relational horizon expansion
RH-A    applicability / required-context behavior
RH-C    selective context construction
```

### 5.1 Production lexical baseline

Checkpoint 135 validates:

```text
RH-L Recall@3            1.00
RH-L MRR                 1.00
RH-S Recall@3            0.75
```

The lexical semantic miss is `class-imbalance`.

### 5.2 Exact dense semantic comparator

Checkpoint 137 preserves FastEmbed 0.8.0 + `BAAI/bge-small-en-v1.5` as an experiment-only exact dense comparator.

It recovers `class-imbalance` but loses `ecdf` from the semantic top three. Dense-only therefore did not earn replacement of lexical retrieval.

### 5.3 Complementary rank fusion

Checkpoint 139 / workflow `32561118325` validates equal-weight RRF over the unchanged lexical and dense top-three rankings:

```text
Ubuntu PASS
Windows PASS
RH-S Recall@3            1.00
RH-S MRR                 0.875
RH-S critical omissions  0 / 4
RH-L Recall@3            1.00
RH-L MRR                 1.00
```

This is evidence for hybrid lexical + exact semantic complementarity on the frozen benchmark. It does not permanently select FastEmbed, BGE, RRF `k=60`, vector persistence, ANN, or a vector database.

### 5.4 First explained MethodologicalHorizon

Specification 012 v1.0 / Checkpoint 141 validate:

```text
storage-neutral direct candidate identities
    -> accepted-current KnowledgeNavigationRepository reads
    -> outbound one-hop accepted relation expansion
    -> deterministic TRUE / FALSE / UNKNOWN applicability evaluation
    -> POSSIBLY_APPLICABLE / INAPPLICABLE / MISSING_CONTEXT
    -> explained included/excluded MethodologicalHorizon
```

Cross-platform gate:

```text
workflow 32561727632
Ubuntu PASS
Windows PASS
RH-R relation cases       4 / 4 PASS
RH-A applicability cases  5 / 5 PASS
authoritative knowledge   unchanged
```

The executable invariant remains:

```text
unknown != false
```

PR #10 containing this slice was merged into `v1-frontend-spike` at:

```text
9319ed9b0a401efa1be85c27a9ce4424a8ce5e1e
```

---

## 6. Selective methodological context is now validated and promoted for a bounded seam

Research 020 and frozen Specification 013 v0.1 tested the first deterministic RH-C policy over a deliberately wide ten-asset Horizon:

```text
explicit requested reasoning functions
    -> PRIMARY_FUNCTION_MATCH
    -> bounded REQUIRES_CONCEPT support
    -> hard max_assets budget
    -> exact accepted-current compact context reads
    -> ContextSelectionResult
    -> MethodologicalContextPack
```

The architecture separates:

```text
SYSTEM-FACING
    Horizon + selected/omitted decisions + omission reasons

MODEL-FACING
    selected methodological knowledge only
```

The frozen gate passed on Ubuntu and Windows without changing targets or thresholds.

Observed cases:

```text
RH-C01 MODEL_OPTION
    selected 2 / 10
    selective/full bytes 0.20020477
    reduction 79.98%

RH-C02 EVIDENCE_OPTION
    selected 2 / 10
    selective/full bytes 0.16462054
    reduction 83.54%

RH-C03 VALIDITY_CONSTRAINT
    selected 3 / 10
    selective/full bytes 0.34635417
    reduction 65.36%

RH-C04 DECISION_FRAMEWORK
    selected 2 / 10
    selective/full bytes 0.28222057
    reduction 71.78%
```

Across all four cases:

```text
required stable-key coverage        1.00
required exact-revision coverage    1.00
irrelevant selected assets          0
selected assets                     <= 3
unexplained omissions               0
```

The full locked V1 suite was:

```text
Ubuntu   42 passed, 2 skipped
Windows  42 passed, 2 skipped
```

Additional demonstrated invariants include stale-revision fail-closed behavior, explicit `BUDGET_LIMIT`, post-budget full-content materialization, deterministic canonical serialization, identical cross-platform digests, preservation of `MISSING_CONTEXT`, omission of retrieval metadata from model context, and authoritative-state isolation.

Checkpoint 143 promotes Specification 013 to accepted bounded v1.0.

Primary evidence:

```text
docs/research/020_first_horizon_relevance_and_selective_context_gate_design.md
docs/specifications/013_v1_horizon_relevance_and_selective_context.md
docs/checkpoints/142_relevance_and_selective_context_contract_frozen.md
docs/checkpoints/143_selective_methodological_context_gate_passed_and_promotion_authorized.md
experiments/retrieval/V1_SELECTIVE_CONTEXT_RESULT.md
```

---

## 7. What Specification 013 v1.0 does and does not establish

Accepted bounded seam:

```text
explicit MethodologicalContextRequest
reasoning-function primary selection
bounded REQUIRES_CONCEPT support
hard asset budget with explicit overflow reason
exact accepted-current selected-context reads
compact reasoning projection
system/model-facing separation
missing-context preservation
canonical deterministic pack serialization
```

Not established:

```text
reasoning_functions solve general semantic relevance
natural-language task -> reasoning-function inference
max_assets = 3 is a universal budget
all Horizons compress similarly
UTF-8 bytes equal provider tokens
selective context improves downstream LLM reasoning
recommendation policy
REQUIRED/BLOCKING policy
open-world concern discovery
final LLM provider/model
multi-agent architecture
```

Do not tune retrieval or add an LLM relevance judge before the next reasoning experiment demonstrates a concrete downstream deficiency.

---

## 8. Current major non-selections

Still deliberately unselected:

```text
final LLM provider/model
number of agents beyond single-principal-reasoner first
multi-agent collaboration architecture
production durable runtime-state persistence schema
production MCP server/tool catalog
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
natural-language task -> reasoning-function mapper
final semantic relevance mechanism
final MethodologicalHorizon budget
final selective context budget
recommendation / REQUIRED-BLOCKING policy
complete Foundation 018 production schema
artifact-storage backend
job queue/cloud deployment
```

---

## 9. Exact next execution order

### A. CLOSE PR #11 PROMOTION

```text
1. complete Checkpoint 143 / Specification 013 v1.0 promotion
2. reconcile current routing/status documents
3. update PR #11 with the measured result
4. verify the exact final PR head workflows are green
5. merge exactly that tested head into v1-frontend-spike
```

### B. FREEZE THE FIRST REAL REASONING VERTICAL SLICE

On a new branch from the promoted PR #11 merge boundary, preregister before model calls:

```text
same frozen project/task evidence
    -> selective MethodologicalContextPack
    -> ADS-owned ReasoningRuntime
    -> one concrete model configuration

versus

same frozen project/task evidence
    -> strong full-Horizon/simple context control
    -> same ReasoningRuntime
    -> same concrete model configuration
```

Measure at least:

```text
reasoning-output quality against frozen obligations
critical methodological omissions
exact knowledge revisions supplied
exact provider/model input/output tokens
latency and cost where observable
whether selective omission causes real quality loss
whether full-Horizon context creates distraction or unnecessary cost
```

### C. ONLY ESCALATE RELEVANCE/RETRIEVAL COMPLEXITY FROM EVIDENCE

If the reasoning vertical slice exposes omissions caused by the deterministic selector or task profile, classify the failure first. Only then consider semantic/LLM relevance, richer task-profile derivation, reranking, or other machinery.

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

docs/specifications/005_v1_agent_runtime_and_interoperability_bakeoff.md
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
docs/specifications/009_v1_retrieval_and_methodological_horizon_benchmark.md
docs/specifications/012_v1_first_methodological_horizon_builder.md
docs/specifications/013_v1_horizon_relevance_and_selective_context.md

docs/research/016_production_retrieval_and_methodological_horizon_benchmark_design.md
docs/research/017_exact_semantic_retrieval_comparator_selection.md
docs/research/018_dense_semantic_failure_complementarity_and_rrf_fusion_rationale.md
docs/research/019_first_methodological_horizon_application_seam.md
docs/research/020_first_horizon_relevance_and_selective_context_gate_design.md

experiments/retrieval/V1_LEXICAL_RETRIEVAL_RESULT.md
experiments/retrieval/V1_RRF_HYBRID_RETRIEVAL_RESULT.md
experiments/retrieval/V1_METHODOLOGICAL_HORIZON_RESULT.md
experiments/retrieval/V1_SELECTIVE_CONTEXT_RESULT.md

docs/checkpoints/135_first_production_lexical_retrieval_baseline_cross_platform_passed.md
docs/checkpoints/137_dense_semantic_retrieval_comparator_cross_platform_result_preserved.md
docs/checkpoints/139_rrf_hybrid_retrieval_cross_platform_gate_passed.md
docs/checkpoints/141_first_methodological_horizon_cross_platform_gate_passed.md
docs/checkpoints/142_relevance_and_selective_context_contract_frozen.md
docs/checkpoints/143_selective_methodological_context_gate_passed_and_promotion_authorized.md
```
