# Research 042: G4 Randomized Ambient Distribution and Grid-Intersection Glints

**Date:** 2026-08-26  
**Status:** Active browser-design refinement, pending human review  
**Scope:** Refines the selected G4 Adaptive Hybrid dark-mode substrate after direct human review of the combined ambient-dynamics experiment.  
**Authority:** Product-design evidence only. Specification 008 remains the promoted Cockpit interaction architecture.  
**Interaction session:** `chatgpt-07`  
**Conversation title:** `07 - Project Cockpit Design Exploration`

## 1. Human review result carried forward

The project owner prefers the `Lively` ambient cadence and wants all four surviving mechanisms retained:

```text
travelling grid currents
intersection glints
ambient light drift
localized semantic activity
```

The combined ambient world should therefore remain visibly alive rather than returning to the earlier very sparse treatment.

## 2. Fixed-coordinate repetition was rejected

The previous combined experiment reused a small number of fixed current rows/columns and glint positions. That made repeated observation reveal the implementation pattern, for example a vertical current repeatedly appearing on the same right-side grid line.

This is not the intended visual behavior.

The new requirement is:

```text
ambient decoration should be spatially stochastic
    while
remaining geometrically coherent with the grid
```

Randomness should affect where and when the decoration appears, not destroy the spatial logic of the substrate.

## 3. Grid currents

Current segments now satisfy:

```text
horizontal OR vertical
position chosen dynamically across the full visible world
position snapped to a real 20 px grid line
start point varies
travel direction varies
travel distance varies
segment length varies
appearance timing varies
```

The current should therefore be capable of appearing on essentially any visible horizontal or vertical grid line rather than cycling through authored coordinates.

`Quiet`, `Balanced`, and `Lively` remain cadence presets. The preferred human direction entering this refinement is `Lively`.

## 4. Glints

Glints should not float at arbitrary sub-grid coordinates.

The accepted geometric rule for this experiment is:

```text
glint center = exact grid-line intersection
```

The G4 substrate uses a 20 px minor grid with stronger 100 px major divisions. Runtime glints snap both x and y coordinates to the 20 px lattice, so every glint lands on the corner of an actual visible grid cell.

This preserves the decorative sparkle while making it feel native to the world rather than overlaid randomly on top of it.

## 5. Ambient drift

The broad low-opacity light fields are also re-seeded dynamically:

```text
starting position varies
size varies
travel vector varies
opacity varies within the active intensity preset
```

Unlike currents and glints, drift is not snapped to grid geometry because its purpose is atmospheric depth rather than precise lattice signaling.

## 6. Semantic versus ambient separation remains intact

The design still separates:

```text
AMBIENT
    decorative current
    decorative glint
    decorative drift

SEMANTIC
    localized project-state activity field
    live project relation/runtime cues
```

Randomized ambient decoration must remain visually subordinate to semantic state even when the selected cadence is lively.

## 7. Runtime implementation strategy for this experiment

The previous CSS-only repeated coordinates are replaced by a small runtime ambient scheduler in:

```text
frontend/design-lab/grid-dynamics-combined.js
```

It creates transient DOM elements, assigns randomized grid-coherent geometry, removes them after animation completion, and re-schedules future events according to the selected cadence preset.

This remains isolated design-lab code. It is not a production architecture decision.

No graph library, motion library, renderer migration, or production Cockpit component is introduced.

## 8. Human review gate

The same URL and controls remain the review surface:

```text
http://localhost:5173/design-lab/grid-dynamics-combined.html

Quiet
Balanced
Lively
Ambient on/off
Semantic on/off
Reduced motion
```

The next human review should answer:

```text
do currents now genuinely feel spatially varied?
do glints reliably appear at grid-cell corners?
is Lively still the preferred cadence after spatial randomization?
should horizontal and vertical current probabilities remain approximately equal?
should any part of the randomized ambient field become more or less frequent?
```

## 9. Production boundary

This refinement does not authorize production Cockpit mutation.

G4 remains the selected substrate direction, dark remains the active design baseline, and light mode remains deferred until the core dark Cockpit system is substantially settled.