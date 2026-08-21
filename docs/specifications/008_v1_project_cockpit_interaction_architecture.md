# Specification 008: V1 Project Cockpit Interaction Architecture

**Date:** 2026-08-21  
**Status:** Promoted V1 interaction architecture  
**Scope:** Accepted bounded interaction architecture for the Project Cockpit after Specification 007 and seven real-browser human review cycles; governs the primary active-work model, spatial focus, scalable navigation, viewport/world semantics, collision safety, immersive chrome, fullscreen, accessibility, and specialist-workspace reuse without freezing the final visual system or final spatial implementation technology  
**Promoted from:** `docs/specifications/007_v1_unified_project_cockpit_interaction_spike.md`  
**Primary evidence:** Research 002 through Research 009 and Checkpoints 117 through 126  
**Design session:** 03  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 03 - Project Cockpit & V1 Integration

## 1. Purpose

This specification records the interaction architecture that has now earned promotion through executable implementation, repeated automated validation, and seven real-browser human product reviews.

It closes the bounded architectural question:

```text
Can ADS use one professional immersive Project Cockpit
as the primary active-work environment while still supporting
large-project navigation, deep analytical work, project context,
and strong accessibility/performance boundaries?
```

The answer for V1 is yes.

This specification does **not** freeze the final Cockpit visual identity, graph/canvas implementation, gesture library, auto-layout, semantic zoom, minimap, stage taxonomy, final route contract, or exact gesture tuning.

## 2. Promoted product model

The primary active-work product model is:

```text
Project Cockpit
    primary immersive active-work environment
    living project-process projection
    native system interaction
    spatial navigation
    focused analytical work

Direct specialist project views
    alternative entry / inspection / record surfaces
    reuse the same substantive modules and project state
```

The Cockpit is a **derived projection over project state**. It must not collapse every project object, methodological relation, artifact lineage, event, or agent into one universal graph.

## 3. Meaningful visible units

Cockpit work units represent user-relevant project work rather than storage primitives or runtime actors.

Examples include:

```text
objective / framing
data understanding
exploration / EDA
investigation
question / blocker
validation design
baseline model
alternative model work
evaluation
approval-relevant work
```

The exact stage taxonomy and final work-unit taxonomy remain evolvable.

## 4. Spatial focus and deep work

Selecting a supported work unit should create the experience:

```text
project map
    -> select meaningful work unit
    -> map recedes / focus transition
    -> full-resolution specialist workspace mounts
    -> perform real analytical work
    -> return to project context
```

The implementation must not depend on permanently nesting a full analytical workspace inside every map node.

At minimum, the architecture has already proven reuse of Data and EDA specialist functionality inside both direct routes and Cockpit focus, plus a dedicated Production Missingness investigation focus.

## 5. Reachability is not simultaneous mounting

The durable performance boundary is:

```text
everything reachable from the Cockpit
    !=
everything mounted or loaded simultaneously
```

Future projects may contain many work units and large analytical artifacts. The Cockpit must therefore preserve selective mounting, backend-driven loading where appropriate, and bounded visible detail.

## 6. Finite navigable world and semantic project plane

The V1 spatial model distinguishes:

```text
FiniteNavigableGridWorld
    navigation / spatial substrate
    continuous grid through surrounding reserve
    symmetric pan/recovery capacity
    world-level ambient depth
    subtle finite-boundary cue

SemanticProjectPlane
    project-stage semantics
    meaningful work units
    connectors
    semantic stage regions
```

Neutral navigation reserve is not automatically project-semantic space.

The semantic project plane may fit inside a viewport at low zoom while the world must still preserve meaningful horizontal and vertical movement and recovery.

The current representative implementation uses a finite world. Promotion does not claim infinite-canvas semantics.

## 7. Two-dimensional project navigation

Large projects must remain navigable when work extends horizontally and vertically beyond one screen.

The promoted architecture requires equivalent capabilities for:

```text
horizontal movement
vertical movement
keyboard movement/recovery
fit project
reset/recenter
jump to meaningful work
search project work
```

The current browser implementation uses native scrolling/trackpad movement and keyboard equivalents. A later canvas library may replace the mechanics if measured scale or interaction requirements justify it, but these user-level capabilities remain required.

## 8. Geometric zoom and native laptop interaction

Bounded geometric zoom is part of the promoted V1 interaction architecture.

Required interaction paths include:

```text
zoom out
current zoom indication
zoom in
reset to 100%
fit project
keyboard zoom/recovery equivalents
native laptop pinch candidate
```

Native pinch should remain temporally stable enough to preserve spatial orientation. The validated browser-input pattern currently includes:

```text
delta-unit normalization
animation-frame coalescing
pathological per-frame delta bounding
immediately current zoom state
bounded exponential scale progression
approximate gesture-anchor preservation
obsolete correction cancellation
```

Exact sensitivity and normalization constants are implementation tuning, not promoted architecture.

A very small occasional pinch hitch remains known deferred polish after the seventh human review.

## 9. Viewport-aware stage orientation

Stage orientation is a navigation aid and must remain usable across zoom and pan.

The promoted model separates:

```text
vertical ruler placement
    viewport-owned / near visible top

horizontal ruler geometry
    project-semantic
    follows rendered stage boundaries
```

The terminal ruler boundaries should align to authoritative rendered semantic boundaries, currently Framing on the left and Evaluation on the right in the representative fixture.

When browser layout/zoom changes those boundaries, synchronization should occur only after the relevant geometry has settled sufficiently to preserve alignment.

The exact stage names, widths, typography, and final visual ruler treatment remain provisional.

## 10. Scalable project location

Project navigation must not scale by adding a permanent toolbar button for every future work category.

The promoted architecture includes a bounded project-location surface combining:

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
    spatially relocate to result
```

Search/jump results must remain usable at laptop viewport sizes and must not be obscured by persistent floating chrome.

The production project-search backend remains unselected.

## 11. Immersive and fold-away chrome

The Cockpit should use essentially the practical application viewport as its operating surface.

Persistent chrome must remain compact and should be explicitly hideable where useful.

The promoted interaction model includes:

```text
compact primary Cockpit HUD
    explicit hide
    explicit restore

project-map controls
    compact bounded surface
    explicit fold
    explicit restore

project details
    available without permanently consuming large vertical space

system focus/context
    available as bounded contextual surface

system composer
    native to Cockpit
    visually integrated
    not a permanently dominant generic chat column
```

The current right-edge vertical map-tool rail has strong positive evidence but its permanent styling/iconography is not frozen.

## 12. Collision-safe floating surfaces

Floating surfaces must never make project work permanently inaccessible.

This includes at least:

```text
system composer
project details
system-focus/context surfaces
Jump/search
approval surfaces
future minimap or related navigation UI
```

The viewport must preserve safe recovery/panning and the surfaces themselves should remain collapsible, bounded, or internally scrollable as needed.

The validated Jump/search behavior treats the persistent composer as an explicit safe-area occupant and keeps lower results reachable at 1024x768.

## 13. True browser fullscreen

The Cockpit supports explicit true fullscreen using the standards-based browser Fullscreen API where available.

Required behavior:

```text
explicit user action
    -> enter fullscreen when supported

fullscreenchange
    -> synchronize visible UI state

Escape / explicit control
    -> leave fullscreen

unsupported / denied
    -> remain in normal immersive Cockpit without product failure
```

Fullscreen must never be assumed available or entered automatically on page load.

## 14. URL-addressable focus state

Important Cockpit focus/deep-work state should remain reconstructable through route/search state so refresh and browser Back/Forward behave like application navigation rather than document reloads.

The current spike has proven a candidate contract around:

```text
/cockpit
focus=map|data|eda|missingness
column=<data variable>
filter=<data filter>
view=distribution|trend
```

The exact final public URL contract remains provisional.

Pan/zoom/HUD/control-fold state is not promoted as project/domain state. Whether some of it belongs in URL or browser-session UI state remains open.

## 15. Accessibility and reduced motion

Core Cockpit interaction must remain keyboard reachable and semantically understandable.

At minimum this applies to:

```text
map work units
focus entry/exit
viewport movement/recovery
zoom and fit/reset
Jump/search
HUD and map-control hide/restore
fullscreen
composer interaction
```

Reduced-motion preferences must preserve understandable focus transitions without relying on motion as the sole carrier of meaning.

Automated accessibility checks remain part of the frontend quality gate but do not replace human product review.

## 16. Responsive desktop/laptop boundary

The current V1 target is a professional desktop/laptop operating environment.

The architecture must remain usable at representative 1440, 1280, and 1024 pixel widths and at laptop-height boundaries such as 1024x768.

Phone UI is outside the scope of this promoted architecture.

## 17. Ambient spatial depth

Human review positively supports a restrained spatial treatment of the Cockpit world:

```text
calm
subtle
professional
spatial
analytical content remains dominant
```

Workspace-level atmosphere belongs to the navigable world rather than a smaller semantic project plane so ambient effects do not reveal accidental implementation boxes.

Exact gradient coordinates, colors, shapes, and opacity values are not frozen.

## 18. Technology boundary

Promotion does not select a graph/canvas or gesture framework.

The current implementation proves the architecture using ordinary:

```text
React
CSS
SVG
DOM geometry
browser scrolling
native wheel/pinch input
View Transition API where available
Fullscreen API
```

A specialized dependency should be introduced only when measured project scale, interaction, layout, virtualization, accessibility, or maintainability requirements justify it.

## 19. Validation evidence

Specification 007 evolved through seven human review cycles and repeated cross-platform/browser gates.

The final promotion-validation implementation head is:

```text
2c3b522e2416d73c015ce5ec2a4560a227524dd9
```

Final workflow:

```text
V1 frontend spike
run number: 155
run id: 32492536072
```

Final results:

```text
Ubuntu build + unit tests
    PASS

Windows build + unit tests
    PASS

Chromium browser interaction + accessibility
    PASS

controlled direct-project visual regression
    PASS
```

The first seventh-review browser gate is also retained as useful diagnostic evidence. It exposed a reproducible stage-ruler timing defect under rapid zoom, which was fixed by delaying ruler measurement until the rendered semantic geometry had settled through an additional animation frame.

## 20. Promotion boundary

The following are promoted for V1:

```text
Project Cockpit as primary immersive active-work model
living project-process projection
meaningful work-unit semantics
spatial focus into real reusable specialist workspaces
reachability != simultaneous mounting
finite navigable world distinct from semantic project plane
2D project navigation and recovery
bounded geometric zoom and native pinch capability
viewport-aware semantic stage orientation
scalable Jump/search project location
compact/fold-away immersive chrome
collision-safe floating surfaces
true fullscreen with graceful fallback
URL-addressable focus/deep-work state
keyboard accessibility and reduced-motion support
world-owned restrained ambient depth
```

The following remain deliberately unfrozen:

```text
remaining tiny occasional pinch hitch
final native-pinch constants
final geometric zoom range
final graph/canvas library
final gesture library
final project auto-layout algorithm
final semantic-zoom/grouping algorithm
final minimap
infinite-canvas semantics
final finite-world extent algorithm
final pan-reserve dimensions
production project-search backend
final stage taxonomy
final stage widths
final stage-ruler material/treatment
permanent vertical tool-rail visual design
final Cockpit visual identity
final public URL contract
pan/zoom/HUD persistence contract
canonical Cockpit screenshot baseline
mobile-phone UI
```

## 21. Relationship to future work

Future Cockpit iterations should treat this specification as the current V1 interaction baseline.

They may revise it when new evidence shows a better architecture, but they should not reopen already validated questions merely because visual/product polish continues.

The next immediate V1 work is outside this Cockpit spike:

```text
1. close the governed PostgreSQL reusable-knowledge round-trip gate
2. execute the Specification 005 runtime bakeoff with one principal reasoner first
3. build and evaluate production retrieval / MethodologicalHorizon construction
```

Cockpit polish and deeper product capability can proceed later on top of this promoted interaction architecture.