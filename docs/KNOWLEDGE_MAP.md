# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources and does not replace them.  
**Last reviewed:** 2026-08-27  
**Current checkpoint:** 231  
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
checkpoint                        231
active branch                     v1-cockpit-design-exploration
latest specification              Specification 024
promoted Cockpit baseline         Specification 008
current boundary                  refined P6 vs P7 project-disposition mixed-category human review
source-vault deployment           PAUSED, Course 2 gate unchanged
```

---

# Held Cockpit visual controls

```text
G4 Adaptive Hybrid world
Dark mode baseline
H4 generic hover/outward response
Reduced in-box resting light
```

Current work-unit category markers:

```text
Question / Blocker        circle
Investigation             square
Validation / Analysis     triangle
Model Work                diamond
Evaluation                plus
```

Foundation 023:

```text
docs/foundations/023_user_configurable_cockpit_appearance_and_semantic_invariants.md
```

Current proven work-unit appearance axes:

```text
Box shape       Normal / Subtle shapes
Micro design    None / Micro material / Micro light
```

---

# Connector treatment and relation semantics

Primary evidence:

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

Accepted direction grammar:

```text
Undirected      no arrow
Forward         arrow at B
Reverse         same arrow at A
Bidirectional   same arrow at both endpoints
```

Exact accepted directionality implementation:

```text
07d573b6569b9f09a3b7e00936f3eadecee721b3
```

Foundation 024:

```text
docs/foundations/024_composable_connector_presentation_and_semantic_directionality.md
```

Relation-class result:

```text
E5  Hue + Tag
    SELECTED / sufficiently settled for current Phase C
```

Latest accepted relation-class implementation:

```text
497e81f06ba1f9901511449237d1bb9f96b2d108
```

Stroke rhythm remains preserved for another future line-level semantic dimension and currently has no semantic assignment.

---

# Current Slice 02F: work-unit project disposition

Primary evidence:

```text
docs/research/059_work_unit_project_disposition_visual_grammar_experiment.md
docs/research/060_disposition_hybrid_refinement_and_mixed_category_practical_comparison.md
```

Current checkpoint:

```text
docs/checkpoints/231_disposition_hybrid_refined_mixed_category_comparison_opened.md
```

Browser route:

```text
frontend/design-lab/work-unit-disposition-grammar.html
frontend/design-lab/work-unit-disposition-grammar.css
frontend/design-lab/work-unit-disposition-grammar.js
```

Local URL:

```text
http://localhost:5173/design-lab/work-unit-disposition-grammar.html
```

Exact refined browser implementation target:

```text
2056bb31d7cb90766e112bc26aaf7339fb568242
```

Semantic separation:

```text
category               WHAT IS THIS?
project disposition    current slice
runtime state          held out
importance / priority  held out
```

Representative visual-test dispositions:

```text
Active / Current
Recommended / Next
Deferred
Completed
Blocked
Future / Not yet active
```

Initial P0-P5 families remain inspectable. Human refinement now focuses on:

```text
P6  Hue + Colored Tag + Tone
    perimeter hue + colored tag + selective tone
    no rhythm

P7  Colored Tag + Tone
    colored tag + same selective tone
    no disposition perimeter hue
    no rhythm
```

P4 State Rhythm remains preserved as standalone experiment evidence.

The page includes a side-by-side practical project fixture where P6 and P7 are rendered across Question, Investigation, Validation, Model and Evaluation categories. This is the current test for category/disposition color conflict.

---

# MC-0004 collaboration route

```text
docs/model_collaboration/threads/MC-0004/BRIEF.md
docs/model_collaboration/threads/MC-0004/THREAD.md
docs/model_collaboration/threads/MC-0004/STATE.json
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
