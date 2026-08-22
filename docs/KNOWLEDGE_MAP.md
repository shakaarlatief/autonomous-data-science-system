# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources but does not replace them.  
**Last reviewed:** 2026-08-22  
**Current checkpoint:** 143  
**Active development branch:** `v1-relevance-selective-context`  
**Active promotion PR:** #11 into `v1-frontend-spike`

## Start here

For a new session or quick reconstruction:

```text
README.md
    project-level overview and current stage

docs/CURRENT_STATE.md
    present state, active gate, exact next step

docs/KNOWLEDGE_MAP.md
    routing layer

docs/VISION.md
    current system purpose and product direction

docs/PRINCIPLES.md
    current high-level design principles

docs/DECISIONS.md
    accepted project-level decisions

docs/OPEN_QUESTIONS.md
    current unresolved questions

docs/DEVELOPMENT_METHOD.md
    preservation/development method

docs/CONTINUITY.md
    continuation and unexpected-boundary recovery

docs/MAJOR_CHANGES.md
    selective structural history
```

Current branch relationship:

```text
active selective-context promotion branch = v1-relevance-selective-context
active PR                             = #11 -> v1-frontend-spike
promoted V1 integration branch       = v1-frontend-spike
main intentionally trails current V1 work
```

The integration branch contains the retrieval/MethodologicalHorizon promotion from PR #10 at:

```text
9319ed9b0a401efa1be85c27a9ce4424a8ce5e1e
```

PR #11 adds the first accepted bounded `MethodologicalContextPack` selection/serialization seam after a successful preregistered RH-C gate.

---

## Current project stage

Prototype V0 is complete with final classification:

> **STRONG FALSIFICATION OF THE CURRENT P0 DESIGN**

Current V1 boundaries:

```text
methodological/object architecture
    Foundations 018-020

governed persistence/interchange
    D-028 through D-031
    closed current seam through Checkpoint 127

Project Cockpit interaction architecture
    Specification 008 promoted through Checkpoint 126
    bounded post-promotion polish through Checkpoint 130

reasoning runtime
    D-032 accepted after completed Specification 005 bakeoff
    OpenAI Agents SDK behind ADS-owned runtime port
    Checkpoint 133

production retrieval / MethodologicalHorizon
    Specification 009 benchmark decomposition
    Checkpoint 135 production lexical PASS
    Checkpoint 137 dense-only comparator preserved
    Checkpoint 139 hybrid retrieval PASS
    Specification 012 v1.0
    Checkpoint 141 first explained MethodologicalHorizon PASS

relevance / selective methodological context
    Research 020
    Specification 013 v1.0 accepted bounded seam
    Checkpoint 142 frozen contract
    Checkpoint 143 successful promotion
    V1_SELECTIVE_CONTEXT_RESULT.md

next
    real reasoning vertical slice
    selective context vs strong full-Horizon/simple control
    one concrete model configuration through ReasoningRuntime
```

---

## Core system boundary

Primary sources:

```text
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
```

Durable interpretation:

```text
LLM
    flexible reasoning component

ADS
    persistent project/process intelligence
    methodological knowledge
    provenance
    deterministic controls where justified
    execution coordination
    professional reasoning/control surface

Human
    goals
    semantics
    consequential judgment
    approvals/intervention where useful
```

Every explicit mechanism must earn its complexity empirically.

---

## Prototype V0 constraint

Authoritative evidence:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
prototype_v0/README.md
docs/checkpoints/096_prototype_v0_final_strong_falsification_and_architecture_diagnostic_conclusion.md
```

Core lesson:

```text
what the SYSTEM should remember
    !=
what the LLM should receive on every reasoning call
```

Do not reintroduce unchanged full structured state every cycle, large always-on context/frontier, path-sensitive trigger activation, generic recursive support reassessment, or universal dependency reopening.

---

## Project object model

Primary source:

```text
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
```

Core structures:

```text
OBJECTS
RELATIONS
EVENTS
VIEWS
```

Important distinctions:

```text
Investigation != Run
Evidence != Finding
Finding != Claim
Claim != Decision
current state != event history
persisted object != derived recommendation
workspace section != fundamental object
```

---

## Methodological navigation and reusable knowledge

Primary sources:

```text
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
```

Relevance progression:

```text
KNOWN -> APPLICABLE -> RELEVANT -> RECOMMENDED -> REQUIRED / BLOCKING
```

Current scaling path:

```text
large global knowledge universe
    -> high-recall project-specific retrieval/filtering
    -> bounded explained MethodologicalHorizon
    -> explicit applicability/context checks
    -> bounded task-specific relevance selection
    -> selective MethodologicalContextPack
    -> real reasoning
```

Reusable representation includes:

```text
KnowledgeAsset
KnowledgeComponent
NarrativeFacet
KnowledgeRelation
conditional KnowledgeRule
KnowledgeCollection
exact stable/revision identity
criterion Finding
ExecutionCapability
```

---

## Accepted V1 persistence, tooling, and interchange

Primary decisions/specifications:

```text
D-028 + docs/specifications/001_v1_sqlite_technical_architecture.md
D-029 + docs/specifications/002_v1_persistence_tooling_standard.md
D-030 + docs/specifications/003_v1_python_project_and_dependency_tooling.md
D-031 + docs/specifications/004_v1_reusable_knowledge_interchange.md
```

Governed round-trip closure:

```text
experiments/architecture_spikes/V1_KNOWLEDGE_ROUNDTRIP_RESULT.md
docs/checkpoints/127_governed_knowledge_roundtrip_closed_across_sqlite_and_postgresql.md
```

Run `32496856945` passed SQLite Ubuntu, SQLite Windows, PostgreSQL 18, and the Alembic revision-ID guard.

---

## Selected V1 reasoning runtime and closed bakeoff

Accepted decision:

```text
D-032
    OpenAI Agents SDK behind an ADS-owned ReasoningRuntime port
    validated starting package openai-agents==0.19.4
```

Primary evidence:

```text
docs/specifications/005_v1_agent_runtime_and_interoperability_bakeoff.md
docs/research/013_openai_agents_complete_candidate_evidence_and_direct_call_comparison.md
docs/research/014_langgraph_1_2_10_released_durability_comparator_audit.md
docs/research/015_langgraph_complete_candidate_three_way_runtime_comparison_and_stop_rule.md

docs/checkpoints/129_direct_model_call_runtime_control_cross_platform_gate_passed.md
docs/checkpoints/131_openai_agents_complete_runtime_candidate_cross_platform_gate_passed.md
docs/checkpoints/132_langgraph_durability_comparator_cross_platform_gate_passed.md
docs/checkpoints/133_v1_reasoning_runtime_selected_and_bakeoff_closed.md

experiments/runtime_bakeoff/DIRECT_CALL_CONTROL_RESULT.md
experiments/runtime_bakeoff/candidates/openai_agents/COMPLETE_RESULT.md
experiments/runtime_bakeoff/candidates/langgraph_runtime/COMPLETE_RESULT.md
```

Interpretation:

```text
OpenAI Agents SDK
    selected initial V1 runtime infrastructure

direct model calls
    minimum-dependency fallback/reference

LangGraph
    future stronger-durability escalation path
```

No final LLM provider/model or multi-agent architecture is selected.

---

## Professional frontend and Project Cockpit

Primary promoted contract:

```text
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
```

Key evidence:

```text
docs/research/002_primary_project_cockpit_interface_concept.md
docs/research/003_unified_cockpit_workspace_and_spatial_focus_architecture.md
docs/research/004_cockpit_spatial_scalability_immersive_chrome_and_fullscreen.md
docs/research/005_cockpit_canvas_dominance_zoom_and_scalable_project_navigation.md
docs/research/006_fourth_cockpit_human_review_balanced_spatial_world_and_visual_orientation.md
docs/research/007_fifth_cockpit_human_review_continuous_grid_world_stage_ruler_and_vertical_tool_rail.md
docs/research/008_sixth_cockpit_human_review_world_ambient_continuity_pinch_stability_and_collision_safety.md
docs/research/009_seventh_cockpit_human_review_pinch_responsiveness_and_interaction_promotion.md
docs/research/012_post_promotion_cockpit_normal_window_and_pinch_sensitivity_review.md

docs/checkpoints/126_seventh_cockpit_review_validated_and_interaction_architecture_promoted.md
docs/checkpoints/130_post_promotion_cockpit_normal_window_and_pinch_polish_gate_passed.md
```

Specification 008 remains current. Exact gesture constants, graph/canvas library, auto-layout, semantic zoom, minimap, final stage taxonomy, final URL contract, project-search backend, frontend stack promotion, chart library, and final visual identity remain unfrozen.

---

## Production retrieval route

### Lexical baseline

```text
docs/research/016_production_retrieval_and_methodological_horizon_benchmark_design.md
docs/specifications/009_v1_retrieval_and_methodological_horizon_benchmark.md
docs/checkpoints/134_retrieval_and_methodological_horizon_benchmark_contract_frozen.md
docs/checkpoints/135_first_production_lexical_retrieval_baseline_cross_platform_passed.md
experiments/retrieval/V1_LEXICAL_RETRIEVAL_RESULT.md
```

Result:

```text
RH-L Recall@3  1.00
RH-L MRR       1.00
RH-S Recall@3  0.75
```

### Exact dense comparator

```text
docs/research/017_exact_semantic_retrieval_comparator_selection.md
docs/specifications/010_v1_exact_semantic_retrieval_comparator.md
docs/checkpoints/136_exact_semantic_retrieval_comparator_contract_frozen.md
docs/checkpoints/137_dense_semantic_retrieval_comparator_cross_platform_result_preserved.md
```

Dense recovers `class-imbalance` but misses lexical `ecdf`; dense-only does not replace lexical retrieval.

### Hybrid comparator

```text
docs/research/018_dense_semantic_failure_complementarity_and_rrf_fusion_rationale.md
docs/specifications/011_v1_rrf_hybrid_retrieval_comparator.md
docs/checkpoints/138_rrf_hybrid_retrieval_comparator_contract_frozen.md
docs/checkpoints/139_rrf_hybrid_retrieval_cross_platform_gate_passed.md
experiments/retrieval/V1_RRF_HYBRID_RETRIEVAL_RESULT.md
```

Run `32561118325`:

```text
Ubuntu PASS
Windows PASS
RH-S Recall@3  1.00
RH-S MRR       0.875
RH-L Recall@3  1.00
RH-L MRR       1.00
```

This is evidence for channel complementarity, not permanent selection of FastEmbed, BGE, RRF `k=60`, embeddings persistence, ANN, or a vector database.

Production lexical implementation routes:

```text
src/ads_system/application/retrieval.py
src/ads_system/application/ports.py
src/ads_system/infrastructure/retrieval/sqlite_fts.py
```

---

## First production-facing MethodologicalHorizon route

Primary design/evidence:

```text
docs/research/019_first_methodological_horizon_application_seam.md
docs/specifications/012_v1_first_methodological_horizon_builder.md
docs/checkpoints/140_first_methodological_horizon_builder_contract_frozen.md
docs/checkpoints/141_first_methodological_horizon_cross_platform_gate_passed.md
experiments/retrieval/V1_METHODOLOGICAL_HORIZON_RESULT.md
```

Validated architecture:

```text
stable/revision-transparent direct candidate
    -> KnowledgeNavigationRepository
    -> accepted-current one-hop outbound relations
    -> deterministic three-valued applicability
    -> explained MethodologicalHorizon
```

Key semantic distinction:

```text
known false -> INAPPLICABLE
unknown required information -> MISSING_CONTEXT
unknown != false
```

Current implementation routes:

```text
src/ads_system/application/horizon.py
src/ads_system/application/horizon_models.py
src/ads_system/application/ports.py
src/ads_system/infrastructure/persistence/navigation_repository.py
```

---

## Selective MethodologicalContextPack route

### Design and frozen contract

```text
docs/research/020_first_horizon_relevance_and_selective_context_gate_design.md
docs/specifications/013_v1_horizon_relevance_and_selective_context.md
docs/checkpoints/142_relevance_and_selective_context_contract_frozen.md
```

### Result and promotion

```text
experiments/retrieval/V1_SELECTIVE_CONTEXT_RESULT.md
docs/checkpoints/143_selective_methodological_context_gate_passed_and_promotion_authorized.md
```

Frozen policy:

```text
requested reasoning functions
    -> primary function matches
    -> bounded REQUIRES_CONCEPT support
    -> hard max_assets
    -> exact accepted-current compact context reads
    -> MethodologicalContextPack
```

Observed on the wide ten-asset Horizon:

```text
RH-C01  2 selected  ratio 0.20020477
RH-C02  2 selected  ratio 0.16462054
RH-C03  3 selected  ratio 0.34635417
RH-C04  2 selected  ratio 0.28222057
```

Across all cases:

```text
required stable-key coverage      1.00
required revision coverage        1.00
irrelevant selected               0
unexplained omissions             0
```

Validated full suite:

```text
Ubuntu   42 passed, 2 skipped
Windows  42 passed, 2 skipped
```

Current implementation routes:

```text
src/ads_system/application/context_models.py
src/ads_system/application/context_selection.py
src/ads_system/application/horizon.py
src/ads_system/application/horizon_models.py
src/ads_system/application/ports.py
src/ads_system/infrastructure/persistence/navigation_repository.py

tests/fixtures/retrieval/selective_context_v1.json
tests/integration/test_selective_methodological_context.py
tests/unit/test_context_selection.py
```

Specification 013 v1.0 accepts the bounded seam but does not promote `max_assets = 3`, reasoning functions as a complete relevance solution, or the ten-asset benchmark as production policy.

---

## Current exact priorities

```text
A. finish PR #11 canonical/routing reconciliation
B. update PR #11 with the measured RH-C result
C. validate the exact final PR #11 head
D. merge exactly that green head into v1-frontend-spike
E. branch from the promoted merge boundary
F. preregister the first real reasoning vertical slice
G. compare selective context with a strong full-Horizon/simple control under one concrete model configuration
```

The next measured bottleneck is downstream reasoning quality and real model/token cost, not further retrieval tuning.

---

## Recent continuity checkpoints

```text
127  governed knowledge round-trip closed across SQLite/PostgreSQL
128  runtime-bakeoff preimplementation evidence refreshed
129  direct model-call runtime control cross-platform PASS
130  post-promotion Cockpit normal-window/pinch polish PASS
131  OpenAI Agents SDK complete candidate cross-platform PASS
132  LangGraph durability comparator cross-platform PASS
133  initial V1 reasoning runtime selected; Specification 005 closed
134  retrieval / MethodologicalHorizon benchmark contract frozen
135  first production lexical retrieval baseline cross-platform PASS
136  exact dense semantic comparator contract frozen
137  dense semantic comparator result preserved; standalone gate FAIL
138  RRF hybrid comparator contract frozen
139  RRF hybrid comparator cross-platform PASS
140  first MethodologicalHorizon builder contract frozen
141  first MethodologicalHorizon cross-platform PASS
142  relevance/selective-context contract frozen
143  selective-context gate passed; Specification 013 promotion authorized
```
