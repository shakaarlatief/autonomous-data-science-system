# Research 006: Fourth Cockpit Human Review, Balanced Spatial World, and Visual Orientation

**Date:** 2026-08-21  
**Status:** Human product-review evidence and bounded design resolution  
**Scope:** Project Cockpit spatial centering, low-zoom navigation, stage orientation, foldable map controls, project-details placement, brand presentation, and restrained ambient visual language  
**Design session:** 03  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 03 - Project Cockpit & V1 Integration

## 1. Context

The third Cockpit browser-review iteration had already established a substantially stronger operating surface:

```text
2D project navigation
geometric zoom
trackpad pinch zoom
searchable Jump to navigation
floating composer
fold-away primary HUD
compact floating project-map controls
true fullscreen
```

The fourth human review was performed against that implementation in a real desktop browser at multiple zoom levels, including the minimum `45%` geometric zoom.

The review was strongly positive overall. The Cockpit was described as getting progressively better, and the subtle ambient grid treatment was explicitly identified as a professional visual quality worth preserving.

The review nevertheless exposed several concrete product defects and refinements.

---

## 2. Human-review observations

### 2.1 Top-left project identity was visibly malformed

The compact Cockpit brand area visually stacked:

```text
ADS
·
Customer Churn Prediction
```

rather than reading as one intentional compact identity row.

This was not a conceptual product problem. It was a CSS-specificity defect caused by an older grid rule overriding the newer horizontal brand-copy intent.

The correction should preserve compactness rather than add more topbar height.

### 2.2 Stage orientation was semantically useful but visually too quiet

The existing stage names were accepted:

```text
Framing
Data & Exploration
Validation
Modeling
Evaluation
```

The issue was presentation rather than taxonomy. At normal and especially reduced geometric zoom, the stage headings felt too small and insufficiently present relative to the map.

The resulting design requirement is stronger than simply increasing one font size:

> **Project-stage orientation should remain visually legible and structurally present even while the analytical graph is geometrically zoomed out.**

A bounded implementation technique is to compensate stage-header typography and header height against geometric canvas zoom so stage orientation does not disappear as quickly as node detail.

This does not settle the final semantic-zoom architecture.

### 2.3 Low-zoom space must be symmetric and independently pannable

The most important review finding concerned spatial geometry.

At low zoom, empty space appeared outside the project grid mainly on the right/bottom side. The user could see that the project was smaller than the viewport, but could not pan equivalently toward the left/top to recenter it.

The intended behavior is:

```text
project plane becomes smaller than viewport
    -> surrounding space exists on every side
    -> project remains centered inside a larger spatial world
    -> user can still pan left / right / up / down
    -> the project can be repositioned around the visual center
```

This means the scrollable world and the project plane are not the same object.

A fixed canvas with `overflow: auto` is insufficient when geometric zoom makes the canvas itself smaller than the scrollport, because browser scrolling can collapse on an axis once `scrollWidth <= clientWidth` or `scrollHeight <= clientHeight`.

The bounded resolution is therefore:

```text
ScrollableProjectWorld
    always larger than the visible viewport by a minimum scroll range
    contains the ProjectCanvas centered geometrically

ProjectCanvas
    has its own logical dimensions
    scales geometrically
    receives equal surrounding margin inside ProjectWorld
```

A useful implementation constraint is:

```text
world width
    = max(
        scaled project width + 2 * minimum project gutter,
        viewport width + minimum scroll range
      )

world height
    = max(
        scaled project height + 2 * minimum project gutter,
        viewport height + minimum scroll range
      )
```

The project canvas is centered inside that world.

This guarantees that very low zoom does not eliminate the ability to pan merely because the project happens to fit inside the current browser window.

### 2.4 Internal project-grid margins should also feel balanced

The browser review also showed that the logical project content itself carried visibly more grid extent to the right of the represented stages than to the left.

This made the project feel compositionally right-heavy even apart from scroll-container behavior.

The representative fixture should therefore use roughly symmetric logical side margins around the stage zones. This is a fixture/layout property, distinct from the larger pan reserve described above.

The distinction is:

```text
internal project margin
    spacing inside the ProjectCanvas around represented project work

external pan reserve
    space in ProjectWorld around the entire ProjectCanvas
```

Both matter for a professional spatial composition.

### 2.5 Project-map controls should be foldable too

The prior iteration already made the primary Cockpit HUD hideable.

The fourth review identified the same principle for the floating map-control cluster containing:

```text
Details
zoom
fit
reset
Jump to
System focus
```

The control cluster is useful, but should not be permanently mandatory visual chrome.

The bounded interaction is:

```text
expanded map controls
    -> explicit fold-right action

folded map controls
    -> small right-edge restore handle remains
```

This preserves discoverability and keyboard access while allowing the map to become visually quieter.

### 2.6 Expanded Details should occupy the upper available corner more efficiently

The Details surface was already acceptable horizontally, but it sat lower than necessary.

The intended placement is:

```text
high in the upper-left project-map area
below the stage-orientation strip
without covering stage labels
```

This is another example of treating floating surfaces as deliberate occupants of canvas space rather than generic panels with arbitrary offsets.

### 2.7 Restrained ambient grid treatment received explicit positive human validation

The review explicitly praised the subtle visual treatment in the grid, including soft smoothly blended colored circular/ambient accents.

This matters because it provides evidence about the desired Cockpit visual language:

```text
professional
subtle
spatial
calm
slightly atmospheric
not flat or sterile
not decorative for its own sake
```

The useful principle is not "always render colored circles." The stronger product lesson is:

> **Premium analytical software can use restrained ambient depth and micro-detail to make a large operating surface feel intentional and spatial, provided readability, contrast, and evidence remain dominant.**

The existing ambient treatment should therefore be preserved during the current Cockpit exploration unless a later visual review finds a concrete reason to change it.

This does not promote the current exact gradients, colors, or glow positions into a permanent design-system contract.

---

## 3. Bounded implementation resolution

The fourth review iteration implements:

```text
horizontal top-left ADS · project identity
stronger stage-heading hierarchy
stage-heading readability compensation across geometric zoom
balanced internal left/right stage-zone margins
always-pannable ProjectWorld distinct from ProjectCanvas
equal ProjectCanvas margins inside ProjectWorld
minimum scroll range even when the scaled project fits the viewport
zoom anchoring based on actual post-layout canvas geometry
fit and jump positioning based on rendered geometry
fold-right project-map controls
right-edge restore affordance
higher desktop Details placement
existing restrained ambient grid treatment preserved
```

The project canvas remains implemented with ordinary React/CSS/SVG/browser primitives. The review does not yet justify promoting a graph/canvas framework.

---

## 4. Validation findings

The implementation was intentionally validated through a temporary review branch and pull request before being advanced into the active frontend branch.

The first review-4 CI attempt exposed two issues:

```text
brand-row CSS override still active
center-symmetry assertion included native scrollbar chrome
```

The brand issue was a real implementation defect and was fixed with a selector that actually outranked the inherited rule.

The next CI attempt exposed a deeper real defect:

```text
minimum zoom + wide viewport
    -> project world narrower than scrollport
    -> horizontal maximum scroll = 0
```

That result directly falsified the fixed-gutter-only model for the user's requirement.

The final implementation separated the always-pannable world from the centered project plane and made world dimensions depend on both project size and viewport size.

Final validation evidence:

```text
GitHub Actions workflow: V1 frontend spike
run number: 122
run id: 32457992939
validated implementation head: 38c17edfe1440095d60f7e9f9bf21d42053de990

Ubuntu build + unit tests
    PASS

Windows build + unit tests
    PASS

Chromium browser / interaction / accessibility gate
    PASS

controlled direct-project visual regression
    PASS
```

The browser gate now explicitly checks:

```text
pan recovery in all four directions
searchable Jump to navigation
zoom controls and trackpad-style pinch behavior
minimum-zoom world remains pannable
ProjectCanvas is centered with symmetric margins inside ProjectWorld
stage orientation remains visually substantial at minimum zoom
brand identity is horizontally aligned
Details placement is high in the available map area
map controls fold and restore
primary HUD folds and restores
composer collision safety
fullscreen behavior
accessibility
```

---

## 5. What is strengthened by this review

The following design directions now have stronger human and executable support:

```text
Project Cockpit as primary active-work surface
canvas-dominant composition
2D pan + geometric zoom
native trackpad interaction
scalable Jump to/search navigation
collapsible/fold-away chrome
stage-zone orientation
balanced spatial composition
separation of scrollable world from analytical project plane
restrained ambient visual depth as part of premium product quality
```

---

## 6. What remains deliberately unselected

This review does not select:

```text
final graph/canvas library
final auto-layout algorithm
final semantic-zoom algorithm
final stage taxonomy
final minimap implementation
final zoom range
final viewport-state persistence contract
final Cockpit visual identity
exact permanent ambient-gradient treatment
canonical Cockpit screenshot baseline
```

---

## 7. Product implication

The fourth review reinforces a broader pattern in Cockpit development:

> **Spatial usability is not only about making content reachable. The operating surface must also remain visually balanced, recoverable, orienting, and intentionally composed as scale changes.**

The next human review should therefore judge both interaction correctness and the felt quality of the newly balanced spatial world before the project promotes Specification 007 or commits to deeper canvas infrastructure.
