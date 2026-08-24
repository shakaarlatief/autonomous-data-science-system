# Major Changes

**Status:** Current selective structural history  
**Authority:** Navigation and project-history aid. Detailed decisions, foundations, specifications, checkpoints, final experiment reports, and Git history remain authoritative for their own scope.  
**Last reviewed:** 2026-08-24

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

The LLM became explicitly one flexible reasoning component inside ADS. System-managed memory, provenance, deterministic guarantees, execution coordination, and human control remain separate concerns, and every explicit mechanism must justify its complexity empirically.

Key source:

```text
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
```

---

## 2026-08-18: Development preservation gained routing, promotion audits, and reconciliation

Development Method v0.3 introduced checkpoint promotion audits, `KNOWLEDGE_MAP`, periodic reconciliation, authority/maturity conventions, `MAJOR_CHANGES`, and explicit separation of current state from detailed experiment ledgers.

Git + Markdown remained the development-preservation substrate until observed scale or consistency problems justified stronger tooling.

Key sources:

```text
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
docs/DEVELOPMENT_METHOD.md
docs/KNOWLEDGE_MAP.md
```

---

## 2026-08-18 to 2026-08-19: Validated supervision and observability separation were established

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
```

---

## 2026-08-19: Prototype V0 strongly falsified the original P0 design

Final classification:

> **STRONG FALSIFICATION OF THE CURRENT P0 DESIGN.**

The broader ADS vision survived, but the original orchestration machinery did not earn its cost. The strongest scaling lesson became:

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

## 2026-08-19: Post-V0 target became a professional interactive data-science operating environment

The target became a professional environment in which ADS carries much of the methodological-navigation and project-memory burden while the human can inspect, discuss, select, override, guide, and approve work interactively.

Key sources:

```text
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
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

## 2026-08-20 to 2026-08-21: V1 local-first persistence, tooling, and governed interchange became operational

The project accepted:

```text
D-028  SQLite-centered local-first operational architecture
D-029  SQLAlchemy Core 2.0 + Alembic 1.x
D-030  pyproject.toml + uv + committed uv.lock + uv_build
D-031  deterministic JSON + JSON Schema 2020-12 interchange with governance
```

The governed knowledge round-trip closed across SQLite/Linux, SQLite/Windows, and PostgreSQL 18. Exact historical project-to-knowledge revision pinning was preserved.

Key sources:

```text
docs/specifications/001_v1_sqlite_technical_architecture.md
docs/specifications/004_v1_reusable_knowledge_interchange.md
docs/checkpoints/127_governed_knowledge_roundtrip_closed_across_sqlite_and_postgresql.md
```

---

## 2026-08-20 to 2026-08-21: Project Cockpit became the promoted primary active-work interaction model

Successive bounded frontend spikes and human review cycles evolved the Cockpit into a scalable spatial operating surface with 2D navigation, bounded zoom, native pinch, scalable Jump/search, floating composer/controls, compact fold-away chrome, fullscreen, and collision-safe surfaces.

Specification 008 promoted the core interaction architecture. Final canvas/gesture libraries, semantic zoom/grouping, visual identity, and final frontend/chart choices remain open.

Key sources:

```text
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
docs/checkpoints/126_seventh_cockpit_review_validated_and_interaction_architecture_promoted.md
docs/checkpoints/130_post_promotion_cockpit_normal_window_and_pinch_polish_gate_passed.md
```

---

## 2026-08-20: Unexpected Session 02 boundary validated preservation but exposed routing drift

Session 02 reached the platform conversation-length limit after substantive Cockpit work had been preserved but before final routing reconciliation. Session 03 reconstructed from repository authority and repaired stale current routing.

The incident demonstrated that substantive preservation and current routing are separate requirements.

Key source:

```text
docs/checkpoints/120_unplanned_session_boundary_reconciliation_and_v1_continuity_restored.md
```

---

## 2026-08-22: Initial V1 reasoning runtime selected after executable bakeoff

Specification 005 compared ADS-owned direct model calls, OpenAI Agents SDK, and LangGraph as ADS-shaped runtime paths.

D-032 accepts:

```text
OpenAI Agents SDK
    behind an ADS-owned ReasoningRuntime port
```

Direct model calls remain a fallback/reference path. No final LLM provider/model or multi-agent architecture is selected.

Key sources:

```text
docs/DECISIONS.md, D-032
docs/specifications/005_v1_agent_runtime_and_interoperability_bakeoff.md
docs/checkpoints/133_v1_reasoning_runtime_selected_and_bakeoff_closed.md
```

---

## 2026-08-22: Retrieval progressed from lexical baseline to explained MethodologicalHorizon

The bounded retrieval/Horizon program established:

```text
Checkpoint 135   lexical retrieval baseline
Checkpoint 137   dense complementary signal
Checkpoint 139   hybrid comparator
Checkpoint 141   explained Horizon with TRUE/FALSE/UNKNOWN applicability
```

The key executable semantic invariant became:

```text
unknown != false
```

The hybrid result remains complementarity evidence, not permanent selection of an embedding model, RRF, vector persistence, ANN, or reranking infrastructure.

---

## 2026-08-22 to 2026-08-23: Selective MethodologicalContextPack validated the system/model context boundary

Specification 013 promoted a bounded selector from a wider Horizon to exact selected revisions. Specification 014 then tested the real-model consequence:

```text
SELECTIVE quality       1.000000
FULL_HORIZON quality    1.000000
SELECTIVE/FULL input    0.334379
input-token reduction   66.56%
critical regressions    none
```

This was the first direct evidence that the post-V0 system/model context separation can preserve measured reasoning quality while materially reducing provider input burden.

Key sources:

```text
docs/specifications/013_v1_horizon_relevance_and_selective_context.md
docs/specifications/014_v1_reasoning_context_value_vertical_slice.md
docs/checkpoints/146_first_real_reasoning_context_value_gate_passed.md
```

---

## 2026-08-23: First recommendation/action-value gate failed

Specification 015 moved downstream from context economy to recommendation/action quality. The full frozen design executed, but the exact-disposition gate failed around `DEFER` versus `NOT_NOW` and the experiment classified `FAIL`.

The result did not justify promoting the recommendation/action seam and did not implicate selective context specifically. The failed implementation was not merged; its frozen design and negative evidence were preserved.

Key sources:

```text
docs/specifications/015_v1_recommendation_action_value_vertical_slice.md
docs/checkpoints/150_specification_015_live_result_failed_exact_disposition_gate.md
experiments/recommendation_action_value/V1_RECOMMENDATION_ACTION_VALUE_RESULT.md
```

---

## 2026-08-23: Dependency-backed DEFER versus NOT_NOW construct passed

Specification 016 prospectively isolated the failed sequencing construct. The live diagnostic observed 36/36 exact dispositions and exact dependency pointers, producing:

```text
DISPOSITION_BOUNDARY_SUPPORTED
```

The architectural consequence was bounded but important:

```text
DEFER-like sequencing
    should carry a concrete represented activating dependency/trigger
    when deterministic distinction from NOT_NOW is required
```

Specification 015 remains immutable `FAIL` evidence.

Key sources:

```text
docs/specifications/016_v1_disposition_semantics_failure_attribution_diagnostic.md
docs/checkpoints/155_disposition_semantics_live_gate_supported.md
```

---

## 2026-08-23: Relation-backed recommendation rerun exposed a provenance-instrumentation defect

Specification 017 returned to the recommendation/action comparison but ended incomplete. The key durable lesson was:

```text
reasoning function / task profile
    !=
reusable knowledge stable-key provenance
```

The system already knew exact supplied revisions and context digests, so requiring duplicate model-authored provenance was an instrumentation mistake. Specification 017 remains permanently incomplete historical evidence.

Key sources:

```text
docs/specifications/017_v1_relation_backed_recommendation_action_value_vertical_slice.md
docs/checkpoints/159_specification_017_live_execution_incomplete_provenance_contract.md
```

---

## 2026-08-23: Governed autonomous live-experiment launcher supported and promoted

Specification 018 established a bounded repository-governed control plane for explicitly authorized frozen experiments:

```text
owner request
    -> repository authorization registry
    -> exact owner/source/CI/duplicate checks
    -> allowlisted workflow_dispatch
    -> independently validating target workflow
```

The launcher receives no provider credential and issue text cannot define arbitrary executable configuration.

Checkpoint 161 classified the bounded outcome as:

```text
GOVERNED_LAUNCHER_SUPPORTED
```

Specification 018 was promoted to `v1-frontend-spike`.

---

## 2026-08-24: System-owned provenance repair completed the matched recommendation experiment, but recommendation value still failed

Specification 019 moved exact supplied-context provenance from model-authored output to deterministic system ownership while leaving recommendation content model-owned.

The complete frozen matched design executed without provenance-induced schema failures or retries, validating the instrumentation repair. The recommendation-value advancement result still classified `FAIL`.

The central recommendation-calibration problem was repeated over-blocking on RB-02. The failed implementation was not promoted; frozen contract, raw result, interpretation, and checkpoints were preserved.

Key sources:

```text
docs/specifications/019_v1_system_owned_provenance_recommendation_action_value_vertical_slice.md
docs/checkpoints/166_specification_019_live_result_failed.md
experiments/system_owned_provenance_recommendation_action_value/V1_SYSTEM_OWNED_PROVENANCE_RECOMMENDATION_ACTION_VALUE_RESULT.md
```

---

## 2026-08-24: Dependency-backed RECOMMENDED versus BLOCKING_REQUIRED boundary supported

Specification 020 prospectively isolated the recommendation-calibration construct exposed by Specification 019. It removed methodological-context treatments and tested one fixed reasoner on six deliberately unambiguous contrastive pairs where genuine blocking was represented by an exact unresolved requirement, an exact active defended downstream scope, an explicit `DEPENDS_ON` relation, and the candidate action that resolves the requirement.

The governed live run completed the frozen 36-observation design with no retries:

```text
reasoner outputs                     36 / 36
provider attempts                    36 / 45
aggregate exact disposition accuracy 1.000000
all 12 variants                      3 / 3 correct
all 6 contrastive pair sides         3 / 3 correct
joint blocking-pointer accuracy      1.000000
RECOMMENDED null-pointer correctness 1.000000
outcome                              BLOCKING_BOUNDARY_SUPPORTED
```

The bounded architectural lesson is:

```text
blocking should not be represented by urgency or priority alone

genuinely BLOCKING_REQUIRED work
    -> exact unresolved requirement
    -> exact active defended downstream scope
    -> explicit scope DEPENDS_ON requirement relation
    -> action resolves requirement
```

This makes taxonomy inseparability and fixed-reasoner inability less likely explanations for Specification 019's RB-02 behavior, but it does not rescore Specification 019 and does not establish selective methodological-context recommendation value or production recommendation enums.

The same stage-boundary review also confirmed recurring lag in mutable routing documents relative to already durable result/checkpoint evidence. That observed consistency problem is now sufficient to justify a small machine-checkable routing manifest and CI validator while retaining Git + Markdown as the substantive preservation architecture.

Key sources:

```text
docs/specifications/020_v1_recommended_vs_blocking_required_calibration_diagnostic.md
docs/checkpoints/171_recommended_vs_blocking_required_calibration_boundary_supported.md
experiments/blocking_calibration/V1_BLOCKING_CALIBRATION_RESULT.md
```
