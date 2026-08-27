# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources and does not replace them.  
**Last reviewed:** 2026-08-27  
**Current checkpoint:** 241  
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
checkpoint                        241
active branch                     v1-cockpit-design-exploration
latest specification              Specification 024
promoted Cockpit baseline         Specification 008
current boundary                  contextual work-unit detail expansion human review
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

Meaning under current test:

```text
HIGH attention
    three ascending micro-bars
    near upper-right frame
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
frontend/design-lab/work-unit-selection-state.css
frontend/design-lab/work-unit-selection-state.js
```

The first browser had a clipping defect for external selection geometry. The repaired implementation moved the selection carrier outside `.node-surface` while preserving surface clipping for internal effects.

Exact repaired visual target:

```text
e7304fe834d86166d843fda7e1df0f4ddb1f793a
```

Human-selected current Phase-C direction:

```text
SEL2  Corner Brackets

SELECTED
    four compact neutral-cool corner brackets
    outside the rendered work-unit frame
    persistent after pointer exit
```

Selection remains separate from hover, keyboard focus, current-process focus membership, attention priority and deep focus.

---

# Current Slice 02L: contextual work-unit detail expansion

Primary evidence:

```text
docs/checkpoints/241_selection_sel2_accepted_contextual_detail_expansion_review_opened.md
docs/research/073_work_unit_contextual_detail_expansion_architecture_experiment.md
frontend/design-lab/work-unit-detail-expansion.html
frontend/design-lab/work-unit-detail-expansion.css
frontend/design-lab/work-unit-detail-expansion.js
```

Local URL:

```text
http://localhost:5173/design-lab/work-unit-detail-expansion.html
```

Exact initial browser implementation target:

```text
0457a27d8e80863738ce3f75aeb11bd4f5c1155d
```

Interaction hierarchy under review:

```text
compact map work unit
    -> selected compact work unit
    -> expanded contextual/detail layer
    -> full specialist workspace / deep focus
```

Candidate expansion architectures:

```text
X0  Compact Control
X1  Vertical Drawer
X2  Right Sidecar
X3  Attached Sheet
X4  Wide Split Card
X5  Context Lens
X6  Layered Reveal
X7  Peek Rail
X8  Inspector Dock
```

Controlled placeholder detail payload:

```text
Purpose
Constraint / state
Evidence
Next action
```

The payload is not a frozen work-unit schema.

Current human gate:

```text
compare X1-X8 against X0
judge spatial orientation and attachment
identify variants that consume too much map context
judge whether X5 crosses prematurely into deep focus
compare inline expansion against X8 Inspector Dock
verify SEL2, A3 and status remain independent
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
