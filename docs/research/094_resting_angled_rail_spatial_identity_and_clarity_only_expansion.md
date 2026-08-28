# Research 094: Resting Angled Rail Spatial Identity and Clarity-Only Expansion

**Date:** 2026-08-28  
**Status:** CANDIDATE STUDY / AWAITING HUMAN REVIEW  
**Scope:** Corrects the design interpretation behind Research 092 and Research 093. Establishes that the intended 2.5D / 3D Cockpit feeling belongs to the right-side rail itself in its ordinary resting state, while any expanded state exists only to make the controls easier to understand.  
**Authority:** Human clarification and current whole-product candidate evidence. Existing accepted Phase-C mechanisms and Specification 008 retain their established authority. This research does not promote the new rail visual treatment before human review.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** `chatgpt-09`  
**Conversation title:** `09 - Project Cockpit Design Exploration`

---

## 1. Human clarification

Research 092 and Research 093 over-interpreted the relationship between spatial presentation and direct manipulation.

The project owner clarified that the supplied Cockpit/FUI reference was intended primarily to communicate the **resting geometry of the bar itself**:

```text
the bar sits at a visually effective angle
that angle makes the surrounding interface feel spatial / 3D
```

The expanded form serves a different purpose:

```text
expanded rail
    = extra clarity about what the controls mean

expanded rail
    != the source of the 3D environment feeling
```

Therefore the previous instruction to slowly pull the rail through intermediate deployment states was based on the wrong design question.

## 2. Corrected design decomposition

The rail problem is now split into three independent concerns.

### A. Spatial identity

```text
always present in the normal resting rail

carried by:
    inward-facing perspective
    fixed right-edge orientation
    visible chassis thickness
    rear construction / depth
    subtle trapezoidal geometry
    world-facing attachment
```

This is the primary design question.

### B. Clarity expansion

```text
optional readability state

may:
    widen the rail
    reveal control labels
    make function easier to understand

must not:
    create the perspective
    intensify the perspective as its semantic purpose
    create new depth planes
    imply that 3D exists only while expanded
```

This is secondary to the resting design.

### C. Direct manipulation

```text
not required for the current spatial-rail goal
```

The project does not currently need separate Hinge, Stack, Console, Blade, Deck or Float drag mechanics in order to create the intended 3D impression.

Direct manipulation is not globally forbidden. It may be revisited later if a distinct functional Cockpit need justifies it. It is simply **not the mechanism by which this rail should feel spatial**.

## 3. Diagnosis of the previous study

Research 093 correctly identified several useful reference properties:

```text
central world remains primary
side surface points inward toward the world
perspective matters
visible frame thickness matters
architectural attachment matters
```

But it then incorrectly bound those properties to deployment:

```text
pull
-> hinge / telescope / console movement
-> progressively stronger spatial state
```

That coupling was unnecessary and distracted from the actual visual problem.

The corrected question is much narrower:

```text
Can the ordinary compact right-side bar itself look like a physical
Cockpit instrument surface oriented into the project world?
```

## 4. Current single-candidate implementation

Live route:

```text
/design-lab/cockpit-reintegration.html?edge=angled
```

Primary artifacts:

```text
frontend/design-lab/cockpit-spatial-rail-study-angle.css
frontend/design-lab/cockpit-spatial-rail-study-angle.js
frontend/e2e/cockpit-reintegration-spatial-rail-angle.spec.ts
```

Loader integration:

```text
frontend/design-lab/cockpit-product-surface-study.js
```

The study intentionally uses one coherent rail direction instead of three new drag architectures.

## 5. Resting rail geometry

The compact state is the primary state under review.

Current study geometry:

```text
compact authored width       72px
right-edge attachment        fixed
perspective distance         1050px
Y orientation                -24deg
X orientation                0.8deg
screen-plane rotation        -0.8deg
front-face Z translation     20px
rear construction offset     +10px x / +7px y / -28px z
```

The front rail and rear construction use the same base orientation. The rear surface is displaced backward so thickness is visible even before any interaction occurs.

The rail also uses:

```text
restrained trapezoidal silhouette
right-edge spine
subtle left-side luminous seam
Quiet-Graphite-compatible dark materials
restrained shadow and frame contrast
```

These are provisional visual choices. The important current hypothesis is the **resting angled physical surface**, not the exact numerical angle or ornament values.

## 6. Clarity-only expansion

The rail has one small button for revealing labels.

Behavior:

```text
compact
    authored width 72px
    icons only

clarity expanded
    authored width 220px
    same real controls
    labels become visible
```

Critically:

```text
front-face 3D transform does not change
rear-face 3D identity does not depend on expansion
project camera does not change
selected WorkUnit does not change
```

The width transition is therefore a readability aid, not a spatial transition.

No drag grip exists in the current study. No slider role exists. No partial deployment states exist.

## 7. Real Cockpit capability remains underneath the rail

The study reuses the actual current Cockpit controls rather than building a visual-only toolbar.

Examples include:

```text
Jump / search
zoom out / zoom in
Fit project
Reset view
Expand selected WorkUnit
Deep Dive
Current process focus
Conversations
Appearance
Hide project HUD
Fullscreen
```

Existing listeners remain attached because the real DOM control nodes are moved into the angled shell.

The legacy fold control is hidden only inside this candidate study because the clarity control is the presentation behavior currently being reviewed.

## 8. Semantic and ownership invariants

Changing rail clarity must not mutate:

```text
WorkUnit category
WorkUnit disposition
operational status
attention
SEL2 selection
X5 semantic state
relation class
D0-D3 directionality
project camera state
Conversation ownership
Deep Dive ownership
```

Full-stage ownership remains unchanged:

```text
full-focus Conversation
    -> angled rail hides

Deep Dive specialist workspace
    -> angled rail hides
```

The rail is product shell presentation only.

## 9. Deterministic validation

Implementation target:

```text
67c3105ff26601a2f259e44007b23ce638b23838
```

Holistic Cockpit workflow:

```text
run       33202773778
job       98956116141
result    SUCCESS
coverage  64 / 64 browser tests passing
```

The four new tests establish that:

```text
1. the compact resting rail already has a non-flat perspective transform
   and a separately transformed rear-depth surface;

2. no Gen 2 drag grip or slider interaction exists in the clarified study;

3. clarity expansion increases readable width and reveals labels while the
   rail transform, project camera and selected WorkUnit remain unchanged;

4. real Cockpit controls remain operational and Conversation / Deep Dive keep
   their established stage ownership.
```

The complete 64-test run also retains all previous source-faithful Cockpit, Phase-C, Product Surface, Research 092 and Research 093 regression coverage.

## 10. Disposition of earlier rail studies

Historical implementations remain preserved for provenance:

```text
Research 092
    A Extruded Blade
    B Layered Deck
    C Dock and Float

Research 093
    A Hinged Instrument Panel
    B Telescoping Layer Stack
    C Spatial Command Console
```

Their current disposition changes in an important but limited way:

```text
preserved as design history / interaction evidence
not the active rail design axis
not candidates the human must compare before proceeding
not required to create the intended 3D Cockpit feeling
```

This does **not** mean every direct-manipulation concept is rejected for all future purposes. It means the previous studies solved a more complicated interaction problem than the current visual goal required.

## 11. Current human-review question

Human review should begin with the compact rail at rest.

Primary questions:

```text
Does the bar itself now make the Cockpit feel spatial?
Is the inward angle visually convincing?
Does the rail look attached to the project environment rather than pasted on top?
Is the visible thickness enough, too much or too decorative?
Is the resting rail calm enough for continuous use?
Does it occupy the right amount of visual attention?
Does the angle make the controls harder to read or click?
```

Only after judging the resting rail should the clarity button be opened.

The expanded state should then be judged only for:

```text
label readability
control comprehension
width / occlusion
quality of compact-to-labelled transition
```

The expanded state is not a second 3D design candidate.

## 12. Exact next step

```text
open the single clarified rail route

/design-lab/cockpit-reintegration.html?edge=angled

judge the compact rail first
then optionally open labels for clarity
preserve concrete visual reactions
refine the rail's resting angle / depth / material only on that evidence
```

No rail visual treatment is promoted at this research boundary.