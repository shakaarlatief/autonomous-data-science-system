# Research 101: Project-General Thread Short-Viewport Containment Recovery

**Date:** 2026-08-29  
**Status:** IMPLEMENTED / DETERMINISTICALLY VERIFIED / AWAITING HUMAN VISUAL CONFIRMATION  
**Research class:** IMPLEMENTATION_INTEGRITY / HUMAN_EVIDENCE / RESPONSIVE_GEOMETRY  
**Scope:** Conversation Boxes project-general thread artifact only. The WorkUnit-to-WorkUnit spacing repaired in Research 100 is human-confirmed correct. Current-process Focus remains out of scope.  
**Interaction environment:** ChatGPT  
**Interaction session:** `chatgpt-10`  
**Branch:** `v1-cockpit-design-exploration`

## 1. Trigger

The project owner pulled the Checkpoint 262 grid-track recovery and visually confirmed:

```text
Conversation WorkUnit spacing
    correct
```

The same screenshot exposed one remaining rail defect:

```text
General project discussion
    not visually contained as its own first thread artifact
    first WorkUnit paints into / over the project-general row
```

This is a narrower defect than the earlier WorkUnit spacing failure. The accepted WorkUnit separation itself is now confirmed by the human review.

## 2. Residual implementation gap

Research 100 protected every WorkUnit grid row with a minimum height large enough to contain the transformed canonical WorkUnit before the 16px inter-track gap begins.

The project-general thread row was left with only:

```text
margin: 0
```

and inherited its sizing from the generic thread-item/grid behavior.

Unlike the WorkUnit rows, it therefore had no explicit containment floor at short desktop heights. The project artifact itself is not transformed, but it still occupies the same scrollable CSS Grid and must reserve enough track height for its existing 58px artifact plus the generic thread-item padding/border.

The project owner's short-height browser screenshot is direct evidence that this first row was not sufficiently protected in the integrated composition.

## 3. Recovery principle

Do not redesign the project-general artifact.

Reserve the row that owns it.

Current project-thread contract in Boxes/artifact mode:

```text
project thread row
    box-sizing       border-box
    height           auto
    min-height       74px
    margin           0
    padding          7px
    overflow         visible

project artifact
    box-sizing       border-box
    min-height       58px

thread-list row-gap
    16px
```

The 74px row corresponds to the existing 58px project artifact plus the existing thread-item vertical padding/border budget. The project artifact's visual design is unchanged.

## 4. Why the short-height regression matters

The prior spacing checks primarily exercised taller browser viewports. The project owner's screenshot came from a wide but vertically short browser content region.

A dedicated regression now uses:

```text
viewport  1776 x 766
```

This approximates the visible browser content region in the supplied screenshot rather than merely matching the outer screenshot dimensions including browser chrome.

The regression requires all of the following simultaneously:

```text
project row height >= 73.5px
project row top/bottom padding >= 7px
project artifact remains complete
first WorkUnit visible surface starts >=16px after project artifact bottom
WorkUnit-to-WorkUnit visible gaps remain >=20px
```

This closes the exact responsive blind spot exposed by the human review without weakening the Research 100 geometry contract.

## 5. Implementation changes

Updated presentation layers:

```text
frontend/design-lab/cockpit-reintegration-presentation-integrity.css
frontend/design-lab/cockpit-reintegration-review-256.css
```

Updated deterministic gate:

```text
frontend/e2e/cockpit-reintegration-review-256.spec.ts
```

No WorkUnit visual geometry, Conversation semantics, Focus behavior or Adaptive Dock composition was changed.

## 6. Deterministic verification

Implementation/test target:

```text
5913467cfffd535215da7ab2cb70bdeb2be9f2e9
```

Complete Cockpit fidelity workflow:

```text
workflow run  33247621778
job           99087735314
result        SUCCESS
browser tests 77 / 77 passing
```

The new 77th regression is:

```text
General project discussion remains a distinct first artifact at a short desktop viewport
```

The complete source-faithful Cockpit suite remains green.

## 7. Current interpretation

Human confirmation now establishes that Research 100 solved the WorkUnit separation defect.

Research 101 addresses only the remaining project-general containment defect seen in that successful spacing retest.

The deterministic result is strong but the final gate is again visual because the defect was reported from the real browser.

Required local result:

```text
General project discussion appears as one complete standalone first conversation artifact
clear dark separation follows it
first WorkUnit begins only after that separation
all WorkUnit spacing remains correct
```

If confirmed, the Conversation rail integrity interruption is closed and Adaptive Conversation Dock product review can resume.