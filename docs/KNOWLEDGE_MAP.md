# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources but does not replace them.  
**Last reviewed:** 2026-08-20

## Start here

For a new session or quick reconstruction:

```text
README.md
    project-level overview and current stage

docs/CURRENT_STATE.md
    concise present state and exact next priority

docs/KNOWLEDGE_MAP.md
    routing layer for important project knowledge

docs/VISION.md
    current system purpose and vision

docs/PRINCIPLES.md
    current design principles

docs/DECISIONS.md
    accepted project-level decisions

docs/OPEN_QUESTIONS.md
    unresolved canonical questions

docs/DEVELOPMENT_METHOD.md
    how the project is developed and preserved

docs/CONTINUITY.md
    how work continues across sessions and the standardized new-chat prompt

docs/MAJOR_CHANGES.md
    selective structural history
```

Prototype V0 is complete. Its final classification is **strong falsification of the current P0 design**. It is no longer an active execution stage.

---

## System purpose and long-term vision

Read:

```text
docs/VISION.md
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
```

Foundation 013 explains why the LLM is one reasoning component inside a wider system rather than the whole system.

Foundation 017 makes the target product concrete as a professional interactive data-science workspace that should carry much of the methodological-navigation burden while preserving deep human interaction and control.

Historical origin:

```text
docs/foundations/001_initial_vision_and_reasoning.md
docs/checkpoints/022_system_level_abstraction_and_reusable_reasoning_vision.md
```

---

## Professional interactive workspace

Primary source:

```text
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
```

The target product is not an upload-to-final-answer black box and not merely a prettier chat interface.

Key ideas include:

```text
professional project workspace
recommended analyses
relevant option space
full knowledge catalog
configurable human involvement
living project memory
living reports
project replay evaluation
```

---

## Product object model, developer workflow, VS Code, Git/GitHub, and execution

Primary source:

```text
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
```

The candidate project model separates:

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

The current representation work does **not** add a universal project `Assessment` object. Foundation 020 instead routes subject-specific criterion verdicts through the existing Question -> Evidence -> Finding -> Claim/Decision chain, with a structured criterion-Finding form where useful.

Professional workflow principles:

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
    source versioning, collaboration, and code provenance
```

Generated consequential code should remain independently runnable, professional, and maintainable. System-triggered and manually triggered runs should preferentially share the same reproducible execution contract.

---

## Methodological-navigation brain and relevance architecture

Primary source:

```text
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
```

Foundation 019 governs how a large reusable knowledge universe may become a small project-specific methodological horizon.

Current relevance progression:

```text
KNOWN
    -> APPLICABLE
    -> RELEVANT
    -> RECOMMENDED
    -> REQUIRED / BLOCKING
```

Important concepts include:

```text
methodological horizon
explicit prerequisite filtering where reliable
flexible reasoning for semantic relevance/tradeoffs
inspectable recommendation rationale
project-signal visibility
ranking by validity importance, information value, impact, cost, risk, redundancy, and user preference
knowledge provenance / scope / maturity / counterexamples
separation of methodological meaning from execution templates
open-world discovery of knowledge gaps
```

The full global catalog should not be sent to the LLM. Project-specific retrieval should produce a small relevant slice.

---

## Reusable methodological knowledge representation architecture

Primary source:

```text
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
```

Foundation 020 is the current promoted source for how reusable methodological knowledge should be represented conceptually.

It was promoted only after:

```text
five heterogeneous original examples
Checkpoint 102 first explicit contract
Checkpoint 104 adversarial review
Checkpoint 105 second reconstruction stress test
an additional Class Imbalance example
```

Core representation direction:

```text
KnowledgeAsset
    stable identity + revision identity
    intrinsic kind
    optional reasoning functions
    optional retrieval/applicability/context structures

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
    global knowledge revisions without one KnowledgeInstance type

Criterion Finding
    structured project Finding form for subject-specific verdicts

ExecutionCapability
    separate implementation bridge

Views
    derived navigation and explanation over knowledge + project state
```

Durable distinctions:

```text
intrinsic knowledge kind != reasoning function
asset != identifiable component != narrative facet
static semantic relation != conditional guidance rule
retrieval cue != applicability predicate != required context != project relevance
methodological knowledge != execution implementation
global knowledge != project-specific object/state
internal representation != human-facing decision tree/workspace view
```

Current representation principles:

```text
docs/PRINCIPLES.md, P-025 and P-026
```

Important historical design evidence:

```text
docs/checkpoints/101_five_example_reusable_knowledge_stress_test_completed.md
docs/checkpoints/102_candidate_conceptual_knowledge_representation_contract.md
docs/checkpoints/104_adversarial_review_of_candidate_knowledge_representation.md
docs/checkpoints/105_refined_representation_second_stress_test.md
```

---

## V1 implementation requirements and selected persistence/retrieval architecture

**Read first for the current implementation-design task:**

```text
docs/checkpoints/107_implementation_requirements_for_methodological_knowledge_subsystem.md
docs/checkpoints/108_v1_architecture_comparison_and_sqlite_centered_selection.md
docs/DECISIONS.md, D-028
```

Checkpoint 107 derived technology-neutral V1 requirements before any database/retrieval choice was allowed.

The requirements include:

```text
stable asset + revision identity
recoverable historical revisions
component-level provenance where needed
typed relation lookup and bounded traversal
minimal TRUE / FALSE / UNKNOWN conditional rules
high-recall semantic candidate retrieval
retrieval/applicability/context separation
project-state lookup for Definitions/Questions/Findings/etc.
bounded methodological-horizon construction
selective budgeted LLM context assembly
human-readable review/export
local-first operation with one active writer acceptable initially
large artifacts outside the operational metadata store
```

Checkpoint 108 then compared plausible architecture families, consulted current SQLite/PostgreSQL/pgvector/Neo4j/vector-store capabilities, and ran a targeted synthetic SQLite feasibility spike.

Accepted V1 decision:

```text
SQLite-centered local-first operational architecture
```

Current direction:

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
    initial in-process exact semantic similarity search

application-level minimal rule evaluator
    predicate / ALL / ANY / NOT / TRUE / FALSE / UNKNOWN

selective context assembler
    small task-specific projection rather than full state

filesystem / Git / artifact storage
    project code and large artifacts outside SQLite
```

Explicit V1 non-selections:

```text
no dedicated graph database
no dedicated vector database/service
no external generic rules engine
no PostgreSQL server by default
no ANN index until measured requirements justify it
```

PostgreSQL + pgvector is the preferred first migration family if later concurrency, shared-server, or semantic-search scale requirements exceed the SQLite envelope.

Reproducible architecture spike:

```text
experiments/architecture_spikes/sqlite_v1_viability.py
```

D-011 is superseded for this persistence/retrieval scope by D-028. Other implementation subsystems remain intentionally unselected until requirements justify choices.

---

## Earlier reusable-knowledge foundations

Earlier theory:

```text
docs/foundations/006_knowledge_activation_and_open_world_reasoning.md
docs/foundations/007_reusable_knowledge_representation_and_composable_components.md
docs/foundations/008_knowledge_quality_generalization_and_evolution.md
```

Post-V0 promoted interpretation:

```text
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
```

V0 evidence:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
```

B1 gained most of the semantic benefit from the four methodological concepts simply being explicitly available. P0's path-sensitive activation and large always-on representation did not earn their cost.

This does **not** reduce future reusable knowledge to a static prompt. Foundations 019 and 020 support selective retrieval, explicit filtering/rules where justified, flexible semantic reasoning, typed reusable knowledge, and inspectable project-specific relevance.

---

## Project state, dependencies, and orchestration

Broad theory:

```text
docs/foundations/004_project_state_dependency_and_state_driven_orchestration.md
```

V0 implementation:

```text
prototype_v0/src/ads_v0/p0.py
prototype_v0/src/ads_v0/p0_controller.py
prototype_v0/src/ads_v0/p0_schema.py
```

Final V0 evidence:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
```

Interpretation:

```text
broad state/dependency theory remains an open design space
!=
current P0 always-on representation is justified

what the system persists
!=
what an LLM receives on every turn

current project state
!=
event history
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

These sources govern semantic validity, information legitimacy, evidence validity, claim validity, traceability/dependency integrity, admissibility, and risk-sensitive assurance.

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

For broader post-V0 evaluation, Foundation 017 introduces project replay and mixed quantitative/qualitative measures such as recommendation coverage, critical omissions, human reminder burden, state-recall failures, reproducibility, and expert judgment.

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

Quick overview:

```text
prototype_v0/README.md
```

Final classification:

```text
STRONG FALSIFICATION OF THE CURRENT P0 DESIGN
```

Do not tune or restart P0 against the completed V0 benchmark.

---

## Held-out supervision and mechanical verification

Read:

```text
docs/foundations/015_held_out_supervision_and_mechanical_verification_architecture.md
```

These evaluation-infrastructure components are separate from the falsified P0 semantic treatment.

---

## Execution and observability separation

Canonical principle:

```text
docs/PRINCIPLES.md, P-022
```

Deep rationale:

```text
docs/foundations/016_execution_observability_separation.md
```

Pattern:

```text
execution / reasoning
    -> persisted state/events
    -> read-only observability
    -> human interface
```

---

## Knowledge preservation and session continuity

Current preservation method:

```text
docs/DEVELOPMENT_METHOD.md
```

Standardized new-chat procedure and active session metadata:

```text
docs/CONTINUITY.md
```

Deep preservation rationale:

```text
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
```

Checkpoint-format contract:

```text
docs/checkpoints/README.md
```

Current design session:

```text
02 - Methodological Brain & Knowledge Units
```

---

## Current unresolved questions

```text
docs/OPEN_QUESTIONS.md
```

`CURRENT_STATE.md` governs the exact active priority if older open-question wording has not yet been reconciled.

---

## Repository authority model

Default order when documents disagree:

```text
1. frozen current specifications/contracts for their declared scope
2. current accepted decisions and canonical specifications
3. current vision/principles/current-state material
4. final experiment reports for their declared experiment scope
5. foundational design memos for rationale and durable hypotheses
6. checkpoints for historical state
7. raw historical material for provenance
```

---

## Exact next step

Write the **V1 technical architecture specification** for D-028's accepted SQLite-centered design.

The specification should make concrete:

```text
logical persistence boundaries and authoritative versus derived state
initial relational entity/table families
stable knowledge identity + revision representation
components / relations / conditional rules
project-object integration and knowledge-revision references
FTS5 indexing and rebuild strategy
embedding generation/storage/cache and exact-search interface
minimal rule evaluator and trace format
methodological-horizon and LLM context assembly boundary
transaction ownership / WAL / foreign-key enforcement
backup/export/recovery and PostgreSQL migration strategy
narrow falsification tests required before broad V1 implementation
```

Do not start broad V1 implementation until this specification is explicit and its highest-risk assumptions have targeted tests.