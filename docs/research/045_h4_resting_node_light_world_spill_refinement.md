# Research 045: H4 Resting Node-Light World-Spill Refinement

**Date:** 2026-08-26  
**Status:** Active Phase-C product-design evidence  
**Interaction environment:** ChatGPT  
**Interaction session:** chatgpt-07  
**Conversation title:** 07 - Project Cockpit Design Exploration

## Human disposition

The project owner reviewed the work-unit interaction-lighting variants and selected:

```text
H4 Integrated Response  SELECTED interaction-lighting direction
```

The selected mechanisms are currently:

```text
localized colored light at rest
fuller node-colored hover halo
pointer-following surface hotspot
local grid/world illumination on hover
immediate connector emphasis on hover
one restrained perimeter sweep on hover entry
small depth lift on hover
```

The project owner then refined the resting-state light. The newer H4 treatment looked good inside the node, but the earlier G4 node treatment projected more colored light into the surrounding grid. The desired result combines both qualities rather than choosing one.

## Refined resting-light hypothesis

At rest, a work unit should feel embedded in and softly illuminating the spatial world.

The resting treatment therefore now has two complementary layers:

```text
near-node rest light
    preserves the colored illumination in and immediately around the left side of the node

broader world bleed
    extends the same node color farther into the grid
    asymmetric and soft rather than a complete neon halo
    visible without pointer interaction
```

The broader bleed deliberately remains strongest near the semantic accent side of the work unit. This preserves hierarchy and avoids making every resting work unit look like a uniformly glowing rectangle.

On hover, H4 still expands into the richer interactive response. The resting world bleed becomes less dominant while the full hover halo, pointer hotspot, hover world spill, connector response and perimeter sweep take over.

## Implementation evidence

Updated isolated design-lab surface:

```text
frontend/design-lab/work-unit-lighting.css
```

The H4-specific refinement adds:

```text
1. a larger and stronger H4 rest-light envelope
2. an additional low-opacity asymmetric world-bleed layer behind each H4 node
3. smooth transition into the richer H4 hover state
```

No production Cockpit component is changed.

## Current design interpretation

This is still a visual hypothesis, not a final production specification. The selected H4 lighting direction can still be adjusted as work-unit visual grammar, semantic states, connectors and focus behavior are designed together.

The grid/world substrate remains provisionally settled and may also be revisited later if integrated evidence warrants it.
