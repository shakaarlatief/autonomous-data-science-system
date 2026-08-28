# Research 096: Structural Conversation Spacing and Current Project Tool Rail Control Set

**Date:** 2026-08-28  
**Status:** IMPLEMENTED / DETERMINISTICALLY VERIFIED / AWAITING HUMAN VISUAL REVIEW  
**Scope:** Follow-up correction to Checkpoint 255 after the project owner confirmed that the Conversation WorkUnit boxes still appeared visually joined despite pulling the latest branch.  
**Interaction environment:** ChatGPT  
**Interaction session:** `chatgpt-09`  
**Branch:** `v1-cockpit-design-exploration`

## 1. Human review input

The project owner reported two active corrections and one explicit non-correction:

```text
Conversation Boxes rail
    the WorkUnit boxes still visually have no spacing
    the repository had already been pulled locally

current flat Project Grid rail
    restore Fullscreen
    remove Expand selected WorkUnit
    remove Hide project HUD

current-process Focus
    already works correctly
    do not modify it
```

Focus was therefore deliberately excluded from this implementation pass.

## 2. Why the previous spacing correction was insufficient

Checkpoint 255 treated the problem primarily as list spacing and applied a larger CSS row gap.

That was not a strong enough layout contract because the Conversation rail renders canonical WorkUnits through scaled/transformed child content inside rail slots. A grid row can therefore report a valid inter-row gap while transformed or overflowing visual content consumes enough of that separation that adjacent WorkUnit surfaces still appear joined.

The human screenshot exposed this gap between layout-level evidence and rendered visual geometry.

The durable lesson is:

```text
Do not validate Conversation WorkUnit separation from CSS gap values alone.
Measure the actual rendered WorkUnit surfaces.
Reserve the intended breathing room in real parent-row layout geometry.
```

## 3. Structural spacing correction

The corrected Boxes-mode layout now combines:

```text
thread-list row gap          16px
WorkUnit thread padding       6px top + 6px bottom
canonical WorkUnit geometry   unchanged
accepted rail footprint       unchanged
```

The additional spacing belongs to the conversation thread row rather than resizing or distorting the canonical WorkUnit.

The browser gate now measures the actual rendered `.node-surface` rectangles at both normal desktop and narrow review widths.

Current deterministic requirements:

```text
project-general artifact -> first WorkUnit visible gap >= 16px
adjacent WorkUnit visible surface gap                  >= 20px
checked at 1600px viewport width
checked at  760px viewport width
```

This closes the exact blind spot that allowed the earlier spacing change to look ineffective while a weaker test still passed.

## 4. Current flat rail control set

The project owner requested a narrower visible control set for the current flat rail candidate.

Retained:

```text
Jump / search
Zoom out
zoom readout
Zoom in
Fit project
Reset view
Deep Dive
Current process focus
Conversations
Appearance
Fullscreen
Tool-label clarity control
```

Removed from the visible current rail candidate:

```text
Expand selected WorkUnit
Hide project HUD
```

The underlying accepted X5 expansion mechanism is not revoked. Only the dedicated rail button is removed from this current product-surface candidate.

Likewise, removal of the Hide project HUD button does not alter the broader promoted ability for immersive/fold-away chrome; it only removes that control from the current reviewed rail composition.

Fullscreen remains a promoted Specification 008 capability and is explicitly visible again in the rail.

## 5. Focus boundary

The project owner explicitly corrected the prior instruction and stated that current-process Focus is working correctly.

Therefore:

```text
M09 focus semantics unchanged
focus membership editing unchanged
context recession unchanged
focus UI unchanged
no new focus code or styling introduced
```

This boundary must be preserved in future continuation.

## 6. Implementation artifacts

```text
frontend/design-lab/cockpit-reintegration-review-256.css
frontend/design-lab/cockpit-spatial-rail-study-angle.js
frontend/e2e/cockpit-reintegration-review-256.spec.ts
```

Implementation target:

```text
e2768a807b2a80f438248a25f7d41e53be561d51
```

## 7. Deterministic evidence

Complete Cockpit fidelity workflow:

```text
workflow run  33211613408
job           98985900484
result        SUCCESS
browser tests 68 / 68 passing
```

The new tests establish that:

```text
actual rendered Conversation WorkUnit surfaces are visibly separated at 1600px
actual rendered Conversation WorkUnit surfaces remain separated at 760px
Fullscreen is visible in the current flat rail
Expand selected WorkUnit is hidden from the current rail
Hide project HUD is hidden from the current rail
clarity expansion preserves the same requested control set
all earlier source-faithful Cockpit mechanisms still pass their regression gates
```

## 8. Disposition

```text
structural Conversation spacing       CURRENT REVIEW IMPLEMENTATION
16px list gap                          current visual tuning value
6px row top/bottom padding             current structural correction
canonical Conversation WorkUnits       unchanged
Fullscreen rail control                RESTORED
Expand selected WorkUnit rail button   REMOVED from current rail candidate
Hide project HUD rail button           REMOVED from current rail candidate
current-process Focus                   explicitly unchanged / working
live topology compass                  carried forward unchanged from Checkpoint 255
production /cockpit                     untouched
```

## 9. Human-review gate

The next human review should check two things only:

```text
1. Conversation Boxes mode
   confirm that the WorkUnits now visibly read as separate cards at the user's actual viewport

2. Project Grid flat rail
   confirm Fullscreen is present
   confirm Expand selected WorkUnit and Hide project HUD are absent
```

The live topology compass remains part of the current substrate and is not reopened by this correction.
