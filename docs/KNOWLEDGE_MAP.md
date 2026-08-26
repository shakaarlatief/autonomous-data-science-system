# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources and does not replace them.  
**Last reviewed:** 2026-08-26  
**Current checkpoint:** 206  
**Active development branch:** `v1-cockpit-design-exploration`  
**Active PR:** none  
**Exploration base:** `v1-frontend-spike` Checkpoint 205 head `2480109fadeee1e480ef03b82e335aacdf9adf91`  
**Promoted V1 integration branch:** `v1-frontend-spike` at `ed5b60bdc882bed0799ce55228ce8187f9c55aa1`

## Start here

```text
README.md                         project overview and current stage
docs/CURRENT_STATE.md             exact present state and continuation
docs/KNOWLEDGE_MAP.md             routing/index layer
docs/current_routing.json         machine-readable project routing metadata
docs/VISION.md                    high-level product/system direction
docs/PRINCIPLES.md                accepted high-level design principles
docs/DECISIONS.md                 accepted project-level decisions
docs/OPEN_QUESTIONS.md            unresolved questions
docs/DEVELOPMENT_METHOD.md        current canonical development method v0.5
docs/CONTINUITY.md                provider-neutral continuity procedure
docs/MAJOR_CHANGES.md             selective structural history
```

Current route:

```text
active development branch        v1-cockpit-design-exploration
active PR                        none
current checkpoint               206
latest specification             Specification 024
Specification 024 outcome        COLLABORATION_STATE_GUARD_ACCEPTED
promoted Cockpit baseline        Specification 008
latest scientific outcome        INCOMPLETE / EXECUTION INTEGRITY FAILED
current boundary                 next-generation Cockpit design exploration
MC-0004 phase                    Claude independent Phase A pending
source-vault deployment          PAUSED, preserved, Course 2 gate unchanged
```

---

# Current stage: next-generation Project Cockpit design exploration

Primary route:

```text
docs/checkpoints/206_source_vault_paused_cockpit_design_exploration_opened.md
docs/research/037_project_cockpit_next_generation_visual_interaction_design_exploration_map.md

docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
docs/specifications/008_v1_project_cockpit_interaction_architecture.md

docs/model_collaboration/threads/MC-0004/BRIEF.md
docs/model_collaboration/threads/MC-0004/THREAD.md
docs/model_collaboration/threads/MC-0004/STATE.json
docs/model_collaboration/REVIEW_INBOX.md
```

Current research sequence:

```text
broad external/product research
    -> independent Claude counter-design
    -> comparative synthesis
    -> realistic visual mockups / bounded interaction prototypes
    -> human product review
    -> implementation specification only if earned
```

No frontend implementation is authorized by the current checkpoint.

---

# Promoted Cockpit interaction architecture remains Specification 008

Primary route:

```text
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
docs/research/002_primary_project_cockpit_interface_concept.md
docs/research/003_unified_cockpit_workspace_and_spatial_focus_architecture.md
docs/research/004_cockpit_spatial_scalability_immersive_chrome_and_fullscreen.md
docs/research/005_cockpit_canvas_dominance_zoom_and_scalable_project_navigation.md
docs/research/006_fourth_cockpit_human_review_balanced_spatial_world_and_visual_orientation.md
docs/research/007_fifth_cockpit_human_review_continuous_grid_world_stage_ruler_and_vertical_tool_rail.md
docs/research/008_sixth_cockpit_human_review_world_ambient_continuity_pinch_stability_and_collision_safety.md
docs/research/009_seventh_cockpit_human_review_pinch_responsiveness_and_interaction_promotion.md
docs/research/012_post_promotion_cockpit_normal_window_and_pinch_sensitivity_review.md
frontend/README.md
```

Promoted interaction properties:

```text
Project Cockpit as primary immersive active-work environment
living project-process projection
meaningful work-unit semantics
spatial focus into reusable specialist workspaces
reachability != simultaneous mounting
finite navigable world distinct from semantic project plane
2D project navigation and recovery
bounded geometric zoom / native pinch capability
viewport-aware stage orientation
scalable Jump/search
compact/fold-away chrome
collision-safe floating surfaces
fullscreen with graceful fallback
URL-addressable focus/deep-work state
keyboard accessibility and reduced-motion support
world-owned restrained ambient depth
```

Still intentionally unfrozen:

```text
final visual identity
final graph/canvas technology
semantic zoom/grouping
project auto-layout
minimap
stage taxonomy / widths / ruler treatment
permanent tool-rail design
final ambient treatment
final route/persistence details
canonical screenshot baseline
```

Research 037 explores this open space. It does not replace Specification 008.

---

# Research 037: next-generation visual and interaction map

Primary route:

```text
docs/research/037_project_cockpit_next_generation_visual_interaction_design_exploration_map.md
```

Coverage:

```text
Spatial world / canvas
Grid and ambient world
Work-unit visual grammar
Relation / connector semantics
Semantic zoom and level of detail
Stage / project orientation
Focus transitions and workspace handoff
Runtime / execution visualization
Blocked / unresolved / approval / completed / deferred state
Navigation, search and command surfaces
Conversation system and full transcript workspace
Inspectors / context / evidence surfaces
Information-density lenses
Depth / 2.5D / bounded 3D
Motion language
Large-project scalability
Light/dark visual identity
Accessibility and reduced motion
Rendering / interaction technology
Loading / empty / error / recovery behavior
```

External reference families include:

```text
React Flow
Dagster
Linear
VS Code
LangSmith Studio
Motion for React
Microsoft Semantic Zoom
Mapbox
Cytoscape.js
Sigma.js
PixiJS
React Three Fiber
Apache Airflow
Prefect
```

Current high-value hypotheses, not decisions:

```text
semantic zoom should be pressure-tested as a major scale/quality improvement
connectors may carry real dependency/activity semantics
moving signals should correspond to real temporal activity
completed work should visually settle
information lenses/facets may control density
context-aware commands may reduce permanent control clutter
compact composer should expand into a first-class Conversation Workspace
2.5D should be evaluated before full 3D
React Flow now deserves a comparator prototype
large project fixtures are required before visual architecture promotion
```

Candidate mockup directions:

```text
A. Precision Instrument
B. Living Analytical Field
C. Spatial Control Room
D. Depth-Aware Workbench
```

No candidate is currently promoted.

---

# Conversation Workspace is a first-class design axis

The compact native composer remains part of the Cockpit, but ADS must also support long, revisitable project conversations.

Research route:

```text
docs/checkpoints/206_source_vault_paused_cockpit_design_exploration_opened.md
docs/research/037_project_cockpit_next_generation_visual_interaction_design_exploration_map.md
docs/research/002_primary_project_cockpit_interface_concept.md
```

Product-level distinction under exploration:

```text
Composer
Conversational response
Conversation history
Conversation Workspace
```

Candidate presentation modes:

```text
docked Conversation Lens
Conversation Focus Workspace
split analytical/conversation workbench
canvas-anchored conversation expansion
direct Conversation specialist view plus Cockpit entry
```

Important invariant:

```text
long conversational history remains available and navigable
    while
consequential project truth is represented in structured project state
```

Messages and project work should eventually be able to reference one another without making raw conversation the project database.

The Conversation Workspace represents user-visible conversation, not hidden reasoning traces.

---

# MC-0004: independent Cockpit counter-design

Primary route:

```text
docs/model_collaboration/threads/MC-0004/BRIEF.md
docs/model_collaboration/threads/MC-0004/THREAD.md
docs/model_collaboration/threads/MC-0004/STATE.json
docs/model_collaboration/REVIEW_INBOX.md
```

Current state:

```text
mode                    INDEPENDENT_THEN_COMPARATIVE
lifecycle               ACTIVE
phase                   PHASE_A_INDEPENDENT_DESIGN
task owner              ChatGPT
target-state writer     ChatGPT
next expected actor     Claude
independence            BLIND_TO_CANDIDATE
Claude secondary path   docs/model_collaboration/threads/MC-0004/messages/**
```

Exact neutral review base:

```text
bedbd23f5aa5f35c79892ae633ccbc6da6ef7d88
```

Phase-A rule:

```text
Claude reads neutral brief + accepted pre-proposal baseline
Claude must not read Research 037 or later proposer candidate material
Claude freezes independent proposal under MC-0004/messages/
only then may comparative synthesis begin
```

If candidate exposure occurs accidentally, preserve the exposure and downgrade the independence classification rather than pretending the review remained blind.

---

# Permanent Source Universe deployment is preserved and paused

Primary route:

```text
docs/checkpoints/205_multimodel_promotion_postmerge_routing_reconciled.md
docs/checkpoints/198_source_substrate_promoted_permanent_vault_bootstrap_opened.md
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md

docs/foundations/022_source_universe_artifact_integrity_and_evidence_provenance_architecture.md
docs/research/034_durable_source_universe_and_evidence_substrate_architecture.md
docs/specifications/023_v1_source_universe_substrate.md
docs/checkpoints/196_source_substrate_accepted_first_corpus_validated.md
docs/source_universe/validation/001_vu_machine_learning_source_substrate_result.md
```

Specification 023 result:

```text
SU-G01 through SU-G23   PASS
SOURCE_SUBSTRATE_ACCEPTED
```

Current boundary interpretation:

```text
permanent bootstrap   PAUSED
substrate             ACCEPTED
real deployment       NOT YET EXECUTED
Course 2              BLOCKED UNTIL RECOVERY GATE PASSES
```

Still required when resumed:

```text
confirm private original source location
confirm genuinely independent backup location
choose permanent private registry/vault/restore layout
compare original corpus to reviewed fingerprints
review every MATCH / DIFFERENT / MISSING / ADDITIONAL outcome
perform reviewed ingestion
working integrity audit
independent verified backup
clean restore
restored integrity audit
public-safe deployment evidence
```

The pause does not alter the source architecture or runbook.

---

# Governed multi-model development is accepted infrastructure

Primary route:

```text
docs/checkpoints/204_multimodel_collaboration_method_promoted.md
docs/checkpoints/205_multimodel_promotion_postmerge_routing_reconciled.md
docs/DEVELOPMENT_METHOD.md
docs/CONTINUITY.md
docs/DECISIONS.md, D-034
docs/model_collaboration/README.md
docs/model_collaboration/INTERACTION_PROVENANCE_AND_NAMING.md
docs/model_collaboration/DEFERRED_REVIEW_AND_CATCHUP.md
docs/model_collaboration/REVIEW_INBOX.md
docs/specifications/024_v1_model_collaboration_state_guard.md
```

Current collaboration status:

```text
MC-0001   CLOSED
MC-0002   CLOSED
MC-0003   CLOSED
MC-0004   ACTIVE / Claude Phase A pending
review inbox   MC-0004 pending
```

Accepted collaboration principles:

```text
repository authority
SOLO remains first-class
selective task-scoped collaboration
one bounded task owner
ROLE != WRITE_SCOPE
one target-state writer at a time
explicit secondary write surfaces
machine-readable collaboration-state coherence guard
transport != authority
durable numbered collaboration provenance
independent-first review where anchoring matters
known contamination disclosure
explicit disagreement classification/routing
provider-local interaction session identities
human project-intent authority without routine transport burden
deferred review/catch-up with exact targets and explicit gates
API orchestration deferred
unattended scheduled model review deferred
```

Provider-neutral checkpoint provenance begins at Checkpoint 204.

---

# Specification 024: accepted collaboration-state guard

Primary route:

```text
docs/specifications/024_v1_model_collaboration_state_guard.md
schemas/model_collaboration_thread_state_v1.schema.json
scripts/check_model_collaboration_state.py
tests/unit/test_model_collaboration_state.py
.github/workflows/model-collaboration-state.yml
```

Final outcome:

```text
COLLABORATION_STATE_GUARD_ACCEPTED
```

The mechanism is a coherence guard, not authenticated model identity or a distributed mutex.

---

# Serious methodological knowledge-universe construction

Primary route:

```text
docs/research/033_methodological_knowledge_universe_construction_framework.md
docs/methodological_knowledge/COVERAGE_MAP.md
docs/checkpoints/193_methodological_knowledge_universe_construction_framework_frozen.md
```

Coverage depth:

```text
C0  MAPPED
C1  SOURCED
C2  DECOMPOSED
C3  OPERATIONALIZED
C4  CONNECTED
C5  BEHAVIORALLY_TESTED
C6  PROJECT_EXPOSED
```

First six deep slices:

```text
Validation and Generalization Design
Missing Data
Feature Selection
Tree Models and Ensembles
Class Imbalance / Metrics / Calibration / Thresholding
Time-Series Methodology
```

The Cockpit exploration is a deliberate product/frontend subtrack. The methodological knowledge-universe program remains the larger V1 objective.

---

# Stable accepted architecture

Current accepted implementation decisions include:

```text
D-028  SQLite-centered local-first operational architecture
D-029  SQLAlchemy Core 2.0 + Alembic 1.x
D-030  pyproject.toml + uv + committed uv.lock + uv_build
D-031  governed deterministic JSON / JSON Schema interchange
D-032  OpenAI Agents SDK behind ADS-owned ReasoningRuntime
D-033  ADS-owned private Source Universe substrate + relational registry
D-034  governed provider-neutral multi-model development collaboration
```

Research 037 promotes no new Level-2 architecture or technology choice.

---

# Exact continuation

```text
1. reconstruct from Checkpoint 206
2. use v1-cockpit-design-exploration as the active research/design branch
3. keep Specification 008 as the promoted Cockpit interaction baseline
4. keep permanent source-vault deployment paused with Course 2 gate unchanged
5. complete Claude MC-0004 Phase A from exact neutral ref bedbd23f5aa5f35c79892ae633ccbc6da6ef7d88
6. preserve Claude's independent proposal under MC-0004/messages/
7. only then compare Claude's design with Research 037
8. select the strongest 2-4 design directions/mechanisms for realistic mockups
9. explicitly mock/prototype long-form Conversation Workspace behavior
10. pressure-test medium/large project maps and active/blocked/completed/runtime states
11. perform human visual/product review
12. freeze implementation only after that evidence
13. resume permanent source-vault deployment whenever the project owner chooses
```
