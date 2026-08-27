# Checkpoint 241: SEL2 Persistent Selection Accepted, Contextual Detail Expansion Review Opened

**Date:** 2026-08-27  
**Status:** Current product-design checkpoint  
**Checkpoint class:** CONTINUITY / PRODUCT_DESIGN / INTERACTION_ARCHITECTURE  
**Project stage:** V1 next-generation Project Cockpit browser-rendered design exploration  
**Scope:** Closes the Checkpoint 240 persistent-selection visual gate after repair of the selection-layer clipping defect and explicit human selection of SEL2 Corner Brackets, then opens a distinct browser experiment for the intermediate contextual-detail layer between compact selected work units and the full specialist workspace promoted by Specification 008.  
**Authority:** Current Phase-C routing/evidence boundary only. Final selection persistence, contextual-detail architecture, internal work-unit information schema, semantic zoom, deep-focus transition and production visual system remain unfrozen.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** chatgpt-08  
**Conversation title:** 08 - Project Cockpit Design Exploration  
**Primary collaborator:** ChatGPT

## 1. Human acceptance closing Checkpoint 240

The persistent-selection browser initially contained a real implementation defect. External selection decorations were mounted inside `.node-surface`, whose `overflow: hidden` clipped the outside-the-frame geometry.

The repair moved selection decorations to the `.grammar-node` layer while preserving surface clipping for internal card effects.

Exact repaired visual target:

```text
e7304fe834d86166d843fda7e1df0f4ddb1f793a
```

After reviewing the repaired browser, the project owner selected:

```text
SEL2  Corner Brackets
```

and responded:

```text
I choose SEL2. Perfect. Proceed.
```

Current accepted Phase-C persistent-selection direction:

```text
SELECTED
    four compact neutral-cool corner brackets
    outside the rendered work-unit frame
    persistent after pointer exit
```

Selection remains separate from hover, keyboard focus, current-process focus membership, attention priority and deep-focus workspace state.

Research evidence:

```text
docs/research/072_work_unit_selection_persistent_state_visual_grammar_experiment.md
```

## 2. Interaction hierarchy now under direct review

The preserved hierarchy is now promoted into a direct browser experiment:

```text
compact map work unit
    -> selected compact work unit
    -> expanded contextual/detail layer
    -> full specialist workspace / deep focus
```

This checkpoint evaluates only the third step.

The contextual layer should answer:

```text
What additional information about this selected work unit is useful
while the user still remains spatially oriented in the project map?
```

It must not silently become the specialist workspace itself.

## 3. Held visual and semantic controls

```text
G4 Adaptive Hybrid world
H4 hover/world response
Reduced in-box resting light
scientific category markers
P7 Neutral Tag + Tone disposition
accepted operational-status carrier
BLOCKED sharper compact ring
FAIL smoother circular compact ring
A3 Signal Bars for HIGH attention
SEL2 Corner Brackets for persistent selection
```

The placeholder detail fields are not a frozen schema.

## 4. New browser target

Local route:

```text
http://localhost:5173/design-lab/work-unit-detail-expansion.html
```

Files:

```text
frontend/design-lab/work-unit-detail-expansion.html
frontend/design-lab/work-unit-detail-expansion.css
frontend/design-lab/work-unit-detail-expansion.js
```

Exact initial browser implementation target:

```text
0457a27d8e80863738ce3f75aeb11bd4f5c1155d
```

Research:

```text
docs/research/073_work_unit_contextual_detail_expansion_architecture_experiment.md
```

Production `/cockpit` remains untouched.

## 5. Candidate contextual-detail architectures

```text
X0  Compact Control
X1  Vertical Drawer
X2  Right Sidecar
X3  Attached Sheet
X4  Wide Split Card
X5  Context Lens
X6  Layered Reveal
X7  Peek Rail
X8  Inspector Dock
```

All candidates expose the same provisional detail payload:

```text
Purpose
Constraint / state
Evidence
Next action
```

Only geometry, attachment and context treatment change.

## 6. Practical interaction proof

```text
click unselected node
    -> select with SEL2
    -> remain compact

click selected compact node
    -> expand contextual detail

click selected expanded node
    -> collapse

Enter / Space
    -> keyboard equivalent

switch X0-X8
    -> change only expansion architecture
```

This does not freeze production trigger semantics or persistence.

## 7. Current human gate

The next actor is the human project owner.

Review:

```text
1. pull v1-cockpit-design-exploration
2. open work-unit-detail-expansion.html
3. compare X1-X8 against X0
4. inspect whether each expanded treatment remains clearly attached to the selected work unit
5. judge preservation of project-map spatial orientation
6. reject variants that consume too much map context or resemble deep focus prematurely
7. compare true inline expansion against X8 Inspector Dock
8. verify SEL2, A3, disposition and operational status remain independently readable
9. prefer / reject / combine / refine
10. keep final internal work-unit information architecture unfrozen
11. keep production Cockpit untouched
```
