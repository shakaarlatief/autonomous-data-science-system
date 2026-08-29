# Checkpoint 263: Project-General Thread Containment Human Recheck Opened

**Date:** 2026-08-29  
**Status:** HUMAN_RECHECK_OPEN  
**Branch:** `v1-cockpit-design-exploration`  
**Interaction session:** `chatgpt-10`

## Human result from Checkpoint 262

The project owner confirmed the Research 100 spacing recovery:

```text
WorkUnit-to-WorkUnit spacing
    correct
```

Therefore the CSS Grid track-gap recovery is human-accepted for the spacing defect it targeted.

The same screenshot exposed one residual problem:

```text
General project discussion artifact
    overlaps / is visually invaded by the first WorkUnit
```

Checkpoint 263 narrows the active gate to that project-general first-row containment only.

## Implemented correction

The project-general thread row now reserves its own minimum track footprint instead of relying on generic automatic grid sizing:

```text
project thread min-height  74px
project thread padding      7px top / bottom
project thread margin       0px
project artifact min-height 58px
thread-list row-gap         16px
```

The project artifact design is unchanged.

The WorkUnit spacing implementation accepted in the Checkpoint 262 human retest is unchanged.

## Deterministic verification

Implementation/test target:

```text
5913467cfffd535215da7ab2cb70bdeb2be9f2e9
```

Workflow:

```text
Cockpit reintegration fidelity
run   33247621778
job   99087735314
result SUCCESS
77 / 77 browser tests passing
```

The new regression explicitly uses a short desktop viewport:

```text
1776 x 766
```

and requires the project-general artifact to remain complete and visibly separated from the first WorkUnit.

## Human recheck

Pull and hard-refresh the plain canonical route:

```text
http://localhost:4173/design-lab/cockpit-reintegration.html
```

Open Conversation in Boxes mode.

Required visible result:

```text
General project discussion is a complete standalone first artifact
no WorkUnit overlaps it
clear dark separation after it
all previously corrected WorkUnit spacing remains intact
```

If confirmed:

```text
close the Conversation presentation-integrity interruption
resume the Adaptive Conversation Dock review from Checkpoint 258 / Research 097
```

If not confirmed:

```text
keep the screenshot and exact route/viewport
continue only project-general rail geometry debugging
```
