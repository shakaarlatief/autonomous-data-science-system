# Checkpoint 216: H4 Selected, Resting World-Spill Human Review Opened

**Date:** 2026-08-26  
**Status:** Current product-design checkpoint  
**Checkpoint class:** CONTINUITY / PRODUCT_DESIGN / HUMAN_REVIEW  
**Project stage:** V1 next-generation Project Cockpit browser-rendered design exploration  
**Scope:** Records selection of H4 Integrated Response as the preferred work-unit interaction-lighting direction and the subsequent resting-light refinement: preserve the clean localized H4 rest treatment, reject a broad circular resting halo, and add only a narrow soft node-colored spill into the surrounding G4 grid from the left/accent side.  
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
subtle left/accent-side resting spill into the grid
full hover halo
pointer-following hotspot
local grid illumination on hover
immediate connector emphasis
single restrained perimeter sweep on hover entry
small hover depth lift
```

## 3. Resting-light refinement and rejection evidence

The project owner liked the clean H4 light treatment inside and immediately around the work-unit box, but wanted a little more of that same node-colored light to continue into the surrounding grid in the normal resting state, especially around the left/accent side of the box.

An initial implementation interpreted that request as a substantially broader radial resting glow around the node. Human review rejected that treatment because it created a conspicuous bright circular halo, made the result visually heavier, and lost the clean/subtle character of the preferred treatment.

The accepted refinement target is therefore:

```text
keep the original clean localized resting light
+
add only a narrow soft continuation into the grid
+
concentrate that continuation around the left/accent side
+
do not create a broad circular resting halo
+
retain the richer full H4 response on hover
```

This is an important distinction between resting atmosphere and interaction lighting. Rest should remain precise and restrained. Hover may become substantially richer because it is transient and directly tied to user interaction.

## 4. Browser experiment canonicalization

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

H4 now inherits the same clean localized base resting light and adds a separate narrow left/accent-side grid spill. The rejected broad radial resting treatment is no longer the native H4 CSS behavior. The temporary JavaScript style injection that had been used to correct the visual treatment has been removed; the accepted behavior is represented directly in the stylesheet.

H1-H3 remain useful comparison evidence. The richer H4 hover mechanisms remain unchanged.

## 5. Production boundary

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

## 6. Human review gate

The next review should answer:

```text
Does H4 retain the clean subtle resting appearance that was preferred?
Does the narrow left/accent-side light extend enough into the grid without becoming a visible circular halo?
Does the box itself retain the newer cleaner internal illumination?
Does hover still feel clearly richer than rest?
```

## 7. Exact continuation

```text
1. use v1-cockpit-design-exploration and Checkpoint 216
2. preserve G4 as the provisionally settled grid/world direction
3. preserve H4 as the selected interaction-lighting direction
4. preserve the rejection of a broad circular resting halo
5. preserve the narrow soft left/accent-side resting grid spill as the current refinement
6. pull the latest branch locally
7. refresh /design-lab/work-unit-lighting.html
8. inspect H4 both at rest and on hover
9. refine the narrow resting spill only if human review still finds it too strong or too weak
10. once interaction lighting is sufficiently settled, proceed into deeper work-unit visual grammar
11. keep production Cockpit implementation untouched until later integrated evidence warrants promotion
12. keep source-vault deployment paused until explicitly resumed
```
