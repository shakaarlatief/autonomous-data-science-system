# G4 Dynamic Source-Binding Supplement

**Status:** Required implementation-provenance supplement to M02  
**Date:** 2026-08-28  
**Machine-readable companion:** `docs/cockpit/g4_dynamic_source_binding_supplement.json`

## Purpose

The original M02 entry in `accepted_implementation_manifest.json` correctly preserved the held G4 behavior from Research 040-043, including randomized grid-coherent currents, Lively current cadence, major-grid-only quiet glints, random ambient drift and reduced-motion behavior.

However, its exact source binding pointed only to the later SEL2-compatible WorkUnit-grammar snapshot. That source is authoritative for the canonical WorkUnit/G4 substrate used by the selected node grammar, but it does not contain the later stochastic scheduler that Research 042-043 accepted.

Human integrated review exposed the consequence: the first replacement Cockpit still showed a small fixed set of repeating ambient currents and glints even though the semantic/invariant text in M02 described the correct stochastic behavior.

This is classified as:

```text
IMPLEMENTATION-PROVENANCE BINDING DEFECT

not
    lost human decision
not
    new design question
not
    permission to redesign G4
```

## Exact missing source

The later accepted G4 dynamics refinement is preserved at:

```text
3ec15a99b0d8103949c673eaf1dd16c3c9d00042
```

with exact blobs:

```text
frontend/design-lab/grid-dynamics-combined.html
    39eb149d1d4d8d7c11d41152b3bd1674761167c0

frontend/design-lab/grid-dynamics-combined.css
    f1cdca643ba02df7f3a8c139d8bec0bd10901b26

frontend/design-lab/grid-dynamics-combined.js
    39006a361e3ae15242b13f1b6048c3ba4a845b21
```

The same three blobs remain byte-identical on the current active branch at the time this supplement is created.

## Required integrated behavior

The combined M02 source graph must now be read as:

```text
SEL2-compatible G4/H4 WorkUnit substrate
    existing M02 binding

PLUS

latest stochastic ambient scheduler
    this supplement
```

The later scheduler requires:

```text
20 px minor grid
100 px major grid

travelling currents
    distributed across full visible world
    horizontal or vertical
    snapped to grid lanes
    varied position
    varied start
    varied direction
    varied travel
    varied segment length
    varied timing

Lively current cadence
    selected integrated direction

major-grid glints
    only at 100 px intersections
    random eligible intersection
    independent quiet scheduler
    max two concurrent
    not accelerated by Lively currents

ambient drift
    variable start
    variable size
    variable vector
    variable opacity

localized semantic activity
    separate from ambient decoration
    semantically higher salience

reduced motion
    no decorative ambient animation
```

## Integration rule

A future integrator may namespace or componentize the scheduler and may use logical-world dimensions instead of transformed screen bounds. It may not replace the stochastic behavior with fixed authored positions merely because an older composite WorkUnit fixture contains repeating ambient spans.

The machine-readable supplement is validated independently in CI until the primary manifest schema is migrated to support multiple exact historical source groups for one implementation obligation.

## Long-term schema implication

The defect reveals a limitation in the current one-target-per-entry manifest shape. One held mechanism can legitimately consist of a later refinement layered on top of an earlier compatible substrate.

A future manifest schema revision should support:

```text
one semantic implementation obligation
    -> multiple exact historical source groups
    -> explicit refinement ordering
```

Until then, this supplement is authoritative for the missing M02 dynamic source group and must be read together with the primary manifest.
