# Current State

**Checkpoint:** 121  
**Date:** 2026-08-20  
**Active development branch:** `v1-frontend-spike`  
**Development stage:** Prototype V0 complete; bounded V1 implementation and product validation across methodological knowledge, persistence/interchange, retrieval/horizon construction, agent/runtime evaluation, and the professional Project Cockpit  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate product priority:** Perform the real-browser human product gate on the passing Specification 007 candidate v0.2 immersive-scale Cockpit slice before freezing any Cockpit technology, layout, semantic-zoom, or visual-baseline decision

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

## System purpose and the V0 constraint

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

and preserves distinctions such as:

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

Human review then established the stronger product model:

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

## Cockpit evidence through Checkpoint 121

Checkpoint 117 confirmed the core interaction:

```text
click meaningful work block
    -> smooth focus/zoom experience
    -> perform real analytical work
    -> return to surrounding project context
```

Checkpoint 118 implemented and automatically validated the first `/cockpit` slice, including shared Data/EDA workspaces, Production Missingness focus, URL-addressable focus state, browser Back restoration, and reduced-motion-safe transitions.

Checkpoint 119's second real-browser human review accepted the stage-zone visual grammar but exposed a real scalability defect: lower/right work could become unreachable behind fixed UI and the map did not yet provide a genuine scalable viewport.

Checkpoint 121 now records implementation and automated validation of the Specification 007 candidate v0.2 immersive-scale requirements.

### Implemented in the current slice

```text
genuine two-dimensional project viewport
logical project plane larger than one screen in both dimensions
horizontal + vertical scroll/trackpad navigation
Arrow-key panning
Shift + Arrow larger movement
Home reset
explicit Reset control
Jump to blocker
Jump to evaluation
sticky top stage strip with stage jump controls
compact default project chrome
expandable/collapsible project-detail HUD
collapsible System Focus as a sibling drawer rather than a map overlay
safe map/composer geometry
explicit browser fullscreen control
fullscreen state synchronization
fullscreen denial/unavailability fallback
shared Data and EDA focus surfaces retained
Production Missingness focus retained
URL/browser-history behavior retained
reduced-motion behavior retained
```

The current representative logical map is `1960 x 980` pixels. That size is evidence that the architecture can exceed one viewport, not a final project-size contract.

### Automated result

Final corrected CI evidence:

```text
V1 frontend spike
run 97
32421209920

Ubuntu build + unit tests
    PASS

Windows build + unit tests
    PASS

Chromium browser + accessibility tests
    PASS

Existing direct-project visual regression
    PASS
```

The first expanded CI attempt failed only because a newly written HUD test asserted stale fixture wording. The test was corrected to the actual current objective semantics and the rerun passed. Checkpoint 121 preserves that failure/correction transparently.

Current implementation commits:

```text
090de83a3cbe592e82e863e78e1364daa5e1f196
Implement scalable immersive Cockpit navigation

6a60fd11001eb20807b11e4e3e3244fa4cfd3d17
Style scalable Cockpit viewport and immersive chrome

a09a2ecb8a8dbefe6c702c82518a91c751d3f4ff
Extend Cockpit scalability and fullscreen browser gates

cd39044f74be7e7303edfa0b0533c568af4f1f93
Correct Cockpit project-details gate expectation
```

---

## Active Cockpit contract and remaining human gate

Current governing sources:

```text
docs/research/002_primary_project_cockpit_interface_concept.md
docs/research/003_unified_cockpit_workspace_and_spatial_focus_architecture.md
docs/research/004_cockpit_spatial_scalability_immersive_chrome_and_fullscreen.md
docs/specifications/007_v1_unified_project_cockpit_interaction_spike.md
docs/checkpoints/121_immersive_scale_cockpit_slice_automated_gate_passed.md
```

Specification 007 remains **candidate v0.2**.

The implementation has passed its automated gate, but the specification explicitly requires a human product review before any broader acceptance or visual freeze.

The next review should determine whether:

```text
the whole practical viewport feels like the operating surface
2D navigation feels natural rather than merely possible
later/right/lower work is discoverable and recoverable
compact project chrome preserves enough orientation
the top stage strip is useful
System Focus and composer remain unobtrusive
Reset/jump controls are useful
fullscreen materially improves the experience
node density/spacing/connectors/typography feel professional
another bounded iteration is required
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

### A. HUMAN PRODUCT GATE FOR SPECIFICATION 007 v0.2

This is the immediate substantive product step.

Open the current `/cockpit` implementation in a real browser and review the new scalable composition before any further Cockpit architecture is frozen.

The review must explicitly cover:

```text
2D navigation quality
large-project orientation
lower/right reachability
compact/expanded project HUD
stage strip
System Focus drawer
composer clearance
Reset and jump navigation
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

docs/specifications/004_v1_reusable_knowledge_interchange.md
docs/specifications/005_v1_agent_runtime_and_interoperability_bakeoff.md
docs/specifications/006_v1_frontend_architecture_and_visual_spike.md
docs/specifications/007_v1_unified_project_cockpit_interaction_spike.md

docs/checkpoints/114_first_production_v1_persistence_vertical_slice_passed.md
docs/checkpoints/115_reusable_knowledge_interchange_contract_validated.md
docs/checkpoints/119_cockpit_spatial_scalability_and_true_fullscreen_requirements_confirmed.md
docs/checkpoints/120_unplanned_session_boundary_reconciliation_and_v1_continuity_restored.md
docs/checkpoints/121_immersive_scale_cockpit_slice_automated_gate_passed.md
```
