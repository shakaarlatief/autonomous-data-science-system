# Current State

**Checkpoint:** 130  
**Date:** 2026-08-21  
**Active development branch:** `v1-runtime-bakeoff`  
**Development stage:** Prototype V0 complete; bounded V1 implementation and integration across methodological knowledge, governed persistence/interchange, retrieval/MethodologicalHorizon construction, runtime evaluation, and the promoted professional Project Cockpit interaction architecture  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate project priority:** Complete the remaining OpenAI Agents SDK core bakeoff gates (`AR-03`, `AR-08`, `AR-09`, `AR-11`) against the validated direct-call control, while a short human retest confirms the latest post-promotion Cockpit Jump/composer and faster-pinch polish. No runtime is selected.

## Active ChatGPT development context

```text
Design session: 03
ChatGPT project: Autonomous Data Science System
Session title: 03 - Project Cockpit & V1 Integration
```

Repository artifacts remain authoritative across chats.

Current executable runtime work and the latest frontend polish live on:

```text
v1-runtime-bakeoff
```

The preserved promoted V1/frontend boundary remains on `v1-frontend-spike`. The default `main` branch intentionally trails current V1 work until an explicit merge/promotion occurs.

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

## 4. Project Cockpit interaction architecture is promoted; latest polish awaits a short human retest

Specification 008 remains the accepted V1 Project Cockpit interaction contract after seven real-browser human review cycles.

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

Promotion gate:

```text
head 2c3b522e2416d73c015ce5ec2a4560a227524dd9
run 155 / 32492536072

Ubuntu build + unit tests                  PASS
Windows build + unit tests                 PASS
Chromium interaction/accessibility         PASS
controlled direct-view visual regression   PASS
```

A later post-promotion human review found two bounded polish issues:

```text
normal Chrome window
    Jump/search could overlap the persistent composer

native trackpad pinch
    substantially smoother than before
    but scale travel per physical gesture still too slow
```

Checkpoint 130 records the bounded repair:

```text
Jump/search
    actual composer geometry is now measured while the palette is open
    palette re-clamps on resize / fullscreen / composer resize
    lower results remain internally scrollable

pinch
    sensitivity 0.0018 -> 0.0024
    coalescing / bounded delta / anchoring retained
```

Automated validation:

```text
head ae83e920b3fa43ee8242bdb1ca2640d23a474c71
run 167 / 32503861255

Ubuntu build + unit tests                  PASS
Windows build + unit tests                 PASS
Chromium interaction/accessibility         PASS
controlled direct-view visual regression   PASS
normal-window Jump re-clamp regression      PASS
faster anchored pinch regression            PASS
```

The tiny remaining native-pinch hitch is still known, real, and non-blocking deferred polish. Exact pinch constants remain unfrozen.

Short human retest still required:

```text
normal window: Jump panel stays above composer and lower results scroll
fullscreen: no regression
trackpad: one natural full pinch in/out has sufficient scale travel
```

Future Cockpit work builds on Specification 008 rather than reopening the basic interaction architecture without new evidence.

---

## 5. Runtime bakeoff is the main active implementation track

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

Research 010 refreshed the ecosystem before implementation. Research 011 then corrected an important package/documentation assumption discovered executable-first: current documentation exposes `agents.testing.ScriptedModel`, but published `openai-agents==0.19.4` does not ship `agents.testing`. The released public `Model` boundary is sufficient for an experiment-local deterministic fake.

Current evaluation order, not selection:

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

### Direct-call control

Checkpoint 129 establishes the executable simpler control.

Validated behavior includes:

```text
ADS-owned model/tool loop
selective context digest + exact knowledge revision provenance
approval interrupt before project-state side effect
serialized process-boundary resume
ADS-owned at-most-once proposal ledger
rejection
stale-context rejection
retry/cancellation handling
normalized trace
ADS-owned structured recommendation
```

Cross-platform direct-control gate:

```text
run 32500521858
Ubuntu PASS
Windows PASS
existing Python suite PASS
```

### OpenAI Agents SDK 0.19.4 core candidate

The candidate is isolated under `experiments/runtime_bakeoff/candidates/openai_agents/`; the framework is not an unconditional ADS dependency and does not enter `ads_system.domain`.

Validated core behavior now includes:

```text
AR-01 domain isolation
AR-02 single-agent tool loop
AR-04 native approval interruption
AR-05 serialized RunState process-boundary resume
AR-06 ADS remains project-state authority
AR-07 context/revision transparency
AR-10 structured output + ADS provenance validation
AR-12 deterministic no-live-provider testing via released public Model boundary
```

Core candidate gate:

```text
run 15 / 32501907783
OpenAI core Ubuntu PASS
OpenAI core Windows PASS
direct controls PASS
existing Python suite PASS
```

The latest combined branch gate after the frontend polish also remained green:

```text
run 20 / 32503861259
OpenAI core Ubuntu PASS
OpenAI core Windows PASS
direct controls Ubuntu PASS
direct controls Windows PASS
existing Python suite PASS
```

OpenAI candidate work still required before any selection judgment:

```text
AR-03 current MCP integration
AR-08 cancellation and bounded timeout
AR-09 controlled failure/retry behavior
AR-11 normalized observability
```

Direct calls remain a valid final winner if no framework earns its dependency and operational burden.

---

## 6. Retrieval / MethodologicalHorizon track

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

## 7. Current major non-selections

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

## 8. Exact next execution order

### A. SHORT HUMAN COCKPIT RETEST

```text
1. pull latest v1-runtime-bakeoff
2. normal Chrome window: open Jump/search and confirm no composer overlap
3. scroll lower Jump results
4. enter fullscreen and confirm no regression
5. real trackpad: one natural full pinch in/out and judge scale travel
```

This is a bounded polish gate, not a reopening of Specification 008.

### B. COMPLETE OPENAI RUNTIME CANDIDATE

```text
1. implement/test AR-03 MCP integration
2. implement/test AR-08 cancellation + bounded timeout
3. implement/test AR-09 controlled failure/retry semantics
4. implement/test AR-11 normalized observability
5. compare completed OpenAI evidence against direct-call control
6. implement LangGraph durability comparator if still decision-relevant
7. decide from evidence whether Microsoft/Google adapters are needed
8. use live provider calls only where deterministic infrastructure cannot establish behavior
9. make explicit runtime/no-runtime promotion decision
```

### C. RETRIEVAL / METHODOLOGICALHORIZON BENCHMARK

Proceed after or in parallel where it does not compete with the runtime experiment.

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

docs/research/010_2026_runtime_bakeoff_preimplementation_refresh.md
docs/research/011_openai_agents_0_19_4_released_api_compatibility_findings.md
docs/research/012_post_promotion_cockpit_normal_window_and_pinch_sensitivity_review.md

docs/specifications/005_v1_agent_runtime_and_interoperability_bakeoff.md
docs/specifications/008_v1_project_cockpit_interaction_architecture.md

experiments/architecture_spikes/V1_KNOWLEDGE_ROUNDTRIP_RESULT.md
experiments/runtime_bakeoff/DIRECT_CALL_CONTROL_RESULT.md
experiments/runtime_bakeoff/candidates/openai_agents/CORE_RESULT.md

docs/checkpoints/127_governed_knowledge_roundtrip_closed_across_sqlite_and_postgresql.md
docs/checkpoints/128_runtime_bakeoff_preimplementation_evidence_refreshed.md
docs/checkpoints/129_direct_call_control_runtime_baseline_passed.md
docs/checkpoints/130_post_promotion_cockpit_normal_window_and_pinch_polish_gate_passed.md
```