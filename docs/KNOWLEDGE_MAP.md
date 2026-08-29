# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources and does not replace them.  
**Last reviewed:** 2026-08-29  
**Current checkpoint:** 263  
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

docs/checkpoints/263_project_general_thread_containment_human_recheck_opened.md
docs/research/101_project_general_thread_short_viewport_containment_recovery.md

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
checkpoint                263
active branch             v1-cockpit-design-exploration
latest specification      Specification 024
promoted Cockpit baseline Specification 008
interaction session       chatgpt-10
conversation title        10 - Project Cockpit Design Exploration
current product boundary  project-general thread containment human recheck
```

---

# Checkpoint 263 project-general containment recovery

Checkpoint 262 produced positive human evidence for the Research 100 WorkUnit spacing repair:

```text
WorkUnit-to-WorkUnit spacing
    correct
```

The same human screenshot exposed one narrower residual defect:

```text
General project discussion
    first conversation object not fully isolated
    first WorkUnit visually invades / overlaps the project-general row
```

Research 101 keeps the human-confirmed WorkUnit spacing mechanism unchanged and gives the project-general row its own explicit containment floor.

Current project-general contract:

```text
thread-list row-gap          16px
project row min-height       74px
project row margin            0px
project row padding           7px top / 7px bottom
project artifact min-height  58px
```

The project artifact itself is not redesigned.

A new regression uses the wide-but-short viewport:

```text
1776 x 766
```

and requires:

```text
project row height >=73.5px
project row padding >=7px top/bottom
first WorkUnit surface begins >=16px after project artifact bottom
WorkUnit-to-WorkUnit visible gaps remain >=20px
```

Current deterministic evidence:

```text
implementation/test target  5913467cfffd535215da7ab2cb70bdeb2be9f2e9
workflow run                33247621778
job                         99087735314
result                      SUCCESS
browser tests               77 / 77 passing
```

Human visual confirmation of the project-general first artifact remains open.

---

# Research 100 WorkUnit spacing recovery remains accepted by human retest

The project owner's live Chrome measurements established the earlier failure:

```text
WorkUnit row border-box       54px
computed margin-bottom        16px
next row starts               16px later
painted node surface          extends ~20.8px beyond row
visible surface gap           ~1.9px
```

Research 100 identified the cause as CSS Grid auto-track sizing absorbing the item margin by shrinking the grid item while the transformed, overflow-visible canonical WorkUnit continued painting outside that row.

The superseded Checkpoint 260 row-owned-margin implementation remains failed diagnostic history, not the current spacing mechanism.

Current WorkUnit spacing mechanism:

```text
thread-list row-gap          16px
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
    Checkpoint 263 project-general containment recheck surface

?conversation=adaptive-dock
    professional co-present Conversation candidate
    product review resumes after Checkpoint 263 confirmation

?edge=none
    internal earlier-shell regression substrate only

explicit ?edge=... / ?rail=...
    historical spatial-rail studies
```

---

# Current-process Focus status

Research 098's Focus lifecycle recovery remains current.

The latest human retest reports Focus working as far as tested. No Focus implementation changed in Checkpoints 260, 262 or 263.

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

Checkpoint 263 neither accepts nor rejects that product-design direction. Product review resumes after the final base-rail containment issue is visually confirmed.

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
    PASS, 77/77 at 5913467cfffd535215da7ab2cb70bdeb2be9f2e9

HUMAN WORKUNIT SPACING RECHECK
    PASS at Checkpoint 262

HUMAN PROJECT-GENERAL CONTAINMENT RECHECK
    OPEN at Checkpoint 263

HUMAN PRODUCT-DESIGN GATE
    Adaptive Conversation Dock review resumes after Checkpoint 263 confirmation
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

Checkpoint 263 changes none of those decisions.

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
Research 101  project-general short-viewport row containment recovery
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

Inspect Boxes on the normal route.

Required result:
    General project discussion is a complete standalone first artifact
    no WorkUnit overlaps it
    clear dark separation follows it
    WorkUnit spacing remains correct
    Focus remains stable

If correct:
    close Checkpoint 263
    close the Conversation presentation-integrity interruption
    resume Adaptive Conversation Dock review

If still wrong:
    preserve screenshot and exact viewport/route
    continue only project-general rail geometry debugging
```
