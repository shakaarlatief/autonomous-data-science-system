# Specification 007: V1 Unified Project Cockpit Interaction Spike

**Date:** 2026-08-21  
**Status:** Candidate V1 frontend interaction specification v0.4 after fourth human review; revised executable interaction gate passed, next human visual/product gate remains open  
**Scope:** Bounded implementation spike for the immersive Project Cockpit, spatial focus interaction, scalable viewport navigation, geometric zoom, scalable project jump/search navigation, balanced always-pannable project space, canvas-dominant and fold-away chrome, true fullscreen, and collision-safe floating surfaces described in Research 002 through Research 006 and Checkpoints 117 through 123  
**Design session:** 03  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 03 - Project Cockpit & V1 Integration

## 1. Purpose

This specification turns the confirmed Project Cockpit direction into an executable frontend experiment without prematurely selecting a node-canvas framework or final product visual language.

The spike must answer whether ADS can provide a professional single-workspace experience in which the user can:

```text
see the project as a living analytical process
    -> navigate a project larger than the current viewport
    -> zoom and recover project context efficiently
    -> continue to pan/recenter even when the project is smaller than the viewport
    -> jump/search to meaningful project work
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

Core map work units, focus entry/exit, composer interactions, viewport navigation, zoom, project jump/search, HUD controls, and fullscreen controls must be keyboard reachable. Focus transitions must remain understandable when reduced motion is requested. The experience must preserve semantic headings/landmarks and must not rely on motion alone for state meaning.

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

### CPK-21: Scalable project jump and search navigation

Project navigation must not scale by adding one permanent toolbar button for every future work type or destination.

The Cockpit must support a bounded `Jump to` interaction that can combine:

```text
quick semantic destinations
    Active work
    Blocker
    Investigation
    Evaluation
    ...

searchable meaningful project work
    title/type search
    select result
    spatially move to result
```

The current representative project must expose `Investigation` as a quick destination because Production missingness is an active Investigation.

Smooth spatial relocation is preferred when reduced motion is not requested. The interaction must complete in a known unobstructed region rather than merely making the target barely visible at an edge.

### CPK-22: Geometric zoom with native laptop interaction

The Cockpit must support bounded geometric zoom in addition to two-dimensional panning.

Required interaction paths:

```text
explicit zoom out
current zoom indication
explicit zoom in
reset to 100%
fit project
keyboard zoom/recovery equivalents
trackpad pinch zoom
```

Two-finger trackpad movement should continue to pan project space naturally.

Zoom should preserve the user's approximate visual anchor where practical. The implementation may use browser-native wheel/pinch event behavior during the spike; this requirement does not by itself justify a canvas-library dependency.

Geometric zoom is not the final semantic-zoom system. It must coexist with the future semantic-scale architecture required by CPK-17.

### CPK-23: Canvas-dominant composition

The project operating surface should remain perceptually dominant throughout the Cockpit.

The composer, project-map controls, project details, and system context should behave as bounded floating or overlay surfaces where appropriate rather than creating large permanent opaque application bands.

In particular:

```text
project canvas should visually continue behind/around the composer
composer should not require a full-width opaque footer
project map controls should not require a second full-width header row
empty space between control clusters should remain visually part of the Cockpit where possible
```

Translucency and blur may be used as restrained material treatment, but the product must avoid decorative glassmorphism or weak contrast.

Collision safety from CPK-20 remains mandatory even when the canvas visually continues beneath floating surfaces.

### CPK-24: Fold-away primary HUD

The compact primary Cockpit HUD must itself be explicitly hideable when the user wants maximum operating space.

Required behavior:

```text
compact HUD
    -> explicit hide action

hidden HUD
    -> project canvas reclaims the vertical space
    -> small explicit restore affordance remains available
```

Pointer-proximity reveal may later supplement this behavior, but hover must not become the only way to recover the HUD.

### CPK-25: Symmetric always-pannable project world

The scrollable spatial world and the logical analytical project plane must be treated as distinct layout concerns.

At every supported geometric zoom, including when the scaled project plane is smaller than the visible browser viewport:

```text
space must remain available around all four sides of the project plane
project plane must remain centered inside that surrounding world
horizontal panning must remain possible
vertical panning must remain possible
user must be able to move the project through the visual center rather than being anchored to top/left
```

A fixed external padding value alone is insufficient if it permits the complete scrollable world to become smaller than the viewport.

The bounded spike should therefore guarantee both:

```text
minimum symmetric project gutter
minimum scroll range beyond the current viewport
```

The final production representation may use a different canvas technology, but it must preserve this interaction property.

### CPK-26: Balanced internal project-plane margins

External pan reserve from CPK-25 is distinct from the layout of content inside the project plane.

The representative project map should not have an arbitrary large unused grid tail on one side while beginning almost immediately at the opposite edge.

Stage zones and representative project work should therefore use visually balanced logical side margins unless project semantics provide a reason for intentional asymmetry.

This requirement does not imply that every future project graph must be perfectly geometrically symmetric.

### CPK-27: Stage orientation must survive geometric zoom

Stage orientation is a navigation aid rather than ordinary node detail.

The stage headings should remain visually clear enough to orient the user at normal, intermediate, and minimum supported geometric zoom. Purely shrinking stage typography proportionally with every canvas zoom is not sufficient if the headings become visually negligible.

The spike may compensate stage-header typography/height against geometric zoom, or later move stage orientation into a more independent semantic/HUD layer.

The stage names/taxonomy remain provisional. This requirement concerns visual orientation, not final stage semantics.

### CPK-28: Fold-away project-map controls

The floating map-control cluster must be explicitly hideable without making its capabilities inaccessible.

Required behavior:

```text
expanded project-map controls
    -> explicit fold action

folded project-map controls
    -> compact edge restore affordance
    -> project operating surface becomes visually quieter
```

The restore affordance must remain keyboard reachable and must not depend on pointer hover.

### CPK-29: Upper-corner placement for project detail surfaces

Expanded project-detail surfaces should use the available upper map area efficiently.

On desktop/laptop layouts, the Details surface should sit close to the upper-left available project-map corner while remaining below, rather than on top of, stage orientation.

This is a placement constraint, not a fixed pixel contract. Collision safety and responsive behavior remain authoritative.

### CPK-30: Restrained ambient spatial depth

Human review positively validated the current subtle ambient treatment of the project grid, including soft blended tonal/color variation that gives the large surface depth without competing with analytical content.

The candidate visual direction should preserve that general design quality:

```text
calm
subtle
professional
spatial
polished
analytical content remains dominant
```

This requirement does not freeze exact circles, gradients, colors, glow coordinates, or opacity values. The principle is restrained ambient depth rather than a specific decorative motif.

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

The scalable-viewport revision should also prove that later-stage and lower work can be located beyond the initial viewport without reducing the project to a single-screen diagram.

---

## 4. Spatial focus architecture

Preferred internal architecture:

```text
CockpitPage
    CompactFoldableCockpitHud
    ProjectMapSurface
        ScrollableProjectWorld
            CenteredProjectCanvas
                StageViewportHeader
                ProjectWorkUnits
        GeometricZoomController
        ProjectJumpSearch
    FocusHost
        DataPage reuse
        EdaPage reuse
        MissingnessFocus spike
    FoldableFloatingProjectControls
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

The scrollable world must also remain conceptually distinct from the logical project plane so minimum geometric zoom does not eliminate panning merely because the project fits inside the current viewport.

The implementation should prefer scalable navigation primitives directly when their stronger shape is already clear instead of knowingly proliferating disposable one-off toolbar controls.

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

Viewport position/zoom should not be persisted into project/domain state. Whether pan/zoom/HUD/control-fold state belongs in URL, browser-session UI state, or transient local UI state remains an implementation question.

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
CPK-T12  composer/context surfaces do not trap underlying work
CPK-T13  compact/expanded project chrome preserves usable viewport
CPK-T14  fullscreen control enters/exits when supported and degrades safely otherwise
CPK-T15  keyboard navigation can recover meaningful map locations without pointer-only panning
CPK-T16  scalable Jump to navigation exposes Investigation and searchable project work
CPK-T17  zoom controls, keyboard zoom, 100% reset, and fit-project behavior operate correctly
CPK-T18  trackpad-style pinch input changes geometric zoom while ordinary two-axis movement remains available
CPK-T19  project canvas visually continues behind the floating composer while lower work can still be brought fully clear of it
CPK-T20  primary Cockpit HUD can explicitly hide and restore without removing access to project navigation
CPK-T21  minimum zoom retains non-zero horizontal and vertical scroll range on a wide desktop viewport
CPK-T22  ProjectCanvas has symmetric surrounding margins inside ProjectWorld at minimum zoom
CPK-T23  user can move away from and recover the canonical position in all four directions
CPK-T24  stage orientation remains visually substantial at minimum supported zoom
CPK-T25  project-map controls can explicitly fold to and restore from an edge affordance
CPK-T26  compact ADS/project identity remains intentional rather than vertically fragmented
CPK-T27  expanded Details uses the upper available map area without covering stage orientation
```

Visual regression should not freeze the exploratory Cockpit design before human review. Screenshot artifacts may be generated for review, but a canonical Cockpit baseline should be promoted only after the visual concept is accepted.

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
final zoom range or zoom persistence contract
final pan-reserve dimensions
production project-search backend
pointer-proximity HUD/control reveal
production agent conversation backend
production streaming interaction protocol
full Validation/Features/Models/Evaluation workspaces
final Cockpit visual identity
exact permanent ambient-grid styling
final animation library
mobile-phone UI
```

---

## 8. Promotion rule

Specification 007 may be promoted only after:

1. the executable interaction gate passes;
2. direct Data/EDA views remain intact;
3. the focus architecture proves technically clean rather than duplicative;
4. the user reviews the revised Cockpit visually and confirms that the interaction direction matches the intended product experience;
5. large-project horizontal/vertical navigation is demonstrated rather than merely described;
6. floating surfaces no longer make lower/right project work inaccessible;
7. compact/fold-away HUD behavior is accepted through human review;
8. true fullscreen behavior is tested with graceful fallback;
9. geometric zoom, fit/recovery, and trackpad pinch behavior are usable in a real browser;
10. scalable Jump to/search navigation is preferable to dedicated-control proliferation in real use;
11. the canvas-dominant composer/control composition is visually accepted;
12. minimum-zoom panning and symmetric surrounding project space feel natural in real browser use;
13. strengthened stage orientation remains useful rather than visually heavy across zoom levels;
14. fold-away project-map controls and higher Details placement are accepted through human review;
15. restrained ambient depth continues to support, rather than distract from, professional analytical use;
16. significant scalability/accessibility defects discovered by the spike are resolved or explicitly incorporated into the next specification.
