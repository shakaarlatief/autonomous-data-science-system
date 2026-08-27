# Research 054: Connector Composition, Directionality and Endpoint-Layering Refinement

**Date:** 2026-08-27  
**Status:** Active Phase-C product-design evidence  
**Scope:** Preserves the next human review of the connector/Port Grammar slice, fixes endpoint-layering, hover-lift attachment and dot-overlap defects, restores the earlier frame-socket treatment, refines K2 socket highlight behavior, and records a preliminary shift from winner-take-all connector selection toward a compositional connector grammar.  
**Authority:** Research/design evidence only. No final connector semantic vocabulary is promoted.

## 1. Human visual defect reports

After the first endpoint-overlay correction, the project owner visually verified the browser and found that K4 hover-port dots still appeared to sit underneath the box surface rather than clearly above the rendered perimeter.

That stacking defect was corrected, but the next browser review exposed a second issue: when a work-unit node enters its accepted H4 hover state, the node lifts upward by 2 px while the connector geometry remained at its pre-hover coordinates. The endpoint marker therefore again appeared to slip underneath the lifted box even though its z-layer was correct.

After that motion defect was fixed, the project owner identified a third refinement: the micro-dot / hover-port circles were still centered directly on the work-unit edge, so roughly half of each circle intruded into the card. On the left side this visibly painted over the category color rail.

The intended hierarchy remains:

```text
world / grid
    -> connector curve below node
    -> work-unit body
    -> micro-dot / hover-port / directional endpoint above node perimeter
```

And the intended geometry invariants are now explicit:

```text
connector endpoint position
    follows the rendered node perimeter continuously
    including temporary hover-lift transforms

micro-dot / hover-port marker
    belongs visually to the connector
    sits mostly outside the work-unit surface
    retains only a very small overlap with the perimeter
```

## 2. Endpoint-layer correction

The dedicated `connector-port-overlay` is explicitly positioned and assigned a stacking level above work-unit nodes.

K4 hover-port styling is explicitly mapped to the overlay relation group because the original K4 CSS selector targeted only the under-node `.connector-link` groups.

Therefore:

```text
K1 Micro Dots
    endpoint markers above node perimeter

K3 Target Cue
    destination cue above node perimeter

K4 Hover Ports
    endpoint markers above node perimeter on related-node hover

connector curves
    remain under nodes
```

## 3. Hover-lift geometry synchronization

The accepted H4 work-unit hover treatment includes:

```text
node transform
    translate3d(0, -2px, 0)
```

Because CSS transforms do not trigger the existing scene `ResizeObserver`, the relation geometry engine previously did not follow that temporary motion.

The connector browser now runs a short requestAnimationFrame geometry synchronization window during both hover entry and hover release:

```text
pointer enter
    follow rendered node geometry through fast 180 ms lift

pointer leave
    follow rendered node geometry through slower ~320 ms release
```

`getBoundingClientRect()` remains the geometry authority, so both the under-node curve endpoint and the above-node dot / hover-port / target cue track the moving rendered perimeter rather than a nominal static position.

Reduced-motion mode performs a single geometry refresh instead of running the short animation-frame synchronization loop.

This is intentional behavior:

```text
node may lift
connector remains physically attached to the lifted node
endpoint marker remains aligned with the visible perimeter
```

Exact hover-lift attachment fix:

```text
ae2951e2325e6e6e624131097dcc1edc732e1844
```

## 4. Micro-dot / hover-port outward offset

Human review then showed that a center-on-edge circle still looked too embedded in the work-unit body, especially where a left-side dot overlapped the category color rail.

The curve anchor remains unchanged at the exact rendered edge. Only the circular terminal marker receives a small outward offset along the attachment side.

Current rule:

```text
curve endpoint
    exact rendered edge

K1 Micro Dot / K4 Hover Port center
    2 SVG user units outward from the edge anchor

result
    dot sits mostly outside the card
    only a small fraction overlaps the border
    left-side dots no longer sit over the category color rail
```

The side-aware offset is:

```text
left      x - 2
right     x + 2
top       y - 2
bottom    y + 2
```

K2 Frame Sockets are not changed by this refinement. K3 directional cues are also left on their existing target-edge treatment pending the later directionality/composition experiment.

Exact outward-dot refinement:

```text
42ec63d17095753dc4ab97628cd859473cbdf5e8
```

## 5. Frame sockets restored and color-synchronized

The project owner explicitly said the frame sockets were good before the endpoint-overlay change and asked to restore them.

Therefore K2 is intentionally different from the dot/hover-port treatment:

```text
K2 Frame Sockets
    remain in the original under-node relation layer
    visually dock into the frame edge
    are not cloned into the above-node endpoint overlay
```

This preserves their more structural, instrument-like character.

The next human review identified one remaining coherence issue: when a relation becomes highlighted, the curve changes to the hovered work-unit color while the K2 socket outline remained grey.

That is now corrected:

```text
K2 rest state
    dark socket interior
    neutral grey socket outline

K2 highlighted relation
    dark socket interior retained
    socket outline adopts --related-rgb
    restrained same-color socket glow
```

The socket therefore stays structural rather than becoming a bright filled marker, while its active relation state now visually matches the connector line.

Exact K2 relation-color refinement:

```text
183264bdd07783eaa2354894592f2cf4a076b6ec
```

## 6. Implementation sequence

```text
b8953973dda9b57bfa2071726ec0aadac0f7c028
    explicit above-node overlay stacking

ff24fbf09fd771e1bdfc574578fa4e2ffdb89d7c
    stop mirroring K2 sockets into overlay

4e597d35b79d807b8481dd6610f0eff261089ca5
    explicit K4 overlay hover-port reveal

ed27290d6f060f13a86d863a2faa7eede3c91a7e
    browser descriptions synchronized with restored socket treatment

ae2951e2325e6e6e624131097dcc1edc732e1844
    relation geometry follows node hover-lift and release motion

42ec63d17095753dc4ab97628cd859473cbdf5e8
    circular terminals moved mostly outside the work-unit perimeter

183264bdd07783eaa2354894592f2cf4a076b6ec
    K2 socket outline follows highlighted relation color
```

Current exact browser implementation target:

```text
183264bdd07783eaa2354894592f2cf4a076b6ec
```

## 7. Preliminary connector-composition insight

The project owner supplied an important conceptual observation, but explicitly asked to fix the current visual mistakes before making the final connector choice.

Preliminary evidence:

```text
connector design should probably be compositional
not one universal K0-K4 winner
```

Reasoning supplied by the project owner:

```text
direction is functional and important
some relations may point one way
some may point the opposite way
some may be bidirectional
some may have no direction
```

Possible future relation meanings mentioned include:

```text
chronological
causal
other semantic relation classes
```

These meanings are examples only. Their final vocabulary is not yet frozen.

The project owner also stated:

```text
Hover Ports should remain available as an option.
For non-directional relation presentation, one of Micro Dots or Frame Sockets
will probably be sufficient initially.
A later user-configurable choice between multiple non-directional endpoint styles
may remain possible.
```

Final preference between dots and sockets is deliberately pending further human review.

## 8. Emerging architecture hypothesis

The connector system may need to separate orthogonal dimensions such as:

```text
RELATION SEMANTICS
    what the relationship means

DIRECTIONALITY
    none
    A -> B
    B -> A
    bidirectional

BASE CONNECTOR PRESENTATION
    curve + optional non-directional attachment treatment

PROGRESSIVE DISCLOSURE
    hover ports / relation emphasis
```

This is a hypothesis to test next, not a promoted contract.

It is consistent with the earlier Cockpit principle that presentation mechanisms should not be mistaken for semantic meaning.

## 9. Current gate

The project owner asked to resolve the visual corrections before giving the fuller connector decision.

Therefore the active gate is:

```text
human verifies K1/K4 dots now touch the work-unit perimeter from mostly outside
human verifies they remain attached during hover lift/release
human verifies K2 retains the preferred structural frame-socket treatment
human verifies K2 socket outline follows the highlighted connector color
-> human gives connector-composition preference
-> only then implement the next combined-directionality experiment
```

No production `/cockpit` files changed.
