# Current State

**Checkpoint:** 118  
**Date:** 2026-08-20  
**Development stage:** Prototype V0 complete; post-V0 product/object/methodological-knowledge architecture accepted; V1 persistence and reusable-knowledge interchange implemented to their tested scopes; agent-runtime selection remains an explicit evaluation track; the professional frontend now includes a passing first unified Project Cockpit interaction spike whose human visual/product gate is the immediate frontend priority  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Execution mode:** Build bounded professional product slices and falsification gates. Prefer standards/existing infrastructure for agent/runtime/interoperability responsibilities, keep ADS domain/project semantics authoritative, and require human product review before freezing major interaction/visual decisions.

## Active ChatGPT development context

```text
Design session: 02
ChatGPT project: Autonomous Data Science System
Session title: 02 - Methodological Brain & Knowledge Units
```

Repository artifacts remain authoritative across chats.

---

## Current product goal

The Autonomous Data Science System should become a professional interactive data-science operating environment that carries much of the methodological memory, project memory, option generation, process navigation, execution discipline, provenance, and reporting burden while preserving strong human inspection, discussion, override, editing, execution, and guidance.

The frontend is part of that architecture rather than a cosmetic layer. The product target is explicitly a modern, visually excellent, premium professional analytical application with strong typography, information hierarchy, dark/light themes, accessibility, responsive professional desktop layouts, polished loading/error/empty states, and high-quality analytical visualization.

A major product-direction refinement is now active:

```text
Project Cockpit
    primary immersive active-work environment

Overview / Data / EDA / Validation / Features / Models / Experiments /
Evaluation / Decisions & History / Report
    direct project inspection and specialist entry views
```

The Cockpit should be capable of deep analytical work itself through spatial focus transitions. The specialist views remain valuable alternative entry paths into the same underlying functionality rather than mandatory escape hatches from the Cockpit.

Primary product sources:

```text
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md

docs/research/002_primary_project_cockpit_interface_concept.md
docs/research/003_unified_cockpit_workspace_and_spatial_focus_architecture.md
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

## Project object model and methodological brain

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

The design does not add a universal top-level `Assessment` object. Subject-specific criterion verdicts use:

```text
Question -> Evidence -> Finding -> Claim/Decision
```

with a structured criterion-Finding form where useful.

Foundation 019 governs methodological relevance:

```text
KNOWN
    -> APPLICABLE
    -> RELEVANT
    -> RECOMMENDED
    -> REQUIRED / BLOCKING
```

Conceptually:

```text
large global knowledge base
    -> high-recall project-specific retrieval/filtering
    -> bounded methodological horizon
    -> explicit checks + flexible reasoning
    -> selective task-specific LLM context
```

Foundation 020 promotes:

```text
KnowledgeAsset
KnowledgeComponent
NarrativeFacet
KnowledgeRelation
Conditional KnowledgeRule
KnowledgeCollection
Project objects referencing exact knowledge revisions
Criterion Finding
ExecutionCapability
Derived Views
```

Promoted methodological representation principles:

```text
P-025  knowledge identity/granularity != reasoning function
P-026  static relationships != conditional guidance rules
```

---

## Accepted V1 persistence architecture and tooling

Accepted decisions/specifications:

```text
D-028 + Specification 001
    SQLite-centered local-first operational architecture
    FTS5 rebuildable lexical index
    rebuildable embeddings / initial exact semantic retrieval
    app-level rule evaluator
    selective context assembly
    filesystem/Git/artifact storage outside DB

D-029 + Specification 002
    SQLAlchemy Core 2.0 stable series
    Alembic 1.x migrations

D-030 + Specification 003
    pyproject.toml
    uv 0.12.5 + committed uv.lock
    uv_build
    src/ads_system
    Python >=3.12
```

PostgreSQL + pgvector remains the preferred first persistence/semantic migration family if real requirements exceed the SQLite envelope.

Checkpoint 114 proves the first production persistence vertical slice on SQLite/Linux, SQLite/Windows, and PostgreSQL 18 and proves exact historical knowledge-revision pinning for project Findings.

---

## Accepted reusable-knowledge interchange

Checkpoint 115 validated the heterogeneous reusable-knowledge bundle under KI-01 through KI-10.

Accepted:

```text
D-031
Specification 004 v1.0
```

Interchange:

```text
standard JSON
+ JSON Schema Draft 2020-12
+ application-level semantic validation
+ deterministic normalization/serialization
```

Authority model:

```text
operational database
    authoritative runtime state

interchange JSON
    human-reviewable / storage-neutral representation

FTS / embeddings / caches
    rebuildable derived state
```

Governance requirement:

```text
CANDIDATE_SET / BENCHMARK_FIXTURE
    cannot silently create accepted methodological authority

ACCEPTED_SNAPSHOT
    trusted restore/bootstrap/migration path
```

Sources:

```text
docs/DECISIONS.md, D-031
docs/specifications/004_v1_reusable_knowledge_interchange.md
docs/checkpoints/115_reusable_knowledge_interchange_contract_validated.md
experiments/architecture_spikes/V1_KNOWLEDGE_INTERCHANGE_RESULT.md
```

---

## Governed persistence round-trip status

A richer governed knowledge round-trip path is implemented, including:

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

The last canonically confirmed gate state remains:

```text
SQLite roundtrip
    PASS

first PostgreSQL 18 roundtrip
    FAIL
```

The first PostgreSQL defect is understood and localized: migration 0002 used a manually named foreign-key constraint longer than PostgreSQL's 63-character identifier limit.

Fix committed:

```text
ba6a92f83aac3a63ebfb7f97a4378c93fa28547b
Shorten interchange migration identifiers for PostgreSQL
```

Status tracing improvement:

```text
a69b8859696fbd3b45124c257d085989d692a207
Make roundtrip gate status traceable to source commit
```

Do not call the governed round-trip complete until a corrected PostgreSQL PASS is persisted and confirmed. Temporary diagnostic artifacts/workflow should be removed after final resolution.

---

## 2026 agentic ecosystem architecture audit

Research 001 concluded:

```text
ADS project/domain/methodological semantics
    are durable product architecture

agent frameworks / MCP / A2A / AG-UI / runtime checkpointing
    are infrastructure and interoperability mechanisms
```

Promoted principles:

```text
P-027
Agent frameworks and interoperability protocols are infrastructure,
not ADS domain authority.

P-028
Prefer deterministic software for explicit work and agent reasoning
for genuine ambiguity.

P-029
The product interface is a first-class reasoning, control, and
quality surface.
```

### MCP

Treat MCP as a first-class candidate external tool/resource integration boundary, not as project memory or an internal application bus.

### A2A

Deferred until ADS actually needs independently deployed remote agent systems.

### AG-UI

Evaluate as an adapter around ADS-owned interaction/run events. Do not make it the domain event model.

---

## Agent-runtime evaluation track

No agent framework, LLM provider, or multi-agent architecture is accepted yet.

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

Mandatory bakeoff areas include:

```text
domain isolation
single-agent tool loop
current MCP integration
human approval interruption
durable resume after process boundary
external ADS project-state authority
context transparency
cancellation/timeouts
failure/retry semantics
structured output
observability
provider/test substitution
```

Start with one principal reasoner. Multi-agent complexity must earn its place through evidence.

A valid result remains using simpler direct model calls if no framework provides enough incremental value.

---

## Professional frontend track

Foundation 021 makes the frontend an active parallel V1 track.

Candidate technical/visual evaluation contract:

```text
docs/specifications/006_v1_frontend_architecture_and_visual_spike.md
```

Current leading stack hypothesis, still not fully promoted as final product architecture:

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

The first project-view frontend now includes:

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

The human review of this first shell was positive about its breadth and professional direction, while identifying two important points:

1. the methodological right panel needed to stop overlapping the Data workspace and needed folding behavior;
2. the shell was primarily an inspection/navigation product and did not yet contain the main active-work interface envisioned for ADS.

The panel defect has been corrected with a collapsible reserved layout column and browser coverage.

---

## Unified Project Cockpit direction

Research 002 and Research 003 now define the active Cockpit design hypothesis.

Strongly confirmed interaction:

```text
click a meaningful work block
    -> smooth spatial focus / zoom experience
    -> perform real analytical work there
    -> return to the surrounding living project map
```

The preferred product model is now:

```text
Cockpit
    complete active-work environment
    project process/reasoning map
    system interaction composer
    focused analytical work surfaces

Direct specialist views
    alternate entry and inspection surfaces
    same substantive functionality where possible
```

The Cockpit should not be restricted to shallow summaries. Deep Data/EDA/Validation/Modeling/Evaluation work should be reachable and usable inside the focus experience when technically appropriate.

Critical scalability principle:

```text
everything reachable from the Cockpit
    !=
everything mounted or loaded simultaneously
```

The implementation should use selective mounting/code splitting/backend pagination or streaming/virtualization where required. Visual continuity does not require one enormous always-rendered DOM graph.

The Cockpit primarily visualizes the project process/reasoning projection. It must not collapse process map, data lineage, methodological knowledge graph, and event history into one unreadable graph.

Sources:

```text
docs/research/002_primary_project_cockpit_interface_concept.md
docs/research/003_unified_cockpit_workspace_and_spatial_focus_architecture.md
docs/checkpoints/117_unified_cockpit_workspace_direction_confirmed.md
```

---

## First executable Cockpit interaction spike

Candidate implementation contract:

```text
docs/specifications/007_v1_unified_project_cockpit_interaction_spike.md
```

Checkpoint 118 records the first executable proof.

Implemented:

```text
/cockpit immersive route
minimal Cockpit chrome
stage-zone living project map
dynamic meaningful work blocks
blocked / attention / selected / complete / deferred visual states
persistent system composer
spatial focus handoff
shared DataPage inside Cockpit focus
shared EdaPage inside Cockpit focus
dedicated Production Missingness focused investigation
URL-addressable focus state
browser Back restoration
reduced-motion-safe transition fallback
```

No graph/canvas framework is selected. The first spike intentionally uses ordinary React/CSS/SVG/browser primitives so the interaction can be evaluated before a library shapes the product.

Automated evidence from GitHub Actions run 70 (`32404745578`) on source commit `5d8412e3d7faeecef1b1669bacda8a5cc2a0466e`:

```text
Ubuntu build + unit tests
    PASS

Windows build + unit tests
    PASS

Chromium browser + accessibility gate
    PASS

Existing project-view visual regression
    PASS
```

The Cockpit itself deliberately does not yet have a canonical screenshot baseline because the human visual/product gate is still pending.

Historical implementation evidence:

```text
docs/checkpoints/118_first_unified_cockpit_interaction_spike_automated_gate_passed.md
```

---

## Retrieval/horizon track remains active

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

The representative reusable-knowledge corpus should become a retrieval benchmark only after the governed persistence/interchange seam is stable enough that fixture changes are not competing with migration debugging.

---

## Still intentionally unselected or incomplete

```text
agent runtime
number of agents
LLM provider/model
MCP server catalog
A2A
AG-UI final role
frontend final stack promotion
chart library
Cockpit final visual identity
Cockpit graph/canvas library
Cockpit auto-layout algorithm
Cockpit final stage taxonomy
Cockpit final URL contract
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

These are attached to requirements or explicit spikes rather than being open-ended technology choices.

---

## Exact near-term execution order

### A. HUMAN COCKPIT PRODUCT REVIEW

Immediate frontend priority:

```text
pull v1-frontend-spike
open /cockpit
review project-map visual character
click Data understanding
click Production missingness
handoff to full Data focus
click EDA evidence
review back/zoom-out behavior
review composer placement and system presence
```

The main question is whether this begins to feel like the primary operating environment of a serious Autonomous Data Science System.

Do not promote Specification 007 or freeze Cockpit screenshot baselines before this review.

### B. GOVERNED ROUNDTRIP CLOSURE

```text
confirm corrected PostgreSQL 18 gate
fix any remaining portability defect honestly
remove temporary diagnostics
close with dedicated checkpoint only on confirmed PASS
```

### C. AGENT RUNTIME BAKEOFF

```text
implement Specification 005 representative workload
begin single-agent first
compare surviving runtimes against actual ADS requirements
```

### D. FRONTEND REFINEMENT AFTER HUMAN REVIEW

Depending on the review:

```text
refine Living Project Map + Focus direction
or compare a materially different Cockpit composition
then decide whether a dedicated spatial canvas library is justified
then expand responsive/dark-mode/Cockpit visual gates
```

Retrieval benchmark work follows in parallel once the knowledge seam is stable.

---

## Minimum reading for continuation

```text
README.md
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
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

docs/specifications/001_v1_sqlite_technical_architecture.md
docs/specifications/002_v1_persistence_tooling_standard.md
docs/specifications/003_v1_python_project_and_dependency_tooling.md
docs/specifications/004_v1_reusable_knowledge_interchange.md
docs/specifications/005_v1_agent_runtime_and_interoperability_bakeoff.md
docs/specifications/006_v1_frontend_architecture_and_visual_spike.md
docs/specifications/007_v1_unified_project_cockpit_interaction_spike.md

docs/checkpoints/114_first_production_v1_persistence_vertical_slice_passed.md
docs/checkpoints/115_reusable_knowledge_interchange_contract_validated.md
docs/checkpoints/116_agentic_ecosystem_audit_and_frontend_track_started.md
docs/checkpoints/117_unified_cockpit_workspace_direction_confirmed.md
docs/checkpoints/118_first_unified_cockpit_interaction_spike_automated_gate_passed.md
```
