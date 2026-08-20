# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources but does not replace them.  
**Last reviewed:** 2026-08-20  
**Current checkpoint:** 118

## Start here

For a new session or quick reconstruction:

```text
README.md
    project-level overview

docs/CURRENT_STATE.md
    present state and exact active priority

docs/KNOWLEDGE_MAP.md
    routing layer

docs/VISION.md
    system purpose and vision

docs/PRINCIPLES.md
    current principles

docs/DECISIONS.md
    accepted project-level decisions

docs/OPEN_QUESTIONS.md
    unresolved canonical questions

docs/DEVELOPMENT_METHOD.md
    development/preservation method

docs/CONTINUITY.md
    cross-session continuation procedure

docs/MAJOR_CHANGES.md
    selective structural history
```

Prototype V0 is complete and its final classification is **STRONG FALSIFICATION OF THE CURRENT P0 DESIGN**.

The project is now implementing bounded V1 slices across:

```text
methodological knowledge
governed persistence/interchange
retrieval/horizon construction
agent/runtime infrastructure
professional frontend
unified Project Cockpit
```

The immediate frontend priority is human review of the first executable Cockpit interaction spike before its visual direction is frozen.

---

## System purpose and long-term product vision

Primary sources:

```text
docs/VISION.md
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
```

Foundation 013 defines the LLM/system/human boundary.

Foundation 017 makes the target product concrete as an interactive data-science workspace.

Foundation 021 strengthens the interface requirement into a first-class modern, polished, visually excellent professional analytical product rather than an end-stage dashboard or chat shell.

Historical origin:

```text
docs/foundations/001_initial_vision_and_reasoning.md
docs/checkpoints/022_system_level_abstraction_and_reusable_reasoning_vision.md
```

---

## Prototype V0 evidence and constraint

Final evidence:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
```

Final classification:

```text
STRONG FALSIFICATION OF THE CURRENT P0 DESIGN
```

Core scaling lesson:

```text
what the SYSTEM should remember
    !=
what the LLM should receive on every reasoning call
```

Do not reintroduce P0's full structured state/context, large always-on frontier, generic recursive reopening, or path-sensitive activation unchanged.

Relevant implementation/history:

```text
prototype_v0/src/ads_v0/p0.py
prototype_v0/src/ads_v0/p0_controller.py
prototype_v0/src/ads_v0/p0_schema.py
```

---

## Project object model and professional developer workflow

Primary source:

```text
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
```

Important distinctions:

```text
Investigation != Run
Evidence != Finding
Finding != Claim
Claim != Decision
current state != event history
persisted object != derived recommendation
workspace section != fundamental object
```

The current design does not add a universal project `Assessment` object.

Subject-specific verdicts use:

```text
Question -> Evidence -> Finding -> Claim/Decision
```

with structured criterion Findings where useful.

Professional-workflow principles:

```text
docs/PRINCIPLES.md, P-023 and P-024
```

Responsibility split:

```text
Autonomous Data Science System
    project/process control plane

VS Code
    developer workbench

Python / Docker / local or remote compute
    execution plane

Git + GitHub
    source versioning, collaboration, provenance
```

---

## Methodological-navigation brain and relevance architecture

Primary source:

```text
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
```

Current relevance progression:

```text
KNOWN
    -> APPLICABLE
    -> RELEVANT
    -> RECOMMENDED
    -> REQUIRED / BLOCKING
```

Core scaling concept:

```text
large global knowledge universe
    -> project-specific retrieval/filtering
    -> bounded methodological horizon
    -> explicit checks + flexible reasoning
    -> inspectable recommendation/requiredness
    -> selective task-specific LLM context
```

---

## Reusable methodological-knowledge representation

Primary source:

```text
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
```

Promoted representation:

```text
KnowledgeAsset
KnowledgeComponent
NarrativeFacet
KnowledgeRelation
Conditional KnowledgeRule
KnowledgeCollection
project objects referencing/influenced by exact knowledge revisions
criterion Finding
ExecutionCapability
derived Views
```

Durable distinctions:

```text
intrinsic knowledge kind != reasoning function
asset != component != narrative facet
static semantic relation != conditional methodological rule
retrieval cue != applicability predicate != required context != project relevance
methodological knowledge != execution implementation
global knowledge != project-specific state
internal representation != human-facing tree/workflow
```

Promoted principles:

```text
docs/PRINCIPLES.md, P-025 and P-026
```

Important design history:

```text
docs/checkpoints/101_five_example_reusable_knowledge_stress_test_completed.md
docs/checkpoints/102_candidate_conceptual_knowledge_representation_contract.md
docs/checkpoints/104_adversarial_review_of_candidate_knowledge_representation.md
docs/checkpoints/105_refined_representation_second_stress_test.md
```

---

## V1 implementation requirements

Primary source:

```text
docs/checkpoints/107_implementation_requirements_for_methodological_knowledge_subsystem.md
```

Checkpoint 107 derives technology-neutral requirements before architecture selection, including revisions, provenance, typed relations, conditional rules, retrieval, project-state lookup, horizon construction, selective context assembly, governance, integrity, backup, and portability.

---

## Accepted V1 persistence/retrieval architecture

Primary sources:

```text
docs/DECISIONS.md, D-028
docs/checkpoints/108_v1_architecture_comparison_and_sqlite_centered_selection.md
docs/specifications/001_v1_sqlite_technical_architecture.md
```

Accepted architecture family:

```text
SQLite-centered local-first operational architecture
```

Direction:

```text
SQLite
    reusable knowledge identities/revisions/components
    typed relations and conditional rules
    provenance/governance
    project epistemic and decision state
    exact project -> knowledge revision references
    execution-capability metadata

FTS5
    rebuildable lexical index

rebuildable embeddings
    initial in-process exact semantic search

application rule evaluator
    predicate / ALL / ANY / NOT / TRUE / FALSE / UNKNOWN

selective context assembler

filesystem / Git / artifact storage
    source code and large artifacts outside SQLite
```

PostgreSQL + pgvector remains the preferred first migration family if later concurrency/shared-server/vector-scale needs exceed the SQLite envelope.

Architecture evidence:

```text
experiments/architecture_spikes/sqlite_v1_viability.py
experiments/architecture_spikes/V1_ARCHITECTURE_GATE_RESULT.md
docs/checkpoints/111_v1_technical_architecture_gate_passed_and_specification_001_promoted.md
```

FT-05 validates the retrieval seam only. It does not validate production retrieval quality or embedding choice.

---

## Accepted implementation and Python tooling

Persistence:

```text
docs/DECISIONS.md, D-029
docs/specifications/002_v1_persistence_tooling_standard.md
```

Accepted:

```text
SQLAlchemy Core 2.0 stable series
Alembic 1.x
SQLAlchemy ORM not primary domain/persistence model
raw DBAPI only for narrow backend-specific behavior
```

Python project:

```text
docs/DECISIONS.md, D-030
docs/specifications/003_v1_python_project_and_dependency_tooling.md
```

Accepted:

```text
pyproject.toml
uv 0.12.5
committed cross-platform uv.lock
uv_build
src/ads_system
Python >=3.12
```

Evidence:

```text
docs/checkpoints/112_v1_persistence_tooling_selected_and_validated.md
docs/checkpoints/113_v1_python_project_tooling_validated.md
experiments/architecture_spikes/V1_PERSISTENCE_TOOLING_RESULT.md
experiments/architecture_spikes/V1_PYTHON_PROJECT_TOOLING_RESULT.md
```

---

## First production persistence vertical slice

Primary milestone:

```text
docs/checkpoints/114_first_production_v1_persistence_vertical_slice_passed.md
experiments/architecture_spikes/V1_PRODUCTION_PERSISTENCE_SLICE_RESULT.md
```

Production package:

```text
src/ads_system/domain/
src/ads_system/application/
src/ads_system/infrastructure/persistence/
migrations/
tests/integration/
```

The same application/repository scenario passed on SQLite/Linux, SQLite/Windows, and PostgreSQL 18.

It proves a project Finding pinned to Random Forest R1 remains pinned to R1 after R2 becomes current.

---

## Accepted reusable-knowledge interchange

Primary sources:

```text
docs/DECISIONS.md, D-031
docs/specifications/004_v1_reusable_knowledge_interchange.md
docs/checkpoints/115_reusable_knowledge_interchange_contract_validated.md
experiments/architecture_spikes/V1_KNOWLEDGE_INTERCHANGE_RESULT.md
```

Accepted V1 interchange:

```text
JSON
+ JSON Schema Draft 2020-12
+ application semantic validation
+ deterministic normalization / serialization
```

Key authority rule:

```text
operational database authority
    !=
interchange representation
    !=
derived retrieval indexes
```

Normal candidate/benchmark import cannot silently create accepted methodological authority.

---

## Governed knowledge round-trip status

The production bridge includes candidate import, explicit acceptance, accepted snapshot export, provenance, relation governance, collections, migration 0002, and historical project-revision pinning.

Last canonically confirmed gate status:

```text
SQLite
    PASS

first PostgreSQL 18 attempt
    FAIL
```

The first PostgreSQL defect was a too-long manually named migration constraint, not a conceptual persistence failure.

Fix:

```text
ba6a92f83aac3a63ebfb7f97a4378c93fa28547b
Shorten interchange migration identifiers for PostgreSQL
```

Traceability improvement:

```text
a69b8859696fbd3b45124c257d085989d692a207
Make roundtrip gate status traceable to source commit
```

Do not call the governed round-trip closed until a corrected PostgreSQL PASS is persisted and confirmed.

---

## 2026 agentic ecosystem and runtime boundary

Primary research:

```text
docs/research/001_2026_agentic_ecosystem_and_integration_architecture_audit.md
```

Architecture conclusion:

```text
ADS domain/project/methodological semantics
    owned by ADS

agent runtimes / MCP / A2A / AG-UI / runtime checkpoints
    replaceable infrastructure/interoperability
```

Promoted principles:

```text
docs/PRINCIPLES.md, P-027 through P-029
```

Important directions:

```text
MCP
    strong candidate external tool/resource integration boundary
    not internal project memory/application bus

A2A
    defer until independently deployed remote agents are required

AG-UI
    evaluate as frontend-agent transport adapter
    do not make it ADS domain event model

multi-agent
    do not adopt by default
    start with one principal reasoner + tools
```

Historical checkpoint:

```text
docs/checkpoints/116_agentic_ecosystem_audit_and_frontend_track_started.md
```

---

## Agent-runtime bakeoff

Candidate evaluation contract:

```text
docs/specifications/005_v1_agent_runtime_and_interoperability_bakeoff.md
```

First-round candidates:

```text
OpenAI Agents SDK
LangGraph
Microsoft Agent Framework
Google ADK 2.0
```

Pydantic AI/Pydantic Graph remains a watchlist candidate.

The bakeoff tests ADS-shaped requirements:

```text
domain isolation
single-agent tools
MCP
human approval
durable resume
external ADS project-state authority
bounded context transparency
cancellation/timeouts
failure/retry
structured outputs
observability
test/provider substitution
```

A valid result is still to use simpler direct model calls if no framework earns its complexity.

---

## Professional frontend and project-view shell

Primary foundation:

```text
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
```

Candidate implementation/visual gate:

```text
docs/specifications/006_v1_frontend_architecture_and_visual_spike.md
```

Current leading stack hypothesis, not yet a final product-stack acceptance:

```text
React
TypeScript
Vite
TanStack Router
TanStack Query
TanStack Table v9
ADS-owned design system
Playwright
Vitest
```

Current project-view shell implements:

```text
Overview
Data
EDA
Decisions & History
methodological guidance
run/activity state
approval interaction
light/dark mode
loading/error states
cross-platform build/tests
Chromium accessibility/interaction tests
controlled project-view visual regression
```

Human review identified and corrected a Data-layout defect where the right methodological panel could overlap the Data workspace. The context panel is now a reserved, collapsible layout column with browser coverage.

Chart strategy remains under evaluation:

```text
ECharts
vs
Plotly
```

Tauri remains a later packaging candidate.

---

## Primary Project Cockpit design

This is now a major active product-design area.

### Initial concept research

```text
docs/research/002_primary_project_cockpit_interface_concept.md
```

Research 002 establishes the missing product layer:

```text
Project Cockpit
    primary active-work environment

normal project views
    direct inspection / navigation / records
```

Core concept:

```text
living project-process map
+ native conversation/system interaction
+ focused analytical work surface
```

Visible Cockpit work units should represent meaningful project work, not agents and not every persisted project object.

### Unified deep-work refinement

```text
docs/research/003_unified_cockpit_workspace_and_spatial_focus_architecture.md
docs/checkpoints/117_unified_cockpit_workspace_direction_confirmed.md
```

Strongly confirmed human interaction requirement:

```text
click a work block
    -> smooth zoom/focus experience
    -> perform real analytical work
    -> return smoothly to project context
```

Deep Data, EDA, Validation, Features, Modeling, Evaluation, and other work should be possible inside this experience where technically appropriate.

Direct specialist routes remain as alternate entrances into the same functionality.

Critical engineering boundary:

```text
everything reachable from the Cockpit
    !=
everything mounted or loaded simultaneously
```

A professional implementation may use:

```text
selective component mounting
route/search state
code splitting
backend pagination/streaming
virtualized large views
browser View Transition API or another motion layer
```

while still presenting one continuous workspace to the user.

---

## First executable Project Cockpit spike

Candidate contract:

```text
docs/specifications/007_v1_unified_project_cockpit_interaction_spike.md
```

Implementation evidence:

```text
docs/checkpoints/118_first_unified_cockpit_interaction_spike_automated_gate_passed.md
```

Current implemented interaction:

```text
/cockpit immersive route
minimal global Cockpit chrome
stage-zone living project map
meaningful dynamic work blocks
explicit complete/blocked/attention/selected/deferred states
persistent bottom system composer
spatial focus handoff
shared DataPage inside focus host
shared EdaPage inside focus host
dedicated Production Missingness focus surface
focus/column/filter/view search state
browser Back restoration
reduced-motion fallback
```

No graph/canvas library is selected yet.

The first spike intentionally uses React/CSS/SVG/browser primitives to evaluate the interaction before React Flow or another canvas framework is allowed to shape the product.

Automated gate on GitHub Actions run 70:

```text
Ubuntu build + unit tests
    PASS

Windows build + unit tests
    PASS

Chromium interaction + accessibility
    PASS

existing project-view visual regression
    PASS
```

The Cockpit has no canonical visual-regression baseline yet because human visual/product review is intentionally required first.

Immediate frontend action:

```text
human opens /cockpit
reviews project map
focuses Data
focuses Production Missingness
hands off to full Data focus
focuses EDA
returns / uses browser Back
reviews composer and overall product feel
```

Do not promote Specification 007 or select a graph library before this review.

---

## Retrieval and MethodologicalHorizon track

Still required:

```text
retrieval-quality fixtures
production lexical retrieval
semantic retrieval candidate evaluation
lexical/semantic fusion if justified
first real MethodologicalHorizon construction
selective LLM context assembly
```

Do not choose an embedding model, reranker, ANN service, or vector database from intuition.

The representative knowledge corpus should become a retrieval benchmark only after the governed persistence/interchange seam is stable enough that fixture changes are not competing with migration debugging.

---

## Epistemic integrity, admissibility, and risk

Primary sources:

```text
docs/foundations/002_epistemic_integrity_and_project_constitution.md
docs/foundations/003_admissibility_risk_and_assurance.md
docs/VISION.md
docs/PRINCIPLES.md
```

---

## Project state and orchestration history

Broad theory:

```text
docs/foundations/004_project_state_dependency_and_state_driven_orchestration.md
```

Interpretation after V0:

```text
broad dependency/state theory remains useful
    !=
P0's always-on representation is justified
```

---

## Earlier reusable-knowledge theory

Read for deeper design history:

```text
docs/foundations/006_knowledge_activation_and_open_world_reasoning.md
docs/foundations/007_reusable_knowledge_representation_and_composable_components.md
docs/foundations/008_knowledge_quality_generalization_and_evolution.md
```

Foundations 019 and 020 govern the current post-V0 interpretation.

---

## Current active priorities

Exact status and sequencing are maintained in:

```text
docs/CURRENT_STATE.md
```

At Checkpoint 118 the immediate high-value action is the human Cockpit review.

Other active bounded tracks remain:

```text
governed PostgreSQL round-trip closure
agent-runtime bakeoff
retrieval-quality benchmark preparation
frontend refinement after Cockpit review
```

---

## Current major non-selections

Do not infer acceptance of any of these merely because they have been discussed:

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
Cockpit final visual identity
Cockpit stage taxonomy
Cockpit auto-layout algorithm
Cockpit final URL contract
system/persona name
Tauri desktop packaging
backend HTTP/API framework
production FTS implementation
embedding model/provider
lexical/semantic fusion
reranker
complete project persistence schema
artifact storage backend
job queue/cloud deployment
```
