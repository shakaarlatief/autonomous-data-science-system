# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources and does not replace them.  
**Last reviewed:** 2026-08-27  
**Current checkpoint:** 244  
**Active development branch:** `v1-cockpit-design-exploration`  
**Active PR:** none  
**Promoted V1 integration branch:** `v1-frontend-spike` at `ed5b60bdc882bed0799ce55228ce8187f9c55aa1`  
**Latest scientific experiment outcome:** `INCOMPLETE / EXECUTION INTEGRITY FAILED`

## Start here

```text
README.md
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/current_routing.json
docs/VISION.md
docs/PRINCIPLES.md
docs/DEVELOPMENT_METHOD.md
docs/CONTINUITY.md
```

Current route:

```text
checkpoint                        244
active branch                     v1-cockpit-design-exploration
latest specification              Specification 024
promoted Cockpit baseline         Specification 008
current boundary                  semantic zoom human review
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
X5 balanced contextual expansion without context recession
L0 Flat Fields provisional working default
Z7 Pull-Back Then Dive deep-focus entry
fullscreen specialist-workspace end state
compact topology compass retained
```

Important targets:

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
Z7 spatial deep focus         04616a52df5cceff6c59223bbd6f07448d027510
```

Foundations:

```text
docs/foundations/023_user_configurable_cockpit_appearance_and_semantic_invariants.md
docs/foundations/024_composable_connector_presentation_and_semantic_directionality.md
```

---

# Slice 02N: deep focus, current Phase-C direction settled

Primary evidence:

```text
docs/checkpoints/243_l0_working_default_deep_focus_transition_review_opened.md
docs/research/075_work_unit_deep_focus_transition_architecture_experiment.md
docs/research/076_claude_informed_factorized_deep_focus_transition_experiment.md
docs/research/077_fullscreen_specialist_workspace_and_spatial_zoom_transition_experiment.md
frontend/design-lab/work-unit-deep-focus-spatial-zoom.html
```

Current result:

```text
Z7 Pull-Back Then Dive
    selected

fullscreen specialist workspace
    selected current end-state direction

project grid / surrounding boxes
    absent in deep focus

compact topology compass
    retained
```

Positive non-selected evidence:

```text
Z2 World Falls Away
Z6 Perspective Corridor, especially 3D / 2.5D quality
```

---

# Current Slice 02O: semantic zoom

Primary evidence:

```text
docs/checkpoints/244_z7_deep_focus_accepted_semantic_zoom_review_opened.md
docs/research/078_project_world_semantic_zoom_level_of_detail_experiment.md
frontend/design-lab/work-unit-semantic-zoom.html
frontend/design-lab/work-unit-semantic-zoom.css
frontend/design-lab/work-unit-semantic-zoom.js
```

Local URL:

```text
http://localhost:5173/design-lab/work-unit-semantic-zoom.html
```

Initial browser target:

```text
65ac02326a75b1c9f056676819d2d1b7b23b74c5
```

Question:

```text
GEOMETRIC ZOOM
    physical / camera scale

SEMANTIC ZOOM
    what information survives, aggregates, disappears or becomes richer by scale?
```

Candidates:

```text
S0  Geometric Control
S1  Progressive Detail
S2  Stage Clusters
S3  Topology First
S4  Focus Preserving
S5  Status First
S6  Glyph Field
S7  Hybrid Contextual
S8  Local Detail Lens
```

Each is shown at provisional Overview, Work and Inspection scales.

S7 is only a browser default. No semantic-zoom candidate has been selected.

---

# Earlier Phase-C evidence routes

```text
docs/research/068_runtime_tag_motion_clean_perimeter_alternatives.md
docs/research/070_shared_operational_status_carrier_blocker_relationship_and_work_unit_detail_deferment.md
docs/research/071_work_unit_attention_priority_visual_grammar_experiment.md
docs/research/072_work_unit_selection_persistent_state_visual_grammar_experiment.md
docs/research/073_work_unit_contextual_detail_expansion_architecture_experiment.md
docs/research/074_work_unit_internal_layout_grammar_experiment.md
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

Current interpretation:

```text
SOURCE_SUBSTRATE_ACCEPTED
permanent deployment PAUSED
not cancelled or superseded
Course 2 gate unchanged
```