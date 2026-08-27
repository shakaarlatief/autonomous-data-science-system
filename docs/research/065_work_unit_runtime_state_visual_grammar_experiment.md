# Research 065: Work-Unit Runtime-State Visual Grammar Experiment

**Date:** 2026-08-27  
**Status:** Active Phase-C product-design evidence  
**Scope:** Opens a browser-rendered comparison for how a work unit should communicate live execution/runtime state while preserving the already-separated category, project-disposition, priority and current-focus dimensions.  
**Authority:** Research/design evidence only. The final ADS runtime ontology, runtime connector-flow grammar and production implementation remain unfrozen.

## 1. Why this slice is next

The preceding work-unit slices have now materially separated and tested:

```text
WHAT IS THIS?
    category / work-unit kind

WHAT IS ITS PROJECT DISPOSITION?
    P7 Neutral Tag + Tone accepted for current Phase C

IS IT IN THE CURRENTLY EMPHASIZED PROCESS?
    current-focus membership + user-curated focus lens accepted as product direction
```

A major semantic axis repeatedly held out from those experiments remains:

```text
WHAT IS HAPPENING NOW?
    runtime / execution state
```

Opening runtime now avoids letting later execution behavior leak accidentally into category, disposition or focus styling.

## 2. Held semantic separation

The new browser explicitly preserves:

```text
category
    what kind of work unit this is

project disposition
    where the work unit stands in the project

runtime state
    what execution is doing right now

priority / relevance
    how important the work is now

current-focus membership
    whether the work belongs to the emphasized process set
```

The current slice isolates only runtime state.

## 3. Provisional runtime fixtures

The first visual-test state set is:

```text
Idle
Queued
Running
Waiting
Waiting for Human
Failed
```

These are not a frozen ADS execution-state ontology.

In particular, the final system may later distinguish additional concepts such as retrying, cancelled, stale, succeeded, waiting for resource, waiting for dependency or waiting for approval. This experiment does not need to solve that ontology before testing visual carriers.

## 4. Held visual controls

The browser carries forward:

```text
G4 Adaptive Hybrid world
Reduced in-box resting light
accepted H4 hover response
scientific category markers
Subtle work-unit shapes
Micro material treatment
P7 neutral project-disposition tag at rest
P7 disposition hue reveal on hover
```

Current-process focus suppression is conceptually separate and is held out of the controlled runtime rows. The practical scene is rendered as an all-visible project context so runtime legibility can be judged without the stronger focus suppression becoming a confound.

## 5. Runtime carrier matrix

The browser exposes seven mechanisms:

```text
R0  Neutral Control
    no runtime-specific carrier

R1  Status Lamp
    small colored status lamp
    static in the isolated carrier test

R2  Activity Rail
    thin bottom-edge runtime rail
    state-specific rhythm / semantic motion for active waiting/running states

R3  Runtime Tag
    compact explicit runtime text label
    tests maximum readability versus tag-density cost

R4  Instrument Cell
    small bottom-right instrument module
    state-specific compact symbol

R5  Motion Signal
    small lamp + localized semantic motion ring
    tests whether live state can feel active without another text label

R6  Restrained Hybrid
    small lamp + compact runtime tag
    tests limited redundant encoding without a large surface treatment
```

No candidate count was selected in advance. These seven survive because they test materially different visual channels.

## 6. Semantic motion rule

Runtime motion is semantic motion, not ambient decoration.

Therefore:

```text
Running / Queued / Waiting / Waiting for Human
    may use restrained state-specific motion

Idle / Failed
    remain interpretable without animated activity

Reduced motion
    removes animation
    does NOT remove the static runtime-state identity
```

This follows the previously preserved distinction between semantic and ambient motion.

## 7. Saved connector stroke rhythm remains reserved

Research 058 preserved connector-line stroke rhythm as a future line-level semantic resource after Hue + Tag was selected for relation class.

This node-level runtime experiment does not consume that resource.

A later runtime-flow connector slice may test whether moving or patterned relation lines are useful for communicating execution flow, data movement or active dependency traversal. No meaning is assigned here.

## 8. Practical mixed-category scene

The page also renders a small mixed-category project scene with neutral P7 disposition tags and representative runtime states.

Its purpose is to reveal problems that controlled rows may hide:

```text
second-tag clutter
runtime/category color competition
runtime/disposition ambiguity
motion overload
monitoring-dashboard appearance
loss of premium analytical feel
```

The practical fixture intentionally includes combinations such as Blocked + Waiting for Human, Active + Running, Recommended + Queued, Active + Failed, Deferred + Waiting and Future + Idle.

These combinations are visual-test examples rather than final semantic rules.

## 9. Browser implementation

Files:

```text
frontend/design-lab/work-unit-runtime-grammar.html
frontend/design-lab/work-unit-runtime-grammar.css
frontend/design-lab/work-unit-runtime-grammar.js
```

Local URL:

```text
http://localhost:5173/design-lab/work-unit-runtime-grammar.html
```

Exact browser implementation target:

```text
099e516bf9a7351a756bee00037edbcc731a2738
```

## 10. Human review gate

The next review should answer:

```text
Which carrier makes runtime state clear without competing with category?
Does R3 add too much tag density beside P7 disposition?
Do R1 / R4 feel sufficiently explicit and learnable?
Does R2 feel like useful runtime instrumentation or unnecessary decoration?
Does R5 semantic motion help without becoming distracting?
Does R6 provide useful redundancy or simply duplicate information?
Does Reduced motion preserve runtime meaning?
Which mechanisms survive the mixed-category scene?
```

The result may be select, reject, combine or refine. No final runtime ontology must be frozen in this gate.

## 11. Production boundary

No production `/cockpit` file changed.

No runtime persistence model is selected.

No execution engine state contract is modified.

No connector-flow semantics are assigned.
