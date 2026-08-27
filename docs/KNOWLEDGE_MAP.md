# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources and does not replace them.  
**Last reviewed:** 2026-08-27  
**Current checkpoint:** 226  
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
checkpoint                        226
active branch                     v1-cockpit-design-exploration
latest specification              Specification 024
promoted Cockpit baseline         Specification 008
current boundary                  connector directionality human review
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

Supporting evidence and prototype:

```text
docs/research/051_user_configurable_cockpit_visual_grammar_and_semantic_invariants.md
docs/research/052_configurable_cockpit_review_connector_geometry_fix_and_foundation_promotion.md
docs/checkpoints/224_user_configurable_cockpit_visual_grammar_prototype_opened.md
frontend/design-lab/work-unit-grammar-customizable.html
frontend/design-lab/work-unit-grammar-customizable.css
frontend/design-lab/work-unit-grammar-customizable.js
```

Production appearance persistence remains unresolved.

---

# Connector presentation result

Previous generic connector browser:

```text
frontend/design-lab/connector-grammar.html
frontend/design-lab/connector-grammar.css
frontend/design-lab/connector-grammar.js
frontend/design-lab/connector-port-layering.css
frontend/design-lab/connector-port-layering.js
```

Primary evidence:

```text
docs/research/053_connector_and_port_visual_grammar_experiment.md
docs/research/054_connector_composition_directionality_and_endpoint_layering_refinement.md
```

Human conclusion:

```text
no single K0-K4 winner is required
approved connector treatments should coexist as user-configurable presentation dimensions
```

Current interpretation:

```text
Rest attachment
    Clean
    Micro dots
    Frame sockets

Hover attachment emphasis
    Off
    On
```

Latest connector refinements:

```text
42ec63d17095753dc4ab97628cd859473cbdf5e8
    K1/K4 circular markers mostly outside the work-unit perimeter

183264bdd07783eaa2354894592f2cf4a076b6ec
    K2 active socket outline / glow follows relation color
```

---

# Foundation 024: composable connector presentation + semantic directionality

Promoted foundation:

```text
docs/foundations/024_composable_connector_presentation_and_semantic_directionality.md
```

Core principle:

```text
semantic relation model
    meaning and directionality governed by ADS / project state

connector presentation profile
    approved user-configurable visual choices
```

Critical invariant:

```text
appearance may change HOW direction is drawn
appearance may not change WHETHER a relation is directed
appearance may not reverse source and target
```

---

# Current Slice 02D: connector directionality

Governing research:

```text
docs/research/055_connector_presentation_configurability_and_directionality_browser_slice.md
```

Current checkpoint:

```text
docs/checkpoints/226_connector_presentation_made_configurable_directionality_review_opened.md
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
41bbdb75f338388f02a34fdf7dbac3ea90f86300
```

Direction states:

```text
D0  Undirected      A — B
D1  Forward         A -> B
D2  Reverse         A <- B
D3  Bidirectional   A <-> B
```

Presentation compatibility controls:

```text
Rest attachment             Clean / Micro dots / Frame sockets
Hover attachment emphasis   On / Off
Reduced motion              On / Off
```

The controls do not change semantic direction.

Final semantic relation classes remain open.

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
