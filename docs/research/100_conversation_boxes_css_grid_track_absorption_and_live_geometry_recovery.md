# Research 100: Conversation Boxes CSS Grid Track Absorption and Live Geometry Recovery

**Date:** 2026-08-29  
**Status:** IMPLEMENTED / DETERMINISTICALLY VERIFIED / AWAITING HUMAN VISUAL CONFIRMATION  
**Research class:** IMPLEMENTATION_INTEGRITY / LIVE_BROWSER_GEOMETRY / REGRESSION_RECOVERY  
**Scope:** Conversation Boxes visible separation only. Current-process Focus remains out of scope because the project owner reports it working as far as tested.  
**Interaction environment:** ChatGPT  
**Interaction session:** `chatgpt-10`  
**Branch:** `v1-cockpit-design-exploration`

## 1. Trigger

Checkpoint 260 asked for another local human recheck after replacing parent-gap spacing with row-owned margins.

The project owner pulled the branch correctly and still saw the WorkUnit conversation boxes visually touching.

A first live-browser diagnostic established that the intended declarations were actually loaded:

```text
rail state                    boxes
integrity stylesheet loaded   true
WorkUnit margin-bottom        16px
WorkUnit padding-top           6px
WorkUnit padding-bottom        6px
```

This ruled out stale Git state, stale browser assets and the historical `artifact` rail state as the explanation for the visible failure.

## 2. Decisive live geometry

The project owner then measured the real rendered grid and WorkUnit geometry in Chrome DevTools.

Representative values were:

```text
thread list
    display                  grid
    grid-auto-rows           auto
    row-gap                  0px

WorkUnit row
    border-box height        54.0px
    computed margin-bottom   16px
    next row starts          16px after row bottom

painted node surface
    extends about            20.8px below the row border box
    visible surface gap      about 1.9px
```

The repeated measured sequence was effectively:

```text
row bottom        262.4
next row top      278.4
row gap           16.0
surface bottom    283.2
next surface top  285.1
visible gap         1.9
```

This reproduces the user's screenshot numerically.

## 3. Root cause

The Checkpoint 260 margin-owned model was wrong for this composition.

CSS Grid includes grid-item margins in auto-track sizing. The WorkUnit grid item was being stretched/shrunk to a 54px border-box while still reporting the intended 16px bottom margin. The canonical Conversation WorkUnit is a transformed child with `overflow: visible`, so its painted surface continued beyond the shrunken row.

The result was:

```text
computed layout gap appears correct
    but
transformed child escapes the shrunken row
    therefore
visible WorkUnit-to-WorkUnit gap collapses to ~1.9px
```

This is why the previous computed-style checks were misleading.

## 4. Correct recovery principle

The accepted visual target from Checkpoint 256 remains unchanged. The canonical WorkUnit itself is not resized.

The spacing carrier is now an explicit CSS Grid inter-track gap again, combined with a minimum WorkUnit row height large enough to contain the transformed canonical artifact's visible surface before the gap begins.

Current contract:

```text
thread-list row-gap          16px
project row margin            0px
WorkUnit row margin           0px
WorkUnit padding              6px top / 6px bottom
wide WorkUnit min-height     78px
responsive <=1450 min-height 73px
```

The responsive threshold follows the existing accepted Conversation rail footprint, where the 92px canonical WorkUnit is rendered at scale 0.74 below 1450px. Its visible surface is therefore approximately 68.1px high. A 73px minimum row followed by a 16px grid gap preserves at least roughly 20px of visible surface separation without changing the canonical WorkUnit.

## 5. Why this differs from the failed margin model

The grid gap exists **between tracks**. It cannot be consumed by shrinking the WorkUnit item's own border box in the way an item margin can.

The minimum row height separately prevents the transformed child from painting far beyond the row that owns it.

The two responsibilities are therefore explicit:

```text
row height
    contains the transformed canonical artifact footprint

grid gap
    owns the visible inter-object breathing room
```

## 6. Implementation changes

Updated presentation layers:

```text
frontend/design-lab/cockpit-reintegration-presentation-integrity.css
frontend/design-lab/cockpit-reintegration-review-256.css
```

Updated regression surfaces:

```text
frontend/e2e/cockpit-reintegration-presentation-integrity.spec.ts
frontend/e2e/cockpit-reintegration-review-256.spec.ts
frontend/e2e/cockpit-reintegration-spatial-rail-angle.spec.ts
```

The regression contract now requires:

```text
row-gap >= 16px
row margins approximately 0
WorkUnit row height >= 72.5px in responsive coverage
WorkUnit padding >= 6px top/bottom
actual visible surface-to-surface gap >= 20px
```

## 7. Responsive blind spot closed

The earlier 1536px test did not reproduce the exact responsive state visible while the project owner had Chrome DevTools docked.

Research 100 adds explicit coverage at:

```text
1100 x 900
```

which enters the existing `@media (max-width: 1450px)` Conversation WorkUnit scale. It is tested with the historical `artifact` rail state as an additional compatibility condition.

The existing wide and narrow route checks remain.

## 8. Deterministic verification

Implementation/test target:

```text
b8a2d095214c3417f95180ca519c7b6224739181
```

Complete Cockpit fidelity workflow:

```text
workflow run  33247046868
job           99086212488
result        SUCCESS
browser tests 76 / 76 passing
```

The successful run includes:

```text
normal desktop spacing
responsive 1100px spacing
narrow review spacing
legacy artifact state at responsive width
legacy artifact state at wide width
Adaptive Dock full-focus / co-present / Threads-drawer lifecycle
current-process Focus remount/synchronization regression
all prior source-faithful Cockpit mechanisms
```

## 9. Test-process note

An immediately preceding run failed for test-maintenance reasons after the spacing implementation was changed:

```text
wrong dynamic stylesheet data-attribute selector in one test helper
historical rail regression still asserting the superseded margin-owned contract
```

Those failures did not indicate product regressions. The assertions were corrected to match the actual dynamic attribute name and the new grid-track contract. The final 76/76 run is the authoritative deterministic result.

## 10. Current gate

The root cause is now concrete rather than inferred, and the deterministic gate reproduces the responsive failure family that the project owner's live geometry exposed.

Human visual confirmation is still required because this issue was discovered through the real browser after earlier green tests.

Required local result:

```text
clear dark breathing room between project-general and first WorkUnit
clear dark breathing room between every WorkUnit
canonical WorkUnit appearance unchanged
Focus remains stable
```

If confirmed, the Conversation spacing integrity interruption can close and Adaptive Conversation Dock product review resumes immediately.
