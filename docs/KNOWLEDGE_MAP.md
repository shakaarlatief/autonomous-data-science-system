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

Current detailed vision of the eventual professional interactive data-science environment. It explains the project workspace concept, methodological option-space navigation, recommended versus applicable versus full-catalog views, configurable human involvement, project memory versus LLM-context separation, living reports, and project-replay evaluation.

Historical origin of the system-level abstraction:

```text
docs/checkpoints/022_system_level_abstraction_and_reusable_reasoning_vision.md
```

The post-V0 product clarification is preserved historically in:

```text
docs/checkpoints/097_post_v0_product_vision_concretized_as_interactive_methodological_workspace.md
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

EDA is the current concrete reference example for this vision.

The central product principle is that the user should not need to repeatedly remember every useful methodological question to ask a general-purpose LLM.

The system may remain highly interactive and should support guided, semi-autonomous, and more autonomous project styles according to project intent.

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

The broad theory lives in:

```text
docs/foundations/004_project_state_dependency_and_state_driven_orchestration.md
```

Prototype V0's concrete implementation lives in:

```text
prototype_v0/src/ads_v0/p0.py
prototype_v0/src/ads_v0/p0_controller.py
prototype_v0/src/ads_v0/p0_schema.py
```

The V0 implementation is now **falsified as the architecture to continue unchanged**. For the evidence and exact mechanism-level lessons, read:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
```

Important distinction:

```text
broad state/dependency theory remains an open design space
!=
current P0 always-on representation is justified
```

V0 found that P0's dependency repair was technically precise, but B1 repaired almost as well while P0 incurred severe repeated-context cost.

Foundation 017 adds another important distinction:

```text
what the system persists
!=
what an LLM receives on every turn
```

Future project memory may be large while model context is selectively retrieved and small.

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
```

V0 evidence:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
```

The important V0 result is that B1 gained most of the semantic benefit simply by receiving the same four methodological concepts statically. P0's explicit activation layer added only a small further improvement and showed path-sensitive activation brittleness.

The post-V0 product vision does not reduce methodological knowledge to a static prompt. Instead it treats a broad, inspectable, evolving method/decision catalog as a candidate system asset while leaving its retrieval, ranking, applicability, and reasoning interface open for design and testing.

---

## Project initialization

```text
docs/foundations/005_project_initialization_and_universal_bootstrap.md
```

How a new project may be characterized and bootstrapped without assuming one global workflow.

For the concrete desired project-start experience, also read:

```text
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
```

---

## System evaluation and behavioral regression

```text
docs/foundations/009_behavioral_reasoning_regression_and_system_evaluation.md
```

Why the evaluated object is a project trajectory rather than only a final model.

Prototype V0 is the first completed controlled realization:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
docs/foundations/010_minimum_falsification_prototype_and_experimental_contract.md
docs/foundations/011_prototype_v0_technical_specification.md
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
```

V0 demonstrates the value of strong controls, preregistration, deterministic checks, blinded semantic judging, explicit resource criteria, and allowing a richer architecture to lose.

For the broader post-V0 evaluation direction, including project replay and mixed quantitative/qualitative product evaluation, read:

```text
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
```

---

## Prototype V0 final result

### Final authoritative report

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
```

### Quick explanation

```text
prototype_v0/README.md
```

### Final compact execution ledger

```text
docs/experiments/prototype_v0/HELD_OUT_STATUS.md
```

### Frozen protocol

```text
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
```

### Final classification

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

Historical completion checkpoints include:

```text
docs/checkpoints/085_held_out_execution_complete_and_full_compact_export_verified.md
docs/checkpoints/090_blinded_semantic_judge_execution_complete.md
docs/checkpoints/093_blinded_semantic_freeze_independently_verified_and_unblinding_authorized.md
docs/checkpoints/095_decoded_semantic_results_verified_and_p0_diagnostic_export_added.md
docs/checkpoints/096_prototype_v0_final_strong_falsification_and_architecture_diagnostic_conclusion.md
```

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

These evaluation-infrastructure components are not part of the falsified P0 semantic treatment. They remain evidence-supported operational infrastructure.

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

Prototype observers:

```text
prototype_v0/src/ads_v0/heldout_monitor.py
prototype_v0/src/ads_v0/semantic_judge_monitor.py
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
3. docs/VISION.md
4. docs/experiments/prototype_v0/FINAL_RESULTS.md
5. docs/foundations/001_initial_vision_and_reasoning.md
```

V0 shows that the answer cannot simply be "add more architecture." Foundation 017 makes the product goal concrete: the system should externalize project navigation and methodological option-space intelligence so the user does not have to reconstruct it through repeated prompts.

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

Current routing/history layers:

```text
docs/KNOWLEDGE_MAP.md
docs/MAJOR_CHANGES.md
docs/checkpoints/
Git history
```

The storage substrate remains Git + Markdown until observed retrieval, dependency, consistency, concurrency, or automation problems justify more advanced infrastructure.

---

## Current unresolved questions

```text
docs/OPEN_QUESTIONS.md
```

Several V0-related question statuses still require post-V0 stage-boundary reconciliation. `docs/CURRENT_STATE.md` and `docs/experiments/prototype_v0/FINAL_RESULTS.md` govern the current experimental interpretation until that reconciliation is complete.

New product/system questions raised by Foundation 017 should be reconciled into the canonical question register during the upcoming post-V0 reconciliation rather than silently treated as settled architecture.

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

A material unresolved conflict should become an explicit open question rather than being silently reconciled.

---

## Current next-design question

Before selecting a V1 architecture, the project should make the desired product/system contract more explicit.

Current questions include:

```text
What should the professional project workspace expose?
What should initialize automatically from project sources?
What is a reusable methodological knowledge object?
How should applicability and recommendation be represented?
How should recommended, relevant, and full-catalog views interact?
What should execute automatically versus await user selection?
What project information must persist?
How should LLM context be selected from persistent project memory?
How should findings change later recommendations and decisions?
How should living reports evolve?
How should guided versus autonomous operation be configured?
How should completed projects become project-replay evaluations?
```

After this product/system contract is clearer, the next experimental architecture question remains approximately:

> What is the smallest low-overhead mechanism that improves reliability beyond a strong B1-like baseline on substantial changing project trajectories where conversational memory and static prompting are expected to fail?

No V1 architecture has yet been accepted.
