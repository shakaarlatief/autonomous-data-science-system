# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources and does not replace them.  
**Last reviewed:** 2026-08-27  
**Current checkpoint:** 240  
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
checkpoint                        240
active branch                     v1-cockpit-design-exploration
latest specification              Specification 024
promoted Cockpit baseline         Specification 008
current boundary                  persistent work-unit selection human review
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
Checkpoints 223-234           metadata/provenance repaired
metadata validator            PASS after repair
micro-checkpointing rule      HARDENED
checkpoint validation gate    HARDENED
routing push validation       HARDENED
new knowledge subsystem       NOT JUSTIFIED
```

Verified metadata-validation repair point:

```text
d2541418a68b9bfd244ec89e4e951e630b3bb61b
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
Question / Blocker        circle / yellow
Investigation             square / green
Validation / Analysis     triangle / blue
Model Work                diamond / red
Evaluation                plus / purple
```

Durable visual foundations:

```text
docs/foundations/023_user_configurable_cockpit_appearance_and_semantic_invariants.md
docs/foundations/024_composable_connector_presentation_and_semantic_directionality.md
```

---

# Connector and relation results

Accepted direction grammar:

```text
Undirected      no arrow
Forward         arrow at B
Reverse         same arrow at A
Bidirectional   same arrow at both endpoints
```

Exact accepted directionality target:

```text
07d573b6569b9f09a3b7e00936f3eadecee721b3
```

Relation-class result:

```text
E5  Hue + Tag
    SELECTED / sufficiently settled for current Phase C
```

Latest accepted relation-class target:

```text
497e81f06ba1f9901511449237d1bb9f96b2d108
```

Stroke rhythm remains preserved for another future line-level semantic dimension and currently has no semantic assignment.

---

# Project disposition and current-process focus

Primary disposition evidence:

```text
docs/research/059_work_unit_project_disposition_visual_grammar_experiment.md
docs/research/060_disposition_hybrid_refinement_and_mixed_category_practical_comparison.md
docs/research/061_project_disposition_neutral_tag_tone_convergence_refinement.md
frontend/design-lab/work-unit-disposition-grammar.html
```

Accepted current Phase-C disposition direction:

```text
P7  Neutral Tag + Tone
```

Exact accepted P7 target:

```text
fac1db37af4225927d6c799e37418a3ad9c42c13
```

Current-process focus evidence:

```text
docs/research/062_current_process_focus_lens_and_context_suppression_experiment.md
docs/research/063_user_curated_current_process_focus_membership.md
frontend/design-lab/work-unit-process-focus.html
```

Accepted direction:

```text
Context visible
Focus current process
Edit focus set
Reset example
```

Exact accepted editable-focus target:

```text
da115b74de526fca05ed6f468bef39bdb801355c
```

---

# Runtime and operational-status route

Runtime evidence:

```text
docs/research/065_work_unit_runtime_state_visual_grammar_experiment.md
docs/research/066_conditional_runtime_state_and_project_disposition_semantic_correction.md
docs/research/067_switchable_runtime_carrier_convergence_and_r1_r5_verification.md
docs/research/068_runtime_tag_motion_clean_perimeter_alternatives.md
docs/checkpoints/236_runtime_state_made_conditional_human_review_reopened.md
docs/checkpoints/237_switchable_runtime_carrier_convergence_review_opened.md
```

Runtime remains conditional / episode-scoped.

Accepted current Phase-C carrier architecture:

```text
Dot + dynamic ring
or
T7 Soft Shade runtime tag
```

Exact accepted T7 target:

```text
08534f94c2f272f969159087de2797a23e36b330
```

Exact switchable-runtime browser with T7 integrated:

```text
fb847bd65ff6e5e4203a89ee2d4f74b7187c8359
```

BLOCKED evidence:

```text
docs/research/069_blocked_as_orthogonal_progress_constraint_visual_grammar_experiment.md
docs/research/070_shared_operational_status_carrier_blocker_relationship_and_work_unit_detail_deferment.md
docs/checkpoints/238_runtime_carrier_accepted_blocked_progress_constraint_review_opened.md
frontend/design-lab/work-unit-blocked-carrier.html
```

Current semantic distinction:

```text
BLOCKER  cause
BLOCKS   relation
BLOCKED  affected work cannot proceed
FAIL     failed current execution attempt
```

Accepted compact red mapping:

```text
BLOCKED    sharper non-circular dynamic ring
FAIL       smoother circular dynamic ring
```

Exact accepted BLOCKED/status target:

```text
88fd3c3cfe7a1eff4664afde06341b7b654c97f4
```

---

# Slice 02J result: attention priority

Primary evidence:

```text
docs/research/071_work_unit_attention_priority_visual_grammar_experiment.md
docs/checkpoints/239_shared_blocked_carrier_accepted_attention_priority_review_opened.md
frontend/design-lab/work-unit-attention-priority.html
```

Human-selected current Phase-C direction:

```text
A3  Signal Bars

HIGH attention
    three ascending micro-bars
    near the upper-right work-unit frame
```

Exact reviewed browser target:

```text
767c66f76974d3c0a851de0dfa17c502817a4b12
```

The final priority ontology, scale, ownership, persistence and relationship to relevance/scheduling remain unfrozen.

---

# Current Slice 02K: persistent work-unit selection

Primary evidence:

```text
docs/research/072_work_unit_selection_persistent_state_visual_grammar_experiment.md
docs/checkpoints/240_attention_priority_a3_accepted_selection_state_review_opened.md
frontend/design-lab/work-unit-selection-state.html
frontend/design-lab/work-unit-selection-state.css
frontend/design-lab/work-unit-selection-state.js
```

Local URL:

```text
http://localhost:5173/design-lab/work-unit-selection-state.html
```

Exact browser implementation target:

```text
3bac1fea4ca820c89a7bc4516497a4c33164ec5d
```

Bounded concept:

```text
SELECTION
    which work unit has the user explicitly chosen for inspection or action?
```

Selection remains separate from:

```text
hover
keyboard focus
current-process focus membership
attention priority
deep-focus / specialist-workspace entry
```

Candidate treatments:

```text
SEL0  Neutral Control
SEL1  Outer Keyline
SEL2  Corner Brackets
SEL3  Inner Frame
SEL4  Edge Ticks
SEL5  Selection Plate
SEL6  Soft Contour
SEL7  Double Corner
SEL8  Keyline + Corners
```

The practical scene supports click selection, keyboard selection through Enter / Space, and Clear selection while keeping H4 hover transient.

---

# Work-unit expansion route

The preserved future hierarchy remains:

```text
compact map work unit
    -> expanded contextual/detail card
    -> full specialist workspace / deep focus
```

The intermediate expanded-card level remains unfrozen and is intentionally deferred until persistent selection converges. It should later be tested with semantic zoom, C5 Internal Layout Grammar, information-density and work-unit detail/provenance presentation.

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

Specification 008 remains accepted and is not replaced by current Phase-C visual experiments.

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
