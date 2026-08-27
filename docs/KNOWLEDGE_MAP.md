# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources and does not replace them.  
**Last reviewed:** 2026-08-27  
**Current checkpoint:** 228  
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
checkpoint                        228
active branch                     v1-cockpit-design-exploration
latest specification              Specification 024
promoted Cockpit baseline         Specification 008
current boundary                  semantic relation-class visual grammar human review
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

## Work-unit category markers

```text
Question / Blocker        circle
Investigation             square
Validation / Analysis     triangle
Model Work                diamond
Evaluation                plus
```

---

# Foundation 023: configurable Cockpit appearance

Promoted foundation:

```text
docs/foundations/023_user_configurable_cockpit_appearance_and_semantic_invariants.md
```

Current proven work-unit appearance axes:

```text
Box shape       Normal / Subtle shapes
Micro design    None / Micro material / Micro light
```

---

# Connector treatment and directionality result

Primary connector evidence:

```text
docs/research/053_connector_and_port_visual_grammar_experiment.md
docs/research/054_connector_composition_directionality_and_endpoint_layering_refinement.md
docs/research/056_directionality_arrow_grammar_and_hover_separation_refinement.md
frontend/design-lab/connector-grammar.html
frontend/design-lab/connector-directionality.html
```

Current connector treatments:

```text
Clean
Micro dots
Frame sockets
Direction arrows
```

Current architecture:

```text
one terminal treatment normally active at a time
hover / focus is a separate reveal / emphasis mechanism
directionality is system-owned semantics
```

Accepted direction grammar:

```text
Undirected      A - B       no arrow
Forward         A -> B      arrow at B
Reverse         A <- B      same arrow at A
Bidirectional   A <-> B     same arrow at both endpoints
```

Exact accepted directionality implementation:

```text
07d573b6569b9f09a3b7e00936f3eadecee721b3
```

Promoted foundation:

```text
docs/foundations/024_composable_connector_presentation_and_semantic_directionality.md
```

---

# Current Slice 02E: semantic relation-class visual grammar

Governing research:

```text
docs/research/057_semantic_relation_class_visual_grammar_experiment.md
```

Current checkpoint:

```text
docs/checkpoints/228_directionality_settled_relation_class_grammar_review_opened.md
```

Browser route:

```text
frontend/design-lab/relation-class-grammar.html
frontend/design-lab/relation-class-grammar.css
frontend/design-lab/relation-class-grammar.js
```

Local URL:

```text
http://localhost:5173/design-lab/relation-class-grammar.html
```

Exact browser implementation target:

```text
9ac3a0a0f51c024d0deec2fe54f11735f4cdd0fb
```

Representative visual-test relation classes:

```text
R0  Chronology / Sequence
R1  Dependency / Prerequisite
R2  Causal / Influence
R3  Evidence / Support
R4  Lineage / Derivation
```

These are provisional fixtures, not a frozen ADS ontology.

Encoding families:

```text
E0  Neutral Control
E1  Semantic Hue
E2  Stroke Rhythm
E3  Explicit Tag
E4  Hue + Stroke
E5  Hue + Tag
E6  Restrained Hybrid
```

Direction is held constant as `A -> B` to isolate semantic relation class.

Runtime-flow relations remain outside this first semantic-class slice.

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
