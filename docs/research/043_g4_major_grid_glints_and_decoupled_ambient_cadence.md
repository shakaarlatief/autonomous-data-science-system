# Research 043: G4 Major-Grid Glints and Decoupled Ambient Cadence

**Date:** 2026-08-26

## Status

Active Phase-C product-design evidence. This document records a human refinement to the selected G4 Adaptive Hybrid grid/world substrate. It does not promote production Cockpit implementation.

## Preserved direction

The following remain active:

```text
G4 Adaptive Hybrid          selected grid/world substrate
Dark mode                   active visual-design baseline
Light mode                  deferred
Travelling grid currents    retained
Intersection glints         retained
Ambient drift               retained
Lively current cadence      preferred
```

## Human refinement

Browser review of the randomized ambient experiment found that glints were technically snapped to the 20 px lattice, but this placed them on corners of the minor grid cells rather than the visibly stronger major grid boxes.

The requested refinement is:

```text
currents
    retain Quiet / Balanced / Lively cadence control
    Lively remains preferred
    continue to randomize across the full minor/major grid world

glints
    become an independent quiet accent
    do not accelerate when currents are set to Lively
    appear only at intersections of the 100 px major grid
    remain randomly distributed among those major intersections
```

This deliberately decouples decorative mechanisms that serve different visual roles.

## Implementation in the isolated design lab

`frontend/design-lab/grid-dynamics-combined.js` now uses separate constants:

```text
minor lattice step   20 px
major lattice step   100 px
```

Currents continue to snap to arbitrary 20 px grid lines so they can traverse the full world with spatial variety.

Glints now choose both x and y from valid 100 px major-grid coordinates. Their scheduler is independent of the ambient intensity preset and uses approximately Quiet timing with at most two concurrent glints.

The current intensity selector therefore primarily controls current and ambient-drift cadence. It no longer forces glints to become frequent under Lively.

## Review question

The next browser check should verify:

```text
1. glints occur only on corners of the large 100 px grid boxes
2. glints remain rare enough to read as occasional accents
3. Lively currents retain the preferred frequency and spatial randomness
4. the combined world still feels alive without sparkle-like noise
```

## Production boundary

No production Cockpit components, route architecture, graph library, motion library, or final visual-system decision is authorized by this refinement.
