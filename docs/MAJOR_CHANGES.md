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

---

## 2026-08-19: Post-V0 product vision became a professional interactive data-science workspace

After closing V0, the project deliberately returned to the broader product goal before choosing another backend architecture.

The target experience was made concrete as a professional interactive project workspace in which the system itself carries much of the methodological-navigation burden while the user can inspect, discuss, select, override, and guide the work.

Important product ideas include:

```text
recommended analyses
relevant option space
full methodological knowledge catalog
living project memory
living reports
project replay evaluation
configurable human involvement
```

A central distinction is:

```text
what the system remembers
    !=
what the LLM receives on every reasoning call
```

Key sources:

```text
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/checkpoints/097_post_v0_product_vision_concretized_as_interactive_methodological_workspace.md
```

---

## 2026-08-19: Product object model and professional developer-workflow integration were concretized

The project next derived a candidate object model from the desired user experience rather than from a storage technology or state-machine implementation.

The conceptual separation is now:

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
Method
Proposal / Investigation / Run / Evidence / Decision
Report / ReportSection
Event / Relation
```

The design also established two new professional-workflow principles:

```text
P-023
The system should complement the professional developer workbench rather than replace it.

P-024
Generated project code should remain independently runnable and professionally maintainable.
```

The current conceptual responsibility split is:

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

System-triggered and manually triggered executions should preferentially share the same reproducible run contract. Git/GitHub should be deeply integrated without becoming the storage substrate for every large artifact.

Local-first execution is a strong current hypothesis for typical projects, but remains deliberately uncommitted as a universal architecture because future remote/cloud/cluster execution should remain possible.

Key sources:

```text
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
docs/checkpoints/098_project_object_model_and_professional_developer_workflow_concretized.md
docs/PRINCIPLES.md, P-023 and P-024
```

---

## 2026-08-19: Methodological-navigation brain became a concrete relevance architecture

The project moved from the broad idea of a reusable method catalog to a more explicit candidate architecture for methodological navigation.

The brain is now understood as potentially containing multiple reusable knowledge types:

```text
methods
question templates
decision frameworks
invariants / hard rules
failure modes
investigation patterns
interpretation knowledge
follow-up / dependency knowledge
```

A staged relevance model was introduced:

```text
KNOWN
    -> APPLICABLE
    -> RELEVANT
    -> RECOMMENDED
    -> REQUIRED / BLOCKING
```

A new concept, the **methodological horizon**, separates a potentially large global knowledge base from the small project-specific slice that should be evaluated and surfaced at a particular moment.

The current candidate flow combines explicit filtering where prerequisites or hard rules are reliable with flexible reasoning for semantic applicability, relevance, tradeoffs, and prioritization.

Recommendation rationale should be inspectable, and reusable knowledge should eventually retain scope, provenance, maturity, counterexamples, and challenge history. Methodological meaning should remain separate from concrete execution templates.

The brain should also remain open-world: flexible reasoning may identify important concerns absent from the explicit catalog, creating candidate knowledge gaps for later review and promotion.

Key sources:

```text
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/checkpoints/099_methodological_navigation_brain_promoted_and_session_rotation_recommended.md
```

---

## 2026-08-20: Reusable methodological knowledge gained a promoted representation architecture

The methodological-navigation design moved from a general relevance architecture to a concrete reusable-knowledge representation that survived two explicit stress-test rounds.

The promoted representation distinguishes:

```text
KnowledgeAsset
KnowledgeComponent
NarrativeFacet
KnowledgeRelation
Conditional KnowledgeRule
KnowledgeCollection
project object references/influence
criterion Findings
ExecutionCapability
Views
```

Promoted principles:

```text
P-025
Reusable knowledge identity/granularity should remain separate from reasoning function.

P-026
Static methodological relationships should remain separate from conditional guidance rules.
```

Key sources:

```text
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
docs/checkpoints/104_adversarial_review_of_candidate_knowledge_representation.md
docs/checkpoints/105_refined_representation_second_stress_test.md
```

---

## 2026-08-20: V1 implementation requirements were derived before technology selection

The project derived 59 technology-neutral requirements before comparing databases or retrieval architectures.

This changed architecture selection from technology preference into a concrete workload decision.

Key source:

```text
docs/checkpoints/107_implementation_requirements_for_methodological_knowledge_subsystem.md
```

---

## 2026-08-20: SQLite-centered local-first V1 persistence/retrieval architecture selected

After explicit requirements and architecture comparison, D-028 selected:

```text
SQLite operational store
FTS5 rebuildable lexical index
rebuildable embeddings with initial exact search
application-level conditional-rule evaluator
selective bounded LLM context assembly
filesystem/Git/artifact storage for large/code artifacts
```

Dedicated graph/vector services, external rules engines, PostgreSQL by default, ANN infrastructure, and multi-store architecture remain deferred until measured requirements justify them.

PostgreSQL + pgvector remains the preferred first migration family if the SQLite envelope is exceeded.

Key sources:

```text
docs/DECISIONS.md, D-028
docs/checkpoints/108_v1_architecture_comparison_and_sqlite_centered_selection.md
experiments/architecture_spikes/sqlite_v1_viability.py
```

---

## 2026-08-20: V1 persistence moved from architecture into production code

The project selected SQLAlchemy Core + Alembic, established standards-based Python/uv tooling, and then implemented the first real V1 persistence vertical slice.

The production slice demonstrated on SQLite/Linux, SQLite/Windows, and PostgreSQL 18 that exact historical project-to-knowledge references survive later knowledge revision changes.

Key sources:

```text
docs/DECISIONS.md, D-029 and D-030
docs/specifications/001_v1_sqlite_technical_architecture.md
docs/specifications/002_v1_persistence_tooling_standard.md
docs/specifications/003_v1_python_project_and_dependency_tooling.md
docs/checkpoints/114_first_production_v1_persistence_vertical_slice_passed.md
```

---

## 2026-08-20: Reusable knowledge gained an accepted deterministic interchange contract

D-031 and Specification 004 now define the accepted V1 interchange as:

```text
JSON
+ JSON Schema Draft 2020-12
+ application semantic validation
+ deterministic serialization
```

The heterogeneous benchmark corpus passed KI-01 through KI-10 across Linux/Windows and Python 3.12-3.14.

Normal candidate/benchmark import cannot silently create accepted methodological authority.

The separate governed database round-trip is still being validated. Its first PostgreSQL attempt exposed a real portability defect in one overlong physical constraint name. The defect was localized and corrected; final corrected PostgreSQL confirmation remains pending at Checkpoint 116.

Key sources:

```text
docs/DECISIONS.md, D-031
docs/specifications/004_v1_reusable_knowledge_interchange.md
docs/checkpoints/115_reusable_knowledge_interchange_contract_validated.md
docs/checkpoints/116_agentic_ecosystem_audit_and_frontend_track_started.md
```

---

## 2026-08-20: Agentic ecosystem audit separated ADS semantics from runtime/protocol infrastructure

A current 2026 ecosystem audit examined MCP, OpenAI Agents SDK, LangGraph, Microsoft Agent Framework, Google ADK, A2A, AG-UI, and observability patterns.

The durable conclusion is:

```text
ADS owns
    project semantics
    methodological semantics
    governance
    provenance
    Findings / Questions / Decisions
    methodological horizon semantics

ADS should preferentially adopt/test
    agent runtime
    durable workflow/checkpoint machinery
    MCP interoperability
    AG-UI transport if useful
    A2A only when remote agents are real
    standard operational observability
```

This produced:

```text
P-027
Agent frameworks and interoperability protocols are infrastructure,
not domain authority.

P-028
Prefer deterministic software for explicit work and agent reasoning
for genuine ambiguity.
```

No agent framework or multi-agent architecture was selected. Specification 005 defines an ADS-shaped bakeoff in which even a no-framework result remains valid.

Key sources:

```text
docs/research/001_2026_agentic_ecosystem_and_integration_architecture_audit.md
docs/specifications/005_v1_agent_runtime_and_interoperability_bakeoff.md
docs/PRINCIPLES.md, P-027 and P-028
```

---

## 2026-08-20: Professional frontend became an early parallel V1 product track

The product-interface requirement was strengthened from "professional workspace" into a first-class visual/product quality commitment.

Foundation 021 now requires a modern, visually excellent, premium professional analytical interface with strong typography, carefully controlled density, accessibility, responsive professional desktop layouts, coherent light/dark modes, high-quality analytical visualization, and deliberately designed loading/empty/error/offline/approval states.

P-029 makes the interface a reasoning/control/quality surface, not an end-stage presentation layer.

Specification 006 defines the first visual/technical spike. The leading but not yet accepted hypothesis is:

```text
React + TypeScript + Vite
TanStack Router / Query / Table
shadcn/ui source-distributed components
ADS-owned design system
Playwright + Vitest
```

ECharts versus Plotly remains an empirical comparison. AG-UI will be tested as an adapter rather than a domain protocol. Tauri is deferred until the browser shell and Python service boundary are stable.

Key sources:

```text
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
docs/specifications/006_v1_frontend_architecture_and_visual_spike.md
docs/PRINCIPLES.md, P-029
docs/checkpoints/116_agentic_ecosystem_audit_and_frontend_track_started.md
```
