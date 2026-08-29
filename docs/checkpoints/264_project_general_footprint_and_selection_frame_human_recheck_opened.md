# Checkpoint 264: Project-General Footprint and Selection-Frame Human Recheck Opened

**Date:** 2026-08-29  
**Status:** HUMAN_RECHECK_OPEN  
**Branch:** `v1-cockpit-design-exploration`  
**Interaction session:** `chatgpt-10`

## Human result from Checkpoint 263

The project owner's latest screenshots confirm the substantive Conversation rail integrity repairs:

```text
WorkUnit-to-WorkUnit spacing
    correct

General project discussion containment
    correct
    no longer invaded by the first WorkUnit
```

The remaining feedback is a small visual-consistency refinement:

```text
General project discussion should match the WorkUnit box size.
Selection framing should surround the visible selected box consistently.
```

## Implemented correction

### Equal visible footprint

```text
normal rail
    General project discussion 232 x 74 px
    WorkUnit box slot          232 x 74 px

responsive <=1450 px
    General project discussion 214 x 69 px
    WorkUnit box slot          214 x 69 px
```

The WorkUnit geometry is unchanged. The project artifact was aligned to the accepted WorkUnit rail footprint.

### Correct selected-surface ownership

In Boxes mode the generic thread row is now structural only and remains visually transparent when active.

Selection is rendered on the visible object:

```text
project-general thread
    selected frame on project artifact

WorkUnit thread
    selected frame on canonical WorkUnit surface
```

Text mode retains its row-based selected treatment.

## Spacing preservation

The human-approved Research 100 geometry is not retuned:

```text
thread-list row-gap 16px
WorkUnit-to-WorkUnit visible gap contract >=20px
```

At the short desktop viewport, equalizing the project artifact height yields a 15px painted edge-to-edge dark separation while the structural CSS Grid gap remains 16px. This is retained rather than increasing spacing that the project owner already approved.

## Deterministic verification

Final implementation/test target:

```text
9881efe313b8cf04d9521c0464050b30b29944c1
```

Complete Cockpit fidelity workflow:

```text
run    33251166351
job    99096968925
result SUCCESS
78 / 78 browser tests passing
```

The dedicated regression verifies equal project/WorkUnit visible dimensions, transparent structural active rows, selected-state border/shadow on the actual visible surfaces and correct selection transfer.

## Human recheck

Pull and hard-refresh:

```text
http://localhost:4173/design-lab/cockpit-reintegration.html
```

Open Conversation in Boxes mode and switch between:

```text
General project discussion
Resolve target definition
other WorkUnit conversations
```

Required visible result:

```text
General project discussion is the same visible size as the WorkUnit boxes
General selection frames only the project box itself
WorkUnit selection frames only the WorkUnit itself
no larger outer wrapper appears around either selection
existing spacing remains correct
```

If confirmed:

```text
close the Conversation presentation-integrity interruption
resume Checkpoint 258 / Research 097 Adaptive Conversation Dock product review
```

If not confirmed:

```text
preserve screenshot and route/viewport
continue only this footprint/selection-frame boundary
```
