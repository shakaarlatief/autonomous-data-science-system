# Checkpoint 211: G4 Selected, Dark-First Baseline Frozen, Ambient Dynamics Review Opened

**Date:** 2026-08-26  
**Status:** Current product-design checkpoint  
**Checkpoint class:** CONTINUITY / PRODUCT_DESIGN / HUMAN_REVIEW  
**Project stage:** V1 next-generation Project Cockpit browser-rendered design exploration  
**Scope:** Records the project owner's selection of G4 Adaptive Hybrid from the first grid/world comparison, freezes dark mode as the current visual-design baseline while deferring light-mode optimization, preserves the explicit allowance for restrained decorative ambient motion, and opens a second browser-rendered design slice comparing subtle G4 dynamics.  
**Authority:** Current routing and human product-direction evidence. Specification 008 remains the promoted V1 Cockpit interaction architecture. No production visual implementation is promoted here.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** chatgpt-07  
**Conversation title:** 07 - Project Cockpit Design Exploration  
**Primary collaborator:** ChatGPT

## 1. G4 is selected

The project owner directly reviewed G1-G4 in the browser design lab and selected:

```text
G4  Adaptive Hybrid
    SELECTED
```

G1-G3 are not retained as primary substrate candidates.

The selection is based on direct visual preference rather than model recommendation alone. G4 was judged the best-looking and most compelling substrate, including its localized light treatment.

This freezes the direction, not every styling constant.

## 2. Dark-first is now the explicit design sequence

Current visual evaluation should optimize for dark mode first.

```text
DARK
    canonical current design-review baseline

LIGHT
    deferred until the core Cockpit visual system is substantially settled
    not a constraint on current dark-mode decisions
```

Light mode is not permanently rejected. It is deliberately sequenced later as its own design problem rather than forcing every experimental mechanism to work equally well in both appearances from the beginning.

## 3. Decorative motion is allowed

The project owner explicitly clarified that decorative visual behavior can be desirable even when it does not encode semantic project state.

The project now distinguishes:

```text
semantic motion
    higher-salience
    communicates real project/runtime change

ambient motion
    decorative
    lower-salience
    slow and sparse
    must not masquerade as semantic state
```

The design goal is not a completely static world. It is a world that can feel subtly alive without becoming rapid, random, or distracting.

## 4. Research 040 governs the new slice

Primary artifact:

```text
docs/research/040_grid_world_g4_selection_dark_first_and_ambient_dynamics_exploration.md
```

It records the G4 decision, dark-first sequencing, semantic/ambient distinction, and the D1-D4 dynamics hypotheses.

## 5. Slice 02 browser lab

New isolated experiment:

```text
frontend/design-lab/grid-dynamics.html
frontend/design-lab/grid-dynamics.css
frontend/design-lab/grid-dynamics.js
```

Expected local URL:

```text
http://localhost:5173/design-lab/grid-dynamics.html
```

The G4 substrate and project fixture remain constant.

Variants:

```text
D1 Quiet Current
    sparse slow light segments travelling along major grid lines

D2 Intersection Glints
    rare small intersection pulses

D3 Ambient Drift
    broad very-low-opacity moving light fields below the grid

D4 Restrained Hybrid
    lower-intensity combination of trace + glint + drift
```

## 6. Inspection controls

The dynamics lab exposes:

```text
Ambient ON/OFF
Semantic ON/OFF
Reduced motion ON/OFF
Focus variant
```

This explicitly tests whether decorative life improves the environment while keeping real semantic activity visibly dominant.

## 7. Production Cockpit remains untouched

Allowed in this checkpoint:

```text
isolated design-lab files
human comparison
visual refinement
throwaway prototype behavior
```

Still not authorized:

```text
replacement of production Cockpit components
production route migration
new graph library
new motion library
final visual-system freeze
final semantic connector architecture
```

## 8. MC-0004 remains in Phase C

```text
Phase A   complete / Claude independent
Phase B   complete / Claude comparative
Phase C   active / browser-rendered human design evaluation
```

The next expected actor remains the human project owner after ChatGPT provides the new dynamics lab.

## 9. Source-vault pause remains unchanged

```text
source-vault bootstrap
    PAUSED
    not cancelled
    not rejected
    not superseded
    Course 2 recovery-integrity gate unchanged
```

## 10. Exact continuation

```text
1. use v1-cockpit-design-exploration and Checkpoint 211 as the current route
2. keep G4 Adaptive Hybrid as the selected grid/world substrate
3. evaluate dark mode only for the current dynamics slice
4. inspect D1-D4 live in the browser
5. use Ambient/Semantic toggles to verify hierarchy
6. record preferred/rejected/combine/refine human disposition
7. refine G4 ambient dynamics if needed
8. then open the next bounded design slice
9. keep production Cockpit implementation untouched until integrated prototype evidence warrants promotion
10. keep source-vault deployment paused until the project owner chooses to resume it
```
