# Research 005: Cockpit Canvas Dominance, Zoom, and Scalable Project Navigation

**Date:** 2026-08-21  
**Status:** Active design evidence from third real-browser Cockpit review  
**Scope:** Human review of the Checkpoint 121 immersive-scale Cockpit slice, with refined requirements for project-space zoom, scalable jump/search navigation, canvas-dominant chrome, floating composer treatment, and explicit HUD collapse  
**Design session:** 03  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 03 - Project Cockpit & V1 Integration

## 1. Review context

Checkpoint 121 established that the Specification 007 v0.2 immersive-scale implementation could provide:

```text
a project larger than one viewport
horizontal and vertical project-space navigation
smooth jump-to-location behavior
compact project details
collision-safe system context
keyboard recovery
true browser fullscreen
```

The implementation then entered the required real-browser human product gate.

The third review did not reject the Cockpit direction. Instead, it exposed a more precise product-quality issue: once basic two-dimensional reachability worked, the remaining application chrome became visibly too dominant relative to the project operating surface.

The review therefore shifts the next refinement from "make the map reachable" toward:

```text
make the project canvas the dominant visual object
while retaining strong orientation, navigation, system interaction, and accessibility
```

---

## 2. Smooth project jumps are accepted, but the interaction must scale

The existing direct jump controls were positively reviewed. Their smooth spatial movement makes the project feel coherent rather than page-like.

However, adding one dedicated toolbar button for every future target category would not scale to a large long-running project.

The stronger navigation model is:

```text
Jump to
    quick semantic destinations
        Active work
        Blocker
        Investigation
        Evaluation
        ...

    project search
        search meaningful project work by title/type
        select result
        spatially move to it
```

The representative project should include `Investigation` as a quick semantic destination because `Production missingness` is an active Investigation.

This is a general product principle for the Cockpit:

```text
when the scalable interaction is already clear,
do not deliberately implement a temporary control pattern that is known to become wrong at realistic project scale
```

This does not justify premature backend ontology or navigation-service complexity. It means the visible interaction should avoid obvious dead-end proliferation where a bounded generic mechanism is already available.

---

## 3. Geometric zoom is now required

Two-dimensional panning alone is insufficient for a professional project-space experience.

The user must be able to zoom out to understand more of the project at once and zoom in to inspect a local branch more closely.

Required geometric interaction:

```text
explicit zoom out
current zoom indication
explicit zoom in
reset to 100%
fit project
```

The zoom operation should preserve the user's approximate visual anchor rather than unexpectedly jumping back to the project origin.

A bounded range is preferable to unconstrained scaling. The spike may use an implementation-oriented range such as approximately 45%-160%, but the exact final range remains a product-tuning detail rather than a durable domain decision.

Geometric zoom is not a substitute for future semantic zoom. They solve different problems:

```text
geometric zoom
    changes visual scale and visible spatial extent

semantic zoom
    changes information density / grouping at different scales
```

The current slice should implement geometric zoom while preserving compatibility with future semantic zoom rather than attempting to solve both at once.

---

## 4. Laptop trackpad behavior is part of the zoom requirement

Button-only zoom is insufficient for the intended desktop/laptop product.

The Cockpit should support the interaction users naturally expect from a spatial surface:

```text
two-finger trackpad movement
    pan through project space

trackpad pinch gesture
    zoom in / out around the gesture location
```

On current Chromium-class browsers, trackpad pinch is commonly surfaced to web content as a wheel event with modifier semantics. The implementation may use browser primitives directly during the spike rather than selecting a spatial-canvas dependency only for gesture handling.

The architectural requirement is interaction-level, not event-API-level:

```text
trackpad pan + pinch must feel native enough for human review
```

Keyboard-accessible equivalents remain required.

---

## 5. The composer should float over a continuous Cockpit canvas

The Checkpoint 121 version protected lower content by reserving a substantial full-width area below the map for the composer.

That solved collision safety, but the third review identified a visual cost: the Cockpit appeared vertically compressed because the entire strip around the composer stopped reading as project space.

The stronger model is:

```text
project viewport continues to the bottom edge

system composer
    floats above the project surface
    uses a restrained translucent material
    does not create a full-width opaque footer band

project-space navigation
    retains enough lower/right overscroll or logical margin
    to bring any work object fully clear of the composer
```

Therefore:

```text
visual canvas continuity
    +
interaction-safe recovery margin
```

is preferred over permanently reserving a non-canvas footer region.

This reconciles immersion with CPK-20 collision safety rather than trading one for the other.

---

## 6. The top of the Cockpit should not contain two persistent full-width layers

The reviewed implementation had two application-level bands before the project stage strip:

```text
ADS / project / execution status / fullscreen / project views

Project operating map / project name / details / reset / jumps / system focus
```

This duplicated project identity and consumed vertical space with large empty intervals between left- and right-aligned controls.

The stronger hierarchy is:

```text
one genuinely compact persistent Cockpit HUD
    ADS + project identity
    high-value execution state
    fullscreen / project-view escape
    explicit collapse control

project stage strip
    directly attached to the operating surface

small floating project-map toolbar
    details
    zoom
    fit/reset
    scalable jump/search
    system focus
```

The dedicated full-width `Project operating map` control row should not survive merely because it already exists.

---

## 7. The primary Cockpit HUD should be explicitly foldable

The third review reiterated an earlier product idea: the remaining top HUD should itself be able to get out of the way when the user wants maximum project space.

Preferred states:

### Compact HUD

```text
ADS · Project name | execution state | fullscreen | project views | collapse
```

### Hidden HUD

```text
project canvas begins at the top of the application
small restore handle remains available
```

Optional pointer-proximity reveal may be explored later as a convenience, but it must never be the only route to hidden controls.

The explicit click/keyboard control is authoritative because the Cockpit must remain usable with keyboard and non-hover input.

---

## 8. Transparency should preserve hierarchy, not become decorative glassmorphism

The review suggested making some chrome visually permeable so unused space still reads as Cockpit.

The accepted interpretation is not "make every bar transparent."

Preferred material treatment:

```text
continuous dark technical canvas

small floating surfaces
    restrained translucency
    subtle blur where useful
    thin border
    restrained shadow
    strong text contrast
```

Avoid:

```text
full-width opaque bands without functional need
excessive glass effects
blur as decoration
weak contrast
layers whose empty middle areas visually remove canvas space
```

The project operating surface should remain perceptually primary.

---

## 9. Implementation response tested in this slice

The bounded third-review implementation uses existing browser/React/CSS/SVG primitives and adds:

```text
2260 x 1180 representative logical project plane

geometric zoom
    explicit - / percentage / + controls
    reset to 100%
    fit-project command
    + / - / 0 / F keyboard equivalents
    trackpad pinch handling around gesture anchor

project movement
    native two-axis scrolling / trackpad movement
    Arrow navigation
    Shift + Arrow larger movement
    Home reset

scalable Jump to interaction
    Active work
    Blocker
    Investigation
    Evaluation
    searchable project-work list

canvas-dominant chrome
    no separate full-width Project operating map row
    floating project-map toolbar
    floating details surface
    floating system-focus surface
    composer over continuous canvas

primary HUD
    reduced height
    explicit hide action
    small explicit restore handle
```

The implementation remains deliberately independent of React Flow or another graph/canvas framework.

---

## 10. Validation evidence

The third-review refinement was validated through a pull-request gate before being fast-forwarded into `v1-frontend-spike`.

Final validated head:

```text
e500eb45c1de59f24b1531b890f55d2ec3bfffc5
```

Final PR validation result:

```text
Ubuntu build + unit tests
    PASS

Windows build + unit tests
    PASS

Chromium interaction + accessibility
    PASS

controlled direct-project visual regression
    PASS
```

The browser gate explicitly exercised:

```text
searchable Jump to navigation
Investigation quick jump
keyboard 2D recovery
zoom buttons
keyboard zoom
fit project
trackpad-style pinch event handling
HUD hide/show
canvas continuation behind the composer
lower-work recovery above the composer
fullscreen
core automated accessibility
```

An earlier browser assertion failed because it measured the target immediately after initiating the deliberately smooth spatial jump. The product jump itself is asynchronous by design. The gate was corrected to wait for the smooth navigation to complete before measuring unobstructed placement. The product also retains explicit zoom-aware target centering rather than relying on browser `scrollIntoView` behavior inside a scaled spatial surface.

---

## 11. What this review does not settle

This review does not select:

```text
final semantic-zoom behavior
final zoom range
minimap
canvas/graph library
project auto-layout algorithm
final stage taxonomy
final project-search backend
final URL/session persistence for pan/zoom
hover/proximity HUD reveal
final visual identity
final Cockpit screenshot baseline
```

The next human gate should evaluate the revised experience directly in a real browser before any of those are promoted.

---

## 12. Current product hypothesis after the third review

The strongest current Cockpit hierarchy is now:

```text
OPTIONAL TRUE BROWSER FULLSCREEN
        |
        v
COMPACT / FOLDABLE COCKPIT HUD
        |
        v
STAGE STRIP ATTACHED TO PROJECT SPACE
        |
        v
CONTINUOUS TWO-DIMENSIONAL PROJECT CANVAS
    pan
    pinch zoom
    explicit zoom
    fit/reset
    jump/search
    click work -> focus workspace
        |
        +--> FLOATING PROJECT CONTROL SURFACE
        +--> FLOATING SYSTEM CONTEXT
        +--> FLOATING NATIVE SYSTEM COMPOSER

all floating surfaces
    must preserve recoverability of project work
```

This remains a candidate product architecture pending the next real-browser human review.
