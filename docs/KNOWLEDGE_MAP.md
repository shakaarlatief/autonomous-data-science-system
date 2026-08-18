# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources but does not replace them.  
**Last reviewed:** 2026-08-18

## Purpose

This file answers a practical question:

> Where does the current project knowledge about a particular topic live?

It is intentionally a routing layer rather than another copy of the project's knowledge.

When this file conflicts with an authoritative current specification or decision, the authoritative source governs.

## Start here

For a new session or a quick reconstruction:

```text
README.md
    project-level overview

docs/CURRENT_STATE.md
    concise present state and exact next step

docs/KNOWLEDGE_MAP.md
    where important knowledge lives

docs/VISION.md
    current system vision

docs/PRINCIPLES.md
    current design principles

docs/DECISIONS.md
    accepted project-level decisions

docs/OPEN_QUESTIONS.md
    unresolved questions

docs/DEVELOPMENT_METHOD.md
    how this project is developed and preserved

docs/CONTINUITY.md
    how work continues across chats/sessions

docs/MAJOR_CHANGES.md
    selective history of major structural changes
```

For active Prototype V0 work also read:

```text
prototype_v0/README.md

docs/foundations/012_preregistered_held_out_evaluation_protocol.md

docs/foundations/015_held_out_supervision_and_mechanical_verification_architecture.md

docs/experiments/prototype_v0/HELD_OUT_STATUS.md
```

---

## System purpose and long-term vision

### Read first

```text
docs/VISION.md
```

Current canonical statement of what the project is trying to build and what "best" means for a project.

### Deep reasoning

```text
docs/foundations/001_initial_vision_and_reasoning.md
```

Origin of the project, why a single end-to-end LLM workflow can be insufficient, questions/evidence orientation, human gates, persistent state, reusable knowledge modules, adaptive activation, and the original preservation philosophy.

```text
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
```

Current system-level synthesis of human-executed projects, human + interactive LLM projects, and system-mediated projects. Explains why the LLM is one reasoning component inside the wider system and why explicit mechanisms must still earn their complexity empirically.

### Important historical origin

```text
docs/checkpoints/022_system_level_abstraction_and_reusable_reasoning_vision.md
```

Historical checkpoint where the system-level distinction was first made explicit. Foundation 013 is the durable promoted synthesis.

---

## Epistemic integrity, admissibility, risk, and project constitution

### Canonical orientation

```text
docs/VISION.md
docs/PRINCIPLES.md
```

### Deep reasoning

```text
docs/foundations/002_epistemic_integrity_and_project_constitution.md
```

Semantic validity, information legitimacy, evidence validity, claim validity, traceability/dependency integrity, and the broader project constitution.

```text
docs/foundations/003_admissibility_risk_and_assurance.md
```

Admissibility, risk-sensitive assurance, controls, and the relationship between integrity requirements and project optimization.

---

## Project state, dependencies, and orchestration

### Deep reasoning

```text
docs/foundations/004_project_state_dependency_and_state_driven_orchestration.md
```

Typed project state, facts versus assumptions versus evidence versus claims versus decisions, dependency semantics, invalidation, staleness, reopening, and state-driven next-action selection.

### Prototype realization

```text
prototype_v0/README.md
prototype_v0/src/ads_v0/p0.py
prototype_v0/src/ads_v0/p0_controller.py
prototype_v0/src/ads_v0/p0_schema.py
```

Prototype V0 implements only a deliberately minimal experimental subset of the broader theory.

---

## Project initialization

```text
docs/foundations/005_project_initialization_and_universal_bootstrap.md
```

How a new project might be characterized, what initial facts/questions should be surfaced, and how initialization can remain general across project types.

---

## Knowledge activation and open-world reasoning

```text
docs/foundations/006_knowledge_activation_and_open_world_reasoning.md
```

How project state may activate relevant methodological concerns without requiring one fixed global workflow.

```text
docs/foundations/007_reusable_knowledge_representation_and_composable_components.md
```

Candidate structure for reusable knowledge components, composability, role separation, and interaction with reasoning.

```text
docs/foundations/008_knowledge_quality_generalization_and_evolution.md
```

Knowledge quality, maturity, scope, promotion, challenge history, generalization, and evolution.

---

## System evaluation and behavioral regression

```text
docs/foundations/009_behavioral_reasoning_regression_and_system_evaluation.md
```

Why the evaluated object is a project trajectory rather than only a final model, and how hidden truth, behavioral envelopes, deterministic checks, semantic judging, self-correction, and dependency-aware evaluation fit together.

---

## Prototype V0: conceptual experiment

### Quick entry point

```text
prototype_v0/README.md
```

Short current explanation of what one run does, the benchmark traps, B0/B1/P0, P0 architecture, H1/H2, 30-run design, and evaluation layers.

### Experimental contract

```text
docs/foundations/010_minimum_falsification_prototype_and_experimental_contract.md
```

Why V0 exists, falsifiable hypotheses, benchmark design, B0/B1/P0 conditions, semantic spine, required behavior, and acceptance envelope.

### Technical specification

```text
docs/foundations/011_prototype_v0_technical_specification.md
```

Detailed technical contract for the V0 implementation.

### Frozen held-out protocol

```text
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
```

H1/H2 bundles, run counts/order, model/provider configuration, budgets, replacement rules, semantic judge, and continuation/falsification criteria.

### Current held-out execution ledger

```text
docs/experiments/prototype_v0/HELD_OUT_STATUS.md
```

Detailed current run ledger, mechanical summaries, resource consequences, interruptions, supervisor validation, and next frozen execution point.

### Current project-level navigation

```text
docs/CURRENT_STATE.md
```

Contains the concise V0 status and next action needed for continuity.

---

## Prototype V0 held-out supervision and mechanical verification

### Durable architecture

```text
docs/foundations/015_held_out_supervision_and_mechanical_verification_architecture.md
```

Explains the separation between frozen treatment execution and external experiment supervision, the read-only M01-M11 mechanical verifier, bounded sequential batching, compact exports, replacement-policy preservation, and the path toward a larger future evaluation platform.

### Accepted operational decision

```text
docs/DECISIONS.md, D-026
```

The retrospectively validated supervisor/verifier is frozen for the remaining Prototype V0 operational execution unless a genuine condition-neutral infrastructure defect is discovered.

### Validation provenance

```text
docs/checkpoints/081_automated_held_out_supervision_implemented_pending_retroactive_validation.md
docs/checkpoints/082_held_out_supervisor_retroactively_validated_and_frozen_for_live_use.md
```

Checkpoint 81 records implementation before use. Checkpoint 82 records the successful `77 passed` software test result, 12/12 retrospective mechanical integrity passes, comparison with the manual ledger, and authorization of the first bounded live supervisor batch.

### Implementation

```text
prototype_v0/src/ads_v0/heldout_runner.py
    frozen treatment executor

prototype_v0/src/ads_v0/heldout_verifier.py
    read-only mechanical verifier

prototype_v0/src/ads_v0/heldout_supervisor.py
    sequential external supervisor
```

---

## Why a system instead of only one strong LLM?

Read in this order:

```text
1. docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
2. docs/VISION.md
3. docs/foundations/001_initial_vision_and_reasoning.md
4. docs/checkpoints/022_system_level_abstraction_and_reusable_reasoning_vision.md
```

Foundation 013 is the best current synthesis. Checkpoint 22 is provenance, not the primary current source.

---

## Why B1 matters and what a P0 loss would mean

Read:

```text
prototype_v0/README.md
docs/foundations/010_minimum_falsification_prototype_and_experimental_contract.md
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
```

The key distinction is between a local treatment result and the broader system-level question.

---

## How this project preserves its own knowledge

### Current method

```text
docs/DEVELOPMENT_METHOD.md
```

### Continuity across chats and models

```text
docs/CONTINUITY.md
```

### Deep rationale and future evolution

```text
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
```

### Selective structural history

```text
docs/MAJOR_CHANGES.md
```

### Historical checkpoints

```text
docs/checkpoints/
```

Checkpoints preserve provenance but should not be treated as automatically current truth.

---

## Major accepted decisions

```text
docs/DECISIONS.md
```

Use this for explicit project-level decisions and their rationale.

Do not infer an accepted decision solely from a foundation or checkpoint when `DECISIONS.md` states otherwise.

---

## Current unresolved questions

```text
docs/OPEN_QUESTIONS.md
```

Use this before assuming an architectural detail is settled.

---

## Major structural evolution

```text
docs/MAJOR_CHANGES.md
```

This is a selective conceptual change log, not a replacement for Git history or checkpoints.

---

## Repository authority model

Use the following default interpretation when documents disagree:

```text
1. frozen current specifications/contracts for their declared scope
2. current accepted decisions and canonical specifications
3. current vision/principles/current-state material
4. foundational design memos for rationale and durable hypotheses
5. checkpoints/session records for historical state
6. raw historical material for provenance
```

A material unresolved conflict should become an explicit open question rather than being silently reconciled.

---

## Knowledge lifecycle

The current preservation lifecycle is:

```text
discussion
    -> checkpoint
    -> promotion audit
    -> canonical/foundational/specification update when warranted
    -> knowledge-map routing update when warranted
    -> periodic knowledge reconciliation
```

No promotion is a valid outcome. Promotion should follow maturity, not enthusiasm.

Detailed rationale: `docs/foundations/014_knowledge_preservation_architecture_and_evolution.md`.