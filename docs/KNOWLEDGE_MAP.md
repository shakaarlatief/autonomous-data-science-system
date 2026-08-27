# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources and does not replace them.  
**Last reviewed:** 2026-08-27  
**Current checkpoint:** 227  
**Active development branch:** `v1-cockpit-design-exploration`  
**Active PR:** none

## Start here

```text
README.md                         project overview and current stage
docs/CURRENT_STATE.md             exact present state and continuation
docs/KNOWLEDGE_MAP.md             routing/index layer
docs/current_routing.json         machine-readable routing metadata
docs/VISION.md                    high-level system direction
docs/PRINCIPLES.md                accepted high-level principles
docs/DEVELOPMENT_METHOD.md        canonical development method
docs/CONTINUITY.md                provider-neutral continuation procedure
```

Current route:

```text
checkpoint                        227
active branch                     v1-cockpit-design-exploration
latest specification              Specification 024
promoted Cockpit baseline         Specification 008
current boundary                  simplified arrow directionality human review
source-vault deployment           PAUSED, Course 2 gate unchanged
```

---

# Held Cockpit visual controls

## Grid/world

```text
G4 Adaptive Hybrid
Dark mode baseline
randomized travelling grid currents
quiet 100 px major-grid glints
ambient drift
localized semantic activity
```

Primary evidence:

```text
docs/research/039_phase_c_browser_rendered_design_experiment_protocol_and_grid_world_slice.md
docs/research/040_grid_world_g4_selection_dark_first_and_ambient_dynamics_exploration.md
docs/research/041_combined_g4_ambient_intensity_tuning.md
docs/research/042_g4_randomized_ambient_distribution_and_grid_intersection_glints.md
docs/research/043_g4_major_grid_glints_and_decoupled_ambient_cadence.md
```

## Work-unit interaction lighting

```text
H4 generic hover/outward response  sufficiently settled
Reduced in-box resting light       selected preferred working baseline
```

Primary evidence:

```text
docs/research/044_work_unit_interaction_lighting_hover_response_exploration.md
docs/research/045_h4_resting_node_light_world_spill_refinement.md
docs/research/047_work_unit_grammar_h4_control_correction_and_inbox_light_comparison.md
```

## Work-unit category markers

```text
Question / Blocker        circle
Investigation             square
Validation / Analysis     triangle
Model Work                diamond
Evaluation                plus
```

Primary convergence evidence:

```text
docs/research/046_work_unit_category_and_silhouette_visual_grammar_experiment.md
docs/research/048_claude_work_unit_grammar_synthesis_and_expanded_browser_round.md
docs/research/049_focused_work_unit_grammar_convergence_and_true_shape_experiment.md
docs/research/050_scientific_marker_selection_and_micro_material_shape_refinement.md
```

---

# Foundation 023: configurable Cockpit appearance

Promoted foundation:

```text
docs/foundations/023_user_configurable_cockpit_appearance_and_semantic_invariants.md
```

Core principle:

```text
semantic project model
    governed by ADS

presentation profile
    approved user-configurable appearance
```

Current proven work-unit appearance axes:

```text
Box shape       Normal / Subtle shapes
Micro design    None / Micro material / Micro light
```

---

# Connector treatment result

Primary generic-connector evidence:

```text
docs/research/053_connector_and_port_visual_grammar_experiment.md
docs/research/054_connector_composition_directionality_and_endpoint_layering_refinement.md
frontend/design-lab/connector-grammar.html
```

Current connector treatments:

```text
Clean
Micro dots
Frame sockets
Direction arrows
```

Human clarification:

```text
one terminal treatment normally active at a time
hover / focus is a separate reveal / emphasis mechanism
```

Therefore unnecessary mixed terminal stacks are not the default design direction.

Retained refinement commits:

```text
42ec63d17095753dc4ab97628cd859473cbdf5e8
    Micro-dot / hover-port circles mostly outside the work-unit perimeter

183264bdd07783eaa2354894592f2cf4a076b6ec
    Frame-socket active outline / glow follows relation color
```

---

# Foundation 024: connector treatment + semantic directionality

Refined foundation:

```text
docs/foundations/024_composable_connector_presentation_and_semantic_directionality.md
```

Current architecture:

```text
semantic relation model
    meaning and directionality governed by ADS / project state

connector treatment
    approved configurable terminal treatment
    normally one active treatment at a time

hover behavior
    orthogonal reveal / emphasis mechanism
```

Direction states:

```text
undirected
A -> B
A <- B
A <-> B
```

If arrows are used, their placement follows semantic direction exactly.

---

# Current Slice 02D: simplified arrow directionality

Governing research:

```text
docs/research/056_directionality_arrow_grammar_and_hover_separation_refinement.md
```

Current checkpoint:

```text
docs/checkpoints/227_directionality_arrow_grammar_simplified_human_review_opened.md
```

Browser route:

```text
frontend/design-lab/connector-directionality.html
frontend/design-lab/connector-directionality.css
frontend/design-lab/connector-directionality.js
```

Local URL:

```text
http://localhost:5173/design-lab/connector-directionality.html
```

Exact browser implementation target:

```text
07d573b6569b9f09a3b7e00936f3eadecee721b3
```

Controlled comparison:

```text
D0  Undirected      A - B
    no arrow

D1  Forward         A -> B
    K3-style arrow docked directly to B

D2  Reverse         A <- B
    same arrow docked directly to A

D3  Bidirectional   A <-> B
    same arrow at both endpoints
```

No dots or sockets are mixed into the directionality browser.

The arrow tip touches the exact rendered work-unit perimeter and follows H4 hover lift / release through the rendered-edge geometry system.

If human review accepts this grammar, directionality is sufficiently converged and the next slice is semantic relation classes.

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

No model-collaboration obligation is currently pending.

C5 Internal Layout Grammar remains deferred to semantic zoom / information-density work.

---

# Promoted Cockpit architecture

```text
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
docs/foundations/023_user_configurable_cockpit_appearance_and_semantic_invariants.md
docs/foundations/024_composable_connector_presentation_and_semantic_directionality.md
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
