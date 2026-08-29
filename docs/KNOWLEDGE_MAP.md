# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources and does not replace them.  
**Last reviewed:** 2026-08-29  
**Current checkpoint:** 262  
**Active development branch:** `v1-cockpit-design-exploration`  
**Active PR:** none  
**Promoted V1 integration branch:** `v1-frontend-spike` at `ed5b60bdc882bed0799ce55228ce8187f9c55aa1`  
**Latest specification:** Specification 024  
**Latest scientific experiment outcome:** `INCOMPLETE / EXECUTION INTEGRITY FAILED`

## Start here

```text
README.md
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/current_routing.json

docs/checkpoints/262_conversation_boxes_grid_track_spacing_human_recheck_opened.md
docs/research/100_conversation_boxes_css_grid_track_absorption_and_live_geometry_recovery.md

docs/checkpoints/261_chatgpt_10_interaction_provenance_reconciliation.md

docs/checkpoints/260_conversation_boxes_row_owned_spacing_human_recheck_opened.md
docs/research/099_conversation_boxes_visible_separation_human_retest_and_row_owned_geometry_recovery.md

docs/checkpoints/259_cockpit_presentation_state_integrity_recovery.md
docs/research/098_intermittent_cockpit_presentation_state_integrity_recovery.md

docs/checkpoints/258_adaptive_conversation_dock_human_review_opened.md
docs/research/097_professional_conversation_copresence_and_adaptive_dock_study.md

docs/checkpoints/257_canonical_cockpit_review_route_normalized.md
docs/checkpoints/256_structural_conversation_spacing_and_project_tool_rail_controls_review_opened.md
docs/research/096_structural_conversation_spacing_and_current_project_tool_rail_control_set.md

docs/research/086_conversation_workspace_orthogonal_access_and_coexistence_architecture.md
docs/research/085_conversation_workspace_a6_refinement_and_entry_transition.md
docs/research/083_a6_adaptive_anchor_and_canonical_box_sidebar_mode.md
docs/research/082_conversation_scope_work_unit_anchor_and_quiet_graphite_baseline.md
docs/research/081_independent_conversation_workspace_dual_design_comparison.md
docs/research/079_conversation_workspace_presentation_architecture_experiment.md

docs/cockpit/README.md
docs/cockpit/PHASE_C_DECISION_LEDGER.md
docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
docs/cockpit/accepted_implementation_manifest.json
```

Current route:

```text
checkpoint                262
active branch             v1-cockpit-design-exploration
latest specification      Specification 024
promoted Cockpit baseline Specification 008
interaction session       chatgpt-10
conversation title        10 - Project Cockpit Design Exploration
current product boundary  Conversation Boxes grid-track spacing human recheck
```

---

# Checkpoint 262 live-browser spacing recovery

Checkpoint 260 failed human review even though the intended spacing declarations were loaded in the project owner's browser.

The first Chrome diagnostic established:

```text
rail state                    boxes
integrity stylesheet loaded   true
margin-bottom                 16px
padding top/bottom             6px / 6px
```

The second diagnostic established the exact rendered failure:

```text
WorkUnit row border-box       54px
computed margin-bottom        16px
next row starts               16px later
painted node surface          extends ~20.8px beyond row
visible surface gap           ~1.9px
```

Research 100 identifies the cause as CSS Grid auto-track sizing absorbing the item margin by shrinking the grid item while the transformed, overflow-visible canonical WorkUnit continued painting outside that row.

The superseded Checkpoint 260 row-owned-margin implementation is therefore preserved as failed diagnostic history, not as the current spacing mechanism.

## Current spacing mechanism

```text
thread-list row-gap          16px
project row margin            0px
WorkUnit row margin           0px
WorkUnit padding              6px top / 6px bottom
wide WorkUnit min-height     78px
responsive <=1450 min-height 73px
canonical WorkUnit           unchanged
```

This separates responsibilities:

```text
minimum row height
    contains transformed canonical artifact footprint

grid-track gap
    provides visible object separation
```

The non-Text selector remains, so compatible historical `artifact` state receives the same Boxes contract.

Implementation:

```text
frontend/design-lab/cockpit-reintegration-presentation-integrity.css
frontend/design-lab/cockpit-reintegration-review-256.css
```

Regression coverage:

```text
frontend/e2e/cockpit-reintegration-presentation-integrity.spec.ts
frontend/e2e/cockpit-reintegration-review-256.spec.ts
frontend/e2e/cockpit-reintegration-spatial-rail-angle.spec.ts
```

Current deterministic evidence:

```text
implementation/test target  b8a2d095214c3417f95180ca519c7b6224739181
workflow run                33247046868
job                         99086212488
result                      SUCCESS
browser tests               76 / 76 passing
```

The new gate explicitly covers 1100px responsive geometry in addition to wide and narrow viewports and requires actual visible WorkUnit surface gaps, not merely computed margins.

Human visual confirmation remains open.

---

# Current whole-product browser

Primary browser:

```text
frontend/design-lab/cockpit-reintegration.html
```

Normal current substrate:

```text
http://localhost:4173/design-lab/cockpit-reintegration.html
```

Adaptive Conversation Dock candidate:

```text
http://localhost:4173/design-lab/cockpit-reintegration.html?conversation=adaptive-dock
```

Route roles:

```text
plain route
    current source-faithful whole-product substrate
    Checkpoint 262 Boxes spacing recheck surface

?conversation=adaptive-dock
    professional co-present Conversation candidate
    same Boxes spacing integrity must hold here
    product review resumes after Checkpoint 262 confirmation

?edge=none
    internal earlier-shell regression substrate only

explicit ?edge=... / ?rail=...
    historical spatial-rail studies
```

---

# Current-process Focus status

Research 098's Focus lifecycle recovery remains current.

The latest human retest reports Focus working as far as tested. No Focus implementation changed in Checkpoints 260 or 262.

Focus is not part of the active defect boundary unless a new concrete reproduction appears.

---

# Adaptive Conversation Dock study remains open

Research 097 diagnoses the old co-present composition as a hierarchy problem:

```text
wide Conversation surface
    + permanently visible Conversation thread rail
    + long-form transcript
    -> resembles a second full application beside the Cockpit
```

The opt-in candidate remains:

```text
full focus
    source-faithful Quiet Graphite Workspace
    persistent Boxes/Text rail

co-present
    compact right secondary dock
    resizable left edge
    Cockpit retains majority visible width
    Threads invokes the same Boxes/Text rail as a drawer
    A6 becomes an invoked inspector sheet
```

Checkpoint 262 neither accepts nor rejects that product-design direction. Product review resumes after the Boxes spacing substrate is visually confirmed.

---

# Interaction provenance

Checkpoint 261 establishes the current interaction:

```text
chatgpt-10
10 - Project Cockpit Design Exploration
```

It corrected post-boundary Research 097 / Checkpoint 258 onward metadata after the prior ChatGPT conversation reached its length limit. Pre-boundary ChatGPT-09 history remains unchanged.

---

# Source-of-truth architecture

Use these layers together:

```text
SEMANTIC / PRODUCT AUTHORITY
    accepted specifications
    foundations
    explicit human-reviewed selections

DESIGN DISPOSITION
    docs/cockpit/PHASE_C_DECISION_LEDGER.md
    exhaustive for its declared Research 037-088 scope

POST-RECOVERY WHOLE-PRODUCT EVIDENCE
    Research 089 onward
    recent checkpoints

IMPLEMENTATION PROVENANCE
    docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
    docs/cockpit/accepted_implementation_manifest.json

CURRENT ROUTING
    docs/CURRENT_STATE.md
    docs/KNOWLEDGE_MAP.md
    docs/current_routing.json
    latest checkpoint + research record
```

A future integrator must never infer accepted implementation details from shorthand labels alone.

---

# Provenance and fidelity gates

Implementation-provenance recovery remains complete:

```text
manifest entries   23
required           19
non-promotable      4
first history gate 33156357834 PASS
```

Current gate model:

```text
PROVENANCE GATE
    PASS

INTERACTION PROVENANCE
    RECONCILED at Checkpoint 261
    chatgpt-10 / 10 - Project Cockpit Design Exploration

DETERMINISTIC INTEGRATION GATE
    PASS, 76/76 at b8a2d095214c3417f95180ca519c7b6224739181

HUMAN BOXES SPACING RECHECK
    OPEN at Checkpoint 262

HUMAN PRODUCT-DESIGN GATE
    Adaptive Conversation Dock review resumes after spacing confirmation
```

---

# Held Conversation architecture

```text
Quiet Graphite baseline
project-general + WorkUnit-scoped conversations
Boxes / Text thread navigation
A6 Adaptive Anchor
no redundant floating A6 WorkUnit box
Conversation access from Grid neutral / selected / X5 / Deep Dive
full-focus + co-present presentation capability
source work-state preservation
Conversation ownership independent from SEL2 selection
compact native Cockpit composer
```

Checkpoint 262 changes none of those decisions.

---

# Other held Phase-C product direction

```text
G4 Adaptive Hybrid world
H4 hover/outward response
Reduced in-box resting light
scientific category-marker grammar
Foundation 023 non-semantic appearance configurability
E5 Hue + Tag relation-class carrier
D0-D3 directionality
single terminal-treatment appearance choice
P7 Neutral Tag + Tone disposition
current-process focus lens
conditional runtime semantics
R1 / T7 switchable operational carrier family
BLOCKER -> BLOCKS -> BLOCKED
BLOCKED sharper ring / FAIL smoother ring
A3 Signal Bars
SEL2 four outside corner brackets
X5 balanced two-axis expansion
L0 provisional Flat Fields
Z7 Pull-Back Then Dive
full-stage specialist workspace
compact topology compass
S0 Geometric Control provisional working default
Specification 008 Jump/search, zoom/recovery and fullscreen capabilities
```

Semantic zoom remains deferred. L0 remains provisional.

---

# Failed holistic integration remains excluded

```text
8e554d847bb3b6318db432abcb5dff742f0fa523
```

remains diagnostic evidence only, not an accepted baseline, production target or visual source of truth.

---

# Recent whole-product studies

```text
Research 092  direct-manipulation spatial rail studies
Research 093  architectural 3D edge studies
Research 094  resting angled rail, rejected for current rail direction
Research 095  flat rail + initial Conversation spacing + live compass
Research 096  structural Conversation spacing + current flat rail control set
Research 097  Adaptive Conversation Dock co-presence candidate
Research 098  intermittent Conversation spacing + Focus integrity recovery
Research 099  failed Boxes human retest + row-owned-margin recovery attempt
Research 100  live CSS Grid geometry diagnosis + explicit grid-track spacing recovery
```

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
Course 2 gate unchanged
```

---

# MC-0004 collaboration route

```text
docs/model_collaboration/threads/MC-0004/BRIEF.md
docs/model_collaboration/threads/MC-0004/THREAD.md
docs/model_collaboration/threads/MC-0004/STATE.json
docs/model_collaboration/REVIEW_INBOX.md
```

No Claude obligation is pending. The next expected actor is the human reviewer.

---

# Exact next step

```text
Pull the latest branch and hard-refresh.

Inspect Boxes first on:
    normal route

Then optionally confirm:
    ?conversation=adaptive-dock route

Required result:
    project-general -> first WorkUnit visible separation
    WorkUnit -> WorkUnit visible separation
    canonical WorkUnit footprint unchanged
    Focus remains stable

If correct:
    close Checkpoint 262
    resume Adaptive Conversation Dock review

If still wrong:
    preserve screenshot and exact route/state
    keep product-design review paused
    continue only Conversation spacing integrity debugging with live rendered geometry
```
