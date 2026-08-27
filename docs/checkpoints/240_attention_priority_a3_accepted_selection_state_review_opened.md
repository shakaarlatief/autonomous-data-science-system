# Checkpoint 240: A3 Attention Priority Accepted, Persistent Selection Review Opened

**Date:** 2026-08-27  
**Status:** Current product-design checkpoint  
**Checkpoint class:** CONTINUITY / PRODUCT_DESIGN / SEMANTIC_VISUAL_GRAMMAR  
**Project stage:** V1 next-generation Project Cockpit browser-rendered design exploration  
**Scope:** Closes the Checkpoint 239 attention-priority visual gate after human selection of A3 Signal Bars, then opens a distinct experiment for persistent work-unit selection as an interaction state separate from hover, keyboard focus, current-process focus membership, attention priority and deep-focus workspace entry.  
**Authority:** Current Phase-C routing/evidence boundary only. Final priority ontology, selection semantics, selection persistence, inline expansion behavior, semantic zoom and production visual system remain unfrozen.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** chatgpt-08  
**Conversation title:** 08 - Project Cockpit Design Exploration  
**Primary collaborator:** ChatGPT

## 1. Human acceptance closing Checkpoint 239

Research 071 compared nine treatments for provisional elevated attention priority:

```text
A0  Neutral Control
A1  Twin Tick
A2  Top Rail
A3  Signal Bars
A4  Side Bracket
A5  HIGH Tag
A6  Beacon
A7  Luminance Lift
A8  Rail + Tag
```

The project owner selected:

```text
A3  Signal Bars
```

and responded:

```text
I choose A3. Perfect. Proceed.
```

Current accepted Phase-C attention-priority visual direction:

```text
HIGH attention
    three ascending micro-bars
    upper-right structural signal
    separated from disposition badge and bottom-right operational status
```

Exact browser implementation in which A3 was reviewed and selected:

```text
767c66f76974d3c0a851de0dfa17c502817a4b12
```

Research evidence:

```text
docs/research/071_work_unit_attention_priority_visual_grammar_experiment.md
```

This acceptance does not freeze the priority ontology, scale, ownership, persistence, relationship to relevance or relationship to scheduling.

## 2. Why persistent selection is the next boundary

The Cockpit now has comparatively mature Phase-C evidence for several separate work-unit channels:

```text
category
project disposition
current-process focus membership
operational status / BLOCKED
attention priority
```

A different interaction state remains:

```text
SELECTION
    which work unit has the user explicitly chosen for inspection or action?
```

Selection must remain distinct from:

```text
HOVER
    transient pointer encounter

KEYBOARD FOCUS
    accessibility / input navigation

CURRENT-PROCESS FOCUS MEMBERSHIP
    whether the work unit belongs to the emphasized process set

ATTENTION PRIORITY
    whether visible work deserves elevated attention

DEEP FOCUS / SPECIALIST WORKSPACE
    higher interaction depth entered from the project map
```

## 3. Relationship to the preserved expanded-box idea

The previously preserved hierarchy remains:

```text
compact map work unit
    -> expanded contextual/detail card
    -> full specialist workspace / deep focus
```

Persistent selection is a useful prerequisite because the system first needs a stable visual answer to which compact work unit the user has chosen.

The new experiment deliberately stops before inline expansion. Clicking a box selects it but does not resize it or mount deeper content.

## 4. New browser target

Local route:

```text
http://localhost:5173/design-lab/work-unit-selection-state.html
```

Files:

```text
frontend/design-lab/work-unit-selection-state.html
frontend/design-lab/work-unit-selection-state.css
frontend/design-lab/work-unit-selection-state.js
```

Exact browser implementation target:

```text
3bac1fea4ca820c89a7bc4516497a4c33164ec5d
```

Research:

```text
docs/research/072_work_unit_selection_persistent_state_visual_grammar_experiment.md
```

Production `/cockpit` remains untouched.

## 5. Controlled selection fixture

Every controlled row holds:

```text
category       Investigation
disposition    Current
status         RUN
priority       HIGH using A3 Signal Bars
selection      SELECTED
```

Only the persistent selection treatment changes.

## 6. Candidate selection treatments

```text
SEL0  Neutral Control
SEL1  Outer Keyline
SEL2  Corner Brackets
SEL3  Inner Frame
SEL4  Edge Ticks
SEL5  Selection Plate
SEL6  Soft Contour
SEL7  Double Corner
SEL8  Keyline + Corners
```

The practical scene supports direct selection transfer by click and by Enter / Space on a keyboard-focused node. A separate Clear selection action proves that persistent selection is an explicit interaction state rather than a permanently required node property.

## 7. Held visual controls

```text
G4 Adaptive Hybrid world
H4 hover/world response
Reduced in-box resting light
scientific category marker family
P7 Neutral Tag + Tone disposition
accepted operational-status carrier grammar
BLOCKED sharper compact ring
FAIL smoother circular compact ring
A3 Signal Bars for HIGH attention
```

Keyboard focus remains explicitly visible and is not delegated to the selection treatment.

## 8. Current human gate

The next actor is the human project owner.

Review:

```text
1. pull v1-cockpit-design-exploration
2. open work-unit-selection-state.html
3. compare SEL1-SEL8 against SEL0
4. move selection between practical-scene work units
5. verify selected state persists after pointer exit
6. verify H4 hover remains transient and semantically different
7. verify A3 Signal Bars remain readable as attention priority
8. inspect BLOCKED / FAIL / RUN coexistence
9. use Tab plus Enter / Space to verify keyboard focus and selection remain different
10. reject treatments that resemble connector ports, priority, hover or project-focus suppression
11. prefer / reject / combine / refine
12. keep inline expansion deferred until selection treatment is sufficiently understood
13. keep production Cockpit untouched
```
