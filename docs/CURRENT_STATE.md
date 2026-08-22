# Current State

**Checkpoint:** 131  
**Date:** 2026-08-22  
**Active development branch:** `v1-runtime-bakeoff`  
**Development stage:** Prototype V0 complete; bounded V1 implementation and integration across methodological knowledge, governed persistence/interchange, retrieval/MethodologicalHorizon construction, runtime evaluation, and the promoted professional Project Cockpit interaction architecture  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate project priority:** Implement the LangGraph durability comparator against the validated direct-call control and the complete OpenAI Agents SDK 0.19.4 candidate. No runtime is selected.

## Active ChatGPT development context

```text
Design session: 03
ChatGPT project: Autonomous Data Science System
Session title: 03 - Project Cockpit & V1 Integration
```

Repository artifacts remain authoritative across chats.

Current executable runtime work lives on:

```text
v1-runtime-bakeoff
```

The preserved promoted V1/frontend boundary remains on `v1-frontend-spike`. The default `main` branch intentionally trails current V1 work until an explicit merge/promotion occurs.

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

and preserves distinctions including:

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

## 3. Accepted V1 persistence/interchange

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
    unique Alembic revision IDs <= 32 chars while the default version table remains

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

Checkpoint 127 closes the richer governed reusable-knowledge persistence/interchange seam.

Final validation:

```text
V1 governed knowledge roundtrip closure gate
run 32496856945

SQLite / Ubuntu     PASS
SQLite / Windows    PASS
PostgreSQL 18       PASS
Alembic revision-ID portability guard PASS on all three jobs
```

Q-048 is closed for the current governed seam.

---

## 4. Project Cockpit interaction architecture is promoted

Specification 008 is the current V1 Project Cockpit interaction contract.

Promoted interaction principles include:

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

Checkpoint 130 subsequently validated two bounded post-promotion implementation repairs:

```text
Jump/search
    dynamically re-clamps above the actual rendered composer in shorter normal windows

native pinch
    sensitivity increased to 0.0024 while preserving coalescing, bounded delta and anchoring
```

Frontend run `167 / 32503861255` passed Ubuntu, Windows, Chromium interaction/accessibility, controlled visual regression, normal-window Jump re-clamping, and the faster anchored-pinch regression. The user's subsequent real-browser retest was accepted as good enough to continue.

The tiny occasional pinch hitch remains non-blocking deferred polish. Exact gesture constants and future Cockpit capabilities remain unfrozen.

---

## 5. Runtime bakeoff is the active implementation track

No agent framework, LLM provider, or multi-agent architecture is accepted.

Durable boundary:

```text
ADS project/domain/methodological semantics
    owned by ADS

agent runtimes / MCP / runtime checkpoints
    replaceable infrastructure
```

Specification 005 defines mandatory gates AR-01 through AR-12 for:

```text
domain isolation
single-agent tool loop
current MCP integration
human approval interrupt
durable process-boundary resume
external project-state authority
context transparency
cancellation/timeouts
failure/retry behavior
ADS-owned structured output
observability
provider/fake-model substitution
```

The ADS-owned framework-neutral harness remains authoritative for candidate comparison and owns the representative workload, context digest/revision provenance, approval/resume semantics, proposal idempotency ledger, and normalized trace/result contract.

---

## 6. Direct model-call control is viable

Checkpoint 129 records the direct-call control cross-platform PASS:

```text
workflow 32500521858
Ubuntu PASS
Windows PASS
existing Python suite PASS
```

The direct-call path proves ADS can implement the required workload without an agent framework, including:

```text
model/tool loop
approval interruption
process-boundary resume
controlled retry
cancellation
stale-context rejection
structured output
normalized trace
at-most-once authoritative proposal meaning through ADS ProposalLedger
```

Its main cost is explicit custom orchestration machinery.

Primary result:

```text
experiments/runtime_bakeoff/DIRECT_CALL_CONTROL_RESULT.md
```

---

## 7. OpenAI Agents SDK 0.19.4 complete candidate is viable

Checkpoint 131 records a complete cross-platform PASS for all Specification 005 mandatory gates.

Validated implementation:

```text
08c1c41246d8ece21e443d938ed477176505e40f
```

Validation:

```text
V1 runtime bakeoff
run 32555526773

Ubuntu
    direct/control harness + full Python suite PASS
    OpenAI Agents complete candidate PASS

Windows
    direct/control harness + full Python suite PASS
    OpenAI Agents complete candidate PASS
```

Mandatory result:

```text
AR-01 through AR-12 PASS
```

New complete-candidate evidence includes:

```text
real local stdio MCP through released MCPServerStdio
application-owned cancellation by ADS run_id
released function-tool timeout -> ToolTimeoutError
controlled read failure/model retry
ADS ProposalLedger preserving authoritative idempotency under replay
SDK lifecycle hooks normalized into ADS RuntimeTrace
```

OpenAI Agents SDK removes meaningful custom plumbing around tool iteration/schema dispatch, approval interruption, serializable/restorable RunState, structured-output validation, native MCP, tool timeouts, and lifecycle hooks.

ADS still owns project/methodological semantics, context construction/digest/revisions, stale-context rejection, human/cancellation policy, side-effect idempotency/domain events, stable normalized provenance, and framework adapter/version compatibility.

Research 011 remains important maturity evidence: published `openai-agents==0.19.4` did not ship the currently documented `agents.testing.ScriptedModel`, so deterministic testing required an experiment-local fake against the released public `Model` interface.

Primary sources:

```text
experiments/runtime_bakeoff/candidates/openai_agents/COMPLETE_RESULT.md
docs/research/011_openai_agents_0_19_4_released_api_compatibility_findings.md
docs/research/013_openai_agents_complete_candidate_evidence_and_direct_call_comparison.md
docs/checkpoints/131_openai_agents_complete_runtime_candidate_cross_platform_gate_passed.md
```

OpenAI Agents SDK is technically viable but **not selected**.

---

## 8. Exact next runtime comparator

LangGraph remains decision-relevant as the strongest durability/checkpoint comparator.

The next implementation must begin with the currently released API surface, not documentation assumptions, and must preserve the same ADS-owned harness/authority boundary.

Priority evidence:

```text
process-boundary checkpoint/resume
interrupt/replay semantics
whether an interrupted node restarts on resume
side-effect placement and ADS idempotency under replay
external project-state authority
provider-neutral deterministic testing
normalized ADS observability
```

If technically viable, complete the same AR-01 through AR-12 contract so direct calls, OpenAI Agents SDK and LangGraph can be compared on equal ADS-shaped evidence.

Only after that comparison should we decide whether Microsoft Agent Framework or Google ADK 2.0 could plausibly change the result enough to justify additional adapters.

---

## 9. Retrieval / MethodologicalHorizon track

The other highest-value V1 track remains:

```text
retrieval-quality fixtures
production lexical retrieval
semantic retrieval candidate evaluation
lexical/semantic fusion only if justified
ranking and omission-quality evaluation
first real MethodologicalHorizon construction
selective LLM context assembly
```

Do not choose an embedding model, reranker, ANN service, or vector database from intuition.

---

## 10. Current major non-selections

Still deliberately unselected:

```text
agent runtime
number of agents
LLM provider/model
durable runtime backend
MCP production server catalog
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
production FTS implementation
embedding model/provider
lexical/semantic fusion
reranker
complete Foundation 018 production schema
artifact-storage backend
job queue/cloud deployment
```

---

## 11. Exact next execution order

### A. LANGGRAPH DURABILITY COMPARATOR

```text
1. audit the currently released LangGraph package/API surface
2. isolate candidate code under experiments/runtime_bakeoff/candidates/langgraph/
3. run the same representative ADS workload with deterministic provider-free model behavior
4. test durable checkpoint/process-boundary resume
5. explicitly test interrupt-node restart/replay semantics and side-effect idempotency
6. complete AR-01 through AR-12 if the candidate remains viable
7. compare direct calls vs OpenAI vs LangGraph on capability, durability, custom machinery, coupling, maturity, testability and operational burden
8. decide whether Microsoft/Google could still change the selection outcome
9. make an explicit runtime/no-runtime promotion decision only from evidence
```

### B. RETRIEVAL / METHODOLOGICALHORIZON BENCHMARK

Proceed after or in parallel where it does not compete with the runtime experiment.

### C. FUTURE COCKPIT CAPABILITY WORK

Build on Specification 008. Do not reopen the promoted basic interaction architecture without new evidence.

---

## 12. Minimum reading for continuation

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

docs/research/010_2026_runtime_bakeoff_preimplementation_refresh.md
docs/research/011_openai_agents_0_19_4_released_api_compatibility_findings.md
docs/research/013_openai_agents_complete_candidate_evidence_and_direct_call_comparison.md

docs/specifications/005_v1_agent_runtime_and_interoperability_bakeoff.md
docs/specifications/008_v1_project_cockpit_interaction_architecture.md

experiments/runtime_bakeoff/DIRECT_CALL_CONTROL_RESULT.md
experiments/runtime_bakeoff/candidates/openai_agents/COMPLETE_RESULT.md

docs/checkpoints/129_direct_model_call_runtime_control_cross_platform_gate_passed.md
docs/checkpoints/130_post_promotion_cockpit_normal_window_and_pinch_polish_gate_passed.md
docs/checkpoints/131_openai_agents_complete_runtime_candidate_cross_platform_gate_passed.md
```
