# Research 095: Conversation Box Spacing, Flat Project Rail and Live Topology Compass

**Date:** 2026-08-28  
**Status:** IMPLEMENTED / DETERMINISTICALLY VERIFIED / AWAITING HUMAN VISUAL REVIEW  
**Scope:** Narrow whole-product corrections requested during review of the source-faithful integrated Cockpit.  
**Interaction environment:** ChatGPT  
**Interaction session:** `chatgpt-09`  
**Branch:** `v1-cockpit-design-exploration`

## 1. Human review input

The project owner requested three corrections:

```text
Conversation Boxes rail
    separate the WorkUnit boxes more clearly
    use breathing room comparable to the gap after the project-general box

right-side Cockpit rail
    keep the current compact structure
    remove the 2.5D / 3D angle
    make it normal 2D

Deep Dive topology compass
    current surrounding box is visually wrong
    compass does not appear to actually work
```

This review supersedes the active spatial-angle hypothesis from Research 094 for the current rail direction. The prior 3D/angled studies remain preserved as historical design evidence.

## 2. Conversation spacing correction

The canonical Boxes rail already preserved the accepted M20 WorkUnit footprint. The remaining issue was vertical packing.

The current correction sets the Boxes-mode thread-list gap to:

```text
10px
```

The exact pixel value remains a whole-product presentation detail that can still be tuned after visual review. The intended decision is more durable:

```text
canonical WorkUnit conversation boxes must read as distinct objects
and must not visually run into each other vertically
```

No WorkUnit geometry, conversation ownership, Boxes/Text semantics or project-general identity changed.

## 3. Flat right-side rail

The project owner explicitly rejected the current 3D treatment while asking to preserve the rail itself.

The correction therefore keeps:

```text
compact right-side position
existing real Cockpit controls
current control ordering
current compact width behavior
clarity-only label expansion
full Conversation / Deep Dive ownership behavior
```

and removes:

```text
perspective
Y/X/Z rotations
front-face Z translation
rear depth plate
3D spine
angled clip-path silhouette
3D-specific shadows
```

The implementation continues to use the existing `?edge=angled` study route for continuity, but the active presentation on that route is now deliberately flat. The route name is historical implementation plumbing, not the current design description.

The current flat rail remains a human-review candidate, not a promoted production surface.

## 4. Compass diagnosis

M17 freezes:

```text
compact topology compass retained
return preserves coherent project context
```

The accepted Z7 fixture at:

```text
04616a52df5cceff6c59223bbd6f07448d027510
```

used a static decorative mini-map with five hard-coded dots. The current integrated Project Grid contains six WorkUnits. The static fixture therefore could not truthfully report current project position and did not update when selection changed.

The project owner's observation that the compass did not really work was correct.

## 5. Live topology compass correction

The new adapter derives its contents from the actual mounted Project Grid.

For every current WorkUnit it now derives:

```text
node key
project-world position
human-readable title
selected/current state
relation adjacency
```

It also reads the real mounted relation groups and renders the current topology links in the mini-map.

The current selected WorkUnit is the single highlighted position. Directly related WorkUnits receive quieter related emphasis. Changing project selection and entering Deep Dive again updates the compass to the new actual source WorkUnit.

Important semantic boundary:

```text
compass is an orientation instrument
compass does not own selection
compass does not mutate project state
compass is not a second project navigator
```

## 6. Compass container correction

The prior composition visually created a box around another boxed mini-map.

The corrected treatment uses:

```text
one compact outer instrument container
one border around the instrument
inner topology field without a second border
clear reserved vertical space before specialist side panels
```

Current authored review geometry:

```text
outer width       132px
minimum height     96px
inner topology     62px high
side reserve      114px
```

These exact values are provisional and may be visually tuned. The important correction is the single coherent instrument hierarchy and collision-free specialist layout.

## 7. Implementation artifacts

```text
frontend/design-lab/cockpit-reintegration-review-255.css
frontend/design-lab/cockpit-reintegration-topology-compass.js
frontend/design-lab/cockpit-reintegration-review-fixes.js
frontend/e2e/cockpit-reintegration-spatial-rail-angle.spec.ts
```

Implementation target:

```text
10cf3cfd26553d95c3b786df6d3a14137a29767a
```

## 8. Deterministic evidence

Complete Cockpit fidelity workflow:

```text
run       33207377429
job       98971755372
result    SUCCESS
browser   65 / 65 passing
```

The five current review checks establish that:

```text
flat rail has no perspective or transform
rear/spine depth construction is hidden
clarity expansion remains presentation-only
Conversation Boxes have deliberate vertical separation
live compass renders one dot per actual WorkUnit
live compass renders current relation links
exactly one current WorkUnit is highlighted
compass follows a changed selection across Deep Dive entry
inner topology field does not add a second border
specialist side panels remain clear of the compass
all existing source-faithful Cockpit tests still pass
```

Automated success does not determine whether the spacing, rail surface or compass styling looks good. Human visual review remains required.

## 9. Disposition

```text
resting 3D / angled rail hypothesis     rejected for current rail direction
Gen 1 / Gen 2 3D studies                preserved as historical evidence
flat compact rail                       current review candidate
clarity-only label expansion            retained
Conversation box separation intent      requested / implemented
exact 10px gap                          provisional visual tuning value
compact topology compass                held M17 capability
static five-dot compass fixture          superseded in integration
live project-derived compass             current implementation candidate
compass as navigator                     not introduced
production /cockpit                       untouched
```

## 10. Human-review gate

Review the current integrated browser in three states:

```text
1. full Conversation, Boxes mode
   judge spacing between every canonical WorkUnit box

2. Project Grid
   judge the flat right-side rail at rest and with label clarity expanded

3. Deep Dive
   judge the single-box compass composition
   confirm that its highlighted position corresponds to the focused WorkUnit
```

Only visual tuning should follow unless review reveals a genuine behavioral defect.
