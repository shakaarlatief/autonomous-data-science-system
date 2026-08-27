# Research 056: Directionality Arrow Grammar and Hover Separation Refinement

**Date:** 2026-08-27  
**Status:** Active Phase-C product-design evidence  
**Scope:** Preserves the human clarification that dots, sockets, arrows and hover behavior should not be unnecessarily combined, and refines the directionality browser to use the original restrained edge-connected arrow treatment only.  
**Authority:** Research/design evidence. Foundation 024 is updated because the clarification changes the durable connector-presentation model.

## 1. Human clarification

After reviewing the first directionality browser, the project owner simplified the connector model:

```text
we have
    sockets
    dots
    arrows
    hover mechanism

hover
    is a mechanism
    not another terminal symbol
    can reveal or emphasize whichever connector treatment is active

there is no need to combine
    arrows + dots
    arrows + sockets
    other unnecessary terminal stacks
```

For directionality specifically, the project owner asked to reuse the exact restrained arrow treatment from the earlier connector experiment and simply place it at the correct endpoint or endpoints.

## 2. Directionality grammar

The refined browser now isolates:

```text
D0  Undirected
    A - B
    no arrow

D1  Forward
    A -> B
    same arrow docked directly to B

D2  Reverse
    A <- B
    exact same arrow docked directly to A

D3  Bidirectional
    A <-> B
    exact same arrow at both endpoints
```

No dot or frame socket is shown in the directionality comparison.

## 3. Arrow geometry

The arrow treatment reuses the earlier K3 chevron geometry rather than the first directionality browser's offset cue.

Rule:

```text
arrow tip
    exact rendered work-unit edge

arrow arms
    remain outside the work-unit body

connector curve
    still terminates at the exact rendered edge
```

This makes the arrow read as a direct continuation of the connector into the work-unit boundary.

The same geometry is mirrored mechanically for reverse direction and duplicated for bidirectional relations.

## 4. Hover separation

Hover is now treated as a separate interaction dimension:

```text
connector treatment
    Clean
    Micro dots
    Frame sockets
    Direction arrows

hover behavior
    persistent
    reveal on hover / focus
    intensify on hover / focus
```

The current directionality browser intentionally does not expose the hover-treatment matrix because that would reintroduce combinations that are irrelevant to the direction-shape question.

The accepted H4 node hover still highlights the active relation and changes the arrow color, but it does not add dots or sockets.

## 5. Semantic constraint

Direction remains semantic:

```text
undirected
forward
reverse
bidirectional
```

If arrows are the active connector treatment, their endpoint placement must follow that semantic state exactly.

An appearance preference cannot:

```text
invent direction
reverse direction
convert bidirectional to one-way
convert one-way to undirected
```

The production treatment for progressive-disclosure arrows remains subject to accessibility and semantic-safety validation.

## 6. Implementation

Updated browser route:

```text
frontend/design-lab/connector-directionality.html
frontend/design-lab/connector-directionality.css
frontend/design-lab/connector-directionality.js
```

Local URL:

```text
http://localhost:5173/design-lab/connector-directionality.html
```

Implementation sequence:

```text
f2a1085740d97849933294738c2caf4c76e2590d
    simplify directionality browser structure and remove mixed terminal controls

a3a4e70fe2660e483f1d1190491bcc5c29d7b63b
    replace mixed terminal styling with arrow-only direction styling

07d573b6569b9f09a3b7e00936f3eadecee721b3
    render four direction states dynamically and dock K3-style arrows directly to work-unit edges
```

Exact browser implementation target:

```text
07d573b6569b9f09a3b7e00936f3eadecee721b3
```

## 7. Current gate

Human visual verification is now intentionally narrow:

```text
verify D0 has no arrow
verify D1 arrow touches B cleanly
verify D2 is the exact mirrored mechanism at A
verify D3 uses the same arrow at both ends
verify no dots / sockets are mixed into arrow directionality
```

If this is visually correct, directionality itself is sufficiently converged to move to semantic relation classes such as chronology, causality, dependency, evidence and lineage.

No production `/cockpit` file changed.
