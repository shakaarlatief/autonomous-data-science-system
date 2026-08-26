# Research 012: Post-promotion Cockpit normal-window and pinch-sensitivity review

**Date:** 2026-08-21  
**Status:** Human-feedback repair implemented and automated gate passed; real-browser human retest pending  
**Scope:** Small post-promotion Cockpit interaction polish on top of Specification 008  
**Authority:** Product-review evidence and bounded implementation rationale only. This memo does not reopen or replace Specification 008.  
**Design session:** 03  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 03 - Project Cockpit & V1 Integration

## 1. Human evidence

After Specification 008 had already been promoted, the user tested the latest Cockpit again in both true browser fullscreen and a normal Chrome window.

The review found two bounded issues:

```text
Jump/search palette
    fullscreen:
        good
        lower results correctly cut off and remain reachable by internal scrolling

    normal browser window:
        palette can extend into / overlap the persistent composer
        lower results therefore occupy the composer region instead of the palette
        becoming shorter and internally scrollable

native trackpad pinch
    substantially smoother than earlier iterations
    remaining tiny occasional hitch still judged non-blocking polish
    scale travel per physical pinch still feels too conservative
```

The screenshots supplied in the human review made the fullscreen-versus-normal-window difference explicit.

The user also requested that future frontend testing handoffs always include exact Git pull/update commands.

## 2. Why the Jump defect survived the earlier gate

The sixth-review repair already constrained the palette using viewport-height formulas and internal result scrolling. That was sufficient for the automated 1024x768 gate and for the user's fullscreen review.

The later normal-window evidence showed that a fixed formula is still weaker than the actual product invariant:

```text
Jump palette bottom
    must remain above
actual rendered composer top
```

Browser chrome, fullscreen transitions, future composer-height changes, and prototype-response content can all change the real collision boundary. Therefore the implementation should derive the available palette height from rendered geometry rather than only from assumed viewport constants.

## 3. Bounded implementation

### 3.1 Composer-aware Jump safe area

While the Jump palette is open, `CockpitProjectMap` now:

```text
1. references the rendered Jump popover
2. finds the rendered `.cockpit-composer-wrap`
3. measures both bounding rectangles
4. computes:

   availableHeight = composer.top - popover.top - 12px safety gap

5. applies that as the popover maximum height
6. re-measures on:
       window resize
       fullscreen change
       composer ResizeObserver notifications
```

CSS retains a `100dvh` based fallback, but rendered composer geometry is now authoritative while the palette is open.

The results list remains the shrinkable/scrollable flex child, so when the available window height falls, the palette itself becomes shorter and lower results are reached through internal scrolling rather than descending into the composer.

### 3.2 Pinch responsiveness

The native pinch sensitivity constant changed from:

```text
0.0018
    ->
0.0024
```

This is another moderate increase. The established smoothing architecture was intentionally left unchanged:

```text
ctrl-wheel pinch recognition
frame coalescing
bounded per-frame delta
exponential scale mapping
immediate zoom state
approximate gesture anchoring
no simultaneous ordinary-pan interpretation
```

The goal is more scale travel per natural physical gesture, not a return to the earlier jumpy implementation.

Exact pinch constants remain product tuning rather than architecture.

## 4. Regression-gate strengthening

The browser test now reproduces the failure class directly:

```text
1. open Cockpit at 1600x900
2. open Jump/search
3. shrink viewport to 1600x720
4. require palette bottom to remain >= 8px above composer top
5. scroll the internal results list to the final result
6. select Subgroup review successfully
```

The pinch test was also adjusted for the intentionally faster scale response while retaining bounded single-gesture progression and anchor-stability checks.

## 5. Automated evidence

Implementation head:

```text
ae83e920b3fa43ee8242bdb1ca2640d23a474c71
```

V1 frontend spike run:

```text
167 / 32503861255

Ubuntu build + unit tests                  PASS
Windows build + unit tests                 PASS
Chromium interaction/accessibility         PASS
controlled direct-view visual regression   PASS
normal-window Jump re-clamp regression      PASS
faster anchored pinch regression            PASS
```

The same branch's runtime bakeoff gate also remained green in run `20 / 32503861259`; the frontend repair did not regress the deterministic runtime control or OpenAI core candidate tests.

## 6. What this does and does not mean

Strengthened:

```text
collision-safe floating-surface behavior now uses actual rendered composer geometry
normal-window Jump behavior has an explicit resize regression
pinch scale travel is faster than the promoted Specification 008 implementation
```

Not promoted or frozen by this review:

```text
final pinch sensitivity
final zoom range
remaining tiny pinch-hitch polish
final Jump visual styling
final composer geometry
final responsive breakpoints
final gesture library
```

Specification 008 remains the accepted interaction architecture. This is bounded post-promotion implementation tuning.

## 7. Human gate still required

The automated gate cannot decide whether `0.0024` feels correct on the user's actual trackpad.

The next human check should be short:

```text
normal Chrome window
    open Jump/search
    confirm panel cuts above composer
    scroll to lower results

fullscreen
    confirm no regression

trackpad
    one natural full pinch in
    one natural full pinch out
    judge whether scale travel is now sufficient
```

If those checks pass, this repair can be treated as settled polish and the main execution focus returns fully to the runtime bakeoff.