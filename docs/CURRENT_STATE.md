# Current State

**Checkpoint:** 114  
**Date:** 2026-08-20  
**Development stage:** Prototype V0 complete; product vision, project object model, methodological-navigation architecture, reusable-knowledge representation, V1 architecture, persistence tooling, Python project tooling, and the first production persistence vertical slice are implemented/validated to their current scope; representative knowledge interchange and retrieval-quality design are now the active boundary  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Execution mode:** The first real V1 persistence path is production code and has passed SQLite/Linux/Windows/PostgreSQL integration gates; broad product implementation remains deliberately bounded while real methodological knowledge and retrieval are made testable

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

D-029 and Specification 002 select:

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

Sources:

```text
docs/specifications/002_v1_persistence_tooling_standard.md
docs/checkpoints/112_v1_persistence_tooling_selected_and_validated.md
experiments/architecture_spikes/V1_PERSISTENCE_TOOLING_RESULT.md
```

The dual-backend tooling gate passed on SQLite and PostgreSQL 18.

## Accepted V1 Python project/dependency tooling

D-030 and Specification 003 select:

```text
standards-based pyproject.toml
uv 0.12.5
committed cross-platform uv.lock
uv_build for the current pure-Python package
src/ads_system source layout
Python >=3.12
```

The committed CI gate passed on Linux and Windows under Python 3.12, 3.13, and 3.14 and verified locked synchronization, tests, package building, and PEP 751 `pylock.toml` export.

Sources:

```text
docs/specifications/003_v1_python_project_and_dependency_tooling.md
docs/checkpoints/113_v1_python_project_tooling_validated.md
experiments/architecture_spikes/V1_PYTHON_PROJECT_TOOLING_RESULT.md
```

## First production V1 persistence vertical slice

Checkpoint 114 records the first real production application path behind Specifications 001-003.

Implemented package structure:

```text
src/ads_system/domain/
src/ads_system/application/
src/ads_system/infrastructure/persistence/
migrations/
tests/integration/
```

The bounded slice implements and tests:

```text
stable KnowledgeAsset identity
immutable KnowledgeRevision history
governance/current accepted revision
KnowledgeComponent tied to an exact parent asset revision
KnowledgeRelation + relation revision/current pointer
Conditional KnowledgeRule owned by an exact knowledge revision
Project + Finding persistence
exact Finding -> historical knowledge revision references
SQLAlchemy UnitOfWork transaction boundary
real Alembic base migration
```

The production integration gate passed:

```text
SQLite / Ubuntu        PASS
SQLite / Windows       PASS
PostgreSQL 18          PASS
```

The scenario explicitly proves that after Random Forest R2 is published, a historical project Finding that used R1 still points to and reconstructs R1. It also verifies relational rejection of a cross-project reference mismatch.

Evidence:

```text
docs/checkpoints/114_first_production_v1_persistence_vertical_slice_passed.md
experiments/architecture_spikes/V1_PRODUCTION_PERSISTENCE_SLICE_RESULT.md
.github/workflows/v1-persistence-vertical-slice.yml
migrations/versions/0001_v1_persistence_core.py
tests/integration/test_persistence_vertical_slice.py
```

This is evidence that the accepted architecture can support its central history/provenance semantics in production code. It is not evidence that the full methodological brain is implemented.

## Current implementation stage

The persistence foundation has now crossed from architecture/spike work into a validated production vertical slice.

Do **not** respond by materializing the entire future schema or choosing an embedding model from intuition.

The next boundary is to connect the persistence substrate to representative reusable methodological knowledge and make retrieval quality measurable.

Preferred sequence:

```text
1. define a deterministic human-readable knowledge interchange/authoring contract;
2. encode a small representative real knowledge corpus from the methodological examples already studied;
3. import/export that corpus through the production revision/governance path;
4. define retrieval-quality fixtures, including required hits and unacceptable omissions;
5. implement production lexical retrieval;
6. evaluate semantic-retrieval candidates before selecting an embedding model/reranker;
7. build the first real MethodologicalHorizon path only after retrieval behavior is measurable.
```

This should preserve the distinction:

```text
operational database authority
    !=
human-readable deterministic representation
    !=
derived lexical/semantic indexes
```

## Still intentionally unselected or incomplete

```text
complete production schema for every Foundation 018 object
full Foundation 020 knowledge-schema coverage
knowledge interchange/authoring format
UUIDv7 generator implementation
production FTS/index implementation
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
docs/specifications/003_v1_python_project_and_dependency_tooling.md
docs/checkpoints/114_first_production_v1_persistence_vertical_slice_passed.md
experiments/architecture_spikes/V1_ARCHITECTURE_GATE_RESULT.md
experiments/architecture_spikes/V1_PERSISTENCE_TOOLING_RESULT.md
experiments/architecture_spikes/V1_PYTHON_PROJECT_TOOLING_RESULT.md
experiments/architecture_spikes/V1_PRODUCTION_PERSISTENCE_SLICE_RESULT.md
docs/experiments/prototype_v0/FINAL_RESULTS.md
docs/CONTINUITY.md
```

## Current priority

**Define the deterministic reusable-knowledge interchange/authoring contract and a small representative real methodological corpus, then use that corpus to create the first retrieval-quality benchmark before selecting a production embedding model or broader methodological-horizon implementation.**
