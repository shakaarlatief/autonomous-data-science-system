# Research 078: Project-World Semantic Zoom Level-of-Detail Experiment

**Date:** 2026-08-27  
**Status:** Active Phase-C interaction-design evidence  
**Scope:** Opens the next project-world design question after the project owner selected Z7 Pull-Back Then Dive for deep-focus entry: how work-unit information should simplify, persist, aggregate or become richer as the navigable project world changes scale.  
**Authority:** Research evidence only. No final semantic-zoom thresholds, clustering semantics, large-project rendering strategy, information schema or production implementation is frozen by this memo.

## 1. Predecessor closure

Research 077 now records the selected deep-focus direction:

```text
Z7 Pull-Back Then Dive
    selected deep-focus entry direction

end state
    fullscreen specialist workspace
    no project grid / surrounding map
    compact topology compass retained
```

Positive but non-selected evidence remains:

```text
Z2 World Falls Away
    useful explicit depth separation

Z6 Perspective Corridor
    useful 3D / 2.5D spatial quality
```

The selected/fixed spatial-browser implementation target is:

```text
04616a52df5cceff6c59223bbd6f07448d027510
```

The compass-overlap fixture defect is repaired at that target.

## 2. Why semantic zoom is next

Specification 008 already promotes bounded geometric zoom and a finite navigable project world, while Research 037 explicitly identified the absence of a deliberate semantic-scale information architecture as a current limitation.

The problem is not merely how large cards become on screen.

The bounded question is:

```text
As the project world zooms out and in,
what information should survive,
what should aggregate,
what should disappear,
and what should become richer?
```

This separates:

```text
GEOMETRIC ZOOM
    physical scale / camera distance

SEMANTIC ZOOM
    information architecture at that scale
```

## 3. New browser

Local route:

```text
http://localhost:5173/design-lab/work-unit-semantic-zoom.html
```

Files:

```text
frontend/design-lab/work-unit-semantic-zoom.html
frontend/design-lab/work-unit-semantic-zoom.css
frontend/design-lab/work-unit-semantic-zoom.js
```

Exact initial implementation target:

```text
65ac02326a75b1c9f056676819d2d1b7b23b74c5
```

Production `/cockpit` remains untouched.

## 4. Controlled scales

Every candidate is viewed at three conceptual levels:

```text
OVERVIEW
    distant project-scale orientation

WORK
    ordinary active Cockpit operation

INSPECTION
    close map-level inspection before X5 expansion / deep focus
```

These are provisional test levels, not a frozen production threshold system.

## 5. Candidate semantic-zoom systems

```text
S0  Geometric Control
    same information largely survives at every scale
    establishes clutter / legibility floor

S1  Progressive Detail
    identity at overview
    operational metadata at work scale
    richer rationale at inspection

S2  Stage Clusters
    overview aggregates individual units into stage-level objects
    units resolve as scale increases

S3  Topology First
    overview privileges relation structure and category markers
    labels/detail strengthen on approach

S4  Focus Preserving
    selected/current work remains richer across distance
    non-current context simplifies earlier

S5  Status First
    overview prioritizes project/runtime state signals
    descriptive identity becomes secondary

S6  Glyph Field
    distant units collapse almost entirely into scientific/category glyphs
    topology carries much of the overview structure

S7  Hybrid Contextual
    selected/current work retains identity and state
    context compresses
    labels and topology remain sufficient for orientation

S8  Local Detail Lens
    global overview stays highly compressed
    selected object remains locally rich even at distant scale
```

S7 is the browser working default only. It is not selected before human review.

## 6. Held controls

The comparison should preserve the current Phase-C semantic direction as much as practical:

```text
scientific work-unit category grammar
A3 HIGH-attention signal bars
SEL2 selection concept
project disposition tags
operational status cues
project connectors
current versus contextual work distinction
```

The fixture is schematic and does not attempt exact pixel fidelity to every accepted predecessor browser.

## 7. Human review gate

Review semantic zoom as an information system rather than a decorative animation:

```text
At Overview scale:
    what must remain readable immediately?

Across scale:
    does detail appear in an intuitive order?

Large projects:
    which strategy prevents clutter without making the world anonymous?

Current-process focus:
    should selected/current work retain more detail than context?

Aggregation:
    do stage clusters help or obscure too much structure?

Topology:
    can relation structure carry orientation at distance?
```

Human review may prefer, reject, combine or refine mechanisms.

## 8. Important non-decisions

Still unfrozen:

```text
exact zoom thresholds
continuous versus discrete semantic transitions
cluster construction and cluster interaction
stage taxonomy / grouping semantics
label collision strategy
large-project virtualization
relation simplification / bundling
selected-node detail persistence
focus-set interaction with scale
priority/status visibility by scale
semantic zoom animation
production graph/canvas library
performance implementation
```

## 9. Checkpoint disposition

Z7 materially closes the deep-focus transition question at the current Phase-C level, so a new checkpoint is warranted to preserve that accepted boundary and route the project into semantic-zoom review.
