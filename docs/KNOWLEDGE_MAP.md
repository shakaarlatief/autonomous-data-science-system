# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources and does not replace them.  
**Last reviewed:** 2026-08-27  
**Current checkpoint:** 237  
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
checkpoint                        237
active branch                     v1-cockpit-design-exploration
latest specification              Specification 024
promoted Cockpit baseline         Specification 008
current boundary                  switchable runtime-carrier convergence human review
source-vault deployment           PAUSED, Course 2 gate unchanged
```

---

# Repository preservation / development-method route

Checkpoint-format authority:

```text
docs/checkpoints/README.md
scripts/check_checkpoint_metadata.py
.github/workflows/checkpoint-metadata.yml
```

Rapid-iteration audit:

```text
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

Current-routing guard:

```text
scripts/check_current_routing.py
.github/workflows/current-routing-consistency.yml
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

Latest accepted P7 implementation:

```text
fac1db37af4225927d6c799e37418a3ad9c42c13
```

Use `Current` for project disposition and reserve `Running` for runtime. The final project-disposition ontology remains unfrozen.

---

# Current-process focus result

Primary evidence:

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

The user can add/remove work units from the current focus without deleting work or changing disposition. Outside-focus nodes and connector segments recede strongly in focus mode and remain recoverable for inspection/editing.

Exact accepted editable-focus implementation:

```text
da115b74de526fca05ed6f468bef39bdb801355c
```

Final focus-set ownership/persistence, automatic suggestions, multiple named lenses and exact membership semantics remain open.

---

# Current Slice 02H: conditional runtime carrier convergence

Semantic-correction evidence:

```text
docs/research/065_work_unit_runtime_state_visual_grammar_experiment.md
docs/research/066_conditional_runtime_state_and_project_disposition_semantic_correction.md
docs/checkpoints/236_runtime_state_made_conditional_human_review_reopened.md
```

Current convergence evidence:

```text
docs/research/067_switchable_runtime_carrier_convergence_and_r1_r5_verification.md
docs/checkpoints/237_switchable_runtime_carrier_convergence_review_opened.md
```

Current browser route:

```text
frontend/design-lab/work-unit-runtime-carrier-switch.html
frontend/design-lab/work-unit-runtime-carrier-switch.css
frontend/design-lab/work-unit-runtime-carrier-switch.js
```

Local URL:

```text
http://localhost:5173/design-lab/work-unit-runtime-carrier-switch.html
```

Exact current browser implementation target:

```text
3a862c659e60e53832eaa5940ddb60d05734cd7d
```

Current semantic separation:

```text
category                  what is this?
project disposition       where does it stand in the project?
runtime                    if a current execution/work episode exists, what is happening in it?
priority / relevance       how important is it now?
current-focus membership   is it in the emphasized process set?
```

Runtime remains conditional.

Critical distinction:

```text
No runtime
    no current execution/work episode exists

Idle runtime
    an execution episode exists but is doing nothing
```

Controlled fixtures:

```text
NONE    No runtime
QUEUE   Queued
RUN     Running
WAIT    Waiting
HUMAN   Waiting for Human
FAIL    Failed current attempt
```

Working compatibility interpretation:

```text
Current                 may have NONE or a live runtime state
Recommended / Next      normally NONE; may be QUEUE if explicitly scheduled
Deferred                normally NONE
Completed               normally NONE
Future                  normally NONE
```

Current runtime remains separate from historical execution provenance.

`Blocked` remains explicitly unresolved as a possible orthogonal progress constraint rather than automatically treated as a peer lifecycle/disposition value.

## R1/R5 verification

Direct implementation inspection established:

```text
R1 = status lamp
R5 = same status lamp + motion ring
```

The two encodings were therefore not literally identical, but the extra ring was too subtle at working scale to make R5 read as a genuinely distinct family except most clearly for Failed. This is retained as negative design evidence.

## Active runtime-carrier convergence

Exactly one carrier is active per live-runtime work unit:

```text
Dot + dynamic ring
Animated runtime tag
```

The dot uses a stronger visible outer ring with state-sensitive motion pacing. The tag uses explicit state text plus a circulating perimeter trace.

Switching operates at two scopes:

```text
GLOBAL
    change every live-runtime node
    clear local overrides

LOCAL
    click the visible runtime carrier
    switch only that node
```

No-runtime nodes show no carrier and expose no carrier-switch target.

Practical scene:

```text
Question        CURRENT + HUMAN
Investigation   CURRENT + RUN
Validation      NEXT + QUEUE
Model Work      CURRENT + FAIL
Evaluation      DEFER + NONE
Investigation   FUTURE + NONE
```

Reduced motion removes animation while preserving static runtime identity.

The final ADS runtime ontology, final carrier, production default/persistence, project-disposition ontology, Blocked semantics, historical execution presentation and runtime-flow connector semantics remain unfrozen.

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