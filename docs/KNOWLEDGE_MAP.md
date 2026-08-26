# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources and does not replace them.  
**Last reviewed:** 2026-08-26  
**Current checkpoint:** 207  
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
current checkpoint               207
latest specification             Specification 024
Specification 024 outcome        COLLABORATION_STATE_GUARD_ACCEPTED
promoted Cockpit baseline        Specification 008
latest scientific outcome        INCOMPLETE / EXECUTION INTEGRITY FAILED
current boundary                 MC-0004 Phase B comparative Cockpit design review
source-vault deployment          PAUSED, preserved, Course 2 gate unchanged
```

---

# Current stage: next-generation Project Cockpit design exploration

Primary route:

```text
docs/checkpoints/207_mc0004_phase_a_frozen_comparative_design_opened.md
docs/checkpoints/206_source_vault_paused_cockpit_design_exploration_opened.md
docs/research/037_project_cockpit_next_generation_visual_interaction_design_exploration_map.md

docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
docs/specifications/008_v1_project_cockpit_interaction_architecture.md

docs/model_collaboration/threads/MC-0004/BRIEF.md
docs/model_collaboration/threads/MC-0004/THREAD.md
docs/model_collaboration/threads/MC-0004/STATE.json
docs/model_collaboration/threads/MC-0004/messages/001_claude_independent_phase_a_proposal.md
docs/model_collaboration/REVIEW_INBOX.md
```

Current sequence:

```text
ChatGPT Research 037
    +
Claude independent Phase A  COMPLETE
    ->
Claude comparative Phase B  ACTIVE
    ->
ChatGPT comparative synthesis
    ->
realistic mockups / bounded mechanism prototypes
    ->
human product review
    ->
implementation specification only if earned
```

No frontend implementation is authorized by the current checkpoint.

---

# MC-0004 status

Claude Phase A is frozen at:

```text
commit                  cd2e12f2c79ee3b2f205457c5940eb2022b4631a
review base             bedbd23f5aa5f35c79892ae633ccbc6da6ef7d88
historical independence BLIND_TO_CANDIDATE
candidate exposures     none
```

Claude changed only the declared collaboration-message surface.

Phase B is now:

```text
phase                   PHASE_B_COMPARATIVE_REVIEW
mode                    COMPARATIVE_ONLY
next expected actor     Claude
allowed Claude writes   docs/model_collaboration/threads/MC-0004/messages/**
```

Claude may now read Research 037 and compare it with the frozen Phase-A proposal. Its comparative response is required before final ChatGPT synthesis.

The first generic cross-model trigger failed because Claude remained on an older branch whose inbox correctly said `NONE`. The failure did not expose candidate design material. Current operational routing therefore explicitly names the active branch/ref when work exists only on an unpromoted branch. Checkpoint 207 preserves this as an empirical collaboration-method finding pending promotion audit.

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

Current candidate directions remain provisional:

```text
A. Precision Instrument
B. Living Analytical Field
C. Spatial Control Room
D. Depth-Aware Workbench
```

Claude's independent candidate set adds:

```text
1. Living Process Canvas      preferred by Claude Phase A
2. Analytical Command Deck    strongest fallback
```

Comparative synthesis will decide which mechanisms, not merely which labels, deserve mockups.

---

# Conversation Workspace is a first-class design axis

The compact native composer remains part of the Cockpit, but ADS must also support long, revisitable project conversations.

Current requirement:

```text
long multi-turn project dialogue
visible previous user/system messages
re-entry into earlier discussion
conversation search/navigation
contextual discussion of visible project work
full Conversation Workspace / transcript experience
```

Consequential outcomes must still map into structured project state rather than living only as prose history.

Claude independently converged on using the validated Cockpit focus-transition model for the Conversation Workspace, with bidirectional links between consequential messages and structured project objects. Threading/persistence details remain provisional.

---

# Governed multi-model development

Canonical route:

```text
docs/DEVELOPMENT_METHOD.md
docs/CONTINUITY.md
docs/DECISIONS.md, D-034
docs/model_collaboration/README.md
docs/model_collaboration/INTERACTION_PROVENANCE_AND_NAMING.md
docs/model_collaboration/DEFERRED_REVIEW_AND_CATCHUP.md
docs/model_collaboration/REVIEW_INBOX.md
docs/specifications/024_v1_model_collaboration_state_guard.md
```

Accepted rules remain repository authority, selective task-scoped collaboration, one bounded task owner, `ROLE != WRITE_SCOPE`, one target-state writer at a time, explicit secondary surfaces, independent-first review where valuable, explicit contamination disclosure, durable numbered messages, and human arbitration only for genuine intent/consequence choices.

The branch-qualified handoff lesson from MC-0004 is not yet promoted into the canonical method.

---

# Source Universe deployment remains paused

Primary route:

```text
docs/checkpoints/198_source_substrate_promoted_permanent_vault_bootstrap_opened.md
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
docs/foundations/022_source_universe_artifact_integrity_and_evidence_provenance_architecture.md
docs/research/034_durable_source_universe_and_evidence_substrate_architecture.md
docs/specifications/023_v1_source_universe_substrate.md
docs/checkpoints/196_source_substrate_accepted_first_corpus_validated.md
```

Current interpretation:

```text
SOURCE_SUBSTRATE_ACCEPTED
permanent deployment PAUSED
not cancelled or superseded
Course 2 gate unchanged
```

---

# Methodological knowledge-universe program remains the larger V1 objective

Primary route:

```text
docs/research/033_methodological_knowledge_universe_construction_framework.md
docs/methodological_knowledge/COVERAGE_MAP.md
docs/checkpoints/193_methodological_knowledge_universe_construction_framework_frozen.md
```

Initial deep slices remain Validation and Generalization Design, Missing Data, Feature Selection, Tree Models and Ensembles, Class Imbalance / Metrics / Calibration / Thresholding, and Time-Series Methodology.

The current Cockpit work is a deliberate frontend/product subtrack, not a replacement for the larger methodological program.
