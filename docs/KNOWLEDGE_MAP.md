# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources but does not replace them.  
**Last reviewed:** 2026-08-19

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

For the completed Prototype V0 experiment, read:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
prototype_v0/README.md
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
docs/experiments/prototype_v0/HELD_OUT_STATUS.md
```

Prototype V0 is complete. Its final classification is **strong falsification of the current P0 design**. It is no longer an active execution stage.

---

## System purpose and long-term vision

### Canonical orientation

```text
docs/VISION.md
README.md
```

### Deep system-level reasoning

```text
docs/foundations/001_initial_vision_and_reasoning.md
```

Origin of the project, why a single end-to-end LLM workflow can be insufficient, and the original state/knowledge/process-navigation vision.

```text
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
```

Current system-level synthesis of human-executed, human-plus-LLM, and system-mediated data-science projects. This is the best current explanation of why the LLM is one reasoning component inside a wider system while explicit mechanisms must still earn their complexity empirically.

### Concrete product and user-experience vision

```text
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
```

Detailed vision of the eventual professional interactive data-science environment: project workspace, methodological option-space navigation, recommended versus applicable versus full-catalog views, configurable human involvement, project-memory versus LLM-context separation, living reports, and project-replay evaluation.

### Candidate project object model and professional developer workflow

```text
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
```

Defines the current product-level candidate object model and the separation among project workspace, VS Code, execution environment, Git/GitHub, artifact storage, and LLM context. It also preserves the requirement that generated consequential code remain independently runnable and professionally maintainable.

Historical product-clarification checkpoints:

```text
docs/checkpoints/097_post_v0_product_vision_concretized_as_interactive_methodological_workspace.md
docs/checkpoints/098_project_object_model_and_professional_developer_workflow_concretized.md
```

---

## Professional interactive workspace and methodological-navigation brain

Read first:

```text
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
```

The target product is not an upload-to-final-answer black box and not merely a prettier chat interface.

The intended system should progressively own the burden of:

```text
maintaining broad methodological option knowledge;
understanding the current project;
surfacing recommended analyses;
exposing lower-priority applicable alternatives;
letting the user inspect the full knowledge catalog;
executing selected work;
preserving evidence, findings, decisions, and provenance;
remembering what happened;
surfacing what becomes relevant next;
maintaining living project outputs and reports.
```

EDA is the current concrete reference example.

The central product principle is that the user should not need to repeatedly remember every useful methodological question to ask a general-purpose LLM.

The system may remain highly interactive and should support guided, semi-autonomous, and more autonomous project styles according to project intent.

---

## Product object model, events, relations, and views

Read:

```text
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
```

The current product-level conceptual model separates:

```text
OBJECTS
RELATIONS
EVENTS
VIEWS
```

Candidate object families include:

```text
Project / IntentItem
Artifact / Dataset / Variable
Question / Assumption / Finding / Claim
Method
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

EDA, Validation, Features, and Models are currently best understood as user-facing views over shared project objects rather than backend silos.

The candidate object model is **not** a frozen storage schema.

---

## Professional developer workbench, VS Code, Git, GitHub, and execution

Canonical principles:

```text
docs/PRINCIPLES.md, P-023 and P-024
```

Deep rationale:

```text
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
```

Current conceptual split:

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

The system should complement VS Code rather than reproduce a full IDE.

Consequential generated project code should remain normal, professional, independently runnable code. A system-triggered execution and a manual terminal/VS Code execution should preferentially share the same reproducible command/configuration contract.

Git/GitHub should be deeply integrated for source versioning and provenance, while large datasets, models, and generated arrays may live in separate artifact storage.

Local-first execution is a strong current hypothesis for typical projects, but it is **not yet a universal architecture decision**. Future execution should remain compatible with remote GPU, cloud, cluster, or organizational infrastructure.

---

## Epistemic integrity, admissibility, risk, and project constitution

```text
docs/foundations/002_epistemic_integrity_and_project_constitution.md
```

Semantic validity, information legitimacy, evidence validity, claim validity, and traceability/dependency integrity.

```text
docs/foundations/003_admissibility_risk_and_assurance.md
```

Admissibility, risk-sensitive assurance, controls, and integrity requirements.

Canonical high-level orientation:

```text
docs/VISION.md
docs/PRINCIPLES.md
```

---

## Project state, dependencies, and orchestration

Broad theory:

```text
docs/foundations/004_project_state_dependency_and_state_driven_orchestration.md
```

Prototype V0 implementation:

```text
prototype_v0/src/ads_v0/p0.py
prototype_v0/src/ads_v0/p0_controller.py
prototype_v0/src/ads_v0/p0_schema.py
```

The V0 implementation is **falsified as the architecture to continue unchanged**.

Final evidence:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
```

Important distinctions:

```text
broad state/dependency theory remains an open design space
!=
current P0 always-on representation is justified
```

and:

```text
what the system persists
!=
what an LLM receives on every turn
```

Foundation 018 adds:

```text
current project state
!=
event history

workspace section
!=
fundamental persisted object
```

---

## Knowledge activation and reusable methodological knowledge

Deep theory:

```text
docs/foundations/006_knowledge_activation_and_open_world_reasoning.md
docs/foundations/007_reusable_knowledge_representation_and_composable_components.md
docs/foundations/008_knowledge_quality_generalization_and_evolution.md
```

Concrete product interpretation:

```text
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
```

V0 evidence:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
```

B1 gained most of the semantic benefit by receiving the same four methodological concepts statically. P0's explicit activation layer added only a small additional improvement and showed path-sensitive activation brittleness.

The post-V0 product vision does not reduce methodological knowledge to a static prompt. It treats a broad, inspectable, evolving method/decision catalog as a candidate system asset while leaving its representation, retrieval, applicability, ranking, and reasoning interface open for design and testing.

---

## Project initialization

Deep theory:

```text
docs/foundations/005_project_initialization_and_universal_bootstrap.md
```

Concrete desired project-start experience:

```text
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
```

---

## System evaluation and behavioral regression

```text
docs/foundations/009_behavioral_reasoning_regression_and_system_evaluation.md
```

Prototype V0 is the first completed controlled realization:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
docs/foundations/010_minimum_falsification_prototype_and_experimental_contract.md
docs/foundations/011_prototype_v0_technical_specification.md
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
```

For the broader post-V0 evaluation direction, including project replay and mixed quantitative/qualitative product evaluation, read Foundation 017.

---

## Prototype V0 final result

Authoritative report:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
```

Quick explanation:

```text
prototype_v0/README.md
```

Final classification:

```text
STRONG FALSIFICATION OF THE CURRENT P0 DESIGN
```

Central pooled result:

```text
B1 targeted mean: 1.73
P0 targeted mean: 1.78
incremental P0 gain: +0.05

B1 completed within budget: 10/10
P0 completed within budget: 3/10

P0/B1 median token ratio: 2.160
```

The current P0 representation must not be expanded merely because it already exists. The broader system vision remains active.

---

## Held-out supervision and mechanical verification

Durable architecture:

```text
docs/foundations/015_held_out_supervision_and_mechanical_verification_architecture.md
```

Implementation:

```text
prototype_v0/src/ads_v0/heldout_runner.py
prototype_v0/src/ads_v0/heldout_verifier.py
prototype_v0/src/ads_v0/heldout_supervisor.py
prototype_v0/src/ads_v0/heldout_monitor.py
```

These evaluation-infrastructure components are not part of the falsified P0 semantic treatment.

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

System pattern:

```text
execution / reasoning
    -> persisted state/events
    -> read-only observability
    -> human interface
```

---

## Why a system instead of only one strong LLM?

Read:

```text
1. docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
2. docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
3. docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
4. docs/VISION.md
5. docs/experiments/prototype_v0/FINAL_RESULTS.md
```

V0 shows that the answer cannot simply be "add more architecture." Foundations 017 and 018 make the product goal concrete: externalize project navigation and methodological option-space intelligence while integrating cleanly with the normal professional code/execution workflow.

---

## Knowledge preservation and session continuity

Current preservation method:

```text
docs/DEVELOPMENT_METHOD.md
```

Canonical session-continuity procedure and standardized first prompt for a new project chat:

```text
docs/CONTINUITY.md
```

Deep preservation rationale:

```text
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
```

---

## Current unresolved questions

```text
docs/OPEN_QUESTIONS.md
```

Several older V0-related statuses still require the planned post-V0 reconciliation. `CURRENT_STATE.md` and the final V0 report govern current interpretation in the meantime.

Product/system questions introduced by Foundations 017 and 018 should be reconciled into the canonical question register during that stage-boundary reconciliation rather than silently treated as settled architecture.

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

## Current next-design question

Before selecting a V1 architecture, continue designing the **methodological-navigation brain**.

Current questions include:

```text
What should a reusable Method/knowledge object contain?
How should applicability conditions be represented?
How should known methods become applicable, relevant, recommended, or required?
How should inapplicable methods remain inspectable?
How should alternatives be surfaced?
How should recommendations explain their reasoning?
What role should the LLM play versus explicit knowledge structures?
How should cost, risk, project intent, and human preference affect ranking?
How should knowledge grow from completed projects without unsafe overgeneralization?
How should recommendation quality be evaluated through project replay and other tests?
```

No V1 backend architecture has yet been accepted.