# Current State

**Checkpoint:** 123  
**Date:** 2026-08-21  
**Active development branch:** `v1-frontend-spike`  
**Development stage:** Prototype V0 complete; bounded V1 implementation and product validation across methodological knowledge, persistence/interchange, retrieval/horizon construction, agent/runtime evaluation, and the professional Project Cockpit  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate product priority:** Perform the next real-browser human product gate on the passing Specification 007 candidate v0.4 Cockpit, with particular attention to balanced low-zoom spatial navigation, stronger stage orientation, fold-away map controls, upper Details placement, and preservation of the restrained ambient grid design language

## Active ChatGPT development context

```text
Design session: 03
ChatGPT project: Autonomous Data Science System
Session title: 03 - Project Cockpit & V1 Integration
```

Repository artifacts remain authoritative across chats.

Current frontend/Cockpit work lives on:

```text
v1-frontend-spike
```

The default `main` branch intentionally trails this work and must not be treated as the latest frontend state until an explicit merge/promotion occurs.

---

## System purpose and V0 constraint

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

## Current project and methodological architecture

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

## Accepted V1 persistence and interchange

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

## Governed knowledge round-trip remains open

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

---

## Agent/runtime track

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

## Professional frontend and Project Cockpit

Foundation 021 makes the frontend a first-class reasoning, control, and quality surface.

The conventional project-view shell already demonstrates:

```text
Overview
Data
EDA
Decisions & History
methodological guidance
Question/Finding/Decision representations
run/activity state
human approval interaction
light/dark themes
loading/error states
cross-platform build/unit tests
Chromium accessibility/interaction tests
controlled direct-project visual regression
```

Human review established the stronger product model:

```text
Project Cockpit
    primary immersive active-work environment
    living project-process map
    native system interaction composer
    smooth focus into real analytical workspaces

Direct specialist views
    alternative entry and inspection paths
    reuse the same substantive modules/state
```

The Cockpit remains a derived projection over project state. It must not collapse the project process map, data/artifact lineage, methodological knowledge graph, and event history into one unreadable graph.

The engineering boundary remains:

```text
everything reachable from the Cockpit
    !=
everything mounted or loaded simultaneously
```

---

## Cockpit evidence through Checkpoint 123

The Cockpit has progressed through four real-browser human review cycles.

```text
Checkpoint 117
    core click-to-focus interaction confirmed

Checkpoint 118
    first executable /cockpit slice validated
    shared Data / EDA focus
    Production Missingness focus
    URL state + browser Back

Checkpoint 119
    stage-zone grammar positively validated
    scale/reachability/fullscreen requirements exposed

Checkpoint 121
    2D immersive-scale viewport implemented and gate passed

Checkpoint 122
    geometric zoom, trackpad pinch, scalable Jump to/search,
    canvas-dominant composer/controls, and fold-away primary HUD validated

Checkpoint 123
    fourth human review implemented and validated:
    balanced project-plane/world geometry,
    stronger stage orientation,
    fold-away map controls,
    corrected compact identity,
    higher Details placement,
    restrained ambient grid treatment preserved
```

### Current Specification 007 v0.4 implementation

The current branch implements:

```text
ProjectWorld != ProjectCanvas

ProjectWorld
    always remains larger than the viewport by a minimum scroll range
    keeps the ProjectCanvas centered
    preserves horizontal and vertical pan at minimum zoom

ProjectCanvas
    representative logical size 2260 x 1180
    balanced internal left/right stage margins
    existing subtle ambient grid/glow treatment retained

navigation
    ordinary two-axis scroll / trackpad movement
    Arrow / Shift+Arrow
    Home reset
    geometric zoom out / percentage / in
    100% reset
    Fit project
    + / - / 0 / F keyboard equivalents
    trackpad-style pinch zoom around the approximate gesture anchor

project orientation
    stronger stage headings
    stage-heading visual scale compensated against geometric zoom

project location
    scalable Jump to menu
    Active work / Blocker / Investigation / Evaluation
    searchable project work

chrome
    compact fold-away primary HUD
    floating map-control bar
    map-control bar can fold to a right-edge restore handle
    floating project Details
    Details positioned high below stage orientation on desktop
    floating System Focus
    floating composer over continuous canvas

focus/deep work
    Data
    EDA
    Production Missingness investigation
    URL/browser-history behavior retained
    reduced-motion behavior retained
    fullscreen retained
```

The fourth-review implementation was validated through temporary review branch `v1-frontend-spike-review4` and PR #3 before being advanced into `v1-frontend-spike`.

Validated code head:

```text
38c17edfe1440095d60f7e9f9bf21d42053de990
```

Final validation evidence:

```text
V1 frontend spike
workflow run number 122
run id 32457992939

Ubuntu build + unit tests
    PASS

Windows build + unit tests
    PASS

Chromium browser interaction + accessibility
    PASS

controlled direct-project visual regression
    PASS
```

Two failed intermediate gates are important historical evidence rather than hidden noise.

The first showed that the brand-row CSS fix had not actually beaten an inherited selector. The next showed a deeper low-zoom defect: with a wide viewport, a fixed-gutter world could become narrower than the scrollport and horizontal scrolling collapsed to zero.

The fixed-gutter-only model was therefore rejected. The passing implementation sizes the world from both the scaled project and the current viewport so panning remains possible at every supported zoom.

Primary current sources:

```text
docs/research/002_primary_project_cockpit_interface_concept.md
docs/research/003_unified_cockpit_workspace_and_spatial_focus_architecture.md
docs/research/004_cockpit_spatial_scalability_immersive_chrome_and_fullscreen.md
docs/research/005_cockpit_canvas_dominance_zoom_and_scalable_project_navigation.md
docs/research/006_fourth_cockpit_human_review_balanced_spatial_world_and_visual_orientation.md
docs/specifications/007_v1_unified_project_cockpit_interaction_spike.md
docs/checkpoints/123_fourth_cockpit_review_balanced_spatial_world_and_orientation_validated.md
```

Specification 007 remains **candidate v0.4**. Automated validation does not promote the specification by itself.

---

## Current Cockpit human gate

The next real-browser review should determine whether:

```text
top-left ADS · project identity now reads intentionally
stage headings are sufficiently clear at 100%, intermediate zoom, and 45%
minimum-zoom project can move/recenter naturally in all four directions
outside-project reserve feels balanced rather than excessive
internal left/right project-plane margins feel balanced
folded map controls are discoverable and unobtrusive
expanded Details is high enough without covering stage orientation
ambient grid depth remains subtle and professional
zoom / pinch / fit / reset / Jump to remain natural after the world-model change
canvas dominance, composer integration, and fullscreen still feel strong
```

If the review exposes problems, preserve them and perform another bounded iteration.

If it succeeds strongly enough, perform a deliberate promotion decision for Specification 007 rather than automatically continuing visual iteration.

Do not freeze a canonical Cockpit screenshot baseline before that decision.

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

Do not choose an embedding model, reranker, ANN service, or vector database from intuition.

The benchmark should evaluate whether important methodological knowledge is found and irrelevant/full-catalog context is avoided, not merely search latency.

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
final geometric zoom range
final pan-reserve dimensions
pan/zoom URL or session persistence contract
project-search backend
pointer-proximity HUD/control reveal
Cockpit final stage taxonomy
Cockpit final URL contract
Cockpit final visual identity
exact permanent ambient-grid styling
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

## Exact next execution order

### A. HUMAN PRODUCT GATE FOR SPECIFICATION 007 v0.4

This is the immediate substantive product step.

Open the current `/cockpit` implementation in a real browser and review the fourth-review composition before any further Cockpit architecture is frozen.

The review must explicitly cover:

```text
compact project identity
stage orientation across zoom
balanced minimum-zoom pan reserve
internal grid balance
fold-away project-map controls
Details placement
ambient grid visual treatment
2D trackpad panning
pinch zoom
explicit zoom / fit / reset
Jump to + search
composer integration
System Focus
keyboard recovery
fullscreen
professional visual quality
```

### B. GOVERNED ROUND-TRIP CLOSURE

In parallel or immediately after the human Cockpit gate where practical:

```text
confirm corrected PostgreSQL 18 gate
fix remaining portability defects honestly if present
remove temporary diagnostics
record closure only on confirmed PASS
```

### C. AGENT RUNTIME BAKEOFF

Execute Specification 005 with one principal reasoner first.

### D. RETRIEVAL / HORIZON BENCHMARK

Begin production retrieval/horizon evaluation once the governed knowledge seam is stable enough that fixture/migration debugging is not competing with retrieval evaluation.

---

## Minimum reading for continuation

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

docs/research/002_primary_project_cockpit_interface_concept.md
docs/research/003_unified_cockpit_workspace_and_spatial_focus_architecture.md
docs/research/004_cockpit_spatial_scalability_immersive_chrome_and_fullscreen.md
docs/research/005_cockpit_canvas_dominance_zoom_and_scalable_project_navigation.md
docs/research/006_fourth_cockpit_human_review_balanced_spatial_world_and_visual_orientation.md

docs/specifications/004_v1_reusable_knowledge_interchange.md
docs/specifications/005_v1_agent_runtime_and_interoperability_bakeoff.md
docs/specifications/006_v1_frontend_architecture_and_visual_spike.md
docs/specifications/007_v1_unified_project_cockpit_interaction_spike.md

docs/checkpoints/114_first_production_v1_persistence_vertical_slice_passed.md
docs/checkpoints/115_reusable_knowledge_interchange_contract_validated.md
docs/checkpoints/119_cockpit_spatial_scalability_and_true_fullscreen_requirements_confirmed.md
docs/checkpoints/120_unplanned_session_boundary_reconciliation_and_v1_continuity_restored.md
docs/checkpoints/121_immersive_scale_cockpit_slice_automated_gate_passed.md
docs/checkpoints/122_third_cockpit_review_zoom_canvas_dominance_and_scalable_navigation_gate_passed.md
docs/checkpoints/123_fourth_cockpit_review_balanced_spatial_world_and_orientation_validated.md
```
