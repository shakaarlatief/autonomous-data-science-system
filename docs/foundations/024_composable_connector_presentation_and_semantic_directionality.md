# Foundation 024: Composable Connector Presentation and Semantic Directionality

**Date:** 2026-08-27  
**Status:** Foundational product-interface direction  
**Scope:** Durable separation between relationship semantics, connector treatment, and hover behavior in the Project Cockpit. Does not freeze the final semantic relation taxonomy, production preference persistence, or graph implementation.  
**Primary evidence:** Research 053 through Research 056, Checkpoints 225 through 227, and repeated human browser review in MC-0004 Phase C.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** chatgpt-08  
**Conversation title:** 08 - Project Cockpit Design Exploration

## Purpose

Browser evaluation showed that clean curves, micro dots, frame sockets, direction arrows, and hover-based reveal/emphasis are all useful, but they do not belong in one visually stacked connector treatment.

The durable connector principle is:

> **ADS owns relationship meaning and directionality; connector treatment and hover behavior are separate presentation mechanisms.**

This extends Foundation 023 from work-unit appearance into relationship presentation while preserving semantic safety.

## 1. Semantic relation state and presentation are separate layers

The architecture should preserve:

```text
semantic relation model
    whether a relation exists
    source and target work units
    relation meaning / class
    directionality
    provenance / evidence where applicable
    runtime or methodological semantics where applicable

connector treatment
    clean line
    micro dots
    frame sockets
    direction arrows when semantically appropriate
    other future approved terminal treatments

hover behavior
    persistent at rest
    reveal on hover / focus
    intensify on hover / focus
```

Changing presentation must never mutate the semantic relation model.

## 2. Directionality is a semantic invariant

The relation model may support:

```text
undirected
A -> B
A <- B
A <-> B
```

The exact future data model remains unfrozen, but the principle is fixed:

```text
user appearance preference
    may change approved presentation behavior

user appearance preference
    may not change WHETHER the relation is directed
    may not reverse source and target
    may not invent direction on an undirected relation
```

When direction arrows are used, arrow placement follows the semantic relation exactly:

```text
undirected       no arrow
A -> B           arrow at B
A <- B           arrow at A
A <-> B          arrows at both ends
```

## 3. One terminal treatment at a time

Human review clarified that useful connector mechanisms should not be visually stacked without a reason.

The preferred model is:

```text
connector treatment
    choose one active terminal treatment for the relation

examples
    Clean
    Micro dots
    Frame sockets
    Direction arrows
```

This explicitly rejects unnecessary combinations such as:

```text
arrow + dot
arrow + socket
socket + dot
```

unless a future semantic requirement gives such a combination a clear purpose and later evidence validates it.

The connector line itself remains common across treatments.

## 4. Hover is an orthogonal interaction mechanism

Hover is not a fifth terminal symbol.

It is an interaction behavior that may operate on whichever connector treatment is active:

```text
selected treatment
    Clean
    Micro dots
    Frame sockets
    Direction arrows

hover / focus behavior
    reveal selected treatment
    or intensify selected treatment
    or leave it persistent and only emphasize the relation
```

Therefore:

```text
hover + dots
    means dots can reveal / intensify on hover

hover + sockets
    means sockets can reveal / intensify on hover

hover + arrows
    means arrows can reveal / intensify on hover if semantic-safety and accessibility requirements are satisfied
```

The product must preserve non-visual and focus-accessible access to semantic direction even when visual progressive disclosure is used.

## 5. Proven connector geometry and interaction behavior

Current browser evidence supports these invariants:

```text
connector curve
    remains beneath work-unit bodies
    anchors to actual rendered node geometry
    follows temporary H4 hover lift / release

Micro dots
    render above the work-unit perimeter
    sit mostly outside the card with only a small overlap

Frame sockets
    retain frame-integrated structural docking
    use a neutral outline at rest
    adopt the active relation color and restrained glow when highlighted

Direction arrows
    reuse the restrained K3-style chevron
    arrow tip docks directly to the relevant work-unit edge
    reverse direction uses the exact same mechanism at the opposite endpoint
    bidirectional relations use the same arrow at both endpoints

Hover relation emphasis
    is separate from terminal type
    may reveal or intensify the selected treatment
```

These remain product-design evidence rather than final production component contracts.

## 6. Strong defaults and curated choice

Configurability does not mean an unlimited connector-style editor.

ADS should provide:

```text
a strong default
small numbers of validated treatment choices
useful presets
clear reset behavior
accessible combinations
semantic-safety validation
```

Some connector treatments may be constrained by relation semantics. For example, a direction-arrow treatment cannot invent direction for an undirected relation.

## 7. Preference hierarchy

Foundation 023's preference hierarchy extends naturally to connector presentation:

```text
user appearance profile
    default connector treatment / hover behavior

project appearance override
    optional project-specific preference

semantic relation state
    independent from both
```

Production persistence, synchronization, collaboration behavior and migration/versioning remain open.

## 8. Accessibility and semantic safety override preference

ADS may constrain or adapt a requested connector appearance when necessary for:

```text
contrast / readability
reduced motion
keyboard / focus visibility
semantic direction distinguishability
large-project density
performance
screen-reader / non-visual representation
```

A presentation preference must never change the underlying relation semantics.

## 9. Current evidence boundary

This foundation promotes:

```text
connector presentation is configurable within approved bounds
semantic relation meaning remains system-owned
directionality remains system-owned
terminal treatment and hover behavior are separate mechanisms
only one terminal treatment should normally be active at a time
arrow placement follows semantic direction exactly
```

It does not promote:

```text
final relation taxonomy
final line-color semantics
final dashed / solid semantics
final dependency / evidence / lineage vocabulary
final runtime-flow connector behavior
production settings persistence
specific graph / canvas implementation
```

Those remain subjects of later evidence.
