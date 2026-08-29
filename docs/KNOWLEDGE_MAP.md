# Knowledge Map

**Status:** Current routing index  
**Authority:** Navigation only. This file points to authoritative or explanatory sources and does not replace them.  
**Last reviewed:** 2026-08-29  
**Current checkpoint:** 264  
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

docs/checkpoints/264_project_general_footprint_and_selection_frame_human_recheck_opened.md
docs/research/102_project_general_box_footprint_and_selection_frame_alignment.md

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

docs/cockpit/README.md
docs/cockpit/PHASE_C_DECISION_LEDGER.md
docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
docs/cockpit/accepted_implementation_manifest.json
```

Current route:

```text
checkpoint                264
active branch             v1-cockpit-design-exploration
latest specification      Specification 024
promoted Cockpit baseline Specification 008
interaction session       chatgpt-10
conversation title        10 - Project Cockpit Design Exploration
current product boundary  project-general footprint + Boxes selected-surface frame human recheck
```

---

# Checkpoint 264 project-general footprint and selection alignment

The latest human screenshots establish that the previous substantive Conversation rail defects are solved:

```text
WorkUnit spacing                  human-confirmed correct
General project containment       human-confirmed correct
current-process Focus             working as far as tested
```

The remaining issue was visual consistency between the project-general thread and WorkUnit threads.

## Footprint

The accepted Conversation WorkUnit rail slot is:

```text
normal rail          232 x 74 px
responsive <=1450    214 x 69 px
```

Research 102 aligns the project-general visible artifact to exactly those dimensions. The WorkUnit geometry is not changed.

## Selection frame

Boxes mode now separates structural-row state from visible-object state:

```text
outer thread row
    structural
    transparent while active

project-general selected surface
    project artifact

WorkUnit selected surface
    canonical WorkUnit node surface
```

Text mode retains generic row selection because the row is the visible item there.

This removes the oversized project-row outline visible in the human screenshot and makes both object families use the same selected-surface concept.

Implementation:

```text
frontend/design-lab/cockpit-reintegration-presentation-integrity.css
```

Regression:

```text
frontend/e2e/cockpit-reintegration-review-256.spec.ts
```

Deterministic evidence:

```text
implementation/test target  9881efe313b8cf04d9521c0464050b30b29944c1
workflow run                33251166351
job                         99096968925
result                      SUCCESS
browser tests               78 / 78 passing
```

The new regression verifies equal visible project/WorkUnit dimensions, transparent structural active rows, selected-state border/shadow on the visible surfaces and correct selection transfer.

Human visual confirmation remains open.

---

# Research 100 and 101 are now human-confirmed substrate

## WorkUnit spacing

Research 100 remains the accepted fix for the CSS Grid track-absorption defect:

```text
thread-list row-gap          16px
WorkUnit row margins          0px
WorkUnit row padding          6px top/bottom
wide min-height              78px
responsive min-height        73px
visible WorkUnit gaps        >=20px regression
```

The project owner explicitly confirmed the resulting WorkUnit spacing is correct.

## Project-general containment

Research 101 reserved a structural first-row footprint so the first transformed WorkUnit could not paint into General project discussion at short desktop height.

The latest screenshots show that overlap is gone, so Research 101 remains accepted underneath the finer Research 102 alignment.

Equalizing the visible project artifact to 74px produces a 15px painted project-to-first-WorkUnit separation at the short viewport while the structural Grid row-gap remains 16px. The existing spacing is intentionally not enlarged because the human reviewer already accepted it.

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
    Checkpoint 264 footprint/selection-frame recheck surface

?conversation=adaptive-dock
    professional co-present Conversation candidate
    product review resumes after Checkpoint 264 confirmation

?edge=none
    internal earlier-shell regression substrate only

explicit ?edge=... / ?rail=...
    historical spatial-rail studies
```

---

# Current-process Focus status

Research 098's Focus lifecycle recovery remains current.

The latest human retest reports Focus working as far as tested. No Focus implementation changed in Checkpoints 260, 262, 263 or 264.

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

Checkpoints 259-264 are integrity/refinement interruptions. They do not promote or reject the Adaptive Dock candidate.

Once the Checkpoint 264 visual recheck passes, resume Checkpoint 258 / Research 097 immediately.

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
    PASS, 78/78 at 9881efe313b8cf04d9521c0464050b30b29944c1

HUMAN WORKUNIT SPACING GATE
    PASSED

HUMAN PROJECT CONTAINMENT GATE
    PASSED

HUMAN PROJECT FOOTPRINT / SELECTION FRAME GATE
    OPEN at Checkpoint 264

HUMAN PRODUCT-DESIGN GATE
    Adaptive Conversation Dock review resumes after Checkpoint 264 confirmation
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

Checkpoint 264 changes none of those semantics.

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
Research 101  project-general short-height containment recovery
Research 102  project-general box footprint + selected-surface frame alignment
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

Switch between General project discussion and multiple WorkUnit threads.

Required result:
    project-general visible box matches WorkUnit footprint
    General selection frames only the visible project box
    WorkUnit selection frames only the visible WorkUnit
    no oversized wrapper appears
    spacing remains correct

If correct:
    close Checkpoint 264
    close the Conversation rail integrity interruption
    resume Adaptive Conversation Dock review

If still wrong:
    preserve screenshot and viewport
    continue only footprint/selection-frame integrity debugging
```
