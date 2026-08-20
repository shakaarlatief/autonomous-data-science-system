# Major Changes

**Status:** Current selective structural history  
**Authority:** Navigation and project-history aid. Detailed decisions, foundations, specifications, checkpoints, final experiment reports, and Git history remain authoritative for their own scope.  
**Last reviewed:** 2026-08-20

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

## 2026-08-09: Prototype V0 became a preregistered falsification experiment

The project deliberately chose to test a small explicit semantic architecture against strong simpler controls rather than building a large autonomous platform first.

```text
B0: strong LLM + strong generic workflow
B1: B0 + the same methodological knowledge supplied statically
P0: same model + typed state + activation + safeguards + dependency repair
    + state-driven action selection
```

The H1/H2 bundles, run order, provider/model configuration, budgets, replacement policy, semantic rubric, blinded judging procedure, and falsification criteria were frozen before P0 implementation.

Key sources:

```text
docs/foundations/010_minimum_falsification_prototype_and_experimental_contract.md
docs/foundations/011_prototype_v0_technical_specification.md
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
```

---

## 2026-08-18: System-level LLM/system/human boundary was promoted into durable architecture

The project distinguished:

```text
human-executed data science
human + interactive LLM data science
system-mediated data science
```

The LLM is one reasoning component inside the system, while every explicit mechanism must justify its complexity empirically.

Key source:

```text
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
```

---

## 2026-08-18: Development Method v0.3 introduced explicit preservation routing and reconciliation

Actual project growth exposed risks in discoverability, implicit promotion, and canonical duplication/drift.

Version 0.3 introduced:

```text
checkpoint promotion audits
KNOWLEDGE_MAP routing
periodic reconciliation
authority/maturity conventions
MAJOR_CHANGES structural history
separation of CURRENT_STATE from detailed experiment ledgers
```

Git + Markdown remains the development-preservation substrate until real retrieval, dependency, consistency, concurrency, or automation problems justify more complex infrastructure.

Key sources:

```text
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
docs/DEVELOPMENT_METHOD.md
docs/KNOWLEDGE_MAP.md
```

---

## 2026-08-18 to 2026-08-19: Prototype V0 gained validated supervision and execution/observability separation

Held-out execution gained a condition-neutral runner/verifier/supervisor architecture and mechanically validated prospective automation.

Long-running experiment operations also exposed the reusable principle:

```text
execution / reasoning
    -> persisted state/events
    -> read-only observability
    -> human interface
```

Key sources:

```text
docs/foundations/015_held_out_supervision_and_mechanical_verification_architecture.md
docs/foundations/016_execution_observability_separation.md
docs/PRINCIPLES.md, P-022
```

---

## 2026-08-19: Prototype V0 completed and strongly falsified the current P0 design

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

P0's targeted semantic gain over B1 was only `+0.05`, while P0 used `2.160x` B1's median tokens and completed only `3/10` runs within budget.

Final classification:

> **STRONG FALSIFICATION OF THE CURRENT P0 DESIGN.**

The architectural consequence is simplification, not abandonment of the wider system vision.

Do not carry forward unchanged:

```text
full typed state resent every reasoning cycle
large always-on state/relation context
generic support-reassessment propagation
path-sensitive tag-trigger activation
universal dependency reopening machinery
full P0 frontier representation
```

The strongest scaling lesson became:

```text
what the SYSTEM should remember
    !=
what the LLM should receive on every reasoning call
```

Key sources:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
prototype_v0/README.md
docs/checkpoints/096_prototype_v0_final_strong_falsification_and_architecture_diagnostic_conclusion.md
```

---

## 2026-08-19: Post-V0 product vision became a professional interactive data-science operating environment

The project deliberately returned to the broader product goal before choosing another orchestration architecture.

The target became a professional project environment in which the system carries much of the methodological-navigation and project-memory burden while the user can inspect, discuss, select, override, and guide work interactively.

Key sources:

```text
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/checkpoints/097_post_v0_product_vision_concretized_as_interactive_methodological_workspace.md
```

---

## 2026-08-19: Product object model and professional developer workflow were concretized

The project derived a candidate object model from the desired user experience rather than from a storage technology.

The central separation became:

```text
OBJECTS
RELATIONS
EVENTS
VIEWS
```

with durable distinctions such as:

```text
Investigation != Run
Evidence != Finding
Finding != Claim
Claim != Decision
current state != event history
workspace section != fundamental object
```

The system should complement VS Code rather than replace it, and generated project code should remain independently runnable and professionally maintainable.

Key sources:

```text
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
docs/PRINCIPLES.md, P-023 and P-024
```

---

## 2026-08-19 to 2026-08-20: Methodological navigation became a bounded-horizon architecture

The methodological brain became broader than a method catalog and adopted the staged relevance model:

```text
KNOWN
    -> APPLICABLE
    -> RELEVANT
    -> RECOMMENDED
    -> REQUIRED / BLOCKING
```

The **MethodologicalHorizon** concept separates a large global knowledge universe from the bounded project-specific slice relevant to current reasoning.

Reusable methodological knowledge then gained a promoted representation around:

```text
KnowledgeAsset
KnowledgeComponent
NarrativeFacet
KnowledgeRelation
Conditional KnowledgeRule
KnowledgeCollection
ExecutionCapability
```

with two promoted principles:

```text
knowledge identity/granularity != reasoning function
static semantic relation != conditional methodological rule
```

Key sources:

```text
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
docs/PRINCIPLES.md, P-025 and P-026
```

---

## 2026-08-20: V1 persistence/retrieval architecture and implementation tooling were selected empirically

After deriving technology-neutral requirements, the project selected:

```text
D-028
SQLite-centered local-first operational architecture
FTS5 lexical retrieval seam
rebuildable embeddings / initial exact semantic retrieval
application rule evaluation
selective LLM context assembly

D-029
SQLAlchemy Core 2.0 + Alembic 1.x

D-030
pyproject.toml + uv + committed uv.lock + uv_build
```

The first production persistence slice then passed on SQLite/Linux, SQLite/Windows, and PostgreSQL 18, including exact historical project-to-knowledge revision pinning.

Key sources:

```text
docs/DECISIONS.md, D-028 through D-030
docs/specifications/001_v1_sqlite_technical_architecture.md
docs/specifications/002_v1_persistence_tooling_standard.md
docs/specifications/003_v1_python_project_and_dependency_tooling.md
docs/checkpoints/114_first_production_v1_persistence_vertical_slice_passed.md
```

---

## 2026-08-20: Reusable knowledge gained an accepted deterministic interchange contract

D-031 and Specification 004 established:

```text
JSON
+ JSON Schema Draft 2020-12
+ application semantic validation
+ deterministic normalization/serialization
```

Candidate/benchmark import cannot silently create accepted methodological authority.

The heterogeneous benchmark corpus passed KI-01 through KI-10 across Linux/Windows and Python 3.12-3.14.

A richer governed import/accept/export round-trip was then implemented. SQLite passes; the last persisted PostgreSQL 18 round-trip status remains failed after a localized identifier-length portability defect. The defect was fixed and revalidation was triggered, but closure still requires a persisted corrected PostgreSQL PASS.

Key sources:

```text
docs/DECISIONS.md, D-031
docs/specifications/004_v1_reusable_knowledge_interchange.md
docs/checkpoints/115_reusable_knowledge_interchange_contract_validated.md
experiments/architecture_spikes/V1_KNOWLEDGE_ROUNDTRIP_STATUS.md
```

---

## 2026-08-20: Agentic ecosystem audit separated ADS semantics from replaceable runtime infrastructure

The 2026 audit concluded:

```text
ADS owns
    project semantics
    methodological semantics
    governance
    provenance
    Questions / Findings / Decisions
    methodological-horizon meaning

Replaceable infrastructure includes
    agent runtimes
    runtime checkpointing
    MCP
    AG-UI adapters
    A2A when independently deployed agents are real
```

This produced P-027 through P-029 and Specification 005. No agent framework or multi-agent architecture was selected; a simple direct-model-call result remains valid if frameworks do not earn their complexity.

Key sources:

```text
docs/research/001_2026_agentic_ecosystem_and_integration_architecture_audit.md
docs/specifications/005_v1_agent_runtime_and_interoperability_bakeoff.md
docs/PRINCIPLES.md, P-027 through P-029
```

---

## 2026-08-20: Professional frontend became an early parallel V1 product track

Foundation 021 strengthened the interface requirement into a first-class product-quality commitment: ADS should be a modern, visually excellent, accessible, responsive professional analytical application rather than an end-stage dashboard or generic chat shell.

Specification 006 introduced the first frontend technical/visual evaluation contract. React + TypeScript + Vite, TanStack Router/Query/Table, an ADS-owned design system, Playwright, and Vitest became the leading implementation hypothesis, while chart selection and final stack promotion remained empirical questions.

Key sources:

```text
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
docs/specifications/006_v1_frontend_architecture_and_visual_spike.md
```

---

## 2026-08-20: Project Cockpit became the strongly preferred primary active-work interface

Human review of the first conventional project-view frontend exposed a missing product layer: the system needed a primary place where the user actively works with the evolving data-science process, not only pages that inspect it.

Research 002 introduced the Project Cockpit as:

```text
living project-process map
+ native system interaction
+ focused analytical work surface
```

Checkpoint 117 then strongly confirmed the interaction:

```text
click meaningful work block
    -> smooth spatial focus
    -> perform real analytical work
    -> return to project context
```

The design was strengthened so deep Data, EDA, Validation, Modeling, Evaluation, and other work can be entered inside the same immersive experience using reusable specialist workspaces. Direct project views remain alternative entry/inspection paths rather than mandatory escape hatches.

The first executable Cockpit spike passed cross-platform build, browser interaction, and accessibility gates without selecting a graph/canvas framework.

Key sources:

```text
docs/research/002_primary_project_cockpit_interface_concept.md
docs/research/003_unified_cockpit_workspace_and_spatial_focus_architecture.md
docs/specifications/007_v1_unified_project_cockpit_interaction_spike.md
docs/checkpoints/117_unified_cockpit_workspace_direction_confirmed.md
docs/checkpoints/118_first_unified_cockpit_interaction_spike_automated_gate_passed.md
```

---

## 2026-08-20: Second Cockpit review established immersive-scale and true-fullscreen requirements

The second real-browser review accepted the stage-zone visual grammar and dark technical operating-surface direction while exposing a real scalability defect: lower/right work could become inaccessible behind fixed floating UI.

The Cockpit direction therefore gained explicit requirements for:

```text
two-dimensional project-space navigation
horizontal and vertical growth
fit/reset/jump navigation
future semantic zoom/grouping
collision-safe floating surfaces
compact/expandable Cockpit HUD
stage orientation at the top of the operating viewport
true browser fullscreen with graceful fallback
keyboard-accessible recovery
```

The operating principle became:

```text
whole practical viewport = Cockpit operating surface
```

without implying that every project object or deep workspace remains mounted simultaneously.

Research 004 and Specification 007 candidate v0.2 govern the next bounded implementation slice. No canvas library, auto-layout algorithm, final semantic-zoom system, final stage taxonomy, or final visual identity is selected yet.

Key sources:

```text
docs/research/004_cockpit_spatial_scalability_immersive_chrome_and_fullscreen.md
docs/specifications/007_v1_unified_project_cockpit_interaction_spike.md
docs/checkpoints/119_cockpit_spatial_scalability_and_true_fullscreen_requirements_confirmed.md
```

---

## 2026-08-20: Unexpected Session 02 boundary validated preservation but exposed routing drift

Session 02 reached the platform conversation-length limit immediately after Checkpoint 119 work was preserved.

The substantive design survived because Research 004, Specification 007 v0.2, and Checkpoint 119 already existed in the repository. However, `README`, `CURRENT_STATE`, `KNOWLEDGE_MAP`, `OPEN_QUESTIONS`, active session provenance, and this major-changes ledger had not all completed their normal end-of-session reconciliation.

Session 03 therefore performed an explicit continuity repair rather than attempting to recreate the missing chat.

The incident validates both sides of the preservation model:

```text
checkpoint/specification preservation protected substantive knowledge

and

current routing/reconciliation still matters for reliable new-session reconstruction
```

Key sources:

```text
docs/CONTINUITY.md
docs/checkpoints/120_unplanned_session_boundary_reconciliation_and_v1_continuity_restored.md
```
