# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources but does not replace them.  
**Last reviewed:** 2026-08-23  
**Current checkpoint:** 147  
**Active development branch:** `v1-recommendation-action-value`  
**Active promotion PR:** #13 into `v1-frontend-spike`  
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
active experiment branch  v1-recommendation-action-value
active PR                  #13 -> v1-frontend-spike
promoted integration head  bd7d1ec5cabc80d39e005d0a12c11295da32f4a6
main                       intentionally behind current V1 work
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

Specification 015 v0.1 / Checkpoint 147
    first recommendation/action-value contract frozen
    GENERIC vs SELECTIVE vs FULL_HORIZON
    provider-free implementation is the active next boundary
```

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
    -> real reasoning evidence [first bounded gate passed]
    -> recommendation / REQUIRED-BLOCKING / action evidence [active frozen slice]
```

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

### Dense semantic comparator

```text
docs/research/017_exact_semantic_retrieval_comparator_selection.md
docs/specifications/010_v1_exact_semantic_retrieval_comparator.md
docs/checkpoints/137_dense_semantic_retrieval_comparator_cross_platform_result_preserved.md
```

Dense retrieval recovered the lexical miss `class-imbalance` but lost `ecdf`; dense-only therefore did not replace lexical retrieval.

### Complementary hybrid comparator

```text
docs/research/018_dense_semantic_failure_complementarity_and_rrf_fusion_rationale.md
docs/specifications/011_v1_rrf_hybrid_retrieval_comparator.md
docs/checkpoints/139_rrf_hybrid_retrieval_cross_platform_gate_passed.md
experiments/retrieval/V1_RRF_HYBRID_RETRIEVAL_RESULT.md
```

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

Across the four frozen cases:

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

Frozen live source:

```text
3592cc3bd91e0aae7e5c667fa0c762ae4acd5395
V1 reasoning context value live / run 32635061634 / successful attempt 2
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

Context-expansion diagnostic:

```text
SELECTIVE unexpected basis mean      0.000000
FULL_HORIZON unexpected basis mean   1.666667
```

This accepts the bounded selective-context + ADS-owned ReasoningRuntime seam. It does not select a final model/provider, universal context budget, general relevance mechanism, or recommendation/REQUIRED-BLOCKING policy.

## Active recommendation/action-value route

Frozen design sources:

```text
docs/research/022_first_recommendation_action_value_vertical_slice_design.md
docs/specifications/015_v1_recommendation_action_value_vertical_slice.md
tests/fixtures/reasoning/recommendation_action_v1.json
docs/checkpoints/147_first_recommendation_action_value_contract_frozen.md
```

Frozen conditions:

```text
GENERIC
    same project/task/action envelope, no reusable methodological assets

SELECTIVE
    accepted Specification 013 exact-revision context

FULL_HORIZON
    all ten exact current accepted Horizon revisions
```

Frozen benchmark dispositions:

```text
BLOCKING_REQUIRED
RECOMMENDED
DEFER
NOT_NOW
```

Frozen cases:

```text
RA-01 VALIDITY_GATE
RA-02 MODEL_CHOICE
RA-03 EVIDENCE_PLAN
RA-04 MISSINGNESS_IMBALANCE
```

Frozen plan:

```text
4 cases x 3 conditions x 3 repetitions
36 reasoner outputs
36 condition-blinded judge outputs
72 planned successful provider calls
maximum 90 attempts
```

Primary metrics are deterministic recommendation/action metrics; semantic judging is secondary. Promotion additionally requires at least one preregistered positive value signal. Otherwise a fully safe ceiling result is classified `SAFE_BUT_NOT_DIFFERENTIATED` rather than being overclaimed.

No provider-free implementation result or live result exists yet.

---

## Current exact continuation

```text
A. implement ADS-owned recommendation result/disposition types provider-free
B. implement exact deterministic evaluator
C. implement GENERIC / SELECTIVE / FULL_HORIZON condition construction
D. add deterministic reasoner/judge plans and fake-runtime coverage
E. add ordinary Ubuntu/Windows provider-free workflow coverage
F. validate the exact implementation head
G. only then establish the explicit secret-gated live execution boundary
```

Do not make a live Specification 015 call before the frozen provider-free implementation is validated. Do not return to retrieval/reranking/vector work without a measured downstream reason.

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
```
