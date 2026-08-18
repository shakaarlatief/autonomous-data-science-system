# Major Changes

**Status:** Current selective structural history  
**Authority:** Navigation and project-history aid. Detailed decisions, foundations, specifications, checkpoints, and Git history remain authoritative for their own content.  
**Last reviewed:** 2026-08-18

## Purpose

This file records only changes that materially alter how the project is understood, built, evaluated, preserved, or continued.

It is not a commit changelog and it does not list routine checkpoint creation, typo fixes, ordinary run execution, or small implementation changes.

A change belongs here when a future contributor or model would benefit from knowing that the project crossed a meaningful architectural, methodological, experimental, or preservation boundary.

---

## 2026-08-07: Dedicated project and layered repository preservation established

The Autonomous Data Science System became a dedicated repository separate from individual data projects.

The initial preservation architecture established the distinction between:

```text
chat as exploratory workspace
repository as durable source of truth
canonical documents
foundational design memos
checkpoints/session records
historical provenance
```

This also introduced the principle:

> The chat is where we think. The repository is where the system remembers.

Key sources:

```text
docs/foundations/001_initial_vision_and_reasoning.md
docs/DECISIONS.md, D-001 through D-010
docs/DEVELOPMENT_METHOD.md, version 0.1
```

---

## 2026-08-08: Development Method v0.2 made checkpointing and chat rotation proactive AI responsibilities

The user no longer needed to remember when project preservation or chat rotation was due.

The AI design collaborator became responsible for:

```text
detecting natural checkpoints;
preserving important uncheckpointed reasoning;
recommending chat rotation when continuity risk becomes material;
keeping maturity distinctions explicit rather than canonizing ideas automatically.
```

Key sources:

```text
docs/DECISIONS.md, D-018 and D-020
docs/DEVELOPMENT_METHOD.md, version 0.2
docs/CONTINUITY.md
```

---

## 2026-08-08 to 2026-08-09: Core system theory expanded into dedicated foundations

The project moved from an inspiring general vision toward explicit theory for:

```text
epistemic integrity and project constitution;
admissibility and risk-sensitive assurance;
project state and dependency-aware revision;
project initialization;
knowledge activation;
reusable knowledge representation;
knowledge quality and evolution;
behavioral system evaluation.
```

Key sources:

```text
docs/foundations/002_epistemic_integrity_and_project_constitution.md
docs/foundations/003_admissibility_risk_and_assurance.md
docs/foundations/004_project_state_dependency_and_state_driven_orchestration.md
docs/foundations/005_project_initialization_and_universal_bootstrap.md
docs/foundations/006_knowledge_activation_and_open_world_reasoning.md
docs/foundations/007_reusable_knowledge_representation_and_composable_components.md
docs/foundations/008_knowledge_quality_generalization_and_evolution.md
docs/foundations/009_behavioral_reasoning_regression_and_system_evaluation.md
```

---

## 2026-08-09: Prototype V0 became a falsification experiment rather than an architecture demonstration

The project deliberately chose to test the smallest explicit semantic architecture against strong simpler controls rather than building a large autonomous system immediately.

The central comparison became:

```text
B0: strong LLM + strong generic data-science workflow
B1: B0 + the same methodological knowledge supplied statically
P0: same model + explicit typed state, activation, safeguards, dependency repair,
    and state-driven action selection
```

The experiment was designed so P0 could fail and be simplified.

Key sources:

```text
docs/foundations/010_minimum_falsification_prototype_and_experimental_contract.md
docs/foundations/011_prototype_v0_technical_specification.md
prototype_v0/
```

---

## 2026-08-09: Held-out experiment preregistered before P0 implementation

The H1/H2 bundles, 30-run order, common model/provider configuration, resource limits, replacement policy, semantic rubric, blinded judging procedure, and continuation/falsification criteria were frozen independently of P0 behavior.

This created the experimental integrity boundary that governs current held-out execution.

Key source:

```text
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
```

---

## 2026-08-09: System-level abstraction made explicit at Checkpoint 22

The project distinguished:

```text
human-executed data science
human + interactive LLM data science
system-mediated data science
```

This clarified that the long-term goal is not merely a better prompt or one longer LLM conversation. The system is intended to externalize reusable process-navigation intelligence while still requiring every architectural mechanism to justify its cost.

Historical source:

```text
docs/checkpoints/022_system_level_abstraction_and_reusable_reasoning_vision.md
```

The durable synthesis was later promoted to Foundation 013.

---

## 2026-08-18: Prototype V0 documentation received a current simple entry point

`prototype_v0/README.md` was rewritten so the experiment can be understood without reconstructing dozens of checkpoints.

It now explains:

```text
what one run does;
benchmark traps;
B0/B1/P0;
P0 architecture;
H1/H2;
mechanical and semantic evaluation;
repository navigation.
```

Historical source:

```text
docs/checkpoints/074_prototype_v0_readme_refreshed_as_current_entry_point.md
```

---

## 2026-08-18: Checkpoint 22 system-level vision promoted into Foundation 013

The project recognized that historically preserved knowledge can still become conceptually buried.

The stable system-level synthesis from Checkpoint 22 was promoted into:

```text
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
```

Checkpoint 22 remains unchanged as provenance.

This was the concrete event that exposed the need to strengthen the preservation lifecycle beyond durability alone.

Historical source:

```text
docs/checkpoints/075_checkpoint_22_system_level_vision_promoted_to_foundation_013.md
```

---

## 2026-08-18: Development Method v0.3 introduced a knowledge-preservation architecture

The preservation method was upgraded after the Checkpoint 22 promotion exposed three scaling risks:

```text
discoverability
implicit promotion
canonical duplication/drift
```

Version 0.3 adds:

```text
an explicit promotion audit at substantive checkpoints;
docs/KNOWLEDGE_MAP.md as a routing layer;
periodic knowledge reconciliation at stage boundaries;
lightweight authority/maturity/provenance metadata conventions;
a selective MAJOR_CHANGES ledger;
separation of concise CURRENT_STATE from detailed experiment ledgers;
explicit deferral criteria for graph/vector/database/automation infrastructure.
```

The current storage foundation remains Git + Markdown. More advanced infrastructure is deliberately deferred until observed scale, retrieval, dependency, or consistency problems justify it.

Key sources:

```text
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
docs/DEVELOPMENT_METHOD.md, version 0.3
docs/KNOWLEDGE_MAP.md
```

This change is meta-architectural. It changes how the project preserves and navigates its own knowledge, not the frozen Prototype V0 treatment architecture.
