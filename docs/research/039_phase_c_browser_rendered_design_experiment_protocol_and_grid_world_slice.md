# Research 039: Phase C Browser-Rendered Design Experiment Protocol and Grid/World Slice

**Date:** 2026-08-26  
**Status:** Active product-design protocol and first bounded experiment definition  
**Scope:** Replaces generated-image UI mockups as the preferred Phase-C evidence mechanism with real browser-rendered design experiments, while preserving real-product references as optional inspiration/evidence. Opens the grid/world substrate as the first isolated Cockpit design slice.  
**Authority:** Research/design protocol only. Specification 008 remains the promoted V1 Cockpit interaction architecture. No production visual system or frontend architecture is promoted here.  
**Primary interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** chatgpt-07  
**Conversation title:** 07 - Project Cockpit Design Exploration  
**Companion collaboration thread:** MC-0004

---

# 1. Why the Phase-C evidence mechanism changes

Research 038 opened a realistic mockup phase after Research 037, Claude's independent Phase-A design, Claude's Phase-B comparative review, and ChatGPT synthesis converged on a bounded set of high-value Cockpit mechanisms.

A generated UI image was then attempted as a first visual artifact. That attempt exposed an important methodological weakness: a generated screenshot can look polished while answering the wrong product question, inventing geometry, controls, text, or interaction behavior that has no executable counterpart.

The project owner therefore chose a stronger evidence process:

```text
real product / design-tool references where useful
    +
small browser-rendered design experiments
    +
continuous human inspection and comparison
    ->
progressively integrated Cockpit prototype
```

Generated-image UI concepts are removed from the preferred Cockpit design workflow.

This does not claim image generation is universally useless. It says that for the current ADS Cockpit, the design questions are better answered by inspectable browser-rendered artifacts whose geometry, typography, density, responsive behavior, motion and interaction can actually be tested.

---

# 2. Revised terminology

For this phase:

```text
reference
    a real external product/example used to understand a design mechanism

browser design experiment
    a small executable HTML/CSS/JS or React experiment built to isolate one or a few design questions

integrated prototype
    a larger executable Cockpit candidate composed from design mechanisms that survived earlier review

production implementation
    code intended to replace or extend the promoted Cockpit architecture after evidence and specification
```

A generated static image is not treated as a prototype.

---

# 3. Design-question-first process

Phase C should not begin by building one giant redesigned Cockpit. Too many simultaneous variables would make human feedback difficult to interpret.

The preferred loop is:

```text
1. choose one concrete design question
2. inspect strong real references when they add evidence
3. build two to four materially different browser variants
4. keep representative content/state constant
5. let the project owner inspect and compare
6. record what is preferred, rejected, combined or still uncertain
7. refine the winning mechanism if needed
8. move to the next design question
9. integrate only mechanisms that survive review
```

This preserves causal clarity. If a full redesign is disliked, the project should not have to guess whether the problem was the grid, node grammar, typography, connector system, depth, motion, stage treatment or conversation layout.

---

# 4. Provisional slice order

The following order is a working sequence, not a frozen roadmap:

```text
Slice 1   grid / spatial world substrate
Slice 2   work-unit visual grammar
Slice 3   connector semantics and static relation language
Slice 4   semantic zoom / level of detail
Slice 5   liveness / motion budget
Slice 6   Conversation Workspace presentation
Slice 7   selection, focus and bounded 2.5D depth
Slice 8   information lenses and command/navigation treatment
Slice 9   integrated Cockpit candidate
Slice 10  medium / large project pressure test
```

Slices may be combined where the mechanisms are inseparable, but each review should still identify what variable is being tested.

---

# 5. Browser experiments are deliberately non-production

Phase C now authorizes isolated executable design-lab artifacts on `v1-cockpit-design-exploration`.

The boundary is:

```text
ALLOWED
    isolated design-lab HTML/CSS/JS or React components
    representative fixture data
    browser-rendered screenshots derived from those artifacts
    bounded interaction controls useful for comparison
    throwaway/rewrite-friendly code

NOT YET AUTHORIZED
    replacement of the promoted Cockpit implementation
    migration of production routes/components to a new design system
    graph-library adoption
    motion-library adoption
    final auto-layout architecture
    final persistence model
    production semantic-zoom architecture
```

Design-lab code optimizes for learning, not compatibility or permanence.

---

# 6. External grid evidence relevant to Slice 1

The first slice starts with the spatial substrate because every later Cockpit state sits on it.

Useful current references include:

## React Flow background primitives

React Flow's current `Background` component exposes three common node-editor substrate families:

```text
lines
dots
cross
```

It also explicitly supports layering multiple backgrounds. Its documentation demonstrates a fine line grid combined with a stronger larger-interval grid, which directly validates the major/minor-grid idea already raised in Research 037.

Reference:
https://reactflow.dev/api-reference/components/background

## tldraw scale-aware grid

tldraw exposes the grid as a replaceable canvas component. Its custom-grid example renders major and minor lines and updates them with camera position, screen bounds, device pixel ratio and theme.

Its options documentation also uses different grid steps at different zoom ranges. This is strong precedent for treating the grid as a scale-aware orientation system rather than one fixed bitmap pattern.

References:
https://tldraw.dev/examples/custom-grid
https://tldraw.dev/sdk-features/options

## Figma restraint

Figma's ordinary canvas defaults emphasize a quiet neutral background rather than continuously visible high-contrast decoration. That is a useful counterweight: a sophisticated spatial workbench does not require a visually loud grid at rest.

Reference:
https://help.figma.com/hc/en-us/articles/360041064814-Explore-the-canvas

---

# 7. Slice 1 question: what should the ADS world substrate feel like?

The grid/world decision should be evaluated with representative work units present, because a beautiful empty grid may compete badly with actual analytical content.

The first design-lab experiment therefore keeps the same minimal project scene while varying only substrate treatment.

Required controls:

```text
dark / light appearance
project-scale / work-scale / inspection-scale simulation
content visible / grid-only inspection
activity field on / off
```

The first four substrate variants are:

## G1 Precision Lines

```text
fine minor Cartesian lines
stronger major divisions
very low resting contrast
no decorative glow
technical / instrument-like
```

Question:
Does this provide the strongest orientation and long-session calm, or does it feel too conventional?

## G2 Dot Matrix

```text
subtle dot field
sparser stronger anchor dots
lower continuous-line noise
clean node-editor feel
```

Question:
Does the lower visual density improve content focus while preserving enough spatial orientation?

## G3 Cross Lattice

```text
small cross/intersection marks
sparse structural rhythm
stronger spatial identity than dots
less continuous geometry than lines
```

Question:
Does this feel distinctive and precise, or unnecessarily stylized?

## G4 Adaptive Hybrid

```text
major/minor line hierarchy
minor detail fades at project scale
subtle localized activity field around genuinely active work
resting state remains calm
```

Question:
Does controlled scale/activity response create useful ADS-specific liveness without becoming decorative science fiction?

---

# 8. Constant representative scene

All four variants use the same minimal churn-project state:

```text
Prediction moment        unresolved / blocking
Production missingness   active investigation
Chronological validation selected
Baseline logistic model  completed
Evaluation               downstream
```

The same connectors, labels and card geometry are used in every variant.

The purpose is not to select the final work-unit grammar yet. The content exists only to reveal whether the substrate supports or competes with realistic Cockpit information.

---

# 9. Human evaluation for the grid/world slice

The project owner should be able to compare the variants using questions such as:

```text
Which substrate is easiest to look at for a long time?
Which makes spatial position easiest to recover?
Which interferes least with node text and relation lines?
Which feels most professional and distinctive for ADS?
Does the grid still work in both light and dark appearance?
At project scale, is the world quieter rather than merely smaller?
Does the localized activity field in G4 communicate useful activity or feel ornamental?
Would you combine part of one variant with another?
```

A preferred answer may be a hybrid such as:

```text
G1 major/minor hierarchy
+
G2 low-noise density
+
G4 scale-aware fading
```

The experiment is intended to make that kind of synthesis possible.

---

# 10. Evidence standard for promotion from Slice 1

The grid/world slice is ready to feed the integrated Cockpit only when:

```text
at least one substrate treatment is preferred under realistic content
light and dark both remain legible
project-scale and closer-scale behavior are understandable
the substrate does not carry critical project meaning by itself
reduced-motion meaning is unaffected
activity effects, if retained, correspond to real project activity
```

No grid choice is promoted by this research document itself.

---

# 11. Immediate implementation boundary

Create an isolated first design-lab artifact at:

```text
frontend/design-lab/grid-world.html
frontend/design-lab/grid-world.css
frontend/design-lab/grid-world.js
```

The experiment should be directly viewable through the Vite development server without changing the production Cockpit route.

Expected local URL:

```text
http://localhost:5173/design-lab/grid-world.html
```

No new frontend dependency is justified for this slice.

---

# 12. Next step after human grid review

Do not immediately build all remaining slices.

First record the human disposition of G1-G4:

```text
preferred
rejected
combine
needs refinement
```

Then either refine the substrate once more or proceed to work-unit visual grammar with the chosen substrate as the shared control background.