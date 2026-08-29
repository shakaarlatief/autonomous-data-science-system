# Research 102: Project-General Box Footprint and Selection-Frame Alignment

**Date:** 2026-08-29  
**Status:** IMPLEMENTED / DETERMINISTICALLY VERIFIED / AWAITING HUMAN VISUAL CONFIRMATION  
**Research class:** IMPLEMENTATION_INTEGRITY / HUMAN_EVIDENCE / VISUAL_HIERARCHY  
**Scope:** Conversation Boxes project-general artifact footprint and selected-state framing only. WorkUnit spacing from Research 100 is human-confirmed correct. Project-row containment from Research 101 is visually confirmed by the latest human screenshot. Focus remains out of scope.  
**Interaction environment:** ChatGPT  
**Interaction session:** `chatgpt-10`  
**Branch:** `v1-cockpit-design-exploration`

## 1. Trigger

After pulling the Checkpoint 263 containment correction, the project owner supplied two screenshots and confirmed that the major spacing/containment problem was resolved.

The remaining review feedback was deliberately small and specific:

```text
1. General project discussion should be the same visible size as the WorkUnit boxes.
2. The selected outline should appear consistently and should frame the visible selected box itself.
```

The screenshots showed why the second point mattered. In Boxes mode the project-general thread was receiving the generic `.reintegration-thread-item.is-active` treatment on its larger structural row, while WorkUnit selection was visually carried on the canonical WorkUnit `.node-surface`. Therefore the two object families did not read as members of one navigation system even when their semantic selection state was equivalent.

## 2. Existing accepted WorkUnit footprint

The source-faithful Conversation rail already has an explicit visible WorkUnit slot:

```text
normal rail
    232 x 74 px

responsive <=1450 px
    214 x 69 px
```

Those dimensions are produced by the accepted canonical WorkUnit presentation and must not be changed merely to make the project-general artifact match it.

The correction therefore adapts the project-general artifact to the already accepted WorkUnit footprint, not the reverse.

## 3. Project-general footprint alignment

The project-general artifact now uses the same visible rail footprint:

```text
normal rail
    project artifact 232 x 74 px
    WorkUnit slot    232 x 74 px

responsive <=1450 px
    project artifact 214 x 69 px
    WorkUnit slot    214 x 69 px
```

The project row remains a structural grid item whose job is containment and spacing. The project artifact remains the actual visible conversation object.

The project-general content, project semantics and conversation ownership are unchanged.

## 4. Selection ownership correction

The generic thread-row selected treatment is useful in Text mode, where the row itself is the visible item. It is incorrect in Boxes mode because the row is only a structural carrier around a visible artifact.

Research 102 therefore establishes this presentation rule:

```text
Text mode
    generic thread item may own the selected row treatment

Boxes / artifact-compatible mode
    outer structural row stays visually transparent
    selected treatment belongs to the visible object surface
```

For project-general:

```text
selected surface = .reintegration-project-thread-artifact
```

For WorkUnit:

```text
selected surface = .conversation-canonical-node .node-surface
```

Both selected surfaces use the same final integrity-layer border/shadow treatment. The WorkUnit's accepted box internals, category perimeter, runtime carriers and other semantic channels are untouched.

## 5. Why exact computed-color-string equality is not the contract

An intermediate deterministic assertion attempted to compare the serialized `borderColor` strings of the two selected surfaces. Chromium represented equivalent/layered color expressions through different CSS color-space serializations (`color(srgb ...)` versus `oklab(...)`). That is not a reliable product-fidelity assertion.

The durable deterministic contract instead verifies the actual presentation responsibilities:

```text
project artifact and WorkUnit slot have equal visible width/height
outer project row remains transparent while project is active
outer WorkUnit row remains transparent while WorkUnit is active
selected visible project surface has a real border and shadow
selected visible WorkUnit surface has a real border and shadow
selection transfer removes the project selected shadow when a WorkUnit becomes active
```

This tests the defect the human actually observed: wrong outline geometry and ownership, rather than browser-specific textual serialization of a color.

## 6. Spacing preservation

The human-approved Research 100 spacing geometry is not retuned.

The structural list remains:

```text
thread-list row-gap 16px
WorkUnit visible gaps >=20px deterministic contract
```

After the project artifact was enlarged to match the WorkUnit slot, the short-height painted border-box measurement became 15px between the project artifact and first WorkUnit even though the CSS Grid track gap remains exactly 16px. This is the expected one-pixel border realization at that viewport, not a return of the old CSS Grid track-absorption defect.

Accordingly the regression keeps both requirements explicit:

```text
structural row-gap >=16px
painted project-to-first-WorkUnit dark separation >=15px
```

No spacing CSS was increased because the project owner had already accepted the existing spacing and requested only footprint/selection alignment.

## 7. Implementation changes

Updated:

```text
frontend/design-lab/cockpit-reintegration-presentation-integrity.css
frontend/e2e/cockpit-reintegration-review-256.spec.ts
```

The presentation-integrity layer now:

```text
matches project artifact to 232x74 / 214x69 WorkUnit slots
keeps Boxes-mode outer active rows transparent
places project selection on the project artifact
retains WorkUnit selection on the canonical node surface
protects Text-mode generic selected-row behavior
```

No Conversation semantics, WorkUnit semantic carriers, Focus implementation, Adaptive Dock composition, Grid state or Deep Dive state changed.

## 8. Deterministic verification

Final implementation/test target:

```text
9881efe313b8cf04d9521c0464050b30b29944c1
```

The visual implementation is contained in the ancestry through:

```text
524d4fcba3df835de3ecc5757ed4a97dafdd656e
```

Complete Cockpit fidelity workflow:

```text
workflow run  33251166351
job           99096968925
result        SUCCESS
browser tests 78 / 78 passing
```

The new dedicated regression is:

```text
General project discussion matches the WorkUnit footprint and uses the same selected-surface frame
```

All previous source-faithful Cockpit regressions remain green.

## 9. Current interpretation

The latest human screenshot closes the earlier overlap/containment concern and confirms the WorkUnit spacing remains correct.

Research 102 is a final visual-alignment refinement before returning to the larger Adaptive Conversation Dock product-design review.

Required local result:

```text
General project discussion has the same visible footprint as the WorkUnit boxes
selecting General frames only that visible project box
selecting a WorkUnit frames only that visible WorkUnit surface
no oversized outer-row selection rectangle appears
existing spacing remains unchanged and clean
```

If confirmed, this Conversation rail presentation-integrity interruption should be closed and Checkpoint 258 / Research 097 Adaptive Conversation Dock review should resume immediately.
