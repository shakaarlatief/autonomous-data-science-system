# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources but does not replace them.  
**Last reviewed:** 2026-08-23  
**Current checkpoint:** 151  
**Active development branch:** `v1-recommendation-action-failure-preservation`  
**Active preservation PR:** #14 -> `v1-frontend-spike`  
**Rejected experiment PR:** #13 (`v1-recommendation-action-value` -> `v1-frontend-spike`), close without merge  
**Promoted V1 integration branch:** `v1-frontend-spike` at PR #12 merge commit `bd7d1ec5cabc80d39e005d0a12c11295da32f4a6`

## Start here

```text
README.md
    project overview and current active track

docs/CURRENT_STATE.md
    present state, current gate, exact next action

docs/KNOWLEDGE_MAP.md
    routing/index layer

docs/VISION.md
    high-level system and product direction

docs/PRINCIPLES.md
    accepted high-level design principles

docs/DECISIONS.md
    accepted project-level decisions

docs/OPEN_QUESTIONS.md
    unresolved design/evaluation questions

docs/DEVELOPMENT_METHOD.md
    development, checkpoint, promotion, and reconciliation method

docs/CONTINUITY.md
    continuation and unexpected-boundary recovery

docs/MAJOR_CHANGES.md
    selective structural history
```

Current branch relationship:

```text
accepted integration head        bd7d1ec5cabc80d39e005d0a12c11295da32f4a6
failed experiment branch         v1-recommendation-action-value
failed experiment PR             #13, do not merge
failure-preservation branch      v1-recommendation-action-failure-preservation
failure-preservation PR          #14 -> v1-frontend-spike
main                             intentionally behind active V1 work except dispatcher exposure
```

---

## Current project stage

Prototype V0 is complete with final classification:

> **STRONG FALSIFICATION OF THE CURRENT P0 DESIGN**

Durable post-V0 constraint:

```text
what the SYSTEM should remember
    !=
what the LLM should receive on every reasoning call
```

Current V1 progression:

```text
Foundations 018-020
    object/state model, methodological navigation, reusable knowledge

D-028 through D-031 / Checkpoint 127
    local-first persistence and governed knowledge interchange

Specification 008 / Checkpoints 126 and 130
    promoted Project Cockpit interaction architecture

D-032 / Checkpoint 133
    OpenAI Agents SDK behind ADS-owned ReasoningRuntime

Checkpoints 135 -> 137 -> 139 -> 141
    lexical retrieval -> dense complementarity -> hybrid comparator -> explained Horizon

Specification 013 v1.0 / Checkpoint 143
    accepted selective exact-revision MethodologicalContextPack

Specification 014 v1.0 / Checkpoint 146
    first real-model selective-context value gate PASS
    quality 1.000000 vs 1.000000
    aggregate provider input-token ratio 0.334379
    66.56% input-token reduction

Specification 015 v0.1 / Checkpoints 147-150
    first recommendation/action-value experiment preregistered, implemented, and executed
    live workflow completed 36 reasoner + 36 blinded judge outputs with zero retries
    frozen advancement outcome FAIL
    failure localized to RA-02 DEFER-vs-NOT_NOW exact disposition calibration
    no recommendation/action seam promoted

Checkpoint 151 / PR #14
    preserve frozen negative evidence and canonical routing
    exclude the rejected recommendation implementation
```

---

## Core system and product boundary

Primary rationale:

```text
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
```

Current division:

```text
LLM
    flexible reasoning component

ADS
    project/process memory
    methodological knowledge/navigation
    provenance and deterministic controls
    execution coordination
    professional interaction surface

Human
    goals and semantics
    consequential judgment
    approvals/intervention where useful
```

Every explicit mechanism must earn its complexity empirically.

---

## Methodological navigation and reusable knowledge

Primary sources:

```text
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
```

Navigation progression:

```text
KNOWN -> APPLICABLE -> RELEVANT -> RECOMMENDED -> REQUIRED / BLOCKING
```

Current executable path:

```text
large reusable knowledge universe
    -> retrieval
    -> bounded explained MethodologicalHorizon
    -> applicability / missing-context checks
    -> bounded task-specific relevance selection
    -> selective MethodologicalContextPack
    -> ADS-owned ReasoningRuntime
    -> real reasoning evidence                      [accepted first bounded gate]
    -> recommendation / REQUIRED-BLOCKING evidence [first gate failed; diagnostic next]
```

Foundation 020 keeps reusable methodological knowledge distinct from project state, execution capability, and presentation.

---

## Accepted persistence, tooling, and interchange

```text
D-028 + docs/specifications/001_v1_sqlite_technical_architecture.md
D-029 + docs/specifications/002_v1_persistence_tooling_standard.md
D-030 + docs/specifications/003_v1_python_project_and_dependency_tooling.md
D-031 + docs/specifications/004_v1_reusable_knowledge_interchange.md
```

Governed persistence/interchange closure:

```text
experiments/architecture_spikes/V1_KNOWLEDGE_ROUNDTRIP_RESULT.md
docs/checkpoints/127_governed_knowledge_roundtrip_closed_across_sqlite_and_postgresql.md
```

The governed accepted-current knowledge seam is validated on SQLite/Ubuntu, SQLite/Windows, and PostgreSQL 18.

---

## Selected V1 reasoning runtime infrastructure

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
```

Interpretation:

```text
OpenAI Agents SDK    initial V1 runtime infrastructure
direct model calls   fallback/reference
LangGraph            possible stronger-durability escalation
```

No final LLM provider/model or multi-agent architecture is selected.

---

## Project Cockpit route

Promoted contract:

```text
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
```

Important checkpoints:

```text
docs/checkpoints/126_seventh_cockpit_review_validated_and_interaction_architecture_promoted.md
docs/checkpoints/130_post_promotion_cockpit_normal_window_and_pinch_polish_gate_passed.md
```

The Project Cockpit is the promoted primary immersive V1 active-work model. Direct specialist views remain alternative entry, inspection, and record paths.

Final frontend stack, chart library, canvas/gesture libraries, auto-layout, semantic zoom, minimap, final stage taxonomy, final URL contract, project-search backend, and visual identity remain open.

---

## Retrieval and MethodologicalHorizon route

### Lexical baseline

```text
docs/research/016_production_retrieval_and_methodological_horizon_benchmark_design.md
docs/specifications/009_v1_retrieval_and_methodological_horizon_benchmark.md
docs/checkpoints/135_first_production_lexical_retrieval_baseline_cross_platform_passed.md
experiments/retrieval/V1_LEXICAL_RETRIEVAL_RESULT.md
```

```text
RH-L Recall@3 = 1.00
RH-L MRR      = 1.00
```

### Dense and hybrid comparators

```text
docs/research/017_exact_semantic_retrieval_comparator_selection.md
docs/specifications/010_v1_exact_semantic_retrieval_comparator.md
docs/checkpoints/137_dense_semantic_retrieval_comparator_cross_platform_result_preserved.md

docs/research/018_dense_semantic_failure_complementarity_and_rrf_fusion_rationale.md
docs/specifications/011_v1_rrf_hybrid_retrieval_comparator.md
docs/checkpoints/139_rrf_hybrid_retrieval_cross_platform_gate_passed.md
experiments/retrieval/V1_RRF_HYBRID_RETRIEVAL_RESULT.md
```

Dense retrieval recovered the lexical `class-imbalance` miss but lost `ecdf`. Equal-weight RRF preserved both measured signals:

```text
RH-S Recall@3 = 1.00
RH-S MRR      = 0.875
```

This is complementarity evidence, not permanent selection of FastEmbed/BGE/RRF/vector infrastructure.

### First explained MethodologicalHorizon

```text
docs/research/019_first_methodological_horizon_application_seam.md
docs/specifications/012_v1_first_methodological_horizon_builder.md
docs/checkpoints/141_first_methodological_horizon_cross_platform_gate_passed.md
experiments/retrieval/V1_METHODOLOGICAL_HORIZON_RESULT.md
```

Key invariant:

```text
known false -> INAPPLICABLE
unknown required information -> MISSING_CONTEXT
unknown != false
```

---

## Selective MethodologicalContextPack route

Design/freeze:

```text
docs/research/020_first_horizon_relevance_and_selective_context_gate_design.md
docs/checkpoints/142_relevance_and_selective_context_contract_frozen.md
```

Accepted contract/result:

```text
docs/specifications/013_v1_horizon_relevance_and_selective_context.md
docs/checkpoints/143_selective_methodological_context_gate_passed_and_promotion_authorized.md
experiments/retrieval/V1_SELECTIVE_CONTEXT_RESULT.md
```

Observed ten-asset methodology-only selective/full ratios:

```text
RH-C01  0.20020477
RH-C02  0.16462054
RH-C03  0.34635417
RH-C04  0.28222057
```

Across all cases:

```text
required stable-key coverage       1.00
required exact-revision coverage   1.00
irrelevant selected assets         0
unexplained omissions              0
```

PR #11 promoted merge:

```text
fd33184fbff588c6737d77af751bc5def0e31954
```

---

## Accepted reasoning-context-value vertical slice

Design/freeze:

```text
docs/research/021_first_reasoning_context_value_vertical_slice_design.md
docs/checkpoints/144_first_reasoning_context_value_contract_frozen.md
docs/checkpoints/145_reasoning_context_value_implementation_gate_cross_platform_passed.md
```

Accepted contract/result:

```text
docs/specifications/014_v1_reasoning_context_value_vertical_slice.md
docs/checkpoints/146_first_real_reasoning_context_value_gate_passed.md
experiments/reasoning_context_value/V1_REASONING_CONTEXT_VALUE_RESULT.md
experiments/reasoning_context_value/results/spec014-live-20260823-run-32635061634/
```

Observed:

```text
reasoner outputs        24 / 24
judge outputs           24 / 24
retries                 0
SELECTIVE quality       1.000000
FULL_HORIZON quality    1.000000
aggregate token ratio   0.334379
input-token reduction   66.56%
critical regressions    none
```

This accepts the bounded selective-context + ADS-owned ReasoningRuntime seam. It does not select a final model/provider, universal context budget, general relevance mechanism, or recommendation/REQUIRED-BLOCKING policy.

PR #12 promoted merge:

```text
bd7d1ec5cabc80d39e005d0a12c11295da32f4a6
```

---

## Failed recommendation/action-value route

Frozen design/provenance:

```text
docs/research/022_first_recommendation_action_value_vertical_slice_design.md
docs/specifications/015_v1_recommendation_action_value_vertical_slice.md
tests/fixtures/reasoning/recommendation_action_v1.json
docs/checkpoints/147_first_recommendation_action_value_contract_frozen.md
docs/checkpoints/148_recommendation_action_provider_free_gate_cross_platform_passed.md
docs/checkpoints/149_specification_015_live_boundary_frozen.md
```

Live execution:

```text
V1 recommendation action value live
run 32642733784
source head d91d50fb2cc46b2047bc21bc5b2ea43c2b1049e4
36 / 36 reasoner outputs
36 / 36 blinded judge outputs
72 provider attempts
0 retries
```

Frozen advancement:

```text
absolute gates  FAIL
relative gates  PASS
expansion gates PASS
value signals   0
outcome          FAIL
```

Single failed gate:

```text
RA-G05
SELECTIVE per-case mean exact disposition accuracy >= 0.80
```

Localized failure:

```text
RA-02 MODEL_CHOICE
GENERIC        0.722222
SELECTIVE      0.666667
FULL_HORIZON   0.666667
```

The repeated mismatches were `DEFER` expected versus `NOT_NOW` observed for:

```text
add-generic-bagging-baseline
plot-all-feature-histograms-before-shortlist
```

All nine RA-02 outputs scored `1.000000` under the condition-blinded semantic judge. The discrepancy motivates disposition-semantics/failure-attribution diagnosis but does not change the frozen FAIL.

Preserved result:

```text
experiments/recommendation_action_value/V1_RECOMMENDATION_ACTION_VALUE_RESULT.md
experiments/recommendation_action_value/results/spec015-live-20260823-run-32642733784/
docs/checkpoints/150_specification_015_live_result_failed_exact_disposition_gate.md
```

PR #13 must close without merge. The failed implementation is not an accepted V1 boundary.

---

## Preservation-only failure route

Checkpoint 151 and PR #14 isolate the historical/frozen negative evidence from the rejected implementation.

```text
docs/checkpoints/151_specification_015_failure_preservation_only_boundary_green.md
branch  v1-recommendation-action-failure-preservation
PR      #14 -> v1-frontend-spike
```

Pre-checkpoint preservation/routing head:

```text
d843c39a26867c70557b978ff5faf778bda5aaaa
```

validated:

```text
Checkpoint metadata            run 32644994687   PASS
V1 reasoning context value     run 32644994598   PASS
```

The branch contains no failed recommendation application/runtime/harness implementation. Its purpose is to ensure negative evidence becomes durable project truth without accidentally promoting the mechanism that failed its gate.

---

## Current exact continuation

```text
A. validate the exact Checkpoint 151 / PR #14 head
B. merge PR #14 into v1-frontend-spike only if green
C. close PR #13 without merge
D. branch separately from the preserved integration line
E. preregister a DEFER-vs-NOT_NOW / failure-attribution diagnostic
F. make no new live model calls before that diagnostic contract is frozen
G. only after diagnosis decide whether a revised recommendation/action seam deserves another value experiment
```

Do not return to retrieval/reranking/vector work without a measured downstream reason.

---

## Recent continuity checkpoints

```text
127  governed knowledge round-trip closed across SQLite/PostgreSQL
133  initial V1 reasoning runtime selected
135  first production lexical retrieval baseline passed
137  dense semantic comparator preserved
139  hybrid retrieval comparator passed
141  first explained MethodologicalHorizon passed
142  selective-context contract frozen
143  selective-context gate passed and promoted
144  first reasoning-context-value contract frozen
145  provider-free reasoning-context-value implementation passed cross-platform
146  first real reasoning-context-value gate passed and promotion authorized
147  first recommendation/action-value contract frozen
148  recommendation/action provider-free implementation passed cross-platform
149  Specification 015 reconciled live-ready boundary frozen
150  Specification 015 live recommendation/action gate failed on exact disposition calibration
151  failed Specification 015 evidence isolated on preservation-only accepted-line branch
```
