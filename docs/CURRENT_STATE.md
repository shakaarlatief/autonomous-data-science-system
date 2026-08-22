# Current State

**Checkpoint:** 135  
**Date:** 2026-08-22  
**Active development branch:** `v1-methodological-horizon`  
**Promoted V1 integration branch:** `v1-frontend-spike` at runtime-selection merge boundary `de78501c3990bce9657fe02a117c9186c76a7955` plus later explicitly merged slices  
**Development stage:** Prototype V0 complete; bounded V1 implementation advancing across methodological knowledge, governed persistence/interchange, production retrieval/MethodologicalHorizon construction, selected reasoning-runtime infrastructure, and the promoted Project Cockpit interaction architecture  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate project priority:** Merge the independently validated production lexical retrieval slice, then evaluate a bounded exact/in-process semantic retrieval comparator against the unchanged Specification 009 RH-S cases before beginning RH-R/RH-A MethodologicalHorizon construction.

## Active ChatGPT development context

```text
Design session: 03
ChatGPT project: Autonomous Data Science System
Session title: 03 - Project Cockpit & V1 Integration
```

Repository artifacts remain authoritative across chats. The default `main` branch intentionally trails current V1 work until explicit later promotion/merge.

---

## 1. System purpose and V0 constraint

ADS is intended to become a professional interactive data-science operating environment in which the system carries much of the methodological memory, project memory, process navigation, evidence discipline, provenance, execution coordination, and reporting burden that otherwise has to be repeatedly supplied through prompts.

The LLM is one flexible reasoning component inside the wider system, not the system itself.

Prototype V0 strongly falsified the then-current P0 implementation strategy. The strongest scaling lesson remains:

```text
what the SYSTEM should remember
    !=
what the LLM should receive on every reasoning call
```

Do not restore P0's large always-on state/context, path-sensitive activation, generic recursive reopening, or full frontier representation unchanged.

---

## 2. Current methodological/project architecture

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

Foundation 019 governs methodological relevance through:

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
    -> high-recall project-specific retrieval/filtering
    -> bounded MethodologicalHorizon
    -> explicit applicability/context checks
    -> flexible relevance/prioritization reasoning
    -> selective task-specific LLM context
```

Foundation 020 governs reusable methodological knowledge around `KnowledgeAsset`, `KnowledgeComponent`, `NarrativeFacet`, `KnowledgeRelation`, conditional `KnowledgeRule`, `KnowledgeCollection`, exact revisions, and `ExecutionCapability`.

---

## 3. Accepted persistence/interchange and runtime architecture

Accepted V1 decisions include:

```text
D-028 + Specification 001
    SQLite-centered local-first operational architecture
    rebuildable FTS5 lexical retrieval
    rebuildable semantic retrieval/cache seam
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

The completed runtime bakeoff was merged through PR #8 into `v1-frontend-spike` at:

```text
de78501c3990bce9657fe02a117c9186c76a7955
```

Direct model calls remain the fallback/reference path. LangGraph remains a future stronger-durability escalation path. No final LLM provider/model or multi-agent architecture is selected.

---

## 4. Project Cockpit interaction architecture is promoted

Specification 008 is the current V1 Project Cockpit interaction contract.

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

Checkpoint 130's post-promotion normal-window/pinch repair was subsequently accepted as good enough to continue. The tiny occasional pinch hitch remains deferred non-blocking polish.

---

## 5. Production lexical retrieval is now validated

Research 016 and frozen Specification 009 v0.1 define the Q-044/Q-045 retrieval/Horizon evaluation decomposition:

```text
RH-L    lexical-addressable retrieval
RH-S    semantic/paraphrase retrieval diagnostics
RH-R    relational horizon expansion
RH-A    applicability / required-context behavior
RH-C    selective context construction
```

Checkpoint 135 validates the first production lexical implementation:

```text
KnowledgeRetrievalPort
KnowledgeRetrievalHit
    -> SqliteFtsKnowledgeRetrieval
    -> rebuildable accepted-current FTS5 projection
```

Final observable gate:

```text
V1 methodological horizon
run 32559177057
source head c462365bf64ebe9d676a0d9ce6402bba61e67279

Ubuntu     PASS
Windows    PASS
```

Observed quality:

```text
indexed accepted-current assets    10
RH-L Recall@3                      1.00
RH-L MRR                           1.00
RH-L critical omissions            0 / 10
RH-L required target rank 1       10 / 10
RH-S diagnostic Recall@3           0.75
```

The one frozen semantic miss is:

```text
RH-S01
positive cases are scarce and overall correctness hides failures on them
    -> target class-imbalance
    -> lexical result: no hits
```

The other three RH-S targets were recovered at rank 1 by the lexical baseline.

Detailed result:

```text
experiments/retrieval/V1_LEXICAL_RETRIEVAL_RESULT.md
```

The first workflow attempt also produced a useful non-product diagnostic: the frozen retrieval gate passed, while the broader regression command used bare `pytest` and lost repository-root import visibility for `experiments.*`. Changing only the command to `python -m pytest` restored the already-validated regression behavior. No benchmark or retrieval behavior changed.

---

## 6. What remains open in Q-044 / Q-045

The lexical slice is no longer hypothetical, but Q-044 and Q-045 remain open.

Still required:

```text
semantic retrieval comparator against unchanged RH-S cases
incremental useful-recall versus candidate-growth analysis
fusion only if lexical and semantic channels are complementary
reranking only if candidate coverage is good but ordering is materially weak
RH-R relation expansion
RH-A applicability / missing-context handling
first bounded real MethodologicalHorizon
RH-C selective context assembly and context-cost evaluation
recommendation-quality evaluation downstream of coverage/retrieval
```

Do not select an embedding model, vector database, ANN service, fusion algorithm, or reranker from intuition.

The next semantic comparator should prefer an exact/in-process design at current corpus scale so the project does not pre-pay ANN/vector infrastructure before scale evidence requires it.

---

## 7. Current major non-selections

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
embedding model/provider
vector database / ANN infrastructure
lexical/semantic fusion
reranker
final MethodologicalHorizon budget/ranking policy
final applicability evaluator
final selective context budget
complete Foundation 018 production schema
artifact-storage backend
job queue/cloud deployment
```

---

## 8. Exact next execution order

### A. MERGE THE VALIDATED LEXICAL SLICE

```text
1. preserve Checkpoint 135 / lexical result / current routing
2. verify checkpoint metadata on the reconciled head
3. update PR #9 with final cross-platform evidence
4. merge PR #9 into v1-frontend-spike
```

### B. BOUNDED SEMANTIC RETRIEVAL COMPARATOR

```text
1. create a new branch from the merged lexical boundary
2. research exact/in-process semantic comparator options and dependency/testing trade-offs
3. keep RH-S queries and lexical control unchanged
4. implement the smallest meaningful semantic candidate
5. measure RH-S incremental recall and irrelevant candidate growth
6. decide whether a semantic channel earns retention
7. introduce fusion only if evidence demonstrates complementarity
```

### C. FIRST REAL METHODOLOGICALHORIZON

```text
1. execute frozen RH-R relational expansion cases
2. execute frozen RH-A applicability/context cases
3. preserve direct/relation-added/inapplicable/missing-context explanations
4. define and evaluate a bounded horizon representation/budget
5. advance to RH-C selective LLM context quality and cost
```

### D. SELECTED RUNTIME PRODUCTION INTEGRATION

Integrate D-032 behind the ADS-owned runtime port when the first real reasoning vertical slice requires it. Do not promote the experiment adapter wholesale before the application contract is clear.

---

## 9. Minimum reading for continuation

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

docs/research/015_langgraph_complete_candidate_three_way_runtime_comparison_and_stop_rule.md
docs/research/016_production_retrieval_and_methodological_horizon_benchmark_design.md

experiments/retrieval/V1_LEXICAL_RETRIEVAL_RESULT.md

docs/checkpoints/127_governed_knowledge_roundtrip_closed_across_sqlite_and_postgresql.md
docs/checkpoints/133_v1_reasoning_runtime_selected_and_bakeoff_closed.md
docs/checkpoints/134_retrieval_and_methodological_horizon_benchmark_contract_frozen.md
docs/checkpoints/135_first_production_lexical_retrieval_baseline_cross_platform_passed.md
```