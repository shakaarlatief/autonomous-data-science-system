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
    how work continues across sessions

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

### Deep reasoning

```text
docs/foundations/001_initial_vision_and_reasoning.md
```

Origin of the project, why a single end-to-end LLM workflow can be insufficient, and the original state/knowledge/process-navigation vision.

```text
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
```

Current system-level synthesis of human-executed, human-plus-LLM, and system-mediated data-science projects. This is the best current explanation of why the LLM is one reasoning component inside a wider system while explicit mechanisms must still earn their complexity empirically.

Historical origin:

```text
docs/checkpoints/022_system_level_abstraction_and_reusable_reasoning_vision.md
```

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

The V0 implementation is now **falsified as the architecture to continue unchanged**. For the evidence and the exact mechanism-level lessons, read:

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

---

## Knowledge activation and reusable methodological knowledge

Deep theory:

```text
docs/foundations/006_knowledge_activation_and_open_world_reasoning.md
docs/foundations/007_reusable_knowledge_representation_and_composable_components.md
docs/foundations/008_knowledge_quality_generalization_and_evolution.md
```

V0 evidence:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
```

The important V0 result is that B1 gained most of the semantic benefit simply by receiving the same four methodological concepts statically. P0's explicit activation layer added only a small further improvement and showed path-sensitive activation brittleness.

Current implication: compact explicit or selectively retrieved methodological knowledge is a stronger default than the current P0 trigger architecture. The final production interaction between knowledge and LLM reasoning remains open.

---

## Project initialization

```text
docs/foundations/005_project_initialization_and_universal_bootstrap.md
```

How a new project may be characterized and bootstrapped without assuming one global workflow.

---

## System evaluation and behavioral regression

```text
docs/foundations/009_behavioral_reasoning_regression_and_system_evaluation.md
```

Why the evaluated object is a project trajectory rather than only a final model.

Prototype V0 is the first completed concrete realization:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
docs/foundations/010_minimum_falsification_prototype_and_experimental_contract.md
docs/foundations/011_prototype_v0_technical_specification.md
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
```

V0 demonstrates the value of strong controls, preregistration, deterministic checks, blinded semantic judging, explicit resource criteria, and allowing a richer architecture to lose.

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

The current post-V0 architectural direction is simplification. Do not tune P0 against the completed held-out benchmark.

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
2. docs/VISION.md
3. docs/experiments/prototype_v0/FINAL_RESULTS.md
4. docs/foundations/001_initial_vision_and_reasoning.md
```

V0 is important here because it shows that the answer cannot simply be "add more architecture." The system-level thesis survives only if individual mechanisms continue to earn their cost against strong simpler workflows.

---

## Knowledge preservation architecture

Current method:

```text
docs/DEVELOPMENT_METHOD.md
```

Deep rationale:

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

The post-V0 project should ask:

> What is the smallest low-overhead mechanism that improves reliability beyond B1 on longer changing project trajectories where conversational memory and static methodological prompting are expected to fail?

Candidate stressors for the next benchmark include multiple sequential state changes, longer dependency chains, partially shared evidence, selectively relevant knowledge, and meaningful under-propagation versus over-propagation consequences.

No V1 architecture has yet been accepted.
