# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources and does not replace them.  
**Last reviewed:** 2026-08-27  
**Current checkpoint:** 234  
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
checkpoint                        234
active branch                     v1-cockpit-design-exploration
latest specification              Specification 024
promoted Cockpit baseline         Specification 008
current boundary                  user-curated current-process focus-set human review
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

Foundation 024:

```text
docs/foundations/024_composable_connector_presentation_and_semantic_directionality.md
```

---

# Connector treatment and relation semantics

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

# Project-disposition result

Primary evidence:

```text
docs/research/059_work_unit_project_disposition_visual_grammar_experiment.md
docs/research/060_disposition_hybrid_refinement_and_mixed_category_practical_comparison.md
docs/research/061_project_disposition_neutral_tag_tone_convergence_refinement.md
frontend/design-lab/work-unit-disposition-grammar.html
```

Human-selected current Phase-C direction:

```text
P7  Neutral Tag + Tone

REST
    category color remains dominant
    disposition tag remains neutral
    Completed / Deferred / Future use selective tonal recession

HOVER
    disposition tag reveals state-specific hue
```

Latest accepted P7 implementation before opening the focus-lens slice:

```text
fac1db37af4225927d6c799e37418a3ad9c42c13
```

P4 State Rhythm and earlier colored alternatives remain preserved as experiment/history evidence.

The final project-disposition ontology remains unfrozen.

---

# Current Slice 02G: current-process focus lens and editable focus set

Primary evidence:

```text
docs/research/062_current_process_focus_lens_and_context_suppression_experiment.md
docs/research/063_user_curated_current_process_focus_membership.md
```

Current checkpoint:

```text
docs/checkpoints/234_user_curated_current_process_focus_set_review_opened.md
```

Browser route:

```text
frontend/design-lab/work-unit-process-focus.html
frontend/design-lab/work-unit-process-focus.css
frontend/design-lab/work-unit-process-focus.js
```

Local URL:

```text
http://localhost:5173/design-lab/work-unit-process-focus.html
```

Exact implementation target:

```text
da115b74de526fca05ed6f468bef39bdb801355c
```

Semantic separation:

```text
work-unit existence         whether the work unit exists in the project
project disposition         semantic state of the work unit
current-focus membership    whether it belongs to the emphasized process set
view emphasis               how strongly work outside the focus is suppressed
```

Lens modes:

```text
Context visible
    accepted P7 treatment remains readable

Focus current process
    in-focus nodes remain full salience
    outside-focus nodes are strongly suppressed
    contextual connector segments recede
    suppressed nodes partially recover on hover
```

Editable membership:

```text
Edit focus set
    reveal per-node membership controls

+ FOCUS
    add node to current focus

- FOCUS
    remove node from current focus

Reset example
    restore the example fixture
```

Membership changes immediately update node suppression, membership counts and connector current/context classification.

Browser `localStorage` is used only as prototype convenience. Final focus-set ownership, persistence, automatic suggestions and multiple named lenses remain open.

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
