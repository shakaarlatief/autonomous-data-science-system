# Foundation 024: Composable Connector Presentation and Semantic Directionality

**Date:** 2026-08-27  
**Status:** Foundational product-interface direction  
**Scope:** Durable separation between relationship semantics and user-configurable connector presentation in the Project Cockpit. Does not freeze the final semantic relation taxonomy, final arrow/cue vocabulary, production preference persistence, or graph implementation.  
**Primary evidence:** Research 053 through Research 055, Checkpoints 225 through 226, and repeated human browser review in MC-0004 Phase C.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** chatgpt-08  
**Conversation title:** 08 - Project Cockpit Design Exploration

## Purpose

Browser evaluation of connector treatments showed that several high-quality mechanisms are useful for different users and working styles. Clean curves, micro dots, frame sockets and hover attachment emphasis do not need to compete for one universal visual winner.

The durable connector principle is:

> **ADS owns relationship meaning and directionality; the user may personalize approved connector-presentation dimensions that do not alter that meaning.**

This extends Foundation 023 from work-unit appearance into relationship presentation.

## 1. Semantic relation state and connector presentation are separate layers

The architecture should preserve:

```text
semantic relation model
    whether a relation exists
    source and target work units
    relation meaning / class
    directionality
    provenance / evidence where applicable
    runtime or methodological semantics where applicable

connector presentation profile
    rest attachment treatment
    hover attachment emphasis
    approved line / cue styling
    other future non-semantic visual preferences
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
    may change HOW direction is drawn

user appearance preference
    may not change WHETHER the relation is directed
    may not reverse source and target
    may not hide required direction so completely that meaning is lost
```

A directed relation must remain recognizably directed in every approved appearance profile.

## 3. Connector presentation is compositional

Human review rejected the need for one universal K0-K4 winner.

The useful mechanisms are better interpreted as orthogonal presentation dimensions:

```text
Rest attachment
    Clean
    Micro dots
    Frame sockets

Hover attachment emphasis
    Off
    On

Direction cue presentation
    semantically required when the relation is directed
    visual style may become configurable later if all approved styles preserve meaning
```

This means K0, K1, K2 and K4 can coexist as user-facing appearance choices rather than mutually exclusive product directions.

K3 contributes the direction-cue mechanism, but its semantic presence is not merely an appearance toggle.

## 4. Proven connector behavior

Current browser evidence supports these interaction invariants:

```text
connector curve
    remains beneath work-unit bodies
    anchors to actual rendered node geometry
    follows temporary H4 hover lift / release

Micro dots / Hover ports
    render above the work-unit perimeter
    sit mostly outside the card with only a small overlap

Frame sockets
    retain frame-integrated structural docking
    use a neutral outline at rest
    adopt the active relation color and restrained glow when highlighted

Hover relation emphasis
    may reveal or intensify attachment points
    must remain subordinate to semantic direction cues
```

These are product-design evidence, not yet production component contracts.

## 5. Strong defaults and curated choice

Configurability does not mean an unlimited connector-style editor.

ADS should provide:

```text
a strong default
small numbers of validated presentation choices
useful presets
clear reset behavior
accessible combinations
semantic-safety validation
```

A likely clean default can remain visually restrained while advanced users choose richer attachment treatments.

## 6. Preference hierarchy

Foundation 023's preference hierarchy extends naturally to connectors:

```text
user appearance profile
    default connector presentation across projects

project appearance override
    optional project-specific connector presentation

semantic relation state
    independent from both
```

Production persistence, synchronization, collaboration behavior and migration/versioning remain open.

## 7. Accessibility and semantic safety override preference

ADS may constrain or adapt a requested connector appearance when necessary for:

```text
contrast / readability
reduced motion
focus visibility
semantic direction distinguishability
large-project density
performance
screen-reader / non-visual representation
```

A user-configurable style must never make direction, relation state or methodological meaning materially ambiguous.

## 8. Current evidence boundary

This foundation promotes:

```text
connector presentation is user-configurable within approved bounds
semantic relation meaning remains system-owned
directionality remains system-owned
presentation dimensions should be compositional rather than monolithic themes
```

It does not promote:

```text
final relation taxonomy
final direction-cue shape
final line-color semantics
final dashed / solid semantics
final dependency / evidence / lineage vocabulary
final runtime-flow connector behavior
production settings persistence
specific graph / canvas implementation
```

Those remain subjects of later evidence.
