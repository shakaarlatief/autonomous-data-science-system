# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources but does not replace them.  
**Last reviewed:** 2026-08-20  
**Current checkpoint:** 120  
**Active development branch:** `v1-frontend-spike`

## Start here

For a new session or quick reconstruction:

```text
README.md
    project-level overview and current branch/stage

docs/CURRENT_STATE.md
    present state, active gates, and exact next step

docs/KNOWLEDGE_MAP.md
    routing layer

docs/VISION.md
    system purpose and long-term vision

docs/PRINCIPLES.md
    current high-level design principles

docs/DECISIONS.md
    accepted project-level decisions

docs/OPEN_QUESTIONS.md
    reconciled current unresolved questions

docs/DEVELOPMENT_METHOD.md
    development/preservation method

docs/CONTINUITY.md
    cross-session continuation and unplanned-boundary recovery

docs/MAJOR_CHANGES.md
    selective structural history
```

Current branch warning:

```text
active frontend/Cockpit work = v1-frontend-spike
main intentionally trails this work
```

A continuation session must not infer the latest project state from `main` alone while this branch relationship remains active.

---

## Current project stage

Prototype V0 is complete and its final classification is:

> **STRONG FALSIFICATION OF THE CURRENT P0 DESIGN**

The project is now implementing bounded V1 slices across:

```text
methodological knowledge
governed persistence/interchange
retrieval / MethodologicalHorizon construction
agent/runtime infrastructure
professional frontend
unified Project Cockpit
```

The immediate substantive product priority is the Specification 007 candidate v0.2 immersive-scale Cockpit slice established by Checkpoint 119.

Checkpoint 120 is the current continuity/reconciliation boundary after Session 02 ended unexpectedly at the platform conversation-length limit.

---

## System purpose and LLM/system/human boundary

Primary sources:

```text
docs/VISION.md
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
```

Current durable interpretation:

```text
LLM
    flexible reasoning component

ADS
    persistent project/process intelligence
    methodological knowledge
    provenance
    deterministic controls where justified
    execution coordination
    professional reasoning/control surface

Human
    goals
    semantics
    consequential judgment
    approvals / intervention where useful
```

Every explicit mechanism must earn its complexity empirically.

---

## Prototype V0 evidence and architectural constraint

Authoritative final evidence:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
prototype_v0/README.md
```

Final result:

```text
B1 targeted mean: 1.73
P0 targeted mean: 1.78
P0 incremental gain: +0.05
P0/B1 median token ratio: 2.160
B1 completion: 10/10
P0 completion: 3/10
```

Core scaling lesson:

```text
what the SYSTEM should remember
    !=
what the LLM should receive on every reasoning call
```

Do not reintroduce unchanged:

```text
full structured state/context every reasoning cycle
large always-on frontier/context
path-sensitive tag-trigger activation
generic recursive support reassessment
universal dependency reopening machinery
```

System-level interpretation:

```text
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
```

Historical final V0 checkpoint:

```text
docs/checkpoints/096_prototype_v0_final_strong_falsification_and_architecture_diagnostic_conclusion.md
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

Core conceptual structures:

```text
OBJECTS
RELATIONS
EVENTS
VIEWS
```

The current design does not add a universal project `Assessment` object.

Subject-specific verdicts use:

```text
Question -> Evidence -> Finding -> Claim / Decision
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

## Methodological-navigation brain and MethodologicalHorizon

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
    -> bounded MethodologicalHorizon
    -> explicit applicability/context checks
    -> flexible relevance/prioritization reasoning
    -> selective task-specific LLM context
```

Active unresolved implementation routing:

```text
docs/OPEN_QUESTIONS.md, Q-044 and Q-045
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
exact stable/revision identity
project-object references/influence
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
internal representation != human-facing workflow/tree
```

Promoted principles:

```text
docs/PRINCIPLES.md, P-025 and P-026
```

Important stress-test history:

```text
docs/checkpoints/101_five_example_reusable_knowledge_stress_test_completed.md
docs/checkpoints/102_candidate_conceptual_knowledge_representation_contract.md
docs/checkpoints/104_adversarial_review_of_candidate_knowledge_representation.md
docs/checkpoints/105_refined_representation_second_stress_test.md
```

---

## Accepted V1 persistence/retrieval architecture

Primary sources:

```text
docs/DECISIONS.md, D-028
docs/specifications/001_v1_sqlite_technical_architecture.md
docs/checkpoints/108_v1_architecture_comparison_and_sqlite_centered_selection.md
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
    initial exact in-process semantic retrieval

application rule evaluator
    TRUE / FALSE / UNKNOWN conditional semantics

selective context assembler

filesystem / Git / artifact storage
    code and large artifacts outside SQLite
```

PostgreSQL + pgvector remains the preferred first migration family if later concurrency/shared-server/vector-scale requirements exceed the SQLite envelope.

Architecture gate evidence:

```text
experiments/architecture_spikes/V1_ARCHITECTURE_GATE_RESULT.md
```

The retrieval seam gate is not evidence of production retrieval quality or embedding choice.

---

## Accepted implementation and Python tooling

Persistence tooling:

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

Python project tooling:

```text
docs/DECISIONS.md, D-030
docs/specifications/003_v1_python_project_and_dependency_tooling.md
```

Accepted:

```text
pyproject.toml
uv + committed uv.lock
uv_build
src/ads_system
Python >=3.12
```

---

## First production persistence vertical slice

Primary milestone:

```text
docs/checkpoints/114_first_production_v1_persistence_vertical_slice_passed.md
experiments/architecture_spikes/V1_PRODUCTION_PERSISTENCE_SLICE_RESULT.md
```

The same bounded application/repository scenario passed on:

```text
SQLite / Linux
SQLite / Windows
PostgreSQL 18
```

It proves that a project Finding pinned to Random Forest R1 remains pinned to R1 after R2 becomes current.

This result is distinct from the later richer governed import/accept/export round-trip.

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

Authority rule:

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

The production bridge includes:

```text
candidate import
explicit acceptance
accepted snapshot export
provenance
relation governance
collections
migration 0002
historical project revision pinning
```

Last persisted gate status:

```text
SQLite
    PASS

PostgreSQL 18
    FAIL
```

Status source:

```text
experiments/architecture_spikes/V1_KNOWLEDGE_ROUNDTRIP_STATUS.md
```

The first PostgreSQL defect was an overlong manually named migration constraint. The identifier was shortened and revalidation was triggered, but the round-trip must not be called closed until a corrected PostgreSQL PASS is persisted and temporary diagnostics are removed.

Active open question:

```text
docs/OPEN_QUESTIONS.md, Q-048
```

---

## Agentic ecosystem and runtime boundary

Primary research:

```text
docs/research/001_2026_agentic_ecosystem_and_integration_architecture_audit.md
```

Durable conclusion:

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

Current protocol directions:

```text
MCP
    first-class external tool/resource integration candidate
    not project memory or internal application bus

AG-UI
    evaluate as transport adapter around ADS-owned interaction/run events
    not domain event model

A2A
    defer until independently deployed remote agents are genuinely required
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

Pydantic AI / Pydantic Graph remains a watchlist candidate.

The bakeoff tests ADS-shaped requirements:

```text
domain isolation
single-agent tool loop
MCP
human approval
durable resume
external ADS project-state authority
bounded context transparency
cancellation/timeouts
failure/retry semantics
structured outputs
observability
test/provider substitution
```

A valid result remains using simpler direct model calls if no framework earns its complexity.

Active open question:

```text
docs/OPEN_QUESTIONS.md, Q-046 and Q-047
```

---

## Professional frontend foundation

Primary foundation:

```text
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
```

Candidate technical/visual evaluation contract:

```text
docs/specifications/006_v1_frontend_architecture_and_visual_spike.md
```

Current leading stack hypothesis, not final accepted architecture:

```text
React
TypeScript
Vite
TanStack Router
TanStack Query
TanStack Table
ADS-owned design system
Playwright
Vitest
```

The project-view shell already includes:

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

Chart strategy remains under evaluation:

```text
ECharts
vs
Plotly
```

Tauri remains a later packaging candidate.

---

## Primary Project Cockpit design

### Initial concept

```text
docs/research/002_primary_project_cockpit_interface_concept.md
```

Research 002 establishes:

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

Visible Cockpit work units represent meaningful project work, not agents and not every persisted object.

### Unified deep-work refinement

```text
docs/research/003_unified_cockpit_workspace_and_spatial_focus_architecture.md
docs/checkpoints/117_unified_cockpit_workspace_direction_confirmed.md
```

Strongly confirmed interaction:

```text
click meaningful work block
    -> smooth spatial focus
    -> perform real analytical work
    -> return to project context
```

Deep Data, EDA, Validation, Features, Modeling, Evaluation, and other work should be reachable in the same experience where technically appropriate.

Direct specialist routes remain alternative entrances to the same substantive modules.

Critical engineering boundary:

```text
everything reachable from the Cockpit
    !=
everything mounted or loaded simultaneously
```

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

Implemented:

```text
/cockpit immersive route
stage-zone living project map
meaningful dynamic work blocks
explicit project-state styling
persistent system composer
spatial focus handoff
shared Data and EDA workspaces
Production Missingness focus surface
focus/column/filter/view route state
browser Back restoration
reduced-motion fallback
```

Automated gate:

```text
Ubuntu build + unit tests
    PASS
Windows build + unit tests
    PASS
Chromium interaction + accessibility
    PASS
existing direct project-view visual regression
    PASS
```

No graph/canvas library was selected.

---

## Second Cockpit human review and immersive-scale requirements

Current design evidence:

```text
docs/research/004_cockpit_spatial_scalability_immersive_chrome_and_fullscreen.md
docs/checkpoints/119_cockpit_spatial_scalability_and_true_fullscreen_requirements_confirmed.md
```

The second real-browser review accepted the stage-zone visual grammar:

```text
technical dark operating canvas
Framing
Data & Exploration
Validation
Modeling
Evaluation
semantic work blocks
meaningful connectors
clear project-state distinctions
```

It also established new requirements:

```text
2D project-space navigation
horizontal + vertical growth
later/right/lower work always reachable
future semantic zoom/grouping
compact/expandable Cockpit HUD
stage orientation at top of operating viewport
true browser fullscreen
collision-safe floating surfaces
fit/reset/jump navigation
keyboard-accessible recovery
```

Specification 007 is now **candidate v0.2** and governs the next bounded frontend implementation slice.

No final canvas library, auto-layout, semantic-zoom implementation, minimap, stage taxonomy, URL contract, or visual identity is accepted yet.

Active open questions:

```text
docs/OPEN_QUESTIONS.md, Q-049 through Q-052
```

---

## Continuity boundary after unexpected Session 02 termination

Primary source:

```text
docs/checkpoints/120_unplanned_session_boundary_reconciliation_and_v1_continuity_restored.md
```

Session 02 reached the platform conversation-length limit immediately after Checkpoint 119 preservation.

Substantive Cockpit knowledge survived in Research 004, Specification 007 v0.2, and Checkpoint 119, but the normal end-of-session reconciliation did not finish.

Session 03 repaired:

```text
README
CURRENT_STATE
KNOWLEDGE_MAP
OPEN_QUESTIONS
CONTINUITY
checkpoint-session provenance
MAJOR_CHANGES
frontend local generated/dependency ignore hygiene
```

Current active session:

```text
Design session: 03
Session title: 03 - Project Cockpit & V1 Integration
```

Unplanned-boundary recovery procedure:

```text
docs/CONTINUITY.md
```

---

## Retrieval and MethodologicalHorizon track

Still required:

```text
retrieval-quality fixtures
production lexical retrieval
semantic retrieval candidate evaluation
lexical/semantic fusion if justified
ranking/omission-quality evaluation
first real MethodologicalHorizon construction
selective LLM context assembly
```

Do not choose an embedding model, reranker, ANN service, or vector database from intuition.

The representative knowledge corpus should become a retrieval benchmark only when the governed persistence/interchange seam is stable enough that fixture changes are not competing with migration debugging.

---

## Epistemic integrity, admissibility, and risk

Primary sources:

```text
docs/foundations/002_epistemic_integrity_and_project_constitution.md
docs/foundations/003_admissibility_risk_and_assurance.md
docs/VISION.md
docs/PRINCIPLES.md
```

These remain durable conceptual sources. Their complete production operationalization remains open.

---

## Current major non-selections

Do not infer acceptance of any of these merely because they have been discussed or used experimentally:

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
Cockpit auto-layout algorithm
Cockpit semantic-zoom algorithm
Cockpit final stage taxonomy
Cockpit final URL contract
Cockpit final visual identity
system/persona name
Tauri desktop packaging
backend HTTP/API framework
production FTS implementation
embedding model/provider
lexical/semantic fusion
reranker
complete project persistence schema
artifact-storage backend
job queue/cloud deployment
```

---

## Exact current priorities

### 1. Project Cockpit immersive-scale slice

Governed by:

```text
docs/research/004_cockpit_spatial_scalability_immersive_chrome_and_fullscreen.md
docs/specifications/007_v1_unified_project_cockpit_interaction_spike.md
docs/checkpoints/119_cockpit_spatial_scalability_and_true_fullscreen_requirements_confirmed.md
```

Implement:

```text
unreachable-content fix
2D viewport navigation
larger-than-one-screen project extent
compact/expandable HUD
top-aligned stage orientation
true browser fullscreen
collision-safe floating surfaces
fit/reset/jump navigation
keyboard-accessible recovery
```

Then rerun automated gates and return to human product review before freezing the design.

### 2. Governed round-trip closure

Confirm a corrected PostgreSQL 18 PASS, fix any remaining real portability defect, remove temporary diagnostics, and checkpoint closure only when evidence is persisted.

### 3. Agent-runtime bakeoff

Execute Specification 005 with one principal reasoner first.

### 4. Retrieval / MethodologicalHorizon benchmark

Evaluate production retrieval and selective context once the governed knowledge seam is stable enough.

---

## Minimum current continuation set

```text
README.md
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/OPEN_QUESTIONS.md
docs/DECISIONS.md
docs/PRINCIPLES.md
docs/CONTINUITY.md

docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md

docs/research/001_2026_agentic_ecosystem_and_integration_architecture_audit.md
docs/research/002_primary_project_cockpit_interface_concept.md
docs/research/003_unified_cockpit_workspace_and_spatial_focus_architecture.md
docs/research/004_cockpit_spatial_scalability_immersive_chrome_and_fullscreen.md

docs/specifications/004_v1_reusable_knowledge_interchange.md
docs/specifications/005_v1_agent_runtime_and_interoperability_bakeoff.md
docs/specifications/006_v1_frontend_architecture_and_visual_spike.md
docs/specifications/007_v1_unified_project_cockpit_interaction_spike.md

docs/checkpoints/114_first_production_v1_persistence_vertical_slice_passed.md
docs/checkpoints/115_reusable_knowledge_interchange_contract_validated.md
docs/checkpoints/119_cockpit_spatial_scalability_and_true_fullscreen_requirements_confirmed.md
docs/checkpoints/120_unplanned_session_boundary_reconciliation_and_v1_continuity_restored.md
```
