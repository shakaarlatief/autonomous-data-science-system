# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources but does not replace them.  
**Last reviewed:** 2026-08-22  
**Current checkpoint:** 144  
**Active development branch:** `v1-reasoning-context-value`  
**Promoted V1 integration branch:** `v1-frontend-spike` at `fd33184fbff588c6737d77af751bc5def0e31954`

## Start here

For a new session or quick reconstruction:

```text
README.md
    project-level overview and current stage

docs/CURRENT_STATE.md
    present state, active experiment, exact next step

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
active reasoning-context experiment branch = v1-reasoning-context-value
promoted V1 integration branch             = v1-frontend-spike
main intentionally trails current V1 work
```

The active branch starts exactly from the PR #11 promotion merge:

```text
fd33184fbff588c6737d77af751bc5def0e31954
```

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
    D-032 accepted after Specification 005 bakeoff
    OpenAI Agents SDK behind ADS-owned ReasoningRuntime
    Checkpoint 133

retrieval / MethodologicalHorizon
    Specification 009 benchmark decomposition
    Checkpoint 135 lexical PASS
    Checkpoint 137 dense-only comparator preserved
    Checkpoint 139 hybrid comparator PASS
    Specification 012 v1.0
    Checkpoint 141 explained MethodologicalHorizon PASS

selective methodological context
    Research 020
    Specification 013 v1.0
    Checkpoint 142 frozen contract
    Checkpoint 143 successful promotion
    V1_SELECTIVE_CONTEXT_RESULT.md

active next experiment
    Research 021
    Specification 014 v0.1 frozen
    context_value_v1.json frozen
    Checkpoint 144
    selective context vs compact full-Horizon reasoning control
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

Current executable path:

```text
large global knowledge universe
    -> retrieval
    -> bounded explained MethodologicalHorizon
    -> explicit applicability/context checks
    -> bounded task-specific relevance selection
    -> selective MethodologicalContextPack
    -> real model reasoning [active experiment]
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

---

## Selected V1 reasoning runtime

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
OpenAI Agents SDK
    selected initial V1 runtime infrastructure

direct model calls
    fallback/reference

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

Key promotion/polish checkpoints:

```text
docs/checkpoints/126_seventh_cockpit_review_validated_and_interaction_architecture_promoted.md
docs/checkpoints/130_post_promotion_cockpit_normal_window_and_pinch_polish_gate_passed.md
```

Final frontend stack promotion, chart library, canvas/gesture libraries, auto-layout, semantic zoom, minimap, final stage taxonomy, final URL contract, project-search backend, and final visual identity remain open.

---

## Retrieval and MethodologicalHorizon route

### Lexical baseline

```text
docs/research/016_production_retrieval_and_methodological_horizon_benchmark_design.md
docs/specifications/009_v1_retrieval_and_methodological_horizon_benchmark.md
docs/checkpoints/135_first_production_lexical_retrieval_baseline_cross_platform_passed.md
experiments/retrieval/V1_LEXICAL_RETRIEVAL_RESULT.md
```

### Dense complementarity

```text
docs/research/017_exact_semantic_retrieval_comparator_selection.md
docs/specifications/010_v1_exact_semantic_retrieval_comparator.md
docs/checkpoints/137_dense_semantic_retrieval_comparator_cross_platform_result_preserved.md
```

Dense recovers `class-imbalance` but misses lexical `ecdf`; dense-only does not replace lexical retrieval.

### Hybrid comparator

```text
docs/research/018_dense_semantic_failure_complementarity_and_rrf_fusion_rationale.md
docs/specifications/011_v1_rrf_hybrid_retrieval_comparator.md
docs/checkpoints/139_rrf_hybrid_retrieval_cross_platform_gate_passed.md
experiments/retrieval/V1_RRF_HYBRID_RETRIEVAL_RESULT.md
```

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

Observed wide-Horizon context ratios:

```text
RH-C01  0.20020477
RH-C02  0.16462054
RH-C03  0.34635417
RH-C04  0.28222057
```

Across all cases:

```text
required exact-revision coverage 1.00
irrelevant selected              0
unexplained omissions            0
```

PR #11 exact tested head:

```text
517a12d14b6bb639258931f5c3c451d35ccd7ec0
```

PR #11 promoted merge:

```text
fd33184fbff588c6737d77af751bc5def0e31954
```

---

## Active first reasoning-context-value vertical slice

Primary sources:

```text
docs/research/021_first_reasoning_context_value_vertical_slice_design.md
docs/specifications/014_v1_reasoning_context_value_vertical_slice.md
tests/fixtures/reasoning/context_value_v1.json
docs/checkpoints/144_first_reasoning_context_value_contract_frozen.md
```

Frozen conditions:

```text
SELECTIVE
    Specification 013 pack
    2-3 exact task-specific revisions

FULL_HORIZON
    all 10 included Horizon revisions
    same compact reasoning projection
```

Frozen reasoner:

```text
gpt-5.6-sol
OpenAI Agents SDK 0.19.4 behind ADS-owned ReasoningRuntime
reasoning effort medium
text verbosity low
no tools
no prior response state
```

Frozen judge:

```text
gpt-5.6-sol
reasoning effort high
condition-blinded
one judge call per reasoner output
```

Frozen live plan:

```text
4 cases
2 conditions
3 repetitions
24 reasoner outputs
24 judge outputs
48 planned successful provider calls
randomization seed 20260822
```

Quality preservation gates:

```text
aggregate selective >= full - 0.05
per-case selective >= full - 0.10
no reproducible selective-only critical-obligation regression
```

Provider-token gates:

```text
selective input tokens < full input tokens in every matched pair
per-case mean selective/full ratio <= 0.80
aggregate mean selective/full ratio <= 0.80
```

No live model call is allowed before the frozen contract/fixture/checkpoint exist. That prerequisite is now satisfied.

---

## Current exact priorities

```text
A. implement ADS-owned reasoning request/outcome/result types and ReasoningRuntime port
B. implement no-tool OpenAI Agents SDK adapter behind the port
C. implement SELECTIVE/FULL_HORIZON condition construction
D. implement deterministic frozen call plan and blinded judge contract
E. add fake-model unit/integration coverage
F. add secret-gated live workflow
G. validate exact implementation head on Ubuntu/Windows with no live API dependency
H. only then execute the frozen live 48-call plan
I. preserve complete result before any tuning
```

Do not change the model, thresholds, rubrics, call count, or context conditions after observing live outputs without first preserving the frozen result.

---

## Recent continuity checkpoints

```text
127  governed knowledge round-trip closed across SQLite/PostgreSQL
133  initial V1 reasoning runtime selected
135  first production lexical retrieval baseline PASS
137  dense semantic comparator preserved
139  hybrid retrieval comparator PASS
141  first explained MethodologicalHorizon PASS
142  relevance/selective-context contract frozen
143  selective-context gate passed and promoted
144  first reasoning-context-value contract frozen
```
