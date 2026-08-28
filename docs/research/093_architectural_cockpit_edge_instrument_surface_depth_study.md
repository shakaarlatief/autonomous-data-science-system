# Research 093: Architectural Cockpit Edge Instrument-Surface Depth Study

**Date:** 2026-08-28  
**Status:** CANDIDATE STUDY / AWAITING HUMAN REVIEW  
**Scope:** Second-generation whole-product study of the Project Cockpit right edge after the first spatial-rail comparison. Tests whether the Cockpit edge itself can become an architectural instrument surface with perspective, visible thickness, fixed-edge attachment and progressively deployable functional depth.  
**Authority:** Human-review candidate evidence only. No Gen 2 variant is selected, promoted or part of the accepted Cockpit baseline. Existing accepted Phase-C mechanisms, Product Surface Study A evidence, and the first-generation spatial-rail study remain preserved with their existing dispositions.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** `chatgpt-09`  
**Conversation title:** `09 - Project Cockpit Design Exploration`

---

## 1. Why a second generation was required

Research 092 tested three ways to make the right-side rail spatial:

```text
A · Extruded Blade
B · Layered Deck
C · Dock and Float
```

Those candidates answered the question:

```text
How can a software tool rail gain depth and direct manipulation?
```

During human review, a stronger visual reference was supplied:

```text
Dribbble
Cockpit Platform x FUI
https://dribbble.com/shots/20914787-Cockpit-Platform-x-FUI
```

The important transferable observation was not the reference's neon / science-fiction styling. The relevant spatial grammar was:

```text
central world remains the primary plane
side panels read as physical instrument surfaces around that plane
surfaces have perspective, frame thickness and z-depth
panels visually point inward toward the central work
edge surfaces suggest hinging, sliding, layering or deployment
additional capability can feel architectural rather than overlaid
```

The human clarification therefore changed the design question to:

```text
Can the Cockpit edge itself become a spatial architectural surface,
rather than a toolbar that merely becomes draggable or receives a shadow?
```

## 2. Design boundary

This study deliberately borrows **spatial structure**, not visual identity.

Preserved ADS direction:

```text
Quiet Graphite / restrained dark-first product identity
professional analytical-product character
calm resting state
accepted WorkUnit and relation grammar
existing project-world semantics
existing Conversation and Deep Dive ownership
```

Not copied from the external reference:

```text
neon-heavy science-fiction color treatment
cinematic HUD ornament for its own sake
planet / globe visual metaphor
entertainment-interface density
unnecessary 3D decoration
```

Depth must communicate attachment, hierarchy or disclosure to earn its presence.

## 3. Gen 2 common interaction model

All three candidates are mounted on the complete source-faithful Cockpit.

Shared rule:

```text
Cockpit edge
    = stable physical anchor

inner grip
    = direct-manipulation handle

pull left
    = deploy capability into the project world

push / drag right
    = stow capability back into the Cockpit edge

intermediate pull position
    = meaningful partial deployment
```

A key implementation correction occurred during the study: Hinge and Console initially translated the whole rig, causing the dragged grip to move with the surface and chase the pointer. The corrected architecture anchors the rig to the Cockpit edge and lets the instrument surfaces widen / telescope leftward from that fixed anchor. The grip is independently interactive while the rest of the fixed rig continues to ignore world-navigation pointer input.

That correction is both mechanically more robust and spatially closer to the architectural-Cockpit hypothesis.

## 4. Candidate A: Hinged Instrument Panel

Route:

```text
/design-lab/cockpit-reintegration.html?edge=hinge
```

Hypothesis:

```text
A quiet edge-mounted instrument wing can pivot toward the user
and become legible only when intentionally pulled into the Cockpit.
```

Composition:

```text
compact resting surface
fixed right-edge anchor
visible mid / rear frame depth
angled front face
trapezoidal / instrument-panel silhouette
pull-dependent width
pull-dependent perspective and z translation
progressive header / label reveal
Navigation / Work / System control groups
```

The candidate is intentionally less like a conventional drawer than Research 092 Candidate A. The face has a mild inward orientation and visible rear construction so it reads as a Cockpit surface rather than a flat rectangle.

Primary review questions:

```text
Does the resting object feel calm and integrated?
Does the deployed surface feel like part of the Cockpit architecture?
Is the perspective useful or merely decorative?
Is progressive disclosure understandable without excessive visual weight?
```

## 5. Candidate B: Telescoping Layer Stack

Route:

```text
/design-lab/cockpit-reintegration.html?edge=stack
```

Hypothesis:

```text
Functional categories can become physical Cockpit planes,
so pulling the edge inward literally brings layers of capability into view.
```

The three real control groups remain:

```text
Navigation
Work
System
```

but each group becomes an independently displaced instrument plane.

At full deployment:

```text
Navigation
    travels farthest into the world / highest apparent depth

Work
    occupies the middle spatial plane

System
    remains closest to the Cockpit edge
```

This is the candidate most directly aligned with the human phrase:

```text
"bring layers to the Cockpit"
```

Primary review questions:

```text
Does depth improve functional grouping?
Do the planes feel architecturally connected or visually scattered?
Is the hierarchy intuitive?
How much project-world occlusion is acceptable?
Could this become a reusable grammar for future Cockpit capability?
```

## 6. Candidate C: Spatial Command Console

Route:

```text
/design-lab/cockpit-reintegration.html?edge=console
```

Hypothesis:

```text
The edge can grow into a deeper context-aware command surface
that partially surrounds the active project plane without becoming a modal page.
```

Composition:

```text
fixed Cockpit-edge anchor
deeper front / mid / rear frame stack
stronger perspective than Hinge
wider deployed surface
selected WorkUnit title carried into the console header
Navigation / Work / System controls
richer two-column control composition when fully deployed
```

The selected WorkUnit title is read from the actual integrated WorkUnit state. It is presentation context only and does not own selection.

Primary review questions:

```text
Does a context-aware console feel powerful or too dominant?
Does it help the Cockpit feel like an analytical command environment?
Does the larger surface obscure too much of the project world?
Should contextual content appear only at deeper deployment states?
```

## 7. Real controls, not visual mock controls

As in Research 092, the study reuses the actual existing Cockpit control nodes.

Functional grouping:

```text
Navigation
    Jump/search
    zoom out / readout / zoom in
    Fit
    Reset

Work
    Expand
    Deep Dive
    current-process Focus
    Conversations

System
    Appearance
    Hide HUD
    Fullscreen
```

The prior fold control is hidden inside the candidate study because direct pull/stow behavior is the interaction being evaluated.

No second visual-only control system was created.

## 8. Semantic and ownership invariants

Pulling or deploying an edge candidate must not mutate:

```text
WorkUnit category
WorkUnit disposition
operational status
attention
SEL2 selection
X5 expansion meaning
relation meaning
D0-D3 directionality
project camera meaning
Conversation ownership
Deep Dive semantic state
```

Context surfaces remain independent from the rail geometry.

Full-focus ownership remains:

```text
full-focus Conversation
    -> architectural edge study hides

Deep Dive specialist workspace
    -> architectural edge study hides
```

The study therefore remains Cockpit shell presentation, never a higher-authority semantic surface.

## 9. Implementation artifacts

Primary Gen 2 implementation:

```text
frontend/design-lab/cockpit-spatial-rail-study-gen2.css
frontend/design-lab/cockpit-spatial-rail-study-gen2.js
```

Fixed-edge deployment correction:

```text
frontend/design-lab/cockpit-spatial-rail-study-gen2-anchor.css
frontend/design-lab/cockpit-spatial-rail-study-gen2-anchor.js
```

Integrated loader / substrate:

```text
frontend/design-lab/cockpit-product-surface-study.js
frontend/design-lab/cockpit-reintegration.html
```

Deterministic browser coverage:

```text
frontend/e2e/cockpit-reintegration-spatial-rail-gen2.spec.ts
```

The existing fidelity workflow already watches `cockpit-spatial-rail-study*`, so Gen 2 changes remain inside the holistic browser gate.

## 10. Execution evidence and failures encountered

### Initial implementation target

```text
ff02be4024da7086b7804d0c20b538d56c0fc82f
```

First complete gate:

```text
58 / 60 passing
```

Stack passed. Hinge and Console failed to remain deployed after real pointer drag.

### First drag-controller correction

```text
afad0e3d554ee273c59b04a3f8131a292528a518
```

Pointer tracking moved from the moving grip to window-level listeners. The same 58 / 60 result showed the deeper problem was architectural rather than event-listener locality.

### Fixed-edge correction

The rig was then made stationary while Hinge and Console surfaces deployed left from the Cockpit edge. The grip was reparented to the fixed rig.

That exposed a second exact failure:

```text
fixed rig intentionally had pointer-events: none
reparented grip inherited the non-interactive boundary
all three candidates became mechanically inert
```

The final correction explicitly restored pointer input only on the grip, preserving world interaction through the rest of the rig.

### Final implementation target

```text
c29b19932bc10a2d3aa1e3d507010a4f3211aa4a
```

Final holistic workflow:

```text
run       33201023215
result    SUCCESS
coverage  60 / 60 browser tests passing
```

The complete suite includes all source-faithful Cockpit regression tests, Product Surface Study A, Research 092 first-generation rail studies and all four Gen 2 architectural-edge tests.

## 11. What the automated gate establishes

It establishes that:

```text
Hinge deploys through real pointer drag
Stack creates three separately displaced functional planes
Console grows into a deeper context-aware surface
selected WorkUnit state remains independently owned
real controls remain functional
Conversation full-focus retains ownership
Deep Dive retains ownership
previous Cockpit fidelity tests continue to pass
```

It does **not** establish:

```text
that any candidate looks good
that perspective is appropriately restrained
that the reference-inspired architectural direction fits ADS
that one candidate should be selected
that the three candidates should be hybridized
```

Those remain human product-design judgments.

## 12. Disposition

```text
Gen 1 A · Extruded Blade          preserved / unselected
Gen 1 B · Layered Deck            preserved / unselected
Gen 1 C · Dock and Float          preserved / unselected

Gen 2 A · Hinged Instrument Panel candidate / unselected
Gen 2 B · Telescoping Layer Stack candidate / unselected
Gen 2 C · Spatial Command Console candidate / unselected
```

No previous candidate is implicitly rejected by opening Gen 2. No Gen 2 candidate is accepted because its tests pass.

## 13. Human-review gate

Human review should interact with all three Gen 2 variants slowly through partial and full deployment.

Evaluate:

```text
architectural integration with the project world
resting calmness
quality of depth / perspective
physical credibility of the fixed edge anchor
quality of intermediate deployment states
functional grouping
occlusion
readability
control reachability
whether depth feels useful rather than decorative
which candidate is closest to the intended Cockpit feeling
whether any specific properties should be combined
```

A winner, rejection or hybrid should be recorded only after that review.