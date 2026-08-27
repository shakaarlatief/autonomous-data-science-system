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

Primary evidence:

```text
docs/checkpoints/242_x5_two_axis_expansion_accepted_internal_layout_review_opened.md
docs/research/074_work_unit_internal_layout_grammar_experiment.md
frontend/design-lab/work-unit-internal-layout.html
```

Candidates remain preserved:

```text
L0  Flat Fields
L1  Structured Grid
L2  Narrative Stack
L3  Summary + Rail
L4  Action First
L5  Dependency Path
L6  Evidence Center
L7  Module Cards
L8  Balanced Instrument
```

Current disposition:

```text
L0 Flat Fields
    provisional working default
    sufficient to continue Phase C
    NOT a final C5 or work-unit-schema decision

L1-L8
    preserved for later review
    not rejected
```

---

# Current Slice 02N: factorized deep-focus transition

Checkpoint:

```text
docs/checkpoints/243_l0_working_default_deep_focus_transition_review_opened.md
```

Original transition evidence:

```text
docs/research/075_work_unit_deep_focus_transition_architecture_experiment.md
frontend/design-lab/work-unit-deep-focus-transition.html
exact repaired target  afd15f52897a295788dc3a1d04b2d1b31ef707f9
```

Claude collaboration evidence:

```text
docs/model_collaboration/threads/MC-0004/messages/005_chatgpt_deep_focus_transition_divergent_ideation_request.md
docs/model_collaboration/threads/MC-0004/messages/006_claude_deep_focus_transition_divergent_ideation.md
Claude response commit  204664ae1e732dd504174bbc62545e9a93adc85f
```

Claude's main decomposition:

```text
object continuity
context retention
context relevance
entry choreography
orientation aid
return choreography
```

Current synthesis evidence:

```text
docs/research/076_claude_informed_factorized_deep_focus_transition_experiment.md
frontend/design-lab/work-unit-deep-focus-factorized.html
frontend/design-lab/work-unit-deep-focus-factorized.css
frontend/design-lab/work-unit-deep-focus-factorized-refinement.css
frontend/design-lab/work-unit-deep-focus-factorized.js
```

Local URL:

```text
http://localhost:5173/design-lab/work-unit-deep-focus-factorized.html
```

Exact current browser target:

```text
0390d8fef9d6647ae17ecd7c948159d0a5b603e5
```

Current comparisons:

```text
Batch A · Object continuity
    A0  F2 Anchored Morph Control
    A1  Anchored Center Stage
    A2  Anchored Context Rail
    A3  Camera Push-Through

Batch B · Context relevance
    B0  F6 Fixed Rail Control
    B1  Neighbor-Aware Context
    B2  Neighbor-Aware + Anchor

Batch C · Staging and orientation
    C0  Hard Replace Control
    C1  Staged Two-Step Entry
    C2  Compass + Soft World
    C3  Hard Replace + Compass

Large interaction studio
    Symmetric return
    Fast return
```

T6 Adaptive Retention by Workspace Type remains preserved but deferred.

Current human gate:

```text
review Batch A for source-object continuity
review Batch B for relevant versus arbitrary retained context
review Batch C for staging and minimal orientation
compare symmetric versus fast return
select mechanisms independently
combine later where useful
keep specialist-workspace internals schematic
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

Current interpretation:

```text
SOURCE_SUBSTRATE_ACCEPTED
permanent deployment PAUSED
not cancelled or superseded
Course 2 gate unchanged
```