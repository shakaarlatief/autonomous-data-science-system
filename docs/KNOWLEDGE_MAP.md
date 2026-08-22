# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources but does not replace them.  
**Last reviewed:** 2026-08-22  
**Current checkpoint:** 131  
**Active development branch:** `v1-runtime-bakeoff`

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
active runtime/integration work = v1-runtime-bakeoff
preserved promoted frontend boundary = v1-frontend-spike
main intentionally trails current V1 work
```

---

## Current project stage

Prototype V0 is complete with final classification:

> **STRONG FALSIFICATION OF THE CURRENT P0 DESIGN**

Current bounded V1 tracks:

```text
methodological knowledge
governed persistence/interchange
retrieval / MethodologicalHorizon construction
agent/runtime infrastructure
professional frontend / Project Cockpit
```

Major current boundaries:

```text
Project Cockpit interaction architecture
    promoted through Specification 008 / Checkpoint 126
    post-promotion normal-window/pinch polish validated in Checkpoint 130

governed reusable-knowledge persistence/interchange
    closed across SQLite/Linux, SQLite/Windows, PostgreSQL 18
    Checkpoint 127

runtime bakeoff
    direct-call control viable, Checkpoint 129
    OpenAI Agents SDK 0.19.4 complete candidate viable, Checkpoint 131
    LangGraph durability comparator next
    no runtime selected
```

The other highest-value active V1 track is production retrieval / MethodologicalHorizon evaluation.

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

Current accepted direction:

```text
SQLite-centered local-first operational architecture
FTS5 rebuildable lexical index
rebuildable embeddings / initial exact semantic retrieval
application rule evaluator
selective context assembler

SQLAlchemy Core 2.0
Alembic 1.x
PostgreSQL portability rules
Alembic revision IDs <= 32 chars while default version table remains

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

## Runtime bakeoff: current active track

Evaluation contract:

```text
docs/specifications/005_v1_agent_runtime_and_interoperability_bakeoff.md
```

Ecosystem/released-API research:

```text
docs/research/001_2026_agentic_ecosystem_and_integration_architecture_audit.md
docs/research/010_2026_runtime_bakeoff_preimplementation_refresh.md
docs/research/011_openai_agents_0_19_4_released_api_compatibility_findings.md
docs/research/013_openai_agents_complete_candidate_evidence_and_direct_call_comparison.md
```

Durable runtime boundary:

```text
ADS domain/project/methodological semantics
    owned by ADS

runtime framework / MCP / runtime checkpoint mechanics
    replaceable infrastructure
```

### ADS-owned framework-neutral harness

Location:

```text
experiments/runtime_bakeoff/
```

Owns:

```text
representative workload
ProjectContextSnapshot
MethodologicalContextPack
RuntimeWorkloadInput
RuntimeRecommendation
RuntimeInterrupt
RuntimeResumeToken
RuntimeTrace
RuntimeOutcome
context-pack digest and exact knowledge revisions
ProposalLedger authoritative side-effect idempotency
```

### Direct-call control

Evidence:

```text
experiments/runtime_bakeoff/DIRECT_CALL_CONTROL_RESULT.md
docs/checkpoints/129_direct_model_call_runtime_control_cross_platform_gate_passed.md
```

Run `32500521858`: Ubuntu/Windows PASS. Direct calls are a viable final outcome, with the cost of significant explicit custom orchestration machinery.

### OpenAI Agents SDK 0.19.4

Evidence:

```text
experiments/runtime_bakeoff/candidates/openai_agents/CORE_RESULT.md
experiments/runtime_bakeoff/candidates/openai_agents/COMPLETE_RESULT.md
docs/research/011_openai_agents_0_19_4_released_api_compatibility_findings.md
docs/research/013_openai_agents_complete_candidate_evidence_and_direct_call_comparison.md
docs/checkpoints/131_openai_agents_complete_runtime_candidate_cross_platform_gate_passed.md
```

Complete validation:

```text
validated implementation 08c1c41246d8ece21e443d938ed477176505e40f
run 32555526773
AR-01 through AR-12 PASS
Ubuntu PASS
Windows PASS
control/full Python suite PASS
```

Important evidence:

```text
real stdio MCP integration
native approval interruption
serialized/restored RunState
application cancellation
function-tool timeout
controlled retry
ADS ProposalLedger idempotency under repeated resume
ADS-normalized observability
provider-free deterministic Model fake
```

OpenAI is technically viable but not selected.

### Next comparator: LangGraph

Exact next work:

```text
audit currently released package/API
implement isolated candidate under experiments/runtime_bakeoff/candidates/langgraph/
use same workload and ADS authority boundary
stress durable checkpoint/process-boundary resume
stress interrupt/node restart/replay semantics
protect side effects through ADS ProposalLedger
complete AR-01..AR-12 if viable
compare direct calls vs OpenAI vs LangGraph
```

Microsoft Agent Framework and Google ADK 2.0 remain conditional candidates only if they could plausibly change the decision after the primary comparison.

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

Exact gesture constants, final layout/stage taxonomy, graph/canvas library, auto-layout, semantic zoom, minimap, production project-search backend, final URL contract and visual identity remain deliberately unfrozen.

---

## Retrieval / MethodologicalHorizon continuation

Primary open questions:

```text
docs/OPEN_QUESTIONS.md, Q-044 and Q-045
```

Still required:

```text
retrieval-quality fixtures
production lexical retrieval
semantic retrieval candidate evaluation
lexical/semantic fusion if justified
ranking and omission-quality evaluation
first real MethodologicalHorizon construction
selective LLM context assembly
```

Do not select embedding/reranking/vector infrastructure from intuition.

---

## Current exact priorities

```text
A. LangGraph durability comparator under Specification 005
B. evidence-based runtime/no-runtime comparison and candidate stopping decision
C. production retrieval / MethodologicalHorizon benchmark
D. future Cockpit capability/product work on top of Specification 008
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
```
