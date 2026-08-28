# Checkpoint 254: Resting Angled Cockpit Rail Human Review Opened

**Date:** 2026-08-28  
**Status:** Current human-review checkpoint  
**Checkpoint class:** CONTINUITY / PRODUCT_DESIGN / WHOLE_PRODUCT_PRESENTATION  
**Project stage:** V1 next-generation Project Cockpit advanced whole-product design exploration on the source-faithful integrated substrate  
**Scope:** Records the project owner's correction that the intended spatial / 3D feeling belongs to the right-side rail itself at rest, not to drag or deployment behavior. Opens human review of one clarified resting angled rail with optional clarity-only label expansion.  
**Authority:** Current routing boundary for right-side rail presentation. Existing accepted Phase-C mechanisms and Specification 008 retain their established authority. The angled rail remains provisional until explicit human selection.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** `chatgpt-09`  
**Conversation title:** `09 - Project Cockpit Design Exploration`  
**Primary collaborator:** ChatGPT

## 1. Boundary correction

Checkpoint 253 opened three Gen 2 architectural edge candidates whose primary interaction was drag-based deployment.

The project owner clarified that this was still the wrong interpretation of the supplied visual reference.

The intended distinction is:

```text
3D / spatial Cockpit feeling
    comes from the bar itself
    in its normal resting state

expanded bar
    exists only for clarity
    so the user can see what each control means
```

Therefore there is no current need for separate Hinge, Stack or Console drag designs, nor for slow review of intermediate deployment states.

Research 094 preserves the detailed correction and implementation evidence.

## 2. Current single candidate

Live route:

```text
http://localhost:4173/design-lab/cockpit-reintegration.html?edge=angled
```

The current candidate is a compact right-edge instrument rail with:

```text
permanent inward-facing perspective
visible rear depth / chassis thickness
fixed right-edge attachment
restrained trapezoidal face geometry
subtle architectural spine
Quiet-Graphite-compatible material treatment
real existing Cockpit controls
```

The rail is already spatial before the user interacts with it.

## 3. Expansion is clarity only

A small rail control can widen the bar from compact icon mode to a labelled mode.

That behavior is deliberately constrained:

```text
compact
    icons
    spatial rail already present

expanded clarity
    wider surface
    same spatial transform
    labels visible
```

It does not:

```text
hinge
fan into layers
float
change depth hierarchy
change the project camera
change selected work
create the 3D effect
```

No drag grip or slider exists in this candidate.

## 4. Previous rail studies

Research 092 and Research 093 remain preserved as design history and interaction evidence.

Their drag architectures are no longer the active comparison set for this visual goal.

This is a scoped correction, not a universal ban on direct manipulation. Future direct manipulation would need its own functional justification rather than being used merely to make the rail feel spatial.

## 5. Implementation artifacts

```text
frontend/design-lab/cockpit-spatial-rail-study-angle.css
frontend/design-lab/cockpit-spatial-rail-study-angle.js
frontend/e2e/cockpit-reintegration-spatial-rail-angle.spec.ts
frontend/design-lab/cockpit-product-surface-study.js
```

The existing holistic fidelity workflow already watches these file families.

## 6. Deterministic validation

Implementation target:

```text
67c3105ff26601a2f259e44007b23ce638b23838
```

Complete Cockpit fidelity run:

```text
run       33202773778
job       98956116141
result    SUCCESS
browser   64 / 64 passing
```

The four new checks specifically protect the clarified boundary:

```text
resting compact rail already has perspective and rear depth
no drag grip / slider exists
clarity expansion leaves rail transform and project state unchanged
real controls and full-stage ownership remain intact
```

All previous source-faithful Cockpit behavior also remains green.

## 7. Preservation disposition

```text
accepted Phase-C mechanisms                 unchanged
Specification 008                           unchanged
Product Surface Study A                     provisional
Research 092 drag studies                   historical / inactive current axis
Research 093 Gen 2 drag studies             historical / inactive current axis
Resting Angled Rail                         current candidate / unselected
clarity-only expansion                      candidate supporting behavior
production /cockpit                         untouched
scientific experiment status                unchanged / INCOMPLETE
```

## 8. Current human-review gate

The next actor is the human reviewer.

The compact state should be judged first for:

```text
quality of the resting angle
strength of the spatial / 3D feeling
physical credibility of the right-edge attachment
visible thickness and depth
calmness
material quality
control readability
visual weight
project-world occlusion
fit with the intended ADS Cockpit character
```

Only after that should the clarity control be opened to judge:

```text
label readability
whether the wider state is useful
whether it obscures too much work
```

There is no need to drag or slowly pull anything.

## 9. Exact next step

```text
open the single resting-angle route
judge the bar itself while compact
optionally click the clarity control to inspect labels
record concrete reactions
then refine the resting rail geometry on evidence
```

No angled-rail visual treatment is promoted at this checkpoint.