# Current State

**Checkpoint:** 128  
**Date:** 2026-08-21  
**Active development branch:** `v1-frontend-spike`  
**Development stage:** Prototype V0 complete; bounded V1 implementation and integration across methodological knowledge, governed persistence/interchange, retrieval/MethodologicalHorizon construction, agent/runtime evaluation, and the promoted professional Project Cockpit interaction architecture  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate project priority:** Implement Specification 005's deterministic ADS-owned runtime-bakeoff harness, then execute the direct-call control and first OpenAI Agents SDK candidate. LangGraph is the next durability comparator. No runtime is selected.

## Active ChatGPT development context

```text
Design session: 03
ChatGPT project: Autonomous Data Science System
Session title: 03 - Project Cockpit & V1 Integration
```

Repository artifacts remain authoritative across chats.

Current bounded V1/frontend work lives on:

```text
v1-frontend-spike
```

The default `main` branch intentionally trails this work and must not be treated as the latest V1/frontend state until an explicit merge/promotion occurs.

---

## 1. System purpose and V0 constraint

ADS is intended to become a professional interactive data-science operating environment in which the system carries much of the methodological memory, project memory, process navigation, evidence discipline, provenance, execution coordination, and reporting burden that otherwise has to be repeatedly supplied by a human through prompts.

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

The intended scaling path is:

```text
large global methodological knowledge universe
    -> project-specific retrieval/filtering
    -> bounded MethodologicalHorizon
    -> explicit applicability/context checks
    -> flexible relevance/prioritization reasoning
    -> selective task-specific LLM context
```

Foundation 020 promotes reusable methodological knowledge around `KnowledgeAsset`, `KnowledgeComponent`, `NarrativeFacet`, `KnowledgeRelation`, conditional `KnowledgeRule`, `KnowledgeCollection`, exact revisions, and `ExecutionCapability`.

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
    unique Alembic revision IDs <= 32 chars while default version table remains

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

Final result:

```text
experiments/architecture_spikes/V1_KNOWLEDGE_ROUNDTRIP_RESULT.md
```

Q-048 is closed for the current governed seam.

---

## 4. Project Cockpit interaction architecture is promoted

Specification 008 is the current V1 Project Cockpit interaction contract after seven real-browser human review cycles.

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

Final promotion gate:

```text
head 2c3b522e2416d73c015ce5ec2a4560a227524dd9
run 155 / 32492536072

Ubuntu build + unit tests                  PASS
Windows build + unit tests                 PASS
Chromium interaction/accessibility         PASS
controlled direct-view visual regression   PASS
```

The tiny remaining native-pinch hitch is known, real, non-blocking deferred polish.

Future Cockpit work builds on Specification 008 rather than reopening the basic interaction architecture without new evidence.

---

## 5. Runtime bakeoff is now the active implementation track

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

Research 010 refreshed the candidate ecosystem against current official documentation on 2026-08-21.

Current **implementation order**, not selection:

```text
CONTROL
    ADS-owned direct model-call runtime

FIRST FRAMEWORK CANDIDATE
    OpenAI Agents SDK

SECOND FRAMEWORK CANDIDATE
    LangGraph

SECONDARY / CONDITIONAL
    Microsoft Agent Framework
    Google ADK 2.0
```

Fresh evidence supporting the order:

```text
OpenAI Agents SDK
    serializable RunState
    structured tool approval interruptions
    local MCP integration
    model/tool timeouts and replay-aware retries
    deterministic provider-neutral ScriptedModel testing

LangGraph
    strongest persistence/durability comparator
    explicit interrupt/checkpoint semantics
    Functional API can minimize graph intrusion
    interrupted node restarts, so side-effect idempotency must be tested

Microsoft Agent Framework
    credible MCP/HITL/checkpoint/provider surface
    Python Functional Workflow API currently experimental

Google ADK 2.0
    GA workflow/runtime family
    Tool Confirmation currently experimental
    resumability documented as best-effort / at-least-once
```

Direct calls remain a valid final winner if no framework earns its dependency/operational burden.

Primary sources:

```text
docs/research/001_2026_agentic_ecosystem_and_integration_architecture_audit.md
docs/research/010_2026_runtime_bakeoff_preimplementation_refresh.md
docs/specifications/005_v1_agent_runtime_and_interoperability_bakeoff.md
docs/checkpoints/128_runtime_bakeoff_preimplementation_evidence_refreshed.md
```

---

## 6. Immediate runtime implementation boundary

Before importing candidate framework types into production application/domain modules, create an isolated ADS-owned bakeoff harness.

The harness should own experiment-level representations for:

```text
ProjectContextSnapshot
MethodologicalContextPack
RuntimeWorkloadInput
RuntimeRecommendation
RuntimeInterrupt
RuntimeResumeToken
RuntimeTrace
RuntimeOutcome
```

Exact names are provisional and do not freeze the final production `ReasoningRuntime` port.

The harness must also own:

```text
canonical representative workload fixture
context-pack digest
exact knowledge revision references
at-most-once proposal side-effect ledger
fake deterministic model script
local side-effect-free MCP reference server/gateway
normalized AR-01 through AR-12 evidence
```

Framework-specific types stay below adapters and outside `ads_system.domain`.

---

## 7. Retrieval / MethodologicalHorizon track

Now that the governed persistence seam is closed, the other highest-value V1 track remains:

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

## 8. Current major non-selections

Still deliberately unselected:

```text
agent runtime
number of agents
LLM provider/model
durable runtime backend
MCP server catalog
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

## 9. Exact next execution order

### A. RUNTIME BAKEOFF HARNESS

```text
1. create isolated runtime-bakeoff implementation branch
2. build ADS-owned deterministic harness and representative fixture
3. build direct-call control
4. build OpenAI Agents SDK adapter using fake/scripted model first
5. evaluate AR-01 through AR-12 without paid calls wherever possible
6. build LangGraph durability comparator if still decision-relevant
7. decide from evidence whether Microsoft/Google adapters are needed
8. use live provider calls only where deterministic infrastructure cannot establish behavior
9. make explicit runtime/no-runtime promotion decision
```

### B. RETRIEVAL / METHODOLOGICALHORIZON BENCHMARK

Proceed after or in parallel where it does not compete with the runtime experiment.

### C. FUTURE COCKPIT CAPABILITY WORK

Build on Specification 008 after current backend/runtime seams are better established.

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

docs/research/001_2026_agentic_ecosystem_and_integration_architecture_audit.md
docs/research/010_2026_runtime_bakeoff_preimplementation_refresh.md

docs/specifications/005_v1_agent_runtime_and_interoperability_bakeoff.md
docs/specifications/008_v1_project_cockpit_interaction_architecture.md

experiments/architecture_spikes/V1_KNOWLEDGE_ROUNDTRIP_RESULT.md

docs/checkpoints/126_seventh_cockpit_review_validated_and_interaction_architecture_promoted.md
docs/checkpoints/127_governed_knowledge_roundtrip_closed_across_sqlite_and_postgresql.md
docs/checkpoints/128_runtime_bakeoff_preimplementation_evidence_refreshed.md
```
