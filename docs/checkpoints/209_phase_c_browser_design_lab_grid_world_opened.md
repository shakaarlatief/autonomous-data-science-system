# Checkpoint 209: Phase C Browser Design Lab Opened, Grid/World Slice First

**Date:** 2026-08-26  
**Status:** Current product-design checkpoint  
**Checkpoint class:** CONTINUITY / PRODUCT_DESIGN / EXPERIMENT_BOUNDARY  
**Project stage:** V1 next-generation Project Cockpit browser-rendered design exploration  
**Scope:** Records the decision to retire generated-image UI mockups from the preferred Cockpit design workflow, authorizes isolated browser-rendered design-lab experiments without changing the promoted Cockpit implementation, freezes Research 039 as the Phase-C experiment protocol, and opens the grid/world substrate as the first bounded design slice.  
**Authority:** Current routing and experiment boundary. Specification 008 remains the promoted V1 Cockpit interaction architecture. No production visual implementation is promoted here.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** chatgpt-07  
**Conversation title:** 07 - Project Cockpit Design Exploration  
**Primary collaborator:** ChatGPT

## 1. The generated-image path is deliberately retired

Phase C was originally described as a realistic mockup phase. A generated UI image was attempted and exposed a methodological weakness: an image can look polished while inventing non-executable geometry, controls, wording and interaction behavior, or even visualize the wrong thing entirely.

The project owner explicitly chose a stronger approach.

The preferred Phase-C evidence process is now:

```text
real external references where useful
    +
small real browser-rendered design experiments
    +
continuous human comparison
    ->
progressively integrated Cockpit prototype
```

Generated-image UI concepts are not part of the preferred Cockpit evaluation workflow.

This is a process correction, not a rejection of visual design exploration.

## 2. Research 039 defines the revised protocol

The new protocol is preserved at:

```text
docs/research/039_phase_c_browser_rendered_design_experiment_protocol_and_grid_world_slice.md
```

Its central distinction is:

```text
reference
    external evidence / inspiration

browser design experiment
    executable bounded artifact isolating one or a few design questions

integrated prototype
    larger executable Cockpit candidate composed from reviewed mechanisms

production implementation
    later evidence-backed replacement/extension of promoted Cockpit code
```

A generated screenshot is not treated as a prototype.

## 3. Phase C now uses design-question-first iteration

Do not construct one giant redesigned Cockpit immediately.

The preferred loop is:

```text
choose one design question
inspect references when useful
build 2-4 materially different browser variants
hold content/state constant
human compares
record preferred/rejected/combine/refine disposition
iterate if necessary
move to next design question
```

This keeps feedback attributable to the mechanism actually being tested.

## 4. Isolated design-lab code is now authorized

The design branch may now contain executable prototype artifacts under an isolated design-lab surface.

Allowed:

```text
HTML/CSS/JS or React design-lab artifacts
representative fixtures
browser-derived screenshots
comparison controls
throwaway/rewrite-friendly prototype code
```

Still not authorized:

```text
replacement of production Cockpit components
production route migration
new graph-library adoption
new motion-library adoption
final semantic-zoom architecture
final layout/persistence architecture
final visual-system freeze
```

The promoted `/cockpit` implementation remains the control baseline.

## 5. First bounded slice: grid / spatial world substrate

Research 039 opens four initial variants:

```text
G1 Precision Lines
    quiet minor/major Cartesian hierarchy

G2 Dot Matrix
    lower-noise dot substrate with sparse stronger anchors

G3 Cross Lattice
    sparse intersection/cross rhythm

G4 Adaptive Hybrid
    major/minor hierarchy + scale-aware detail + localized activity field
```

All variants use the same minimal Customer Churn project scene so the substrate, not content differences, is under review.

## 6. External evidence used for the first slice

Relevant current references include:

```text
React Flow Background
    lines / dots / cross variants
    layered background example

tldraw custom grid
    major/minor rendering
    camera/theme/device-pixel-ratio aware

tldraw options
    zoom-dependent grid step sizes

Figma canvas
    useful counterexample emphasizing a quiet neutral substrate
```

No external product is being copied or selected as the ADS implementation.

## 7. First design-lab target

Create:

```text
frontend/design-lab/grid-world.html
frontend/design-lab/grid-world.css
frontend/design-lab/grid-world.js
```

Expected development URL:

```text
http://localhost:5173/design-lab/grid-world.html
```

The first artifact should allow human inspection of:

```text
all four variants
dark / light appearance
project/work/inspection scale simulation
content visible / grid-only state
activity field on / off
```

No dependency addition is needed.

## 8. MC-0004 remains active in Phase C

MC-0004 is not closed yet because human product direction is still pending.

Current interpretation:

```text
Phase A  frozen independent Claude design
Phase B  frozen comparative review
Phase C  active browser-rendered design evaluation
```

The next expected sequence is:

```text
ChatGPT builds bounded grid/world experiment
human inspects and gives disposition
ChatGPT records result
then the next design slice is opened
```

## 9. Source-vault pause remains unchanged

The permanent source-vault bootstrap remains:

```text
PAUSED
not cancelled
not rejected
not superseded
accepted Source Universe architecture/runbook unchanged
Course 2 recovery-integrity gate unchanged
```

## 10. Exact continuation

```text
1. use v1-cockpit-design-exploration and Checkpoint 209 as the current route
2. use Research 039 as the Phase-C browser-experiment protocol
3. keep generated-image UI concepts out of the preferred Cockpit workflow
4. build the isolated G1-G4 grid/world design lab without touching production Cockpit code
5. verify it through a real browser
6. present the browser-rendered variants to the project owner
7. record preferred/rejected/combine/refine disposition
8. refine the substrate if necessary
9. then open the next bounded design slice, likely work-unit visual grammar
10. keep MC-0004 active until human direction and the next prototype boundary are clear
11. keep source-vault deployment paused until the project owner chooses to resume it
