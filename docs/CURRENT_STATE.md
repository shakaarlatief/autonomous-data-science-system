# Current State

**Checkpoint:** 262  
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
docs/checkpoints/262_conversation_boxes_grid_track_spacing_human_recheck_opened.md
docs/research/100_conversation_boxes_css_grid_track_absorption_and_live_geometry_recovery.md

docs/checkpoints/261_chatgpt_10_interaction_provenance_reconciliation.md
```

Checkpoint 262 is the active product gate.

The previous Checkpoint 260 row-owned-margin spacing implementation failed human review even though the intended declarations were loaded. Live Chrome geometry supplied by the project owner then identified the exact layout failure rather than another inferred cause.

Current human evidence remains:

```text
current-process Focus
    working as far as tested

Conversation Boxes before Checkpoint 262 recovery
    visually joined
    computed 16px margins present
    visible surface gap only about 1.9px
```

Adaptive Conversation Dock product judgment remains paused only until this underlying Boxes presentation is visually confirmed again.

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
    current Checkpoint 262 Boxes spacing human-recheck surface

?conversation=adaptive-dock
    opt-in professional co-present Conversation candidate
    same spacing integrity must hold here
    product-design review resumes after Checkpoint 262 confirmation

?edge=none
    internal earlier-shell regression substrate only

explicit ?edge=... / ?rail=...
    historical spatial-rail studies
```

---

# Checkpoint 262 Conversation Boxes recovery

## Live-browser diagnosis

The project owner's first diagnostic proved that the intended Checkpoint 260 CSS was really active:

```text
rail state                    boxes
integrity stylesheet loaded   true
WorkUnit margin-bottom        16px
WorkUnit padding-top           6px
WorkUnit padding-bottom        6px
```

Therefore stale Git state, stale Vite output and browser cache were not the cause.

The second diagnostic measured the actual rendered grid and WorkUnit geometry. Representative values were:

```text
thread list display           grid
row-gap                       0px
WorkUnit row height           54.0px
computed margin-bottom        16px
row-to-row distance           16.0px
painted surface bottom        ~20.8px below row bottom
visible surface gap           ~1.9px
```

This numerically matches the user's screenshot.

## Exact root cause

The Checkpoint 260 margin-owned model was incompatible with this transformed-grid composition.

CSS Grid included the WorkUnit margin in auto-track sizing and shrank the stretched item border box. The source-faithful Conversation WorkUnit is a transformed child with visible overflow, so its painted node surface continued beyond that shrunken row.

Thus:

```text
computed margin = 16px
    did not imply
visible WorkUnit surface separation = 16px
```

Research 100 records the complete reasoning and measurements.

## Current spacing contract

The visual target from Checkpoint 256 remains unchanged. The canonical WorkUnit is not resized or redesigned.

Current implementation:

```text
thread-list row-gap          16px
project row margin            0px
WorkUnit row margin           0px
WorkUnit padding              6px top / 6px bottom
wide WorkUnit min-height     78px
responsive <=1450 min-height 73px
```

The two responsibilities are now separated:

```text
minimum row height
    contains the transformed canonical WorkUnit footprint

grid track gap
    owns the visible breathing room between objects
```

The non-Text compatibility selector remains, so both current `boxes` and historical-compatible `artifact` rail states receive the same spacing contract.

Implementation artifacts:

```text
frontend/design-lab/cockpit-reintegration-presentation-integrity.css
frontend/design-lab/cockpit-reintegration-review-256.css
```

---

# Deterministic fidelity status

Implementation/test target:

```text
b8a2d095214c3417f95180ca519c7b6224739181
```

Latest complete Cockpit fidelity workflow:

```text
workflow run  33247046868
job           99086212488
result        SUCCESS
browser tests 76 / 76 passing
```

The strengthened gate now includes:

```text
1600px desktop spacing
1100px responsive spacing
760px narrow spacing
legacy artifact state under responsive and wide layouts
actual WorkUnit surface-to-surface gap >=20px
Adaptive Dock full-focus / co-present / Threads-drawer spacing lifecycle
current-process Focus lifecycle/remount synchronization
all previous source-faithful Cockpit mechanisms
```

An immediately preceding run failed because two historical test files still encoded old test plumbing/old margin-contract expectations. Those assertions were corrected; the final 76/76 workflow is the authoritative deterministic result.

A green deterministic gate still does not substitute for the current human visual recheck because the defect itself was discovered through real-browser visual evidence.

---

# Current-process Focus

No Focus code was changed for Checkpoint 262.

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

Checkpoint 262 does not accept, reject or retune this candidate. It repairs the Boxes rail substrate needed to judge it reliably.

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

Inspect Boxes first on:
    http://localhost:4173/design-lab/cockpit-reintegration.html

Then optionally confirm the same spacing on:
    ?conversation=adaptive-dock

Required visible result:
    clear dark separation after project-general artifact
    clear dark separation between every WorkUnit
    canonical WorkUnit footprint unchanged
    Focus continues working

If correct:
    close Checkpoint 262
    resume Checkpoint 258 Adaptive Conversation Dock visual review immediately

If still wrong:
    preserve screenshot and exact route/state
    keep Adaptive Dock product judgment paused
    continue only Conversation presentation-integrity debugging using live rendered geometry
```
