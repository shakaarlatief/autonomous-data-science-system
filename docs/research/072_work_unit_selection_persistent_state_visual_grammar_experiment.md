# Research 072: Work-Unit Selection Persistent-State Visual Grammar Experiment

**Date:** 2026-08-27  
**Status:** Active Phase-C semantic/visual experiment  
**Scope:** Opens a bounded visual grammar experiment for persistent user selection after A3 Signal Bars received explicit human acceptance for elevated attention priority.  
**Authority:** Research evidence only. This memo does not freeze selection cardinality, selection persistence, detail-opening behavior, semantic zoom, deep-focus transitions, keyboard-focus treatment, or the final Cockpit visual system.

## 1. Boundary transition from attention priority

Research 071 isolated one narrow question:

```text
ATTENTION PRIORITY
    among visible work, which work deserves more attention now?
```

The project owner selected:

```text
A3  Signal Bars
```

and responded:

```text
I choose A3. Perfect. Proceed.
```

Current accepted Phase-C priority direction:

```text
HIGH attention
    three ascending micro-bars
    near the upper-right frame
    structurally separated from disposition and operational status
```

The priority ontology, ownership, persistence and relationship to scheduling/relevance remain unfrozen.

## 2. Why persistent selection is the next bounded question

The Cockpit now has distinct working visual channels for:

```text
category
project disposition
current-process membership
operational status / BLOCKED
attention priority
```

A separate interaction state remains necessary:

```text
SELECTION
    which work unit has the user explicitly chosen for inspection or action?
```

Selection must not be confused with:

```text
HOVER
    transient pointer encounter

KEYBOARD FOCUS
    accessibility / input navigation state

CURRENT-PROCESS FOCUS MEMBERSHIP
    whether the work unit belongs to the emphasized process set

ATTENTION PRIORITY
    whether visible work deserves elevated attention

DEEP FOCUS / SPECIALIST WORKSPACE
    a higher interaction depth entered from the map
```

The word `focus` is therefore avoided for this slice except when describing those already distinct concepts.

## 3. Relationship to the preserved work-unit expansion idea

The project owner previously proposed:

```text
compact work-unit box
    -> expanded contextual/detail box
    -> full specialist workspace / deep focus
```

Persistent selection is a prerequisite interaction question for that later hierarchy because the Cockpit needs a stable answer to:

```text
which compact work unit is currently chosen?
```

This slice deliberately stops there. Clicking a work unit selects it but does not yet resize it, open inline details or mount a specialist workspace.

## 4. Held controls

The experiment keeps:

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
```

Selection uses a provisional neutral cool highlight so category hue and attention priority remain independently readable.

## 5. Browser implementation

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

Initial browser implementation target:

```text
3bac1fea4ca820c89a7bc4516497a4c33164ec5d
```

Production `/cockpit` remains untouched.

## 6. Human-detected selection-layer clipping defect and repair

The project owner inspected the initial browser and reported that SEL0, SEL1 and SEL2 appeared effectively identical.

Implementation inspection confirmed a real rendering defect rather than merely insufficient visual contrast.

The selection decorations were generated inside `.node-surface`, while `.node-surface` intentionally uses:

```css
overflow: hidden;
```

Several candidate geometries deliberately extend outside the rendered work-unit surface:

```text
SEL1  Outer Keyline       inset -4px
SEL2  Corner Brackets     inset -5px
SEL4  Edge Ticks          inset -5px
SEL6  Soft Contour        inset -5px
SEL7  Double Corner       inset -6px
SEL8  Keyline + Corners   includes the same outer geometry
```

Therefore the selection ornaments were clipped by the surface that was supposed to contain only the work-unit's internally clipped material and lighting layers.

The repair preserves the surface clipping contract and instead changes layer ownership:

```text
BEFORE
    grammar-node
        node-surface        overflow hidden
            selection geometry
                -> outer portions clipped

AFTER
    grammar-node
        selection geometry  overflow-visible sibling layer
        node-surface        overflow hidden remains intact
            internal material / light / text / status / priority
```

No candidate definition, semantic meaning, hover behavior, priority signal or operational-status behavior was intentionally changed by this repair.

Exact repaired visual implementation target:

```text
e7304fe834d86166d843fda7e1df0f4ddb1f793a
```

This remains inside Checkpoint 240's existing selection-state human-review gate and therefore does not warrant a new checkpoint.

## 7. Controlled fixture

Every controlled row uses the same work unit:

```text
category       Investigation
disposition    Current
status         RUN
priority       HIGH
selection      SELECTED
```

Only the persistent selection treatment changes.

## 8. Candidate selection treatments

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

### SEL0 Neutral Control
No selected-specific cue. Baseline.

### SEL1 Outer Keyline
A thin neutral outline sits just outside the rendered work-unit frame.

### SEL2 Corner Brackets
Four compact neutral corner brackets sit outside the frame and persist after pointer exit.

### SEL3 Inner Frame
A restrained inset frame sits inside the work-unit surface.

### SEL4 Edge Ticks
Four small mid-edge ticks mark the selected object. This intentionally tests whether instrument-like ticks become too similar to connector ports or priority markers.

### SEL5 Selection Plate
The selected work unit gains a subtle persistent elevation and neutral plate shadow. This intentionally tests possible collision with H4 hover lift.

### SEL6 Soft Contour
A low-salience outer contour/glow persists around the selected node. This is partly a falsification candidate because it may resemble hover/world illumination.

### SEL7 Double Corner
Only the upper-left and lower-right corners receive stronger selection brackets, testing asymmetric minimalism.

### SEL8 Keyline + Corners
Combines SEL1 and SEL2 to test whether restrained redundant geometry improves persistent recognition or merely adds clutter.

## 9. Practical interaction scene

The practical scene contains mixed category, disposition, operational-status and priority combinations. Exactly one work unit is selected in the initial fixture.

Interaction proof:

```text
click work unit
    -> move persistent selection to that work unit

Enter / Space on keyboard-focused work unit
    -> select it

Clear selection
    -> remove persistent selection

pointer hover
    -> H4 hover remains transient and independent
```

This is a browser interaction proof only. Final single-selection versus multi-selection semantics remain open.

## 10. Accessibility boundary

Keyboard focus remains conceptually separate from selection.

A keyboard-focused node may be selected or unselected. The browser keeps an explicit `:focus-visible` outline so the selection treatment is never asked to perform accessibility focus duty.

## 11. Human review gate

Review the repaired browser rather than the original clipped target:

```text
1. compare SEL1-SEL8 against SEL0 after the layering repair
2. verify SEL1 / SEL2 / SEL4 / SEL6 / SEL7 / SEL8 are now visibly distinct
3. verify the selected state remains visible after pointer exit
4. verify hover still reads as transient and stronger/localized rather than persistent selection
5. verify A3 HIGH-attention signal bars remain independent
6. inspect BLOCKED / FAIL / RUN coexistence
7. click between work units in the practical scene
8. use keyboard focus and Enter / Space selection
9. reject treatments that resemble connector ports, priority, hover or project-focus suppression
10. prefer / reject / combine / refine
```

## 12. Still unfrozen

```text
final selection visual treatment
single versus multi-selection
selection persistence across navigation / refresh
selection ownership in URL/session/project state
relationship between selection and inline expansion
relationship between selection and deep-focus workspace entry
selected-node command surface
selected-node inspector behavior
semantic zoom
C5 Internal Layout Grammar
expanded contextual/detail card
selected/focused persistent treatment in production
```
