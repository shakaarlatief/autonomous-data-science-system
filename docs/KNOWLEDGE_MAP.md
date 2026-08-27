# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources and does not replace them.  
**Last reviewed:** 2026-08-27  
**Current checkpoint:** 243  
**Active development branch:** `v1-cockpit-design-exploration`  
**Active PR:** none  
**Promoted V1 integration branch:** `v1-frontend-spike` at `ed5b60bdc882bed0799ce55228ce8187f9c55aa1`  
**Latest scientific experiment outcome:** `INCOMPLETE / EXECUTION INTEGRITY FAILED`

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
checkpoint                        243
active branch                     v1-cockpit-design-exploration
latest specification              Specification 024
promoted Cockpit baseline         Specification 008
current boundary                  deep-focus transition human review
source-vault deployment           PAUSED, Course 2 gate unchanged
```

---

# Repository preservation / development-method route

```text
docs/checkpoints/README.md
scripts/check_checkpoint_metadata.py
.github/workflows/checkpoint-metadata.yml
scripts/check_current_routing.py
.github/workflows/current-routing-consistency.yml
docs/research/064_rapid_iteration_repository_preservation_audit_and_checkpoint_hygiene.md
```

Current audit result:

```text
architecture                  SOUND
metadata/provenance repair    PRESERVED
micro-checkpointing rule      HARDENED
checkpoint validation gate    HARDENED
routing push validation       HARDENED
new knowledge subsystem       NOT JUSTIFIED
```

---

# Held Cockpit visual and semantic controls

```text
G4 Adaptive Hybrid world
Dark mode baseline
H4 hover/outward response
Reduced in-box resting light
scientific category-marker grammar
E5 Hue + Tag relation-class carrier
P7 Neutral Tag + Tone disposition
editable current-process focus set
conditional runtime semantics
switchable runtime carrier with T7 Soft Shade
BLOCKER -> BLOCKS -> BLOCKED cause/effect model
BLOCKED sharper compact ring
FAIL smoother circular compact ring
A3 Signal Bars for HIGH attention
SEL2 Corner Brackets for persistent selection
X5 balanced two-axis contextual expansion without context recession
```

Foundations:

```text
docs/foundations/023_user_configurable_cockpit_appearance_and_semantic_invariants.md
docs/foundations/024_composable_connector_presentation_and_semantic_directionality.md
```

Important accepted targets:

```text
directionality                07d573b6569b9f09a3b7e00936f3eadecee721b3
relation class E5             497e81f06ba1f9901511449237d1bb9f96b2d108
P7 disposition                fac1db37af4225927d6c799e37418a3ad9c42c13
editable current focus        da115b74de526fca05ed6f468bef39bdb801355c
T7 Soft Shade                 08534f94c2f272f969159087de2797a23e36b330
switchable runtime            fb847bd65ff6e5e4203a89ee2d4f74b7187c8359
BLOCKED/status carrier        88fd3c3cfe7a1eff4664afde06341b7b654c97f4
A3 attention priority         767c66f76974d3c0a851de0dfa17c502817a4b12
SEL2 persistent selection     e7304fe834d86166d843fda7e1df0f4ddb1f793a
X5 contextual expansion       94bc1100b7388cc56497cafc03051ce326424a80
```

---

# Slice 02M: internal layout, deferred

```text
docs/checkpoints/242_x5_two_axis_expansion_accepted_internal_layout_review_opened.md
docs/research/074_work_unit_internal_layout_grammar_experiment.md
frontend/design-lab/work-unit-internal-layout.html
```

```text
L0 Flat Fields
    provisional working default

L1-L8
    preserved for later review
    not rejected
```

---

# Current Slice 02N: fullscreen spatial deep-focus transition

Checkpoint:

```text
docs/checkpoints/243_l0_working_default_deep_focus_transition_review_opened.md
```

Evidence progression:

```text
Research 075
    docs/research/075_work_unit_deep_focus_transition_architecture_experiment.md
    frontend/design-lab/work-unit-deep-focus-transition.html
    repaired target afd15f52897a295788dc3a1d04b2d1b31ef707f9

Research 076
    docs/research/076_claude_informed_factorized_deep_focus_transition_experiment.md
    frontend/design-lab/work-unit-deep-focus-factorized.html
    latest target fddb344c2b18221d326c9ba5bde98e84edf98f56

Research 077
    docs/research/077_fullscreen_specialist_workspace_and_spatial_zoom_transition_experiment.md
    frontend/design-lab/work-unit-deep-focus-spatial-zoom.html
    exact target b375eb253990ce3c20f34dd9d5b735bd532789f2
```

Claude collaboration evidence:

```text
docs/model_collaboration/threads/MC-0004/messages/005_chatgpt_deep_focus_transition_divergent_ideation_request.md
docs/model_collaboration/threads/MC-0004/messages/006_claude_deep_focus_transition_divergent_ideation.md
Claude response commit  204664ae1e732dd504174bbc62545e9a93adc85f
```

Claude's decomposition remains useful:

```text
object continuity
context retention
context relevance
entry choreography
orientation aid
return choreography
```

Latest human refinement:

```text
deepest specialist workspace
    should own the full active stage

project map / grid
    should disappear fully after entry

compact topology compass
    strongly liked as a small orientation detail

transition
    should explore stronger spatial zoom / moving-through-space behavior
```

Current local URL:

```text
http://localhost:5173/design-lab/work-unit-deep-focus-spatial-zoom.html
```

Current candidates:

```text
Z0  Direct Replace Control
Z1  Card Zoom-In
Z2  World Falls Away
Z3  Camera Dive
Z4  Workspace Aperture
Z5  Depth Parallax
Z6  Perspective Corridor
Z7  Pull-Back Then Dive
```

All candidates hold the final deep-focus end state constant:

```text
fullscreen specialist workspace
no visible project grid / map
compact topology compass retained
```

Current human gate:

```text
compare Z0-Z7
judge which feels like entering the selected work unit
judge spatial depth versus disorientation
judge repeated-use comfort
judge aperture / portal continuity
judge whether pull-back before dive helps
judge whether the compact compass is sufficient after the map disappears
prefer / reject / combine / refine
```

---

# Earlier Phase-C evidence routes

```text
docs/research/068_runtime_tag_motion_clean_perimeter_alternatives.md
docs/research/070_shared_operational_status_carrier_blocker_relationship_and_work_unit_detail_deferment.md
docs/research/071_work_unit_attention_priority_visual_grammar_experiment.md
docs/research/072_work_unit_selection_persistent_state_visual_grammar_experiment.md
docs/research/073_work_unit_contextual_detail_expansion_architecture_experiment.md
```

---

# MC-0004 collaboration route

```text
docs/model_collaboration/threads/MC-0004/BRIEF.md
docs/model_collaboration/threads/MC-0004/THREAD.md
docs/model_collaboration/threads/MC-0004/STATE.json
docs/model_collaboration/REVIEW_INBOX.md
```

No model-collaboration obligation is currently pending.

---

# Promoted Cockpit architecture

```text
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
docs/foundations/021_professional_product_interface_and_frontend_design_foundation.md
docs/foundations/023_user_configurable_cockpit_appearance_and_semantic_invariants.md
docs/foundations/024_composable_connector_presentation_and_semantic_directionality.md
```

Specification 008 remains accepted and is not replaced by current browser experiments.

---

# Source Universe route

```text
docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md
docs/foundations/022_source_universe_artifact_integrity_and_evidence_provenance_architecture.md
docs/research/034_durable_source_universe_and_evidence_substrate_architecture.md
docs/specifications/023_v1_source_universe_substrate.md
```

```text
SOURCE_SUBSTRATE_ACCEPTED
permanent deployment PAUSED
not cancelled or superseded
Course 2 gate unchanged
```
