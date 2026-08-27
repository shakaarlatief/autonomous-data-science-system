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

## 5. Controlled fixture

Every controlled row uses the same work unit:

```text
category       Investigation
disposition    Current
status         RUN
priority       HIGH
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

## 7. Practical interaction scene

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

## 8. Accessibility boundary

Keyboard focus remains conceptually separate from selection.

A keyboard-focused node may be selected or unselected. The browser keeps an explicit `:focus-visible` outline so the selection treatment is never asked to perform accessibility focus duty.

## 9. Human review gate

Review:

```text
1. compare SEL1-SEL8 against SEL0
2. verify the selected state remains visible after pointer exit
3. verify hover still reads as transient and stronger/localized rather than persistent selection
4. verify A3 HIGH-attention signal bars remain independent
5. inspect BLOCKED / FAIL / RUN coexistence
6. click between work units in the practical scene
7. use keyboard focus and Enter / Space selection
8. reject treatments that resemble connector ports, priority, hover or project-focus suppression
9. prefer / reject / combine / refine
```

## 10. Still unfrozen

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

Production `/cockpit` remains untouched.
