# Specification 007: V1 Unified Project Cockpit Interaction Spike

**Date:** 2026-08-20  
**Status:** Candidate V1 frontend interaction specification v0.1 pending executable and human validation  
**Scope:** First bounded implementation spike for the immersive Project Cockpit and spatial focus interaction described in Research 002, Research 003, and Checkpoint 117  
**Design session:** 02  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 02 - Methodological Brain & Knowledge Units

## 1. Purpose

This specification turns the confirmed Project Cockpit direction into an executable frontend experiment without prematurely selecting a node-canvas framework or final product visual language.

The spike must answer whether ADS can provide a professional single-workspace experience in which the user can:

```text
see the project as a living analytical process
    -> select a meaningful work unit
    -> smoothly enter a focused analytical workspace
    -> perform real Data / EDA work using the same functional components as direct project views
    -> retain project/system context
    -> return spatially to the project map
```

The goal is not to finish the Cockpit. The goal is to establish the interaction architecture and test whether the experience is strong enough to justify deeper visual exploration.

---

## 2. Non-negotiable product requirements

### CPK-01: Immersive primary surface

The Cockpit must use the full application window with minimal persistent chrome. The normal project sidebar, topbar, and methodological side panel must not permanently consume Cockpit space.

### CPK-02: Living project map

The zoomed-out state must show a bounded project-process projection with stage orientation and dynamic work units. It must not expose every persisted domain object or represent agents as the primary visible units.

### CPK-03: Meaningful work-unit semantics

Visible units should represent user-relevant project work such as:

```text
objective/framing
Data understanding
EDA investigation
Question/blocker
validation design
baseline modeling
alternative model work
evaluation
```

### CPK-04: Spatial click-to-focus interaction

Selecting supported work units must create the experience that the selected unit expands into the working surface and the wider project recedes. Returning must restore the project map context.

The implementation may hand off between DOM surfaces internally. It must not literally scale a small node into a complex table/chart workspace.

### CPK-05: No browser-style page reload

Focus changes must occur inside the single-page application. Deep analytical work must not require a document reload.

### CPK-06: Shared specialist functionality

The spike must prove that at least Data and EDA functionality can be used in both:

```text
direct project route
Cockpit focus host
```

without duplicating their substantive implementation.

### CPK-07: URL-addressable focus state

Cockpit focus and important local analytical state must be representable in route/search state so refresh, browser Back/Forward, bookmarking, and future deep links can reconstruct the active workspace.

### CPK-08: Native system composer

A system interaction composer must be visually native to the Cockpit. The spike may use non-authoritative mock behavior, but the interaction must not be designed as a permanently dominant generic chat column.

### CPK-09: Project-state visibility

The zoomed-out map must make completed, active, blocked, approval-waiting, recommended/relevant, and deferred work visually distinguishable without requiring the user to inspect hidden metadata.

### CPK-10: Focus-aware context

The focused workspace must expose enough context to make clear:

```text
where the user is
why this work exists
how to return
what methodological/project state is relevant
```

### CPK-11: Performance architecture boundary

The implementation must preserve the principle:

```text
everything reachable from the Cockpit
    !=
everything mounted or loaded simultaneously
```

This spike must not create one enormous always-mounted project graph containing every deep analytical component.

### CPK-12: Accessibility and reduced motion

Core map work units, focus entry/exit, and composer interactions must be keyboard reachable. Focus transitions must remain understandable when reduced motion is requested. The experience must preserve semantic headings/landmarks and must not rely on motion alone for state meaning.

### CPK-13: Responsive professional desktop behavior

The interaction must remain usable at 1440, 1280, and 1024 pixel desktop/laptop widths. Horizontal project-map scrolling is acceptable in an early spike if spatial relationships remain understandable, but deep work surfaces must not overlap permanent chrome.

### CPK-14: No premature canvas-library lock-in

The first spike should use ordinary React/CSS/SVG/browser primitives where sufficient. React Flow or another spatial-canvas library should only be selected after the interaction proves valuable and concrete requirements justify the dependency.

### CPK-15: Human visual/product gate

Automated tests are necessary but insufficient. The spike is not accepted until human review determines that the Cockpit feels like the primary product work environment rather than a decorative process diagram placed on top of existing pages.

---

## 3. Representative scenario

Use the existing deterministic Customer Churn Prediction fixture.

The project map should communicate at least:

```text
Objective defined
Data understood
Prediction moment unresolved / blocking
Production missingness investigation awaiting attention
EDA available
Chronological validation selected
Logistic baseline completed
Random Forest benchmark deferred
Evaluation work downstream
```

Supported first focus targets:

```text
Data understanding
EDA
Production missingness investigation
```

The Data and EDA targets must use the existing specialist workspace components rather than a second Cockpit-specific implementation.

---

## 4. Spatial focus architecture

Preferred internal architecture:

```text
CockpitPage
    ProjectMapSurface
    FocusHost
        DataPage reuse
        EdaPage reuse
        MissingnessFocus spike
    SystemComposer
```

The visible transition may use the browser View Transition API when available, with a CSS/reduced-motion-safe fallback.

The browser implementation should behave conceptually as:

```text
project map work unit
    -> transition starts
    -> map recedes
    -> full-resolution focus workspace mounts
```

not:

```text
complex workspace permanently nested inside scaled node
```

---

## 5. Route-state contract for the spike

Candidate Cockpit route:

```text
/cockpit
```

Candidate search state:

```text
focus=map|data|eda|missingness
column=<data variable>
filter=<data filter>
view=distribution|trend
```

The exact public URL contract remains provisional. The spike must prove that this state model supports Back/Forward and refresh without visible page-loading semantics.

---

## 6. Automated validation gates

The first implementation gate should prove at minimum:

```text
CPK-T01  /cockpit renders immersive map without normal permanent shell chrome
CPK-T02  Data work unit enters a real Data workspace
CPK-T03  Data focus preserves column/filter route state
CPK-T04  EDA work unit enters the existing EDA workspace
CPK-T05  EDA view state remains addressable
CPK-T06  Missingness work unit opens a dedicated focused investigation surface
CPK-T07  focus -> map return works and remains keyboard reachable
CPK-T08  browser Back restores prior Cockpit focus state
CPK-T09  core Cockpit has no serious/critical automated accessibility violations
CPK-T10  normal direct /data and /eda routes continue to work
```

Visual regression should not freeze the first exploratory Cockpit design before human review. A screenshot artifact may be generated for review, but a canonical baseline should be promoted only after the visual concept is accepted.

---

## 7. Explicit non-goals

This spike does not yet select or implement:

```text
React Flow or another graph framework
final project auto-layout algorithm
final stage taxonomy
multi-level arbitrary/infinite spatial nesting
production agent conversation backend
production streaming interaction protocol
full Validation/Features/Models/Evaluation workspaces
final Cockpit visual identity
final animation library
mobile-phone UI
```

---

## 8. Promotion rule

Specification 007 may be promoted only after:

1. the executable interaction gate passes;
2. direct Data/EDA views remain intact;
3. the focus architecture proves technically clean rather than duplicative;
4. the user reviews the Cockpit visually and confirms that the interaction direction matches the intended product experience;
5. any significant scalability/accessibility defect discovered by the spike is resolved or explicitly incorporated into the next specification.
