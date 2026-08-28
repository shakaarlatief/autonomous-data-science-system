# Cockpit Provisional Shell and Open Presentation Register

**Status:** Active integration-control register, not a design specification  
**Scope:** Prevents source-faithful holistic reintegration from silently promoting shell scaffolding, fixture geometry, or convenience controls into accepted Cockpit design decisions.

## 1. Why this register exists

The current Cockpit reintegration combines many mechanisms that were reviewed independently. Integration needs enough shell geometry and control placement to exercise them together, but those incidental choices do not automatically inherit design authority.

The governing rule for this stage is:

```text
accepted capability or mechanism
    remains accepted

integration glue needed to compose it
    remains provisional

provisional glue does not become a design decision
    until it receives its own bounded review and preservation event
```

This register is therefore part of the fidelity boundary. It should be consulted before any future holistic screenshot, implementation pass, or human review is interpreted as a complete visual baseline.

## 2. Accepted capability versus provisional presentation

| Area | Already held | Still provisional / explicitly open |
| --- | --- | --- |
| Project world | Project Cockpit as a navigable finite project world; G4/H4 substrate; meaningful WorkUnits | Physical world extent, exact backing dimensions, default viewport occupancy, empty reserve around the grid, edge treatment and final initial framing |
| Navigation | 2D trackpad/scroll movement, bounded geometric zoom, native pinch candidate, drag as an alternate spatial interaction, Fit/Reset/Jump recovery | Final zoom range, final wheel/pinch constants, final gesture technology, whether additional visible pan affordances or minimap are needed |
| Jump/search | Scalable Jump/search capability | Current long top search bar, its width, placement, always-visible state, label treatment, result presentation and relationship to compact/fold-away chrome |
| HUD | Compact/fold-away immersive chrome direction from Specification 008 | Current single long top HUD, exact height, grouping, order, labels, button sizes and whether controls are persistent or folded away |
| WorkUnits | Canonical 176 x 92 compact project-scene geometry, H4, markers, P7, status, A3, SEL2 and accepted X5 | Fixture node positions, project-layout algorithm and final information density at different zoom levels |
| WorkUnit appearance | Foundation 023 semantic/presentation separation; Normal/Subtle category shape; None/Material/Lumen micro design; reduced-motion safety | Final settings UI, where settings live, profile naming, persistence/synchronization and any additional theme/density dimensions |
| Connectors | E5 relation-class presentation; system-owned directionality; approved configurable connector presentation mechanisms | Exact holistic settings adapter for Clean/Micro dots/Frame sockets/direction-safe presentation, hover disclosure configuration and final settings placement |
| Relations | E5 carrier and directionality grammar | Current DEP/EVID/LINE/CAUSE fixture labels and the four current fixture links are integration examples, not the final relation ontology |
| Context expansion | X5 balanced two-axis expansion without context recession | Final contextual-detail content schema beyond the currently held working defaults |
| Deep focus | Z7 Pull-Back Then Dive entry, full-stage specialist ownership and compact topology compass | Reverse/return choreography, final specialist internal composition, final workspace command surfaces and exact deep-focus chrome |
| Conversation | Quiet Graphite baseline, project/work-unit scope distinction, Boxes/Text rail choice, A6, Grid + Deep Dive access, co-present/full-focus modes and state preservation | Current compact composer geometry, placement and iconography; final Conversation Workspace integration shell and settings placement |
| Fullscreen | True browser fullscreen with graceful fallback | Final fullscreen button placement and visual treatment |
| Status overlays | Need for orientation/recovery information | Current bottom-left Project Grid box, top-right Geometric Zoom box and bottom-right Integration Glue diagnostic box are design-lab scaffolding, not accepted product chrome |

## 3. Current world-size and framing warning

The reintegration browser currently uses a fixed `1440 x 760` world backing because that is the controlled source-fixture geometry used to compose the accepted WorkUnit implementations.

That number is **not** a final Cockpit world-size decision.

Likewise, the current Fit calculation, minimum/maximum zoom values, node fixture coordinates and the amount of dark space visible around the world are not promoted visual decisions. The project has already preserved that final finite-world extent, stage widths, minimap, semantic zoom/grouping and related scale questions remain open.

A future bounded review must therefore ask separately:

```text
How much of the project world should normally occupy the viewport?
How much spatial reserve should surround active work?
How should finite-world edges read?
Should the world grow from content, from stages, or from another layout authority?
What should the initial camera position and scale be?
What happens as the project becomes much larger?
```

These questions must not be answered accidentally by keeping the current fixture dimensions.

## 4. Input contract now required during integration

The promoted interaction architecture and current human correction establish this integrated input contract:

```text
ordinary laptop two-finger scrolling
    -> 2D spatial movement / panning

native trackpad pinch or spread
    -> geometric zoom around the gesture anchor

pointer drag on open world
    -> alternate panning mechanism

Fit / Reset / Jump
    -> explicit recovery paths
```

A generic wheel event must not be interpreted as zoom. Chromium trackpad pinch is exposed as a `ctrlKey` wheel stream and should use the already promoted frame-coalesced pinch treatment.

This is an integration correction, not a new visual-design selection.

## 5. Sharpness and fractional zoom

The reintegration must not keep the project plane permanently promoted as one composited transform texture. Persistent transform compositing can leave text, one-pixel grid lines and small carriers visibly soft after a gesture settles.

Current integration policy:

```text
while actively navigating
    allow transform compositing for responsiveness

after navigation settles
    release the persistent will-change hint
    align rendered translation to the device-pixel grid
    allow Chromium to rerasterize the current view
```

This is a rendering-quality mitigation, not a final semantic-zoom solution. At very small geometric scales, fewer physical pixels are available by definition. Final semantic zoom / level-of-detail behavior remains intentionally open.

## 6. Cross-mechanism validation requirement

A mechanism is not considered safely integrated merely because its original isolated browser experiment passed.

The holistic gate must exercise sequences that combine mechanisms, including at minimum:

```text
pan -> pinch -> select -> Jump -> X5 expand
appearance switch -> relation geometry -> semantic invariants
X5 expanded -> Z7 enter -> specialist full stage -> return
return -> preserved selected/expanded project state
hover/selection/status/attention while relation geometry is live
reduced motion across X5/Z7/world animation
provisional settings overlay without stealing world navigation input
missing CSS/JS dependency detection
```

The gate should fail on dead controls, missing assets, semantic mutation caused by appearance settings, or one mechanism intercepting input intended for another.

## 7. User-adjustable capabilities inventory

The following adjustable capabilities must remain visible in the reintegration plan even when their final settings UI is not yet mounted:

### Currently safe to exercise in the integrated Grid

```text
WorkUnit shape
    Normal
    Subtle category-specific silhouette

WorkUnit micro design
    None
    Material
    Lumen

Reduced motion
    On / Off
```

These may alter approved presentation only. They must not alter scientific category markers, relation meaning/directionality, operational status, disposition, selection, attention, or runtime semantics.

### Accepted capability awaiting exact-source holistic adapter

```text
Connector presentation
    Clean
    Micro dots
    Frame sockets
    direction-safe semantic treatment
    hover/reveal behavior as an orthogonal presentation mechanism
```

This capability is not to be forgotten, but it should not be approximated by inventing a new mixed-terminal implementation during reintegration.

### Accepted capability that mounts with Conversation Workspace

```text
Conversation rail
    Boxes
    Text
```

This should arrive with the exact Quiet Graphite / A6 Conversation Workspace family so the choice is tested in its correct context.

## 8. Design-lab-only elements currently visible

The following current elements are diagnostic/integration scaffolding unless separately promoted later:

- the `Checkpoint 251 · source-faithful reintegration` subtitle;
- the `Integration Glue` diagnostic card;
- the gesture-explanation chip;
- the provisional appearance panel itself;
- placeholder specialist panels;
- fixture project name/content where used only to exercise interactions.

They must not migrate into production `/cockpit` merely because they exist in the integration browser.

## 9. Promotion rule

Before any provisional item in this register becomes part of the Cockpit design:

```text
isolate the bounded question
-> compare/refine if useful
-> obtain human evidence
-> preserve the decision
-> bind exact accepted implementation evidence
-> only then remove the item from this provisional register
```

Until that happens, the source-faithful integrated browser is a **composition and interaction-validation surface**, not a blanket approval of every pixel visible on screen.
