# Current State

**Checkpoint:** 263  
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
docs/checkpoints/263_project_general_thread_containment_human_recheck_opened.md
docs/research/101_project_general_thread_short_viewport_containment_recovery.md

docs/checkpoints/262_conversation_boxes_grid_track_spacing_human_recheck_opened.md
docs/research/100_conversation_boxes_css_grid_track_absorption_and_live_geometry_recovery.md
```

Checkpoint 263 is the active product gate.

The Checkpoint 262 human retest is now partially closed with positive human evidence:

```text
Conversation WorkUnit spacing
    correct

current-process Focus
    working as far as tested
```

The same human screenshot exposed one narrower remaining defect:

```text
General project discussion
    not contained as a distinct first conversation artifact
    first WorkUnit visibly invades / overlaps that row
```

Research 101 protects the project-general row at short desktop heights without changing the accepted WorkUnit spacing geometry from Research 100.

Adaptive Conversation Dock product judgment remains paused only until this final underlying Conversation rail containment issue is visually confirmed.

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
    current Checkpoint 263 project-general containment human-recheck surface

?conversation=adaptive-dock
    opt-in professional co-present Conversation candidate
    product-design review resumes after Checkpoint 263 confirmation

?edge=none
    internal earlier-shell regression substrate only

explicit ?edge=... / ?rail=...
    historical spatial-rail studies
```

---

# Research 100 WorkUnit spacing recovery is human-confirmed

The project owner's Checkpoint 262 retest confirmed that the WorkUnit-to-WorkUnit spacing now looks correct.

The accepted Research 100 contract therefore remains:

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

The current grid-track model separates responsibilities correctly:

```text
minimum WorkUnit row height
    contains transformed canonical footprint

grid row-gap
    owns visible inter-object breathing room
```

Do not reopen the WorkUnit spacing model without new contradictory human evidence.

---

# Checkpoint 263 project-general containment recovery

## Human evidence

The successful WorkUnit spacing screenshot still showed the project-general first conversation object being visually invaded by the first WorkUnit.

This exposed a separate first-row containment gap rather than another WorkUnit spacing failure.

## Residual implementation gap

Research 100 gave WorkUnit rows explicit minimum heights but left the project-general row dependent on generic grid sizing.

The project artifact itself is not transformed, but at a short desktop content height its row still needs a minimum footprint large enough for:

```text
existing project artifact  58px
existing row padding        7px top / 7px bottom
row border budget
```

Current project row contract:

```text
project row box-sizing       border-box
project row height           auto
project row min-height       74px
project row margin            0px
project row padding           7px top / 7px bottom
project artifact min-height  58px
thread-list row-gap          16px
```

The visual design of the project-general artifact is unchanged.

Implementation artifacts:

```text
frontend/design-lab/cockpit-reintegration-presentation-integrity.css
frontend/design-lab/cockpit-reintegration-review-256.css
```

## Short-height regression

A new browser regression uses:

```text
1776 x 766
```

which approximates the actual visible page region in the supplied wide desktop screenshot after browser chrome is excluded.

It requires:

```text
project row height >=73.5px
project row padding >=7px top/bottom
first WorkUnit visible surface begins >=16px after project artifact bottom
WorkUnit-to-WorkUnit visible gaps remain >=20px
```

This explicitly protects the previously untested wide-but-short browser shape.

---

# Deterministic fidelity status

Implementation/test target:

```text
5913467cfffd535215da7ab2cb70bdeb2be9f2e9
```

Latest complete Cockpit fidelity workflow:

```text
workflow run  33247621778
job           99087735314
result        SUCCESS
browser tests 77 / 77 passing
```

The 77-test gate includes all previous source-faithful Cockpit coverage plus the new short-height project-general containment regression.

The new test passed under the exact current implementation:

```text
General project discussion remains a distinct first artifact at a short desktop viewport
```

A green deterministic gate still does not substitute for the current human visual recheck because this residual defect was identified directly in the project owner's real browser.

---

# Current-process Focus

No Focus code was changed for Checkpoint 263.

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

Checkpoint 263 does not accept, reject or retune this candidate. It repairs the final observed base-rail containment issue needed to judge it reliably.

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

Required visible result:
    General project discussion is one complete standalone first artifact
    no WorkUnit overlaps it
    clear dark separation follows it
    WorkUnit spacing remains correct
    Focus continues working

If correct:
    close Checkpoint 263
    close the Conversation presentation-integrity interruption
    resume Checkpoint 258 Adaptive Conversation Dock visual review immediately

If still wrong:
    preserve screenshot and exact viewport/route
    continue only project-general rail geometry debugging
```
