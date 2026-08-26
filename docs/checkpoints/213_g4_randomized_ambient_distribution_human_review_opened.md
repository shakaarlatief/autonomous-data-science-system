# Checkpoint 213: G4 Randomized Ambient Distribution Human Review Opened

**Date:** 2026-08-26  
**Status:** Current product-design checkpoint  
**Checkpoint class:** CONTINUITY / PRODUCT_DESIGN / HUMAN_REVIEW  
**Project stage:** V1 next-generation Project Cockpit browser-rendered design exploration  
**Scope:** Records the human preference for Lively combined G4 ambient motion, rejects fixed-coordinate repetition, refines currents/glints/drift into spatially re-seeded runtime behavior, and opens direct human review of the randomized distribution without authorizing production Cockpit mutation.  
**Authority:** Current product-design routing/evidence boundary only. Specification 008 remains the promoted Cockpit interaction architecture.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** chatgpt-07  
**Conversation title:** 07 - Project Cockpit Design Exploration  
**Primary collaborator:** ChatGPT

## 1. Current accepted direction inside Phase C

The following product-design choices remain active:

```text
G4 Adaptive Hybrid          selected grid/world substrate
Dark mode                   active visual-design baseline
Light mode                  deferred until the dark Cockpit is substantially settled
Ambient decorative motion   allowed and desired
Lively cadence              current human preference
```

This is still design evidence rather than a promoted production visual specification.

## 2. Human refinement request

After inspecting the combined G4 dynamics experiment, the project owner requested two concrete changes:

```text
1. currents must not repeat on fixed authored rows/columns
   they should be able to appear anywhere across the grid

2. glints must occur at actual grid-box corners / line intersections
   rather than at arbitrary visual coordinates
```

The same spatial-randomization principle should apply to other ambient effects where meaningful.

## 3. Experiment updated in place

The review surface remains:

```text
frontend/design-lab/grid-dynamics-combined.html
frontend/design-lab/grid-dynamics-combined.css
frontend/design-lab/grid-dynamics-combined.js
```

Expected local URL:

```text
http://localhost:5173/design-lab/grid-dynamics-combined.html
```

The existing controls remain:

```text
Quiet
Balanced
Lively
Ambient on/off
Semantic on/off
Reduced motion
```

## 4. Runtime distribution behavior

The revised design-lab engine now creates transient randomized ambient elements.

### Currents

```text
random horizontal / vertical orientation
random grid line across the full visible canvas
coordinates snapped to the 20 px lattice
random start position
random direction
random travel distance
random segment length
random timing
```

### Glints

```text
random x grid coordinate
random y grid coordinate
both snapped to 20 px
therefore every glint lands at an actual grid intersection
```

### Ambient drift

```text
random start position
random size
random movement vector
random opacity within preset bounds
```

The semantic activity layer remains separate and is not randomized as decoration.

## 5. Production boundary remains unchanged

Only isolated design-lab code and design/routing documentation are authorized here.

Still not authorized:

```text
production Cockpit component replacement
production route mutation
final graph/canvas technology selection
final motion architecture
final semantic connector architecture
light-mode production redesign
```

## 6. Current human gate

The project owner should pull the latest `v1-cockpit-design-exploration` branch, refresh the existing combined dynamics URL, and inspect especially the `Lively` preset for long enough to observe multiple re-seeded events.

The review question is now distribution quality rather than mechanism selection:

```text
are currents convincingly spread across the grid?
are glints anchored to grid-cell corners?
does Lively remain the preferred cadence?
should any ambient mechanism be tuned further?
```

## 7. Source-vault pause

The permanent source-vault bootstrap remains paused, preserved, and unchanged. The Course 2 recovery-integrity gate is unaffected.

## 8. Exact continuation

```text
1. use v1-cockpit-design-exploration and Checkpoint 213
2. keep G4 + dark-first + all ambient mechanisms
3. pull latest branch locally
4. refresh /design-lab/grid-dynamics-combined.html
5. inspect Quiet / Balanced / Lively, with emphasis on Lively
6. verify currents appear across many rows and columns
7. verify glints land on real grid intersections
8. record human disposition
9. tune if necessary
10. only after the grid/world layer is sufficiently settled, open the next bounded Cockpit design slice
```