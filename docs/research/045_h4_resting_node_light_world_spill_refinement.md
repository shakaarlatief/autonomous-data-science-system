# Research 045: H4 Resting Node-Light World-Spill Refinement

**Date:** 2026-08-26  
**Status:** Completed Phase-C product-design evidence  
**Interaction environment:** ChatGPT  
**Interaction session:** chatgpt-07, completed in chatgpt-08  
**Conversation title:** 07 - Project Cockpit Design Exploration, continued in 08 - Project Cockpit Design Exploration

## Human disposition

The project owner reviewed the work-unit interaction-lighting variants and selected:

```text
H4 Integrated Response  SELECTED interaction-lighting direction
```

The selected mechanisms are:

```text
localized colored light at rest
fuller node-colored hover halo
pointer-following surface hotspot
local grid/world illumination on hover
immediate connector emphasis on hover
one restrained perimeter sweep on hover entry
small depth lift on hover
```

The project owner then refined the resting-state light. The newer H4 treatment looked good inside the node, but the earlier G4 node treatment projected more colored light into the surrounding grid. The desired result combined both qualities rather than choosing one.

## Refined resting-light result

At rest, a work unit should feel embedded in and softly illuminating the spatial world.

The accepted treatment uses two complementary layers:

```text
near-node rest light
    preserves the accepted colored illumination in and immediately around the node

narrow asymmetric world spill
    extends the same node color farther into the surrounding grid
    strongest through the semantic accent / left side
    visible without pointer interaction
    does not broaden into a generalized circular halo
```

A broader circular resting halo was explicitly rejected because it made the node feel surrounded by a generalized neon cloud and weakened the cleaner precision of H4.

A later reach increase also unintentionally strengthened the spill inside the card. That was corrected. The final reviewed treatment preserves the accepted in-box illumination while extending the additional light outward into the grid only.

## Hover-release result

Video review showed that the first H4 hover state ended too abruptly when the pointer left the work unit.

The accepted timing principle became asymmetric:

```text
pointer enters
    immediate and crisp response

pointer leaves
    light, depth, connector emphasis and world spill decay more gradually
    perimeter sweep resolves with a longer, softer final fade
```

The project owner subsequently judged the revised hover animation to be perfect. That timing should be preserved unless later integrated evidence exposes a new problem.

## Final human review

After pulling the final outward-only resting-spill correction at branch head `bdf021d90b9a849cd2c9f992e0e18e1cc6deb80a`, the project owner reviewed H4 again and judged the result good.

The current interaction-lighting disposition is therefore:

```text
H4 Integrated Response             SELECTED
resting in-box illumination        ACCEPTED
outward left-side resting spill    ACCEPTED
broad circular resting halo        REJECTED
hover-entry timing                  ACCEPTED
hover-release timing                ACCEPTED
```

No further lighting-only variant is currently justified.

## What remains intentionally for later integrated slices

The closure of this slice does not imply that light can never change again.

Several later project-state questions may use lighting as one visual channel, but they should be tested in the context of those semantic states rather than by continuing to tune generic hover lighting now:

```text
selected / focused persistent treatment
running / queued / waiting state
blocked / approval-required state
final semantic category palette
integration with final work-unit silhouette/category grammar
integration with connector semantics and semantic zoom
```

These are different design questions. They should not keep the H4 hover/rest slice artificially open.

## Implementation evidence

Current isolated design-lab surface:

```text
frontend/design-lab/work-unit-lighting.html
frontend/design-lab/work-unit-lighting.css
frontend/design-lab/work-unit-lighting.js
```

No production Cockpit component is changed by this evidence.

## Design interpretation

H4 is the provisionally settled work-unit interaction-lighting direction for the next design slices.

It remains a design-lab result rather than a final production visual specification. Later integrated evidence may justify adjustment, but the project should now stop micro-tuning generic rest/hover lighting and proceed to deeper work-unit visual grammar.
