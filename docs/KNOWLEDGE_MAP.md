# Knowledge Map

**Status:** Current routing index and evergreen topic library  
**Authority:** Navigation only. This file points to authoritative or explanatory sources and does not replace them.  
**Last reviewed:** 2026-08-29  
**Current checkpoint:** 265  
**Active development branch:** `v1-cockpit-design-exploration`  
**Active PR:** none  
**Promoted V1 integration branch:** `v1-frontend-spike` at `ed5b60bdc882bed0799ce55228ce8187f9c55aa1`  
**Latest specification:** Specification 024  
**Latest scientific experiment outcome:** `INCOMPLETE / EXECUTION INTEGRITY FAILED`

## How to use this map

This file has two durable layers:

```text
CURRENT CONTINUATION ROUTE
    what is active now and what to read next

EVERGREEN TOPIC LIBRARY
    topic -> current authority + deep rationale + evidence/history + specialized index
```

The current route may change frequently. The evergreen library must survive stage changes so a future collaborator can find relevant knowledge without already knowing a checkpoint, research or specification number.

## Current continuation route

Start here:

```text
README.md
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/current_routing.json
docs/checkpoints/265_development_method_v06_knowledge_routing_and_verification_reconciliation.md
docs/research/103_repository_knowledge_discoverability_and_risk_scaled_verification_audit.md
```

Development Method v0.6 is current. It restores evergreen topic routing and introduces V0-V4 risk-scaled verification.

The active **Cockpit product** human-review gate remains:

```text
docs/checkpoints/264_project_general_footprint_and_selection_frame_human_recheck_opened.md
docs/research/102_project_general_box_footprint_and_selection_frame_alignment.md
```

Required visual result:

```text
General project discussion
    same visible footprint as WorkUnit boxes
    selected frame belongs to visible project box only

WorkUnit conversation
    selected frame belongs to visible WorkUnit surface only

Conversation spacing
    remains correct

current-process Focus
    remains working as far as tested
```

Normal browser:

```text
frontend/design-lab/cockpit-reintegration.html
```

Adaptive Conversation Dock remains opt-in and resumes after Checkpoint 264 confirmation:

```text
docs/checkpoints/258_adaptive_conversation_dock_human_review_opened.md
docs/research/097_professional_conversation_copresence_and_adaptive_dock_study.md
```

Current method tooling:

```text
scripts/select_cockpit_verification.py
.github/workflows/cockpit-reintegration-fidelity.yml
scripts/check_knowledge_map.py
.github/workflows/knowledge-map-integrity.yml
```

Last complete pre-v0.6 Cockpit gate:

```text
implementation/test target  9881efe313b8cf04d9521c0464050b30b29944c1
workflow run                33251166351
job                         99096968925
browser tests               78 / 78 passing
```

Checkpoint 265 changes development/routing/verification architecture, not the reviewed Cockpit product implementation.

## Evergreen topic library

### System vision, epistemic integrity, admissibility, human/system boundary
<!-- KM-TOPIC: system-vision -->

Use for what ADS is, why it exists beyond one LLM, epistemic integrity, admissibility/risk and responsibility boundaries.

```text
docs/VISION.md
docs/PRINCIPLES.md
docs/DECISIONS.md
docs/foundations/001_initial_vision_and_reasoning.md
docs/foundations/002_epistemic_integrity_and_project_constitution.md
docs/foundations/003_admissibility_risk_and_assurance.md
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
```

### Project state, initialization, dependency structure and orchestration
<!-- KM-TOPIC: project-state -->

Use for the project object, state-driven orchestration, dependency-aware work, initialization/bootstrap and project-relative methodological state.

```text
docs/foundations/004_project_state_dependency_and_state_driven_orchestration.md
docs/foundations/005_project_initialization_and_universal_bootstrap.md
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
docs/specifications/016_v1_disposition_semantics_failure_attribution_diagnostic.md
docs/specifications/020_v1_recommended_vs_blocking_required_calibration_diagnostic.md
docs/specifications/021_v1_dependency_backed_recommendation_action_value_vertical_slice.md
docs/specifications/022_v1_project_state_methodological_horizon_coverage_diagnostic.md
docs/research/032_project_state_methodological_horizon_coverage_diagnostic.md
```

### Reusable knowledge, activation, representation, quality and evolution
<!-- KM-TOPIC: reusable-knowledge -->

Use for reusable methodology/knowledge units, open-world activation, composability, quality and generalization.

```text
docs/foundations/006_knowledge_activation_and_open_world_reasoning.md
docs/foundations/007_reusable_knowledge_representation_and_composable_components.md
docs/foundations/008_knowledge_quality_generalization_and_evolution.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
docs/specifications/004_v1_reusable_knowledge_interchange.md
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
```

### Evaluation, falsification, supervision and execution integrity
<!-- KM-TOPIC: evaluation-falsification -->

Use for falsification-first evaluation, held-out supervision, observability, prototype V0 and experiment integrity.

```text
docs/foundations/009_behavioral_reasoning_regression_and_system_evaluation.md
docs/foundations/010_minimum_falsification_prototype_and_experimental_contract.md
docs/foundations/011_prototype_v0_technical_specification.md
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
docs/foundations/015_held_out_supervision_and_mechanical_verification_architecture.md
docs/foundations/016_execution_observability_separation.md
docs/experiments/prototype_v0/FINAL_RESULTS.md
prototype_v0/README.md
docs/checkpoints/096_prototype_v0_final_strong_falsification_and_architecture_diagnostic_conclusion.md
```

Specification 022 remains `INCOMPLETE / EXECUTION INTEGRITY FAILED`; do not infer comparative scientific conclusions from it.

### V1 persistence, tooling, interchange and agent runtime
<!-- KM-TOPIC: v1-runtime-persistence -->

Use for SQLite/persistence, Python tooling, interchange, runtime selection and runtime bakeoff evidence.

```text
docs/specifications/001_v1_sqlite_technical_architecture.md
docs/specifications/002_v1_persistence_tooling_standard.md
docs/specifications/003_v1_python_project_and_dependency_tooling.md
docs/specifications/004_v1_reusable_knowledge_interchange.md
docs/specifications/005_v1_agent_runtime_and_interoperability_bakeoff.md
docs/research/010_2026_runtime_bakeoff_preimplementation_refresh.md
docs/research/013_openai_agents_complete_candidate_evidence_and_direct_call_comparison.md
docs/research/014_langgraph_1_2_10_released_durability_comparator_audit.md
docs/research/015_langgraph_complete_candidate_three_way_runtime_comparison_and_stop_rule.md
experiments/runtime_bakeoff/candidates/openai_agents/COMPLETE_RESULT.md
experiments/runtime_bakeoff/candidates/langgraph_runtime/COMPLETE_RESULT.md
```

### Retrieval, MethodologicalHorizon, relevance and selective reasoning context
<!-- KM-TOPIC: retrieval-horizon -->

Use for retrieval benchmarks, exact/hybrid comparators, MethodologicalHorizon construction, relevance and selective context.

```text
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/specifications/009_v1_retrieval_and_methodological_horizon_benchmark.md
docs/specifications/010_v1_exact_semantic_retrieval_comparator.md
docs/specifications/011_v1_rrf_hybrid_retrieval_comparator.md
docs/specifications/012_v1_first_methodological_horizon_builder.md
docs/specifications/013_v1_horizon_relevance_and_selective_context.md
docs/specifications/014_v1_reasoning_context_value_vertical_slice.md
docs/OPEN_QUESTIONS.md
```

### Recommendation, disposition, calibration, provenance and action value
<!-- KM-TOPIC: recommendation-calibration -->

Use for recommendation value, failure attribution, relation-backed recommendations, system-owned provenance and blocking/calibration semantics.

```text
docs/specifications/015_v1_recommendation_action_value_vertical_slice.md
docs/specifications/016_v1_disposition_semantics_failure_attribution_diagnostic.md
docs/specifications/017_v1_relation_backed_recommendation_action_value_vertical_slice.md
docs/specifications/018_v1_governed_autonomous_live_experiment_launcher.md
docs/specifications/019_v1_system_owned_provenance_recommendation_action_value_vertical_slice.md
docs/specifications/020_v1_recommended_vs_blocking_required_calibration_diagnostic.md
docs/specifications/021_v1_dependency_backed_recommendation_action_value_vertical_slice.md
docs/OPEN_QUESTIONS.md
```

### Methodological Knowledge Universe construction and coverage
<!-- KM-TOPIC: methodological-knowledge-universe -->

Use for the methodological knowledge universe, coverage architecture, source-to-knowledge construction and current coverage state.

```text
docs/research/028_system_identity_methodological_navigation_and_knowledge_universe_construction.md
docs/research/031_methodological_knowledge_universe_coverage_architecture.md
docs/research/033_methodological_knowledge_universe_construction_framework.md
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
docs/methodological_knowledge/COVERAGE_MAP.md
docs/checkpoints/193_methodological_knowledge_universe_construction_framework_frozen.md
```

### Source Universe, evidence substrate and permanent vault
<!-- KM-TOPIC: source-universe -->

Use for durable source storage, source artifact integrity, evidence provenance, source-substrate validation and paused permanent-vault deployment.

```text
docs/foundations/022_source_universe_artifact_integrity_and_evidence_provenance_architecture.md
docs/research/034_durable_source_universe_and_evidence_substrate_architecture.md
docs/specifications/023_v1_source_universe_substrate.md
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
docs/source_universe/validation/001_vu_machine_learning_source_substrate_result.md
docs/checkpoints/196_source_substrate_accepted_first_corpus_validated.md
```

Current status: substrate accepted; permanent deployment PAUSED, not rejected. Course 2 gate unchanged.

### Development method, preservation, continuity and model collaboration
<!-- KM-TOPIC: development-continuity -->

Use for how ADS itself is built, preserved, reconstructed, reviewed and coordinated across models/sessions.

```text
docs/DEVELOPMENT_METHOD.md
docs/CONTINUITY.md
docs/checkpoints/README.md
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
docs/research/035_multi_model_development_collaboration_architecture.md
docs/research/036_deferred_asynchronous_review_and_catchup_architecture.md
docs/research/064_rapid_iteration_repository_preservation_audit_and_checkpoint_hygiene.md
docs/research/103_repository_knowledge_discoverability_and_risk_scaled_verification_audit.md
docs/model_collaboration/README.md
docs/model_collaboration/INTERACTION_PROVENANCE_AND_NAMING.md
docs/model_collaboration/DEFERRED_REVIEW_AND_CATCHUP.md
docs/model_collaboration/REVIEW_INBOX.md
docs/specifications/024_v1_model_collaboration_state_guard.md
```

Structural validators:

```text
scripts/check_checkpoint_metadata.py
scripts/check_current_routing.py
scripts/check_knowledge_map.py
scripts/check_model_collaboration_state.py
```

### Project Cockpit architecture and product model
<!-- KM-TOPIC: cockpit-architecture -->

Use for the interactive workspace vision, project object integration, professional UI foundation and promoted Cockpit interaction architecture.

```text
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
docs/specifications/006_v1_frontend_architecture_and_visual_spike.md
docs/specifications/007_v1_unified_project_cockpit_interaction_spike.md
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
frontend/design-lab/cockpit-reintegration.html
```

### Cockpit visual grammar, appearance and connector semantics
<!-- KM-TOPIC: cockpit-visual-grammar -->

Use for category grammar, WorkUnit appearance, connector class/directionality, disposition/runtime/attention presentation and configurable non-semantic appearance.

```text
docs/foundations/023_user_configurable_cockpit_appearance_and_semantic_invariants.md
docs/foundations/024_composable_connector_presentation_and_semantic_directionality.md
docs/cockpit/PHASE_C_DECISION_LEDGER.md
docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
```

The Phase-C ledger is the disposition index for Research 037-088. Exact accepted implementation provenance is in the manifest.

### Cockpit selection, expansion, focus, Deep Dive and zoom states
<!-- KM-TOPIC: cockpit-interaction-states -->

Use for SEL2 selection, X5 expansion, current-process Focus, specialist/Deep Dive entry, zoom/recovery and held/provisional state distinctions.

```text
docs/cockpit/PHASE_C_DECISION_LEDGER.md
docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
docs/research/098_intermittent_cockpit_presentation_state_integrity_recovery.md
```

Important current distinctions: L0 Flat Fields remains provisional; semantic zoom remains deferred with S0 geometric control as the working default.

### Conversation Workspace, scope, navigation and Cockpit coexistence
<!-- KM-TOPIC: conversation-workspace -->

Use for Quiet Graphite, project-general versus WorkUnit conversation scope, Boxes/Text, A6, access from Grid/Deep Dive, state preservation and Adaptive Conversation Dock work.

```text
docs/research/079_conversation_workspace_presentation_architecture_experiment.md
docs/research/081_independent_conversation_workspace_dual_design_comparison.md
docs/research/082_conversation_scope_work_unit_anchor_and_quiet_graphite_baseline.md
docs/research/083_a6_adaptive_anchor_and_canonical_box_sidebar_mode.md
docs/research/085_conversation_workspace_a6_refinement_and_entry_transition.md
docs/research/086_conversation_workspace_orthogonal_access_and_coexistence_architecture.md
docs/research/097_professional_conversation_copresence_and_adaptive_dock_study.md
docs/checkpoints/258_adaptive_conversation_dock_human_review_opened.md
```

Recent presentation-integrity sequence:

```text
docs/research/098_intermittent_cockpit_presentation_state_integrity_recovery.md
docs/research/099_conversation_boxes_visible_separation_human_retest_and_row_owned_geometry_recovery.md
docs/research/100_conversation_boxes_css_grid_track_absorption_and_live_geometry_recovery.md
docs/research/101_project_general_thread_short_viewport_containment_recovery.md
docs/research/102_project_general_box_footprint_and_selection_frame_alignment.md
```

### Cockpit implementation provenance and source-faithful reintegration
<!-- KM-TOPIC: cockpit-provenance-fidelity -->

Use for why the first holistic integration failed, exact source recovery, implementation manifest, reintegration and fidelity gates.

```text
docs/research/087_holistic_integrated_cockpit_baseline_and_accepted_invariants_audit.md
docs/research/088_integrated_cockpit_fidelity_failure_and_source_of_truth_recovery_audit.md
docs/research/089_cockpit_implementation_provenance_recovery_completion_and_exact_history_gate.md
docs/research/090_current_branch_exact_source_compatibility_and_reintegration_strategy.md
docs/research/091_source_faithful_reintegration_interaction_integrity_gate.md
docs/checkpoints/251_cockpit_implementation_provenance_recovered_and_reintegration_opened.md
docs/cockpit/README.md
docs/cockpit/PHASE_C_DECISION_LEDGER.md
docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
docs/cockpit/accepted_implementation_manifest.json
scripts/check_cockpit_implementation_manifest.py
.github/workflows/cockpit-implementation-provenance.yml
.github/workflows/cockpit-reintegration-fidelity.yml
scripts/select_cockpit_verification.py
```

The failed integrated browser at `8e554d847bb3b6318db432abcb5dff742f0fa523` is diagnostic evidence only, not an accepted baseline.

### Cockpit shell, spatial rail, topology compass and current shell studies
<!-- KM-TOPIC: cockpit-shell-rail -->

Use for the right-edge rail, depth/direct-manipulation studies, rejected angled rail, flat current rail, live topology compass and current shell controls.

```text
docs/research/092_spatial_edge_rail_depth_direct_manipulation_and_docking_study.md
docs/research/093_architectural_cockpit_edge_instrument_surface_depth_study.md
docs/research/094_resting_angled_rail_spatial_identity_and_clarity_only_expansion.md
docs/research/095_conversation_spacing_flat_project_rail_and_live_topology_compass.md
docs/research/096_structural_conversation_spacing_and_current_project_tool_rail_control_set.md
docs/checkpoints/255_flat_project_tool_rail_and_live_topology_compass_human_review_opened.md
docs/checkpoints/256_structural_conversation_spacing_and_project_tool_rail_controls_review_opened.md
docs/checkpoints/257_canonical_cockpit_review_route_normalized.md
```

The resting angled rail is historical/rejected for the current direction. The flat rail and live topology compass remain the current reviewed substrate.

### Canonical history, major changes, decisions and unresolved questions
<!-- KM-TOPIC: canonical-history -->

Use when reconstructing why the current project looks the way it does, what is explicitly accepted, what changed structurally and what remains open.

```text
docs/DECISIONS.md
docs/OPEN_QUESTIONS.md
docs/PRINCIPLES.md
docs/VISION.md
docs/MAJOR_CHANGES.md
docs/checkpoints/README.md
```

Specialized historical indexes should be used instead of scanning every checkpoint blindly:

```text
docs/methodological_knowledge/COVERAGE_MAP.md
docs/cockpit/PHASE_C_DECISION_LEDGER.md
docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
docs/model_collaboration/REVIEW_INBOX.md
```

## Map maintenance rule

At a meaningful promotion/reconciliation boundary:

```text
1. update the current continuation route if the active state changed;
2. ask whether any evergreen topic gained/lost a governing source;
3. link new specialized indexes rather than duplicating them;
4. preserve maturity/status distinctions;
5. run scripts/check_knowledge_map.py;
6. do not update the map merely because another commit/checkpoint exists.
```

If a new major domain emerges, add a new topic marker rather than squeezing it into an unrelated category. The validator may be expanded only when a real structural need is observed.
