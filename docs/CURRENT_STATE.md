# Current State

**Checkpoint:** 116  
**Date:** 2026-08-20  
**Development stage:** Prototype V0 complete; post-V0 product/object/methodological-knowledge architecture accepted; V1 persistence foundation and reusable-knowledge interchange implemented to their tested scopes; agent-runtime selection and professional frontend product shell are now explicit parallel evaluation tracks while the governed PostgreSQL round-trip remains open pending corrected confirmation  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Execution mode:** Build bounded professional product slices and falsification gates. Prefer standards/existing infrastructure for agent/runtime/interoperability responsibilities, but keep ADS domain/project semantics independent and authoritative.

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

The frontend is part of that product architecture rather than a cosmetic layer. The target is now explicitly a modern, visually excellent, premium professional analytical application with strong typography, information hierarchy, dark/light themes, accessibility, responsive professional desktop layouts, polished loading/error/empty states, and high-quality analytical visualization.

Primary product sources:

```text
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
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
```

The design does not add a universal top-level `Assessment` object. Subject-specific criterion verdicts use:

```text
Question -> Evidence -> Finding -> Claim/Decision
```

with a structured criterion-Finding form where useful.

Foundation 019 governs the methodological horizon:

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

The first production persistence vertical slice in Checkpoint 114 passed on SQLite/Linux, SQLite/Windows, and PostgreSQL 18 and proves exact historical knowledge-revision pinning for project Findings.

---

## Accepted reusable-knowledge interchange

Checkpoint 115 validated the heterogeneous reusable-knowledge bundle under KI-01 through KI-10.

The previously pending promotion is now complete:

```text
D-031
Specification 004 v1.0
```

Accepted interchange:

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

Current confirmed gate state:

```text
SQLite roundtrip
    PASS

first PostgreSQL 18 roundtrip
    FAIL
```

The PostgreSQL failure is understood and localized. Migration 0002 used a manually named foreign-key constraint longer than PostgreSQL's 63-character identifier limit.

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

At Checkpoint 116, a corrected PostgreSQL PASS has not yet been persisted and confirmed. Do not call the governed round-trip complete until that happens.

Temporary diagnostic artifacts/workflow should be removed after final resolution.

---

## 2026 agentic ecosystem architecture audit

A current external-ecosystem audit has now been completed:

```text
docs/research/001_2026_agentic_ecosystem_and_integration_architecture_audit.md
```

Main conclusion:

```text
ADS project/domain/methodological semantics
    are durable product architecture

agent frameworks / MCP / A2A / AG-UI / runtime checkpointing
    are infrastructure and interoperability mechanisms
```

These should not be conflated.

New principles:

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

Treat MCP as a first-class candidate external tool/resource integration boundary, not as project memory or an internal application bus. Current 2026 MCP architecture has changed materially and new code should not depend on deprecated Roots, Sampling, or Logging behavior.

### A2A

Deferred until ADS actually needs independently deployed remote agent systems.

### AG-UI

Evaluate in the frontend spike as an adapter around ADS-owned interaction/run events. Do not make it the domain event model.

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

Leading hypothesis:

```text
React
TypeScript
Vite
TanStack Router
TanStack Query
TanStack Table v9
shadcn/ui source-distributed components
ADS-owned design tokens / visual language
Playwright
Vitest
```

This is not yet accepted as the final frontend stack.

Current evidence favors Vite over Next.js for the V1 shell because ADS is local-first, Python-backed, highly interactive, and has no demonstrated SEO/server-rendering requirement. The spike may reopen that decision if it exposes a missing capability.

Chart strategy remains open:

```text
ECharts
vs
Plotly
```

They will be compared on the same ADS analytical examples.

Tauri 2 remains a later desktop-packaging candidate after the normal browser shell and Python service boundary are stable.

The first frontend should be visually serious rather than a disposable dashboard. It should test Overview, Data, EDA, Decisions/History, methodological statuses, Question/Finding/Decision representations, run/activity state, one approval interaction, light/dark themes, loading/error/offline states, accessibility, responsive widths, and controlled visual regression screenshots.

---

## Retrieval/horizon track remains active

The agent/frontend audit changes sequencing but does not remove retrieval from the methodological brain.

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
AG-UI
frontend final stack
chart library
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

These are now attached to explicit requirements or planned spikes rather than being open-ended technology questions.

---

## Near-term execution order

Three active bounded tracks:

```text
A. GOVERNED ROUNDTRIP CLOSURE
   confirm corrected PostgreSQL 18 gate
   fix any remaining portability defect honestly
   remove temporary diagnostics
   close with dedicated checkpoint only on confirmed PASS

B. AGENT RUNTIME BAKEOFF
   implement Specification 005 representative workload
   begin single-agent first
   compare surviving runtimes against actual ADS requirements

C. FRONTEND PRODUCT SPIKE
   implement Specification 006 shell from typed deterministic mock state
   establish real design system and professional visual character
   test accessibility/visual states
   compare chart systems
   evaluate AG-UI mapping without domain coupling
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

docs/specifications/001_v1_sqlite_technical_architecture.md
docs/specifications/002_v1_persistence_tooling_standard.md
docs/specifications/003_v1_python_project_and_dependency_tooling.md
docs/specifications/004_v1_reusable_knowledge_interchange.md
docs/specifications/005_v1_agent_runtime_and_interoperability_bakeoff.md
docs/specifications/006_v1_frontend_architecture_and_visual_spike.md

docs/checkpoints/114_first_production_v1_persistence_vertical_slice_passed.md
docs/checkpoints/115_reusable_knowledge_interchange_contract_validated.md
docs/checkpoints/116_agentic_ecosystem_audit_and_frontend_track_started.md

docs/experiments/prototype_v0/FINAL_RESULTS.md
docs/CONTINUITY.md
```

## Current priority

**Close the corrected governed PostgreSQL round-trip honestly, then begin the Specification 005 agent-runtime bakeoff and Specification 006 professional frontend visual/technical spike as parallel bounded V1 tracks. Keep retrieval-quality work evidence-driven and do not introduce multi-agent, vector, or orchestration complexity before it earns its place.**
