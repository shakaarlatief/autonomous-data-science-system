# Research 008: Sixth Cockpit Human Review, World Ambient Continuity, Pinch Stability, and Collision Safety

**Date:** 2026-08-21  
**Status:** Human product-review evidence and bounded design resolution  
**Scope:** Ambient world continuity, laptop trackpad pinch behavior, stage-ruler terminal geometry, Jump-to palette collision safety, and continuity preservation after the sixth real-browser Project Cockpit review  
**Design session:** 03  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 03 - Project Cockpit & V1 Integration

## 1. Context

The fifth Cockpit review had moved the product from a smaller project rectangle surrounded by blank reserve toward a stronger spatial model:

```text
finite navigable grid world
    contains
        semantic project plane
            stage regions
            work units
            connectors
```

It also introduced a viewport-aware semantic stage ruler and a compact vertical tool rail on the right.

The sixth human review was performed in a real desktop browser against the passing Specification 007 candidate v0.5 implementation. The user again judged the overall direction positively and explicitly described the Cockpit as making real progression.

The review nevertheless identified four concrete defects that materially affected visual continuity or interaction quality:

```text
1. ambient depth still revealed the old project-plane box
2. laptop pinch zoom was visibly too jumpy
3. terminal stage-ruler geometry was inconsistent
4. Jump-to/search overlapped the persistent system composer
```

The review included screenshots and a 13.55-second, 1920x1080, 30-fps browser recording of the pinch gesture. The video matters because the defect was temporal interaction quality rather than a static screenshot-only problem.

---

## 2. Human-review findings

### 2.1 Ambient visual depth must belong to the navigable world

The continuous finite grid introduced in the fifth review was conceptually correct, but the previous CSS still rendered an additional radial ambient treatment on the smaller `ProjectCanvas` itself.

At reduced zoom, this produced an unwanted visual boundary:

```text
large grid world
    contains
        smaller project plane with its own glow
                                  ^
                                  visible cutoff
```

Because the smaller glow stopped exactly at the project-plane edge, the user could still perceive the former box even though the grid had been extended correctly.

This is a useful architectural lesson:

> **Visual effects that are intended to establish atmosphere for the spatial workspace must be owned by the spatial world, not accidentally by a smaller semantic sub-plane.**

The project plane may still contain semantic zones, nodes and connectors, but world-level atmospheric depth should not expose implementation boundaries that are not meaningful to the user.

The bounded resolution therefore removes the redundant `ProjectCanvas::before` ambient layer and keeps the restrained radial atmosphere on `ProjectWorld`.

This preserves the positively reviewed design language while removing the clipped-box artifact.

### 2.2 Native trackpad pinch must be continuous enough to feel spatial

The fifth-review implementation recognized Chromium/macOS/Windows-style pinch input through `wheel` events with `ctrlKey=true`, but transformed every received event directly with:

```text
zoom factor = exp(-deltaY * sensitivity)
```

The user-provided video showed that the resulting interaction was technically functional but visibly too jumpy.

The issue is not merely animation polish. A spatial analytical workspace depends on stable proprioception: the user should understand where they are while scaling the world.

The refined interaction model is:

```text
native pinch/wheel events
    -> normalize delta units
    -> accumulate very short burst inside one animation frame
    -> clamp pathological per-frame delta
    -> apply conservative exponential scale
    -> preserve the current gesture anchor
    -> update scroll geometry after layout
```

Additional implementation requirements emerged:

- the current zoom value used for incoming gesture events must be immediately available and must not depend on a stale React render closure;
- a new gesture update should supersede an obsolete pending anchor-correction frame rather than letting multiple old corrections fight each other;
- tiny real zoom increments are allowed to round to the same displayed integer percentage;
- therefore visual label changes are not an appropriate definition of continuous gesture progress.

The implementation now maintains an immediate `zoomRef`, coalesces pinch deltas per animation frame, clamps extreme per-frame input, uses a reduced sensitivity, and anchors geometry around the gesture point.

This remains a browser/native-input spike, not a final cross-device gesture engine. Real laptop hardware review remains authoritative.

### 2.3 Stage-ruler geometry should be derived from rendered semantic boundaries

The fifth-review ruler separated vertical screen-space orientation from horizontal semantic alignment. That direction remains correct.

However, its horizontal geometry was inferred from:

```text
canvas bounding width
    / logical canvas width
    -> inferred geometric scale
    -> inferred semantic gutter
```

At minimum CSS `zoom`, browser rendering semantics did not make that inference match the actual rendered stage-region boundaries. This produced the edge inconsistency visible in the human review, especially around `Framing` and `Evaluation`.

The first sixth-review CI gate confirmed the problem quantitatively. The attempted ruler differed from the actual rendered semantic boundaries by approximately:

```text
left terminal delta   84 px
right terminal delta 182 px
```

The better source of truth already existed in the DOM: the rendered `stage-framing` and `stage-evaluation` regions.

The bounded resolution therefore derives the ruler directly from those rendered boundaries:

```text
ruler left
    = rendered left edge of Framing

ruler right
    = rendered right edge of Evaluation
```

This avoids reconstructing browser zoom geometry from assumptions.

The terminal stages also use the same text alignment and underline inset logic as the middle stages. Neutral grid reserve outside the semantic project plane therefore remains visibly neutral instead of appearing to belong partially to Framing or Evaluation.

Broader lesson:

> **When a view-layer guide must align exactly with another rendered semantic surface, derive it from authoritative rendered geometry when browser transforms make inferred geometry unreliable.**

This is a view-layer rule, not a domain-model dependency.

### 2.4 Jump/search must respect the composer as a safe-area boundary

The scalable `Jump to` palette was the correct replacement for proliferating one-off jump buttons, but opening a long result list could make the palette descend into the persistent system composer.

The user correctly identified the practical consequence: lower project results could become difficult to see or select.

That violates the already accepted collision-safety principle from CPK-20.

The refined layout treats the composer as a real viewport-safe-area boundary:

```text
upper Cockpit chrome
    ↓
Jump/search palette
    internal scroll region
    bounded max height
    ↓
explicit gap
    ↓
persistent system composer
```

The palette is now fixed in viewport space adjacent to the right-side rail, its maximum height is computed from available screen height, and only the result region scrolls internally.

This is stronger than merely raising the panel by a fixed number of pixels because it preserves usability at the supported 1024x768 laptop boundary.

---

## 3. Bounded implementation resolution

The sixth-review repair implements:

```text
world-owned ambient radial depth
ProjectCanvas ambient pseudo-layer removed
no smaller project-plane atmospheric cutoff

stable native pinch pipeline
    immediate zoom ref
    delta-mode normalization
    animation-frame coalescing
    bounded per-frame delta
    lower sensitivity
    gesture-anchor preservation
    obsolete anchor-correction frame cancellation

stage ruler
    horizontal extent derived from rendered Framing/Evaluation boundaries
    consistent terminal-stage typography/underline treatment
    vertical viewport pinning preserved

Jump/search palette
    fixed collision-safe placement
    max height derived from viewport/composer reserve
    independently scrolling results
    lowest representative result remains selectable at 1024x768
```

No graph/canvas library was added. The implementation still uses ordinary React, CSS, SVG, DOM geometry and native browser input.

---

## 4. Validation history

The sixth-review implementation was validated on temporary branch:

```text
v1-frontend-spike-review6
```

through PR #5.

### 4.1 First validation attempt

First implementation head:

```text
39a2fea181ceebb286f2775eee6d409a45df76b1
```

Workflow:

```text
V1 frontend spike
run number 138
run id 32474789703
```

Results:

```text
Ubuntu build + unit tests
    PASS

Windows build + unit tests
    PASS

Chromium browser gate
    FAIL
```

The browser gate produced two failures.

#### Real implementation failure: inferred ruler geometry

The ruler was still inferred from canvas geometry and did not match the actual terminal semantic stage boundaries at minimum zoom.

This was a genuine product defect. It was fixed by using the rendered Framing and Evaluation stage-region rectangles as the alignment source of truth.

#### Test-model failure: requiring every rounded percentage to change

The pinch regression test required every small synthetic wheel event to make the integer percentage label strictly increase.

At the deliberately smoother sensitivity, two distinct underlying zoom values can legitimately display the same rounded integer percentage. The assertion therefore penalized the behavior it was intended to protect.

The gate was corrected to measure meaningful properties instead:

```text
first pinch increment is small
anchor remains stable
multiple events produce bounded cumulative forward progression
final zoom remains well below a large jump
```

The product sensitivity was not increased merely to satisfy the integer label assertion.

### 4.2 Corrected validation

Validated implementation head:

```text
a2e401408c55a74905e0654c40185f4f9990becc
```

Workflow:

```text
V1 frontend spike
run number 140
run id 32475241980
```

Final results:

```text
Ubuntu build + unit tests
    PASS

Windows build + unit tests
    PASS

Chromium browser interaction + accessibility
    PASS

controlled direct-project visual regression
    PASS
```

The validated branch was then fast-forwarded into `v1-frontend-spike`. GitHub consequently records PR #5 as merged at the same validated head.

---

## 5. What the new automated gate proves

The added sixth-review tests now establish that:

```text
ambient radial depth exists on ProjectWorld
ProjectCanvas no longer owns a competing ambient pseudo-layer

stage ruler starts at the rendered Framing boundary
stage ruler ends at the rendered Evaluation boundary
terminal stage title/underline rules are consistent

small pinch input produces a small scale increment
pinch remains approximately anchored to the chosen work unit
repeated input produces bounded cumulative scale progression

Jump/search stays above the persistent composer at 1024x768
its results region can scroll independently
its lowest representative result remains selectable
```

The existing gate continues to cover:

```text
2D movement and recovery
minimum-zoom panning
fit/reset/explicit zoom
searchable project navigation
Data / EDA / Missingness deep focus
browser Back / URL state
fold-away chrome
fullscreen
composer collision recovery
accessibility
cross-platform builds
```

---

## 6. What remains a human gate

Automated wheel events cannot establish that laptop pinch now *feels* correct on the user's actual trackpad.

The next human review should therefore explicitly test:

```text
slow pinch in
slow pinch out
fast pinch in/out
pinch around different map regions
switch immediately between two-finger pan and pinch
observe whether the visual anchor remains understandable
```

Likewise, screenshot assertions can prove ruler alignment but cannot fully determine whether the stage ruler feels visually balanced at every zoom and horizontal pan position.

The user should also confirm that:

```text
ambient circles no longer reveal a smaller hidden box
Framing and Evaluation ruler terminals now feel intentional
Jump/search is comfortably usable above the composer
```

---

## 7. What remains deliberately unselected

This review does not select or freeze:

```text
final graph/canvas library
final gesture library
final auto-layout algorithm
final semantic-zoom algorithm
final stage taxonomy
final minimap implementation
final geometric zoom range
final world dimensions
final viewport-state persistence contract
final project-search backend
final Cockpit visual identity
exact permanent ambient gradient geometry
canonical Cockpit screenshot baseline
```

The current implementation still has not produced evidence that a dedicated canvas/graph or gesture dependency earns its complexity.

---

## 8. Product implication

The sixth review strengthens three broader design rules.

First:

> **Spatial atmosphere should follow the user's navigable world, not reveal arbitrary implementation containers.**

Second:

> **Continuous spatial controls should be validated as temporal interactions, not merely as commands that eventually reach the correct state.**

Third:

> **Floating analytical controls must respect each other as explicit safe-area occupants of the same workspace.**

These rules should carry forward even if the eventual production implementation replaces the current CSS/DOM primitives.

The next substantive step remains another real-browser human review of the corrected Cockpit before Specification 007 is promoted or deeper canvas infrastructure is selected.
