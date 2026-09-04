# Knowledge Map

**Status:** Current evergreen subject library
**Authority:** Navigation only. This file routes subjects to repository evidence and does not replace the authority of the routed artifacts.
**Last reviewed:** 2026-09-04

## Purpose

`docs/KNOWLEDGE_MAP.md` is the repository's semantic library: **subject -> relevant knowledge artifacts**.

It is intentionally not the current-state document and not the structural repository guide:

```text
Need to know what is happening right now?     docs/CURRENT_STATE.md
Need the machine-readable live pointer?        docs/current_routing.json
Need to know what each file/folder type means? docs/README.md
Need knowledge about a subject?                docs/KNOWLEDGE_MAP.md
Need the reconstruction procedure?             docs/CONTINUITY.md
```

A source may appear under multiple subjects when it genuinely informs multiple questions. Topic membership is retrieval metadata, not an authority claim.

## Coverage contract

The library is deliberately exhaustive for the three numbered durable knowledge families:

```text
docs/foundations/      every numbered foundation must be routed
docs/specifications/   every numbered specification must be routed
docs/research/         every numbered research record must be routed
```

Historical checkpoints are much more numerous and are not duplicated as hundreds of visible links. Every numbered checkpoint is covered by validated semantic range assignments later in this file, while especially important checkpoints may be linked directly inside relevant subjects.

A governed historical intermediate checkpoint milestone has no active checkpoint number and therefore cannot truthfully participate in a numeric range. Every `docs/checkpoints/intermediate_*.md` milestone must instead be routed directly under at least one semantically appropriate subject. Specialized domain indexes remain authoritative where they exist.

Mechanical coverage and path integrity are checked by `scripts/check_knowledge_map.py`.

## Subject index

1. System identity, vision, epistemic integrity and human/system boundary
2. Project state, initialization, dependency structure and orchestration
3. Reusable methodological knowledge, activation, representation and evolution
4. Evaluation, falsification, supervision, observability and execution integrity
5. V1 persistence, tooling, interchange and reasoning runtime
6. Retrieval, MethodologicalHorizon, relevance and selective reasoning context
7. Recommendation value, disposition, provenance, dependencies and calibration
8. Methodological Knowledge Universe construction and coverage
9. Source Universe, evidence substrate and permanent vault
10. Development method, preservation, continuity and multi-model governance
11. Project Cockpit product architecture and professional interaction model
12. Cockpit world, canvas, grid, ambient dynamics and spatial navigation
13. WorkUnit visual grammar, appearance, disposition and runtime carriers
14. Connector, port, relation-class and directionality visual grammar
15. Selection, expansion, focus, Deep Dive and semantic zoom states
16. Conversation Workspace, scope, navigation and Cockpit coexistence
17. Cockpit implementation provenance, source-faithful reintegration and fidelity
18. Cockpit shell, project rail, topology compass and docking studies
19. Canonical decisions, principles, major changes and unresolved questions

## Subject library

### System identity, vision, epistemic integrity and human/system boundary
<!-- KM-TOPIC: system-identity -->

Use for what ADS is, why it exists beyond one LLM, epistemic integrity, admissibility/risk and responsibility boundaries.

```text
docs/VISION.md
docs/PRINCIPLES.md
docs/DECISIONS.md
docs/OPEN_QUESTIONS.md
docs/foundations/001_initial_vision_and_reasoning.md
docs/foundations/002_epistemic_integrity_and_project_constitution.md
docs/foundations/003_admissibility_risk_and_assurance.md
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
docs/research/001_2026_agentic_ecosystem_and_integration_architecture_audit.md
docs/research/028_system_identity_methodological_navigation_and_knowledge_universe_construction.md
```

### Project state, initialization, dependency structure and orchestration
<!-- KM-TOPIC: project-state -->

Use for the project object, initialization, state-driven orchestration, dependency-aware work and project-relative methodological state.

```text
docs/PRINCIPLES.md
docs/DECISIONS.md
docs/OPEN_QUESTIONS.md
docs/foundations/004_project_state_dependency_and_state_driven_orchestration.md
docs/foundations/005_project_initialization_and_universal_bootstrap.md
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
docs/specifications/016_v1_disposition_semantics_failure_attribution_diagnostic.md
docs/specifications/020_v1_recommended_vs_blocking_required_calibration_diagnostic.md
docs/specifications/021_v1_dependency_backed_recommendation_action_value_vertical_slice.md
docs/specifications/022_v1_project_state_methodological_horizon_coverage_diagnostic.md
docs/research/019_first_methodological_horizon_application_seam.md
docs/research/028_system_identity_methodological_navigation_and_knowledge_universe_construction.md
docs/research/029_dependency_backed_recommendation_value_design.md
docs/research/030_methodological_navigation_vs_downstream_recommendation_calibration.md
docs/research/032_project_state_to_methodological_horizon_coverage_diagnostic_design.md
```

### Reusable methodological knowledge, activation, representation and evolution
<!-- KM-TOPIC: knowledge-representation -->

Use for reusable knowledge units, open-world activation, representation, quality, composability, generalization and evolution.

```text
docs/PRINCIPLES.md
docs/DECISIONS.md
docs/foundations/006_knowledge_activation_and_open_world_reasoning.md
docs/foundations/007_reusable_knowledge_representation_and_composable_components.md
docs/foundations/008_knowledge_quality_generalization_and_evolution.md
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
docs/specifications/004_v1_reusable_knowledge_interchange.md
docs/research/028_system_identity_methodological_navigation_and_knowledge_universe_construction.md
docs/research/031_methodological_navigation_coverage_architecture_and_evaluation_review.md
docs/research/033_methodological_knowledge_universe_construction_framework.md
docs/methodological_knowledge/COVERAGE_MAP.md
```

### Evaluation, falsification, supervision, observability and execution integrity
<!-- KM-TOPIC: evaluation-falsification -->

Use for falsification-first evaluation, held-out supervision, observability, prototype V0 and experiment-integrity boundaries.

```text
docs/PRINCIPLES.md
docs/DECISIONS.md
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

Specification 022 remains `INCOMPLETE / EXECUTION INTEGRITY FAILED`; no comparative scientific conclusion may be inferred from that run.

### V1 persistence, tooling, interchange and reasoning runtime
<!-- KM-TOPIC: runtime-persistence -->

Use for persistence architecture, Python/dependency tooling, interchange and the reasoning-runtime bakeoff.

```text
docs/DECISIONS.md
docs/specifications/001_v1_sqlite_technical_architecture.md
docs/specifications/002_v1_persistence_tooling_standard.md
docs/specifications/003_v1_python_project_and_dependency_tooling.md
docs/specifications/004_v1_reusable_knowledge_interchange.md
docs/specifications/005_v1_agent_runtime_and_interoperability_bakeoff.md
docs/research/001_2026_agentic_ecosystem_and_integration_architecture_audit.md
docs/research/010_2026_runtime_bakeoff_preimplementation_refresh.md
docs/research/011_openai_agents_0_19_4_released_api_compatibility_findings.md
docs/research/012_post_promotion_cockpit_normal_window_and_pinch_sensitivity_review.md
docs/research/013_openai_agents_complete_candidate_evidence_and_direct_call_comparison.md
docs/research/014_langgraph_1_2_10_released_durability_comparator_audit.md
docs/research/015_langgraph_complete_candidate_three_way_runtime_comparison_and_stop_rule.md
```

### Retrieval, MethodologicalHorizon, relevance and selective reasoning context
<!-- KM-TOPIC: retrieval-horizon -->

Use for retrieval benchmarks, exact/dense/hybrid comparators, MethodologicalHorizon construction, relevance gating and reasoning-context value.

```text
docs/DECISIONS.md
docs/OPEN_QUESTIONS.md
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
docs/specifications/009_v1_retrieval_and_methodological_horizon_benchmark.md
docs/specifications/010_v1_exact_semantic_retrieval_comparator.md
docs/specifications/011_v1_rrf_hybrid_retrieval_comparator.md
docs/specifications/012_v1_first_methodological_horizon_builder.md
docs/specifications/013_v1_horizon_relevance_and_selective_context.md
docs/specifications/014_v1_reasoning_context_value_vertical_slice.md
docs/research/016_production_retrieval_and_methodological_horizon_benchmark_design.md
docs/research/017_exact_semantic_retrieval_comparator_selection.md
docs/research/018_dense_semantic_failure_complementarity_and_rrf_fusion_rationale.md
docs/research/019_first_methodological_horizon_application_seam.md
docs/research/020_first_horizon_relevance_and_selective_context_gate_design.md
docs/research/021_first_reasoning_context_value_vertical_slice_design.md
docs/research/031_methodological_navigation_coverage_architecture_and_evaluation_review.md
docs/research/032_project_state_to_methodological_horizon_coverage_diagnostic_design.md
docs/methodological_knowledge/COVERAGE_MAP.md
```

### Recommendation value, disposition, provenance, dependencies and calibration
<!-- KM-TOPIC: recommendation-action -->

Use for recommendation/action value, failure attribution, relation/dependency-backed recommendations, system-owned provenance and blocking/calibration semantics.

```text
docs/DECISIONS.md
docs/OPEN_QUESTIONS.md
docs/foundations/004_project_state_dependency_and_state_driven_orchestration.md
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
docs/specifications/015_v1_recommendation_action_value_vertical_slice.md
docs/specifications/016_v1_disposition_semantics_failure_attribution_diagnostic.md
docs/specifications/017_v1_relation_backed_recommendation_action_value_vertical_slice.md
docs/specifications/018_v1_governed_autonomous_live_experiment_launcher.md
docs/specifications/019_v1_system_owned_provenance_recommendation_action_value_vertical_slice.md
docs/specifications/020_v1_recommended_vs_blocking_required_calibration_diagnostic.md
docs/specifications/021_v1_dependency_backed_recommendation_action_value_vertical_slice.md
docs/research/022_first_recommendation_action_value_vertical_slice_design.md
docs/research/023_defer_not_now_disposition_semantics_failure_attribution_design.md
docs/research/024_relation_backed_recommendation_action_value_design.md
docs/research/025_governed_autonomous_live_experiment_launcher_design.md
docs/research/026_system_owned_provenance_recommendation_action_value_design.md
docs/research/027_recommended_vs_blocking_required_calibration_design.md
docs/research/028_system_identity_methodological_navigation_and_knowledge_universe_construction.md
docs/research/029_dependency_backed_recommendation_value_design.md
docs/research/030_methodological_navigation_vs_downstream_recommendation_calibration.md
```

### Methodological Knowledge Universe construction and coverage
<!-- KM-TOPIC: methodological-knowledge-universe -->

Use for the broad methodological universe, coverage architecture, source-to-knowledge construction and current coverage state.

```text
docs/DECISIONS.md
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
docs/specifications/022_v1_project_state_methodological_horizon_coverage_diagnostic.md
docs/specifications/023_v1_source_universe_substrate.md
docs/research/028_system_identity_methodological_navigation_and_knowledge_universe_construction.md
docs/research/031_methodological_navigation_coverage_architecture_and_evaluation_review.md
docs/research/032_project_state_to_methodological_horizon_coverage_diagnostic_design.md
docs/research/033_methodological_knowledge_universe_construction_framework.md
docs/research/034_durable_source_universe_and_evidence_substrate_architecture.md
docs/methodological_knowledge/COVERAGE_MAP.md
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
docs/checkpoints/193_methodological_knowledge_universe_construction_framework_frozen.md
docs/checkpoints/267_cockpit_frontend_paused_source_vault_bootstrap_resumed.md
```

### Source Universe, evidence substrate and permanent vault
<!-- KM-TOPIC: source-universe -->

Use for durable source storage, artifact integrity, evidence provenance, source-substrate validation, permanent-vault deployment/resumption and the bounded local-execution prerequisite opened before ingestion.

```text
docs/DECISIONS.md
docs/foundations/022_source_universe_artifact_integrity_and_evidence_provenance_architecture.md
docs/specifications/023_v1_source_universe_substrate.md
docs/research/034_durable_source_universe_and_evidence_substrate_architecture.md
docs/research/105_codexless_local_execution_bridge_evaluation.md
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
docs/source_universe/validation/001_vu_machine_learning_source_substrate_result.md
docs/local_execution/DIRECT_GIT_INVESTIGATION_LESSONS.md
docs/checkpoints/196_source_substrate_accepted_first_corpus_validated.md
docs/checkpoints/198_source_substrate_promoted_permanent_vault_bootstrap_opened.md
docs/checkpoints/267_cockpit_frontend_paused_source_vault_bootstrap_resumed.md
docs/checkpoints/268_first_corpus_matched_codexless_local_execution_evaluation_opened.md
docs/checkpoints/270_codexless_controlled_write_verified_local_execution_accepted.md
docs/checkpoints/271_bounded_direct_git_synchronization_verified_source_vault_resume_ready.md
docs/checkpoints/274_archive_unarchive_reacquire_verified_source_vault_ingestion_resumed.md
docs/checkpoints/275_guided_proceed_in_chat_roundtrip_verified_source_vault_active.md
docs/checkpoints/276_codex_codexless_upstream_ecosystem_research_opened_source_vault_paused.md
```

Current substrate status is routed from `CURRENT_STATE.md`; this subject section preserves the durable architecture and evidence chain rather than copying live status.

### Development method, preservation, continuity and multi-model governance
<!-- KM-TOPIC: development-governance -->

Use for how ADS itself is built, preserved, reconstructed, verified and coordinated across chats, branches and models.

```text
docs/README.md
docs/DEVELOPMENT_METHOD.md
docs/CONTINUITY.md
docs/MAJOR_CHANGES.md
docs/checkpoints/README.md
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
docs/specifications/024_v1_model_collaboration_state_guard.md
docs/specifications/025_v1_governed_repository_integrity_and_continuity_hardening.md
docs/specifications/026_v1_repository_integrity_recovery_amendment.md
docs/specifications/027_v1_historical_intermediate_checkpoint_integrity_extension.md
docs/research/035_multi_model_development_collaboration_architecture.md
docs/research/036_deferred_asynchronous_review_and_catchup_architecture.md
docs/research/064_rapid_iteration_repository_preservation_audit_and_checkpoint_hygiene.md
docs/research/080_explicit_coordination_branch_claude_trigger_hardening.md
docs/research/103_repository_knowledge_discoverability_and_risk_scaled_verification_audit.md
docs/research/104_repository_information_architecture_and_exhaustive_knowledge_routing_refinement.md
docs/research/105_codexless_local_execution_bridge_evaluation.md
docs/research/106_governed_repository_integrity_and_continuity_bootstrap_hardening.md
docs/research/107_post_outage_repository_integrity_recovery_audit.md
docs/research/108_historical_intermediate_checkpoint_integrity_and_discoverability_audit.md
docs/research/109_codex_desktop_thread_handoff_and_catalog_reconciliation.md
docs/research/110_durable_bidirectional_codex_thread_handoff_and_cooperative_release.md
docs/research/111_archive_unarchive_reacquire_closes_codex_desktop_handoff.md
docs/research/112_guided_proceed_in_chat_shared_ready_and_repeatable_roundtrip.md
docs/research/113_codex_codexless_upstream_ecosystem_architecture_research_program.md
docs/research/114_current_codex_app_server_architecture_and_ads_implications.md
docs/research/115_public_codexless_current_architecture_pr_landscape_and_ads_delta.md
docs/research/116_flexible_multi_repository_codexless_authority_and_runtime_repository_architecture.md
docs/research/117_reuse_first_multimodal_document_architecture_and_local_media_handoff.md
docs/research/CODEX_UPSTREAM_ADS_COMPARISON_MATRIX.md
docs/local_execution/LOCAL_RUNTIME_REPOSITORY.md
docs/local_execution/validation/033_semantic_git_commit_push_surface_publication_and_public_ads_push_verified.md
docs/local_execution/validation/034_chatgpt_tool_projection_refresh_and_connector_coexistence_observations.md
docs/local_execution/validation/035_running_codex_supervision_liveness_gap_reproduced.md
docs/local_execution/validation/036_live_config_batchwrite_qualification_host_boundary.md
docs/local_execution/validation/037_flexible_authority_live_source_published_restart_pending.md
docs/local_execution/validation/038_runtime_repository_bootstrap_private_git_credentials_boundary.md
docs/local_execution/validation/039_workspace_standard_and_document_read_live_qualified.md
docs/local_execution/validation/040_codex_pdf_skill_visual_read_reuse_experiment.md
docs/local_execution/validation/041_codex_native_local_image_view_qualified.md
docs/local_execution/validation/042_model_free_mcp_image_bridge_publication_preflight_qualified.md
docs/local_execution/validation/043_model_free_mcp_image_bridge_live_chatgpt_vision_qualified.md
docs/checkpoints/284_model_free_mcp_image_bridge_live_chatgpt_vision_qualified.md
docs/local_execution/validation/044_managed_primary_runtime_poppler_page_rendering_probe_qualified.md
docs/checkpoints/285_managed_primary_runtime_poppler_page_rendering_probe_qualified.md
docs/local_execution/validation/045_sandboxed_managed_pdf_render_publication_preflight_qualified.md
docs/checkpoints/286_sandboxed_managed_pdf_render_publication_preflight_qualified.md
docs/local_execution/validation/046_document_render_live_source_published_restart_pending.md
docs/checkpoints/287_document_render_live_source_published_restart_pending.md
docs/local_execution/validation/047_document_render_live_chatgpt_vision_qualified.md
docs/checkpoints/288_document_render_live_chatgpt_vision_qualified.md
docs/local_execution/validation/048_representative_pdf_fidelity_exposes_windows_command_exec_capture_ceiling.md
docs/checkpoints/289_representative_pdf_fidelity_exposes_windows_command_exec_capture_ceiling.md
docs/local_execution/validation/049_official_pdf_skill_local_ads_handoff_research_prioritized.md
docs/checkpoints/290_official_pdf_skill_local_ads_handoff_research_prioritized.md
docs/OPEN_ARCHITECTURE_BACKLOG.md
docs/local_execution/DIRECT_GIT_INVESTIGATION_LESSONS.md
docs/model_collaboration/README.md
docs/model_collaboration/INTERACTION_PROVENANCE_AND_NAMING.md
docs/model_collaboration/DEFERRED_REVIEW_AND_CATCHUP.md
docs/model_collaboration/REVIEW_INBOX.md
docs/checkpoints/204_multimodel_collaboration_method_promoted.md
docs/checkpoints/265_development_method_v06_knowledge_routing_and_verification_reconciliation.md
docs/checkpoints/266_repository_information_architecture_and_exhaustive_knowledge_routing.md
docs/checkpoints/267_cockpit_frontend_paused_source_vault_bootstrap_resumed.md
docs/checkpoints/268_first_corpus_matched_codexless_local_execution_evaluation_opened.md
docs/checkpoints/269_codexless_read_path_verified_continuity_reconciled_for_chatgpt_12_handoff.md
docs/checkpoints/270_codexless_controlled_write_verified_local_execution_accepted.md
docs/checkpoints/271_bounded_direct_git_synchronization_verified_source_vault_resume_ready.md
docs/checkpoints/272_codex_desktop_thread_handoff_verified_deeplink_candidate_preflighted.md
docs/checkpoints/273_durable_bidirectional_codex_thread_handoff_verified_cooperative_release_next.md
docs/checkpoints/274_archive_unarchive_reacquire_verified_source_vault_ingestion_resumed.md
docs/checkpoints/275_guided_proceed_in_chat_roundtrip_verified_source_vault_active.md
docs/checkpoints/276_codex_codexless_upstream_ecosystem_research_opened_source_vault_paused.md
```

### Project Cockpit product architecture and professional interaction model
<!-- KM-TOPIC: cockpit-core -->

Use for the interactive workspace vision, project-object integration, professional UI foundation and promoted Cockpit interaction architecture.

```text
docs/DECISIONS.md
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
docs/specifications/006_v1_frontend_architecture_and_visual_spike.md
docs/specifications/007_v1_unified_project_cockpit_interaction_spike.md
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
docs/research/002_primary_project_cockpit_interface_concept.md
docs/research/003_unified_cockpit_workspace_and_spatial_focus_architecture.md
docs/research/004_cockpit_spatial_scalability_immersive_chrome_and_fullscreen.md
docs/research/037_project_cockpit_next_generation_visual_interaction_design_exploration_map.md
docs/research/038_mc0004_comparative_cockpit_design_synthesis_and_mockup_direction_set.md
docs/research/039_phase_c_browser_rendered_design_experiment_protocol_and_grid_world_slice.md
docs/research/087_holistic_integrated_cockpit_baseline_and_accepted_invariants_audit.md
docs/cockpit/PHASE_C_DECISION_LEDGER.md
docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
docs/checkpoints/267_cockpit_frontend_paused_source_vault_bootstrap_resumed.md
```

### Cockpit world, canvas, grid, ambient dynamics and spatial navigation
<!-- KM-TOPIC: cockpit-world -->

Use for canvas dominance, grid world, zoom, ambient dynamics, world continuity and spatial orientation.

```text
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
docs/specifications/007_v1_unified_project_cockpit_interaction_spike.md
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
docs/research/004_cockpit_spatial_scalability_immersive_chrome_and_fullscreen.md
docs/research/005_cockpit_canvas_dominance_zoom_and_scalable_project_navigation.md
docs/research/006_fourth_cockpit_human_review_balanced_spatial_world_and_visual_orientation.md
docs/research/007_fifth_cockpit_human_review_continuous_grid_world_stage_ruler_and_vertical_tool_rail.md
docs/research/008_sixth_cockpit_human_review_world_ambient_continuity_pinch_stability_and_collision_safety.md
docs/research/009_seventh_cockpit_human_review_pinch_responsiveness_and_interaction_promotion.md
docs/research/037_project_cockpit_next_generation_visual_interaction_design_exploration_map.md
docs/research/038_mc0004_comparative_cockpit_design_synthesis_and_mockup_direction_set.md
docs/research/039_phase_c_browser_rendered_design_experiment_protocol_and_grid_world_slice.md
docs/research/040_grid_world_g4_selection_dark_first_and_ambient_dynamics_exploration.md
docs/research/041_combined_g4_ambient_motion_intensity_tuning.md
docs/research/042_g4_randomized_ambient_distribution_and_grid_intersection_glints.md
docs/research/043_g4_major_grid_glints_and_decoupled_ambient_cadence.md
docs/cockpit/PHASE_C_DECISION_LEDGER.md
```

### WorkUnit visual grammar, appearance, disposition and runtime carriers
<!-- KM-TOPIC: work-unit-visual-grammar -->

Use for WorkUnit shape/category grammar, lighting, configurable appearance, disposition, runtime, blockers and attention presentation.

```text
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
docs/foundations/023_user_configurable_cockpit_appearance_and_semantic_invariants.md
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
docs/research/044_work_unit_interaction_lighting_hover_response_exploration.md
docs/research/045_h4_resting_node_light_world_spill_refinement.md
docs/research/046_work_unit_category_and_silhouette_visual_grammar_experiment.md
docs/research/047_work_unit_grammar_h4_control_correction_and_inbox_light_comparison.md
docs/research/048_claude_work_unit_grammar_synthesis_and_expanded_browser_round.md
docs/research/049_focused_work_unit_grammar_convergence_and_true_shape_experiment.md
docs/research/050_scientific_marker_selection_and_micro_material_shape_refinement.md
docs/research/051_user_configurable_cockpit_visual_grammar_and_semantic_invariants.md
docs/research/052_configurable_cockpit_review_connector_geometry_fix_and_foundation_promotion.md
docs/research/059_work_unit_project_disposition_visual_grammar_experiment.md
docs/research/060_disposition_hybrid_refinement_and_mixed_category_practical_comparison.md
docs/research/061_project_disposition_neutral_tag_tone_convergence_refinement.md
docs/research/065_work_unit_runtime_state_visual_grammar_experiment.md
docs/research/066_conditional_runtime_state_and_project_disposition_semantic_correction.md
docs/research/067_switchable_runtime_carrier_convergence_and_r1_r5_verification.md
docs/research/068_runtime_tag_motion_clean_perimeter_alternatives.md
docs/research/069_blocked_as_orthogonal_progress_constraint_visual_grammar_experiment.md
docs/research/070_shared_operational_status_carrier_blocker_relationship_and_work_unit_detail_deferment.md
docs/research/071_work_unit_attention_priority_visual_grammar_experiment.md
docs/research/072_work_unit_selection_persistent_state_visual_grammar_experiment.md
docs/research/073_work_unit_contextual_detail_expansion_architecture_experiment.md
docs/research/074_work_unit_internal_layout_grammar_experiment.md
docs/cockpit/PHASE_C_DECISION_LEDGER.md
docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
```

### Connector, port, relation-class and directionality visual grammar
<!-- KM-TOPIC: connector-visual-grammar -->

Use for composable connector presentation, ports, directionality, relation classes and semantic/non-semantic visual channels.

```text
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
docs/foundations/023_user_configurable_cockpit_appearance_and_semantic_invariants.md
docs/foundations/024_composable_connector_presentation_and_semantic_directionality.md
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
docs/research/051_user_configurable_cockpit_visual_grammar_and_semantic_invariants.md
docs/research/052_configurable_cockpit_review_connector_geometry_fix_and_foundation_promotion.md
docs/research/053_connector_and_port_visual_grammar_experiment.md
docs/research/054_connector_composition_directionality_and_endpoint_layering_refinement.md
docs/research/055_connector_presentation_configurability_and_directionality_browser_slice.md
docs/research/056_directionality_arrow_grammar_and_hover_separation_refinement.md
docs/research/057_semantic_relation_class_visual_grammar_experiment.md
docs/research/058_relation_class_hue_tag_selection_and_stroke_channel_reservation.md
docs/cockpit/PHASE_C_DECISION_LEDGER.md
docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
```

### Selection, expansion, focus, Deep Dive and semantic zoom states
<!-- KM-TOPIC: interaction-focus -->

Use for persistent selection, contextual expansion, current-process Focus, Deep Dive/specialist transitions and semantic-zoom decisions.

```text
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
docs/research/062_current_process_focus_lens_and_context_suppression_experiment.md
docs/research/063_user_curated_current_process_focus_membership.md
docs/research/071_work_unit_attention_priority_visual_grammar_experiment.md
docs/research/072_work_unit_selection_persistent_state_visual_grammar_experiment.md
docs/research/073_work_unit_contextual_detail_expansion_architecture_experiment.md
docs/research/074_work_unit_internal_layout_grammar_experiment.md
docs/research/075_work_unit_deep_focus_transition_architecture_experiment.md
docs/research/076_claude_informed_factorized_deep_focus_transition_experiment.md
docs/research/077_fullscreen_specialist_workspace_and_spatial_zoom_transition_experiment.md
docs/research/078_project_world_semantic_zoom_level_of_detail_experiment.md
docs/cockpit/PHASE_C_DECISION_LEDGER.md
docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
```

### Conversation Workspace, scope, navigation and Cockpit coexistence
<!-- KM-TOPIC: conversation-workspace -->

Use for conversation scope, Quiet Graphite, Boxes/Text, A6, coexistence with Grid/Deep Dive, state preservation, adaptive dock and presentation-integrity work.

```text
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
docs/research/079_conversation_workspace_presentation_architecture_experiment.md
docs/research/081_independent_conversation_workspace_dual_design_comparison.md
docs/research/082_conversation_scope_work_unit_anchor_and_quiet_graphite_baseline.md
docs/research/083_a6_adaptive_anchor_and_canonical_box_sidebar_mode.md
docs/research/084_claude_informed_conversation_anchor_synthesis.md
docs/research/085_conversation_workspace_a6_refinement_and_entry_transition.md
docs/research/086_conversation_workspace_orthogonal_access_and_coexistence_architecture.md
docs/research/095_conversation_spacing_flat_project_rail_and_live_topology_compass.md
docs/research/096_structural_conversation_spacing_and_current_project_tool_rail_control_set.md
docs/research/097_professional_conversation_copresence_and_adaptive_dock_study.md
docs/research/098_intermittent_cockpit_presentation_state_integrity_recovery.md
docs/research/099_conversation_boxes_visible_separation_human_retest_and_row_owned_geometry_recovery.md
docs/research/100_conversation_boxes_css_grid_track_absorption_and_live_geometry_recovery.md
docs/research/101_project_general_thread_short_viewport_containment_recovery.md
docs/research/102_project_general_box_footprint_and_selection_frame_alignment.md
docs/checkpoints/255_flat_project_rail_conversation_spacing_and_live_compass_review_opened.md
docs/checkpoints/258_adaptive_conversation_dock_human_review_opened.md
docs/checkpoints/264_project_general_footprint_and_selection_frame_human_recheck_opened.md
docs/checkpoints/267_cockpit_frontend_paused_source_vault_bootstrap_resumed.md
docs/cockpit/PHASE_C_DECISION_LEDGER.md
docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
```

### Cockpit implementation provenance, source-faithful reintegration and fidelity
<!-- KM-TOPIC: cockpit-provenance -->

Use for the holistic-integration failure, exact implementation recovery, provenance manifests, source-faithful reintegration, historical intermediate fidelity milestones and fidelity verification.

```text
docs/DEVELOPMENT_METHOD.md
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
docs/research/087_holistic_integrated_cockpit_baseline_and_accepted_invariants_audit.md
docs/research/088_integrated_cockpit_fidelity_failure_and_source_of_truth_recovery_audit.md
docs/research/089_cockpit_implementation_provenance_recovery_completion_and_exact_history_gate.md
docs/research/090_current_branch_exact_source_compatibility_and_reintegration_strategy.md
docs/research/091_source_faithful_reintegration_interaction_integrity_gate.md
docs/research/098_intermittent_cockpit_presentation_state_integrity_recovery.md
docs/research/103_repository_knowledge_discoverability_and_risk_scaled_verification_audit.md
docs/checkpoints/251_cockpit_implementation_provenance_recovered_and_reintegration_opened.md
docs/checkpoints/intermediate_2026-08-28_source_faithful_reintegration_interaction_integrity_gate.md
docs/checkpoints/267_cockpit_frontend_paused_source_vault_bootstrap_resumed.md
docs/cockpit/README.md
docs/cockpit/PHASE_C_DECISION_LEDGER.md
docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
docs/cockpit/accepted_implementation_manifest.json
scripts/check_cockpit_implementation_manifest.py
.github/workflows/cockpit-implementation-provenance.yml
.github/workflows/cockpit-reintegration-fidelity.yml
scripts/select_cockpit_verification.py
```

### Cockpit shell, project rail, topology compass and docking studies
<!-- KM-TOPIC: shell-rail -->

Use for right-edge shell/rail studies, depth/direct manipulation, the flat project rail, live topology compass and adaptive docking.

```text
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
docs/research/092_spatial_edge_rail_depth_direct_manipulation_and_docking_study.md
docs/research/093_architectural_cockpit_edge_instrument_surface_depth_study.md
docs/research/094_resting_angled_rail_spatial_identity_and_clarity_only_expansion.md
docs/research/095_conversation_spacing_flat_project_rail_and_live_topology_compass.md
docs/research/096_structural_conversation_spacing_and_current_project_tool_rail_control_set.md
docs/research/097_professional_conversation_copresence_and_adaptive_dock_study.md
docs/checkpoints/255_flat_project_rail_conversation_spacing_and_live_compass_review_opened.md
docs/checkpoints/258_adaptive_conversation_dock_human_review_opened.md
docs/checkpoints/267_cockpit_frontend_paused_source_vault_bootstrap_resumed.md
docs/cockpit/PHASE_C_DECISION_LEDGER.md
```

### Canonical decisions, principles, major changes and unresolved questions
<!-- KM-TOPIC: canonical-history -->

Use when reconstructing why the current project looks the way it does, what is explicitly accepted, what changed structurally and what remains open.

```text
docs/VISION.md
docs/PRINCIPLES.md
docs/DECISIONS.md
docs/OPEN_QUESTIONS.md
docs/MAJOR_CHANGES.md
docs/README.md
docs/checkpoints/README.md
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
docs/research/064_rapid_iteration_repository_preservation_audit_and_checkpoint_hygiene.md
docs/research/103_repository_knowledge_discoverability_and_risk_scaled_verification_audit.md
docs/research/104_repository_information_architecture_and_exhaustive_knowledge_routing_refinement.md
docs/research/108_historical_intermediate_checkpoint_integrity_and_discoverability_audit.md
docs/methodological_knowledge/COVERAGE_MAP.md
docs/cockpit/PHASE_C_DECISION_LEDGER.md
docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
docs/model_collaboration/REVIEW_INBOX.md
docs/checkpoints/267_cockpit_frontend_paused_source_vault_bootstrap_resumed.md
```

## Historical checkpoint topic routing

The following compact routing records assign every numbered checkpoint to one or more subjects. This keeps chronological knowledge exhaustively classifiable without turning the human-facing library into a second copy of the checkpoint directory.

<!-- KM-CHECKPOINT-RANGE: 000-010 system-identity knowledge-representation evaluation-falsification -->
<!-- KM-CHECKPOINT-RANGE: 011-096 evaluation-falsification -->
<!-- KM-CHECKPOINT-RANGE: 097-107 knowledge-representation -->
<!-- KM-CHECKPOINT-RANGE: 108-115 runtime-persistence -->
<!-- KM-CHECKPOINT-RANGE: 116-126 cockpit-core cockpit-world -->
<!-- KM-CHECKPOINT-RANGE: 127-133 runtime-persistence -->
<!-- KM-CHECKPOINT-RANGE: 134-146 retrieval-horizon -->
<!-- KM-CHECKPOINT-RANGE: 147-185 recommendation-action -->
<!-- KM-CHECKPOINT-RANGE: 186-193 methodological-knowledge-universe project-state -->
<!-- KM-CHECKPOINT-RANGE: 194-198 source-universe -->
<!-- KM-CHECKPOINT-RANGE: 199-205 development-governance -->
<!-- KM-CHECKPOINT-RANGE: 206-210 cockpit-world development-governance -->
<!-- KM-CHECKPOINT-RANGE: 211-217 cockpit-world work-unit-visual-grammar -->
<!-- KM-CHECKPOINT-RANGE: 218-224 work-unit-visual-grammar -->
<!-- KM-CHECKPOINT-RANGE: 225-229 connector-visual-grammar work-unit-visual-grammar -->
<!-- KM-CHECKPOINT-RANGE: 230-240 work-unit-visual-grammar interaction-focus -->
<!-- KM-CHECKPOINT-RANGE: 241-245 interaction-focus -->
<!-- KM-CHECKPOINT-RANGE: 246-248 conversation-workspace -->
<!-- KM-CHECKPOINT-RANGE: 249-252 cockpit-provenance cockpit-core shell-rail -->
<!-- KM-CHECKPOINT-RANGE: 253-257 shell-rail conversation-workspace -->
<!-- KM-CHECKPOINT-RANGE: 258-264 conversation-workspace cockpit-provenance -->
<!-- KM-CHECKPOINT-RANGE: 265-266 development-governance -->
<!-- KM-CHECKPOINT-RANGE: 267-267 source-universe development-governance cockpit-core conversation-workspace shell-rail -->
<!-- KM-CHECKPOINT-RANGE: 268-272 source-universe development-governance -->
<!-- KM-CHECKPOINT-RANGE: 273-273 development-governance -->
<!-- KM-CHECKPOINT-RANGE: 274-274 source-universe development-governance -->
<!-- KM-CHECKPOINT-RANGE: 275-275 source-universe development-governance -->
<!-- KM-CHECKPOINT-RANGE: 276-276 source-universe development-governance -->
<!-- KM-CHECKPOINT-RANGE: 277-278 development-governance -->
<!-- KM-CHECKPOINT-RANGE: 279-279 development-governance -->
<!-- KM-CHECKPOINT-RANGE: 280-290 development-governance -->

Important numbered checkpoints are linked directly in the subject sections above. Governed historical intermediate milestones are also linked directly because they have no numeric range identity. For exact chronological history, use `docs/checkpoints/README.md`, the checkpoint directory, specialized ledgers and Git history.

## Specialized library indexes

```text
docs/methodological_knowledge/COVERAGE_MAP.md
docs/cockpit/PHASE_C_DECISION_LEDGER.md
docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
docs/model_collaboration/REVIEW_INBOX.md
```

These are first-class routing surfaces for domains where one global map would otherwise become too large.

## Maintenance rule

At a meaningful promotion or reconciliation boundary:

```text
1. route every new numbered foundation/specification/research record to at least one subject;
2. add multiple subject memberships when that improves retrieval;
3. keep current/live state out of this file and update CURRENT_STATE/current_routing instead;
4. link specialized indexes rather than duplicating their full contents;
5. preserve maturity and authority distinctions in the source artifacts themselves;
6. extend checkpoint range routing when new checkpoint numbers move beyond the covered range;
7. directly route every governed historical intermediate checkpoint milestone under at least one subject;
8. add a new subject only when a genuinely distinct durable knowledge domain emerges;
9. run scripts/check_knowledge_map.py.
```

Do not update this map merely because another commit exists. Update it when the project's durable knowledge structure changes.
