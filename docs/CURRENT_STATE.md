# Current State

**Checkpoint:** 126  
**Date:** 2026-08-21  
**Active development branch:** `v1-frontend-spike`  
**Development stage:** Prototype V0 complete; bounded V1 implementation and integration across methodological knowledge, governed persistence/interchange, retrieval/MethodologicalHorizon construction, agent/runtime evaluation, and the professional Project Cockpit  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate project priority:** Close the governed PostgreSQL 18 reusable-knowledge round-trip gate. The Project Cockpit interaction architecture has now been promoted and is no longer the immediate blocking V1 track.

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

## 4. Governed knowledge round-trip remains open

A richer governed knowledge path is implemented, including:

```text
candidate import
explicit acceptance
accepted-current pointers
accepted snapshot export
provenance
relation governance
collections
migration 0002
historical project revision pinning
```

Last persisted gate state remains:

```text
SQLite round-trip
    PASS

PostgreSQL 18 round-trip
    FAIL
```

The first PostgreSQL defect was localized to a manually named migration constraint longer than PostgreSQL's 63-character identifier limit. The identifier was shortened and revalidation was triggered, but the repository still does not contain a persisted corrected PostgreSQL PASS.

Do not call this gate closed until:

```text
corrected PostgreSQL 18 round-trip PASS is persisted
remaining portability defects, if any, are fixed honestly
temporary diagnostic artifacts/workflow are removed
closure is recorded in a dedicated checkpoint
```

This gate is separate from Checkpoint 114's narrower persistence slice, which already passed PostgreSQL.

This is now the immediate project priority.

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

The Cockpit remains a derived projection over project state. It must not collapse the project process map, data/artifact lineage, methodological knowledge graph, event history, and runtime actors into one unreadable graph.

The engineering boundary remains:

```text
everything reachable from the Cockpit
    !=
everything mounted or loaded simultaneously
```

### Promoted interaction architecture

```text
meaningful work units
    objective/framing
    data understanding
    exploration/investigation
    questions/blockers
    validation
    modeling
    evaluation

spatial focus
    meaningful work unit
        -> real specialist workspace
        -> return to project context

FiniteNavigableGridWorld != SemanticProjectPlane

FiniteNavigableGridWorld
    continuous grid through navigation reserve
    symmetric pan/recovery capacity
    world-owned restrained ambient depth
    subtle finite-boundary cue

SemanticProjectPlane
    stage semantics
    work units
    connectors
    neutral reserve remains non-semantic

2D navigation
    horizontal + vertical movement
    keyboard recovery
    fit/reset
    Jump/search

bounded geometric zoom
    explicit +/-
    zoom indication
    100% reset
    fit project
    keyboard equivalents
    native laptop pinch capability

ViewportStageRuler
    vertically near the visible viewport top
    horizontally follows rendered semantic stage geometry
    terminal alignment sourced from authoritative rendered stage boundaries

scalable project location
    semantic quick destinations
    searchable meaningful project work

immersive chrome
    compact fold-away primary HUD
    fold-away project-map controls
    floating Details
    floating System Focus
    floating native composer
    collision-safe overlays

true browser fullscreen
    explicit action
    fullscreenchange synchronization
    Escape/explicit exit
    graceful unsupported/denied fallback

URL-addressable focus/deep-work state
keyboard accessibility
reduced-motion support
```

### Evidence through Checkpoint 126

The Cockpit progressed through seven real-browser human review cycles.

```text
117  core click-to-focus direction confirmed
118  first executable /cockpit gate passed
119  scale/reachability/fullscreen requirements exposed
121  immersive-scale 2D viewport gate passed
122  geometric zoom, scalable Jump/search, canvas-dominant chrome validated
123  balanced ProjectWorld/ProjectCanvas geometry and stronger orientation validated
124  continuous grid world, viewport-aware stage ruler, vertical tool rail validated
125  world ambient, pinch stability, ruler authority, Jump/composer collision repair passed
126  real laptop pinch/hardware gate accepted strongly enough for promotion;
     pinch responsiveness increased;
     latent ruler-timing defect found and repaired;
     final cross-platform/browser gate passed;
     Specification 008 promoted
```

Final promotion implementation head:

```text
2c3b522e2416d73c015ce5ec2a4560a227524dd9
```

Final validation:

```text
V1 frontend spike
run number 155
run id 32492536072

Ubuntu build + unit tests
    PASS

Windows build + unit tests
    PASS

Chromium browser interaction + accessibility
    PASS

controlled direct-project visual regression
    PASS
```

The first seventh-review gate remains useful diagnostic evidence. Ubuntu/Windows passed, while Chromium repeatedly exposed stage-ruler misalignment under rapid minimum-zoom transition. The defect was traced to ruler measurement occurring before the zoomed rendered geometry had fully settled and was repaired by synchronizing after an additional animation frame.

### Known deferred Cockpit polish

The user still observes a very small occasional hitch during native pinch zoom.

Current classification:

```text
known
real
non-blocking
deferred polish
```

It should be revisited when future Cockpit/input-device work makes that efficient. It is not a reason to keep the interaction architecture unpromoted.

---

## 7. Current major non-selections

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
pointer-proximity HUD/control reveal
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

Specification 008 promotes interaction architecture, not these final implementation or visual choices.

---

## 8. Exact next execution order

### A. GOVERNED POSTGRESQL ROUND-TRIP CLOSURE

This is now the immediate substantive V1 step.

```text
confirm corrected PostgreSQL 18 governed round-trip gate
fix remaining portability defects honestly if present
persist a corrected PASS
remove temporary diagnostic machinery
record closure only after evidence exists
```

Do not infer a pass from Checkpoint 114 or from the earlier localized defect fix.

### B. AGENT RUNTIME BAKEOFF

Execute Specification 005 with one principal reasoner first.

Direct model calls remain a valid result if no framework earns its complexity.

### C. RETRIEVAL / METHODOLOGICALHORIZON BENCHMARK

Build the first production retrieval/horizon evaluation:

```text
retrieval-quality fixtures
production lexical retrieval
semantic retrieval candidate evaluation
lexical/semantic fusion only if justified
ranking / omission-quality evaluation
first real bounded MethodologicalHorizon
selective LLM context assembly
```

Do not choose an embedding model, reranker, ANN service, or vector database from intuition.

### D. FUTURE COCKPIT PRODUCT WORK

Future Cockpit work should build on Specification 008 rather than reopening the basic interaction architecture without new evidence.

Relevant future work includes deeper specialist workspaces, production system conversation, real project-state integration, semantic scale/grouping, project auto-layout, broader project-size tests, and visual/product polish including the deferred tiny pinch hitch.

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
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md

docs/research/001_2026_agentic_ecosystem_and_integration_architecture_audit.md
docs/research/002_primary_project_cockpit_interface_concept.md
docs/research/003_unified_cockpit_workspace_and_spatial_focus_architecture.md
docs/research/004_cockpit_spatial_scalability_immersive_chrome_and_fullscreen.md
docs/research/005_cockpit_canvas_dominance_zoom_and_scalable_project_navigation.md
docs/research/006_fourth_cockpit_human_review_balanced_spatial_world_and_visual_orientation.md
docs/research/007_fifth_cockpit_human_review_continuous_grid_world_stage_ruler_and_vertical_tool_rail.md
docs/research/008_sixth_cockpit_human_review_world_ambient_continuity_pinch_stability_and_collision_safety.md
docs/research/009_seventh_cockpit_human_review_pinch_responsiveness_and_interaction_promotion.md

docs/specifications/004_v1_reusable_knowledge_interchange.md
docs/specifications/005_v1_agent_runtime_and_interoperability_bakeoff.md
docs/specifications/006_v1_frontend_architecture_and_visual_spike.md
docs/specifications/007_v1_unified_project_cockpit_interaction_spike.md
docs/specifications/008_v1_project_cockpit_interaction_architecture.md

docs/checkpoints/114_first_production_v1_persistence_vertical_slice_passed.md
docs/checkpoints/115_reusable_knowledge_interchange_contract_validated.md
docs/checkpoints/120_unplanned_session_boundary_reconciliation_and_v1_continuity_restored.md
docs/checkpoints/121_immersive_scale_cockpit_slice_automated_gate_passed.md
docs/checkpoints/122_third_cockpit_review_zoom_canvas_dominance_and_scalable_navigation_gate_passed.md
docs/checkpoints/123_fourth_cockpit_review_balanced_spatial_world_and_orientation_validated.md
docs/checkpoints/124_continuous_grid_world_stage_ruler_and_vertical_tool_rail_gate_passed.md
docs/checkpoints/125_sixth_cockpit_review_ambient_pinch_ruler_and_collision_repairs_validated.md
docs/checkpoints/126_seventh_cockpit_review_validated_and_interaction_architecture_promoted.md
```
