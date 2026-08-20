# Current State

**Checkpoint:** 108  
**Date:** 2026-08-20  
**Development stage:** Prototype V0 complete; product vision, project object model, methodological-navigation architecture, reusable-knowledge representation, implementation requirements, and V1 persistence/retrieval architecture selected; V1 technical architecture specification is the active task  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Execution mode:** Prototype V0 is closed; no further B0/B1/P0 treatment or V0 semantic-judge inference is authorized

## Active ChatGPT development context

```text
Design session: 02
ChatGPT project: Autonomous Data Science System
Session title: 02 - Methodological Brain & Knowledge Units
```

This is interaction/provenance metadata. Repository artifacts remain authoritative for reconstruction across chats.

## Current project goal

The Autonomous Data Science System aims to create the best defensible data-science process for a project's objectives, constraints, deliverables, and desired human involvement.

The intended product is a professional interactive data-science environment, not an upload-to-final-answer black box. The system should carry much of the methodological memory, project memory, option generation, process navigation, execution discipline, provenance, and reporting burden while keeping the user able to inspect, discuss, select, override, edit, run, and guide the work.

Primary product sources:

```text
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
```

## Prototype V0 constraint

Prototype V0 strongly falsified the current P0 implementation strategy on the churn benchmark family.

Central result:

```text
B1 targeted mean: 1.73
P0 targeted mean: 1.78
incremental P0 gain: +0.05

B1 completed within budget: 10/10
P0 completed within budget: 3/10

P0/B1 median token ratio: 2.160
```

The broader system vision remains open. The strongest scaling lesson is:

```text
what the SYSTEM should remember
    !=
what the LLM should receive on every reasoning call
```

Do not carry forward P0's large always-on state/context representation unchanged.

Authoritative evidence:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
```

## Project object model and professional workflow

The product model separates:

```text
OBJECTS
RELATIONS
EVENTS
VIEWS
```

Candidate project objects include:

```text
Project / IntentItem
Artifact / Dataset / Variable
Question / Assumption / Finding / Claim
Proposal / Investigation / Run / Evidence / Decision
Report / ReportSection
Event / Relation
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

The current design does not add a universal top-level `Assessment` object. Subject-specific methodological verdicts should use the existing Question -> Evidence -> Finding -> Claim/Decision chain, with a structured criterion-Finding form where useful.

The system should complement VS Code rather than replace it. Generated consequential project code should remain independently runnable and professionally maintainable.

Primary source:

```text
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
```

## Methodological-navigation brain

Foundation 019 governs the relevance architecture.

The methodological brain is broader than a method catalog and may contain methods, question templates, decision frameworks, hard rules, failure modes, investigation patterns, interpretation knowledge, and follow-up/dependency knowledge.

Relevance progression:

```text
KNOWN
    -> APPLICABLE
    -> RELEVANT
    -> RECOMMENDED
    -> REQUIRED / BLOCKING
```

The key scaling abstraction is the **methodological horizon**:

```text
large global knowledge base
    -> project-specific retrieval/filtering
    -> small current methodological horizon
    -> explicit checks + flexible reasoning
    -> required / recommended / relevant / not now
```

Primary source:

```text
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
```

## Promoted reusable methodological-knowledge representation

Foundation 020 is the promoted conceptual representation source.

Current architecture:

```text
KnowledgeAsset
    stable identity + revision identity
    intrinsic kind
    optional reasoning functions
    retrieval/applicability/context structures

KnowledgeComponent
    stably identifiable sub-knowledge when needed

NarrativeFacet
    non-addressable explanatory content

KnowledgeRelation
    stable semantic relationship

Conditional KnowledgeRule
    guarded methodological implication
    standalone or component

KnowledgeCollection
    organizational/navigation grouping

Project object model
    references / instantiates / is constrained or informed by
    global knowledge revisions without one universal KnowledgeInstance

Criterion Finding
    structured project Finding form for subject-specific verdicts

ExecutionCapability
    separate implementation bridge

Views
    derived navigation and explanation over knowledge + project state
```

Durable separations:

```text
intrinsic knowledge kind != reasoning function
asset != component != narrative facet
static semantic relation != conditional methodological rule
retrieval cue != applicability predicate != context requirement != project relevance
methodological knowledge != execution implementation
global knowledge != project-specific state
internal representation != human-facing decision tree/workspace view
```

Primary source:

```text
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
```

Promoted representation principles:

```text
P-025  Reusable knowledge identity and granularity should be separate from reasoning function.
P-026  Static methodological relationships and conditional guidance rules should remain distinct.
```

## Implementation requirements completed

Checkpoint 107 derived the technology-neutral requirements that architecture candidates must satisfy before technology selection.

Important V1 requirements include:

```text
stable asset + revision identity
recoverable knowledge history
component-level provenance where required
typed relation lookup and bounded traversal
minimal TRUE / FALSE / UNKNOWN conditional rules
high-recall semantic candidate retrieval
explicit retrieval/applicability/context separation
bounded methodological-horizon construction
project-state lookup for Definitions/Questions/Findings/etc.
selective, budgeted LLM context assembly
human-readable knowledge review/export
single-user/local practicality
large artifacts outside the metadata store
```

Source:

```text
docs/checkpoints/107_implementation_requirements_for_methodological_knowledge_subsystem.md
```

## Selected V1 persistence/retrieval architecture

Architecture comparison and targeted research are complete.

Accepted decision:

```text
D-028
Use a SQLite-centered local-first architecture for V1 methodological
knowledge and project metadata/state.
```

The selected direction is:

```text
SQLite operational store
    reusable knowledge identities/revisions/components
    relations / conditional rules
    provenance / governance
    project epistemic and decision state
    project references to exact knowledge revisions
    execution-capability metadata

SQLite FTS5
    rebuildable lexical index

rebuildable embeddings
    initial in-process exact semantic similarity search

application-layer rule evaluator
    minimal predicate / ALL / ANY / NOT / UNKNOWN semantics

selective LLM context assembly
    bounded task-specific projection

filesystem / Git / artifact storage
    project code and large artifacts outside SQLite
```

Key non-selections for V1:

```text
no dedicated graph database
no dedicated vector database/service
no external generic rules engine
no PostgreSQL server by default
no ANN index until measured retrieval requirements justify one
```

PostgreSQL + pgvector is the preferred first migration family if future multi-writer, shared-server, concurrency, or semantic-index scale requirements exceed the SQLite envelope.

A targeted synthetic feasibility spike is preserved at:

```text
experiments/architecture_spikes/sqlite_v1_viability.py
```

The spike does not establish production SLOs. It showed no order-of-magnitude reason to introduce specialized relation/vector infrastructure at the expected V1 scale.

Detailed comparison and evidence:

```text
docs/checkpoints/108_v1_architecture_comparison_and_sqlite_centered_selection.md
docs/DECISIONS.md, D-028
```

D-011 is superseded for this persistence/retrieval scope but remains applicable to implementation subsystems that are still intentionally unselected.

## Current design stage

Do **not** start broad V1 implementation yet.

The next task is to write the **V1 technical architecture specification** for the accepted SQLite-centered design.

The specification should define:

```text
1. logical persistence boundaries and authoritative versus derived state;
2. initial relational entity/table families;
3. stable knowledge identity and revision strategy;
4. KnowledgeComponent / KnowledgeRelation / KnowledgeRule representation;
5. Foundation 018 project-object integration and exact knowledge-revision references;
6. FTS5 indexing and rebuild behavior;
7. embedding generation/storage/cache and exact-search interface;
8. minimal rule-evaluation interface and trace format;
9. methodological-horizon and LLM context-pack assembly boundaries;
10. transaction ownership, WAL, foreign-key enforcement, and concurrency rules;
11. backup/export/recovery and PostgreSQL migration strategy;
12. narrow architecture tests that would falsify the design before broad V1 implementation.
```

Still unselected:

```text
ORM / SQL toolkit
migration framework
exact physical schema
embedding model
reranker
LLM provider
frontend framework
API framework
job queue
artifact store
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

Checkpoint metadata/session-provenance repair remains closed under Checkpoint 103.

## Minimum reading for continuation

```text
README.md
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/VISION.md
docs/PRINCIPLES.md
docs/DECISIONS.md
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
docs/checkpoints/107_implementation_requirements_for_methodological_knowledge_subsystem.md
docs/checkpoints/108_v1_architecture_comparison_and_sqlite_centered_selection.md
docs/experiments/prototype_v0/FINAL_RESULTS.md
docs/CONTINUITY.md
```

## Current priority

**Write the V1 technical architecture specification for the accepted SQLite-centered design, including the minimal falsification tests that must pass before broad V1 implementation begins.**
