# Research 061: Project-Disposition Neutral-Tag + Tone Convergence Refinement

**Date:** 2026-08-27  
**Status:** Active Phase-C product-design evidence  
**Scope:** Records human rejection of persistent disposition color in the mixed-category scene and refines the project-disposition convergence candidate to neutral tag + tonal hierarchy, with state color revealed only on hover.  
**Authority:** Research/design evidence only. The disposition fixtures remain provisional and do not freeze the final ADS project-state ontology.

## 1. Human review evidence

The project owner reviewed the practical mixed-category P6/P7 comparison and found both persistent-color variants somewhat confusing once category color and disposition color coexisted.

Human conclusion:

```text
best direction
    tag + tone

resting tag
    neutral / uncolored

hover
    tag reveals the disposition color

persistent disposition perimeter hue
    not preferred for the convergence candidate

persistent disposition-colored tag
    not preferred for the convergence candidate
```

This is not a rejection of disposition hue as a possible transient interaction cue. It is a rejection of keeping that second semantic color system persistently active on the resting work unit in this mixed-category design.

## 2. Refined convergence candidate

P7 is now redefined as:

```text
P7  Neutral Tag + Tone

REST
    category hue remains the dominant persistent work-unit color
    disposition tag is present but neutral
    Completed / Deferred / Future use the retained selective tonal hierarchy
    no disposition-colored outer perimeter
    no state rhythm

HOVER
    tag border and text reveal the disposition-specific hue
    H4 node interaction remains otherwise unchanged
```

This deliberately separates persistent category recognition from transient disposition emphasis.

## 3. Why this resolves the observed confusion

The practical comparison showed that a category-colored scientific marker/frame plus a second persistent disposition hue can create unnecessary competition.

The refined grammar therefore uses different channels at different persistence levels:

```text
category
    persistent scientific marker + category color

project disposition
    persistent explicit neutral text tag
    + selective tone where lifecycle recession is useful
    + transient state color on hover
```

This preserves semantic certainty without requiring the resting map to carry two equally salient color systems on every work unit.

## 4. Preserved alternatives

The earlier candidates remain preserved in git and the browser comparison controls:

```text
P4 State Rhythm
    retained as historical design evidence

P6 Hue + Colored Tag + Tone
    retained as a comparison control

previous P7 Colored Tag + Tone
    preserved in repository history
```

No prior mechanism is silently erased.

## 5. Browser implementation

Files:

```text
frontend/design-lab/work-unit-disposition-grammar.html
frontend/design-lab/work-unit-disposition-grammar.css
frontend/design-lab/work-unit-disposition-grammar.js
```

Local URL:

```text
http://localhost:5173/design-lab/work-unit-disposition-grammar.html
```

Exact refined browser implementation target:

```text
fac1db37af4225927d6c799e37418a3ad9c42c13
```

The page now opens directly in P7 Neutral Tag + Tone.

## 6. Human verification gate

The next review should verify:

```text
resting P7 tags are neutral
hovering a P7 node reveals the correct disposition hue in the tag
category colors remain visually dominant at rest
tonal reduction remains useful rather than implying low importance or disabled state
mixed-category practical scene is materially less confusing than the persistent-color variants
```

If accepted, project-disposition visual encoding can be treated as sufficiently converged for the current Phase-C round while the final disposition ontology remains open.

## 7. Production boundary

No production `/cockpit` file changed.

No final disposition ontology is promoted.

No runtime-state grammar is selected.

No importance/priority grammar is selected.
