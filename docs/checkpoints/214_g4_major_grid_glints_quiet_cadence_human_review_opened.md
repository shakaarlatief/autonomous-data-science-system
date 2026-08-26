# Checkpoint 214: G4 Major-Grid Glints and Quiet Glint Cadence Human Review Opened

**Date:** 2026-08-26  
**Status:** Current product-design checkpoint  
**Checkpoint class:** CONTINUITY / PRODUCT_DESIGN / HUMAN_REVIEW  
**Project stage:** V1 next-generation Project Cockpit browser-rendered design exploration  
**Scope:** Records the human refinement that G4 currents should retain Lively cadence and full-grid spatial randomness while glints should appear only at major-grid intersections and remain approximately Quiet regardless of the current intensity preset.  
**Authority:** Current product-design routing/evidence boundary only. Specification 008 remains the promoted Cockpit interaction architecture.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** chatgpt-07  
**Conversation title:** 07 - Project Cockpit Design Exploration  
**Primary collaborator:** ChatGPT

## 1. Preserved human-selected direction

```text
G4 Adaptive Hybrid          SELECTED
Dark mode                   current design baseline
Light mode                  deferred
Travelling currents         KEEP
Ambient drift               KEEP
Intersection glints         KEEP
Lively current cadence      PREFERRED
```

## 2. New refinement

The project owner clarified that the glints should not use the minor 20 px grid intersections.

They should instead appear only at the corners of the visibly larger grid boxes, meaning intersections of the 100 px major grid.

The project owner also requested different cadence behavior for currents and glints:

```text
currents
    Lively remains preferred
    randomized across the grid

glints
    approximately Quiet
    rare accent rather than frequent sparkle
    independent of Quiet / Balanced / Lively current selection
```

## 3. Browser experiment updated

The existing review surface remains:

```text
frontend/design-lab/grid-dynamics-combined.html
frontend/design-lab/grid-dynamics-combined.css
frontend/design-lab/grid-dynamics-combined.js
```

Expected local URL:

```text
http://localhost:5173/design-lab/grid-dynamics-combined.html
```

The implementation now separates:

```text
GRID_STEP        20 px   currents may use any grid line
MAJOR_GRID_STEP 100 px   glints may use only major intersections
```

Glint scheduling is independent from the intensity selector and remains approximately Quiet, with long gaps and low concurrency.

## 4. Human review gate

The next browser review should determine:

```text
are glints now exactly on corners of the large grid boxes?
are they rare enough?
do Lively currents still feel right?
does the combined world feel polished rather than sparkly?
```

## 5. Production boundary

No production Cockpit implementation is authorized. The isolated design lab remains the only implementation surface changed by this refinement.

## 6. Source-vault pause

The permanent source-vault bootstrap remains paused, preserved, and unchanged. The Course 2 recovery-integrity gate is unaffected.

## 7. Exact continuation

```text
1. use v1-cockpit-design-exploration and Checkpoint 214
2. preserve G4, dark-first, and Lively current preference
3. pull latest branch locally
4. refresh /design-lab/grid-dynamics-combined.html
5. verify glints land only on 100 px major-grid intersections
6. verify glints remain approximately Quiet while currents can stay Lively
7. record human disposition
8. tune again only if needed
9. close the grid/world slice provisionally once its character is sufficiently settled
10. then open the next bounded Cockpit design slice
```
