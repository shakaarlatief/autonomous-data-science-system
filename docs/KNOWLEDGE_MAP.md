# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources but does not replace them.  
**Last reviewed:** 2026-08-23  
**Current checkpoint:** 158  
**Active development branch:** `v1-recommendation-action-value-relation-backed`  
**Active PR:** #16 -> `v1-frontend-spike`  
**Promoted V1 integration branch:** `v1-frontend-spike` at Specification 016 promotion merge `6bda0c1efcf078476859b2c2c64fb0586964899d`

## Start here

```text
README.md
    project overview and active track

docs/CURRENT_STATE.md
    present boundary and exact continuation

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
    development/checkpoint/promotion method

docs/CONTINUITY.md
    continuation and unexpected-boundary recovery

docs/MAJOR_CHANGES.md
    selective structural history
```

Current branch relationship:

```text
promoted integration head      6bda0c1efcf078476859b2c2c64fb0586964899d
active experiment branch       v1-recommendation-action-value-relation-backed
active PR                      #16 -> v1-frontend-spike
Specification 015 failed PR    #13 closed without merge
failure preservation PR        #14 merged
Specification 016 PR           #15 merged
main                           intentionally behind active V1 work except dispatcher exposure
```

---

## Current project stage

Prototype V0 final classification:

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
    project object/state model
    methodological navigation
    reusable methodological knowledge

D-028 through D-031 / Checkpoint 127
    local-first persistence and governed knowledge interchange

Specification 008 / Checkpoints 126,130
    promoted Project Cockpit interaction architecture

D-032 / Checkpoint 133
    OpenAI Agents SDK behind ADS-owned ReasoningRuntime

Checkpoints 135 -> 137 -> 139 -> 141
    lexical retrieval -> dense complementarity -> hybrid comparator -> explained Horizon

Specification 013 / Checkpoint 143
    accepted selective exact-revision MethodologicalContextPack

Specification 014 / Checkpoint 146
    first real-model selective-context value gate PASS

Specification 015 / Checkpoints 147-151
    first recommendation/action-value experiment FAIL
    failed implementation rejected
    negative evidence preserved

Specification 016 / Checkpoints 152-155
    dependency-backed DEFER-vs-NOT_NOW diagnostic
    DISPOSITION_BOUNDARY_SUPPORTED
    promoted through PR #15

Specification 017 / Checkpoint 156
    second relation-backed recommendation/action-value contract frozen

Checkpoint 157
    complete provider-free Specification 017 implementation passed Ubuntu + Windows

Checkpoint 158 [active]
    explicit manual Specification 017 live boundary frozen
    final reconciled provider-free head validation pending
```

---

## Core architecture routes

### Product/object/system boundary

```text
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
```

Key distinctions:

```text
OBJECTS / RELATIONS / EVENTS / VIEWS
Investigation != Run
Evidence != Finding
Finding != Claim
Claim != Decision
current state != event history
persisted object != derived recommendation
```

### Methodological navigation and reusable knowledge

```text
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
```

Navigation sequence:

```text
KNOWN -> APPLICABLE -> RELEVANT -> RECOMMENDED -> REQUIRED / BLOCKING
```

Current executable chain:

```text
knowledge universe
    -> retrieval
    -> explained MethodologicalHorizon
    -> applicability / missing context
    -> bounded relevance selection
    -> exact selective MethodologicalContextPack
    -> ADS-owned ReasoningRuntime
    -> measured real reasoning
    -> relation-backed recommendation/action evaluation [active]
```

---

## Persistence, interchange, and runtime

```text
D-028 + docs/specifications/001_v1_sqlite_technical_architecture.md
D-029 + docs/specifications/002_v1_persistence_tooling_standard.md
D-030 + docs/specifications/003_v1_python_project_and_dependency_tooling.md
D-031 + docs/specifications/004_v1_reusable_knowledge_interchange.md
D-032 + docs/specifications/005_v1_agent_runtime_and_interoperability_bakeoff.md
```

Governed round-trip closure:

```text
experiments/architecture_spikes/V1_KNOWLEDGE_ROUNDTRIP_RESULT.md
docs/checkpoints/127_governed_knowledge_roundtrip_closed_across_sqlite_and_postgresql.md
```

Initial reasoning runtime:

```text
OpenAI Agents SDK behind ADS-owned ReasoningRuntime
validated starting package openai-agents==0.19.4

direct model calls   fallback/reference
LangGraph            possible future durability escalation
```

No final model/provider or multi-agent architecture is selected.

---

## Project Cockpit route

Promoted interaction contract:

```text
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
```

Key checkpoints:

```text
docs/checkpoints/126_seventh_cockpit_review_validated_and_interaction_architecture_promoted.md
docs/checkpoints/130_post_promotion_cockpit_normal_window_and_pinch_polish_gate_passed.md
```

The Cockpit is the promoted primary immersive active-work model. It is intended to expose project navigation, chat/reasoning, analytical workspaces, evidence, recommendations, decisions, and state through one professional interface. Final frontend/chart/canvas choices and production backend/API wiring remain open.

---

## Retrieval -> Horizon -> selective context route

Lexical baseline:

```text
docs/specifications/009_v1_retrieval_and_methodological_horizon_benchmark.md
docs/checkpoints/135_first_production_lexical_retrieval_baseline_cross_platform_passed.md
experiments/retrieval/V1_LEXICAL_RETRIEVAL_RESULT.md
```

Dense complementarity:

```text
docs/specifications/010_v1_exact_semantic_retrieval_comparator.md
docs/checkpoints/137_dense_semantic_retrieval_comparator_cross_platform_result_preserved.md
```

Hybrid comparator:

```text
docs/specifications/011_v1_rrf_hybrid_retrieval_comparator.md
docs/checkpoints/139_rrf_hybrid_retrieval_cross_platform_gate_passed.md
experiments/retrieval/V1_RRF_HYBRID_RETRIEVAL_RESULT.md
```

Explained Horizon:

```text
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

Selective context:

```text
docs/research/020_first_horizon_relevance_and_selective_context_gate_design.md
docs/specifications/013_v1_horizon_relevance_and_selective_context.md
docs/checkpoints/143_selective_methodological_context_gate_passed_and_promotion_authorized.md
experiments/retrieval/V1_SELECTIVE_CONTEXT_RESULT.md
```

On the frozen ten-asset Horizon, SELECTIVE retained every required exact revision while reducing methodology-only context by roughly 65% to 84%.

---

## Accepted real reasoning-context route

```text
docs/research/021_first_reasoning_context_value_vertical_slice_design.md
docs/specifications/014_v1_reasoning_context_value_vertical_slice.md
docs/checkpoints/144_first_reasoning_context_value_contract_frozen.md
docs/checkpoints/145_reasoning_context_value_implementation_gate_cross_platform_passed.md
docs/checkpoints/146_first_real_reasoning_context_value_gate_passed.md
experiments/reasoning_context_value/V1_REASONING_CONTEXT_VALUE_RESULT.md
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

PR #12 promoted merge:

```text
bd7d1ec5cabc80d39e005d0a12c11295da32f4a6
```

---

## First recommendation/action route: failed but preserved

Frozen design/result:

```text
docs/research/022_first_recommendation_action_value_vertical_slice_design.md
docs/specifications/015_v1_recommendation_action_value_vertical_slice.md
docs/checkpoints/147_first_recommendation_action_value_contract_frozen.md
docs/checkpoints/148_recommendation_action_provider_free_gate_cross_platform_passed.md
docs/checkpoints/149_specification_015_live_boundary_frozen.md
docs/checkpoints/150_specification_015_live_result_failed_exact_disposition_gate.md
experiments/recommendation_action_value/V1_RECOMMENDATION_ACTION_VALUE_RESULT.md
```

Live result:

```text
run                 32642733784
reasoner outputs    36 / 36
judge outputs       36 / 36
retries             0
advancement         FAIL
```

The only failed named gate was a shared `DEFER` versus `NOT_NOW` exact-label disagreement on two noncritical RA-02 actions. The failed implementation PR #13 was closed without merge; negative evidence was preserved through PR #14 / Checkpoint 151.

---

## Dependency-backed disposition route

```text
docs/research/023_defer_not_now_disposition_semantics_failure_attribution_design.md
docs/specifications/016_v1_disposition_semantics_failure_attribution_diagnostic.md
tests/fixtures/reasoning/disposition_semantics_v1.json
docs/checkpoints/152_disposition_semantics_failure_attribution_contract_frozen.md
docs/checkpoints/153_disposition_semantics_provider_free_gate_cross_platform_passed.md
docs/checkpoints/154_specification_016_live_boundary_frozen.md
docs/checkpoints/155_disposition_semantics_live_gate_supported.md
experiments/disposition_semantics/V1_DISPOSITION_SEMANTICS_RESULT.md
```

Live result:

```text
run                               32652636943
36 / 36 exact dispositions        correct
18 / 18 expected-DEFER pointers   exact
18 / 18 expected-NOT_NOW pointers null
outcome                           DISPOSITION_BOUNDARY_SUPPORTED
```

Promoted merge:

```text
6bda0c1efcf078476859b2c2c64fb0586964899d
```

Supported constraint: DEFER-like sequencing should carry a concrete activating dependency/trigger when deterministic separation from NOT_NOW is required. Production enums and persistence schema remain open.

---

## Active relation-backed recommendation/action route

Preregistered design:

```text
docs/research/024_relation_backed_recommendation_action_value_design.md
docs/specifications/017_v1_relation_backed_recommendation_action_value_vertical_slice.md
tests/fixtures/reasoning/relation_backed_recommendation_action_v1.json
docs/checkpoints/156_relation_backed_recommendation_action_value_contract_frozen.md
```

Provider-free implementation:

```text
experiments/relation_backed_recommendation_action_value/environment.py
experiments/relation_backed_recommendation_action_value/harness.py
experiments/relation_backed_recommendation_action_value/judge.py
experiments/relation_backed_recommendation_action_value/runner.py
tests/unit/test_relation_backed_recommendation_action_harness.py
tests/integration/test_relation_backed_recommendation_action_value_vertical_slice.py
.github/workflows/v1-relation-backed-recommendation-action-value.yml
```

Cross-platform implementation gate:

```text
docs/checkpoints/157_relation_backed_recommendation_action_provider_free_gate_cross_platform_passed.md
validated head    07da2a091b5686b0378c7f8114495fe1d0b29c32
workflow          32655457836
Ubuntu targeted   13 passed
Windows targeted  13 passed
Ubuntu full       71 passed, 2 skipped
Windows full      71 passed, 2 skipped
```

The complete fake experiment executes all 36 reasoner + 36 judge outputs and correctly classifies a perfect three-condition ceiling as `SAFE_BUT_NOT_DIFFERENTIATED`.

Frozen live boundary:

```text
docs/checkpoints/158_specification_017_live_boundary_frozen.md
.github/workflows/v1-relation-backed-recommendation-action-value-live.yml
manual confirmation  RUN_SPEC_017_FROZEN
required branch       v1-recommendation-action-value-relation-backed
```

No Specification 017 live provider call has occurred.

---

## Current exact continuation

```text
A. validate the exact final reconciled PR #16 head under:
       V1 relation-backed recommendation action value
       V1 reasoning context value
       V1 disposition semantics diagnostic
       Checkpoint metadata
B. if that exact head is green, make no further experiment-branch commits
C. copy only the identical Specification 017 live workflow to main
D. manually dispatch it from v1-recommendation-action-value-relation-backed
E. enter RUN_SPEC_017_FROZEN
F. preserve the complete artifact before interpretation
```

Do not alter Specifications 015 or 016. Do not change Specification 017's fixture, definitions, thresholds, value signals, model treatment, repetitions, randomization, or retry rules after live results are observed.

---

## Recent continuity checkpoints

```text
127  governed knowledge round-trip closed across SQLite/PostgreSQL
133  initial V1 reasoning runtime selected
135  lexical retrieval baseline passed
137  dense semantic comparator preserved
139  hybrid retrieval comparator passed
141  first explained MethodologicalHorizon passed
143  selective-context gate passed and promoted
146  real reasoning-context gate passed
150  first recommendation/action live gate failed
151  failed evidence preserved without implementation promotion
155  dependency-backed disposition live gate supported
156  relation-backed recommendation/action contract frozen
157  relation-backed recommendation/action provider-free gate passed
158  Specification 017 live boundary frozen
```
