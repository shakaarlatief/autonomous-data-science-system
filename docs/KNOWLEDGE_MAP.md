# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources but does not replace them.  
**Last reviewed:** 2026-08-20  
**Current checkpoint:** 121  
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
active frontend/Cockpit work = v1-frontend-spike
main intentionally trails this work
```

A continuation session must identify the active branch rather than assuming the default branch contains the latest project state.

---

## Current project stage and next action

Prototype V0 is complete with final classification:

> **STRONG FALSIFICATION OF THE CURRENT P0 DESIGN**

The project is now developing bounded V1 slices across:

```text
methodological knowledge
governed persistence/interchange
retrieval / MethodologicalHorizon construction
agent/runtime infrastructure
professional frontend
Project Cockpit
```

The immediate substantive product step is now:

```text
HUMAN PRODUCT GATE
for the Specification 007 candidate v0.2 immersive-scale Cockpit slice
```

Checkpoint 121 records that the v0.2 implementation has passed its automated gate. No final Cockpit technology, semantic-zoom, layout, or visual baseline should be frozen before the real-browser review.

Primary current routing:

```text
docs/CURRENT_STATE.md
docs/specifications/007_v1_unified_project_cockpit_interaction_spike.md
docs/research/004_cockpit_spatial_scalability_immersive_chrome_and_fullscreen.md
docs/checkpoints/121_immersive_scale_cockpit_slice_automated_gate_passed.md
```

---

## System purpose and LLM/system/human boundary

Primary sources:

```text
docs/VISION.md
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
```

Durable interpretation:

```text
LLM
    flexible reasoning component

ADS
    persistent project/process intelligence
    methodological knowledge
    provenance/governance
    deterministic controls where justified
    execution coordination
    professional reasoning/control surface

Human
    goals and semantics
    consequential judgment
    approvals/intervention where useful
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

Core result:

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

Core conceptual structure:

```text
OBJECTS
RELATIONS
EVENTS
VIEWS
```

No universal top-level project `Assessment` object is currently accepted.

Subject-specific verdicts use:

```text
Question -> Evidence -> Finding -> Claim / Decision
```

with criterion Findings where useful.

Professional workflow principles:

```text
docs/PRINCIPLES.md, P-023 and P-024
```

Responsibility split:

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

## Methodological-navigation brain and MethodologicalHorizon

Primary source:

```text
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
```

Relevance progression:

```text
KNOWN
    -> APPLICABLE
    -> RELEVANT
    -> RECOMMENDED
    -> REQUIRED / BLOCKING
```

Scaling path:

```text
large global knowledge universe
    -> project-specific retrieval/filtering
    -> bounded MethodologicalHorizon
    -> explicit applicability/context checks
    -> flexible relevance/prioritization reasoning
    -> selective task-specific LLM context
```

Active retrieval questions:

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
stable identity + exact revision identity
project-object references/influence
criterion Finding
ExecutionCapability
derived Views
```

Durable separations:

```text
intrinsic knowledge kind != reasoning function
asset != component != narrative facet
static semantic relation != conditional methodological rule
retrieval cue != applicability predicate != required context != project relevance
methodological knowledge != execution implementation
global knowledge != project-specific state
internal representation != human-facing workflow/tree
```

Important representation history:

```text
docs/checkpoints/101_five_example_reusable_knowledge_stress_test_completed.md
docs/checkpoints/102_candidate_conceptual_knowledge_representation_contract.md
docs/checkpoints/104_adversarial_review_of_candidate_knowledge_representation.md
docs/checkpoints/105_refined_representation_second_stress_test.md
docs/checkpoints/106_foundation_020_promoted_and_implementation_requirements_next.md
```

---

## Accepted V1 persistence architecture and tooling

Architecture:

```text
docs/DECISIONS.md, D-028
docs/specifications/001_v1_sqlite_technical_architecture.md
docs/checkpoints/108_v1_architecture_comparison_and_sqlite_centered_selection.md
docs/checkpoints/111_v1_technical_architecture_gate_passed_and_specification_001_promoted.md
```

Accepted V1 direction:

```text
SQLite-centered local-first operational state
FTS5 rebuildable lexical index
rebuildable embeddings / initial exact semantic retrieval
application-level TRUE/FALSE/UNKNOWN rule evaluator
selective LLM context assembly
filesystem/Git/artifact storage for large/code artifacts
```

Persistence tooling:

```text
docs/DECISIONS.md, D-029
docs/specifications/002_v1_persistence_tooling_standard.md
docs/checkpoints/112_v1_persistence_tooling_selected_and_validated.md
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
docs/checkpoints/113_v1_python_project_tooling_validated.md
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

It proves exact historical project-to-knowledge revision pinning after a newer knowledge revision becomes current.

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

Candidate/benchmark import cannot silently create accepted methodological authority.

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

The first PostgreSQL defect was an overlong manually named migration constraint. The identifier was shortened and revalidation was triggered, but closure still requires a persisted corrected PostgreSQL PASS and removal of temporary diagnostics.

Active question:

```text
docs/OPEN_QUESTIONS.md, Q-048
```

Do not conflate this richer gate with Checkpoint 114's already-passing narrower PostgreSQL persistence slice.

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

Runtime bakeoff:

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

A simpler direct-model-call result remains valid if no framework earns its complexity.

Active questions:

```text
docs/OPEN_QUESTIONS.md, Q-046 and Q-047
```

---

## Professional frontend foundation

Primary foundation:

```text
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
```

Initial frontend evaluation contract:

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

The conventional project-view shell already demonstrates Overview, Data, EDA, Decisions & History, methodological guidance, run state, approval interaction, themes, loading/error handling, cross-platform builds/tests, accessibility checks, and controlled direct-project visual regression.

Chart strategy remains under evaluation:

```text
ECharts
vs
Plotly
```

Tauri remains a later packaging candidate.

---

## Project Cockpit concept and deep-work architecture

Initial product concept:

```text
docs/research/002_primary_project_cockpit_interface_concept.md
```

Core model:

```text
Project Cockpit
    primary active-work environment
    living project-process map
    native system interaction
    focused analytical work surface

Direct specialist views
    alternative inspection / entry paths
```

Unified deep-work architecture:

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

Critical engineering boundary:

```text
everything reachable from the Cockpit
    !=
everything mounted or loaded simultaneously
```

Direct routes and Cockpit focus reuse the same substantive Data/EDA/etc. workspaces rather than duplicating them.

---

## First executable Project Cockpit spike

Candidate contract:

```text
docs/specifications/007_v1_unified_project_cockpit_interaction_spike.md
```

First implementation evidence:

```text
docs/checkpoints/118_first_unified_cockpit_interaction_spike_automated_gate_passed.md
```

Validated in the first slice:

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
cross-platform build/unit tests
Chromium interaction/accessibility
existing direct-project visual regression
```

No graph/canvas library was selected.

---

## Second human review and immersive-scale requirements

Design evidence:

```text
docs/research/004_cockpit_spatial_scalability_immersive_chrome_and_fullscreen.md
docs/checkpoints/119_cockpit_spatial_scalability_and_true_fullscreen_requirements_confirmed.md
```

The second real-browser review accepted the stage-zone visual grammar and exposed a real scale/reachability defect.

It established requirements for:

```text
genuine 2D project-space navigation
horizontal + vertical project growth
later/right/lower work always reachable
future semantic zoom/grouping
compact/expandable Cockpit HUD
stage orientation near top of operating viewport
true browser fullscreen
collision-safe floating/docked surfaces
fit/reset/jump navigation
keyboard-accessible recovery
```

Specification 007 was revised to candidate v0.2 for this bounded slice.

---

## Immersive-scale Cockpit implementation and automated gate

Current implementation evidence:

```text
docs/checkpoints/121_immersive_scale_cockpit_slice_automated_gate_passed.md
```

Current implementation now demonstrates:

```text
1960 x 980 representative logical project plane
genuine horizontal and vertical viewport movement
scroll/trackpad navigation
Arrow-key and Shift+Arrow panning
Home reset
explicit Reset
Jump to blocker
Jump to evaluation
sticky top stage strip + stage jumps
later/right/lower representative work
compact default project chrome
expandable/collapsible project HUD
collapsible System Focus sibling drawer
composer-safe map geometry
explicit browser Fullscreen API control
fullscreen denial/unavailable fallback
shared Data/EDA/Missingness focus behavior retained
URL/history/reduced-motion behavior retained
```

Final corrected CI evidence:

```text
V1 frontend spike run 97
32421209920

Ubuntu build + unit tests                  PASS
Windows build + unit tests                 PASS
Chromium browser + accessibility           PASS
Existing direct-project visual regression  PASS
```

The first expanded run failed only because one newly authored test used stale fixture wording. Checkpoint 121 records that failure and the test-contract correction transparently.

### Current Cockpit status

```text
Specification 007
    candidate v0.2

automated immersive-scale gate
    PASS

human product gate
    PENDING
```

No final graph/canvas library, minimap, auto-layout system, semantic-zoom algorithm, stage taxonomy, URL contract, visual identity, or Cockpit screenshot baseline has been selected.

---

## Current frontend continuation

Immediate next work:

```text
real-browser human product review of /cockpit
```

Review specifically:

```text
2D navigation quality
large-project orientation
lower/right reachability
compact/expanded HUD
stage strip
System Focus drawer
composer clearance
Reset/jump navigation
keyboard recovery
browser fullscreen
visual hierarchy / professional quality
```

If the review exposes weaknesses, perform another bounded iteration and preserve the evidence.

If it passes strongly, decide explicitly which parts are mature enough to promote. Do not infer promotion from the automated gate alone.

Active open frontend questions:

```text
docs/OPEN_QUESTIONS.md, Q-049 through Q-052
```

---

## Retrieval / MethodologicalHorizon track

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

Do not select an embedding model, reranker, ANN service, or vector database from intuition.

The benchmark must test omission quality, relevance, and context cost rather than search speed alone.

---

## Current major non-selections

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
Cockpit auto-layout algorithm
Cockpit minimap implementation
Cockpit semantic-zoom algorithm
Cockpit final stage taxonomy
Cockpit final URL contract
Cockpit final visual identity
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

---

## Continuity and preservation routing

Current development/preservation method:

```text
docs/DEVELOPMENT_METHOD.md
```

Cross-session procedure:

```text
docs/CONTINUITY.md
```

Checkpoint-format contract:

```text
docs/checkpoints/README.md
```

Checkpoint 120 records recovery from the unexpected Session 02 conversation boundary and the requirement to reconstruct from the active feature branch rather than `main` when branch-local work is newer.

Checkpoint 121 is the current implementation/verification boundary.

---

## Exact next execution order

```text
A. HUMAN COCKPIT PRODUCT GATE
   review current /cockpit in a real browser
   preserve visual/interaction findings
   iterate if necessary
   do not freeze architecture or screenshot baseline prematurely

B. GOVERNED ROUND-TRIP CLOSURE
   confirm corrected PostgreSQL 18 gate
   fix remaining portability defects if any
   remove temporary diagnostics
   close only on persisted PASS

C. AGENT RUNTIME BAKEOFF
   execute Specification 005
   begin with one principal reasoner

D. RETRIEVAL / HORIZON BENCHMARK
   validate lexical/semantic retrieval and first real MethodologicalHorizon
   only after governed knowledge fixtures are stable enough
```

For the most exact current state and continuation point, prefer `docs/CURRENT_STATE.md` over this routing index.