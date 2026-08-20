# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources but does not replace them.  
**Last reviewed:** 2026-08-20

## Start here

For a new session or quick reconstruction:

```text
README.md
    project-level overview

docs/CURRENT_STATE.md
    present state and exact active priority

docs/KNOWLEDGE_MAP.md
    routing layer

docs/VISION.md
    system purpose and vision

docs/PRINCIPLES.md
    current principles

docs/DECISIONS.md
    accepted project-level decisions

docs/OPEN_QUESTIONS.md
    unresolved canonical questions

docs/DEVELOPMENT_METHOD.md
    development/preservation method

docs/CONTINUITY.md
    cross-session continuation procedure

docs/MAJOR_CHANGES.md
    selective structural history
```

Prototype V0 is complete and its final classification is **STRONG FALSIFICATION OF THE CURRENT P0 DESIGN**. The project is now implementing bounded V1 product slices across methodological knowledge, governed persistence, agent/runtime infrastructure, and the professional frontend.

---

## System purpose and long-term product vision

Primary sources:

```text
docs/VISION.md
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
```

Historical origin:

```text
docs/foundations/001_initial_vision_and_reasoning.md
docs/checkpoints/022_system_level_abstraction_and_reusable_reasoning_vision.md
```

Foundation 013 explains the LLM/system/human boundary. Foundation 017 makes the target product concrete as an interactive data-science workspace. Foundation 021 strengthens the interface requirement into a first-class modern, polished, visually excellent professional analytical product rather than an end-stage dashboard or chat shell.

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

The current design does not add a universal project `Assessment` object. Subject-specific criterion verdicts use the existing Question -> Evidence -> Finding -> Claim/Decision chain, with a structured criterion-Finding form where useful.

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

## Methodological-navigation brain and relevance architecture

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
    -> bounded methodological horizon
    -> explicit checks + flexible reasoning
    -> inspectable recommendation/requiredness
```

The full knowledge catalog should not be sent to the LLM on every reasoning call.

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
project objects referencing/influenced by exact knowledge revisions
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
internal representation != human-facing tree/workflow
```

Promoted principles:

```text
docs/PRINCIPLES.md, P-025 and P-026
```

Important design history:

```text
docs/checkpoints/101_five_example_reusable_knowledge_stress_test_completed.md
docs/checkpoints/102_candidate_conceptual_knowledge_representation_contract.md
docs/checkpoints/104_adversarial_review_of_candidate_knowledge_representation.md
docs/checkpoints/105_refined_representation_second_stress_test.md
```

---

## V1 implementation requirements

Primary source:

```text
docs/checkpoints/107_implementation_requirements_for_methodological_knowledge_subsystem.md
```

Checkpoint 107 derives 59 technology-neutral capabilities before architecture selection, including stable revisions, provenance, typed relations, tri-valued rules, semantic retrieval, project-state lookup, methodological-horizon construction, selective LLM context assembly, governance, integrity, backup, and portability.

---

## Accepted V1 persistence/retrieval architecture

Accepted decision and comparison:

```text
docs/DECISIONS.md, D-028
docs/checkpoints/108_v1_architecture_comparison_and_sqlite_centered_selection.md
docs/specifications/001_v1_sqlite_technical_architecture.md
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
    initial in-process exact semantic search

application rule evaluator
    predicate / ALL / ANY / NOT / TRUE / FALSE / UNKNOWN

selective context assembler

filesystem / Git / artifact storage
    source code and large artifacts outside SQLite
```

Explicit V1 non-selections unless evidence changes the requirement envelope:

```text
dedicated graph database
dedicated vector database/service
external generic rules engine
PostgreSQL server by default
ANN index
```

PostgreSQL + pgvector remains the preferred first migration family if later concurrency/shared-server/vector-scale needs exceed the SQLite envelope.

Architecture evidence:

```text
experiments/architecture_spikes/sqlite_v1_viability.py
experiments/architecture_spikes/V1_ARCHITECTURE_GATE_RESULT.md
docs/checkpoints/111_v1_technical_architecture_gate_passed_and_specification_001_promoted.md
```

FT-05 validates the retrieval architecture seam only. It does not validate production retrieval quality or embedding choice.

---

## Accepted implementation and Python tooling

Persistence:

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

Python project:

```text
docs/DECISIONS.md, D-030
docs/specifications/003_v1_python_project_and_dependency_tooling.md
```

Accepted:

```text
pyproject.toml
uv 0.12.5
committed cross-platform uv.lock
uv_build
src/ads_system
Python >=3.12
```

Evidence:

```text
docs/checkpoints/112_v1_persistence_tooling_selected_and_validated.md
docs/checkpoints/113_v1_python_project_tooling_validated.md
experiments/architecture_spikes/V1_PERSISTENCE_TOOLING_RESULT.md
experiments/architecture_spikes/V1_PYTHON_PROJECT_TOOLING_RESULT.md
```

---

## First production V1 persistence vertical slice

Primary milestone:

```text
docs/checkpoints/114_first_production_v1_persistence_vertical_slice_passed.md
experiments/architecture_spikes/V1_PRODUCTION_PERSISTENCE_SLICE_RESULT.md
```

Production package:

```text
src/ads_system/domain/
src/ads_system/application/
src/ads_system/infrastructure/persistence/
migrations/
tests/integration/
```

The same application/repository scenario passed on SQLite/Linux, SQLite/Windows, and PostgreSQL 18. It proves a project Finding pinned to Random Forest R1 remains pinned to R1 after R2 becomes current.

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

Key authority rule:

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

The current production bridge includes candidate import, explicit acceptance, accepted snapshot export, provenance, relation governance, collections, migration 0002, and historical project-revision pinning.

Current confirmed gate status at Checkpoint 116:

```text
SQLite
    PASS

first PostgreSQL 18 attempt
    FAIL
```

The PostgreSQL defect was not conceptual. One manually named migration constraint exceeded PostgreSQL's 63-character identifier limit.

Fix:

```text
ba6a92f83aac3a63ebfb7f97a4378c93fa28547b
Shorten interchange migration identifiers for PostgreSQL
```

Traceability improvement:

```text
a69b8859696fbd3b45124c257d085989d692a207
Make roundtrip gate status traceable to source commit
```

Do not treat this governed round-trip as closed until a corrected PostgreSQL PASS is persisted and confirmed.

Historical transition:

```text
docs/checkpoints/116_agentic_ecosystem_audit_and_frontend_track_started.md
```

---

## 2026 agentic ecosystem and runtime boundary

Primary research source:

```text
docs/research/001_2026_agentic_ecosystem_and_integration_architecture_audit.md
```

Current architecture conclusion:

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

Important current directions:

```text
MCP
    strong candidate external tool/resource integration boundary
    not internal project memory/application bus

A2A
    defer until independently deployed remote agents are required

AG-UI
    evaluate as frontend-agent transport adapter
    do not make it ADS domain event model

multi-agent
    do not adopt by default
    start with one principal reasoner + tools
```

Current 2026 MCP notes in the research memo include the new stateless core and deprecation of Roots, Sampling, and Logging, so older MCP assumptions should not be copied into V1.

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

Pydantic AI/Pydantic Graph remains a watchlist candidate.

The bakeoff tests actual ADS-shaped requirements rather than generic features:

```text
domain isolation
single-agent tools
MCP
human approval
durable resume
external ADS project-state authority
bounded context transparency
cancellation/timeouts
failure/retry
structured outputs
observability
test/provider substitution
```

A valid result is still to use simpler direct model calls if no framework earns its complexity.

---

## Professional frontend and product interface

Primary foundation:

```text
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
```

Candidate implementation/visual gate:

```text
docs/specifications/006_v1_frontend_architecture_and_visual_spike.md
```

Current leading hypothesis, not yet accepted:

```text
React
TypeScript
Vite
TanStack Router
TanStack Query
TanStack Table v9
shadcn/ui source-distributed components
ADS-owned design system
Playwright
Vitest
```

Current product requirement:

```text
modern
premium/professional
visually excellent
compact but calm analytical density
strong typography
high-quality light/dark modes
accessible
responsive at professional laptop/desktop widths
polished loading/empty/error/offline states
high-quality analytical visualizations
```

The frontend begins before backend completion using deterministic typed ADS mock state behind a replaceable data-source boundary.

Chart strategy remains under test:

```text
ECharts
vs
Plotly
```

Tauri is a later desktop-packaging candidate, not part of the first web shell.

---

## Earlier reusable-knowledge theory

Read for deeper design history:

```text
docs/foundations/006_knowledge_activation_and_open_world_reasoning.md
docs/foundations/007_reusable_knowledge_representation_and_composable_components.md
docs/foundations/008_knowledge_quality_generalization_and_evolution.md
```

Foundations 019 and 020 govern the current post-V0 interpretation.

---

## Project state, dependencies, and orchestration history

Broad theory:

```text
docs/foundations/004_project_state_dependency_and_state_driven_orchestration.md
```

Prototype V0 evidence:

```text
prototype_v0/src/ads_v0/p0.py
prototype_v0/src/ads_v0/p0_controller.py
prototype_v0/src/ads_v0/p0_schema.py
docs/experiments/prototype_v0/FINAL_RESULTS.md
```

Interpretation:

```text
broad dependency/state theory remains useful
    !=
P0's always-on representation is justified
```

---

## Epistemic integrity, admissibility, risk, and project constitution

Read:

```text
docs/foundations/002_epistemic_integrity_and_project_constitution.md
docs/foundations/003_admissibility_risk_and_assurance.md
docs/VISION.md
docs/PRINCIPLES.md
```

---

## Execution and observability separation

Read:

```text
docs/PRINCIPLES.md, P-022
docs/foundations/016_execution_observability_separation.md
```

Agent/runtime tracing should remain supplementary to ADS-owned project provenance and operational event semantics.

---

## Prototype V0 final result

Authoritative report:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
```

Final classification:

```text
STRONG FALSIFICATION OF THE CURRENT P0 DESIGN
```

Do not restart or tune P0 against the completed benchmark.

---

## Knowledge preservation and session continuity

Read:

```text
docs/DEVELOPMENT_METHOD.md
docs/CONTINUITY.md
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
docs/checkpoints/README.md
```

Current design session:

```text
02 - Methodological Brain & Knowledge Units
```

---

## Repository authority model

Default order when documents disagree:

```text
1. frozen/current specifications or contracts for their declared scope
2. current accepted decisions and canonical specifications
3. current vision/principles/current-state material
4. final experiment reports for their declared experiment scope
5. foundational design memos
6. checkpoints
7. raw historical material
```

---

## Exact next step

The active bounded sequence is now:

```text
1. close corrected governed PostgreSQL round-trip honestly
   -> confirm PASS or fix remaining portability defect
   -> remove temporary diagnostics
   -> checkpoint closure only after evidence

2. implement Specification 005 agent-runtime bakeoff
   -> one principal reasoner first
   -> compare existing runtime infrastructure against ADS workload
   -> no multi-agent architecture by default

3. implement Specification 006 frontend product spike
   -> real design system
   -> Overview / Data / EDA / Decisions-History
   -> methodological state UI
   -> approval/run interaction
   -> accessibility and visual regression
   -> ECharts vs Plotly comparison
   -> AG-UI mapping feasibility

4. resume retrieval-quality benchmark and lexical retrieval
   -> required hits / optional hits / critical omissions
   -> semantic retrieval comparison only after measurable baseline
```

The goal is now to build the smallest professional end-to-end product architecture in which each new layer has earned its complexity.