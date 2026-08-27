# Research 077: Fullscreen Specialist Workspace and Spatial Zoom Transition Experiment

**Date:** 2026-08-27  
**Status:** Active Phase-C interaction-design evidence  
**Scope:** Narrows the deep-focus transition question after the project owner expressed a strong preference that the deepest specialist workspace fully replace the project map, while retaining the compact topology compass, and requested more advanced spatial zoom / through-space transition concepts.  
**Authority:** Research evidence only. The fullscreen end state and compass are strong current preferences for this slice, but final production deep-focus architecture, transition choreography, motion timing, return behavior and workspace composition remain unfrozen.

## 1. Human trigger

The project owner reviewed the Claude-informed factorized browser and clarified two things.

First, the deepest specialist workspace should feel deeper than the current retained-map treatments:

```text
if this is the deepest / biggest box,
the grid should no longer be visible
and the specialist workspace should become the whole page,
closer to Hard Replace
```

Second, the compact topology compass was positively received:

```text
I really like the compass.
It is a nice small detailed feature.
```

The project owner then requested a more advanced spatial transition concept:

```text
zoom into the box
or the background zooming out or in
moving through the space
```

This is interpreted as a request to test spatial depth and camera-like movement rather than another set of map-retention amounts.

## 2. Revised factorization

Research 076 separated transition dimensions. This follow-up now holds the end state constant:

```text
DEEPEST SPECIALIST WORKSPACE END STATE

workspace
    fullscreen inside the Cockpit stage

project grid / map
    fully absent after transition completes

orientation aid
    compact topology compass retained

source state
    selected X5 expanded work unit

workspace internals
    schematic and unfrozen
```

This lets the new browser vary only:

```text
SPATIAL TRANSITION CHOREOGRAPHY
    how does the user feel they moved
    from the project-map depth layer
    into the specialist-workspace depth layer?
```

The current hypothesis is that a stronger spatial metaphor may better match the Cockpit's already-promoted geometric zoom and navigable-world architecture than a simple modal-like expansion.

## 3. New browser

Local route:

```text
http://localhost:5173/design-lab/work-unit-deep-focus-spatial-zoom.html
```

Files:

```text
frontend/design-lab/work-unit-deep-focus-spatial-zoom.html
frontend/design-lab/work-unit-deep-focus-spatial-zoom.css
frontend/design-lab/work-unit-deep-focus-spatial-zoom-refinement.css
frontend/design-lab/work-unit-deep-focus-spatial-zoom.js
```

Exact latest implementation target:

```text
b375eb253990ce3c20f34dd9d5b735bd532789f2
```

Production `/cockpit` remains untouched.

## 4. Controlled candidates

All candidates begin from the same off-center selected X5 card and end in the same fullscreen specialist workspace with the same compass.

```text
Z0  Direct Replace Control
    baseline fade / replace
    minimal spatial metaphor

Z1  Card Zoom-In
    selected work unit grows toward the viewer
    surrounding world is swallowed behind it

Z2  World Falls Away
    project world recedes rapidly into depth
    selected card pushes forward

Z3  Camera Dive
    camera appears to move through the selected work unit
    grid and world rush outward past the viewport

Z4  Workspace Aperture
    selected work unit becomes an aperture containing the workspace
    aperture expands until it fills the stage

Z5  Depth Parallax
    surrounding work units move outward on separate depth vectors
    selected work advances into the workspace

Z6  Perspective Corridor
    project grid tilts into a perspective corridor / floor
    camera appears to travel through the world into deep focus

Z7  Pull-Back Then Dive
    brief backward movement first establishes depth
    then camera accelerates through the selected work unit
```

Z0 is retained as the simplest control. Z1-Z7 are deliberately more spatial and cinematic, but still restrained enough to test in a professional technical interface.

## 5. Dynamic source origin

The selected X5 card is deliberately off-center.

JavaScript measures its actual rendered rectangle and writes:

```text
origin left / top
origin width / height
origin center x / y
origin right / bottom
```

into CSS custom properties for each scene.

This means source-relative transitions are not special-cased to the center of the viewport.

Z4 uses the measured card rectangle as the initial clip-path aperture, then expands it to the full stage.

## 6. Compass treatment

The topology compass is now held constant across every deep-focus end state in this browser.

The intended distinction is:

```text
project map / grid
    navigation surface
    disappears in deep focus

compact topology compass
    orientation / return anchor
    survives in deep focus
```

This is not yet a final production minimap specification. Exact size, placement, topology abstraction, interaction and semantic detail remain unfrozen.

## 7. Fullscreen meaning

"Fullscreen" in this research means the specialist workspace owns the entire active Cockpit stage rather than remaining a framed card above the project map.

It does not yet decide whether production deep focus uses browser Fullscreen API, hides every application-level chrome surface, or changes URL / browser-history semantics. Those remain separate production questions.

## 8. Reduced motion

All spatial movement is presentation-only.

```text
prefers-reduced-motion
    transitions collapse to effectively instant
    same fullscreen specialist-workspace end state
    same compass orientation aid
```

No semantic meaning depends on motion.

## 9. Human review gate

The new review should judge:

```text
which spatial mechanism most feels like entering the selected work unit?
which makes the transition feel like moving through a navigable project world?
which remains controlled rather than theatrical?
which remains comfortable when repeated many times?
which preserves clear object continuity from X5 into deep focus?
is the compact compass enough orientation once the full map disappears?
```

The project owner may prefer, reject, combine or refine mechanisms. Exact timing and easing remain deliberately unfrozen.

## 10. Checkpoint disposition

No new checkpoint is created.

This is a broadened and narrowed executable comparison inside the existing Checkpoint 243 deep-focus-transition review gate:

```text
Research 075
    initial F0-F8 architectures

Research 076
    Claude-informed factorization

Research 077
    fullscreen end-state hypothesis
    + spatial zoom / through-space transition comparison
```

A new checkpoint becomes warranted when the human review actually settles a materially new deep-focus architecture or otherwise changes the current product-design boundary.
