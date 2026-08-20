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

Prototype V0 is complete and its final classification is **STRONG FALSIFICATION OF THE CURRENT P0 DESIGN**. The project is now in V1 architecture/tooling design.

---

## System purpose and long-term vision

Primary sources:

```text
docs/VISION.md
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
```

Historical origin:

```text
docs/foundations/001_initial_vision_and_reasoning.md
docs/checkpoints/022_system_level_abstraction_and_reusable_reasoning_vision.md
```

Foundation 013 explains the LLM/system/human boundary. Foundation 017 makes the target product concrete as a professional interactive data-science workspace rather than an upload-to-final-answer black box.

---

## Project object model and professional developer workflow

Primary source:

```text
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
```

Important distinctions include:

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

Checkpoint 107 derives the technology-neutral capabilities required before architecture selection, including stable revisions, component provenance, typed relations, tri-valued rules, semantic retrieval, project-state lookup, methodological-horizon construction, selective LLM context assembly, governance, integrity, backup, and portability.

---

## Accepted V1 persistence/retrieval architecture

Accepted decision and comparison:

```text
docs/DECISIONS.md, D-028
docs/checkpoints/108_v1_architecture_comparison_and_sqlite_centered_selection.md
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

Explicit V1 non-selections unless later evidence changes the requirement envelope:

```text
dedicated graph database
dedicated vector database/service
external generic rules engine
PostgreSQL server by default
ANN index
```

PostgreSQL + pgvector is the preferred first migration family if later concurrency/shared-server/vector-scale needs exceed the SQLite envelope.

Initial architecture scale spike:

```text
experiments/architecture_spikes/sqlite_v1_viability.py
```

---

## Accepted V1 technical architecture specification

**Read first for current V1 persistence/retrieval implementation work:**

```text
docs/specifications/001_v1_sqlite_technical_architecture.md
```

Status:

```text
Accepted V1 technical specification v1.0
```

It defines the migration-safe implementation boundaries beneath D-028, including:

```text
application/domain persistence ports around SQLite
one operational DB with logical sys_/kg_/prj_/exec_/idx_ modules
application-generated durable UUIDs, UUIDv7 preferred
UTC domain timestamps
STRICT authoritative tables where practical
explicit relational integrity + bounded validated JSON
immutable accepted knowledge content revisions
separate governance state/history
project-type-specific lifecycle semantics
exact project -> knowledge revision references
minimal declarative rule AST; no executable stored code
FTS5 and embeddings as rebuildable derived state
HorizonBuilder and ContextAssembler application services
one controlled write path + short transactions
foreign_keys=ON / WAL / synchronous=FULL baseline
ordered migrations
online backup + verified restore
human-readable deterministic knowledge export
explicit PostgreSQL migration contract
```

The contract is intentionally structured so foreseeable infrastructure evolution remains bounded:

```text
SQLite -> PostgreSQL
exact semantic retrieval -> pgvector / ANN / other SemanticIndex provider
bounded relational traversal -> specialized RelationQuery projection/provider
```

without redefining methodological knowledge, project objects, rules, horizon semantics, or user workflows.

---

## V1 technical-architecture falsification evidence

Historical design/validation checkpoints:

```text
docs/checkpoints/109_v1_technical_architecture_specified_and_falsification_gate_defined.md
docs/checkpoints/110_preliminary_v1_sqlite_architecture_spike_passes_and_postgres_gate_pending.md
docs/checkpoints/111_v1_technical_architecture_gate_passed_and_specification_001_promoted.md
```

Reproducible gate artifacts:

```text
experiments/architecture_spikes/v1_schema_spike.sql
experiments/architecture_spikes/v1_sqlite_architecture_falsification.py
experiments/architecture_spikes/v1_postgres_portability_spike.py
experiments/architecture_spikes/V1_ARCHITECTURE_GATE_RESULT.md
```

Gate result:

```text
FT-01 through FT-11   PASS on SQLite architecture harness
FT-12                 PASS on PostgreSQL 18 portability harness
```

Important boundary:

```text
FT-05 = PASS_ARCHITECTURE_ONLY
```

It validates the replaceable retrieval/index/horizon seam with a deterministic toy semantic provider. It does not validate the production embedding model, retrieval recall, fusion algorithm, or reranker.


---

## Accepted V1 implementation and Python project tooling

Persistence tooling:

```text
docs/DECISIONS.md, D-029
docs/specifications/002_v1_persistence_tooling_standard.md
docs/checkpoints/112_v1_persistence_tooling_selected_and_validated.md
experiments/architecture_spikes/V1_PERSISTENCE_TOOLING_RESULT.md
```

Accepted direction:

```text
SQLAlchemy Core 2.0 stable series
Alembic 1.x
SQLAlchemy ORM not the primary domain/persistence model
raw DBAPI only for narrow backend-specific adapter behavior
```

Python project/dependency/build tooling:

```text
docs/DECISIONS.md, D-030
docs/specifications/003_v1_python_project_and_dependency_tooling.md
docs/checkpoints/113_v1_python_project_tooling_validated.md
pyproject.toml
uv.lock
experiments/architecture_spikes/V1_PYTHON_PROJECT_TOOLING_RESULT.md
```

Accepted direction:

```text
standards-based pyproject.toml
uv 0.12.5
committed cross-platform uv.lock
uv_build for the current pure-Python package
src/ads_system source layout
Python >=3.12, tested on 3.12/3.13/3.14 on Linux + Windows
```

The persistence and packaging tools are implementation mechanisms behind the already-accepted architecture; they do not redefine the methodological/domain object model.

---

## Earlier reusable-knowledge theory

Read when deeper rationale/history is needed:

```text
docs/foundations/006_knowledge_activation_and_open_world_reasoning.md
docs/foundations/007_reusable_knowledge_representation_and_composable_components.md
docs/foundations/008_knowledge_quality_generalization_and_evolution.md
```

Foundations 019 and 020 govern the current promoted post-V0 interpretation.

---

## Project state, dependencies, and orchestration

Broad theory:

```text
docs/foundations/004_project_state_dependency_and_state_driven_orchestration.md
```

Prototype V0 implementation/evidence:

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

## Project initialization

Read:

```text
docs/foundations/005_project_initialization_and_universal_bootstrap.md
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
```

---

## System evaluation and behavioral regression

Read:

```text
docs/foundations/009_behavioral_reasoning_regression_and_system_evaluation.md
docs/experiments/prototype_v0/FINAL_RESULTS.md
```

---

## Prototype V0 final result

Authoritative report:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
```

Frozen protocol:

```text
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
```

Final classification:

```text
STRONG FALSIFICATION OF THE CURRENT P0 DESIGN
```

Do not restart/tune P0 against the completed benchmark.

---

## Execution and observability separation

Read:

```text
docs/PRINCIPLES.md, P-022
docs/foundations/016_execution_observability_separation.md
```

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

Implement the **first production-quality V1 persistence vertical slice** behind Specifications 001-003.

The smallest coherent slice should exercise:

```text
stable knowledge identity + immutable accepted revision
knowledge governance/current pointer
component / relation / conditional-rule storage
project identity and minimal epistemic state
exact project -> knowledge revision reference
repository ports and UnitOfWork
Alembic base migration
SQLite integration tests
PostgreSQL portability CI
```

Do not materialize every Foundation 018 object or build the full frontend/autonomous workflow before this first real persistence path has been validated.
