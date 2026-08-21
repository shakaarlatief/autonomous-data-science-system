# Current State

**Checkpoint:** 122  
**Date:** 2026-08-21  
**Active development branch:** `v1-frontend-spike`  
**Development stage:** Prototype V0 complete; bounded V1 implementation and product validation across methodological knowledge, persistence/interchange, retrieval/horizon construction, agent/runtime evaluation, and the professional Project Cockpit  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate product priority:** Perform the next real-browser human product gate on the passing Specification 007 candidate v0.3 Cockpit refinement, with particular attention to zoom, trackpad interaction, canvas dominance, scalable Jump to/search navigation, floating composer/controls, and fold-away primary HUD

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

Primary sources:

```text
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
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

## Cockpit evidence through Checkpoint 122

Checkpoint 117 confirmed the core click-to-focus interaction.

Checkpoint 118 implemented and automatically validated the first `/cockpit` slice, including shared Data/EDA workspaces, Production Missingness focus, URL-addressable focus state, browser Back restoration, and reduced-motion-safe transitions.

Checkpoint 119's second real-browser review accepted the stage-zone visual grammar but exposed real scale and immersion defects: lower/right work could become unreachable, the project was still too single-screen-like, and persistent chrome consumed too much workspace.

Checkpoint 121 then implemented and validated the first immersive-scale requirements:

```text
genuine two-dimensional project viewport
horizontal + vertical movement
project extent larger than one viewport
keyboard panning and recovery
compact project details
collapsible System Focus
true browser fullscreen
collision-safe map/composer geometry
```

The third real-browser review, now preserved in Research 005 and Checkpoint 122, accepted the smooth jump interaction but identified a stronger professional composition:

```text
project canvas should be the dominant visual object
project navigation should scale through Jump to + search
geometric zoom is required
trackpad pan and pinch zoom are required
composer should float over continuous canvas
map controls should float rather than consume a full-width row
one compact top HUD is preferable to duplicated persistent layers
primary HUD should itself be foldable
```

### Current Specification 007 v0.3 implementation

The current branch now implements:

```text
2260 x 1180 representative logical project plane
native two-axis scroll/trackpad movement
Arrow / Shift+Arrow / Home navigation

geometric zoom
    zoom out
    zoom percentage
    zoom in
    reset to 100%
    fit project
    + / - / 0 / F keyboard equivalents
    trackpad-style pinch handling around the gesture anchor

scalable Jump to navigation
    Active work
    Blocker
    Investigation
    Evaluation
    searchable project-work list

canvas-dominant chrome
    no separate full-width Project operating map control row
    floating translucent map toolbar
    floating project details
    floating System Focus
    composer floating over continuous project canvas
    lower/right logical margin for unobstructed work recovery

primary Cockpit HUD
    reduced persistent height
    explicit hide action
    small explicit restore affordance

existing deep-work behavior retained
    Data focus
    EDA focus
    Production Missingness focus
    URL state
    browser Back
    reduced motion
    fullscreen
```

The implementation was validated on a temporary PR branch and then fast-forwarded into `v1-frontend-spike`.

Validated implementation head:

```text
e500eb45c1de59f24b1531b890f55d2ec3bfffc5
```

Final validation result:

```text
V1 frontend spike
PR workflow run 105
32453067031

Ubuntu build + unit tests
    PASS

Windows build + unit tests
    PASS

Chromium browser interaction + accessibility
    PASS

controlled direct-project visual regression
    PASS
```

The browser gate explicitly exercises searchable Jump to navigation, Investigation quick jump, keyboard recovery, zoom buttons, keyboard zoom, fit project, trackpad-style pinch input, primary HUD hide/show, canvas continuation behind the composer, lower-work unobstructed recovery, fullscreen, and automated accessibility.

An earlier browser assertion measured lower-work placement immediately after starting a deliberately smooth jump. The navigation implementation was hardened with explicit zoom-aware target centering, and the test was corrected to wait for the asynchronous smooth motion before measuring its final unobstructed placement. The product was not degraded to an abrupt jump merely to satisfy a synchronous test.

---

## Active Cockpit contract and remaining human gate

Current governing sources:

```text
docs/research/002_primary_project_cockpit_interface_concept.md
docs/research/003_unified_cockpit_workspace_and_spatial_focus_architecture.md
docs/research/004_cockpit_spatial_scalability_immersive_chrome_and_fullscreen.md
docs/research/005_cockpit_canvas_dominance_zoom_and_scalable_project_navigation.md
docs/specifications/007_v1_unified_project_cockpit_interaction_spike.md
docs/checkpoints/122_third_cockpit_review_zoom_canvas_dominance_and_scalable_navigation_gate_passed.md
```

Specification 007 is now **candidate v0.3**.

The revised implementation has passed its automated gate, but the specification still requires another human product review before broader acceptance or any visual freeze.

The next review should determine whether:

```text
the project canvas now visually dominates the application
one-line top HUD is compact enough
HUD hide/restore feels natural
floating map controls are clear without feeling cluttered
composer feels native to the canvas rather than like a footer
ordinary two-finger trackpad movement pans naturally
trackpad pinch zoom feels natural and anchored correctly
explicit zoom / fit / reset controls feel useful
Jump to quick destinations + project search feel scalable
lower/right work remains easy to recover into a clear area
fullscreen + fold-away chrome create the intended immersive experience
```

Do not freeze a Cockpit visual-regression baseline before that review.

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
pan/zoom URL or session persistence contract
project-search backend
pointer-proximity HUD reveal
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

## Exact next execution order

### A. HUMAN PRODUCT GATE FOR SPECIFICATION 007 v0.3

This is the immediate substantive product step.

Open the current `/cockpit` implementation in a real browser and review the revised canvas-dominant composition before any further Cockpit architecture is frozen.

The review must explicitly cover:

```text
canvas dominance
compact/fold-away primary HUD
stage strip
floating map toolbar
Jump to quick semantics + project search
2D panning
trackpad pinch zoom
explicit zoom controls
fit/reset recovery
floating System Focus
composer integration
lower/right reachability
keyboard recovery
browser fullscreen
visual hierarchy and professional quality
```

If the review exposes problems, preserve them and perform another bounded Cockpit iteration.

If it succeeds strongly enough, decide what, if anything, is mature enough to promote. Do not assume that an automated PASS alone promotes Specification 007 or selects a final canvas/semantic-zoom architecture.

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

docs/research/001_2026_agentic_ecosystem_and_integration_architecture_audit.md
docs/research/002_primary_project_cockpit_interface_concept.md
docs/research/003_unified_cockpit_workspace_and_spatial_focus_architecture.md
docs/research/004_cockpit_spatial_scalability_immersive_chrome_and_fullscreen.md
docs/research/005_cockpit_canvas_dominance_zoom_and_scalable_project_navigation.md

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
```
