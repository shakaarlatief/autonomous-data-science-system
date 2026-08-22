# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources but does not replace them.  
**Last reviewed:** 2026-08-22  
**Current checkpoint:** 145  
**Active development branch:** `v1-reasoning-context-value`  
**Active promotion PR:** #12 into `v1-frontend-spike`  
**Promoted V1 integration branch:** `v1-frontend-spike` at PR #11 merge commit `fd33184fbff588c6737d77af751bc5def0e31954`

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
active experiment branch  v1-reasoning-context-value
active PR                  #12 -> v1-frontend-spike
promoted integration head  fd33184fbff588c6737d77af751bc5def0e31954
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
    object/state model
    methodological navigation
    reusable knowledge architecture

D-028 through D-031 / Checkpoint 127
    local-first persistence
    governed reusable-knowledge interchange

Specification 008 / Checkpoints 126 and 130
    Project Cockpit interaction architecture

D-032 / Checkpoint 133
    OpenAI Agents SDK behind ADS-owned ReasoningRuntime

Checkpoints 135 -> 137 -> 139 -> 141
    lexical retrieval
    dense semantic comparator
    complementary hybrid comparator
    first explained MethodologicalHorizon

Specification 013 v1.0 / Checkpoint 143
    first accepted selective MethodologicalContextPack seam

Specification 014 v0.1 / Checkpoints 144-145
    first selective-context versus compact full-Horizon real-reasoning experiment
    provider-free implementation and reconciliation complete
    live experiment is the next substantive action
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
    -> real reasoning evidence [active]
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

## Active reasoning-context-value vertical slice

Frozen design sources:

```text
docs/research/021_first_reasoning_context_value_vertical_slice_design.md
docs/specifications/014_v1_reasoning_context_value_vertical_slice.md
tests/fixtures/reasoning/context_value_v1.json
docs/checkpoints/144_first_reasoning_context_value_contract_frozen.md
```

Provider-free implementation checkpoint:

```text
docs/checkpoints/145_reasoning_context_value_implementation_gate_cross_platform_passed.md
```

Production-facing implementation:

```text
src/ads_system/application/reasoning.py
src/ads_system/application/ports.py
src/ads_system/infrastructure/runtime/openai_agents.py
```

Experiment implementation:

```text
experiments/reasoning_context_value/environment.py
experiments/reasoning_context_value/harness.py
experiments/reasoning_context_value/judge.py
experiments/reasoning_context_value/runner.py
```

Frozen conditions:

```text
SELECTIVE
    Specification 013 pack
    2-3 exact task-specific revisions

FULL_HORIZON
    all 10 exact Horizon revisions
    same compact reasoning projection
```

Frozen live plan:

```text
4 cases
2 conditions
3 repetitions
24 reasoner outputs
24 condition-blinded judge outputs
48 planned successful provider calls
randomization seed 20260822
maximum provider attempts 60
```

Frozen quality gates:

```text
aggregate selective >= full - 0.05
per-case selective >= full - 0.10
no reproducible selective-only critical-obligation regression
```

Frozen provider-token gates:

```text
selective input tokens < full input tokens in every matched pair
per-case mean selective/full <= 0.80
aggregate mean selective/full <= 0.80
```

Provider-free implementation evidence:

```text
first implementation head  aadf425fdb24db2512e2171f4a99be3c87d8cb80
workflow                   V1 reasoning context value / 32568052820
Ubuntu                     PASS
Windows                    PASS
```

Fully reconciled pre-live head before the final routing-only updates:

```text
23cf0c09fadbe11330edfed19c10e7e194f5be18
```

It passed Checkpoint metadata, the reasoning-context workflow on Ubuntu and Windows, selective-context regression, first-Horizon-builder regression, and MethodologicalHorizon regression.

This is infrastructure evidence only. No live Specification 014 reasoner/judge call has occurred yet.

---

## Current exact continuation

Pre-live implementation, PR reconciliation, and canonical routing reconciliation are complete.

The only remaining precondition is that the **current** documentation-adjusted PR head remains green under the same provider-free gates. Once confirmed, the next substantive action is:

```text
.github/workflows/v1-reasoning-context-value-live.yml
branch: v1-reasoning-context-value
confirmation: RUN_SPEC_014_FROZEN
secret: OPENAI_API_KEY
```

After the run:

```text
1. inspect the complete uploaded workflow artifact
2. preserve raw and aggregate result before any tuning
3. create the live-result checkpoint
4. apply Specification 014's frozen advancement rule
5. only then decide promotion, repair, or the next experiment
```

Do not merge PR #12 on provider-free evidence alone. Do not change the frozen model, prompts, fixture, semantic rubric, thresholds, repetitions, retry policy, or context construction before the live result is preserved.

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
```