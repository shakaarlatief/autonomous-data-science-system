# Research 073: Work-Unit Contextual Detail Expansion Architecture Experiment

**Date:** 2026-08-27  
**Status:** Active Phase-C interaction-design experiment  
**Scope:** Closes the persistent-selection visual gate after human selection of SEL2 Corner Brackets and opens a bounded browser experiment for the intermediate contextual-detail layer between compact selected work units and the full specialist workspace promoted by Specification 008.  
**Authority:** Research evidence only. This memo does not freeze final work-unit information architecture, expansion persistence, deep-focus transition semantics, semantic zoom, large-project collision handling, or production implementation architecture.

## 1. Human acceptance closing the persistent-selection gate

Research 072 compared:

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

The first browser implementation contained a real layering defect: external selection geometry was mounted inside `.node-surface`, whose `overflow: hidden` clipped the intended outside-the-frame carriers. SEL1, SEL2, SEL4, SEL6, SEL7 and SEL8 therefore could not be judged reliably.

The repair moved the selection geometry to the `.grammar-node` layer while preserving surface clipping for internal material and lighting.

Exact repaired selection-browser visual target:

```text
e7304fe834d86166d843fda7e1df0f4ddb1f793a
```

After reviewing that repaired browser, the project owner selected:

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

The final selection cardinality, persistence ownership and URL/session/project-state behavior remain unfrozen.

## 2. Why contextual detail expansion is now the next boundary

A previously preserved interaction idea is:

```text
compact map work unit
    -> expanded contextual/detail card
    -> full specialist workspace / deep focus
```

Persistent selection was intentionally resolved first because the system needs a stable answer to which compact node is chosen before it can reveal more information about that node.

The next bounded question is therefore:

```text
CONTEXTUAL DETAIL EXPANSION
    after a compact work unit is selected,
    how should it reveal additional project context
    without immediately becoming the full specialist workspace?
```

This is an interaction-depth problem rather than a final data-schema problem.

## 3. Semantic and interaction separation held constant

```text
HOVER
    transient pointer interaction

SELECTION
    persistent chosen work unit

ATTENTION PRIORITY
    visible work deserves elevated attention

OPERATIONAL STATUS
    live runtime state or BLOCKED presentation

CONTEXTUAL DETAIL
    temporary richer information while remaining in the project map

DEEP FOCUS / SPECIALIST WORKSPACE
    full-resolution task environment at a deeper interaction layer
```

The experiment must not silently collapse contextual detail into deep focus.

## 4. Held visual controls

```text
G4 Adaptive Hybrid world
H4 hover/world response
Reduced in-box resting light
scientific category markers
P7 Neutral Tag + Tone disposition
accepted compact operational-status carrier
BLOCKED sharper compact ring
FAIL smoother circular compact ring
A3 Signal Bars for HIGH attention
SEL2 Corner Brackets for persistent selection
```

## 5. Detail payload is deliberately provisional

Every expansion candidate exposes the same placeholder contextual fields:

```text
Purpose
Constraint / state
Evidence
Next action
```

These fields exist only to give the expansion geometry realistic information density.

They are **not** a frozen work-unit schema or C5 Internal Layout Grammar.

## 6. Candidate expansion architectures

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

### X0 Compact Control
No contextual-detail layer. Tests whether expansion earns its visual and interaction cost at all.

### X1 Vertical Drawer
The selected card keeps its width and upper anchor while growing downward as one integrated object.

### X2 Right Sidecar
The compact source node remains stable while an attached right-hand detail wing appears.

### X3 Attached Sheet
A separate detail sheet hangs directly below the compact node through a short attachment stem.

### X4 Wide Split Card
The selected node becomes one wider two-column object with summary on the left and contextual details on the right.

### X5 Context Lens
The selected node grows in both axes while nearby context recedes. This deliberately probes the boundary where contextual detail starts behaving like deep focus.

### X6 Layered Reveal
The compact source card remains visually on top while a larger offset detail layer emerges behind it.

### X7 Peek Rail
Only a shallow information rail appears. This tests whether a very small intermediate step is useful or too weak.

### X8 Inspector Dock
The node remains compact and details appear in a stable scene-level inspector. This is a deliberate challenge to the inline-expansion premise.

## 7. Interaction proof in the practical scene

```text
click unselected node
    -> select it with SEL2
    -> keep compact

click selected compact node
    -> expand contextual detail

click selected expanded node
    -> collapse

Enter / Space
    -> keyboard equivalent of the same action

switch X0-X8
    -> change expansion architecture only
```

The interaction proof remains browser-local and does not freeze production navigation or persistence.

## 8. Browser

Local route:

```text
http://localhost:5173/design-lab/work-unit-detail-expansion.html
```

Files:

```text
frontend/design-lab/work-unit-detail-expansion.html
frontend/design-lab/work-unit-detail-expansion.css
frontend/design-lab/work-unit-detail-expansion-scroll.css
frontend/design-lab/work-unit-detail-expansion.js
```

Exact initial browser implementation target:

```text
0457a27d8e80863738ce3f75aeb11bd4f5c1155d
```

### Review-ergonomics adjustment

During the first human inspection, the project owner asked that the large explanatory page header scroll out of the viewport instead of remaining sticky, because the sticky header consumed substantial vertical space while comparing the lower expansion candidates.

The shared design-lab header remains sticky elsewhere. This browser overrides that behavior only for `.expansion-header`:

```text
position: static
```

No expansion candidate, semantic treatment, layout geometry or interaction behavior changed.

Exact browser target with the non-sticky review header:

```text
7e6861188e1e7e7eaeee599ca901108ca434753d
```

This is a review-usability refinement inside the existing Checkpoint 241 gate, not a new checkpoint or product-level header decision.

Production `/cockpit` remains untouched.

## 9. Current human review gate

Review:

```text
1. compare X1-X8 against X0
2. judge which treatment best preserves spatial orientation in the project map
3. judge whether attached panels remain obviously owned by the selected node
4. identify variants that consume too much project-map space
5. judge whether X5 crosses too far into deep-focus behavior
6. judge whether X7 provides enough information to justify a separate interaction depth
7. compare inline expansion against X8 Inspector Dock
8. verify SEL2, A3 and operational status remain independently legible
9. prefer / reject / combine / refine
10. do not freeze final internal work-unit information architecture from this geometry experiment alone
```

## 10. Still unfrozen

```text
final contextual-detail expansion treatment
expansion trigger semantics in production
single versus multiple expanded work units
expansion persistence across navigation / refresh
collision avoidance and repositioning
large-project expansion behavior
semantic zoom interaction with expansion
final work-unit internal information architecture
C5 Internal Layout Grammar
provenance/evidence detail presentation
selected-node command surface
transition from contextual detail to specialist workspace
URL representation for selected / expanded / deep-focus state
production animation implementation
```
