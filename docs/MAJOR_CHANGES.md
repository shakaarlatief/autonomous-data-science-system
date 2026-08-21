# Major Changes

**Status:** Current selective structural history  
**Authority:** Navigation and project-history aid. Detailed decisions, foundations, specifications, checkpoints, final experiment reports, and Git history remain authoritative for their own scope.  
**Last reviewed:** 2026-08-21

## Purpose

This file records only changes that materially alter how the project is understood, built, evaluated, preserved, or continued. It is not a commit changelog.

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

The project moved from a broad vision to explicit theories for epistemic integrity, admissibility/risk, project state and revision, project initialization, knowledge activation, reusable knowledge, knowledge quality/evolution, and behavioral system evaluation.

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

The project deliberately chose to test a small explicit semantic architecture against strong simpler controls before building a large autonomous platform.

```text
B0: strong LLM + strong generic workflow
B1: B0 + same methodological knowledge supplied statically
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

## 2026-08-18: System-level LLM/system/human boundary became durable architecture

The project distinguished human-executed data science, interactive LLM-assisted data science, and system-mediated data science.

The LLM is one reasoning component inside ADS. Every explicit mechanism must justify its complexity empirically.

Key source:

```text
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
```

---

## 2026-08-18: Development preservation gained routing, promotion audits, and reconciliation

Development Method v0.3 introduced:

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

## 2026-08-18 to 2026-08-19: Prototype V0 gained validated supervision and observability separation

Held-out execution gained a condition-neutral runner/verifier/supervisor architecture and mechanically validated prospective automation.

The reusable execution principle became:

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

## 2026-08-19: Prototype V0 strongly falsified the current P0 design

Final pooled evidence:

```text
                         B0          B1          P0
Targeted mean           1.47        1.73        1.78
Strong targeted pass    0/10        0/10        0/10
Critical failure runs   0/10        0/10        0/10
Completed in budget    10/10       10/10        3/10
Budget exhausted        0/10        0/10        7/10
Median total tokens  122,544.5   120,564.5   260,370.0
```

Final classification:

> **STRONG FALSIFICATION OF THE CURRENT P0 DESIGN.**

The architectural consequence is simplification, not abandonment of the wider system vision.

The strongest scaling lesson became:

```text
what the SYSTEM should remember
    !=
what the LLM should receive on every reasoning call
```

Do not carry forward unchanged full typed state on every call, large always-on context/frontiers, generic recursive support reassessment, narrow path-sensitive trigger activation, or universal dependency reopening machinery.

Key sources:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
prototype_v0/README.md
docs/checkpoints/096_prototype_v0_final_strong_falsification_and_architecture_diagnostic_conclusion.md
```

---

## 2026-08-19: Post-V0 product vision became a professional interactive data-science operating environment

The project returned to the broader product goal before selecting another orchestration architecture.

The target became a professional environment in which ADS carries much of the methodological-navigation and project-memory burden while the human can inspect, discuss, select, override, guide, and approve work interactively.

Key source:

```text
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
```

---

## 2026-08-19: Product object model and professional developer workflow were concretized

The central separation became:

```text
OBJECTS
RELATIONS
EVENTS
VIEWS
```

with durable distinctions including:

```text
Investigation != Run
Evidence != Finding
Finding != Claim
Claim != Decision
current state != event history
workspace section != fundamental object
```

ADS should complement VS Code rather than replace it, and generated project code should remain independently runnable and professionally maintainable.

Key source:

```text
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
```

---

## 2026-08-19 to 2026-08-20: Methodological navigation became a bounded-horizon architecture

The methodological brain adopted:

```text
KNOWN
    -> APPLICABLE
    -> RELEVANT
    -> RECOMMENDED
    -> REQUIRED / BLOCKING
```

The **MethodologicalHorizon** separates a large global knowledge universe from the bounded project-specific slice relevant to current reasoning.

Reusable knowledge gained a promoted representation around:

```text
KnowledgeAsset
KnowledgeComponent
NarrativeFacet
KnowledgeRelation
Conditional KnowledgeRule
KnowledgeCollection
ExecutionCapability
```

Key sources:

```text
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
```

---

## 2026-08-20: V1 persistence/retrieval architecture and implementation tooling were selected empirically

The project accepted:

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

The first production persistence slice passed SQLite/Linux, SQLite/Windows, and PostgreSQL 18, including exact historical project-to-knowledge revision pinning.

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

This produced P-027 through P-029 and Specification 005. No agent framework or multi-agent architecture was selected; direct model calls remain a valid bakeoff outcome.

---

## 2026-08-20: Professional frontend became an early parallel V1 product track

Foundation 021 strengthened the interface requirement into a first-class product-quality commitment: ADS should be a modern, visually excellent, accessible, responsive professional analytical application rather than an end-stage dashboard or generic chat shell.

Specification 006 introduced the first frontend technical/visual evaluation contract. React + TypeScript + Vite, TanStack Router/Query/Table, an ADS-owned design system, Playwright, and Vitest became the leading hypothesis, while chart selection and final stack promotion remained empirical questions.

---

## 2026-08-20: Project Cockpit became the strongly preferred primary active-work interface

Human review exposed a missing product layer: ADS needed a primary place where the user actively works with the evolving data-science process, not only pages that inspect it.

Research 002 introduced the Project Cockpit as:

```text
living project-process map
+ native system interaction
+ focused analytical work surface
```

Checkpoint 117 confirmed:

```text
click meaningful work block
    -> smooth spatial focus
    -> perform real analytical work
    -> return to project context
```

Direct project views remain alternative entry/inspection paths rather than mandatory escape hatches.

---

## 2026-08-20 to 2026-08-21: Cockpit evolved into a scalable spatial operating surface

Successive human reviews and bounded implementation gates established:

```text
large two-dimensional project extent
horizontal + vertical navigation
true fullscreen
geometric zoom + fit/reset/recovery
native trackpad pan/pinch candidate
scalable Jump to + searchable project work
canvas-dominant floating composer/controls
compact fold-away primary HUD

ProjectWorld != ProjectCanvas
    surrounding world stays pannable
    semantic plane stays distinct
    neutral reserve does not become stage semantics

continuous finite grid world
viewport-aware semantic stage ruler
compact fold-away right-edge map controls
world-owned restrained ambient depth
collision-safe Jump/search relative to composer
```

The seventh review then supplied the missing real-laptop product evidence. Pinch was judged substantially smoother, Jump/search and stage orientation were accepted, and the remaining tiny occasional pinch hitch was explicitly classified as non-blocking polish. The only requested product adjustment was moderately faster pinch travel.

Pinch sensitivity was increased from `0.00135` to `0.0018` without changing the smoothing/anchoring architecture.

The first seventh-review browser gate exposed a reproducible stage-ruler timing defect under rapid zoom. The semantic source of truth was already correct, but ruler measurement could occur before zoomed geometry had fully settled. The implementation was repaired to synchronize after an additional animation frame.

Final validated head:

```text
2c3b522e2416d73c015ce5ec2a4560a227524dd9
```

Final gate:

```text
V1 frontend spike
run 155 / 32492536072

Ubuntu build + unit tests                 PASS
Windows build + unit tests                PASS
Chromium interaction/accessibility        PASS
controlled direct-view visual regression  PASS
```

---

## 2026-08-21: Project Cockpit interaction architecture was promoted

Checkpoint 126 closes the bounded Specification 007 interaction spike after seven real-browser human review cycles.

The promoted V1 interaction contract is now:

```text
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
```

Promoted architecture:

```text
Project Cockpit as primary immersive active-work model
living project-process projection
meaningful work-unit semantics
spatial focus into real reusable specialist workspaces
reachability != simultaneous mounting
FiniteNavigableGridWorld != SemanticProjectPlane
2D project navigation and recovery
bounded geometric zoom and native pinch capability
viewport-aware semantic stage orientation
scalable Jump/search project location
compact/fold-away immersive chrome
collision-safe floating surfaces
true fullscreen with graceful fallback
URL-addressable focus/deep-work state
keyboard accessibility and reduced-motion support
world-owned restrained ambient depth
```

Promotion deliberately does **not** freeze:

```text
remaining tiny pinch hitch
final pinch/zoom constants
final graph/canvas or gesture library
final auto-layout
final semantic zoom/grouping
final minimap
final stage taxonomy/widths
final stage-ruler material
permanent tool-rail styling
final ambient styling
final public URL contract
pan/zoom/HUD persistence
final visual identity
canonical Cockpit screenshot baseline
```

The Project Cockpit is therefore no longer the immediate blocking V1 track. The next priority is the governed PostgreSQL reusable-knowledge round-trip closure, followed by the agent-runtime bakeoff and retrieval/MethodologicalHorizon benchmark.

Key sources:

```text
docs/research/009_seventh_cockpit_human_review_pinch_responsiveness_and_interaction_promotion.md
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
docs/checkpoints/126_seventh_cockpit_review_validated_and_interaction_architecture_promoted.md
```

---

## 2026-08-20: Unexpected Session 02 boundary validated preservation but exposed routing drift

Session 02 reached the platform conversation-length limit immediately after Checkpoint 119 work was preserved.

Research 004, Specification 007, and Checkpoint 119 protected the substantive work, while incomplete reconciliation left stale routing in README/CURRENT_STATE/KNOWLEDGE_MAP/OPEN_QUESTIONS and provenance files.

Session 03 repaired the routing explicitly.

The incident demonstrated:

```text
checkpoint/specification preservation protects substantive knowledge
    and
current routing/reconciliation remains necessary for reliable continuation
```

Key source:

```text
docs/checkpoints/120_unplanned_session_boundary_reconciliation_and_v1_continuity_restored.md
```
