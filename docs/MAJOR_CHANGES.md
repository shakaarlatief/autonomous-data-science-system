# Major Changes

**Status:** Current selective structural history  
**Authority:** Navigation and project-history aid. Detailed decisions, foundations, specifications, checkpoints, final experiment reports, and Git history remain authoritative for their own scope.  
**Last reviewed:** 2026-08-23

## Purpose

This file records only changes that materially alter how the project is understood, built, evaluated, preserved, or continued. It is not a commit changelog.

---

## 2026-08-07: Dedicated project and layered repository preservation established

The Autonomous Data Science System became a dedicated repository separate from individual data projects. The initial preservation model separated chat exploration from durable repository authority and introduced canonical documents, foundations, checkpoints, and historical provenance.

Core maxim:

> The chat is where we think. The repository is where the system remembers.

Key sources:

```text
docs/foundations/001_initial_vision_and_reasoning.md
docs/DECISIONS.md, D-001 through D-010
```

---

## 2026-08-08: Checkpointing and chat rotation became proactive AI responsibilities

Development Method v0.2 made the AI design collaborator responsible for detecting natural preservation checkpoints and continuity risk instead of relying on the user to remember repository updates.

Key sources:

```text
docs/DECISIONS.md, D-018 and D-020
docs/DEVELOPMENT_METHOD.md
docs/CONTINUITY.md
```

---

## 2026-08-08 to 2026-08-09: Core system theory expanded into dedicated foundations

The project developed explicit theories for epistemic integrity, admissibility/risk, project state and revision, project initialization, knowledge activation, reusable knowledge, knowledge evolution, and behavioral system evaluation.

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

The project chose to test a bounded explicit semantic architecture against strong simpler controls before building a large autonomous platform.

```text
B0: strong LLM + strong generic workflow
B1: B0 + same methodological knowledge supplied statically
P0: same model + typed state + activation + safeguards + dependency repair
    + state-driven action selection
```

The benchmark, run order, model/provider configuration, budgets, judging procedure, and falsification criteria were frozen before P0 implementation.

Key sources:

```text
docs/foundations/010_minimum_falsification_prototype_and_experimental_contract.md
docs/foundations/011_prototype_v0_technical_specification.md
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
```

---

## 2026-08-18: System-level LLM/system/human boundary became durable architecture

The LLM became explicitly one flexible reasoning component inside ADS. System-managed memory, provenance, deterministic guarantees, execution coordination, and human control must remain separate concerns, and every explicit mechanism must justify its complexity empirically.

Key source:

```text
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
```

---

## 2026-08-18: Development preservation gained routing, promotion audits, and reconciliation

Development Method v0.3 introduced checkpoint promotion audits, `KNOWLEDGE_MAP`, periodic reconciliation, authority/maturity conventions, `MAJOR_CHANGES`, and explicit separation of current state from detailed experiment ledgers.

Git + Markdown remains the development-preservation substrate until observed retrieval, consistency, dependency, concurrency, or automation problems justify more complex infrastructure.

Key sources:

```text
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
docs/DEVELOPMENT_METHOD.md
docs/KNOWLEDGE_MAP.md
```

---

## 2026-08-18 to 2026-08-19: Prototype V0 gained validated supervision and observability separation

Held-out execution gained a condition-neutral runner/verifier/supervisor architecture and mechanically validated prospective automation.

Reusable execution principle:

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

The architectural consequence was simplification, not abandonment of the wider system vision. The strongest scaling lesson became:

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

## 2026-08-19: Post-V0 vision became a professional interactive data-science operating environment

The target became a professional environment in which ADS carries much of the methodological-navigation and project-memory burden while the human can inspect, discuss, select, override, guide, and approve work interactively.

Key source:

```text
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
```

---

## 2026-08-19: Product object model and developer workflow were concretized

The central model became:

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

The `MethodologicalHorizon` separates a large global knowledge universe from the bounded project-specific slice plausibly relevant to current reasoning. Reusable knowledge gained promoted representation around assets, components, narrative facets, relations, conditional rules, collections, and separate execution capabilities.

Key sources:

```text
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
```

---

## 2026-08-20: V1 local-first persistence and Python tooling were selected empirically

The project accepted:

```text
D-028  SQLite-centered local-first operational architecture
D-029  SQLAlchemy Core 2.0 + Alembic 1.x
D-030  pyproject.toml + uv + committed uv.lock + uv_build
```

The first production persistence slice passed SQLite/Linux, SQLite/Windows, and PostgreSQL 18, including exact historical project-to-knowledge revision pinning.

Key sources:

```text
docs/DECISIONS.md, D-028 through D-030
docs/specifications/001_v1_sqlite_technical_architecture.md
docs/specifications/002_v1_persistence_tooling_standard.md
docs/specifications/003_v1_python_project_and_dependency_tooling.md
```

---

## 2026-08-20 to 2026-08-21: Reusable knowledge interchange and governed round-trip became operational

D-031 and Specification 004 established deterministic JSON + JSON Schema 2020-12 interchange, semantic validation, deterministic normalization/serialization, and explicit candidate-versus-accepted governance.

The richer governed round-trip then closed across:

```text
SQLite / Ubuntu     PASS
SQLite / Windows    PASS
PostgreSQL 18       PASS
```

Checkpoint 127 closes the current governed persistence/interchange seam.

Key sources:

```text
docs/DECISIONS.md, D-031
docs/specifications/004_v1_reusable_knowledge_interchange.md
experiments/architecture_spikes/V1_KNOWLEDGE_ROUNDTRIP_RESULT.md
docs/checkpoints/127_governed_knowledge_roundtrip_closed_across_sqlite_and_postgresql.md
```

---

## 2026-08-20 to 2026-08-21: Project Cockpit became the promoted primary active-work interaction model

Foundation 021 made the interface a first-class reasoning/control surface. Successive bounded spikes and seven real-browser human review cycles evolved the Cockpit into a scalable spatial operating surface with 2D navigation, bounded zoom, native pinch, scalable Jump/search, floating composer/controls, compact fold-away chrome, fullscreen, and collision-safe surfaces.

Specification 008 promoted the core interaction architecture. Final canvas/gesture libraries, auto-layout, semantic zoom/grouping, minimap, stage taxonomy, visual identity, and final frontend/chart choices remain open.

Key sources:

```text
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
docs/checkpoints/126_seventh_cockpit_review_validated_and_interaction_architecture_promoted.md
docs/checkpoints/130_post_promotion_cockpit_normal_window_and_pinch_polish_gate_passed.md
```

---

## 2026-08-20: Unexpected Session 02 boundary validated preservation but exposed routing drift

Session 02 reached the platform conversation-length limit after substantive Cockpit work had been preserved but before final routing reconciliation. Session 03 reconstructed from repository authority and repaired stale current routing through Checkpoint 120.

The incident demonstrated that substantive preservation and current routing are separate requirements.

Key source:

```text
docs/checkpoints/120_unplanned_session_boundary_reconciliation_and_v1_continuity_restored.md
```

---

## 2026-08-22: Initial V1 reasoning runtime selected after executable bakeoff

Specification 005 compared ADS-owned direct model calls, OpenAI Agents SDK 0.19.4, and LangGraph 1.2.10 as real ADS-shaped runtime paths.

D-032 accepts:

```text
OpenAI Agents SDK
    behind an ADS-owned ReasoningRuntime port
    validated starting package openai-agents==0.19.4
```

Direct model calls remain the fallback/reference path. LangGraph remains a possible future durability escalation. No final LLM provider/model or multi-agent architecture is selected.

Key sources:

```text
docs/DECISIONS.md, D-032
docs/specifications/005_v1_agent_runtime_and_interoperability_bakeoff.md
docs/checkpoints/133_v1_reasoning_runtime_selected_and_bakeoff_closed.md
```

---

## 2026-08-22: Retrieval progressed from lexical baseline to explained MethodologicalHorizon

The bounded retrieval/Horizon program produced:

```text
Checkpoint 135
    lexical RH-L Recall@3 1.00 / MRR 1.00

Checkpoint 137
    dense semantic comparator recovered class-imbalance but lost ecdf
    dense-only did not replace lexical

Checkpoint 139
    equal-weight RRF preserved complementary signals
    RH-S Recall@3 1.00 / MRR 0.875

Checkpoint 141
    accepted-current one-hop relation expansion
    TRUE / FALSE / UNKNOWN applicability
    POSSIBLY_APPLICABLE / INAPPLICABLE / MISSING_CONTEXT
```

The key executable semantic invariant is:

```text
unknown != false
```

The hybrid result remains complementarity evidence, not permanent selection of FastEmbed, BGE, RRF, vector persistence, ANN, or reranking infrastructure.

---

## 2026-08-22: Selective MethodologicalContextPack validated the system/model context boundary

Specification 013 tested:

```text
explicit task reasoning functions
    -> primary Horizon matches
    -> bounded REQUIRES_CONCEPT support
    -> hard max_assets budget
    -> exact accepted-current compact reasoning projection
    -> MethodologicalContextPack
```

On a deliberately wide ten-asset Horizon, the four frozen cases selected only 2-3 exact revisions and reduced methodology-only context by roughly 65% to 84% while preserving required revision coverage and explicit omission reasons.

The important architecture is:

```text
SYSTEM
    retains wider Horizon and omission decisions

MODEL-FACING PACK
    contains selected exact methodological revisions only
```

Checkpoint 143 promotes Specification 013 to accepted bounded v1.0.

---

## 2026-08-23: First real-model selective-context value gate passed

Specification 014 / Checkpoint 146 tested the accepted SELECTIVE pack against a compact FULL_HORIZON control under the same task/project evidence and concrete runtime/model treatment.

Observed:

```text
aggregate semantic quality
    SELECTIVE      1.000000
    FULL_HORIZON   1.000000

aggregate provider input tokens
    SELECTIVE mean 1013.00
    FULL mean      3029.50
    ratio          0.334379
    reduction      66.56%

critical regressions  none
retries               0
```

This is the first direct evidence that the post-V0 system/model context separation can preserve measured reasoning quality while materially reducing provider input burden. It also promotes the first production-facing ADS-owned `ReasoningRuntime` request/outcome/usage/trace seam used by live calls under D-032.

The concrete model configuration remains experiment evidence, not a final provider/model decision.

Key sources:

```text
docs/specifications/014_v1_reasoning_context_value_vertical_slice.md
docs/checkpoints/146_first_real_reasoning_context_value_gate_passed.md
experiments/reasoning_context_value/V1_REASONING_CONTEXT_VALUE_RESULT.md
```

---

## 2026-08-23: First recommendation/action-value gate failed and changed the immediate development direction

Specification 015 moved downstream from context economy to:

```text
RELEVANT
    -> RECOMMENDED
    -> REQUIRED / BLOCKING
    -> bounded project action
```

The experiment was preregistered before implementation and live calls. It compared GENERIC, SELECTIVE, and FULL_HORIZON under the same project microstates, task profiles, action menus, and model/runtime treatment.

Live workflow `32642733784` completed all:

```text
36 reasoner outputs
36 condition-blinded judge outputs
72 provider attempts
0 retries
```

The GitHub workflow succeeded as an execution, but the frozen experiment result was:

```text
absolute gates    FAIL
relative gates    PASS
expansion gates   PASS
value signals     0
outcome            FAIL
```

Fourteen of fifteen named gates passed. The single failure was the per-case exact-disposition gate on `RA-02 MODEL_CHOICE`:

```text
GENERIC        0.722222
SELECTIVE      0.666667
FULL_HORIZON   0.666667
required floor 0.800000
```

The repeated discrepancy was `DEFER` expected versus `NOT_NOW` observed for two noncritical expansion actions. SELECTIVE and FULL_HORIZON produced the same pattern, GENERIC behaved almost identically, and the blinded semantic judge scored all nine RA-02 outputs `1.000000`.

The result therefore does not justify promoting the recommendation/action seam and does not support blaming selective context specifically. It changes the immediate development direction from recommendation-state coupling to a separately preregistered disposition-semantics/failure-attribution diagnostic, especially whether `DEFER` and `NOT_NOW` are operationally separable enough for deterministic project navigation.

The failed implementation is not merged into the accepted V1 integration branch. Its frozen design, raw result, and failure interpretation are preserved separately as project evidence.

Key sources:

```text
docs/research/022_first_recommendation_action_value_vertical_slice_design.md
docs/specifications/015_v1_recommendation_action_value_vertical_slice.md
docs/checkpoints/150_specification_015_live_result_failed_exact_disposition_gate.md
experiments/recommendation_action_value/V1_RECOMMENDATION_ACTION_VALUE_RESULT.md
```

---

## 2026-08-23: Dependency-backed DEFER versus NOT_NOW construct passed the live diagnostic

Specification 016 isolated the narrow failure mode from Specification 015 before another recommendation-value comparison. It removed methodological-context treatments, retrieval, Horizon construction, semantic judging, tools, and project mutation, and tested only whether a stronger relation-backed sequencing distinction could be represented and applied reliably.

Frozen distinction:

```text
DEFER
    action already justified in represented plan
    + exact unresolved supplied activating trigger
    + action becomes current next work after trigger
    + exact defer_until_id

NOT_NOW
    no current material justification
    + no represented supplied activating trigger relation
    + null defer_until_id
```

The live workflow `32652636943` executed from the exact frozen head `7db27fd35151c10cdb3562cdf4410fb8f4b09e8b` and observed:

```text
reasoner outputs                     36 / 36
provider attempts                    36 / 45
failed attempts                      0
retries                              0
aggregate exact disposition accuracy 1.000000
all 12 variants                      3 / 3 correct
all 6 contrastive pair sides         3 / 3 correct
DEFER trigger-pointer accuracy       1.000000
NOT_NOW null-pointer correctness     1.000000
```

Frozen outcome:

```text
DISPOSITION_BOUNDARY_SUPPORTED
```

The result narrows the Specification 015 failure attribution. Operational inseparability of the labels is less likely when sequencing is represented by an explicit activating relation, and fixed-reasoner inability is less likely on deliberately unambiguous cases. The historical discrepancy remains consistent with the original RA-02 project state not encoding a uniquely activating DEFER relation strongly enough.

Specification 015 remains an immutable `FAIL` and is not rescored. Both disputed historical expected-DEFER examples are merely diagnosed as not admissible examples of unambiguous Specification 016 DEFER under the stronger construction rule.

The architectural consequence is bounded but important:

```text
DEFER-like sequencing
    should not be a bare low-priority label
    if deterministic distinction from NOT_NOW is required;
    it should carry a concrete represented activating dependency/trigger.
```

This does not promote production DEFER/NOT_NOW enums or automatic project mutation. The next justified step is a separately preregistered recommendation/action-value experiment that preserves the stronger relation-backed sequencing construction and again tests whether SELECTIVE methodological context adds value beyond a strong GENERIC reasoner.

Key sources:

```text
docs/research/023_defer_not_now_disposition_semantics_failure_attribution_design.md
docs/specifications/016_v1_disposition_semantics_failure_attribution_diagnostic.md
docs/checkpoints/155_disposition_semantics_live_gate_supported.md
experiments/disposition_semantics/V1_DISPOSITION_SEMANTICS_RESULT.md
experiments/disposition_semantics/results/spec016-live-20260823-run-32652636943/
```
