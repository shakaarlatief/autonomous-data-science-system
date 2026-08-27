# Research 077: Fullscreen Specialist Workspace and Spatial Zoom Transition Experiment

**Date:** 2026-08-27  
**Status:** Phase-C interaction-design evidence, human selection recorded  
**Scope:** Narrows the deep-focus transition question after the project owner expressed a strong preference that the deepest specialist workspace fully replace the project map, while retaining the compact topology compass, and requested more advanced spatial zoom / through-space transition concepts.  
**Authority:** Research evidence supporting the current Phase-C direction. Production implementation, exact timing/easing, return choreography, compass semantics and specialist-workspace composition remain unfrozen.

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

This was interpreted as a request to test spatial depth and camera-like movement rather than another set of map-retention amounts.

## 2. Revised factorization

Research 076 separated transition dimensions. This follow-up holds the end state constant:

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

The browser varies only:

```text
SPATIAL TRANSITION CHOREOGRAPHY
    how does the user feel they moved
    from the project-map depth layer
    into the specialist-workspace depth layer?
```

The governing hypothesis is that a stronger spatial metaphor better matches the Cockpit's already-promoted geometric zoom and navigable-world architecture than a modal-like expansion.

## 3. Browser

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

Exact selected/fixed implementation target:

```text
04616a52df5cceff6c59223bbd6f07448d027510
```

At this target the large interaction studio defaults to Z7 and the compass no longer visually overlaps the schematic top-right workspace panel.

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

## 5. Human selection

The project owner explicitly identified three strong candidates:

```text
Z2  liked
Z6  liked
Z7  liked
```

The specific human evidence was:

```text
Z6
    gives a bit of the 3D / 2.5D feeling

Z7
    nice and sharp
```

The project owner hesitated between Z6 and Z7, then selected:

```text
Z7  Pull-Back Then Dive
    SELECTED current Phase-C deep-focus entry direction
```

Interpretation:

```text
entry
    short controlled pull-back
    establishes depth / spatial anticipation
    then accelerates toward and through selected work

end state
    fullscreen specialist workspace
    no project grid / surrounding work units
    compact topology compass retained
```

Z6 is not treated as a failed direction. Its perspective-corridor / 2.5D quality is positive design evidence that may be useful later for project-world depth or semantic-zoom work, but Z7 is the selected deep-focus transition.

Z2 is likewise preserved as positive evidence for the value of explicit world-depth separation.

## 6. Dynamic source origin

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

## 7. Compass treatment and fixture correction

The topology compass is held constant across every deep-focus end state.

The intended distinction is:

```text
project map / grid
    navigation surface
    disappears in deep focus

compact topology compass
    orientation / return anchor
    survives in deep focus
```

During human review, the compass appeared to contain or overlap another rounded box. Inspection showed that the compass was positioned above the schematic top-right workspace panel, whose border remained visible behind it and could read as a second compass container.

The refinement now reserves clear vertical space in the right workspace column beneath the compass and gives the compass an opaque isolated surface. This is a fixture/layout repair, not a new compass semantic decision.

The project owner likes the compass as a small orientation detail, but final production compass semantics remain unfrozen:

```text
exact topology abstraction
selected-position meaning
interactive versus passive behavior
size and placement
relationship to Return-to-project
semantic detail density
```

## 8. Fullscreen meaning

"Fullscreen" here means the specialist workspace owns the entire active Cockpit stage rather than remaining a framed card above the project map.

It does not yet decide whether production deep focus uses the browser Fullscreen API, hides every application-level chrome surface, or changes URL / browser-history semantics. Those remain separate production questions.

## 9. Reduced motion

All spatial movement is presentation-only.

```text
prefers-reduced-motion
    transitions collapse to effectively instant
    same fullscreen specialist-workspace end state
    same compass orientation aid
```

No semantic meaning depends on motion.

## 10. Current accepted Phase-C direction from this slice

```text
DEEPEST WORK-UNIT INTERACTION

compact map work unit
    -> SEL2 selected
    -> X5 balanced contextual expansion
    -> Z7 Pull-Back Then Dive
    -> fullscreen specialist workspace

fullscreen specialist workspace
    no project grid
    no surrounding project boxes
    compact topology compass retained
```

This is strong enough to close the Checkpoint 243 deep-focus transition review and route the next design question through a new checkpoint.

## 11. Still unfrozen

```text
exact Z7 duration / easing
entry interruption / cancellation
return-transition choreography
production compass semantics and interaction
browser Fullscreen API behavior
application chrome visibility in deep focus
workspace mounting mechanics
URL / browser-history state
specialist-workspace composition
performance implementation
```
