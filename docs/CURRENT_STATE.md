# Current State

**Checkpoint:** 111  
**Date:** 2026-08-20  
**Development stage:** Prototype V0 complete; product vision, project object model, methodological-navigation architecture, reusable-knowledge representation, implementation requirements, V1 architecture selection, technical architecture specification, and architecture falsification gate completed; bounded V1 implementation-contract/tooling design is the active task  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Execution mode:** V1 persistence/retrieval architecture is accepted and validated; broad product implementation remains deferred while the first bounded implementation contract/tooling is selected

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

Prototype V0 strongly falsified the then-current P0 implementation strategy on the churn benchmark family.

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

## Project object model

Foundation 018 separates:

```text
OBJECTS
RELATIONS
EVENTS
VIEWS
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

The design does not add a universal top-level `Assessment` object. Subject-specific criterion verdicts use:

```text
Question -> Evidence -> Finding -> Claim/Decision
```

with a structured criterion-Finding form where useful.

Project objects retain type-specific lifecycle semantics rather than being collapsed into one generic JSON/revision object.

## Methodological-navigation brain

Foundation 019 governs the methodological horizon and staged relevance model:

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
    -> required / recommended / relevant / not now
```

The LLM receives a selective task-specific projection, not the entire persistent state.

## Promoted reusable methodological-knowledge representation

Foundation 020 is the promoted conceptual representation source:

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

Durable distinctions include:

```text
intrinsic knowledge kind != reasoning function
asset != component != narrative facet
static relation != conditional rule
retrieval cue != applicability != required context != relevance
methodological knowledge != execution implementation
global knowledge != project-specific state
internal representation != human-facing decision tree/workspace
```

Promoted principles:

```text
P-025  Reusable knowledge identity/granularity is separate from reasoning function.
P-026  Static methodological relationships are separate from conditional guidance rules.
```

## Technology-neutral implementation requirements

Checkpoint 107 defines 59 requirements covering:

```text
stable identity and recoverable revisions
component provenance
typed relation lookup / bounded traversal
TRUE/FALSE/UNKNOWN rules
semantic candidate retrieval
retrieval/applicability/context separation
methodological-horizon construction
project-state lookup
exact project-to-knowledge revision references
provenance/governance
selective LLM context assembly
human inspectability
backup/integrity/portability
```

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

Not selected without new evidence:

```text
dedicated graph database
dedicated vector database/service
external generic rules engine
PostgreSQL server by default
ANN index
```

PostgreSQL + pgvector remains the preferred first migration family if the SQLite envelope is exceeded.

Architecture comparison:

```text
docs/checkpoints/108_v1_architecture_comparison_and_sqlite_centered_selection.md
docs/DECISIONS.md, D-028
```

## Accepted V1 technical architecture

Specification 001 is now the accepted V1 technical contract:

```text
docs/specifications/001_v1_sqlite_technical_architecture.md
```

Status:

```text
Accepted V1 technical specification v1.0
```

Key technical boundaries:

```text
one SQLite operational DB with logical sys_/kg_/prj_/exec_/idx_ modules
SQLite hidden behind application/domain persistence ports
application-generated UUID durable identities, UUIDv7 preferred
UTC domain timestamps
STRICT core tables where practical
explicit relational integrity for important identity/history/reference semantics
bounded validated/versioned JSON for flexible payloads
immutable accepted knowledge content revisions
separate governance state/history
project objects retain type-specific lifecycle semantics
exact project -> knowledge revision references
minimal declarative tri-valued rule AST; no stored executable code
FTS5 and embeddings as rebuildable derived state
HorizonBuilder and ContextAssembler as application services
one application-owned write path
short transactions only
foreign_keys=ON, WAL, synchronous=FULL baseline
ordered migrations
online backup + verified restore
human-readable deterministic knowledge export
explicit PostgreSQL portability contract
```

The architecture is deliberately designed so foreseeable infrastructure changes are localized:

```text
SQLite -> PostgreSQL
exact semantic search -> pgvector / ANN / another provider
bounded relation traversal -> specialized graph projection/provider if later justified
```

without rewriting methodological semantics, project-object meaning, rule semantics, horizon logic, or user-facing workflow concepts.

## Architecture falsification evidence

The committed CI gate passed all architecture tests:

```text
FT-01  PASS  historical knowledge revision integrity
FT-02  PASS  component/relation integrity
FT-03  PASS  Missing Data tri-valued rule reconstruction
FT-04  PASS  criterion-Finding chain
FT-05  PASS_ARCHITECTURE_ONLY  bounded hybrid retrieval path
FT-06  PASS  missing/stale embedding behavior
FT-07  PASS  context-budget enforcement
FT-08  PASS  transaction failure injection
FT-09  PASS  WAL reader/writer behavior
FT-10  PASS  backup/restore/integrity
FT-11  PASS  derived-index rebuild
FT-12  PASS  PostgreSQL 18 portability mapping
```

Evidence:

```text
experiments/architecture_spikes/V1_ARCHITECTURE_GATE_RESULT.md
experiments/architecture_spikes/v1_schema_spike.sql
experiments/architecture_spikes/v1_sqlite_architecture_falsification.py
experiments/architecture_spikes/v1_postgres_portability_spike.py
docs/checkpoints/109_v1_technical_architecture_specified_and_falsification_gate_defined.md
docs/checkpoints/110_preliminary_v1_sqlite_architecture_spike_passes_and_postgres_gate_pending.md
docs/checkpoints/111_v1_technical_architecture_gate_passed_and_specification_001_promoted.md
```

Important boundary:

```text
FT-05 does not validate the eventual production embedding model,
retrieval recall, fusion algorithm, or reranker.
```

Those remain separate empirical questions behind replaceable retrieval interfaces.

## Defect learned during architecture testing

The first spike attempted to enforce project-scoped uniqueness using a SQLite subquery expression index. SQLite rejected that construct.

The accepted correction is more professional and portable:

```text
carry project_id explicitly where project-scoped subtype integrity needs it
    +
composite foreign key back to the project entity identity
    +
ordinary UNIQUE(project_id, semantic_key)
```

The relation current-revision pointer is likewise constrained to a revision belonging to the same relation through a composite foreign key.

These corrections are now incorporated into Specification 001 v1.0.

## Current design/implementation stage

Architecture-family selection and architecture-seam validation are complete.

Do **not** jump directly to the full frontend/autonomous product.

The active task is to define the **bounded V1 persistence/retrieval implementation contract and tooling** underneath Specification 001.

Determine:

```text
1. SQL access / repository implementation approach;
2. schema migration implementation approach;
3. reviewed production migration/DDL organization;
4. typed domain/repository interfaces and UnitOfWork boundary;
5. UUIDv7 implementation choice;
6. deterministic export/import representation;
7. first real retrieval-quality benchmark before embedding-model selection;
8. retained SQLite + PostgreSQL architecture tests in CI.
```

The selection should optimize long-term maintainability and portability, not merely fastest prototype coding.

## Still intentionally unselected

```text
production full DDL
ORM / SQL toolkit
migration library
embedding model/provider
lexical/semantic fusion algorithm
reranker
LLM provider
frontend/API framework
job queue
artifact-storage backend
cloud deployment
```

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
docs/checkpoints/111_v1_technical_architecture_gate_passed_and_specification_001_promoted.md
experiments/architecture_spikes/V1_ARCHITECTURE_GATE_RESULT.md
docs/experiments/prototype_v0/FINAL_RESULTS.md
docs/CONTINUITY.md
```

## Current priority

**Select and specify the bounded V1 persistence/retrieval implementation approach and tooling under Specification 001, preserving the validated migration seams. Do not begin broad product implementation yet.**
