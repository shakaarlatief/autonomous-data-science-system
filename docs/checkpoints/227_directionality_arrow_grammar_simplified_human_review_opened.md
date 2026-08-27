# Checkpoint 227: Directionality Arrow Grammar Simplified, Human Review Opened

**Date:** 2026-08-27  
**Status:** Current product-design checkpoint  
**Checkpoint class:** CONTINUITY / PRODUCT_DESIGN / REFINEMENT  
**Project stage:** V1 next-generation Project Cockpit browser-rendered design exploration  
**Scope:** Preserves the human clarification that connector terminal treatment and hover behavior are separate mechanisms, simplifies the directionality browser to the original edge-connected arrow treatment, and opens a narrow visual verification gate before semantic relation-class work.  
**Authority:** Current Phase-C routing boundary. Foundation 024 is refined accordingly. Final semantic relation taxonomy remains unfrozen.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** chatgpt-08  
**Conversation title:** 08 - Project Cockpit Design Exploration  
**Primary collaborator:** ChatGPT

## 1. Human clarification

The project owner rejected unnecessary mixed terminal treatments in the directionality experiment.

Current model:

```text
connector treatments
    Clean
    Micro dots
    Frame sockets
    Direction arrows

hover
    separate behavior
    can reveal or emphasize the selected treatment
```

Do not interpret hover as a terminal symbol that must be combined with arrows, dots or sockets.

## 2. Directionality browser refinement

The directionality page now shows arrows only:

```text
D0  A - B
    no arrow

D1  A -> B
    arrow at B

D2  A <- B
    same arrow at A

D3  A <-> B
    same arrow at A and B
```

No dots or sockets are shown in this controlled comparison.

## 3. Arrow geometry

The arrow uses the earlier K3-style edge-connected geometry:

```text
arrow tip
    exact work-unit perimeter

arrow arms
    outside the box

forward / reverse / bidirectional
    same mechanism, only endpoint placement changes
```

Rendered-edge geometry and H4 hover-lift synchronization remain active.

## 4. Foundation refinement

Foundation 024 now states:

```text
semantic relation state
    system-owned

connector treatment
    one active terminal treatment at a time

hover behavior
    orthogonal interaction mechanism
```

This avoids unnecessary symbol stacking while preserving user-configurable presentation.

## 5. Browser target

Local URL:

```text
http://localhost:5173/design-lab/connector-directionality.html
```

Exact implementation target:

```text
07d573b6569b9f09a3b7e00936f3eadecee721b3
```

Research:

```text
docs/research/056_directionality_arrow_grammar_and_hover_separation_refinement.md
```

## 6. Current human gate

```text
verify D0 remains undirected and clean
verify D1 arrow docks directly to B
verify D2 is the exact mirrored arrow at A
verify D3 is the same arrow at both ends
verify arrow treatment is not mixed with dots or sockets
```

If accepted, proceed to semantic relation-class design.

## 7. Production boundary

Production `/cockpit` remains untouched.

No graph/canvas dependency is selected.

Specification 008 remains the promoted Cockpit interaction architecture.

Permanent source-vault deployment remains paused and the Course 2 gate is unchanged.