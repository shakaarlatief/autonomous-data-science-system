# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources and does not replace them.  
**Last reviewed:** 2026-08-26  
**Current checkpoint:** 210  
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
current checkpoint               210
latest specification             Specification 024
Specification 024 outcome        COLLABORATION_STATE_GUARD_ACCEPTED
promoted Cockpit baseline        Specification 008
latest scientific outcome        INCOMPLETE / EXECUTION INTEGRITY FAILED
current boundary                 MC-0004 Phase C grid/world human review
source-vault deployment          PAUSED, preserved, Course 2 gate unchanged
```

---

# Current stage: browser-rendered Project Cockpit design experiments

Primary route:

```text
docs/checkpoints/210_grid_world_design_lab_browser_verified_human_review_opened.md
docs/checkpoints/209_phase_c_browser_design_lab_grid_world_opened.md
docs/research/039_phase_c_browser_rendered_design_experiment_protocol_and_grid_world_slice.md
docs/research/038_mc0004_comparative_cockpit_design_synthesis_and_mockup_direction_set.md
docs/research/037_project_cockpit_next_generation_visual_interaction_design_exploration_map.md

docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
docs/specifications/008_v1_project_cockpit_interaction_architecture.md

docs/model_collaboration/threads/MC-0004/BRIEF.md
docs/model_collaboration/threads/MC-0004/THREAD.md
docs/model_collaboration/threads/MC-0004/STATE.json
docs/model_collaboration/threads/MC-0004/messages/001_claude_independent_phase_a_proposal.md
docs/model_collaboration/threads/MC-0004/messages/002_claude_comparative_review.md
docs/model_collaboration/REVIEW_INBOX.md

frontend/design-lab/grid-world.html
frontend/design-lab/grid-world.css
frontend/design-lab/grid-world-overrides.css
frontend/design-lab/grid-world.js
```

Current sequence:

```text
ChatGPT Research 037
    +
Claude independent Phase A  COMPLETE / BLIND_TO_CANDIDATE
    ->
Claude comparative Phase B  COMPLETE / COMPARATIVE_ONLY
    ->
ChatGPT Research 038 synthesis  COMPLETE
    ->
Research 039 browser-experiment protocol  ACTIVE METHOD
    ->
G1-G4 grid/world design lab  BROWSER VERIFIED
    ->
human grid/world disposition  CURRENT GATE
    ->
next bounded design slice
    ->
progressively integrated Cockpit prototype
    ->
production implementation only if earned
```

Generated-image UI concepts are not part of the preferred Cockpit design workflow.

---

# Phase C browser-design protocol

Research 039 replaces generated-image mockups with a design-question-first loop:

```text
choose one design question
inspect real external references where useful
build two to four materially different browser variants
hold representative content/state constant
human compares
record PREFER / REJECT / COMBINE / REFINE / UNRESOLVED
refine if necessary
move to the next design question
```

Current provisional slice order:

```text
Slice 1   grid / spatial world substrate             ACTIVE HUMAN REVIEW
Slice 2   work-unit visual grammar                   NEXT EXPECTED SLICE
Slice 3   connector semantics and static language
Slice 4   semantic zoom / level of detail
Slice 5   liveness / motion budget
Slice 6   Conversation Workspace presentation
Slice 7   selection, focus and bounded 2.5D depth
Slice 8   information lenses and command/navigation treatment
Slice 9   integrated Cockpit candidate
Slice 10  medium / large project pressure test
```

The sequence is provisional. Related mechanisms may be combined when they cannot be evaluated independently.

Isolated `frontend/design-lab/**` code is allowed for learning. It is not production Cockpit code.

---

# Grid / world substrate experiment

Experiment route:

```text
frontend/design-lab/grid-world.html
```

Expected Vite URL:

```text
http://localhost:5173/design-lab/grid-world.html
```

Constant project scene:

```text
Prediction moment         unresolved / blocking
Production missingness    active investigation
Chronological validation  selected
Baseline logistic model   completed / settled
Evaluation                 downstream
```

Variants:

```text
G1  Precision Lines
    fine minor Cartesian lines
    stronger major divisions

G2  Dot Matrix
    low-noise dot field
    sparse stronger anchor dots

G3  Cross Lattice
    sparse repeated cross/intersection rhythm

G4  Adaptive Hybrid
    major/minor hierarchy
    scale-aware detail reduction
    bounded local activity field
```

Controls:

```text
dark / light appearance
project / work / inspection scale simulation
content visible / grid-only state
activity field on / off
per-variant focus mode
```

Browser verification:

```text
Chromium load                 PASS
JavaScript page errors        NONE
four variant render           PASS
appearance control            PASS
scale control                 PASS
browser screenshot render     PASS
```

The initial G3 implementation produced visually heavy repeated bands. Real browser inspection caught the defect and it was corrected to a sparse cross pattern before human review.

Current human questions:

```text
Which substrate is most comfortable for long sessions?
Which gives the clearest spatial orientation?
Which interferes least with work-unit text and relation lines?
Which feels professional and distinctive for ADS?
Does the preference hold in both light and dark appearance?
Does project scale become appropriately quieter?
Does G4 local activity communicate real state or feel ornamental?
Should mechanisms be combined across variants?
```

---

# MC-0004 status

Claude Phase A is frozen at:

```text
commit                  cd2e12f2c79ee3b2f205457c5940eb2022b4631a
review base             bedbd23f5aa5f35c79892ae633ccbc6da6ef7d88
historical independence BLIND_TO_CANDIDATE
candidate exposures     none
```

Claude Phase B is frozen at:

```text
commit          d94d696214a41d2a3904aa9ce2a42bdab5f2f3ce
classification  COMPARATIVE_ONLY
message         docs/model_collaboration/threads/MC-0004/messages/002_claude_comparative_review.md
```

Current thread state:

```text
phase                   PHASE_C_BROWSER_DESIGN_EVALUATION
next expected actor     human
pending Claude review   NONE
```

The strongest independently reinforced design findings remain:

```text
semantic zoom is a major remaining quality/scalability opportunity
current work-unit grammar is too generic
connectors should encode type + direction + state/liveness
motion should be sparse and tied to real temporal project activity
the resting world should remain calm
full long-form conversation is first-class
2.5D is preferred before full 3D
```

Research 037 contributes especially strong external product evidence, information-density lenses, multi-axis state separation and appropriate caution around conversation persistence.

Claude contributes especially strong code-level specificity, a falsifiable connector-motion hypothesis, decision-ready recommendation discipline and a valid scope-creep warning around excessive technology prototyping.

The strongest genuine unresolved disagreement remains command architecture at scale. Its resolution gate is medium/large project evidence, not model preference.

The first generic cross-model trigger failure remains preserved as empirical collaboration-method evidence: work on an unpromoted branch must explicitly identify repository + branch/ref + routing/thread surface when handed to another model.

---

# Research 038: integrated direction hypotheses

Research 038 remains useful as the integrated synthesis of Research 037 and Claude's Phase-A/Phase-B contributions.

Its direction set remains:

```text
M1  Living Precision Canvas          preferred integrated anchor
M2  Spatial Control Room             strongest integrated alternative
M3  Depth-Aware Analytical Workbench bounded high-upside alternative
```

These labels are no longer the first thing being validated through static mockups. Their underlying mechanisms are instead being decomposed and tested through browser-rendered slices.

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

No production Cockpit implementation file has been modified by Phase C.

---

# Conversation Workspace remains a first-class design axis

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

The exact conversation persistence/threading model remains deliberately open.

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
