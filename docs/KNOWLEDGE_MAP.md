# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources but does not replace them.  
**Last reviewed:** 2026-08-21  
**Current checkpoint:** 130  
**Active development branch:** `v1-runtime-bakeoff`

## Start here

For a new session or quick reconstruction:

```text
README.md
    project-level overview and current branch/stage

docs/CURRENT_STATE.md
    present state, active gates, and exact next step

docs/KNOWLEDGE_MAP.md
    routing layer

docs/VISION.md
    current system purpose and product direction

docs/PRINCIPLES.md
    current high-level design principles

docs/DECISIONS.md
    accepted project-level decisions

docs/OPEN_QUESTIONS.md
    reconciled current unresolved questions

docs/DEVELOPMENT_METHOD.md
    development/preservation method

docs/CONTINUITY.md
    cross-session continuation and unplanned-boundary recovery

docs/MAJOR_CHANGES.md
    selective structural history
```

Current branch relationship:

```text
active executable V1/runtime work = v1-runtime-bakeoff
preserved promoted V1/frontend boundary = v1-frontend-spike
main intentionally trails current V1 work
```

A continuation session must not infer the latest project state from `main` alone while this branch relationship remains active.

---

## Current project stage

Prototype V0 is complete and its final classification is:

> **STRONG FALSIFICATION OF THE CURRENT P0 DESIGN**

The project is now implementing bounded V1 slices across:

```text
methodological knowledge
governed persistence/interchange
retrieval / MethodologicalHorizon construction
agent/runtime infrastructure
professional frontend
Project Cockpit
```

Current major boundaries:

```text
Project Cockpit interaction architecture
    promoted through Specification 008 / Checkpoint 126
    post-promotion Jump/pinch polish automatically validated through Checkpoint 130
    short real-browser/hardware retest remains open

governed reusable-knowledge persistence/interchange seam
    closed across SQLite/Linux, SQLite/Windows, PostgreSQL 18
    Checkpoint 127

runtime bakeoff
    ecosystem refreshed in Checkpoint 128
    direct-call control passed in Checkpoint 129
    OpenAI Agents SDK 0.19.4 core subgate now passes cross-platform
    remaining OpenAI gates AR-03 / AR-08 / AR-09 / AR-11 still open
```

The main execution priority is the **Specification 005 one-principal-reasoner runtime bakeoff**. The production retrieval/MethodologicalHorizon benchmark is the other highest-value active V1 track.

---

## System purpose and LLM/system/human boundary

Primary sources:

```text
docs/VISION.md
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
```

Current durable interpretation:

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
    approvals / intervention where useful
```

Every explicit mechanism must earn its complexity empirically.

---

## Prototype V0 evidence and architectural constraint

Authoritative evidence:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
prototype_v0/README.md
docs/checkpoints/096_prototype_v0_final_strong_falsification_and_architecture_diagnostic_conclusion.md
```

Core scaling lesson:

```text
what the SYSTEM should remember
    !=
what the LLM should receive on every reasoning call
```

Do not reintroduce unchanged:

```text
full structured state/context every reasoning cycle
large always-on frontier/context
path-sensitive tag-trigger activation
generic recursive support reassessment
universal dependency reopening machinery
```

---

## Project object model and professional developer workflow

Primary source:

```text
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
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

Core structures:

```text
OBJECTS
RELATIONS
EVENTS
VIEWS
```

Subject-specific verdicts use:

```text
Question -> Evidence -> Finding -> Claim / Decision
```

with structured criterion Findings where useful.

Professional-workflow responsibility split:

```text
ADS
    project/process control plane

VS Code
    developer workbench

Python / Docker / local or remote compute
    execution plane

Git + GitHub
    source versioning, collaboration, provenance
```

---

## Methodological-navigation brain and reusable knowledge

Primary sources:

```text
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
```

Relevance progression:

```text
KNOWN
    -> APPLICABLE
    -> RELEVANT
    -> RECOMMENDED
    -> REQUIRED / BLOCKING
```

Scaling concept:

```text
large global knowledge universe
    -> project-specific retrieval/filtering
    -> bounded MethodologicalHorizon
    -> explicit applicability/context checks
    -> flexible relevance/prioritization reasoning
    -> selective task-specific LLM context
```

Reusable representation:

```text
KnowledgeAsset
KnowledgeComponent
NarrativeFacet
KnowledgeRelation
Conditional KnowledgeRule
KnowledgeCollection
exact stable/revision identity
project-object references/influence
criterion Finding
ExecutionCapability
derived Views
```

Durable distinctions:

```text
intrinsic knowledge kind != reasoning function
asset != component != narrative facet
static semantic relation != conditional methodological rule
retrieval cue != applicability predicate != required context != project relevance
methodological knowledge != execution implementation
global knowledge != project-specific state
internal representation != human-facing workflow/tree
```

Key stress-test/promotion sources:

```text
docs/checkpoints/101_five_example_reusable_knowledge_stress_test_completed.md
docs/checkpoints/102_candidate_conceptual_knowledge_representation_contract.md
docs/checkpoints/104_adversarial_review_of_candidate_knowledge_representation.md
docs/checkpoints/105_refined_representation_second_stress_test.md
docs/checkpoints/106_foundation_020_promoted_and_implementation_requirements_next.md
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

Accepted direction:

```text
SQLite-centered local-first operational architecture
FTS5 rebuildable lexical index
rebuildable embeddings / initial exact semantic retrieval
application rule evaluator
selective context assembler
filesystem / Git / artifact storage outside SQLite

SQLAlchemy Core 2.0
Alembic 1.x
PostgreSQL identifier portability
unique Alembic revision IDs <= 32 chars while the default version table remains

pyproject.toml
uv + committed uv.lock
uv_build
src/ads_system
Python >=3.12

JSON
JSON Schema Draft 2020-12
application semantic validation
deterministic interchange normalization/serialization
```

Early milestones:

```text
docs/checkpoints/114_first_production_v1_persistence_vertical_slice_passed.md
docs/checkpoints/115_reusable_knowledge_interchange_contract_validated.md
```

Checkpoint 114 passed the first production persistence slice on SQLite/Linux, SQLite/Windows, and PostgreSQL 18.

Checkpoint 115 validated the reusable-knowledge interchange contract across Linux/Windows and Python 3.12 through 3.14.

---

## Governed reusable-knowledge round-trip: CLOSED

Current authoritative result:

```text
experiments/architecture_spikes/V1_KNOWLEDGE_ROUNDTRIP_RESULT.md
experiments/architecture_spikes/V1_KNOWLEDGE_ROUNDTRIP_STATUS.md
docs/checkpoints/127_governed_knowledge_roundtrip_closed_across_sqlite_and_postgresql.md
```

Final gate:

```text
V1 governed knowledge roundtrip closure gate
run 32496856945

SQLite / Ubuntu     PASS
SQLite / Windows    PASS
PostgreSQL 18       PASS
Alembic revision-ID portability guard PASS on all three jobs
```

Validated governed behavior includes:

```text
candidate import
explicit acceptance
accepted-current pointers
accepted snapshot export
provenance
relation governance
collections
migration 0002
historical project revision pinning across later acceptance
```

Two portability defects were resolved:

```text
PostgreSQL 63-byte identifier limit
    -> overlong manually named constraint shortened

Alembic default version table VARCHAR(32)
    -> revision `0002_reusable_knowledge_interchange` shortened to
       `0002_knowledge_interchange`
```

A deterministic regression guard now requires unique Alembic revision IDs with length <= 32 characters.

Q-048 is closed as an implementation gate.

This evidence does not validate retrieval/horizon quality, embeddings, reranking, or knowledge-authoring UX.

---

## Agent/runtime bakeoff: ACTIVE

Primary research/specification/evidence:

```text
docs/research/001_2026_agentic_ecosystem_and_integration_architecture_audit.md
docs/research/010_2026_runtime_bakeoff_preimplementation_refresh.md
docs/research/011_openai_agents_0_19_4_released_api_compatibility_findings.md
docs/specifications/005_v1_agent_runtime_and_interoperability_bakeoff.md

docs/checkpoints/128_runtime_bakeoff_preimplementation_evidence_refreshed.md
docs/checkpoints/129_direct_call_control_runtime_baseline_passed.md

experiments/runtime_bakeoff/DIRECT_CALL_CONTROL_RESULT.md
experiments/runtime_bakeoff/candidates/openai_agents/CORE_RESULT.md
```

Durable boundary:

```text
ADS domain/project/methodological semantics
    owned by ADS

agent runtimes / MCP / runtime checkpoints
    replaceable infrastructure/interoperability
```

Current evaluation order, not selection:

```text
CONTROL
    direct model calls with ADS-owned execution semantics

FIRST FRAMEWORK CANDIDATE
    OpenAI Agents SDK

SECOND DURABILITY COMPARATOR
    LangGraph

SECONDARY / CONDITIONAL
    Microsoft Agent Framework
    Google ADK 2.0
```

### Direct-call control

Checkpoint 129 proves the simpler control is executable rather than hypothetical.

Validated cross-platform behavior includes:

```text
ADS-owned model/tool loop
exact context-pack digest + revision provenance
approval before authoritative side effect
serialized process-boundary resume
ADS-owned at-most-once proposal ledger
repeated-resume idempotency
rejection
stale-context rejection
cancellation
controlled retry
normalized trace
ADS-owned structured recommendation
```

Gate:

```text
run 32500521858
Ubuntu PASS
Windows PASS
existing Python suite PASS
```

### OpenAI Agents SDK 0.19.4 core candidate

The candidate is isolated under:

```text
experiments/runtime_bakeoff/candidates/openai_agents/
```

The framework remains outside `ads_system.domain` and is not an unconditional production dependency.

Validated core gates:

```text
AR-01 domain isolation
AR-02 single-agent tool loop
AR-04 native approval interruption
AR-05 serialized RunState process-boundary resume
AR-06 external ADS project-state authority
AR-07 exact context/revision transparency
AR-10 structured output + ADS provenance validation
AR-12 deterministic no-live-provider testing through released public Model boundary
```

Core gate:

```text
run 15 / 32501907783
Ubuntu PASS
Windows PASS
direct controls PASS
existing Python suite PASS
```

Latest combined branch gate after Checkpoint-130 frontend polish:

```text
run 20 / 32503861259
OpenAI core Ubuntu PASS
OpenAI core Windows PASS
direct control Ubuntu PASS
direct control Windows PASS
existing Python suite PASS
```

Research 011 records an important maturity finding:

```text
current docs advertise agents.testing.ScriptedModel
published openai-agents==0.19.4 does not ship agents.testing
released public Model interface is sufficient for an isolated deterministic fake
```

Remaining OpenAI mandatory work:

```text
AR-03 current MCP integration
AR-08 cancellation and bounded timeout
AR-09 controlled failure/retry behavior
AR-11 normalized observability
```

No runtime is selected. Direct calls remain a valid final winner if no framework earns its dependency/operational burden.

---

## Professional frontend foundation

Primary foundation/specification:

```text
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
docs/specifications/006_v1_frontend_architecture_and_visual_spike.md
```

Leading stack hypothesis, not final accepted architecture:

```text
React
TypeScript
Vite
TanStack Router
TanStack Query
TanStack Table
ADS-owned design system
Playwright
Vitest
```

Chart strategy remains under evaluation:

```text
ECharts
vs
Plotly
```

Tauri remains deferred.

---

## Project Cockpit: promoted interaction architecture plus bounded post-promotion polish

Historical research and spike evolution:

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

docs/specifications/007_v1_unified_project_cockpit_interaction_spike.md
```

Current authoritative interaction contract:

```text
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
```

Promotion checkpoint:

```text
docs/checkpoints/126_seventh_cockpit_review_validated_and_interaction_architecture_promoted.md
```

Current post-promotion polish checkpoint:

```text
docs/checkpoints/130_post_promotion_cockpit_normal_window_and_pinch_polish_gate_passed.md
```

Promoted model:

```text
Project Cockpit
    primary immersive active-work environment
    living project-process projection
    native system interaction
    focused analytical work

Direct specialist views
    alternative entry / inspection / records
    reuse the same modules/state
```

Promoted interaction principles:

```text
meaningful work units rather than every persisted object
spatial focus into real specialist workspaces
reachability != simultaneous mounting
FiniteNavigableGridWorld != SemanticProjectPlane
2D navigation and recovery
bounded geometric zoom
native laptop pinch capability
viewport-aware stage orientation
scalable Jump/search project location
compact/fold-away immersive chrome
collision-safe floating surfaces
true fullscreen with graceful fallback
URL-addressable focus/deep-work state
keyboard accessibility and reduced-motion support
world-owned restrained ambient depth
```

Promotion validation:

```text
head 2c3b522e2416d73c015ce5ec2a4560a227524dd9
run 155 / 32492536072

Ubuntu build + unit tests                 PASS
Windows build + unit tests                PASS
Chromium interaction/accessibility        PASS
controlled direct-view visual regression  PASS
```

Checkpoint-130 bounded polish:

```text
normal-window Jump/search collision
    -> palette now measures actual composer boundary
    -> re-clamps on resize/fullscreen/composer resize

native pinch scale travel
    -> PINCH_SENSITIVITY 0.0018 -> 0.0024
    -> smoothing/coalescing/anchoring retained
```

Automated polish gate:

```text
head ae83e920b3fa43ee8242bdb1ca2640d23a474c71
run 167 / 32503861255

Ubuntu build + unit tests                  PASS
Windows build + unit tests                 PASS
Chromium interaction/accessibility         PASS
controlled direct-view visual regression   PASS
normal-window Jump re-clamp regression      PASS
faster anchored pinch regression            PASS
```

Short human retest remains open for actual Chrome-window geometry and real trackpad feel. The remaining tiny occasional pinch hitch remains non-blocking deferred polish.

Still deliberately unfrozen:

```text
final pinch/zoom constants
final graph/canvas or gesture library
final auto-layout algorithm
final semantic zoom/grouping
final minimap
infinite-canvas semantics
final finite-world extent algorithm
production project-search backend
final stage taxonomy/widths
final stage-ruler visual treatment
permanent vertical tool-rail styling/iconography
final ambient styling
final public URL contract
pan/zoom/HUD persistence contract
final visual identity
canonical Cockpit screenshot baseline
```

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

Do not choose an embedding model, reranker, ANN service, or vector database from intuition.

The benchmark should distinguish catalog absence, retrieval omission, applicability judgment, ranking failure, recommendation error, and required-concern omission.

---

## Current exact cross-track priorities

```text
A. Short Checkpoint-130 Cockpit human retest
   normal-window Jump/composer safety
   fullscreen non-regression
   real-trackpad pinch travel

B. Complete OpenAI Agents SDK Specification-005 gates
   AR-03 MCP
   AR-08 cancellation/timeouts
   AR-09 failure/retry
   AR-11 observability
   then compare with direct-call control

C. Retrieval / MethodologicalHorizon benchmark

D. LangGraph durability comparator if still decision-relevant after completed OpenAI evidence
```

The governed persistence/interchange seam is no longer an active blocker.

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
126  seventh Cockpit review + final gate + interaction architecture promotion
127  governed knowledge round-trip closed across SQLite and PostgreSQL
128  runtime-bakeoff ecosystem evidence refreshed
129  direct-call runtime control baseline passed cross-platform
130  post-promotion normal-window Jump/pinch polish automated gate passed; human retest open
```
