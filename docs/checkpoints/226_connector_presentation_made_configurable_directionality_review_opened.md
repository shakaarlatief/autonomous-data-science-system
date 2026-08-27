# Checkpoint 226: Connector Presentation Made Configurable, Directionality Review Opened

**Date:** 2026-08-27  
**Status:** Current product-design checkpoint  
**Checkpoint class:** CONTINUITY / PRODUCT_DESIGN / PROMOTION  
**Project stage:** V1 next-generation Project Cockpit browser-rendered design exploration  
**Scope:** Closes the K0-K4 winner-selection gate, preserves the human decision to retain approved connector treatments as user-configurable presentation dimensions, promotes connector semantic/presentation separation into Foundation 024, and opens the next directionality browser slice.  
**Authority:** Current Phase-C routing boundary. Foundation 024 is promoted as durable product-interface direction. Final semantic relation taxonomy, final direction-cue vocabulary and production persistence remain unfrozen.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** chatgpt-08  
**Conversation title:** 08 - Project Cockpit Design Exploration  
**Primary collaborator:** ChatGPT

## 1. Human connector decision

The project owner decided that the useful connector mechanisms should coexist as user-adjustable presentation choices rather than forcing one winner.

Current presentation interpretation:

```text
Rest attachment
    Clean
    Micro dots
    Frame sockets

Hover attachment emphasis
    Off
    On
```

The previous K0/K1/K2/K4 candidates are therefore retained as compatible presentation mechanisms.

## 2. Semantic boundary

The same configurability rule cannot be applied blindly to relation meaning.

The durable distinction is:

```text
user may configure
    HOW a connector is presented

ADS / project relation model determines
    WHAT the relation means
    WHETHER it is directed
    WHICH way it points
```

A user preference may not silently remove, reverse or invent semantic direction.

## 3. Foundation promotion

Promoted artifact:

```text
docs/foundations/024_composable_connector_presentation_and_semantic_directionality.md
```

Core principle:

```text
ADS owns relation meaning and directionality
+
user controls approved non-semantic connector presentation dimensions
```

This extends Foundation 023 without replacing it.

## 4. Latest connector visual evidence

Retained refinements:

```text
42ec63d17095753dc4ab97628cd859473cbdf5e8
    K1/K4 circular markers moved mostly outside the work-unit perimeter

183264bdd07783eaa2354894592f2cf4a076b6ec
    K2 sockets adopt the active relation color / glow while highlighted
```

Held geometry/interaction behavior:

```text
curve below node body
rendered-edge anchoring
hover-lift geometry synchronization
above-node dots / hover ports
frame-integrated K2 sockets
```

## 5. Directionality browser opened

Research:

```text
docs/research/055_connector_presentation_configurability_and_directionality_browser_slice.md
```

Browser route:

```text
frontend/design-lab/connector-directionality.html
frontend/design-lab/connector-directionality.css
frontend/design-lab/connector-directionality.js
```

Local URL:

```text
http://localhost:5173/design-lab/connector-directionality.html
```

Exact browser implementation target:

```text
41bbdb75f338388f02a34fdf7dbac3ea90f86300
```

## 6. Directionality matrix

The next human comparison is:

```text
D0  Undirected      A — B
D1  Forward         A -> B
D2  Reverse         A <- B
D3  Bidirectional   A <-> B
```

The page also exposes Clean / Micro dots / Frame sockets and Hover emphasis On/Off so the human can check compatibility without reopening the connector-style decision.

## 7. Important non-decisions

Still open:

```text
final direction-cue shape
final semantic relation taxonomy
chronology / causality / dependency / evidence / lineage encoding
line color / dash semantics
runtime-flow connector behavior
production connector settings persistence
final graph / canvas implementation
```

## 8. Production boundary

No production `/cockpit` file changed.

No graph/canvas dependency is selected.

Specification 008 remains the promoted Cockpit interaction architecture.

The permanent source-vault bootstrap remains paused and the Course 2 gate is unchanged.

## 9. Exact continuation

```text
1. pull v1-cockpit-design-exploration
2. open http://localhost:5173/design-lab/connector-directionality.html
3. compare D0-D3
4. optionally switch Clean / Micro dots / Frame sockets
5. toggle Hover attachment emphasis and confirm direction remains semantically visible
6. judge forward, reverse and bidirectional cue clarity
7. preserve keep / refine / replace direction-cue evidence
8. only then open semantic relation-class exploration
9. keep production Cockpit untouched
10. keep source-vault deployment paused until explicitly resumed
```