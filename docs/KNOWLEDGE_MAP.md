# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources and does not replace them.  
**Last reviewed:** 2026-08-26  
**Current checkpoint:** 221  
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
checkpoint                        221
active development branch        v1-cockpit-design-exploration
active PR                        none
latest specification             Specification 024
promoted Cockpit baseline        Specification 008
current boundary                 expanded work-unit grammar human browser review
source-vault deployment          PAUSED, Course 2 gate unchanged
```

---

# Active Cockpit design route

## Grid/world baseline: provisionally settled

```text
G4 Adaptive Hybrid    SELECTED
Dark mode             ACTIVE DESIGN BASELINE
Light mode            DEFERRED
```

Retained ambient behavior:

```text
travelling currents       randomized across 20 px grid lines, Lively preferred
major-grid glints          100 px intersections only, approximately Quiet
ambient drift              retained
localized semantic glow    retained
fixed authored positions   rejected
```

Primary evidence:

```text
docs/research/039_phase_c_browser_rendered_design_experiment_protocol_and_grid_world_slice.md
docs/research/040_grid_world_g4_selection_dark_first_and_ambient_dynamics_exploration.md
docs/research/041_combined_g4_ambient_motion_intensity_tuning.md
docs/research/042_g4_randomized_ambient_distribution_and_grid_intersection_glints.md
docs/research/043_g4_major_grid_glints_and_decoupled_ambient_cadence.md

docs/checkpoints/210_grid_world_design_lab_browser_verified_human_review_opened.md
docs/checkpoints/211_g4_selected_dark_first_ambient_dynamics_review_opened.md
docs/checkpoints/212_combined_g4_ambient_intensity_human_review_opened.md
docs/checkpoints/213_g4_randomized_ambient_distribution_human_review_opened.md
docs/checkpoints/214_g4_major_grid_glints_quiet_cadence_human_review_opened.md

frontend/design-lab/grid-world.html
frontend/design-lab/grid-dynamics.html
frontend/design-lab/grid-dynamics-combined.html
```

Research 040 preserves:

```text
semantic motion
    communicates project/runtime meaning

ambient/decorative motion
    may exist purely for polish/atmosphere
    must remain lower-salience and must not masquerade as semantic state
```

---

# Completed Slice 02A: H4 generic interaction lighting

Primary evidence:

```text
docs/research/044_work_unit_interaction_lighting_hover_response_exploration.md
docs/research/045_h4_resting_node_light_world_spill_refinement.md
docs/checkpoints/215_grid_world_provisionally_settled_work_unit_lighting_review_opened.md
docs/checkpoints/216_h4_selected_resting_world_spill_human_review_opened.md
docs/checkpoints/217_h4_interaction_lighting_settled_work_unit_visual_grammar_opened.md
frontend/design-lab/work-unit-lighting.html
frontend/design-lab/work-unit-lighting.css
frontend/design-lab/work-unit-lighting.js
```

Human review selected:

```text
H4 Integrated Response  SELECTED
```

Retained generic model:

```text
REST
    clean localized/asymmetric in-box illumination
    narrow asymmetric outward world spill
    no broad circular resting halo

HOVER
    full node-colored halo
    pointer-following/specular hotspot
    stronger local grid/world illumination
    immediate connector emphasis
    one restrained perimeter sweep on entry
    small depth lift
    fast entry + smoother slower release
```

The current grammar work also preserves:

```text
signature edge + signature position along edge
-> resting-light origin
```

and keeps an explicit:

```text
H4 baseline vs Reduced in-box-light comparison
```

---

# Current Slice 02B: expanded work-unit category grammar

First-round evidence:

```text
docs/research/046_work_unit_category_and_silhouette_visual_grammar_experiment.md
docs/research/047_work_unit_grammar_h4_control_correction_and_inbox_light_comparison.md
docs/checkpoints/218_work_unit_visual_grammar_browser_experiment_human_review_opened.md
docs/checkpoints/219_work_unit_grammar_preliminary_review_claude_ideation_requested.md
docs/checkpoints/220_work_unit_grammar_h4_control_corrected_claude_ideation_ready.md
frontend/design-lab/work-unit-grammar.html
frontend/design-lab/work-unit-grammar.css
frontend/design-lab/work-unit-grammar-lighting-controls.css
frontend/design-lab/work-unit-grammar.js
```

First-round candidates:

```text
W1  Unified Precision Frame
W2  Edge-Signature Grammar
W3  Structural Silhouette Family
W4  Hybrid Semantic Instrument
```

Human disposition:

```text
implementation quality  positive
selection               none
candidate-space breadth too narrow for convergence
```

## Claude divergent ideation: completed

Request:

```text
docs/model_collaboration/threads/MC-0004/messages/003_chatgpt_work_unit_grammar_divergent_ideation_request.md
```

Response:

```text
docs/model_collaboration/threads/MC-0004/messages/004_claude_work_unit_grammar_divergent_ideation.md
```

Response commit:

```text
faf18ed9932d60a24dd80589b0ec0ba71c5940fd
```

Claude concept families:

```text
C1  Instrument Glyph Family
C2  Structural Topology Family
C3  Material Language Family
C4  Port Grammar
C5  Internal Layout Grammar
C6  Aspect & Proportion Family
C7  Compact Marker Rail
C8  Scientific Marker Family
```

No artificial candidate-count cap was applied.

## Expanded executable round

Governing synthesis:

```text
docs/research/048_claude_work_unit_grammar_synthesis_and_expanded_browser_round.md
```

Current checkpoint:

```text
docs/checkpoints/221_claude_work_unit_ideation_ingested_expanded_browser_review_opened.md
```

Browser route:

```text
frontend/design-lab/work-unit-grammar-expanded.html
frontend/design-lab/work-unit-grammar-expanded.css
frontend/design-lab/work-unit-grammar-expanded.js
```

Local URL:

```text
http://localhost:5173/design-lab/work-unit-grammar-expanded.html
```

Exact browser implementation head before routing-only documentation:

```text
32883ada35506a713a7c780beca08f363ba29fab
```

Expanded matrix:

```text
Batch A · Glyph strategy
    G0 Letter Control
    G1 Instrument Glyph Family
    G2 Compact Marker Rail
    G3 Scientific Marker Family

Batch B · Structural grammar
    S0 Chamfer Control
    S1 Structural Topology Family
    S2 Aspect & Proportion Family
    S3 Inner Instrument Architecture

Batch C · Material channel
    M0 Plain Surface Control
    M1 Material Language Family

Batch D · Integrated candidates
    I0 Current W4 Hybrid Control
    I1 W4 + Instrument Glyph
    I2 W4 + Scientific Marker
```

`S3 Inner Instrument Architecture` is the ChatGPT synthesis addition covering the underexplored inner-frame channel without introducing live-looking content.

Current controls:

```text
Category strip / Project scene
H4 baseline / Reduced
All / Glyph / Structure / Surface / Integrated presentation filters
Reduced motion
```

Presentation filtering does not alter candidate status:

```text
hidden != rejected
batching != rejection
```

Preserved deferred candidates:

```text
C4 Port Grammar             -> connector-semantics slice
C5 Internal Layout Grammar  -> semantic zoom / information-density slice
```

Current evidence state:

```text
Claude ideation             COMPLETE
ChatGPT synthesis           COMPLETE
expanded browser round      IMPLEMENTED
human expanded review       OPEN
production promotion        NOT AUTHORIZED
```

---

# MC-0004 collaboration route

```text
docs/model_collaboration/threads/MC-0004/BRIEF.md
docs/model_collaboration/threads/MC-0004/THREAD.md
docs/model_collaboration/threads/MC-0004/STATE.json
docs/model_collaboration/threads/MC-0004/messages/001_claude_independent_phase_a_proposal.md
docs/model_collaboration/threads/MC-0004/messages/002_claude_comparative_review.md
docs/model_collaboration/threads/MC-0004/messages/003_chatgpt_work_unit_grammar_divergent_ideation_request.md
docs/model_collaboration/threads/MC-0004/messages/004_claude_work_unit_grammar_divergent_ideation.md
docs/model_collaboration/REVIEW_INBOX.md
```

```text
Phase A  Claude independent proposal  cd2e12f2c79ee3b2f205457c5940eb2022b4631a  BLIND_TO_CANDIDATE
Phase B  Claude comparative review    d94d696214a41d2a3904aa9ce2a42bdab5f2f3ce  COMPARATIVE_ONLY
Phase C  browser-rendered design evaluation
Latest   Claude divergent ideation    faf18ed9932d60a24dd80589b0ec0ba71c5940fd
Current  expanded browser human review
```

No model-collaboration obligation is currently pending.

---

# Phase-C design protocol

```text
choose one design question
inspect real references if useful
build bounded browser variants
hold unrelated variables constant
human compares
record prefer/reject/combine/refine
use another model selectively when divergent design value is expected
iterate if needed
move to the next design question
```

Generated-image UI concepts are not part of the preferred Cockpit evaluation workflow.

Isolated experimental code lives under:

```text
frontend/design-lab/**
```

The production `/cockpit` remains the control baseline until later integrated evidence warrants promotion.

---

# Broad Cockpit research and synthesis

```text
docs/research/037_project_cockpit_next_generation_visual_interaction_design_exploration_map.md
docs/research/038_mc0004_comparative_cockpit_design_synthesis_and_mockup_direction_set.md
```

Remaining major slices include:

```text
multi-axis status treatment
connector visual language
Port Grammar
semantic zoom
Internal Layout Grammar
stage/orientation system
Conversation Workspace
conversation + analytical coexistence
information-density lenses
runtime/waiting/approval visualization
focus/depth transitions
command architecture at scale
large-project grouping/layout
final design system
```

---

# Promoted Cockpit interaction architecture

```text
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
```

Specification 008 remains accepted and is not replaced by the current visual experiments.

---

# Source Universe route

```text
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
docs/foundations/022_source_universe_artifact_integrity_and_evidence_provenance_architecture.md
docs/research/034_durable_source_universe_and_evidence_substrate_architecture.md
docs/specifications/023_v1_source_universe_substrate.md
```

Current interpretation:

```text
SOURCE_SUBSTRATE_ACCEPTED
permanent deployment PAUSED
not cancelled or superseded
Course 2 gate unchanged
```

---

# Methodological knowledge-universe program

```text
docs/research/033_methodological_knowledge_universe_construction_framework.md
docs/methodological_knowledge/COVERAGE_MAP.md
```

The current Cockpit work is a deliberate frontend/product subtrack and does not replace the larger methodological program.
