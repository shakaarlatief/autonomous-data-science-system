# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources but does not replace them.  
**Last reviewed:** 2026-08-23  
**Current checkpoint:** 156  
**Active development branch:** `v1-recommendation-action-value-relation-backed`  
**Active PR:** #16 -> `v1-frontend-spike`  
**Promoted V1 integration branch:** `v1-frontend-spike` at Specification 016 promotion merge `6bda0c1efcf078476859b2c2c64fb0586964899d`

## Start here

```text
README.md
    project overview and active track

docs/CURRENT_STATE.md
    present boundary and exact next action

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

Specification 015 / Checkpoints 147-150
    first recommendation/action-value experiment
    frozen live outcome FAIL

Checkpoint 151 / PR #14
    negative evidence preserved without adopting failed implementation

Specification 016 / Checkpoints 152-155
    dependency-backed disposition construct frozen, implemented, run, and supported

Specification 017 / Checkpoint 156 [active]
    second recommendation/action-value contract frozen
    relation-backed sequencing truth
    provider-free implementation next
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

### Methodological navigation/reusable knowledge

```text
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
```

Navigation sequence:

```text
KNOWN -> APPLICABLE -> RELEVANT -> RECOMMENDED -> REQUIRED / BLOCKING
```

Executable path validated through real reasoning:

```text
knowledge universe
    -> retrieval
    -> explained MethodologicalHorizon
    -> applicability / missing context
    -> bounded relevance selection
    -> exact selective MethodologicalContextPack
    -> ADS-owned ReasoningRuntime
    -> measured reasoning
```

Recommendation/action value beyond a strong generic reasoner remains unresolved and is the active empirical boundary.

---

## Persistence, interchange, and runtime

```text
D-028 + docs/specifications/001_v1_sqlite_technical_architecture.md
D-029 + docs/specifications/002_v1_persistence_tooling_standard.md
D-030 + docs/specifications/003_v1_python_project_and_dependency_tooling.md
D-031 + docs/specifications/004_v1_reusable_knowledge_interchange.md
D-032 + docs/specifications/005_v1_agent_runtime_and_interoperability_bakeoff.md
```

Governed knowledge round-trip closure:

```text
experiments/architecture_spikes/V1_KNOWLEDGE_ROUNDTRIP_RESULT.md
docs/checkpoints/127_governed_knowledge_roundtrip_closed_across_sqlite_and_postgresql.md
```

Initial runtime selection:

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

The Cockpit is the promoted primary immersive active-work model. Final frontend/chart/canvas choices and production backend/API architecture remain open.

---

## Retrieval -> Horizon route

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

### Dense complementarity

```text
docs/research/017_exact_semantic_retrieval_comparator_selection.md
docs/specifications/010_v1_exact_semantic_retrieval_comparator.md
docs/checkpoints/137_dense_semantic_retrieval_comparator_cross_platform_result_preserved.md
```

Dense recovered `class-imbalance` but lost `ecdf`, so dense-only did not replace lexical retrieval.

### Hybrid comparator

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

This remains complementarity evidence, not permanent vector-stack selection.

### Explained Horizon

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

## Selective context route

```text
docs/research/020_first_horizon_relevance_and_selective_context_gate_design.md
docs/specifications/013_v1_horizon_relevance_and_selective_context.md
docs/checkpoints/142_relevance_and_selective_context_contract_frozen.md
docs/checkpoints/143_selective_methodological_context_gate_passed_and_promotion_authorized.md
experiments/retrieval/V1_SELECTIVE_CONTEXT_RESULT.md
```

On the ten-asset Horizon, the four frozen cases selected only 2-3 exact revisions with full required stable-key and exact-revision coverage and no unexplained omissions.

PR #11 promoted merge:

```text
fd33184fbff588c6737d77af751bc5def0e31954
```

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

## Failed first recommendation/action route

Frozen design/result:

```text
docs/research/022_first_recommendation_action_value_vertical_slice_design.md
docs/specifications/015_v1_recommendation_action_value_vertical_slice.md
tests/fixtures/reasoning/recommendation_action_v1.json
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

Only `RA-G05` failed, concentrated on two expected `DEFER` versus observed `NOT_NOW` expansion actions in RA-02. The result remains immutable.

Failure preservation:

```text
docs/checkpoints/151_specification_015_failure_preservation_only_boundary_green.md
PR #14 merged at 10aa3f59bedc5ee45a38f0ae05c68da901d9adff
PR #13 closed without merge
```

---

## Supported disposition-semantics route

Frozen design and implementation:

```text
docs/research/023_defer_not_now_disposition_semantics_failure_attribution_design.md
docs/specifications/016_v1_disposition_semantics_failure_attribution_diagnostic.md
tests/fixtures/reasoning/disposition_semantics_v1.json
docs/checkpoints/152_disposition_semantics_failure_attribution_contract_frozen.md
docs/checkpoints/153_disposition_semantics_provider_free_gate_cross_platform_passed.md
docs/checkpoints/154_specification_016_live_boundary_frozen.md
```

Live result:

```text
frozen source head                    7db27fd35151c10cdb3562cdf4410fb8f4b09e8b
workflow run                          32652636943
reasoner outputs                      36 / 36
provider attempts                     36 / 45
retries                               0
aggregate exact disposition accuracy  1.000000
DEFER trigger-pointer accuracy        1.000000
NOT_NOW null-pointer correctness      1.000000
outcome                               DISPOSITION_BOUNDARY_SUPPORTED
```

Stable result route:

```text
docs/checkpoints/155_disposition_semantics_live_gate_supported.md
experiments/disposition_semantics/V1_DISPOSITION_SEMANTICS_RESULT.md
experiments/disposition_semantics/results/spec016-live-20260823-run-32652636943/
```

Promoted merge:

```text
6bda0c1efcf078476859b2c2c64fb0586964899d
```

Supported bounded constraint:

```text
DEFER-like sequencing requires a concrete represented activating dependency/trigger
if deterministic distinction from NOT_NOW-like absence of current justification is expected.
```

This is not yet a production enum or complete Foundation 018 relation schema.

---

## Active relation-backed recommendation/action-value route

Frozen sources:

```text
docs/research/024_relation_backed_recommendation_action_value_design.md
docs/specifications/017_v1_relation_backed_recommendation_action_value_vertical_slice.md
tests/fixtures/reasoning/relation_backed_recommendation_action_v1.json
docs/checkpoints/156_relation_backed_recommendation_action_value_contract_frozen.md
```

Active PR:

```text
#16 -> v1-frontend-spike
```

Conditions:

```text
GENERIC
SELECTIVE
FULL_HORIZON
```

Cases:

```text
RB-01  VALIDITY_GATE_AND_SEQUENCE
RB-02  COMPACT_MODEL_SHORTLIST_AND_TUNING_SEQUENCE
RB-03  DISTRIBUTION_EVIDENCE_BEFORE_TRANSFORMATION
RB-04  MISSINGNESS_IMBALANCE_DECISION_SEQUENCE
```

Relation-backed action result:

```text
action_id
    + disposition
    + defer_until_id
    + rationale
```

Frozen pointer invariant:

```text
DEFER -> exact supplied unresolved activating trigger
non-DEFER -> null pointer
```

Frozen outcomes:

```text
PROMOTE_RELATION_BACKED_RECOMMENDATION_SEAM
SAFE_BUT_NOT_DIFFERENTIATED
FAIL
```

Call plan:

```text
36 reasoner outputs
36 blinded judge outputs
72 planned successful provider calls
90 maximum attempts
seed 2026082303
```

At Checkpoint 156:

```text
implementation     not started
provider-free gate not run
live calls         0
```

---

## Current exact continuation

```text
A. implement relation-backed result/validator
B. implement frozen three-condition context construction
C. implement deterministic action/scope/clarification/basis/pointer metrics
D. implement blinded judge contract
E. prove complete fake-runtime 36 + 36 shape
F. add real-persistence provider-free integration coverage
G. add ordinary Ubuntu/Windows CI without provider credentials
H. preserve exact green implementation head
I. only then expose/run a secret-gated live workflow
```

Do not alter or rescore Specifications 015 or 016. Do not change Specification 017's frozen fixture or gates in response to future live results. Do not return to retrieval/reranking/vector work without a measured downstream reason.

---

## Recent continuity checkpoints

```text
127  governed knowledge round-trip closed across SQLite/PostgreSQL
133  initial V1 reasoning runtime selected
135  lexical retrieval baseline passed
137  dense semantic comparator preserved
139  hybrid retrieval comparator passed
141  first explained MethodologicalHorizon passed
142  selective-context contract frozen
143  selective-context gate passed and promoted
144  reasoning-context-value contract frozen
145  provider-free reasoning-context implementation passed
146  real reasoning-context gate passed
147  recommendation/action contract frozen
148  recommendation/action provider-free gate passed
149  recommendation/action live boundary frozen
150  recommendation/action live gate failed
151  failed evidence preserved without implementation promotion
152  disposition-semantics diagnostic contract frozen
153  disposition-semantics provider-free gate passed cross-platform
154  Specification 016 live boundary frozen
155  dependency-backed disposition-semantics live gate supported
156  relation-backed recommendation/action-value contract frozen
```
