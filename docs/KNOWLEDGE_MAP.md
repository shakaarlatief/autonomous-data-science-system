# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources but does not replace them.  
**Last reviewed:** 2026-08-21  
**Current checkpoint:** 126  
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
    current system purpose and product direction

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
active bounded V1/frontend work = v1-frontend-spike
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
Project Cockpit
```

The Project Cockpit interaction architecture is now promoted through Specification 008 after seven real-browser human review cycles and a final passing cross-platform/browser gate.

The immediate project priority is the **governed PostgreSQL 18 reusable-knowledge round-trip closure**.

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

Authoritative evidence:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
prototype_v0/README.md
docs/checkpoints/096_prototype_v0_final_strong_falsification_and_architecture_diagnostic_conclusion.md
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

Core structures:

```text
OBJECTS
RELATIONS
EVENTS
VIEWS
```

No universal project `Assessment` object is currently justified.

Subject-specific verdicts use:

```text
Question -> Evidence -> Finding -> Claim / Decision
```

with structured criterion Findings where useful.

Professional-workflow responsibility split:

```text
ADS
    project/process control plane

VS Code
    developer workbench

Python / Docker / local or remote compute
    execution plane

Git + GitHub
    source versioning, collaboration, provenance
```

---

## Methodological-navigation brain and reusable knowledge

Primary sources:

```text
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
```

Relevance progression:

```text
KNOWN
    -> APPLICABLE
    -> RELEVANT
    -> RECOMMENDED
    -> REQUIRED / BLOCKING
```

Scaling concept:

```text
large global knowledge universe
    -> project-specific retrieval/filtering
    -> bounded MethodologicalHorizon
    -> explicit applicability/context checks
    -> flexible relevance/prioritization reasoning
    -> selective task-specific LLM context
```

Reusable representation:

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

Key stress-test/promotion sources:

```text
docs/checkpoints/101_five_example_reusable_knowledge_stress_test_completed.md
docs/checkpoints/102_candidate_conceptual_knowledge_representation_contract.md
docs/checkpoints/104_adversarial_review_of_candidate_knowledge_representation.md
docs/checkpoints/105_refined_representation_second_stress_test.md
docs/checkpoints/106_foundation_020_promoted_and_implementation_requirements_next.md
```

---

## Accepted V1 persistence, tooling, and interchange

Primary decisions/specifications:

```text
D-028 + docs/specifications/001_v1_sqlite_technical_architecture.md
D-029 + docs/specifications/002_v1_persistence_tooling_standard.md
D-030 + docs/specifications/003_v1_python_project_and_dependency_tooling.md
D-031 + docs/specifications/004_v1_reusable_knowledge_interchange.md
```

Accepted direction:

```text
SQLite-centered local-first operational architecture
FTS5 rebuildable lexical index
rebuildable embeddings / initial exact semantic retrieval
application rule evaluator
selective context assembler
filesystem / Git / artifact storage outside SQLite

SQLAlchemy Core 2.0
Alembic 1.x

pyproject.toml
uv + committed uv.lock
uv_build
src/ads_system
Python >=3.12

JSON
JSON Schema Draft 2020-12
application semantic validation
deterministic interchange normalization/serialization
```

Key milestones:

```text
docs/checkpoints/114_first_production_v1_persistence_vertical_slice_passed.md
docs/checkpoints/115_reusable_knowledge_interchange_contract_validated.md
```

Checkpoint 114's bounded persistence slice passed SQLite/Linux, SQLite/Windows, and PostgreSQL 18 and proves exact historical project-to-knowledge revision pinning.

Checkpoint 115 validates the reusable knowledge interchange contract but is not evidence that the later richer governed import/accept/export round-trip passed PostgreSQL.

---

## Governed knowledge round-trip status

Status source:

```text
experiments/architecture_spikes/V1_KNOWLEDGE_ROUNDTRIP_STATUS.md
```

Last persisted state:

```text
SQLite
    PASS

PostgreSQL 18
    FAIL
```

The known first PostgreSQL defect was an overlong manually named migration constraint. The identifier was shortened and revalidation was triggered, but the gate must not be called closed until a corrected PostgreSQL PASS is persisted and temporary diagnostics are removed.

Active open question:

```text
docs/OPEN_QUESTIONS.md, Q-048
```

This is now the immediate execution track.

---

## Agentic ecosystem and runtime boundary

Primary research/specification:

```text
docs/research/001_2026_agentic_ecosystem_and_integration_architecture_audit.md
docs/specifications/005_v1_agent_runtime_and_interoperability_bakeoff.md
```

Durable boundary:

```text
ADS domain/project/methodological semantics
    owned by ADS

agent runtimes / MCP / A2A / AG-UI / runtime checkpoints
    replaceable infrastructure/interoperability
```

First-round runtime candidates:

```text
OpenAI Agents SDK
LangGraph
Microsoft Agent Framework
Google ADK 2.0
```

A valid bakeoff outcome remains simpler direct model calls if no framework earns its complexity.

---

## Professional frontend foundation

Primary foundation/specification:

```text
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
docs/specifications/006_v1_frontend_architecture_and_visual_spike.md
```

Leading stack hypothesis, not final accepted architecture:

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

Chart strategy remains under evaluation:

```text
ECharts
vs
Plotly
```

Tauri remains a later packaging candidate.

---

## Project Cockpit: promoted interaction architecture

### Historical concept and spike evolution

Primary research/history:

```text
docs/research/002_primary_project_cockpit_interface_concept.md
docs/research/003_unified_cockpit_workspace_and_spatial_focus_architecture.md
docs/research/004_cockpit_spatial_scalability_immersive_chrome_and_fullscreen.md
docs/research/005_cockpit_canvas_dominance_zoom_and_scalable_project_navigation.md
docs/research/006_fourth_cockpit_human_review_balanced_spatial_world_and_visual_orientation.md
docs/research/007_fifth_cockpit_human_review_continuous_grid_world_stage_ruler_and_vertical_tool_rail.md
docs/research/008_sixth_cockpit_human_review_world_ambient_continuity_pinch_stability_and_collision_safety.md
docs/research/009_seventh_cockpit_human_review_pinch_responsiveness_and_interaction_promotion.md

docs/specifications/007_v1_unified_project_cockpit_interaction_spike.md

docs/checkpoints/117_unified_cockpit_workspace_direction_confirmed.md
docs/checkpoints/118_first_unified_cockpit_interaction_spike_automated_gate_passed.md
docs/checkpoints/119_cockpit_spatial_scalability_and_true_fullscreen_requirements_confirmed.md
docs/checkpoints/121_immersive_scale_cockpit_slice_automated_gate_passed.md
docs/checkpoints/122_third_cockpit_review_zoom_canvas_dominance_and_scalable_navigation_gate_passed.md
docs/checkpoints/123_fourth_cockpit_review_balanced_spatial_world_and_orientation_validated.md
docs/checkpoints/124_continuous_grid_world_stage_ruler_and_vertical_tool_rail_gate_passed.md
docs/checkpoints/125_sixth_cockpit_review_ambient_pinch_ruler_and_collision_repairs_validated.md
docs/checkpoints/126_seventh_cockpit_review_validated_and_interaction_architecture_promoted.md
```

### Current authoritative Cockpit interaction contract

```text
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
```

Promoted model:

```text
Project Cockpit
    primary immersive active-work environment
    living project-process projection
    native system interaction
    focused analytical work

Direct specialist views
    alternative entry / inspection / records
    reuse the same modules/state
```

Promoted interaction principles:

```text
meaningful work units rather than every persisted object
spatial focus into real specialist workspaces
reachability != simultaneous mounting
FiniteNavigableGridWorld != SemanticProjectPlane
2D navigation and recovery
bounded geometric zoom
native laptop pinch capability
viewport-aware stage orientation
scalable Jump/search project location
compact/fold-away immersive chrome
collision-safe floating surfaces
true fullscreen with graceful fallback
URL-addressable focus/deep-work state
keyboard accessibility and reduced-motion support
world-owned restrained ambient depth
```

Final promotion implementation head:

```text
2c3b522e2416d73c015ce5ec2a4560a227524dd9
```

Final validation:

```text
V1 frontend spike
run 155 / 32492536072

Ubuntu build + unit tests                 PASS
Windows build + unit tests                PASS
Chromium interaction/accessibility        PASS
controlled direct-view visual regression  PASS
```

The seventh human review explicitly accepted Jump/search and stage orientation, judged pinch smoothness substantially improved, classified the remaining tiny occasional pinch hitch as non-blocking polish, and requested only moderately faster pinch travel before proceeding.

Pinch sensitivity was increased from `0.00135` to `0.0018` while the coalescing/bounding/anchoring architecture remained unchanged.

The first seventh-review browser gate also exposed a real ruler timing defect under rapid zoom. It was reproduced on rerun and repaired by measuring authoritative rendered stage geometry after an additional layout/render frame. The final gate then passed.

### Still deliberately unfrozen

```text
remaining tiny occasional pinch hitch
final native-pinch constants
final geometric zoom range
final graph/canvas library
final gesture library
final auto-layout algorithm
final semantic zoom/grouping
final minimap
infinite-canvas semantics
final finite-world extent algorithm
production project-search backend
final stage taxonomy
final stage widths
final stage-ruler visual treatment
permanent vertical tool-rail styling/iconography
final ambient-grid/gradient styling
final public URL contract
pan/zoom/HUD persistence contract
final visual identity
canonical Cockpit screenshot baseline
```

Future Cockpit work should build on Specification 008 rather than reopening the basic interaction architecture without new evidence.

---

## Retrieval / MethodologicalHorizon continuation

Still required:

```text
retrieval-quality fixtures
production lexical retrieval
semantic retrieval candidate evaluation
lexical/semantic fusion if justified
ranking and omission-quality evaluation
first real MethodologicalHorizon construction
selective LLM context assembly
```

Do not choose an embedding model, reranker, ANN service, or vector database from intuition.

---

## Current exact cross-track priorities

```text
A. Governed PostgreSQL knowledge-roundtrip closure
B. Specification 005 one-principal-reasoner runtime bakeoff
C. Retrieval / MethodologicalHorizon benchmark once the governed persistence seam is stable enough
D. Future Cockpit capability/product polish on top of promoted Specification 008
```

---

## Recent continuity checkpoints

```text
114  first production V1 persistence vertical slice passed
115  reusable knowledge interchange validated
116  agentic ecosystem audit + frontend track started
117  unified Cockpit workspace direction confirmed
118  first Cockpit automated gate passed
119  spatial scalability + fullscreen requirements confirmed
120  unexpected-session continuity reconciliation completed
121  immersive-scale Cockpit automated gate passed
122  third Cockpit review + zoom/canvas-dominance/scalable-navigation gate passed
123  fourth Cockpit review + balanced spatial world/orientation gate passed
124  fifth Cockpit review + continuous grid world/stage-ruler/vertical-tool-rail gate passed
125  sixth Cockpit review + ambient/pinch/ruler/collision repairs validated
126  seventh Cockpit review + final gate + interaction architecture promotion
```
