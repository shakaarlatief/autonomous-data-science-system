# Research 054: Connector Composition, Directionality and Endpoint-Layering Refinement

**Date:** 2026-08-27  
**Status:** Active Phase-C product-design evidence  
**Scope:** Preserves the next human review of the connector/Port Grammar slice, fixes endpoint-layering and hover-lift attachment defects, restores the earlier frame-socket treatment, and records a preliminary shift from winner-take-all connector selection toward a compositional connector grammar.  
**Authority:** Research/design evidence only. No final connector semantic vocabulary is promoted.

## 1. Human visual defect reports

After the first endpoint-overlay correction, the project owner visually verified the browser and found that K4 hover-port dots still appeared to sit underneath the box surface rather than clearly above the rendered perimeter.

That stacking defect was corrected, but the next browser review exposed a second issue: when a work-unit node enters its accepted H4 hover state, the node lifts upward by 2 px while the connector geometry remained at its pre-hover coordinates. The endpoint marker therefore again appeared to slip underneath the lifted box even though its z-layer was correct.

The intended hierarchy remains:

```text
world / grid
    -> connector curve below node
    -> work-unit body
    -> micro-dot / hover-port / directional endpoint above node perimeter
```

And the intended geometry invariant is now explicit:

```text
connector endpoint position
    follows the rendered node perimeter continuously
    including temporary hover-lift transforms
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
endpoint marker remains centered on the visible perimeter
```

Exact hover-lift attachment fix:

```text
ae2951e2325e6e6e624131097dcc1edc732e1844
```

## 4. Frame sockets restored to the earlier treatment

The project owner explicitly said the frame sockets were good before the endpoint-overlay change and asked to restore them.

Therefore K2 is intentionally different from the dot/hover-port treatment:

```text
K2 Frame Sockets
    remain in the original under-node relation layer
    visually dock into the frame edge
    are not cloned into the above-node endpoint overlay
```

This preserves their more structural, instrument-like character.

## 5. Implementation sequence

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
```

Current exact browser implementation target:

```text
ae2951e2325e6e6e624131097dcc1edc732e1844
```

## 6. Preliminary connector-composition insight

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

## 7. Emerging architecture hypothesis

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

## 8. Current gate

The project owner asked to resolve the visual corrections before giving the fuller connector decision.

Therefore the active gate is:

```text
human verifies K1/K4 endpoint markers stay attached above the perimeter during hover lift
human verifies K2 restored frame-socket treatment
-> human gives connector-composition preference
-> only then implement the next combined-directionality experiment
```

No production `/cockpit` files changed.
