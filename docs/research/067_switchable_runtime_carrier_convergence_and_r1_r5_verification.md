# Research 067: Switchable Runtime Carrier Convergence and R1/R5 Verification

**Date:** 2026-08-27  
**Status:** Active Phase-C runtime-carrier convergence evidence  
**Scope:** Verifies the project owner's observation that the earlier R1 Status Lamp and R5 Motion Signal were visually collapsing together, then opens a narrower two-carrier runtime presentation experiment with global and per-work-unit switching.  
**Authority:** Research evidence for the current Project Cockpit runtime slice. This memo does not freeze the final ADS runtime ontology, runtime carrier, project-disposition ontology, or production preference-persistence architecture.

## 1. Human observation

During review of the corrected conditional-runtime browser, the project owner observed that:

```text
R1 Status Lamp
R5 Motion Signal
```

looked effectively the same for Queued, Running, Waiting and Waiting for Human, while Failed was the only state where the difference was clearly visible.

The project owner also rejected the combined dot-plus-tag runtime presentation as the wrong composition and proposed a new direction:

```text
one runtime carrier at a time

carrier A
    dot + dynamic circle/ring

carrier B
    runtime tag whose perimeter line circulates dynamically

switching
    global: switch every live-runtime box together
    local: click a work unit's visible runtime carrier to switch only that box
```

## 2. Verification of R1 versus R5

The browser implementation was inspected directly.

R1 was:

```css
html[data-runtime-encoding="r1"] .runtime-lamp {
  opacity: 1;
}
```

R5 was:

```css
html[data-runtime-encoding="r5"] .runtime-lamp,
html[data-runtime-encoding="r5"] .runtime-motion-ring {
  opacity: 1;
}
```

Therefore R1 and R5 were **not literally identical in implementation**.

R5 added a `runtime-motion-ring` around the same lamp used by R1. For Queued, Running, Waiting and Waiting for Human that ring used the same pulse animation with different durations. Failed changed the ring more visibly by making it a rotated rounded-square/diamond-like shape.

The practical result nevertheless validates the human observation:

```text
structurally different
+
perceptually insufficiently different at working scale
```

The motion ring was too subtle and too spatially coincident with the R1 lamp for the live non-failure states to read as a meaningfully different carrier family.

This is treated as negative design evidence. The old broad R1-R6 matrix remains preserved historically, but R1 and R5 are not carried forward as distinct convergence candidates.

## 3. New convergence hypothesis

The refined architecture is:

```text
runtime remains conditional
+
exactly one runtime carrier is shown per live-runtime work unit
+
carrier appearance may be user-selectable
```

The two active carrier candidates are intentionally different in information density and visual character.

### Carrier A: Dot + dynamic ring

```text
compact
instrument-like
low text density
state-colored core dot
clearly visible dynamic outer ring
```

The ring is deliberately stronger than the previous R5 ring so it no longer collapses perceptually into a static status lamp.

Runtime state remains represented through color plus state-sensitive motion pacing. Failed keeps a sharper non-circular ring treatment.

### Carrier B: Animated runtime tag

```text
explicit textual state
state-colored text
state-colored perimeter
circulating perimeter trace
```

The tag does **not** copy the expanding/breathing behavior of the dot carrier. Instead, a bright perimeter segment circulates around the tag outline. This provides semantic motion while keeping the two carrier families visually distinct.

## 4. Exactly one runtime carrier per box

The refinement explicitly rejects the earlier stacked composition:

```text
dot + runtime tag simultaneously
```

as the default runtime presentation.

For a live runtime episode, a work unit now shows either:

```text
Dot + dynamic ring
```

or:

```text
Animated runtime tag
```

but not both.

The neutral P7 project-disposition tag remains conceptually separate and is still shown in the held control because it communicates a different semantic axis.

## 5. Global switching

The browser includes a global runtime-carrier control:

```text
Dot + dynamic ring
Animated runtime tag
```

Choosing a global carrier:

```text
changes every live-runtime work unit together
+
clears any existing local per-box overrides
```

This tests the product idea that a user may prefer a compact instrumental Cockpit or a more explicit textual Cockpit without changing underlying semantic state.

## 6. Per-work-unit switching

Each live-runtime work unit exposes its currently visible runtime carrier as the local interaction target.

Behavior:

```text
click visible dot/ring
    -> this work unit switches to animated tag

click visible animated tag
    -> this work unit switches to dot/ring
```

Only that work unit changes.

If the resulting local choice differs from the current global carrier, the node is treated as a local override. If it is switched back to match the global carrier, the override is removed.

This gives the requested two levels of control:

```text
all boxes at once
+
one box at a time
```

## 7. No-runtime invariant

Research 066 remains binding for this refinement:

```text
No runtime
    means no current execution/work episode exists
```

Therefore a no-runtime work unit renders:

```text
no dot
no ring
no runtime tag
no runtime-carrier switch target
```

Deferred and Future examples in the practical scene remain clean when they have no current runtime episode.

## 8. Reduced-motion behavior

Runtime motion remains semantic rather than ambient.

Reduced motion therefore removes animation but preserves state identity:

```text
Dot mode
    static colored dot + static outer ring

Tag mode
    static colored tag + static perimeter
```

No state depends on motion alone.

## 9. Browser implementation

New bounded browser:

```text
http://localhost:5173/design-lab/work-unit-runtime-carrier-switch.html
```

Files:

```text
frontend/design-lab/work-unit-runtime-carrier-switch.html
frontend/design-lab/work-unit-runtime-carrier-switch.css
frontend/design-lab/work-unit-runtime-carrier-switch.js
```

Exact browser implementation target:

```text
3a862c659e60e53832eaa5940ddb60d05734cd7d
```

Production `/cockpit` remains untouched.

## 10. Practical-scene fixture

The mixed-category practical scene preserves conditional runtime:

```text
Question        CURRENT + HUMAN
Investigation   CURRENT + RUN
Validation      NEXT + QUEUE
Model Work      CURRENT + FAIL
Evaluation      DEFER + NONE
Investigation   FUTURE + NONE
```

The user can globally switch all four live-runtime boxes or locally mix dot and tag carriers in the same scene.

## 11. Current review questions

```text
1. Is the strengthened dot ring now visibly dynamic rather than effectively identical to a static lamp?
2. Does the circulating tag perimeter feel clean and intentional?
3. Which carrier is preferable as a default, if either?
4. Is supporting both as user-selectable appearance useful rather than unnecessary complexity?
5. Does global switching feel natural?
6. Does per-box switching feel natural?
7. Does a mixed scene with local overrides remain coherent?
8. Does exactly one runtime carrier avoid the earlier dot-plus-tag clutter?
9. Does Reduced motion preserve interpretability?
```

## 12. Promotion audit

Strong active evidence:

```text
R1 and R5 were technically different but perceptually insufficiently differentiated
stacking dot and runtime tag is not the preferred composition
one runtime carrier at a time is the current convergence hypothesis
global and per-work-unit carrier switching are worth direct human evaluation
```

Still unfrozen:

```text
final runtime carrier
whether both carriers survive to production
production default carrier
production persistence scope
final runtime ontology
final Blocked semantics
final project-disposition ontology
runtime-flow connector semantics
```
