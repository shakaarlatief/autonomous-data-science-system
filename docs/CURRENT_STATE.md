# Current State

**Checkpoint:** 264  
**Date:** 2026-08-29  
**Active development branch:** `v1-cockpit-design-exploration`  
**Active PR:** none  
**Promoted V1 integration branch:** `v1-frontend-spike` at `ed5b60bdc882bed0799ce55228ce8187f9c55aa1`  
**Latest specification:** Specification 024 remains accepted. Specification 008 remains the promoted V1 Project Cockpit interaction architecture.  
**Latest scientific experiment:** Specification 022 remains `INCOMPLETE / EXECUTION INTEGRITY FAILED`; no GENERIC / ADS_HORIZON / ORACLE_HORIZON comparison may be inferred from that run.

## Active interaction context

```text
Interaction environment  ChatGPT
Project / workspace      Autonomous Data Science System
Interaction session      chatgpt-10
Conversation title       10 - Project Cockpit Design Exploration
Primary collaborator     ChatGPT
Collaboration thread     MC-0004
```

Repository artifacts remain authoritative across chats and models.

---

# Current active boundary

```text
docs/checkpoints/264_project_general_footprint_and_selection_frame_human_recheck_opened.md
docs/research/102_project_general_box_footprint_and_selection_frame_alignment.md

docs/checkpoints/263_project_general_thread_containment_human_recheck_opened.md
docs/research/101_project_general_thread_short_viewport_containment_recovery.md

docs/checkpoints/262_conversation_boxes_grid_track_spacing_human_recheck_opened.md
docs/research/100_conversation_boxes_css_grid_track_absorption_and_live_geometry_recovery.md
```

Checkpoint 264 is the active product gate.

The latest human screenshots now establish:

```text
Conversation WorkUnit spacing
    correct

General project discussion containment
    correct

current-process Focus
    working as far as tested
```

The remaining Conversation rail issue is deliberately narrow:

```text
General project discussion visible footprint
    should match WorkUnit box footprint

Boxes selected-state frame
    should surround the visible selected object itself
    should not create a larger generic outer-row rectangle
```

Research 102 implements that alignment without changing the already accepted WorkUnit spacing, WorkUnit geometry, Focus behavior or Conversation semantics.

Adaptive Conversation Dock product judgment remains paused only until this final small Boxes visual-consistency recheck is confirmed.

Production `/cockpit` remains untouched.

---

# Whole-product browser and routes

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
    source-faithful whole-product substrate
    current Checkpoint 264 project-general footprint/selection-frame human-recheck surface

?conversation=adaptive-dock
    opt-in professional co-present Conversation candidate
    product-design review resumes after Checkpoint 264 confirmation

?edge=none
    internal earlier-shell regression substrate only

explicit ?edge=... / ?rail=...
    historical spatial-rail studies
```

---

# Research 100 WorkUnit spacing recovery is human-confirmed

The project owner has explicitly confirmed that the WorkUnit-to-WorkUnit spacing is now correct.

The accepted Research 100 contract remains:

```text
thread-list row-gap          16px
WorkUnit row margin           0px
WorkUnit padding              6px top / 6px bottom
wide WorkUnit min-height     78px
responsive <=1450 min-height 73px
actual visible WorkUnit gap  >=20px deterministic contract
```

The canonical WorkUnit is not resized or redesigned.

Research 100's root cause remains preserved:

```text
margin-owned spacing
    was absorbed into CSS Grid auto-track sizing
    while transformed WorkUnit children painted beyond shrunken rows
    producing ~1.9px visible separation despite 16px computed margins
```

Do not reopen the WorkUnit spacing architecture without new contradictory human evidence.

---

# Research 101 project-general containment is human-confirmed

Checkpoint 263 added an explicit structural project row after the first WorkUnit had previously invaded the project-general row at short desktop heights.

The latest screenshots confirm that General project discussion is now a clean standalone first object and is no longer overlapped by WorkUnit 1.

Research 101 therefore remains accepted as the containment mechanism underneath the current finer visual-alignment pass.

---

# Checkpoint 264 project-general footprint and selection alignment

## Human evidence

The latest screenshots show two closely related visual inconsistencies after the larger containment defects were fixed:

```text
General project discussion
    visible box smaller than the WorkUnit box slots

selected state
    General received a larger generic thread-row frame
    WorkUnits visually carried selection on the canonical node surface
```

The issue is not semantic selection state. It is presentation ownership and geometry.

## Exact footprint alignment

The accepted Conversation WorkUnit slot remains unchanged:

```text
normal rail          232 x 74 px
responsive <=1450    214 x 69 px
```

The project-general artifact now matches that footprint exactly:

```text
normal project artifact       232 x 74 px
responsive project artifact   214 x 69 px
```

The WorkUnit is not resized to fit the project artifact. The project artifact is aligned to the accepted WorkUnit rail footprint.

## Selected-state ownership

In Boxes / artifact-compatible mode:

```text
outer .reintegration-thread-item
    structural only
    transparent even while active

project-general selected surface
    .reintegration-project-thread-artifact

WorkUnit selected surface
    .conversation-canonical-node .node-surface
```

The final integrity layer applies the selected border/shadow to the actual visible object surfaces.

In Text mode the generic row selection treatment remains available because the row itself is the visible navigation object.

## Spacing remains unchanged

The list still owns a structural 16px CSS Grid row gap.

After enlarging the project artifact to the WorkUnit footprint, the short-height painted edge-to-edge project-to-first-WorkUnit distance is 15px because the two visible 1px borders consume one pixel of the nominal track separation measurement. The structural gap remains 16px, and the human-approved WorkUnit spacing is not retuned.

Deterministic contract:

```text
CSS Grid row-gap                     >=16px
project -> first WorkUnit dark gap   >=15px
WorkUnit -> WorkUnit visible gap     >=20px
```

---

# Deterministic fidelity status

Final implementation/test target:

```text
9881efe313b8cf04d9521c0464050b30b29944c1
```

The visual implementation is present in its ancestry through:

```text
524d4fcba3df835de3ecc5757ed4a97dafdd656e
```

Latest complete Cockpit fidelity workflow:

```text
workflow run  33251166351
job           99096968925
result        SUCCESS
browser tests 78 / 78 passing
```

The new regression explicitly verifies:

```text
project artifact and WorkUnit slot have equal visible width/height
project outer structural row remains transparent while selected
WorkUnit outer structural row remains transparent while selected
project selected surface receives a visible border/shadow
WorkUnit selected surface receives a visible border/shadow
selection transfer removes the project selected shadow
short-height containment remains intact
all earlier source-faithful mechanisms remain green
```

An intermediate test compared serialized CSS color strings and was rejected as a brittle assertion because Chromium may represent equivalent/layered colors through different CSS color spaces. The durable test asserts the actual geometry and selected-surface responsibility seen by the human reviewer.

A green deterministic gate still does not substitute for the current human visual recheck.

---

# Current-process Focus

No Focus code was changed for Checkpoints 262, 263 or 264.

Research 098's recovery remains current:

```text
one authoritative focusMembership set
node scope reapplied from that set
WorkUnit remount/replacement observer
membership controls restored on replacement carriers
relations resynchronized after node repair
Focus stylesheet statically loaded
accepted opacity/filter contract protected from later style precedence
```

Current human evidence is positive: Focus is working as far as tested.

Do not reopen Focus without another concrete reproduction.

---

# Adaptive Conversation Dock remains open, not promoted

Checkpoint 258 and Research 097 remain the product-design evidence for Conversation/Cockpit co-presence.

The candidate still tests:

```text
full-focus
    source-faithful Quiet Graphite Workspace
    persistent Boxes/Text rail

co-present
    compact resizable right-side secondary dock
    Cockpit remains majority visible
    Threads invokes the same Boxes/Text rail as a drawer
    A6 available as invoked inspector sheet
```

Checkpoints 259-264 are integrity/refinement interruptions underneath that still-open product-design review. They do not accept, reject or retune the Adaptive Dock direction.

Once Checkpoint 264 is visually confirmed, resume the Adaptive Conversation Dock review immediately rather than opening another unrelated design branch.

---

# Interaction continuity

Checkpoint 261 remains the provenance boundary for the current conversation:

```text
interaction session  chatgpt-10
conversation title   10 - Project Cockpit Design Exploration
```

Post-boundary Research 097 / Checkpoint 258 onward provenance was reconciled without rewriting pre-boundary ChatGPT-09 history.

---

# Held Conversation semantics remain intact

```text
Quiet Graphite baseline
project-general + WorkUnit-scoped conversation
Boxes / Text user-switchable thread navigation
A6 Adaptive Anchor
no redundant A6 floating home card
Conversation access from Grid neutral / selected / X5 / Deep Dive
full-focus + co-present capability
source work-state preservation
Conversation ownership separate from SEL2 selection
compact native Cockpit composer
```

Checkpoint 264 changes none of these semantics.

---

# Other held Phase-C decisions remain intact

```text
G4 Adaptive Hybrid world
H4 hover/world response
Reduced in-box resting light
scientific category-marker grammar
Foundation 023 non-semantic appearance configurability
E5 Hue + Tag relation-class carrier
D0-D3 semantic directionality
single active connector terminal treatment
P7 Neutral Tag + Tone disposition
editable current-process focus set
conditional runtime semantics
one switchable operational carrier
T7 Soft Shade runtime tag
BLOCKER -> BLOCKS -> BLOCKED cause/effect model
BLOCKED sharper compact ring
FAIL smoother circular compact ring
A3 Signal Bars for HIGH attention
SEL2 four outside corner brackets
X5 balanced contextual expansion without context recession
L0 Flat Fields provisional working internal-layout default
Z7 Pull-Back Then Dive specialist-workspace entry
full-stage specialist workspace
compact topology compass retained
S0 Geometric Control provisional zoom working default
Specification 008 Jump/search, zoom/recovery and fullscreen capabilities
```

L0 remains provisional. Semantic zoom remains deferred.

Implementation provenance remains governed by:

```text
docs/cockpit/ACCEPTED_IMPLEMENTATION_MANIFEST.md
docs/cockpit/accepted_implementation_manifest.json
```

The failed holistic browser at `8e554d847bb3b6318db432abcb5dff742f0fa523` remains diagnostic evidence only.

---

# Deferred / paused work remains unchanged

```text
semantic zoom
    DEFERRED
    S0 geometric control remains the provisional working default

source-vault bootstrap
    PAUSED
    not cancelled or rejected

Course 2 source-universe gate
    unchanged
```

---

# Exact next step

```text
Human pulls the latest v1-cockpit-design-exploration branch and hard-refreshes.

Inspect Boxes on:
    http://localhost:4173/design-lab/cockpit-reintegration.html

Switch between:
    General project discussion
    Resolve target definition
    other WorkUnit threads

Required visible result:
    General project discussion matches the WorkUnit box footprint
    selecting General frames only the General project box
    selecting a WorkUnit frames only that WorkUnit surface
    no oversized outer-row selection rectangle appears
    existing spacing remains correct
    Focus remains stable

If correct:
    close Checkpoint 264
    close the Conversation presentation-integrity interruption
    resume Checkpoint 258 Adaptive Conversation Dock visual review immediately

If still wrong:
    preserve screenshot and exact viewport/route
    continue only the footprint/selection-frame boundary
```
