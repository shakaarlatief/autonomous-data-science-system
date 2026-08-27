# Research 054: Connector Composition, Directionality and Endpoint-Layering Refinement

**Date:** 2026-08-27  
**Status:** Active Phase-C product-design evidence  
**Scope:** Preserves the next human review of the connector/Port Grammar slice, fixes the remaining endpoint-layering defect, restores the earlier frame-socket treatment, and records a preliminary shift from winner-take-all connector selection toward a compositional connector grammar.  
**Authority:** Research/design evidence only. No final connector semantic vocabulary is promoted.

## 1. Human visual defect report

After the first endpoint-overlay correction, the project owner visually verified the browser and found that K4 hover-port dots still appeared to sit underneath the box surface rather than clearly above the rendered perimeter.

The intended hierarchy remains:

```text
world / grid
    -> connector curve below node
    -> work-unit body
    -> micro-dot / hover-port / directional endpoint above node perimeter
```

The defect was not in relation geometry. It was a stacking-context / overlay-layer implementation issue.

## 2. Endpoint-layer correction

The dedicated `connector-port-overlay` is now explicitly positioned and assigned a stacking level above work-unit nodes.

K4 hover-port styling is also explicitly mapped to the overlay relation group, because the original K4 CSS selector targeted only the under-node `.connector-link` groups.

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

Exact implementation sequence:

```text
b8953973dda9b57bfa2071726ec0aadac0f7c028
    explicit above-node overlay stacking

ff24fbf09fd771e1bdfc574578fa4e2ffdb89d7c
    stop mirroring K2 sockets into overlay

4e597d35b79d807b8481dd6610f0eff261089ca5
    explicit K4 overlay hover-port reveal

ed27290d6f060f13a86d863a2faa7eede3c91a7e
    browser descriptions synchronized with restored socket treatment
```

Current exact browser implementation target:

```text
ed27290d6f060f13a86d863a2faa7eede3c91a7e
```

## 3. Frame sockets restored to the earlier treatment

The project owner explicitly said the frame sockets were good before the endpoint-overlay change and asked to restore them.

Therefore K2 is intentionally different from the dot/hover-port treatment:

```text
K2 Frame Sockets
    remain in the original under-node relation layer
    visually dock into the frame edge
    are not cloned into the above-node endpoint overlay
```

This preserves their more structural, instrument-like character.

## 4. Preliminary connector-composition insight

The project owner also supplied an important conceptual observation, but explicitly asked to fix the current visual mistakes before making the final connector choice.

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

## 5. Emerging architecture hypothesis

The connector system may therefore need to separate orthogonal dimensions such as:

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

## 6. Current gate

The project owner asked to stop after the visual corrections and provide the fuller connector decision next.

Therefore the active gate is:

```text
human verifies corrected K1/K4 above-node endpoints
human verifies K2 restored frame-socket treatment
-> human gives connector-composition preference
-> only then implement the next combined-directionality experiment
```

No production `/cockpit` files changed.
