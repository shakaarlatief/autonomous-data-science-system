# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources but does not replace them.  
**Last reviewed:** 2026-08-22  
**Current checkpoint:** 133  
**Active development branch:** `v1-runtime-bakeoff` pending final CI/reconciliation and merge into `v1-frontend-spike`

## Start here

For a new session or quick reconstruction:

```text
README.md
    project-level overview and current stage

docs/CURRENT_STATE.md
    present state, active gates, exact next step

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
runtime selection/reconciliation = v1-runtime-bakeoff
preserved promoted V1/frontend boundary = v1-frontend-spike
main intentionally trails current V1 work
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
    OpenAI Agents SDK behind ADS-owned runtime port
    Checkpoint 133

immediate next methodological track
    production retrieval / MethodologicalHorizon
    Q-044 / Q-045
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

Professional workflow split:

```text
ADS         project/process control plane
VS Code     developer workbench
compute     execution plane
Git/GitHub  source/provenance/collaboration
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

Scaling path:

```text
large global knowledge universe
    -> project-specific retrieval/filtering
    -> bounded MethodologicalHorizon
    -> explicit applicability/context checks
    -> flexible relevance/prioritization reasoning
    -> selective task-specific LLM context
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

## Accepted V1 persistence, tooling and interchange

Primary decisions/specifications:

```text
D-028 + docs/specifications/001_v1_sqlite_technical_architecture.md
D-029 + docs/specifications/002_v1_persistence_tooling_standard.md
D-030 + docs/specifications/003_v1_python_project_and_dependency_tooling.md
D-031 + docs/specifications/004_v1_reusable_knowledge_interchange.md
```

Accepted direction:

```text
SQLite-centered local-first operational architecture
FTS5 rebuildable lexical index
rebuildable embeddings / initial exact semantic retrieval
application rule evaluator
selective context assembler

SQLAlchemy Core 2.0
Alembic 1.x
PostgreSQL portability rules

pyproject.toml
uv + committed uv.lock
uv_build
Python >=3.12

JSON
JSON Schema Draft 2020-12
semantic validation
deterministic normalization/serialization
```

Governed round-trip closure:

```text
experiments/architecture_spikes/V1_KNOWLEDGE_ROUNDTRIP_RESULT.md
docs/checkpoints/127_governed_knowledge_roundtrip_closed_across_sqlite_and_postgresql.md
```

Final run `32496856945` passed SQLite Ubuntu, SQLite Windows, PostgreSQL 18, and the Alembic revision-ID guard.

---

## Selected V1 reasoning runtime and closed bakeoff

Accepted decision:

```text
D-032
    OpenAI Agents SDK behind an ADS-owned ReasoningRuntime port
    validated starting package openai-agents==0.19.4
```

Executed evaluation contract:

```text
docs/specifications/005_v1_agent_runtime_and_interoperability_bakeoff.md
    completed v0.2
```

Core architecture boundary:

```text
ADS domain/project/methodological semantics
    owned by ADS

runtime framework / MCP / runtime checkpoint mechanics
    replaceable infrastructure
```

ADS-owned runtime provenance and side-effect authority remain independent of framework-native tracing/checkpoint semantics.

### Direct-call control

Evidence:

```text
experiments/runtime_bakeoff/DIRECT_CALL_CONTROL_RESULT.md
docs/checkpoints/129_direct_model_call_runtime_control_cross_platform_gate_passed.md
```

Run `32500521858`: Ubuntu/Windows PASS.

Interpretation:

```text
viable minimum-dependency fallback/reference
maximum explicit control
more ADS-owned generic orchestration machinery
```

### OpenAI Agents SDK 0.19.4

Evidence:

```text
experiments/runtime_bakeoff/candidates/openai_agents/COMPLETE_RESULT.md
docs/research/011_openai_agents_0_19_4_released_api_compatibility_findings.md
docs/research/013_openai_agents_complete_candidate_evidence_and_direct_call_comparison.md
docs/checkpoints/131_openai_agents_complete_runtime_candidate_cross_platform_gate_passed.md
```

Validation:

```text
run 32555526773
AR-01 through AR-12 PASS
Ubuntu PASS
Windows PASS
```

Important result:

```text
native model/tool loop and schema dispatch
approval interruption
serializable/restorable RunState
real stdio MCP
function-tool timeout
application cancellation
controlled retry
structured output
ADS-normalized observability
provider-free deterministic testing through public Model interface
```

This is the selected initial V1 runtime infrastructure through D-032.

### LangGraph 1.2.10 durability comparator

Evidence:

```text
experiments/runtime_bakeoff/candidates/langgraph_runtime/COMPLETE_RESULT.md
docs/research/014_langgraph_1_2_10_released_durability_comparator_audit.md
docs/checkpoints/132_langgraph_durability_comparator_cross_platform_gate_passed.md
```

Validated package set:

```text
langgraph==1.2.10
langgraph-checkpoint-sqlite==3.1.1
langchain-mcp-adapters==0.3.1
mcp==1.28.1
```

Run `32556382248`: Ubuntu/Windows PASS, 9 comparator tests on each platform.

Interpretation:

```text
stronger explicit persisted execution/checkpoint durability
completed prior read nodes preserved on tested resume path
interrupt node restarts from beginning on resume
ADS ProposalLedger still required for authoritative exactly-once meaning
larger dependency/operational/topology surface
released MCP adapter required explicit MCP v1 compatibility pin
```

LangGraph is not selected now. It remains a future durability escalation path.

### Three-way comparison and stop rule

Primary source:

```text
docs/research/015_langgraph_complete_candidate_three_way_runtime_comparison_and_stop_rule.md
```

Promotion checkpoint:

```text
docs/checkpoints/133_v1_reasoning_runtime_selected_and_bakeoff_closed.md
```

Microsoft Agent Framework and Google ADK 2.0 are not implemented in the current bakeoff because no preserved current differentiator is likely to overturn D-032. Reopen only if a new first-order requirement makes them decision-relevant.

No final LLM provider/model or multi-agent architecture is selected.

---

## Professional frontend and Project Cockpit

Primary foundation/specifications:

```text
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
docs/specifications/006_v1_frontend_architecture_and_visual_spike.md
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
```

Promotion/history:

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

Current promoted interaction model:

```text
Project Cockpit as primary immersive active-work environment
meaningful work-unit projection
spatial focus into real specialist workspaces
FiniteNavigableGridWorld != SemanticProjectPlane
2D navigation/recovery
bounded geometric zoom/native pinch
viewport-aware stage orientation
scalable Jump/search
compact/foldable HUD/tool rail
collision-safe floating surfaces
true fullscreen
URL-addressable focus
keyboard/reduced-motion support
world-owned ambient depth
```

The subsequent human retest accepted the Checkpoint-130 normal-window Jump repair and faster pinch as good enough to continue. The tiny occasional pinch hitch is deferred polish.

Exact gesture constants, final layout/stage taxonomy, graph/canvas library, auto-layout, semantic zoom, minimap, production project-search backend, final URL contract and visual identity remain deliberately unfrozen.

---

## Immediate active track: production retrieval / MethodologicalHorizon

Primary open questions:

```text
docs/OPEN_QUESTIONS.md
    Q-044
    Q-045
```

Required evaluation:

```text
retrieval-quality fixtures
production lexical retrieval
semantic retrieval candidate evaluation
lexical/semantic fusion only if justified
ranking and omission-quality evaluation
first real MethodologicalHorizon construction
selective LLM context assembly
recommendation quality separated from knowledge/retrieval coverage
```

Failure categories should distinguish:

```text
knowledge absent from catalog
known but not retrieved
retrieved but judged inapplicable
applicable but ranked too low
recommended but skipped
recommended incorrectly
required concern omitted
```

Do not select embedding/reranking/vector infrastructure from intuition.

---

## Current exact priorities

```text
A. finish runtime-branch reconciliation, CI and merge into v1-frontend-spike
B. start production retrieval / MethodologicalHorizon benchmark
C. integrate D-032 into production only when the first real reasoning vertical slice needs the runtime port
D. continue future Cockpit capability/product work on top of Specification 008
```

---

## Recent continuity checkpoints

```text
114  first production V1 persistence vertical slice passed
115  reusable knowledge interchange validated
116  agentic ecosystem audit + frontend track started
117  unified Cockpit workspace direction confirmed
118  first Cockpit automated gate passed
119  spatial scalability + fullscreen requirements confirmed
120  unexpected-session continuity reconciliation completed
121  immersive-scale Cockpit automated gate passed
122  zoom/canvas-dominance/scalable-navigation gate passed
123  balanced spatial world/orientation gate passed
124  continuous grid world/stage-ruler/vertical-tool-rail gate passed
125  ambient/pinch/ruler/collision repairs validated
126  seventh Cockpit review + interaction architecture promotion
127  governed knowledge round-trip closed across SQLite/PostgreSQL
128  runtime-bakeoff preimplementation evidence refreshed
129  direct model-call runtime control cross-platform PASS
130  post-promotion Cockpit normal-window/pinch polish PASS
131  OpenAI Agents SDK 0.19.4 complete candidate cross-platform PASS
132  LangGraph 1.2.10 durability comparator cross-platform PASS
133  initial V1 reasoning runtime selected; Specification 005 closed
```