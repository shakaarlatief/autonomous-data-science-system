# Research 007: Fifth Cockpit Human Review, Continuous Grid World, Stage Ruler, and Vertical Tool Rail

**Date:** 2026-08-21  
**Status:** Human product-review evidence and bounded design resolution  
**Scope:** Project Cockpit continuous spatial grid, neutral navigation reserve, viewport-aware stage orientation, finite-world boundary signaling, and vertical project-map controls  
**Design session:** 03  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 03 - Project Cockpit & V1 Integration

## 1. Context

The fourth Cockpit review established a balanced always-pannable spatial world around the semantic project plane. That iteration fixed an important navigation defect: even when geometric zoom made the project smaller than the viewport, the user could still pan in all four directions and recenter the project.

The fifth human review was strongly positive about the continuing progress, but the improved geometry exposed a new visual weakness. At minimum zoom, the project plane appeared as a relatively small gridded rectangle surrounded by a much larger ungridded dark reserve.

The navigation reserve was functionally correct, but the composition made the Cockpit feel like a small diagram inside a larger empty container rather than one large professional spatial workspace.

The user proposed a stronger direction:

```text
zoom out / pan beyond current project extent
    -> grid continues through the surrounding navigation space
    -> workspace feels spatially larger rather than like a smaller box
    -> stage orientation remains available near the top
    -> true finite boundaries remain possible but should be subtle
```

The review also asked whether the map-control cluster should remain horizontal or become vertical.

---

## 2. Primary design resolution: navigation space is grid space, not semantic stage space

The strongest interpretation is not to stretch the existing stage columns to fill every newly visible pixel.

That would conflate two different concepts:

```text
navigation / spatial reserve
    space in which the user can pan, recenter and orient the project

semantic project regions
    Framing
    Data & Exploration
    Validation
    Modeling
    Evaluation
```

If stage widths expanded merely because the browser became wider or the user zoomed out, the apparent semantic extent of a stage would become a viewport-dependent visual accident.

The resolved architecture is therefore:

```text
FiniteNavigableGridWorld
    neutral spatial reserve
    subtle ambient depth
    finite boundary cue

    SemanticProjectPlane
        stage regions
        work units
        connectors
```

The full navigable world carries the grid. The project plane carries methodological/project semantics.

This preserves the user's desired large-workspace feeling without making blank navigation reserve falsely mean "more Framing" or "more Modeling".

---

## 3. Continuous finite grid world

### 3.1 Grid continuity

The previous design applied the grid primarily to the semantic project canvas. The new design moves the grid treatment to the larger scrollable world itself.

Consequently:

```text
pan left/right/up/down
    -> grid continues

zoom out
    -> surrounding reserve is still grid

semantic project plane becomes smaller than viewport
    -> it remains embedded in one continuous spatial workspace
```

The semantic project plane no longer needs a visible rectangular background boundary of its own.

### 3.2 Grid scale follows geometric zoom

The world grid cell size is tied to the current geometric zoom.

This avoids the perceptual mismatch in which work units shrink while the grid remains at a fixed screen-space size. The grid therefore participates in spatial scale while higher-level orientation such as the stage ruler can remain readable in screen space.

### 3.3 Finite rather than falsely infinite

The Cockpit is not currently claiming an infinite canvas.

The world remains finite and bounded. However, reaching the end should not expose a large decorative outer void. A restrained inset edge/fade is sufficient to indicate that the user has reached the current spatial boundary.

The useful principle is:

> **Finite spatial limits should be discoverable without making the operating world visually feel like a card inside another page.**

The exact future world extent remains provisional and may later become dynamic as project-layout requirements mature.

---

## 4. Viewport-aware stage ruler

The fifth review exposed an orientation problem created by the new pan reserve.

If the stage strip remains physically inside the semantic project plane, then panning above that plane can produce:

```text
neutral grid above
stage labels much lower in the viewport
```

If stage labels are instead completely fixed to the browser, horizontal panning can detach them from the stage geometry they are meant to describe.

The resolved behavior is hybrid:

```text
vertical position
    owned by the viewport
    -> stage ruler remains near the top while panning vertically

horizontal position and width
    owned by the semantic project plane
    -> ruler moves left/right with project-stage geometry
    -> labels remain aligned with their actual stage regions
```

This is effectively a viewport-aware semantic ruler.

It provides persistent orientation without stretching stage semantics across neutral navigation space.

### 4.1 Stage width remains semantic

The stage ruler retains the representative stage proportions of the semantic project plane.

Neutral grid space left or right of the project plane does not become an additional stage.

At extreme horizontal pan positions, some stage labels may move partially or fully outside the viewport because the semantic project plane itself has moved. That is correct. A permanently screen-filling stage ruler would falsely imply that all visible neutral grid belongs to named stages.

### 4.2 Screen-space legibility

The ruler is rendered as a viewport overlay rather than being geometrically scaled as ordinary map content.

Its typography therefore remains readable at low geometric zoom while its horizontal geometry still tracks the scaled semantic project plane.

This is a useful early example of the broader semantic-scale principle already required by Specification 007: not every piece of orientation information should shrink identically with analytical content.

---

## 5. Vertical tool rail resolution

The fifth review explicitly questioned whether the foldable project-map control bar was better horizontal or vertical.

For the revised composition, vertical is the stronger candidate.

The reasons are structural rather than cosmetic:

```text
top edge
    now has a meaningful stage-orientation role

right edge
    is better suited to compact spatial-tool controls

vertical rail
    consumes little horizontal canvas area
    avoids competing with the stage ruler
    scales better as bounded spatial controls evolve
    can fold cleanly into the right boundary
```

The implemented rail contains the same capabilities:

```text
Details
zoom out / percentage / zoom in
fit
reset
Jump to / search
System focus
fold / restore
```

Persistent text labels are suppressed in the compact rail, but accessible names, native titles and visual tooltips preserve discoverability and keyboard/screen-reader semantics.

The Jump/search surface opens to the left of the rail so it expands into available workspace rather than beyond the browser edge.

This vertical arrangement remains a candidate pending the next human browser review. It is not yet a frozen product-standard toolbar.

---

## 6. Ambient visual language

The previous review explicitly validated the subtle atmospheric grid treatment.

The fifth iteration therefore extends rather than removes that design language:

```text
continuous low-contrast grid
restrained radial ambient accents
subtle depth
no large blank outer-space region
small finite-boundary cue
```

The exact gradients remain provisional. The durable direction is that the Cockpit can feel spatial and premium without turning into decorative glassmorphism or sacrificing analytical readability.

---

## 7. Bounded implementation

The implementation uses ordinary React, CSS and browser geometry rather than introducing a spatial-canvas framework.

The bounded changes are:

```text
ProjectWorld owns the continuous grid and ambient depth
ProjectCanvas becomes visually transparent while retaining semantic geometry
stage strip removed from the geometrically scaled project plane
viewport stage-ruler overlay added
stage ruler tracks ProjectCanvas horizontal rendered geometry
stage ruler remains vertically pinned during world scrolling
stage regions retain semantic widths
finite-world edge cue retained
horizontal toolbar replaced by right-side vertical tool rail
Jump/search opens leftward from tool rail
old responsive horizontal-toolbar positioning explicitly neutralized
```

Zoom, fit, reset and jump calculations continue to use rendered canvas geometry rather than assuming a fixed unscaled origin.

---

## 8. Validation findings

The implementation was validated through temporary PR #4 before being advanced into `v1-frontend-spike`.

The first CI run exposed a real responsive inheritance defect:

```text
new vertical rail
    + old <=1180px horizontal-toolbar rule
    -> left: 12px remained active
    -> rail moved to left edge at 1024px
    -> left-opening Jump/search popover moved outside viewport
    -> searchable navigation became unusable
```

This was not treated as test noise.

The responsive vertical-rail rule was made authoritative by explicitly restoring:

```text
left: auto
right: 8px
vertical start alignment
visible overflow for popovers/tooltips
```

The corrected gate then passed completely.

Final validation evidence:

```text
GitHub Actions workflow: V1 frontend spike
run number: 130
run id: 32470701290
validated implementation head: dcc265cedb86c7a3917db62667db45cca49cdcd8
pull request: #4

Ubuntu build + unit tests
    PASS

Windows build + unit tests
    PASS

Chromium browser / interaction / accessibility gate
    PASS

controlled direct-project visual regression
    PASS
```

The browser suite includes explicit fifth-review checks for:

```text
continuous world grid at minimum zoom
semantic project plane can sit well below the viewport top while stage ruler remains pinned
stage ruler remains pinned after vertical movement
stage ruler horizontally follows the ProjectCanvas
vertical rail is narrow and genuinely vertically ordered
vertical rail folds and restores
```

The pre-existing browser gates also continue to pass for:

```text
2D movement
searchable Jump to navigation
lower-work recovery above the composer
zoom / fit / reset
pinch-style zoom
fullscreen
HUD folding
Data/EDA focus reuse
browser Back
accessibility
controlled direct-project visual regression
```

---

## 9. What is strengthened by this review

The following directions now have stronger human and executable support:

```text
large finite spatial grid as the Cockpit operating world
navigation reserve distinct from semantic stage meaning
continuous grid rather than a small gridded project box
viewport-aware stage orientation
screen-space orientation can differ from geometrically scaled content
right-side vertical spatial-tool rail
fold-away chrome
restrained ambient visual depth
```

---

## 10. What remains deliberately unselected

This review does not select:

```text
final canvas or graph framework
final world extent algorithm
infinite canvas semantics
final stage taxonomy
final stage widths
final semantic-zoom algorithm
final minimap
final zoom range
final viewport-state persistence
final tool-rail iconography/tooltip system
final Cockpit visual identity
canonical Cockpit screenshot baseline
```

---

## 11. Product implication

The fifth review sharpens an important distinction:

> **The Cockpit's spatial world can be visually continuous without making every visible region semantically equivalent. Navigation space should feel like part of the product while project-stage meaning remains explicit and stable.**

The next human browser review should judge whether this continuous-grid world actually feels larger, calmer and more professional in use, whether the hybrid stage ruler feels natural while panning in every direction, and whether the vertical tool rail is preferable to the previous horizontal control cluster before any of these visual details are frozen.