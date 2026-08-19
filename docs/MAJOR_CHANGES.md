# Major Changes

**Status:** Current selective structural history  
**Authority:** Navigation and project-history aid. Detailed decisions, foundations, specifications, checkpoints, final experiment reports, and Git history remain authoritative for their own scope.  
**Last reviewed:** 2026-08-19

## Purpose

This file records only changes that materially alter how the project is understood, built, evaluated, preserved, or continued.

It is not a commit changelog.

---

## 2026-08-07: Dedicated project and layered repository preservation established

The Autonomous Data Science System became a dedicated repository separate from individual data projects.

The initial preservation model distinguished:

```text
chat as exploratory workspace
repository as durable source of truth
canonical documents
foundational design memos
checkpoints
historical provenance
```

This established the maxim:

> The chat is where we think. The repository is where the system remembers.

Key sources:

```text
docs/foundations/001_initial_vision_and_reasoning.md
docs/DECISIONS.md, D-001 through D-010
```

---

## 2026-08-08: Checkpointing and chat rotation became proactive AI responsibilities

Development Method v0.2 made the AI design collaborator responsible for detecting natural checkpoints, preserving important uncheckpointed reasoning, and recommending session rotation when continuity risk becomes material.

Key sources:

```text
docs/DECISIONS.md, D-018 and D-020
docs/DEVELOPMENT_METHOD.md
docs/CONTINUITY.md
```

---

## 2026-08-08 to 2026-08-09: Core system theory expanded into dedicated foundations

The project moved from a broad vision to explicit theories for:

```text
epistemic integrity
admissibility and risk-sensitive assurance
project state and dependency-aware revision
project initialization
knowledge activation
reusable knowledge representation
knowledge quality and evolution
behavioral system evaluation
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

## 2026-08-09: Prototype V0 became a falsification experiment

The project deliberately chose to test a small explicit semantic architecture against strong simpler controls rather than building a large autonomous platform first.

```text
B0: strong LLM + strong generic workflow
B1: B0 + the same methodological knowledge supplied statically
P0: same model + typed state + activation + safeguards + dependency repair
    + state-driven action selection
```

The experiment was explicitly designed so P0 could lose and be simplified.

Key sources:

```text
docs/foundations/010_minimum_falsification_prototype_and_experimental_contract.md
docs/foundations/011_prototype_v0_technical_specification.md
```

---

## 2026-08-09: Held-out evaluation was preregistered before P0 implementation

The H1/H2 bundles, 30-run order, common model/provider configuration, budgets, replacement policy, semantic rubric, blinded judging procedure, and continuation/falsification criteria were frozen before P0 implementation.

Key source:

```text
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
```

---

## 2026-08-09 to 2026-08-18: The system-level LLM/system/human boundary became explicit and durable

The project distinguished:

```text
human-executed data science
human + interactive LLM data science
system-mediated data science
```

The key implication is that the LLM is one reasoning component inside the system, while every explicit mechanism must still justify its complexity empirically.

The idea originated in Checkpoint 22 and was later promoted to Foundation 013 after the project recognized that historically preserved knowledge can still become conceptually buried.

Key sources:

```text
docs/checkpoints/022_system_level_abstraction_and_reusable_reasoning_vision.md
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
```

---

## 2026-08-18: Development Method v0.3 introduced an explicit knowledge-preservation architecture

Actual project growth exposed risks in discoverability, implicit promotion, and canonical duplication/drift.

Version 0.3 introduced:

```text
checkpoint promotion audits
KNOWLEDGE_MAP routing
periodic stage-boundary reconciliation
lightweight authority/maturity conventions
MAJOR_CHANGES structural history
separation of CURRENT_STATE from detailed experiment ledgers
explicit deferral criteria for more advanced knowledge infrastructure
```

Git + Markdown remains the current preservation substrate until demonstrated retrieval, dependency, consistency, concurrency, or automation problems justify more complex infrastructure.

Key sources:

```text
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
docs/DEVELOPMENT_METHOD.md
docs/KNOWLEDGE_MAP.md
```

---

## 2026-08-18: Prototype V0 gained validated external supervision and mechanical verification

After early held-out execution showed that manual transport/bookkeeping no longer added scientific value, the project introduced a condition-neutral external layer:

```text
heldout_runner.py
    frozen one-attempt executor

heldout_verifier.py
    read-only mechanical verification

heldout_supervisor.py
    bounded sequential orchestration
```

The verifier was retrospectively validated against all existing attempts before prospective use. This automated repetitive experiment operations without changing treatment semantics.

Key sources:

```text
docs/foundations/015_held_out_supervision_and_mechanical_verification_architecture.md
docs/checkpoints/082_held_out_supervisor_retroactively_validated_and_frozen_for_live_use.md
```

---

## 2026-08-19: Execution and observability were separated as a system-level principle

Running long treatment and semantic-evaluation processes exposed a reusable design principle:

```text
execution / reasoning
    -> persisted structured state or events
    -> read-only observability
    -> human interface
```

Detailed timestamps, heartbeats, elapsed time, progress rendering, and future dashboards belong preferentially in a sidecar observer rather than the trusted execution path.

Key sources:

```text
docs/PRINCIPLES.md, P-022
docs/foundations/016_execution_observability_separation.md
docs/checkpoints/091_execution_observability_separation_promoted_and_semantic_monitor_added.md
```

---

## 2026-08-19: Prototype V0 completed and strongly falsified the current P0 design

All treatment and semantic evidence completed under the preregistered protocol:

```text
30 / 30 treatment slots resolved
34 / 34 persisted attempts mechanically verified PASS
60 / 60 blinded semantic judge passes completed
0 manual semantic adjudications
blinded evidence frozen before condition decoding
```

The final pooled comparison was:

```text
                         B0          B1          P0
Targeted mean           1.47        1.73        1.78
Strong targeted pass    0/10        0/10        0/10
Critical failure runs   0/10        0/10        0/10
Completed in budget    10/10       10/10        3/10
Budget exhausted        0/10        0/10        7/10
Median total tokens  122,544.5   120,564.5   260,370.0
```

P0's targeted semantic gain over B1 was only `+0.05`, far below the preregistered material-reliability threshold. B1 and P0 had identical critical-failure and strong-targeted-pass counts, while P0 used `2.160x` B1's median tokens.

Post-unblinding P0 diagnostics found no false action blocks, no critical over-invalidation, and no held-out-specific hard coding. P0 dependency repair was precise, but the same repair behavior was already near ceiling in B1. The current activation mechanism also showed path sensitivity, and generic support-reassessment produced avoidable internal state churn.

Foundation 012's reliability-cost strong-falsification clause is therefore met.

Final classification:

> **STRONG FALSIFICATION OF THE CURRENT P0 DESIGN.**

The architectural consequence is simplification, not abandonment of the broader system vision.

Do not continue unchanged:

```text
full typed state resent every reasoning cycle
large always-on state/relation context
generic support-reassessment propagation
path-sensitive tag-trigger activation
universal dependency reopening machinery
full P0 frontier representation
```

The next design stage starts from the strong B1 baseline and asks what smallest low-overhead mechanism can improve reliability on harder, longer, changing project trajectories.

Key sources:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
prototype_v0/README.md
docs/checkpoints/096_prototype_v0_final_strong_falsification_and_architecture_diagnostic_conclusion.md
```
