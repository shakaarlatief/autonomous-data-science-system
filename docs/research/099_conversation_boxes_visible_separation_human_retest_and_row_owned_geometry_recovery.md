# Research 099: Conversation Boxes Visible-Separation Human Retest and Row-Owned Geometry Recovery

**Date:** 2026-08-29  
**Status:** IMPLEMENTED / DETERMINISTIC GATE PASS / HUMAN RECHECK OPEN  
**Research class:** IMPLEMENTATION_INTEGRITY / HUMAN_EVIDENCE / WHOLE_PRODUCT_PRESENTATION  
**Scope:** Conversation Boxes rail visible separation only. Current-process Focus is explicitly out of scope because the project owner reports it working in this retest.  
**Authority:** Human visual evidence governs whether the accepted Conversation spacing is actually visible. Checkpoint 256 remains authoritative for the intended spacing values and canonical WorkUnit footprint. This research changes implementation ownership, not the visual design target.

## 1. Trigger

Checkpoint 259 asked the project owner to retest the two previously intermittent presentation failures after Research 098 recovery.

The retest produced a split result:

```text
current-process Focus
    working as far as tested

Conversation Boxes
    still visually joined
    original visible breathing room is still absent
```

The project owner supplied screenshots from both the adaptive Conversation route and the normal full-focus Conversation surface. The screenshots show the WorkUnit artifacts stacking directly against one another rather than reading as distinct conversation objects.

This human evidence invalidates the claim that the Checkpoint 259 Conversation-spacing recovery was sufficient, even though its deterministic tests were green.

## 2. Correction to Research 098 diagnosis

Research 098 identified real problems, but its Conversation diagnosis was incomplete.

It correctly observed that the current renderer identifies work threads with:

```text
data-thread-scope="work"
```

while some historical spacing rules referenced:

```text
.is-workunit-thread
```

However, the integrated Phase-C completion adapter also restores `.is-workunit-thread` onto rows that contain canonical WorkUnit artifacts. Therefore stale selector identity alone does not explain the still-visible failure.

The more important integration weakness is that the accepted separation remained too dependent on surrounding layout state:

```text
parent grid row-gap
    + exact data-conversation-rail="boxes" selector
    + transformed canonical WorkUnit children
    + late whole-product styles
```

The current Conversation controller treats every non-Text rail value as the Boxes/artifact presentation. Historical persistence also used the value `artifact`, while current UI naming uses `boxes`.

That means a runtime or restored state can still semantically and visually resolve to Boxes while exact `data-conversation-rail="boxes"` styling is too narrow. The supplied screenshot does not prove that `artifact` was the exact runtime value, so this research does not claim that as the sole reproduced root cause. It does establish it as a concrete compatibility hole that the existing test suite did not cover.

## 3. Why the previous deterministic gate was insufficient

The prior tests asserted:

```text
computed parent row-gap >= 16px
computed WorkUnit row padding >= 6px
rendered node-surface distance above a minimum threshold
```

Those assertions were valid for the clean Playwright state that the test created. They did not prove that the user-visible Boxes presentation remained protected under every state that the controller itself resolves as Boxes.

The human retest therefore exposes a test-contract problem as well as a CSS problem:

```text
clean automated state passed
actual local visual state failed
```

The correct response is not to dismiss the screenshot because the test passed. The test must be strengthened around the observed failure family.

## 4. Recovery principle

The separation is now owned by the actual Conversation thread rows themselves.

The parent grid is deliberately no longer responsible for the accepted breathing room:

```text
parent list row-gap
    0px

project-general row
    16px bottom margin

WorkUnit row
    6px top padding
    6px bottom padding
    16px bottom margin

last WorkUnit row
    no trailing bottom margin
```

This preserves the already-reviewed visual target while making its geometry explicit at the object that must be separated.

The canonical WorkUnit box is not resized or redesigned.

## 5. Rail-state compatibility boundary

The row-owned spacing selectors now apply to:

```text
html:not([data-conversation-rail="text"])
```

rather than only:

```text
html[data-conversation-rail="boxes"]
```

This is intentional and matches the Conversation controller's own semantic resolution:

```text
text
    Text mode

anything else
    Boxes / artifact mode
```

The legacy `artifact` representation is therefore covered without requiring a browser state migration to occur before the visual contract becomes valid.

## 6. Implementation changes

Changed presentation layers:

```text
frontend/design-lab/cockpit-reintegration-presentation-integrity.css
frontend/design-lab/cockpit-reintegration-review-256.css
```

Changed deterministic gates:

```text
frontend/e2e/cockpit-reintegration-presentation-integrity.spec.ts
frontend/e2e/cockpit-reintegration-review-256.spec.ts
frontend/e2e/cockpit-reintegration-spatial-rail-angle.spec.ts
```

The older gates were updated so they no longer require parent `row-gap` to carry the spacing. They instead verify row-owned margins and the actual rendered separation between surfaces.

## 7. New compatibility regression

A new regression explicitly uses a user-like viewport:

```text
1536 x 864
```

and then forces the historical rail state:

```text
data-conversation-rail="artifact"
```

while the current UI still resolves Boxes as selected.

The test requires the same visible separation contract to survive that state.

This is deliberately stronger than merely testing the current canonical `boxes` string.

## 8. Focus disposition

No Focus implementation was changed in this pass.

The project owner's current evidence is:

```text
Focus is working as far as tested.
```

Therefore Research 098's Focus lifecycle recovery remains carried forward, but Focus is no longer part of the active defect investigation unless the project owner reproduces another failure.

## 9. Deterministic verification

Implementation target:

```text
29419f7a1ccbd3cbcdc98f333e1b594c01d63fb1
```

Complete Cockpit fidelity workflow:

```text
workflow run  33241369935
job           99071179670
result        SUCCESS
browser tests 74 / 74 passing
```

The suite includes the new legacy-artifact/user-like-viewport regression and all earlier source-faithful Cockpit tests.

## 10. Interpretation boundary

A 74/74 deterministic pass means the new implementation satisfies the encoded geometry contract.

It does not yet prove that the project owner's local browser now looks correct. The issue was discovered visually after a previous green gate, so the next gate remains human.

The project owner should pull the new branch state and inspect the Boxes rail again. The required visible result is simple:

```text
clear dark breathing room between the project-general artifact and first WorkUnit
clear dark breathing room between every successive WorkUnit
no change to the canonical WorkUnit footprint
no change to Focus behavior
```

If that visible result is confirmed, this integrity interruption can close and Adaptive Conversation Dock product review resumes.
