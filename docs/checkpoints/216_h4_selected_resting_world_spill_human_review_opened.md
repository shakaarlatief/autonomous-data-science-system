# Checkpoint 216: H4 Selected, Resting World-Spill Human Review Opened

**Date:** 2026-08-26  
**Status:** Current product-design checkpoint  
**Checkpoint class:** CONTINUITY / PRODUCT_DESIGN / HUMAN_REVIEW  
**Project stage:** V1 next-generation Project Cockpit browser-rendered design exploration  
**Scope:** Records selection of H4 Integrated Response as the preferred work-unit interaction-lighting direction and opens a narrower review of stronger resting node-colored illumination into the surrounding G4 grid while preserving the newer in-node light treatment.  
**Authority:** Current Phase-C product-design routing/evidence boundary only. Specification 008 remains the promoted Cockpit interaction architecture.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** chatgpt-07  
**Conversation title:** 07 - Project Cockpit Design Exploration  
**Primary collaborator:** ChatGPT

## 1. Grid/world status

The G4 Adaptive Hybrid grid/world remains provisionally settled.

Preserved current world choices include:

```text
G4 Adaptive Hybrid
Dark-first sequencing
Lively randomized currents
Quiet major-grid glints
Ambient drift
Localized semantic activity
```

This is not a permanent freeze. Integrated evidence may still justify later refinement.

## 2. Work-unit lighting selection

Human review selected:

```text
H4 Integrated Response  SELECTED
```

H4 currently combines:

```text
localized/asymmetric rest light
full hover halo
pointer-following hotspot
local grid illumination on hover
immediate connector emphasis
single restrained perimeter sweep on hover entry
small hover depth lift
```

## 3. Resting world-spill refinement

The project owner likes the newer H4 light inside the work-unit box but wants some of the same node-colored light visible in the surrounding grid in the normal resting state.

The earlier broad circular halo treatment was rejected because it made the node feel surrounded by a generalized neon cloud. The accepted direction instead keeps the cleaner H4 in-box illumination and projects a narrow, soft continuation of the node color primarily through the accent/left side into the grid.

The current intended result is therefore:

```text
keep the accepted in-box H4 illumination unchanged
+
keep a narrow soft resting spill into the grid
+
extend additional resting light outward through the left/accent side only
+
keep the spill asymmetric and restrained at rest
+
retain richer full H4 response on hover
-
do not increase the resting light farther into the card
-
do not restore the earlier broad circular halo
```

A first canonicalized version of this treatment was positively reviewed by the project owner as matching the intended visual idea. A subsequent small reach increase also made the spill slightly stronger and moved its inward edge farther into the box. Human review correctly identified that as unintended. The correction preserves the new outward reach while restoring the previously accepted in-box intensity, blur and inward boundary.

## 4. Hover-release refinement from video review

The project owner also supplied a browser recording of H4 interaction. Review of that recording showed that the richer hover state returned to the resting state too abruptly after the pointer left the work unit.

The selected timing principle is asymmetric:

```text
pointer enters work unit
-> response stays immediate and crisp

pointer leaves work unit
-> light, depth, connector emphasis and world spill decay more gradually
-> the one-time perimeter sweep also receives a longer, softer final fade
```

After implementation, the project owner explicitly judged the revised hover animation to be perfect. The current hover-entry and hover-release timing should therefore be preserved unless later integrated evidence reveals a new problem.

## 5. Browser experiment updated

Current review surface:

```text
frontend/design-lab/work-unit-lighting.html
frontend/design-lab/work-unit-lighting.css
frontend/design-lab/work-unit-lighting.js
```

Expected local URL:

```text
http://localhost:5173/design-lab/work-unit-lighting.html
```

Only H4 receives the resting world-spill refinement. The smoother release timing affects the shared interaction layers used by the lighting comparison, while H4 remains the selected direction and the primary review target. H1-H3 remain comparison evidence.

## 6. Production boundary

No production Cockpit implementation is authorized.

Still unresolved include:

```text
final work-unit shapes
final semantic colors
selected-state lighting
runtime-state lighting
blocked/waiting/approval treatment
final connector visual language
semantic zoom behavior
focus transition architecture
```

## 7. Human review gate

The next review should answer:

```text
Does H4 project the desired extra light into the grid without increasing the resting light inside the box?
Is the outward left-side spill still narrow enough to avoid a neon-card look?
Does the box itself retain the previously accepted clean internal illumination?
```

The hover timing no longer requires routine review because the project owner explicitly approved it as perfect.

## 8. Exact continuation

```text
1. use v1-cockpit-design-exploration and Checkpoint 216
2. preserve G4 as the provisionally settled grid/world direction
3. preserve H4 as the selected interaction-lighting direction
4. preserve the currently approved hover-entry and hover-release timing
5. pull the latest branch locally
6. refresh /design-lab/work-unit-lighting.html
7. inspect only whether the resting spill now extends farther into the grid without increasing in-box light
8. once interaction lighting is sufficiently settled, proceed into deeper work-unit visual grammar
9. keep production Cockpit implementation untouched until later integrated evidence warrants promotion
10. keep source-vault deployment paused until explicitly resumed
```
