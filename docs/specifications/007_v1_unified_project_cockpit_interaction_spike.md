# Specification 007: V1 Unified Project Cockpit Interaction Spike

**Date:** 2026-08-20  
**Status:** Candidate V1 frontend interaction specification v0.2 after first and second human review; executable interaction gate passed, immersive-scale human gate remains open  
**Scope:** Bounded implementation spike for the immersive Project Cockpit, spatial focus interaction, scalable viewport navigation, immersive chrome, and true fullscreen described in Research 002 through Research 004 and Checkpoints 117 through 118  
**Design session:** 02  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 02 - Methodological Brain & Knowledge Units

## 1. Purpose

This specification turns the confirmed Project Cockpit direction into an executable frontend experiment without prematurely selecting a node-canvas framework or final product visual language.

The spike must answer whether ADS can provide a professional single-workspace experience in which the user can:

```text
see the project as a living analytical process
    -> navigate a project larger than the current viewport
    -> select a meaningful work unit
    -> smoothly enter a focused analytical workspace
    -> perform real Data / EDA work using the same functional components as direct project views
    -> retain project/system context
    -> return spatially to the project map
```

The goal is not to finish the Cockpit. The goal is to establish the interaction architecture and test whether the experience is strong enough and scalable enough to justify deeper visual exploration.

---

## 2. Non-negotiable product requirements

### CPK-01: Immersive primary surface

The Cockpit must use essentially the full application window with minimal persistent chrome. The normal project sidebar, topbar, and methodological side panel must not permanently consume Cockpit space.

The large project title/objective/summary composition from the first spike is not sufficient as the permanent Cockpit layout. Project metadata must be available without permanently reserving substantial vertical space.

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

Core map work units, focus entry/exit, composer interactions, viewport navigation, and fullscreen controls must be keyboard reachable. Focus transitions must remain understandable when reduced motion is requested. The experience must preserve semantic headings/landmarks and must not rely on motion alone for state meaning.

### CPK-13: Responsive professional desktop behavior

The interaction must remain usable at 1440, 1280, and 1024 pixel desktop/laptop widths. A project larger than the viewport must support explicit horizontal and vertical movement. Deep work surfaces and floating chrome must not overlap content in a way that makes it unreachable.

### CPK-14: No premature canvas-library lock-in

The early spike should use ordinary React/CSS/SVG/browser primitives where sufficient. React Flow or another spatial-canvas library should only be selected after the interaction proves valuable and concrete pan/zoom/layout/virtualization requirements justify the dependency.

### CPK-15: Human visual/product gate

Automated tests are necessary but insufficient. The spike is not accepted until human review determines that the Cockpit feels like the primary product work environment rather than a decorative process diagram placed on top of existing pages.

### CPK-16: Two-dimensional scalable viewport

The project process may substantially exceed the current viewport in both dimensions.

The Cockpit must therefore support a professional viewport model with at least:

```text
horizontal movement
vertical movement
recovery to a known overview
jump/focus to meaningful work
```

Pointer panning, trackpad panning, wheel behavior, scroll containers, and later canvas-library primitives are implementation choices. The semantic requirement is that later stages and vertical branches remain reachable regardless of project size.

### CPK-17: Semantic scale strategy

Large-project readability must not rely only on geometric zoom.

The architecture must permit later semantic zoom and grouping such that different scale levels can expose different information density:

```text
project/stage summaries
meaningful work units
focused investigation detail
```

The spike does not need to implement the final semantic-zoom algorithm, but it must not choose a DOM/layout structure that assumes every work object remains simultaneously visible at full detail.

### CPK-18: Immersive and collapsible Cockpit chrome

The Cockpit should maintain only a compact persistent HUD.

Detailed project metadata such as the full title, objective, summary counts, and project context should be available through an explicit expand/collapse interaction rather than permanently allocating substantial canvas height.

Hover/proximity behavior may supplement the interaction but must not be the only way to reveal controls or project metadata.

Stage labels should be visually integrated with the operating viewport and should remain visible or quickly recoverable while moving vertically through a large project.

### CPK-19: True fullscreen mode

The Cockpit must evaluate an explicit true-fullscreen control using the standards-based browser Fullscreen API where supported.

Required behavior:

```text
explicit user action
    -> enter fullscreen when available

fullscreenchange
    -> synchronize UI state

Escape / explicit control
    -> leave fullscreen

unsupported / denied
    -> degrade to normal immersive Cockpit without failure
```

The application must not assume fullscreen can be entered automatically on page load.

### CPK-20: Collision-safe floating surfaces

The system composer, contextual inspector, approval UI, minimap, and other floating surfaces must never make work units permanently inaccessible.

The map viewport must reserve appropriate safe insets or be pannable beyond overlay boundaries. Context surfaces should be collapsible or repositionable when needed.

A user must always be able to bring a work unit into an unobstructed working area.

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

The scalable-viewport revision should also prove that later-stage work can be located beyond the initial viewport without reducing the project to a single-screen diagram.

---

## 4. Spatial focus architecture

Preferred internal architecture:

```text
CockpitPage
    CompactCockpitHud
    StageViewportHeader
    ProjectMapSurface
    FocusHost
        DataPage reuse
        EdaPage reuse
        MissingnessFocus spike
    FloatingContextSurface
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

The map surface must be architected as a viewport over project space rather than a static diagram whose entire logical extent must fit in one browser frame.

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

Viewport position/zoom should not be persisted into project/domain state. Whether it belongs in URL/session UI state remains an implementation question.

---

## 6. Automated validation gates

The implementation gate should prove at minimum:

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
CPK-T11  later/right and lower work remains reachable through viewport navigation
CPK-T12  docked composer/context surfaces do not trap underlying work
CPK-T13  compact/expanded project chrome preserves usable viewport
CPK-T14  fullscreen control enters/exits when supported and degrades safely otherwise
CPK-T15  keyboard navigation can recover meaningful map locations without pointer-only panning
```

Visual regression should not freeze the exploratory Cockpit design before human review. Screenshot artifacts may be generated for review, but a canonical baseline should be promoted only after the visual concept is accepted.

---

## 7. Explicit non-goals

This spike does not yet select or fully implement:

```text
React Flow or another graph framework
final project auto-layout algorithm
final stage taxonomy
final semantic-zoom algorithm
final minimap/navigation implementation
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
5. large-project horizontal/vertical navigation is demonstrated rather than merely described;
6. floating surfaces no longer make lower/right project work inaccessible;
7. immersive header/chrome behavior is accepted through human review;
8. true fullscreen behavior is tested with graceful fallback;
9. significant scalability/accessibility defects discovered by the spike are resolved or explicitly incorporated into the next specification.
