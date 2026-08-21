# Current State

**Checkpoint:** 127  
**Date:** 2026-08-21  
**Active development branch:** `v1-frontend-spike`  
**Development stage:** Prototype V0 complete; bounded V1 implementation and integration across methodological knowledge, governed persistence/interchange, retrieval/MethodologicalHorizon construction, agent/runtime evaluation, and the promoted professional Project Cockpit interaction architecture  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate project priority:** Execute Specification 005's agent-runtime bakeoff beginning with one principal reasoner. The governed reusable-knowledge persistence/interchange seam is now closed across SQLite/Linux, SQLite/Windows, and PostgreSQL 18; retrieval/MethodologicalHorizon evaluation is the other highest-value active V1 track.

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

The Autonomous Data Science System is intended to become a professional interactive data-science operating environment in which the system carries much of the methodological memory, project memory, process navigation, evidence discipline, provenance, execution coordination, and reporting burden that otherwise has to be repeatedly supplied by a human through prompts.

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

Primary sources:

```text
docs/VISION.md
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
docs/experiments/prototype_v0/FINAL_RESULTS.md
```

---

## 2. Current project and methodological architecture

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

Foundation 020 promotes reusable methodological knowledge around:

```text
KnowledgeAsset
KnowledgeComponent
NarrativeFacet
KnowledgeRelation
Conditional KnowledgeRule
KnowledgeCollection
exact knowledge revisions
ExecutionCapability
project objects referencing/influenced by knowledge
```

No universal top-level `Assessment` object is currently justified. Subject-specific verdicts use the existing epistemic chain, with structured criterion Findings where useful:

```text
Question -> Evidence -> Finding -> Claim / Decision
```

---

## 3. Accepted V1 persistence and interchange

Accepted decisions/specifications currently include:

```text
D-028 + Specification 001
    SQLite-centered local-first operational architecture
    FTS5 rebuildable lexical index
    rebuildable embeddings / initial exact semantic retrieval
    application-level rule evaluator
    selective context assembly
    filesystem/Git/artifact storage outside the DB

D-029 + Specification 002
    SQLAlchemy Core 2.0
    Alembic 1.x

D-030 + Specification 003
    pyproject.toml
    uv + committed uv.lock
    uv_build
    src/ads_system
    Python >=3.12

D-031 + Specification 004
    JSON
    JSON Schema Draft 2020-12
    application semantic validation
    deterministic reusable-knowledge normalization/serialization
```

Checkpoint 114 proves the first production persistence vertical slice on SQLite/Linux, SQLite/Windows, and PostgreSQL 18, including exact historical project-to-knowledge revision pinning.

Checkpoint 115 validates the heterogeneous reusable-knowledge interchange contract across Linux/Windows and Python 3.12-3.14.

---

## 4. Governed knowledge round-trip is closed

Checkpoint 127 closes the richer governed reusable-knowledge persistence/interchange seam.

Validated behavior includes:

```text
candidate import
explicit acceptance
accepted-current pointers
accepted snapshot export
provenance
relation governance
collections
migration 0002
historical project revision pinning across later knowledge acceptance
```

Final validation:

```text
V1 governed knowledge roundtrip closure gate
run 32496856945

SQLite / Ubuntu     PASS
SQLite / Windows    PASS
PostgreSQL 18       PASS
Alembic revision-ID portability guard PASS on all three jobs
```

Final result source:

```text
experiments/architecture_spikes/V1_KNOWLEDGE_ROUNDTRIP_RESULT.md
```

Two PostgreSQL portability defects were found and fixed before closure:

```text
1. manually named migration constraint exceeded PostgreSQL's 63-byte identifier limit
2. migration revision `0002_reusable_knowledge_interchange` exceeded
   Alembic's default `alembic_version.version_num VARCHAR(32)` envelope
```

Migration 0002 now uses:

```text
revision = "0002_knowledge_interchange"
down_revision = "0001_v1_persistence_core"
```

No migration payload or governed-knowledge semantics changed.

A deterministic regression guard now enforces unique Alembic revision IDs with length <= 32 characters.

The temporary PostgreSQL diagnostic workflow was removed after closure. The temporary PR validation workflow is not part of the permanent active branch.

Q-048 is therefore answered/closed as an implementation gate.

This closure does **not** validate retrieval quality, embeddings, reranking, MethodologicalHorizon construction, selective LLM context quality, external-source ingestion, or knowledge-authoring UX.

---

## 5. Agent/runtime track

No agent framework, LLM provider, or multi-agent architecture is accepted yet.

The durable boundary is:

```text
ADS project/domain/methodological semantics
    owned by ADS

agent runtimes / MCP / A2A / AG-UI / runtime checkpoints
    replaceable infrastructure/interoperability
```

Specification 005 defines the runtime bakeoff among:

```text
OpenAI Agents SDK
LangGraph
Microsoft Agent Framework
Google ADK 2.0
```

The bakeoff begins with one principal reasoner. A simpler direct-model-call result remains valid if no framework earns its complexity.

This is now the immediate bounded execution track.

---

## 6. Professional frontend and promoted Project Cockpit interaction architecture

Foundation 021 makes the frontend a first-class reasoning, control, and quality surface.

The Project Cockpit is now the promoted V1 primary active-work interaction model.

Current authoritative interaction contract:

```text
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
```

Promoted product model:

```text
Project Cockpit
    primary immersive active-work environment
    living project-process projection
    native system interaction
    spatial navigation
    focused analytical work

Direct specialist project views
    alternative entry / inspection / record paths
    reuse the same substantive modules/state
```

Promoted interaction architecture includes:

```text
meaningful work units rather than every persisted object
spatial focus into real specialist workspaces
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
keyboard accessibility
reduced-motion support
world-owned restrained ambient depth
```

Final promotion implementation head:

```text
2c3b522e2416d73c015ce5ec2a4560a227524dd9
```

Final frontend validation:

```text
V1 frontend spike
run 155 / 32492536072

Ubuntu build + unit tests                 PASS
Windows build + unit tests                PASS
Chromium interaction/accessibility        PASS
controlled direct-project visual regression PASS
```

The remaining tiny occasional native-pinch hitch is known, real, non-blocking, and deferred product polish.

Future Cockpit work should build on Specification 008 rather than reopening the basic interaction architecture without new evidence.

---

## 7. Retrieval / MethodologicalHorizon track

The persistence/interchange seam is now stable enough that retrieval evaluation no longer needs to compete with unresolved cross-backend migration debugging.

Still required:

```text
retrieval-quality fixtures
production lexical retrieval
semantic retrieval candidate evaluation
lexical/semantic fusion only if justified
ranking and omission-quality evaluation
first real MethodologicalHorizon construction
selective LLM context assembly
```

The benchmark must distinguish failure modes such as:

```text
knowledge absent from catalog
known but not retrieved
retrieved but judged inapplicable
applicable but ranked too low
recommended incorrectly
required concern omitted
```

Do not choose an embedding model, reranker, ANN service, or vector database from intuition.

---

## 8. Current major non-selections

Do not infer acceptance of any of these merely because they have been discussed or used in a spike:

```text
agent runtime
number of agents
LLM provider/model
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
final native-pinch normalization/sensitivity constants
final geometric zoom range
final finite-world extent algorithm
infinite-canvas semantics
final pan-reserve dimensions
pan/zoom/HUD/control-fold persistence contract
production project-search backend
Cockpit final stage taxonomy
Cockpit final stage widths
Cockpit final stage-ruler material/treatment
permanent vertical map-tool-rail styling/iconography
Cockpit final public URL contract
Cockpit final visual identity
exact permanent ambient-grid/gradient styling
canonical Cockpit screenshot baseline
system/persona name
Tauri desktop packaging
backend HTTP/API framework
production FTS implementation
embedding model/provider
lexical/semantic fusion
reranker
complete Foundation 018 production schema
artifact-storage backend
job queue/cloud deployment
```

Specification 008 promotes Cockpit interaction architecture, not these final implementation or visual choices.

---

## 9. Exact next execution order

### A. AGENT RUNTIME BAKEOFF

Execute Specification 005 with one principal reasoner first.

The evaluation must preserve ADS-owned domain/project/methodological semantics outside the candidate runtime and must allow the outcome:

```text
no framework earns its complexity
    -> retain simpler direct model calls
```

Do not infer a multi-agent architecture merely because runtime frameworks support one.

### B. RETRIEVAL / METHODOLOGICALHORIZON BENCHMARK

Build the first production retrieval/horizon evaluation now that the governed persistence seam is closed.

```text
retrieval-quality fixtures
production lexical retrieval
semantic retrieval candidate evaluation
fusion only if justified
ranking / omission-quality evaluation
first bounded MethodologicalHorizon
selective LLM context assembly
```

### C. FUTURE COCKPIT CAPABILITY / PRODUCT WORK

Build on Specification 008 with deeper specialist workspaces, production system conversation, real project-state integration, semantic scale/grouping, project auto-layout, broader project-size tests, and later visual/input polish.

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
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md

docs/specifications/004_v1_reusable_knowledge_interchange.md
docs/specifications/005_v1_agent_runtime_and_interoperability_bakeoff.md
docs/specifications/006_v1_frontend_architecture_and_visual_spike.md
docs/specifications/008_v1_project_cockpit_interaction_architecture.md

experiments/architecture_spikes/V1_KNOWLEDGE_ROUNDTRIP_RESULT.md

docs/checkpoints/114_first_production_v1_persistence_vertical_slice_passed.md
docs/checkpoints/115_reusable_knowledge_interchange_contract_validated.md
docs/checkpoints/120_unplanned_session_boundary_reconciliation_and_v1_continuity_restored.md
docs/checkpoints/126_seventh_cockpit_review_validated_and_interaction_architecture_promoted.md
docs/checkpoints/127_governed_knowledge_roundtrip_closed_across_sqlite_and_postgresql.md
```
