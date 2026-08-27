# Research 059: Work-Unit Project-Disposition Visual Grammar Experiment

**Date:** 2026-08-27  
**Status:** Active Phase-C product-design evidence  
**Scope:** Closes the relation-class tag-refinement gate after positive human verification and opens a bounded browser experiment for how a work unit should communicate its project disposition without conflating category, runtime state or importance.  
**Authority:** Research/design evidence only. The disposition fixtures are representative visual-test states and do not freeze the final ADS project-state ontology.

## 1. Preceding human decision

The project owner accepted the refined E5 relation-class treatment after the final tag-placement and typography adjustments:

```text
E5 Hue + Tag
    selected for relation-class meaning

final tag refinement
    taller tag body retained
    tag restored clearly above connector line
    slightly taller lettering accepted

human result
    Perfect. Let's proceed.
```

The latest accepted relation-class browser implementation before opening this slice is:

```text
497e81f06ba1f9901511449237d1bb9f96b2d108
```

Stroke rhythm from E2/E4/E6 remains preserved as a future line-level semantic resource, with no meaning assigned yet.

## 2. Why project disposition is the next question

Earlier work-unit grammar research separated four different questions that must not collapse into one visual treatment:

```text
WHAT IS THIS?
    category / work-unit kind

WHAT IS ITS PROJECT DISPOSITION?
    active / recommended / deferred / completed / blocked / future

WHAT IS HAPPENING NOW?
    idle / queued / running / waiting / failed / waiting for human

HOW IMPORTANT IS IT NOW?
    required / recommended / relevant / lower priority
```

The first question now has a selected scientific-marker grammar. Connector semantics and relation-class meaning have also progressed substantially.

The next bounded work-unit question is therefore:

> How should a work unit communicate its project disposition while preserving category identity and without implying runtime or priority semantics that are not actually present?

This is especially important because the Cockpit must eventually make differences between unresolved, active, completed, blocked and future work visible without turning every node into a dense status dashboard.

## 3. Provisional disposition fixtures

The browser uses six representative project-disposition states:

```text
S0  Active / Current
    work currently central to the project path

S1  Recommended / Next
    a strong candidate for the next project action

S2  Deferred
    valid work intentionally postponed for now

S3  Completed
    work whose current project obligation is satisfied

S4  Blocked
    work unable to proceed until another condition is resolved

S5  Future / Not yet active
    known possible work outside the current active horizon
```

These states are fixtures for visual evaluation only.

They do **not** freeze:

```text
final state names
final state count
exact lifecycle transitions
whether blocked is represented as a disposition, constraint or orthogonal axis in the production data model
```

The browser is allowed to use a representative blocked state because it is a high-value visual distinction even while the final ontology remains open.

## 4. Held controls

The experiment deliberately holds constant:

```text
same Investigation category in every row
scientific square category marker
same node category hue
Subtle work-unit shape
M1 micro-material treatment
Reduced in-box resting light
accepted H4 hover/world response
same title and descriptive copy
runtime state = idle / not visualized
importance = constant / not visualized
no connector relation-class change
```

This prevents project disposition from being confused with category, runtime activity or priority.

## 5. Encoding families

The browser exposes seven disposition strategies:

```text
P0  Neutral Control
    no disposition encoding on the work unit

P1  Disposition Hue
    restrained state-colored outer perimeter

P2  Explicit Tag
    compact neutral state label only

P3  Tonal Hierarchy
    state carried through opacity / saturation / brightness changes

P4  State Rhythm
    compact top-edge line rhythm with no state hue

P5  Hue + Tag
    redundant state hue plus explicit compact label

P6  Restrained Hybrid
    hue + tag + rhythm, with selective tonal reduction for completed/deferred/future states
```

The count is evidence-driven rather than quota-driven. Each family tests a materially different visual information channel or combination.

## 6. Why these channels matter

### Disposition hue

Potential benefit:

```text
fast grouping
low text density
```

Risk:

```text
competes with category color
may be confused with relation-class hue
color-only accessibility weakness
```

### Explicit tag

Potential benefit:

```text
high semantic certainty
low learning burden
```

Risk:

```text
node-label density
may make every work unit feel like a status card
```

### Tonal hierarchy

Potential benefit:

```text
quiet professional hierarchy
easily makes future/deferred/completed work recede
```

Risk:

```text
may accidentally imply importance
may make completed work look disabled
may reduce legibility too aggressively
```

### State rhythm

Potential benefit:

```text
uses a non-color visual channel
compact and potentially learnable
```

Risk:

```text
can resemble engineering-diagram notation
may not survive semantic zoom
may compete with the stroke-rhythm resource already reserved for future line-level semantics
```

The browser intentionally exposes this tension rather than assuming one rhythm vocabulary can safely serve both nodes and connectors.

### Redundant combinations

Potential benefit:

```text
stronger recognition
better accessibility
```

Risk:

```text
over-encoding
visual noise
semantic channels become difficult to reserve for later runtime / importance axes
```

## 7. Interaction rule

H4 hover remains the held interaction behavior.

Disposition cues must remain intelligible when the work unit receives:

```text
2 px hover lift
node-colored halo
pointer-following hotspot
perimeter sweep
```

Hover must not mutate project disposition.

Runtime activity remains deliberately absent from this slice.

## 8. Browser implementation

Files:

```text
frontend/design-lab/work-unit-disposition-grammar.html
frontend/design-lab/work-unit-disposition-grammar.css
frontend/design-lab/work-unit-disposition-grammar.js
```

Local URL:

```text
http://localhost:5173/design-lab/work-unit-disposition-grammar.html
```

Exact browser implementation target:

```text
565fdeabc1ebaa29f993699a4c0673b29e972be3
```

## 9. Human review gate

The current human review should answer:

```text
Which strategies make the six dispositions distinguishable without reading every external row label?
Does state hue compete with category hue?
Does a compact node tag improve clarity or create too much status-card density?
Does tonal hierarchy communicate lifecycle position or incorrectly imply priority?
Are node-state rhythms useful or better reserved for another semantic dimension?
Does a restrained combination outperform its individual channels?
```

The human does not need to select the final ADS project-state ontology in this gate.

## 10. Production boundary

No production `/cockpit` file changed.

No final project-disposition ontology is promoted.

No runtime-state visual grammar is selected.

No priority/importance grammar is selected.

No graph/canvas dependency is selected.

The permanent source-vault bootstrap remains paused and the Course 2 gate remains unchanged.
