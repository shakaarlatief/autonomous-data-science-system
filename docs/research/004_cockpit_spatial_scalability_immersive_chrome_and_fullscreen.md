# Research 004: Cockpit Spatial Scalability, Immersive Chrome, and Fullscreen

**Date:** 2026-08-20  
**Status:** Active design exploration after second human Cockpit review  
**Scope:** Spatial growth, viewport navigation, immersive chrome, overlay safety, and true browser fullscreen for the Project Cockpit  
**Design session:** 02  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 02 - Methodological Brain & Knowledge Units

## 1. Trigger

The first executable Cockpit interaction spike passed its automated gate and was reviewed in a real browser.

Human review confirmed that the stage-zone visual grammar is strong:

```text
Framing
Data & Exploration
Validation
Modeling
Evaluation
```

with a technical background grid, semantic work blocks, and visible connections.

The review also exposed four important requirements:

```text
1. lower/right floating UI must never make project content inaccessible;
2. large projects need professional two-dimensional navigation and growth;
3. project title/header chrome currently consumes too much of the Cockpit viewport;
4. ADS should support actual browser fullscreen in addition to immersive in-app layout.
```

These are not cosmetic refinements. They define how the Cockpit can scale into a serious long-running project workspace.

---

## 2. Immediate defect: floating surfaces must not cover unreachable content

The first spike places the system composer and a System Focus surface near the lower viewport edge.

In the reviewed composition, lower project content can become visually obscured while the map itself does not provide enough viewport movement to reveal it.

This violates the more general rule:

```text
floating chrome may overlay the viewport
    !=
project content may become unreachable
```

Any docked composer, inspector, approval card, minimap, or floating control must reserve a safe interaction area or be independently collapsible/movable.

Preferred behavior:

```text
map viewport
    has bottom/right safe insets for docked surfaces

floating inspector
    collapsible
    never traps underlying nodes

composer
    docked to viewport
    map can still pan/scroll behind and beyond it
```

The viewport should always be able to move far enough that any work block can be brought into a fully unobstructed central working region.

---

## 3. Large projects should become a spatial workspace, not a taller static diagram

The project map must be able to grow substantially in both axes.

Do not solve scale only by stacking more blocks vertically.

Preferred interaction model:

```text
large logical canvas
    horizontal growth across methodological/project stages
    vertical growth for branches, parallel investigations, reopened work, and subproblems

viewport
    pan horizontally
    pan vertically
    zoom
    fit project
    fit active path
    jump to selected work
```

The user must be able to move right through later project areas. Browser-visible horizontal movement is therefore not optional.

The visual experience may use direct scrolling, click-drag/space-drag panning, trackpad two-axis panning, wheel/Shift+wheel behavior, or a canvas library later. The exact mechanism remains to be tested, but the semantic requirement is durable: the project is larger than the viewport and the viewport navigates over it.

Accessibility requires a non-pointer path as well. Keyboard focus, jump/search commands, and explicit navigation controls must remain available even if freeform panning becomes the primary pointer interaction.

---

## 4. Scaling requires semantic zoom, not only geometric zoom

A very large project cannot remain readable if every work block is always shown at the same detail level.

Preferred principle:

```text
zoomed out
    stage health
    active path
    blockers
    major milestones
    grouped investigations

middle scale
    meaningful work units
    important branches
    dependencies

focused scale
    individual investigation/artifact/question surfaces
    detailed analytical workspace
```

This is semantic zoom: the amount and type of information changes with scale.

Potential professional mechanisms:

```text
collapsible stage regions
grouped branch clusters
summary nodes for completed historical work
expand-on-demand investigations
active-path emphasis
search/jump-to-object
minimap or navigator
"fit active work" and "fit project" commands
```

The project map should not become an indiscriminate graph of every persisted object.

---

## 5. Stage headers should become part of the viewport frame

Human review strongly preferred the stage names and boundaries, but the first spike places them inside a large rounded map panel below a large project heading.

The stronger direction is:

```text
Cockpit viewport begins near the top of the application

Framing | Data & Exploration | Validation | Modeling | Evaluation | ...
    remain spatially aligned with the canvas
    remain visible or rapidly recoverable while navigating
```

Candidate behavior:

```text
sticky stage strip
    horizontally moves with the logical canvas
    vertically stays at the top of the Cockpit viewport
```

The technical grid and stage divisions should feel like the operating surface itself, not a dashboard card placed inside another page.

---

## 6. Project title/header should collapse into immersive chrome

The large project title, objective sentence, and summary counts are useful orientation information, but they should not permanently consume a large fraction of the primary work surface.

Preferred model:

```text
normal project views
    conventional project chrome is acceptable

Cockpit
    compact persistent HUD
    full project metadata available on demand
```

Candidate Cockpit top states:

### Compact state

```text
ADS | Customer Churn Prediction | running 1 | approval 1 | search | project views | fullscreen
```

approximately one small toolbar high.

### Expanded project HUD

Triggered by an explicit click/keyboard control, and optionally discoverable by pointer proximity:

```text
project title
objective
current stage
blocking questions
run state
important project metadata
```

The expanded HUD may slide/fade down over the canvas and retract again.

Pointer-hover alone must not be required because that would be inaccessible and unreliable on touch/keyboard devices.

The initial project title may still appear prominently when opening a project or when the user explicitly requests project context, but not as permanently allocated vertical layout space.

---

## 7. True browser fullscreen is desirable and technically feasible

The Cockpit should have an explicit fullscreen control.

For the web application this means using the standards-based Fullscreen API where available:

```text
user activates fullscreen control
    -> Cockpit/root element requests fullscreen
    -> browser chrome is removed
    -> Cockpit uses the full display

Escape / explicit exit control
    -> leaves fullscreen
```

Important constraints:

```text
fullscreen must originate from a user interaction
support/permission must be detected
fullscreenchange must synchronize UI state
failure must degrade cleanly to normal immersive mode
```

The normal in-app immersive mode remains valuable even when browser fullscreen is unavailable.

Future standalone packaging, for example a desktop shell, may provide an even stronger native-window fullscreen experience, but it is not required to achieve true fullscreen in the browser spike.

---

## 8. Recommended combined Cockpit hierarchy

The strongest current product model is:

```text
BROWSER / DESKTOP WINDOW

optional TRUE FULLSCREEN
        |
        v
COMPACT COCKPIT HUD
        |
STICKY STAGE STRIP
        |
        v
+---------------------------------------------------------------+
|                                                               |
|             LARGE TWO-DIMENSIONAL PROJECT CANVAS              |
|                                                               |
|     pan / scroll / zoom / semantic zoom / branch / group      |
|                                                               |
|                                                               |
+---------------------------------------------------------------+
        |
DOCKED SYSTEM COMPOSER
```

Additional context surfaces should be overlays/drawers that are collapsible and collision-safe rather than permanent columns.

---

## 9. Important distinction: infinite-feeling does not require infinite implementation

The interface may feel spatially open without requiring an unbounded mathematical canvas in V1.

A production implementation can use a bounded but dynamically expanding logical workspace with virtualization and selective mounting.

```text
visible/relevant work units
    rendered

offscreen distant work
    cheap representation or unmounted

deep Data/EDA/Model workspaces
    mounted only when focused
```

This preserves the earlier rule:

```text
everything reachable from the Cockpit
    !=
everything mounted simultaneously
```

---

## 10. Revised near-term Cockpit requirements

Before the next human gate, the Cockpit should demonstrate:

```text
1. no inaccessible lower/right content;
2. horizontal and vertical viewport movement;
3. enough logical canvas size to prove later-stage navigation;
4. compact/collapsible project header;
5. stage labels aligned near the top of the operating viewport;
6. explicit true-fullscreen toggle with graceful fallback;
7. composer and contextual surfaces that never make nodes unreachable;
8. at least one fit/reset/jump navigation affordance;
9. keyboard-accessible alternatives to pointer panning;
10. no premature requirement that every project block remain visible at every zoom/detail level.
```

Semantic zoom, branch grouping, minimap, automatic layout, and canvas-library selection can then be evaluated against real project scale rather than selected prematurely.
