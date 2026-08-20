# Current State

**Checkpoint:** 120  
**Date:** 2026-08-20  
**Active development branch:** `v1-frontend-spike`  
**Development stage:** Prototype V0 complete; bounded V1 implementation and product validation across methodological knowledge, persistence/interchange, retrieval/horizon construction, agent/runtime evaluation, and the professional Project Cockpit  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Immediate product priority:** Implement the Specification 007 candidate v0.2 immersive-scale Cockpit slice established by the second human review, then return to a human product gate before freezing the design

## Active ChatGPT development context

```text
Design session: 03
ChatGPT project: Autonomous Data Science System
Session title: 03 - Project Cockpit & V1 Integration
```

Repository artifacts remain authoritative across chats.

The active frontend/Cockpit work currently lives on `v1-frontend-spike`; the default `main` branch trails this work and must not be treated as the latest frontend state until an explicit merge/promotion occurs.

---

## What we are building

The Autonomous Data Science System is intended to become a professional interactive data-science operating environment in which the system carries much of the methodological memory, project memory, process navigation, evidence discipline, provenance, execution coordination, and reporting burden that otherwise has to be repeatedly supplied by a human through prompts.

The LLM is one flexible reasoning component inside the wider system, not the system itself.

The product should preserve strong human inspection, discussion, override, editing, execution, approval, and guidance.

Primary vision sources:

```text
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
```

---

## Prototype V0 constraint

Prototype V0 strongly falsified the then-current P0 implementation strategy.

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

Authoritative evidence:

```text
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

Foundation 019 governs methodological relevance:

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

Foundation 020 promotes the reusable representation around:

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

Accepted decisions/specifications:

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

Last persisted gate state:

```text
SQLite round-trip
    PASS

PostgreSQL 18 round-trip
    FAIL
```

The first PostgreSQL defect was localized to a manually named migration constraint longer than PostgreSQL's 63-character identifier limit.

The identifier was shortened and revalidation was triggered, but the repository does not yet contain a persisted corrected PostgreSQL PASS.

Do not call this gate closed until:

```text
corrected PostgreSQL 18 round-trip PASS is persisted
remaining portability defects, if any, are fixed honestly
temporary diagnostic artifacts/workflow are removed
closure is recorded in a dedicated checkpoint
```

This gate is separate from Checkpoint 114's narrower production persistence slice, which already passed PostgreSQL.

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

The bakeoff begins with one principal reasoner and tests ADS-shaped requirements such as domain isolation, tools, MCP, approval interruption, durable resume, external project-state authority, bounded context transparency, cancellation, retry semantics, structured output, observability, and test/provider substitution.

A simple direct-model-call result remains valid if no framework earns its complexity.

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
controlled project-view visual regression
```

Human review then established the stronger Project Cockpit direction.

### Strongly preferred product model

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

The Cockpit is a derived projection over project state. It must not collapse the project process map, data/artifact lineage, methodological knowledge graph, and event history into one unreadable graph.

The implementation must preserve:

```text
everything reachable from the Cockpit
    !=
everything mounted or loaded simultaneously
```

---

## Cockpit evidence through Checkpoint 119

Checkpoint 117 confirmed the spatial interaction:

```text
click meaningful work block
    -> smooth focus/zoom experience
    -> perform real analytical work
    -> return to surrounding project context
```

Checkpoint 118 records the first executable `/cockpit` spike and its passing automated gate.

Implemented and validated at that stage:

```text
immersive Cockpit route
stage-zone living project map
meaningful dynamic work blocks
blocked / attention / selected / complete / deferred states
persistent system composer
spatial focus handoff
shared Data and EDA workspaces inside focus
Production Missingness focused investigation
URL-addressable focus state
browser Back restoration
reduced-motion-safe transition fallback
Ubuntu/Windows build + unit tests PASS
Chromium interaction/accessibility PASS
existing direct project-view visual regression PASS
```

The second real-browser human review, preserved in Checkpoint 119, accepted the current stage-zone visual grammar:

```text
technical dark operating canvas
visible stage boundaries
Framing
Data & Exploration
Validation
Modeling
Evaluation
semantic work blocks
meaningful connections
clear project-state distinctions
```

The same review found a real accessibility/scalability defect: lower/right project work can become unreachable behind fixed composer/context UI because the current map does not yet provide sufficient viewport movement.

---

## Active Cockpit implementation contract

Current governing sources:

```text
docs/research/004_cockpit_spatial_scalability_immersive_chrome_and_fullscreen.md
docs/specifications/007_v1_unified_project_cockpit_interaction_spike.md
docs/checkpoints/119_cockpit_spatial_scalability_and_true_fullscreen_requirements_confirmed.md
```

Specification 007 is **candidate v0.2**, not a final frozen interface specification.

Before the next human gate, the Cockpit must demonstrate:

```text
1. no inaccessible lower/right work;
2. horizontal and vertical project-space navigation;
3. project extent larger than one viewport;
4. compact/collapsible project HUD instead of a large permanent header;
5. stage orientation aligned near the top of the operating viewport;
6. explicit true-browser-fullscreen control with graceful fallback;
7. collision-safe composer/context surfaces;
8. at least one fit/reset/jump navigation affordance;
9. keyboard-accessible recovery/navigation independent of pointer panning;
10. architecture compatible with future semantic zoom/grouping without requiring every work object at full detail.
```

No graph/canvas library, minimap implementation, auto-layout algorithm, semantic-zoom algorithm, final stage taxonomy, final URL contract, or final Cockpit visual identity is selected yet.

Do not freeze a canonical Cockpit visual-regression baseline before the next human product gate.

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

The retrieval benchmark should evaluate whether relevant methodological knowledge is found and whether irrelevant/full-catalog context is avoided, not merely search latency.

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
complete Foundation 018 production schema
artifact-storage backend
job queue/cloud deployment
```

---

## Continuity repair completed at Checkpoint 120

Session 02 reached the platform conversation-length limit unexpectedly immediately after Checkpoint 119 preservation.

The substantive design survived in Research 004, Specification 007 v0.2, and Checkpoint 119, but the normal end-of-session routing/current-state reconciliation had not completed.

Checkpoint 120 records the repair.

Reconciled surfaces include:

```text
README.md
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/OPEN_QUESTIONS.md
docs/CONTINUITY.md
docs/checkpoints/README.md
docs/MAJOR_CHANGES.md
.gitignore frontend generated/dependency hygiene
```

Design Session 03 is now the active repository-development context.

---

## Exact next execution order

### A. IMPLEMENT SPECIFICATION 007 v0.2 IMMERSIVE-SCALE COCKPIT SLICE

This is the immediate substantive product step.

```text
fix unreachable lower/right work
    -> implement professional 2D viewport navigation
    -> prove project extent beyond one screen
    -> compact/expandable HUD
    -> top-aligned stage strip/orientation
    -> true browser fullscreen
    -> collision-safe floating surfaces
    -> fit/reset/jump navigation
    -> keyboard-accessible recovery
```

Then rerun cross-platform build, browser interaction, accessibility, and relevant visual checks and return to human product review.

Do not select/freeze a final canvas, auto-layout, semantic-zoom, or visual-baseline architecture before that review.

### B. GOVERNED ROUND-TRIP CLOSURE

In parallel or immediately after the bounded frontend slice where practical:

```text
confirm corrected PostgreSQL 18 gate
fix remaining portability defects honestly if present
remove temporary diagnostics
record closure only on confirmed PASS
```

### C. AGENT RUNTIME BAKEOFF

Execute Specification 005 with one principal reasoner first.

### D. RETRIEVAL / HORIZON BENCHMARK

Begin production retrieval/horizon evaluation once the governed knowledge seam is stable enough that fixture and migration debugging are not competing.

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
```
