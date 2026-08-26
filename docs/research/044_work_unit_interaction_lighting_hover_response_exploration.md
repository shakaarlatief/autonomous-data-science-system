# Research 044: Work-Unit Interaction Lighting and Hover Response Exploration

**Date:** 2026-08-26  
**Status:** ACTIVE PRODUCT-DESIGN RESEARCH / HUMAN EVALUATION  
**Project stage:** V1 next-generation Project Cockpit browser-rendered design exploration  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** chatgpt-07  
**Conversation title:** 07 - Project Cockpit Design Exploration

## 1. Boundary

The G4 Adaptive Hybrid grid/world layer is now provisionally settled for the current design sequence.

That does not mean the grid is permanently frozen. It means the current evidence is strong enough to stop tuning it continuously and move to the next bounded question while preserving the option to revisit it later.

Current preserved grid/world direction:

```text
G4 Adaptive Hybrid             selected substrate
Dark mode                      current baseline
Light mode                     deferred
Currents                       randomized, Lively preferred
Glints                         100 px major-grid intersections only
Glint cadence                  approximately Quiet and independent
Ambient drift                  retained
Localized semantic activity    retained
```

The next question is not yet the complete final work-unit grammar. The first bounded work-unit slice isolates **interaction lighting**.

## 2. Human design hypothesis

The project owner explicitly liked the colored light treatment around work units and proposed stronger color-specific response on hover.

Representative desired behavior:

```text
rest
    localized / asymmetric colored atmosphere
    quiet enough for long sessions

hover
    node-specific color becomes more visible
    full box may illuminate
    response should feel premium and dynamic

selected / active / running
    later slices may use stronger persistent or semantic treatments
```

A yellow Question should therefore be capable of producing a yellow hover response; other semantic categories should respond in their own representative color.

## 3. Why asymmetric rest lighting is retained for comparison

A full bright perimeter around every node at rest risks making the Cockpit look like a field of neon cards.

The current hypothesis is therefore:

```text
REST       localized / asymmetric / atmospheric
HOVER      fuller / responsive / brighter
SELECTED   persistent focus treatment, later slice
RUNTIME    state-bearing semantic treatment, later slice
```

This hierarchy is a hypothesis to test, not a final design specification.

## 4. Browser experiment

New isolated design-lab surface:

```text
frontend/design-lab/work-unit-lighting.html
frontend/design-lab/work-unit-lighting.css
frontend/design-lab/work-unit-lighting.js
```

Expected local URL:

```text
http://localhost:5173/design-lab/work-unit-lighting.html
```

The G4 world is held visually constant across the four treatments.

The node categories/colors remain representative and are not yet a frozen semantic palette.

## 5. H1 Full Halo

```text
rest
    localized left-side glow

hover
    full colored perimeter halo
    brighter semantic accent edge
    small 2 px depth lift
```

Purpose:

- determine whether a full colored hover halo is already sufficient;
- establish the lowest-complexity responsive baseline.

Risk:

- may feel too conventional or insufficiently integrated with the world.

## 6. H2 Cursor Edge

Adds a pointer-proximity/specular light field.

```text
hover
    H1 full halo
    + localized hotspot follows pointer position across the box
```

Purpose:

- test whether pointer-responsive lighting adds tactile/premium character;
- judge whether the interaction feels physically responsive rather than merely highlighted.

Risk:

- may become distracting if too strong or too continuously noticeable.

## 7. H3 World Spill

Adds local environmental response.

```text
hover
    full node halo
    nearby grid softly inherits node color
    immediate connected paths become clearer
```

Purpose:

- make work units feel embedded in the G4 project world rather than layered on top of it;
- combine aesthetic response with useful topology emphasis.

Risk:

- colored world spill could muddy the grid or visually overstate hover importance.

## 8. H4 Integrated Response

Combines the strongest candidate mechanisms:

```text
localized rest light
full hover perimeter
pointer-following hotspot
local grid illumination
immediate connector emphasis
single restrained perimeter sweep on hover entry
small depth lift
```

The perimeter sweep occurs once when hover begins. It is not a looping animation.

Purpose:

- test the richest plausible interaction before deciding which mechanisms actually deserve to survive.

Risk:

- too many individually attractive mechanisms can still combine into over-animation.

## 9. Important non-decisions

This experiment does **not** freeze:

```text
final work-unit shapes
final semantic category colors
final status palette
final selected-state treatment
final runtime-state lighting
final blocked-state treatment
final card dimensions
final typography
final connector vocabulary
final 2.5D depth system
production animation implementation
production motion library
```

It isolates hover/interaction lighting only.

## 10. Human evaluation questions

The project owner should compare the variants directly in the browser and may combine rather than select literally.

Questions:

```text
1. should the full-perimeter colored hover halo survive?
2. is pointer-following/specular light attractive or distracting?
3. should nearby grid geometry inherit a faint node color on hover?
4. should immediate connectors become clearer on hover?
5. is the one-time perimeter sweep worth retaining?
6. is the 2 px depth lift noticeable in a good way?
7. should rest lighting remain asymmetric/localized?
```

## 11. Reduced-motion principle

The design lab exposes a reduced-motion toggle.

In reduced motion:

- the perimeter sweep is removed;
- transitions become immediate;
- static hover emphasis remains available.

The final production accessibility behavior remains to be designed later.

## 12. Production boundary

All implementation remains under:

```text
frontend/design-lab/**
```

No production Cockpit component, route, renderer, graph library or motion architecture is changed by this research slice.

## 13. Expected continuation

```text
human reviews H1-H4
-> preserve / reject / combine mechanisms
-> refine once if needed
-> then continue deeper work-unit visual grammar
   shape / category identity / status / selected / runtime treatment
```
