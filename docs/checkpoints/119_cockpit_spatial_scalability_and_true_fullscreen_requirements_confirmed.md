# Checkpoint 119: Cockpit Spatial Scalability and True Fullscreen Requirements Confirmed

**Date:** 2026-08-20  
**Status:** Historical design and human-product-review checkpoint  
**Checkpoint class:** DESIGN  
**Project stage:** Post-V0 V1 professional frontend exploration; second human review of executable Project Cockpit  
**Scope:** Records acceptance of the stage-zone visual grammar and captures newly exposed requirements for large-project navigation, collision-safe floating UI, compact immersive chrome, and true browser fullscreen  
**Authority:** Historical rationale and design evidence. Research 004 and candidate Specification 007 v0.2 define the active implementation requirements. This checkpoint does not select a final canvas library, auto-layout algorithm, semantic-zoom implementation, or final visual identity.  
**Design session:** 02  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 02 - Methodological Brain & Knowledge Units

## 1. Human review result

The second real-browser Cockpit review positively confirmed the current stage-zone visual grammar.

Particularly successful elements:

```text
technical dark operating canvas
stage areas with visible boundaries
Framing / Data & Exploration / Validation / Modeling / Evaluation orientation
semantic work blocks
connections between meaningful project work
clear blocked / investigation / decision / completed distinctions
```

This supports continuing the living-project-map direction rather than returning to a normal page/dashboard as the primary work interface.

---

## 2. Immediate defect discovered

The lower-right Cockpit composition can make content difficult or impossible to access because the map does not yet provide enough viewport movement while the composer/System Focus surfaces occupy fixed space.

This is a real usability defect, not merely a visual preference.

New requirement:

```text
floating/docked Cockpit chrome
    must never make project work unreachable
```

The next implementation must provide safe viewport insets and/or sufficient pan/scroll movement, plus collapsible contextual surfaces.

---

## 3. Large-project scalability direction

The user explicitly raised that real projects may become much larger than the first demonstration.

The response is not to stack all future blocks vertically or force the entire project to fit one viewport.

The Cockpit should become a two-dimensional navigable workspace:

```text
horizontal project/stage progression
+
vertical branching / parallel work / reopened work
+
viewport pan or scroll
+
zoom
+
fit/jump/search navigation
```

Later/right project work must be explicitly reachable.

As scale grows, semantic zoom/grouping is expected to become necessary so completed history and detailed branches do not remain equally prominent at all zoom levels.

No final graph/canvas implementation is selected yet.

---

## 4. Immersive layout requirement strengthened

The first spike successfully removed the normal project sidebar and right methodological column, but the large Cockpit title/objective/summary header still consumes too much permanent space.

The target is now stronger:

```text
whole practical viewport
    = Cockpit operating surface
```

Preferred direction:

```text
small persistent HUD
stage strip near top of viewport
large map/canvas immediately below
bottom system composer
project metadata expands on demand and retracts again
```

The stage zones should feel like the application itself rather than a rounded map card nested below a dashboard-style project header.

Hover/proximity may enhance the experience but cannot be the only interaction because controls must remain keyboard/touch accessible.

---

## 5. True fullscreen confirmed as a product requirement

A browser-level fullscreen option is desired in addition to the in-app immersive Cockpit.

The next implementation should evaluate the standards-based browser Fullscreen API so a user action can remove browser chrome and let ADS occupy the complete display when supported.

Required production behavior includes:

```text
explicit user action
support detection
enter fullscreen
fullscreen state synchronization
explicit exit + normal Escape behavior
graceful fallback when unavailable/denied
```

The application must not depend on automatically entering fullscreen during page load.

---

## 6. Preservation/promotion audit

This review does not justify a new project-level Foundation or technology decision.

It does justify:

```text
Research 004
    cockpit spatial scalability, immersive chrome, true fullscreen

Specification 007 revision
    v0.1 -> candidate v0.2
    adds scalable viewport, semantic scale boundary,
    compact chrome, fullscreen, and collision-safe overlay gates
```

No React Flow/canvas framework, minimap implementation, automatic layout system, or semantic-zoom algorithm is selected.

---

## 7. Exact next frontend slice

Before the next human review:

```text
1. fix inaccessible lower/right content;
2. add explicit horizontal + vertical project viewport navigation;
3. demonstrate project extent larger than one screen;
4. replace large permanent project header with compact/expandable Cockpit HUD;
5. move stage orientation to the top of the operating viewport;
6. add true-fullscreen control with graceful fallback;
7. keep composer/context surfaces collision-safe;
8. add fit/reset/jump navigation affordance;
9. preserve keyboard accessibility;
10. rerun cross-platform build, interaction, accessibility, and visual checks;
11. return to human visual/product review before freezing the design.
```
