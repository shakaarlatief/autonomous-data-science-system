# Current State

**Checkpoint:** 133  
**Date:** 2026-08-22  
**Active development branch:** `v1-runtime-bakeoff` pending final CI/reconciliation and merge into `v1-frontend-spike`  
**Development stage:** Prototype V0 complete; bounded V1 architecture and implementation advancing across methodological knowledge, governed persistence/interchange, retrieval/MethodologicalHorizon construction, selected reasoning-runtime infrastructure, and the promoted Project Cockpit interaction architecture  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate project priority:** Finish the runtime-selection reconciliation/merge, then begin the production retrieval / MethodologicalHorizon benchmark for Q-044 and Q-045. Do not expand the runtime bakeoff further without a new requirement capable of changing D-032.

## Active ChatGPT development context

```text
Design session: 03
ChatGPT project: Autonomous Data Science System
Session title: 03 - Project Cockpit & V1 Integration
```

Repository artifacts remain authoritative across chats.

The preserved promoted V1/frontend boundary remains on:

```text
v1-frontend-spike
```

The current runtime selection work is on:

```text
v1-runtime-bakeoff
```

The default `main` branch intentionally trails current V1 work until explicit later promotion/merge.

---

## 1. System purpose and V0 constraint

ADS is intended to become a professional interactive data-science operating environment in which the system carries much of the methodological memory, project memory, process navigation, evidence discipline, provenance, execution coordination, and reporting burden that otherwise has to be repeatedly supplied through prompts.

The LLM is one flexible reasoning component inside the wider system, not the system itself.

Prototype V0 strongly falsified the then-current P0 implementation strategy:

```text
B1 targeted mean: 1.73
P0 targeted mean: 1.78
incremental gain: +0.05

B1 completed within budget: 10/10
P0 completed within budget: 3/10

P0/B1 median token ratio: 2.160
```

The strongest scaling lesson remains:

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

The intended scaling path remains:

```text
large global methodological knowledge universe
    -> project-specific retrieval/filtering
    -> bounded MethodologicalHorizon
    -> explicit applicability/context checks
    -> flexible relevance/prioritization reasoning
    -> selective task-specific LLM context
```

Foundation 020 governs reusable methodological knowledge around `KnowledgeAsset`, `KnowledgeComponent`, `NarrativeFacet`, `KnowledgeRelation`, conditional `KnowledgeRule`, `KnowledgeCollection`, exact revisions, and `ExecutionCapability`.

---

## 3. Accepted V1 persistence and interchange

Accepted decisions/specifications:

```text
D-028 + Specification 001
    SQLite-centered local-first operational architecture
    FTS5 rebuildable lexical index
    rebuildable embeddings / initial exact semantic retrieval
    application-level rule evaluator
    selective context assembly

D-029 + Specification 002 v1.1
    SQLAlchemy Core 2.0
    Alembic 1.x
    PostgreSQL identifier portability

D-030 + Specification 003
    pyproject.toml
    uv + committed uv.lock
    uv_build
    Python >=3.12

D-031 + Specification 004
    JSON
    JSON Schema Draft 2020-12
    semantic validation
    deterministic normalization/serialization
```

Checkpoint 127 closes the governed reusable-knowledge persistence/interchange seam across:

```text
SQLite / Ubuntu     PASS
SQLite / Windows    PASS
PostgreSQL 18       PASS
```

Q-048 is closed for this seam.

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

Checkpoint 130 validated the bounded normal-window Jump/composer repair and faster anchored pinch implementation. The subsequent human retest accepted the result as good enough to continue.

The tiny occasional pinch hitch remains non-blocking deferred polish. Exact gesture constants and future Cockpit capabilities remain unfrozen.

---

## 5. Initial V1 reasoning runtime is selected

D-032 accepts:

```text
OpenAI Agents SDK
    behind an ADS-owned ReasoningRuntime port

validated starting package
    openai-agents==0.19.4
```

This is a version-governed V1 infrastructure decision, not permanent framework lock-in.

The durable boundary remains:

```text
ADS project/domain/methodological semantics
    -> owned by ADS

runtime Agent / Runner / RunState / MCP state
    -> replaceable execution infrastructure
```

Framework-specific types remain below the adapter boundary.

In particular:

```text
Agent != Project
RunState != project memory
runtime session/thread != project identity
framework tracing != authoritative provenance
framework tool definition != sole ADS ExecutionCapability definition
```

ADS continues to own:

```text
MethodologicalContextPack construction
exact context-pack digest and knowledge revision references
stale-context rejection
human-control/approval policy
application cancellation policy
authoritative side-effect idempotency and domain events
stable RuntimeTrace / provenance
runtime-state compatibility/version policy
```

MCP remains an external tool/resource interoperability boundary, not project memory or the internal ADS application bus.

The runtime is single-principal-reasoner first. No multi-agent architecture is selected.

---

## 6. Runtime bakeoff is closed for the current V1 selection question

Specification 005 v0.2 is the completed evaluation contract.

### Direct-call control

Checkpoint 129:

```text
workflow 32500521858
Ubuntu PASS
Windows PASS
```

The control remains a viable fallback/reference/escape path, but would require ADS to own more generic orchestration machinery.

### OpenAI Agents SDK 0.19.4

Checkpoint 131:

```text
workflow 32555526773
AR-01 through AR-12 PASS
Ubuntu PASS
Windows PASS
```

It removes meaningful generic plumbing around model/tool iteration, tool schema/dispatch, approval interruption, serializable/restorable RunState, structured output, stdio MCP, tool timeout, and lifecycle hooks while preserving ADS authority.

Research 011 records the released-package/docs mismatch around the absent documented `agents.testing.ScriptedModel`. Deterministic testing remained possible through an experiment-local fake against the released public `Model` interface.

### LangGraph 1.2.10

Checkpoint 132:

```text
workflow 32556382248
Ubuntu PASS, 9 comparator tests
Windows PASS, 9 comparator tests
```

Validated package set:

```text
langgraph==1.2.10
langgraph-checkpoint-sqlite==3.1.1
langchain-mcp-adapters==0.3.1
mcp==1.28.1
```

LangGraph demonstrated stronger explicit persisted workflow/checkpoint durability. It also introduced more runtime topology/dependencies and explicit interrupt-node restart semantics. Repeated resume still required the ADS `ProposalLedger` to preserve authoritative exactly-once project meaning.

The MCP v1 pin is preserved as real dependency-maturity evidence because the released adapter's dependency range admitted an incompatible MCP v2 generation.

### Stop rule

Research 015 found no current Microsoft Agent Framework or Google ADK 2.0 differentiator likely to overturn the result. They are not implemented now and remain reopenable if a future first-order requirement justifies reconsideration.

Checkpoint 133 records the promotion and closure.

---

## 7. Immediate active track: retrieval and MethodologicalHorizon

Q-044 and Q-045 are now the highest-value methodological implementation questions.

Required work:

```text
retrieval-quality fixtures
production lexical retrieval
semantic retrieval candidate evaluation
lexical/semantic fusion only if justified
ranking and omission-quality evaluation
first real MethodologicalHorizon construction
selective LLM context assembly
recommendation quality separated from catalog/retrieval coverage
```

Evaluation must distinguish at least:

```text
knowledge absent from catalog
known but not retrieved
retrieved but judged inapplicable
applicable but ranked too low
recommended but skipped
recommended incorrectly
required concern omitted
```

Do not select an embedding model, reranker, ANN service, or vector database from intuition.

The first step after branch reconciliation is to inspect the current production persistence/retrieval implementation and define a benchmark before adding retrieval technology.

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
production FTS retrieval behavior/ranking
embedding model/provider
lexical/semantic fusion
reranker
complete Foundation 018 production schema
artifact-storage backend
job queue/cloud deployment
```

---

## 9. Exact next execution order

### A. COMPLETE RUNTIME-BRANCH RECONCILIATION AND MERGE

```text
1. reconcile CURRENT_STATE / KNOWLEDGE_MAP / OPEN_QUESTIONS / MAJOR_CHANGES
2. verify Checkpoint 133 metadata and branch CI
3. merge PR #8 into v1-frontend-spike if green
4. begin the next bounded branch from that promoted V1 boundary
```

### B. RETRIEVAL / METHODOLOGICALHORIZON BENCHMARK

```text
1. inspect current production retrieval and persistence surfaces
2. define benchmark fixtures, expected retrieval/horizon outcomes and failure categories
3. implement/evaluate lexical retrieval first
4. evaluate semantic retrieval as a candidate
5. add fusion/reranking only if measured evidence justifies it
6. construct and evaluate the first bounded real MethodologicalHorizon
7. measure selective LLM context quality and cost
```

### C. SELECTED RUNTIME PRODUCTION INTEGRATION

Integrate D-032 behind an ADS-owned port when the first real reasoning vertical slice requires it. Do not promote the experiment adapter wholesale or add runtime machinery before the application contract is clear.

### D. FUTURE COCKPIT CAPABILITY WORK

Build on Specification 008. Do not reopen the promoted basic interaction architecture without new evidence.

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

docs/research/010_2026_runtime_bakeoff_preimplementation_refresh.md
docs/research/011_openai_agents_0_19_4_released_api_compatibility_findings.md
docs/research/013_openai_agents_complete_candidate_evidence_and_direct_call_comparison.md
docs/research/014_langgraph_1_2_10_released_durability_comparator_audit.md
docs/research/015_langgraph_complete_candidate_three_way_runtime_comparison_and_stop_rule.md

experiments/runtime_bakeoff/DIRECT_CALL_CONTROL_RESULT.md
experiments/runtime_bakeoff/candidates/openai_agents/COMPLETE_RESULT.md
experiments/runtime_bakeoff/candidates/langgraph_runtime/COMPLETE_RESULT.md

docs/checkpoints/127_governed_knowledge_roundtrip_closed_across_sqlite_and_postgresql.md
docs/checkpoints/129_direct_model_call_runtime_control_cross_platform_gate_passed.md
docs/checkpoints/130_post_promotion_cockpit_normal_window_and_pinch_polish_gate_passed.md
docs/checkpoints/131_openai_agents_complete_runtime_candidate_cross_platform_gate_passed.md
docs/checkpoints/132_langgraph_durability_comparator_cross_platform_gate_passed.md
docs/checkpoints/133_v1_reasoning_runtime_selected_and_bakeoff_closed.md
```