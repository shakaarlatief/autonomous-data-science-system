# Current State

**Checkpoint:** 112  
**Date:** 2026-08-20  
**Development stage:** Prototype V0 complete; product vision, project object model, methodological-navigation architecture, reusable-knowledge representation, implementation requirements, V1 architecture selection, accepted technical architecture, architecture falsification, and persistence-tooling selection are complete; the first production V1 persistence foundation is the active task  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Execution mode:** V1 persistence/retrieval architecture and persistence tooling are accepted and validated; broad product implementation remains deferred while the first production-quality persistence vertical slice is built and tested

## Active ChatGPT development context

```text
Design session: 02
ChatGPT project: Autonomous Data Science System
Session title: 02 - Methodological Brain & Knowledge Units
```

Repository artifacts remain authoritative across chats.

## Current product goal

The Autonomous Data Science System should be a professional interactive data-science environment that carries much of the methodological memory, project memory, option generation, process navigation, execution discipline, provenance, and reporting burden while preserving strong human inspection, discussion, override, editing, execution, and guidance.

Primary product sources:

```text
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
```

## Prototype V0 constraint

Prototype V0 strongly falsified the then-current P0 implementation strategy.

Key result:

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

Foundation 020 promotes the reusable-knowledge representation:

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

Promoted principles:

```text
P-025  Reusable knowledge identity/granularity is separate from reasoning function.
P-026  Static methodological relationships are separate from conditional guidance rules.
```

## Technology-neutral implementation requirements

Checkpoint 107 defines 59 requirements covering stable identity/revisions, component provenance, relation traversal, tri-valued rules, semantic retrieval, project-state lookup, methodological-horizon construction, exact revision references, governance, selective context assembly, backup, integrity, and portability.

Source:

```text
docs/checkpoints/107_implementation_requirements_for_methodological_knowledge_subsystem.md
```

## Accepted V1 architecture family

D-028 accepts a SQLite-centered local-first V1 architecture:

```text
SQLite operational store
    reusable knowledge metadata/state
    project metadata/state
    relations / rules / provenance / governance
    exact project-to-knowledge references
    execution-capability metadata

SQLite FTS5
    rebuildable lexical index

rebuildable embeddings
    initial in-process exact semantic retrieval

application-layer rule evaluator
selective LLM context assembly

filesystem / Git / artifact storage
    project code and large artifacts outside SQLite
```

PostgreSQL + pgvector remains the preferred first migration family if the SQLite envelope is exceeded.

Architecture comparison:

```text
docs/checkpoints/108_v1_architecture_comparison_and_sqlite_centered_selection.md
docs/DECISIONS.md, D-028
```

## Accepted V1 technical architecture

Specification 001 is the accepted V1 persistence/retrieval technical contract:

```text
docs/specifications/001_v1_sqlite_technical_architecture.md
```

The committed architecture gate passed:

```text
FT-01 through FT-11   PASS on SQLite
FT-12                 PASS on PostgreSQL 18
```

Evidence:

```text
experiments/architecture_spikes/V1_ARCHITECTURE_GATE_RESULT.md
experiments/architecture_spikes/v1_schema_spike.sql
experiments/architecture_spikes/v1_sqlite_architecture_falsification.py
experiments/architecture_spikes/v1_postgres_portability_spike.py
docs/checkpoints/111_v1_technical_architecture_gate_passed_and_specification_001_promoted.md
```

Important boundary:

```text
FT-05 validates the retrieval architecture seam only.
It does not validate the eventual embedding model, reranker,
retrieval recall, or fusion algorithm.
```

## Accepted V1 persistence tooling

D-029 and Specification 002 now select:

```text
SQLAlchemy Core 2.0 stable series
    primary V1 relational schema/query/transaction toolkit

Alembic 1.x
    authoritative production schema-migration history

SQLAlchemy ORM
    not the primary V1 domain/persistence model

raw DBAPI / driver SQL
    narrow adapter-specific use only
```

Current accepted tooling specification:

```text
docs/specifications/002_v1_persistence_tooling_standard.md
```

Selection rationale and research:

```text
docs/checkpoints/112_v1_persistence_tooling_selected_and_validated.md
```

Dual-backend evidence:

```text
experiments/architecture_spikes/tooling_sqlalchemy_core_alembic_spike.py
experiments/architecture_spikes/V1_PERSISTENCE_TOOLING_RESULT.md
.github/workflows/v1-persistence-tooling-spike.yml
```

The CI spike passed on SQLite and PostgreSQL 18:

```text
SQLALCHEMY_CORE=PASS
ALEMBIC_MIGRATION=PASS
PORTABLE_UUID=PASS
TRANSACTION_BOUNDARY=PASS
DIALECT_SPECIFIC_DDL_ISOLATION=PASS
TOOLING_SPIKE_RESULT=PASS
```

Important implementation consequences:

```text
Core MetaData describes the current relational schema.
Alembic revisions are the authoritative production schema-evolution path.
Autogenerate may assist but every migration requires human/code review.
Constraint naming is mandatory.
SQLite STRICT migrations must preserve STRICT explicitly during table recreation.
SQLite UUIDs use canonical hyphenated TEXT through a dialect-aware adapter;
PostgreSQL uses native UUID.
Backend-specific PRAGMAs/FTS remain inside persistence/index adapters or migrations.
```

SQLAlchemy 2.1 remains beta at this checkpoint, so V1 stays on the stable 2.0 API line until an explicit later review.

## Current implementation stage

The architecture family, technical seam, SQL toolkit, and migration framework are now selected with executable SQLite/PostgreSQL evidence.

Do **not** implement the entire product schema or frontend at once.

The active task is the first **production-quality V1 persistence vertical slice** behind Specifications 001 and 002.

It should define and implement the smallest coherent durable core that proves the real application boundary:

```text
system schema/migration metadata
knowledge node / asset / immutable revision / governance
knowledge component / relation / rule
project identity + the minimum epistemic objects required by the slice
exact project -> knowledge revision references
repository ports + application UnitOfWork boundary
SQLite connection factory/adapter contract
first Alembic base migration
SQLite integration tests
PostgreSQL portability CI
```

The implementation should remain bounded enough that architecture defects are cheap to correct.

## Still intentionally unselected

```text
project package/build manager and lockfile mechanism
complete production schema for every Foundation 018 object
embedding model/provider
lexical/semantic fusion algorithm
reranker
LLM provider
frontend/API framework
job queue
artifact-storage backend
cloud deployment
async persistence
```

These should be selected only when their requirements become concrete.

## Continuity status

Active session:

```text
Design session: 02
ChatGPT project: Autonomous Data Science System
Session title: 02 - Methodological Brain & Knowledge Units
```

Current preservation contract:

```text
docs/DEVELOPMENT_METHOD.md
docs/CONTINUITY.md
docs/checkpoints/README.md
```

## Minimum reading for continuation

```text
README.md
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/DECISIONS.md
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
docs/checkpoints/107_implementation_requirements_for_methodological_knowledge_subsystem.md
docs/checkpoints/108_v1_architecture_comparison_and_sqlite_centered_selection.md
docs/specifications/001_v1_sqlite_technical_architecture.md
docs/specifications/002_v1_persistence_tooling_standard.md
docs/checkpoints/112_v1_persistence_tooling_selected_and_validated.md
experiments/architecture_spikes/V1_ARCHITECTURE_GATE_RESULT.md
experiments/architecture_spikes/V1_PERSISTENCE_TOOLING_RESULT.md
docs/experiments/prototype_v0/FINAL_RESULTS.md
docs/CONTINUITY.md
```

## Current priority

**Implement the first production V1 persistence vertical slice using SQLAlchemy Core + Alembic behind Specifications 001/002, with SQLite as the V1 operational store and retained PostgreSQL portability tests. Keep the slice small enough to falsify remaining implementation assumptions before broad product construction.**
