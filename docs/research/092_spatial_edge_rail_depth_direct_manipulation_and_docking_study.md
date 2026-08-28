# Research 092: Spatial Edge Rail Depth, Direct Manipulation and Docking Study

**Date:** 2026-08-28  
**Status:** CANDIDATE STUDY / AWAITING HUMAN REVIEW  
**Scope:** Advanced whole-product presentation study for the right-edge Project Cockpit tool surface. Tests functional depth, direct pull/stow behavior, progressive disclosure, layered controls and bounded detach/redock interaction on top of the source-faithful integrated Cockpit.  
**Authority:** Human-review candidate evidence only. No rail variant in this memo is selected, promoted or part of the accepted Cockpit baseline. Accepted WorkUnit, relation, project-world, Conversation, X5, Z7 and semantic mechanisms retain their existing authority.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** `chatgpt-09`  
**Conversation title:** `09 - Project Cockpit Design Exploration`

---

## 1. Human design prompt

The current Product Surface Study A replaced the rejected long horizontal integration toolbar with a compact right-side spatial tool rail. During whole-Cockpit human review, a stronger possibility was proposed:

```text
Do not treat the rail as a flat toolbar that is merely shown or hidden.

Treat the right edge as a spatial control object with depth.
Let the user pull it into the Cockpit.
Let additional function appear as physical/spatial layers.
Let the user put that capability away again through direct manipulation.
Potentially allow a rail to detach into the world and redock.
```

The design question is therefore not simply whether the rail should look more three-dimensional. The question is whether **depth and direct manipulation can carry useful Cockpit interaction semantics**.

## 2. Internal design context

This study builds on existing Cockpit direction rather than reopening accepted Phase-C mechanisms.

Relevant prior evidence includes:

```text
Research 007
    continuous finite project world
    right-side vertical map/tool direction

Research 008
    world-owned spatial atmosphere
    bounded floating surfaces / collision-aware product behavior

Research 009 / Specification 008
    compact and fold-away immersive chrome
    scalable Jump/search
    spatial navigation and recovery

Research 091 + Product Surface Study A
    complete source-faithful integrated Cockpit as the current
    whole-product evaluation substrate
```

The right-side rail itself remains provisional product presentation. The accepted capabilities accessible through it are not provisional merely because their shell is under review.

## 3. External interaction references consulted

Three reference families were used for inspiration during this bounded study:

### Apple visionOS ornaments

The relevant design idea is that controls can occupy a spatial layer slightly in front of a primary content surface rather than consuming the same content plane. The transferable principle is **functional z-order and spatial attachment**, not visual imitation of visionOS.

### Microsoft Fluent elevation

The relevant principle is that elevation, ambient shadow and directional shadow communicate hierarchy and relationship. Depth is most useful when it explains what is attached, above, active or temporary, rather than when it exists as decorative 3D styling.

### Dockview docking / floating interaction models

The relevant interaction ideas are edge-pinned groups, floating groups, drag-based relocation, bounded movement, snapping and redocking. The transferable principle is **direct manipulation with recoverable attachment states**.

These external references are inspiration only. They do not define ADS product semantics or override internal human-reviewed design evidence.

## 4. Study hypothesis

The durable hypothesis being tested is:

```text
DEPTH SHOULD ENCODE FUNCTION

attachment
    the control object belongs to the Cockpit edge

hierarchy
    controls can occupy distinguishable functional layers

progressive disclosure
    pulling the object farther can reveal more capability

temporary detachment
    a surface may become spatially independent without becoming semantically independent

recovery
    direct manipulation should include obvious ways to stow or redock
```

A visually impressive but semantically meaningless 3D rail would not satisfy this hypothesis.

## 5. Candidate A: Extruded Blade

Route:

```text
/design-lab/cockpit-reintegration.html?focus=map&work=v&rail=blade
```

Interaction model:

```text
compact edge blade
    -> grip and drag left
    -> blade physically widens into the Cockpit
    -> labels and grouping progressively appear
    -> docked / partial / fully-open snap states
    -> drag right to stow
```

Functional groups:

```text
Navigation
Work
System
```

Important design property:

The same real controls remain mounted. The blade changes their spatial presentation rather than replacing them with a second mock toolbar.

Primary question:

```text
Can progressive physical opening make a dense tool rail both calm at rest
and substantially more legible when the user wants it?
```

Potential strength:
- direct and understandable relation between pull distance and disclosure;
- keeps a strong edge attachment;
- labels become available without permanently widening the shell.

Potential risk:
- could still feel like a conventional drawer with 3D decoration if the depth does not add enough functional value.

## 6. Candidate B: Layered Deck

Route:

```text
/design-lab/cockpit-reintegration.html?focus=map&work=v&rail=deck
```

Interaction model:

```text
compact stacked edge object
    -> grip and drag left
    -> functional layers fan into the Cockpit
    -> Navigation / Work / System occupy distinct spatial planes
    -> secondary layers become usable when opened
    -> drag right to stack them back at the edge
```

Primary question:

```text
Can the rail become a reusable spatial organization system for Cockpit capability,
rather than merely a column of buttons?
```

Potential strength:
- most directly explores the user's idea that pulling the rail can "bring layers into the Cockpit";
- creates a possible future grammar for different categories of Cockpit function;
- depth communicates functional grouping rather than only surface elevation.

Potential risk:
- fan-out may become visually busy or gimmicky;
- too much lateral spread could obscure the project world;
- the layer taxonomy must remain meaningful if this direction is later developed.

## 7. Candidate C: Dock and Float

Route:

```text
/design-lab/cockpit-reintegration.html?focus=map&work=v&rail=float
```

Interaction model:

```text
edge-docked rail
    -> pull left past detach threshold
    -> rail becomes a lifted floating object
    -> move it through bounded project space
    -> related surfaces open beside its current position
    -> return it to the right-edge snap zone
    -> release to redock
```

Primary question:

```text
Should Cockpit chrome sometimes become a manipulable spatial object
that can temporarily live where the user is working?
```

Potential strength:
- strongest direct-manipulation model;
- can put controls near current work without permanently consuming screen width;
- detach/redock expresses a genuine change of spatial relationship.

Potential risk:
- floating chrome may compete with WorkUnits and connectors;
- users may need more recovery/discoverability support;
- freedom of placement can become clutter if not tightly bounded.

## 8. Shared implementation invariants

All three candidates obey the same integration boundary:

```text
real existing Cockpit controls are moved/reused
not recreated as visual mocks

WorkUnit semantics remain unchanged
relation meaning and directionality remain unchanged
selected WorkUnit remains unchanged by rail manipulation
project camera remains independent from rail manipulation

full-focus Conversation owns the stage when active
deep-focus specialist workspace owns the stage when active
spatial rail study surfaces disappear rather than competing with those states

reduced-motion behavior remains available
keyboard manipulation/recovery remains available
floating movement is bounded

legacy click-to-fold arrow is hidden inside the study variants
because direct manipulation is the interaction under evaluation
```

No candidate is allowed to acquire semantic authority merely because it occupies a visually higher z-plane.

## 9. Implementation artifacts

Primary study artifacts:

```text
frontend/design-lab/cockpit-spatial-rail-study.css
frontend/design-lab/cockpit-spatial-rail-study.js
frontend/e2e/cockpit-reintegration-spatial-rail.spec.ts
```

Study loader / integrated substrate:

```text
frontend/design-lab/cockpit-product-surface-study.js
frontend/design-lab/cockpit-product-surface-study.css
frontend/design-lab/cockpit-product-surface-study-readability.css
frontend/design-lab/cockpit-reintegration.html
```

CI coverage was also strengthened because the prior workflow path filter watched `cockpit-reintegration*` but not the newer whole-product study modules. The holistic fidelity workflow now also watches:

```text
frontend/design-lab/cockpit-product-surface-study*
frontend/design-lab/cockpit-spatial-rail-study*
```

This prevents future whole-product study code from bypassing the browser fidelity gate.

## 10. Automated validation

Implementation target before preservation docs:

```text
30f92a55537a9b0a2ec14695ed2982ded4ec9c0e
```

Final holistic workflow:

```text
workflow run  33197594115
job           98938593583
result        SUCCESS
browser tests 56 / 56 passing
```

The spatial-rail tests specifically prove:

```text
A / Blade
    pulls open
    becomes materially wider
    reveals labelled groups
    preserves selected WorkUnit
    retains real Jump/search behavior

B / Layered Deck
    creates three distinct spatial layers
    fans them apart when pulled
    keeps secondary controls usable
    preserves selected WorkUnit

C / Dock and Float
    detaches from the edge
    moves within bounded project space
    retains real Jump/search behavior
    redocks through the edge snap zone
    preserves selected WorkUnit

focus ownership
    full-focus Conversation suppresses the study rail
```

The same 56-test run also retained all existing source-faithful WorkUnit, relation, G4/H4, X5, Z7, Conversation, appearance and navigation coverage.

## 11. Product-surface corrections completed during the study

The new rail work exposed two older Product Surface Study A assertions that had not yet reached the intended human-readable result:

```text
Conversation search text
    legacy child selector still held it at 8px
    corrected to a normal readable line box

full Conversation composer
    still reserved excessive resting height
    redundant context strip removed
    resting textarea and actions compacted
    normal message/composer typography retained
```

These were corrected without changing Quiet Graphite ownership or Conversation semantics.

## 12. Current outcome

```text
TECHNICAL STUDY IMPLEMENTED
HOLISTIC BROWSER GATE PASS
HUMAN REVIEW OPEN
NO WINNER SELECTED
NO HYBRID SELECTED
NO PRODUCTION CHANGE
```

The three candidates remain deliberately comparable evidence.

## 13. Human review questions

The next review should judge each candidate in the complete Cockpit rather than as an isolated animation.

Key questions:

```text
Which resting state is calmest and least intrusive?

Does drag-to-open feel more natural than click-to-fold?

Does depth actually clarify relationship and function,
or does it read as ornamental 3D?

Does Blade's progressive disclosure feel useful and premium?

Do the Layered Deck planes create meaningful organization,
or visual clutter?

Does Dock and Float feel powerful and flexible,
or too intrusive in the project world?

Is the grip discoverable without becoming visually loud?

Should later exploration combine strengths of multiple candidates?
```

A hybrid may be explored after human evidence, but no hybrid should be inferred before reviewing the three current candidates.

## 14. Next boundary

```text
human compare A / Blade, B / Layered Deck and C / Dock and Float
    -> record concrete reactions
    -> preserve rejected / held / preferred properties separately
    -> refine or combine only on evidence
    -> do not promote a rail design before explicit human selection
```

Production `/cockpit` remains untouched.