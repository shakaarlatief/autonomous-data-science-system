# Checkpoint 253: Architectural Cockpit Edge Gen 2 Human Review Opened

**Date:** 2026-08-28  
**Status:** Current human-review checkpoint  
**Checkpoint class:** CONTINUITY / PRODUCT_DESIGN / WHOLE_PRODUCT_INTERACTION  
**Project stage:** V1 next-generation Project Cockpit advanced whole-product design exploration on the source-faithful integrated substrate  
**Scope:** Preserves the second-generation architectural Cockpit edge study prompted by the human FUI/Cockpit reference and opens human comparison of three fixed-edge instrument-surface candidates.  
**Authority:** Current routing boundary for Gen 2 edge-surface review. Existing accepted Phase-C mechanisms and Specification 008 retain their established authority. Product Surface Study A, Research 092 candidates and all Gen 2 candidates remain provisional unless explicitly selected.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** `chatgpt-09`  
**Conversation title:** `09 - Project Cockpit Design Exploration`  
**Primary collaborator:** ChatGPT

## 1. Boundary transition

Checkpoint 252 opened the first three-way spatial rail study:

```text
A · Extruded Blade
B · Layered Deck
C · Dock and Float
```

Human review then supplied a stronger architectural-Cockpit reference and clarified that the desired direction was not merely a draggable or elevated toolbar.

The new hypothesis is:

```text
the Cockpit edge itself can behave like an instrument surface
with thickness, perspective and spatial attachment around the project world
```

Research 093 preserves the detailed rationale, implementation and execution evidence.

## 2. Reference-derived design direction

The supplied external reference was:

```text
Cockpit Platform x FUI
https://dribbble.com/shots/20914787-Cockpit-Platform-x-FUI
```

The study uses only the relevant spatial grammar:

```text
central world remains primary
side surfaces surround / point toward the central plane
visible panel thickness and perspective
architectural edge attachment
possible hinge / telescope / console deployment
```

ADS does not adopt the reference's neon science-fiction styling as a design decision.

## 3. Open Gen 2 candidates

### A · Hinged Instrument Panel

```text
fixed right Cockpit edge
-> pull inner grip left
-> angled instrument wing widens / pivots toward the user
-> header and control labels progressively appear
-> push back to stow
```

### B · Telescoping Layer Stack

```text
fixed right Cockpit edge
-> pull inner grip left
-> Navigation / Work / System become three separate depth planes
-> planes telescope different distances into the project world
-> push back to restack
```

### C · Spatial Command Console

```text
fixed right Cockpit edge
-> pull inner grip left
-> edge expands into a deeper context-aware command surface
-> selected WorkUnit title remains visible as presentation context
-> controls gain a wider multi-column composition at full deployment
-> push back to stow
```

No Gen 2 candidate is selected.

## 4. Live human-review routes

```text
A · Hinged Instrument Panel
http://localhost:4173/design-lab/cockpit-reintegration.html?edge=hinge

B · Telescoping Layer Stack
http://localhost:4173/design-lab/cockpit-reintegration.html?edge=stack

C · Spatial Command Console
http://localhost:4173/design-lab/cockpit-reintegration.html?edge=console
```

A lab-only `COCKPIT EDGE · GEN 2` switcher permits comparison in the same integrated project context.

## 5. Fixed-edge interaction correction

The final interaction architecture is intentionally:

```text
Cockpit edge / rig
    fixed in place

instrument surface
    deploys left from the fixed edge

grip
    remains attached to the stable edge
    receives direct pointer input

project world behind the rig
    keeps normal pointer ownership outside the grip / deployed surface
```

This is both mechanically robust and closer to the physical instrument-panel idea under review.

## 6. Real capability remains underneath the study

The candidate surfaces reorganize the actual existing controls:

```text
Navigation
    Jump/search
    zoom
    Fit
    Reset

Work
    Expand
    Deep Dive
    Focus
    Conversations

System
    Appearance
    Hide HUD
    Fullscreen
```

No fake parallel toolbar was introduced.

## 7. Ownership and semantic invariants

Spatial deployment must not mutate:

```text
WorkUnit semantic state
selection
relation meaning / directionality
X5 meaning
project camera meaning
Conversation ownership
Deep Dive semantic state
```

Stage ownership remains:

```text
full-focus Conversation
    hides Gen 2 surface

Deep Dive
    hides Gen 2 surface
```

The candidate therefore remains shell presentation only.

## 8. Deterministic validation

Final implementation target before preservation:

```text
c29b19932bc10a2d3aa1e3d507010a4f3211aa4a
```

Final complete Cockpit fidelity workflow:

```text
run       33201023215
result    SUCCESS
browser   60 / 60 passing
```

The complete gate includes all earlier source-faithful reintegration checks, Phase-C completion checks, Conversation and Product Surface Study A checks, first-generation spatial-rail tests and the four Gen 2 architectural-edge tests.

## 9. Preservation disposition

```text
accepted Phase-C mechanisms                 unchanged
Specification 008                           unchanged
Product Surface Study A                     provisional
Gen 1 A · Extruded Blade                    preserved / unselected
Gen 1 B · Layered Deck                      preserved / unselected
Gen 1 C · Dock and Float                    preserved / unselected
Gen 2 A · Hinged Instrument Panel           candidate / unselected
Gen 2 B · Telescoping Layer Stack           candidate / unselected
Gen 2 C · Spatial Command Console           candidate / unselected
production /cockpit                         untouched
scientific experiment status                unchanged / INCOMPLETE
```

Opening Gen 2 does not reject Gen 1. Passing CI does not select Gen 2.

## 10. Current human-review gate

The next actor is the human reviewer.

Review should physically drag each candidate through partial and full deployment and judge:

```text
resting calmness
architectural integration
perspective / depth quality
fixed-edge credibility
intermediate-state quality
functional grouping
project-world occlusion
readability
control access
whether depth communicates function rather than decoration
closest match to the intended ADS Cockpit feeling
properties worth combining across candidates
```

## 11. Exact next step

```text
open A, B and C
slowly drag the fixed inner grip
compare partial and full states
record concrete reactions
then preserve refinement / rejection / selection evidence
```

No winner or hybrid is selected at this checkpoint.