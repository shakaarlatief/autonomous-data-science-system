# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources and does not replace them.  
**Last reviewed:** 2026-08-27  
**Current checkpoint:** 242  
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
checkpoint                        242
active branch                     v1-cockpit-design-exploration
latest specification              Specification 024
promoted Cockpit baseline         Specification 008
current boundary                  expanded work-unit internal layout human review
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

Foundations:

```text
docs/foundations/023_user_configurable_cockpit_appearance_and_semantic_invariants.md
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
```

Latest accepted relation-class implementation:

```text
497e81f06ba1f9901511449237d1bb9f96b2d108
```

Stroke rhythm remains reserved for a future orthogonal line-level semantic dimension.

---

# Project disposition and current-process focus

Primary disposition evidence:

```text
docs/research/059_work_unit_project_disposition_visual_grammar_experiment.md
docs/research/060_disposition_hybrid_refinement_and_mixed_category_practical_comparison.md
docs/research/061_project_disposition_neutral_tag_tone_convergence_refinement.md
```

Human-selected current Phase-C direction:

```text
P7  Neutral Tag + Tone
```

Latest accepted P7 implementation:

```text
fac1db37af4225927d6c799e37418a3ad9c42c13
```

Current-process focus evidence:

```text
docs/research/062_current_process_focus_lens_and_context_suppression_experiment.md
docs/research/063_user_curated_current_process_focus_membership.md
frontend/design-lab/work-unit-process-focus.html
```

Human-accepted current direction:

```text
Context visible
Focus current process
Edit focus set
Reset example
```

Exact accepted editable-focus implementation:

```text
da115b74de526fca05ed6f468bef39bdb801355c
```

---

# Slice 02H: conditional runtime carrier

Evidence:

```text
docs/research/065_work_unit_runtime_state_visual_grammar_experiment.md
docs/research/066_conditional_runtime_state_and_project_disposition_semantic_correction.md
docs/research/067_switchable_runtime_carrier_convergence_and_r1_r5_verification.md
docs/research/068_runtime_tag_motion_clean_perimeter_alternatives.md
```

Runtime remains conditional.

```text
No runtime
    no current execution/work episode exists

Idle runtime
    an execution episode exists but is doing nothing
```

Accepted current Phase-C carrier architecture:

```text
Dot + dynamic ring
or
T7 Soft Shade tag
```

Exact accepted T7 motion-browser target:

```text
08534f94c2f272f969159087de2797a23e36b330
```

Exact switchable-runtime browser with T7 integrated:

```text
fb847bd65ff6e5e4203a89ee2d4f74b7187c8359
```

---

# Slice 02I: BLOCKED carrier and blocker relationship

Primary evidence:

```text
docs/research/069_blocked_as_orthogonal_progress_constraint_visual_grammar_experiment.md
docs/research/070_shared_operational_status_carrier_blocker_relationship_and_work_unit_detail_deferment.md
frontend/design-lab/work-unit-blocked-carrier.html
```

Accepted current Phase-C semantic distinction:

```text
BLOCKER    cause / unresolved work or dependency
BLOCKS     relation from cause to affected work
BLOCKED    resulting current progress constraint
FAIL       failed current execution attempt
```

Accepted compact red mapping:

```text
BLOCKED    sharper non-circular dynamic ring
FAIL       smoother circular dynamic ring
```

Exact accepted visual target:

```text
88fd3c3cfe7a1eff4664afde06341b7b654c97f4
```

---

# Slice 02J: attention priority result

Primary evidence:

```text
docs/research/071_work_unit_attention_priority_visual_grammar_experiment.md
frontend/design-lab/work-unit-attention-priority.html
```

Human-selected current Phase-C direction:

```text
A3  Signal Bars
```

Exact browser target in which A3 was selected:

```text
767c66f76974d3c0a851de0dfa17c502817a4b12
```

The final priority ontology, ownership and relationship to relevance/scheduling remain open.

---

# Slice 02K: persistent selection result

Primary evidence:

```text
docs/checkpoints/240_attention_priority_a3_accepted_selection_state_review_opened.md
docs/research/072_work_unit_selection_persistent_state_visual_grammar_experiment.md
frontend/design-lab/work-unit-selection-state.html
```

The first browser had a clipping defect for external selection geometry. The repaired implementation moved the selection carrier outside `.node-surface` while preserving surface clipping for internal effects.

Exact repaired visual target:

```text
e7304fe834d86166d843fda7e1df0f4ddb1f793a
```

Human-selected current Phase-C direction:

```text
SEL2  Corner Brackets
```

---

# Slice 02L: contextual work-unit detail expansion result

Primary evidence:

```text
docs/checkpoints/241_selection_sel2_accepted_contextual_detail_expansion_review_opened.md
docs/research/073_work_unit_contextual_detail_expansion_architecture_experiment.md
frontend/design-lab/work-unit-detail-expansion.html
frontend/design-lab/work-unit-detail-expansion-x5-accepted.css
frontend/design-lab/work-unit-detail-expansion-x5-accepted.js
```

Human-selected current Phase-C direction:

```text
X5 balanced two-axis expansion
WITHOUT surrounding-context recession
```

Accepted geometry:

```text
390 x 210
one integrated work-unit object
balanced width + height growth
surrounding map remains at normal salience
```

Exact refined X5 implementation target:

```text
94bc1100b7388cc56497cafc03051ce326424a80
```

The original X5 context-recession mechanism remains historical evidence only.

---

# Current Slice 02M: expanded work-unit internal layout

Primary evidence:

```text
docs/checkpoints/242_x5_two_axis_expansion_accepted_internal_layout_review_opened.md
docs/research/074_work_unit_internal_layout_grammar_experiment.md
frontend/design-lab/work-unit-internal-layout.html
frontend/design-lab/work-unit-internal-layout.css
frontend/design-lab/work-unit-internal-layout.js
```

Local URL:

```text
http://localhost:5173/design-lab/work-unit-internal-layout.html
```

Exact initial browser implementation target:

```text
871075bcda8ff812e1a96b18b442c803d5da7faf
```

Held outer geometry:

```text
X5 two-axis expansion
390 x 210
NO surrounding-context recession
```

Candidate internal layouts:

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

Controlled placeholder payload:

```text
Purpose
Constraint
Evidence
Next action
Blocking cause
Recent activity
```

The payload is not a frozen work-unit schema.

Current human gate:

```text
compare L0-L8 with outer geometry held constant
judge scan path, hierarchy and density
reject miniature-dashboard behavior
inspect robustness to longer content
inspect future room for provenance/evidence and commands
prefer / reject / combine / refine
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
