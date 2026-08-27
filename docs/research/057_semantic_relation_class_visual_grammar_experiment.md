# Research 057: Semantic Relation-Class Visual Grammar Experiment

**Date:** 2026-08-27  
**Status:** Active Phase-C product-design evidence  
**Scope:** Closes the simplified arrow-directionality verification after positive human review and opens a bounded browser experiment for how different relationship meanings should be visually distinguished.  
**Authority:** Research/design evidence only. The representative relation classes are fixtures for visual evaluation and are not a frozen ADS semantic ontology.

## 1. Preceding human decision

The project owner visually reviewed the simplified D0-D3 directionality browser and judged it:

```text
perfect
```

Therefore the direction grammar is sufficiently settled for the current design phase:

```text
Undirected      A - B       no arrow
Forward         A -> B      same restrained arrow at B
Reverse         A <- B      same restrained arrow at A
Bidirectional   A <-> B     same restrained arrow at both endpoints
```

The arrow tip remains docked to the exact rendered work-unit perimeter and follows H4 hover-lift geometry.

## 2. Next design question

With connector treatment, hover behavior and directionality separated, the next unresolved semantic question is:

> How should different relationship meanings remain distinguishable on the Project Cockpit without turning the map into a dense technical diagram?

This question is deliberately separate from directionality.

```text
DIRECTION
    whether and which way the relation points

RELATION CLASS
    what the relationship means
```

A chronology relation and a causal relation may both be A -> B while still carrying different semantics.

## 3. Provisional relation fixtures

The browser uses five representative relation classes:

```text
R0  Chronology / Sequence
    Work B follows Work A in project order

R1  Dependency / Prerequisite
    Work B depends on Work A being available or resolved

R2  Causal / Influence
    a change in Work A can affect Work B

R3  Evidence / Support
    Work A supplies evidence used to support Work B

R4  Lineage / Derivation
    Work B is derived from an output or artifact of Work A
```

These categories were selected because they represent meaningfully different relationship concepts already relevant to the wider ADS design discussion.

They are **not** a final taxonomy. Classes may later be renamed, split, merged, added or removed after methodological/product evidence.

Runtime-flow relations remain outside this first semantic-class slice because runtime state may require a different visual/temporal grammar.

## 4. Held controls

The experiment deliberately holds constant:

```text
G4 world
Reduced in-box resting light
accepted H4 hover behavior
scientific work-unit category markers
Subtle work-unit shapes
Micro-material surface treatment
same Investigation -> Validation node pair
same A -> B arrow direction
same rendered-edge connector geometry
same arrow geometry
```

Only the visual channel used to distinguish relation class changes.

## 5. Encoding families

The browser exposes seven strategies:

```text
E0  Neutral Control
    same neutral line for every class
    no additional semantic encoding

E1  Semantic Hue
    class-specific restrained line/arrow hue

E2  Stroke Rhythm
    neutral hue
    class-specific solid/dash/dot rhythm

E3  Explicit Tag
    neutral line
    compact midpoint semantic code

E4  Hue + Stroke
    redundant class-specific hue and line rhythm

E5  Hue + Tag
    class-specific hue plus explicit semantic tag

E6  Restrained Hybrid
    hue + stroke + compact semantic tag
```

The count is evidence-driven, not quota-driven. Each strategy tests a genuinely different information channel or combination.

## 6. Why these channels matter

### Hue

Potential benefit:

```text
rapid pre-attentive grouping
clean continuous line geometry
```

Risk:

```text
competes with work-unit category colors
color-vision accessibility
may imply importance/status rather than relation meaning
```

### Stroke rhythm

Potential benefit:

```text
works without color
can remain compact at map scale
```

Risk:

```text
may feel like engineering-diagram notation
small dash patterns may degrade under zoom
```

### Explicit tag

Potential benefit:

```text
high semantic certainty
low learning burden
```

Risk:

```text
text density
midpoint labels may clutter large projects
```

### Redundant combinations

Potential benefit:

```text
stronger accessibility
multiple recognition channels
```

Risk:

```text
over-encoding
visual noise
unnecessary duplication
```

## 7. Interaction rule

Hovering either endpoint highlights the relation using its semantic-class color, but does not change its class or direction.

The accepted H4 node interaction remains the control.

Direction arrows remain persistent because direction is semantic. The relation-class encoding likewise must remain available without depending exclusively on hover if that encoding becomes required for meaning.

## 8. Browser implementation

Files:

```text
frontend/design-lab/relation-class-grammar.html
frontend/design-lab/relation-class-grammar.css
frontend/design-lab/relation-class-grammar.js
```

Local URL:

```text
http://localhost:5173/design-lab/relation-class-grammar.html
```

Exact browser implementation target:

```text
9ac3a0a0f51c024d0deec2fe54f11735f4cdd0fb
```

## 9. Human review gate

The current human comparison should answer:

```text
Does hue help or compete with node color?
Are stroke rhythms legible and professional?
Are semantic tags useful or too text-heavy?
Does redundancy improve clarity enough to justify its noise?
Which mechanisms remain plausible at large-project scale?
Do any representative classes require stronger differentiation than others?
```

The human does not need to select the final ADS relation taxonomy in this gate.

## 10. Production boundary

No production `/cockpit` file changed.

No graph/canvas dependency is selected.

No final semantic relation taxonomy is promoted.

No final relation-color or dash vocabulary is promoted.

The permanent source-vault bootstrap remains paused and the Course 2 gate remains unchanged.
