# Current State

**Checkpoint:** 109  
**Date:** 2026-08-20  
**Development stage:** Prototype V0 complete; product vision, project object model, methodological-navigation architecture, reusable-knowledge representation, implementation requirements, V1 persistence/retrieval architecture, and candidate V1 technical architecture specification completed; narrow architecture falsification is the active task  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Execution mode:** Prototype V0 is closed; broad V1 implementation is not yet authorized

## Active ChatGPT development context

```text
Design session: 02
ChatGPT project: Autonomous Data Science System
Session title: 02 - Methodological Brain & Knowledge Units
```

This is provenance/navigation metadata. Repository artifacts remain authoritative across chats.

## Current product goal

The Autonomous Data Science System should be a professional interactive data-science environment that carries much of the methodological memory, project memory, option generation, process navigation, execution discipline, provenance, and reporting burden while preserving strong human inspection, discussion, override, editing, execution, and guidance.

Primary product sources:

```text
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
```

## Prototype V0 constraint

Prototype V0 strongly falsified the current P0 implementation strategy on the churn benchmark family.

Key result:

```text
B1 targeted mean: 1.73
P0 targeted mean: 1.78
incremental gain: +0.05

B1 completed within budget: 10/10
P0 completed within budget: 3/10

P0/B1 median token ratio: 2.160
```

The broader system vision remains open. The strongest scaling lesson remains:

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

Important project distinctions include:

```text
Investigation != Run
Evidence != Finding
Finding != Claim
Claim != Decision
current state != event history
persisted object != derived recommendation
workspace section != fundamental object
```

The system does not currently add a universal top-level `Assessment` object. Subject-specific criterion verdicts should use:

```text
Question -> Evidence -> Finding -> Claim/Decision
```

with a structured criterion-Finding form where useful.

Different project objects retain different lifecycle semantics. The candidate V1 technical architecture therefore does **not** force all project state into one generic JSON object or one universal revision model.

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

The LLM should receive a selective task-specific projection, not the entire persistent knowledge/project state.

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

Checkpoint 107 defines 59 implementation requirements covering:

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

## Accepted V1 persistence/retrieval architecture

D-028 accepts a SQLite-centered local-first V1 architecture.

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
    minimal predicate / ALL / ANY / NOT / UNKNOWN semantics

selective LLM context assembly

filesystem / Git / artifact storage
    project code and large artifacts outside SQLite
```

Not selected for V1 without new evidence:

```text
dedicated graph database
dedicated vector database/service
external generic rules engine
PostgreSQL server by default
ANN index
```

PostgreSQL + pgvector is the preferred first migration family if the SQLite envelope is exceeded.

Architecture comparison and initial scale spike:

```text
docs/checkpoints/108_v1_architecture_comparison_and_sqlite_centered_selection.md
experiments/architecture_spikes/sqlite_v1_viability.py
docs/DECISIONS.md, D-028
```

## Candidate V1 technical architecture specification

The first implementation-level technical contract is now preserved at:

```text
docs/specifications/001_v1_sqlite_technical_architecture.md
```

Status:

```text
candidate v0.1
frozen for narrow architecture falsification
not yet broad implementation authority
```

The specification is explicitly designed to avoid foreseeable expensive rearchitecture.

Key directions include:

```text
one SQLite operational database with logical sys_/kg_/prj_/exec_/idx_ modules
application/domain persistence ports around SQLite
application-generated UUID durable identities, UUIDv7 preferred
UTC domain timestamps independent of SQLite date semantics
STRICT authoritative tables where practical
relational structure for important identities/history/references
validated/versioned JSON only as a bounded flexible payload
immutable accepted knowledge content revisions
separate governance state/events from immutable content
technical identity supertypes only where they improve FK integrity
project objects retain type-specific lifecycle semantics
exact project references to knowledge revisions
minimal declarative rule AST; no SQL/code stored as rules
FTS5 and embeddings are rebuildable derived state
HorizonBuilder and ContextAssembler are application services
one application-owned write path
short transactions; never hold DB writes across LLM/network work
foreign_keys=ON on every SQLite connection
WAL + synchronous=FULL default durability profile
ordered migrations
online backup + verified restore
human-readable deterministic knowledge export
explicit PostgreSQL portability contract
```

A central portability requirement is:

```text
SQLite -> PostgreSQL
exact vector search -> pgvector/ANN/provider
bounded relational traversal -> specialized graph projection if later justified
```

should be infrastructure evolution behind stable application ports, not a redesign of methodological meaning, project semantics, rule logic, horizon construction, or user workflows.

Historical checkpoint:

```text
docs/checkpoints/109_v1_technical_architecture_specified_and_falsification_gate_defined.md
```

## Architecture falsification gate

Broad V1 implementation remains blocked until a narrow spike addresses the specification's tests:

```text
FT-01  identity/revision historical integrity
FT-02  component/relation integrity
FT-03  Missing Data rule reconstruction
FT-04  criterion-Finding chain
FT-05  retrieval/horizon coverage fixture
FT-06  missing/stale embedding behavior
FT-07  context-budget enforcement
FT-08  transaction atomicity/failure injection
FT-09  WAL reader/writer behavior
FT-10  backup/restore/integrity
FT-11  derived-index rebuild
FT-12  PostgreSQL portability review/spike
```

The spike should use representative knowledge from Histogram, Missing Data, Temporal Validation, Random Forest, Prediction-Time Feature Eligibility, and Class Imbalance rather than database-only toy rows.

A failing test should trigger the smallest evidence-supported architectural correction. Failure of one retrieval/index component must not automatically imply replacing the authoritative database.

## Still intentionally unselected

```text
exact full DDL
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

These should be selected only when the next implementation layer makes their requirements concrete.

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
docs/checkpoints/109_v1_technical_architecture_specified_and_falsification_gate_defined.md
docs/experiments/prototype_v0/FINAL_RESULTS.md
docs/CONTINUITY.md
```

## Current priority

**Implement the narrow V1 architecture falsification spike for Specification 001. Do not begin broad V1 product implementation until the gate has been evaluated.**
