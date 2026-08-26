# Foundation 023: User-Configurable Cockpit Appearance and Semantic Invariants

**Date:** 2026-08-26  
**Status:** Foundational product-interface direction  
**Scope:** Durable separation between Cockpit semantic meaning and user-configurable visual presentation. Does not freeze final settings persistence, theme inventory, team-sharing behavior, or final production component implementation.  
**Primary evidence:** Research 046 through Research 051, Checkpoints 218 through 224, and repeated human browser review in MC-0004 Phase C.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** chatgpt-08  
**Conversation title:** 08 - Project Cockpit Design Exploration

## Purpose

The Cockpit is a long-lived professional working environment for a user's own data-science projects. Phase-C browser evaluation showed that several visual mechanisms can be high quality, coherent, and semantically compatible at the same time. Requiring one universal aesthetic winner would therefore discard useful product value without improving methodological integrity.

The durable product principle is:

> **ADS owns semantic meaning; the user may personalize approved presentation dimensions that do not alter that meaning.**

This makes personalization a first-class product capability rather than an accidental theme layer.

## 1. Semantic project state and appearance are separate layers

The architecture should preserve the distinction:

```text
semantic project model
    work-unit meaning
    project disposition
    runtime state
    importance / recommendation strength
    evidence and provenance
    methodological constraints

presentation profile
    approved visual appearance choices
    visual density / richness choices where safe
    non-semantic stylistic preferences
```

Changing presentation must not mutate the underlying project model or imply a different analytical state.

## 2. Stable semantic invariants

Some visual channels may be reserved because they carry meaning or provide important redundancy.

Current evidence establishes the following work-unit category marker mapping for the active design direction:

```text
Question / Blocker        circle
Investigation             square
Validation / Analysis     triangle
Model Work                diamond
Evaluation                plus
```

The exact future work-unit taxonomy remains evolvable, but once a category-to-marker mapping is active inside a project/product version it should remain stable enough to be learnable.

Likewise, presentation preferences must not silently redefine:

```text
required / blocking
recommended
relevant / applicable
deferred
completed
queued
running
waiting
failed
approval needed
```

Those semantics remain system-owned.

## 3. Approved appearance dimensions may coexist

Phase-C evidence supports the principle that visually successful mechanisms can become orthogonal configuration dimensions rather than mutually exclusive winners.

Current proven examples include:

```text
Box shape
    normal rectangular work units
    subtle category-specific silhouettes

Micro design
    none
    micro-material treatment
    micro-light / lumen treatment
```

These options remain one coherent product language because typography, hierarchy, semantic marker mapping, state meaning, and interaction behavior remain stable.

Future appearance dimensions may be added only when they satisfy the same semantic-safety test.

## 4. Strong defaults remain necessary

Configurability does not mean ADS should present an uncurated collection of arbitrary visual options.

The product should provide:

```text
a strong default
small numbers of coherent approved choices
useful presets
clear reset / restore behavior
accessible combinations only
```

Current evidence prefers Reduced in-box resting illumination as the work-unit baseline while preserving the accepted H4 hover and outward-world response.

The purpose of personalization is user ownership and long-session comfort, not novelty for its own sake.

## 5. User and project preference hierarchy

A plausible durable preference model is:

```text
user appearance profile
    personal default across projects

project appearance override
    optional project-specific preference

semantic project state
    independent from both
```

This hierarchy is directionally accepted, but the exact production persistence contract remains unfrozen.

Open implementation questions include:

```text
account synchronization
local vs server persistence
per-project precedence
team/shared-project behavior
whether appearance is personal or shareable in collaborative projects
settings import/export
migration/versioning of appearance profiles
```

## 6. Accessibility and semantic safety override appearance preference

Appearance configuration is constrained by product correctness.

ADS may override, disable, or adapt a requested visual preference when necessary for:

```text
contrast/readability
reduced-motion requirements
keyboard/focus visibility
screen-reader compatibility
state distinguishability
semantic ambiguity avoidance
performance constraints
```

No user preference should make a semantic state materially harder to interpret or cause decorative motion to masquerade as runtime/project meaning.

## 7. Appearance should be compositional

The preferred implementation direction is configuration over independent approved dimensions rather than a collection of unrelated monolithic themes.

Conceptually:

```text
appearance profile
    shape grammar
    surface richness
    theme / color environment
    density where safe
    motion preference
    other future approved dimensions
```

Presets can select combinations of these dimensions, while advanced users may adjust them individually.

This keeps the design system maintainable and makes new combinations easier to validate.

## 8. Customization does not weaken product identity

A configurable Cockpit should still unmistakably feel like ADS.

Identity remains anchored by:

```text
shared spatial world
shared typography and hierarchy
shared work-unit semantics
shared scientific marker grammar
shared interaction behavior
shared state semantics
shared analytical workspace architecture
restrained professional visual register
```

Customization operates inside those boundaries.

## 9. Evidence boundary

This foundation promotes the **principle** of user-configurable approved appearance dimensions and the semantic/presentation separation.

It does not promote:

```text
the final production settings UI
localStorage as production persistence
all current design-lab choices as mandatory production options
final visual-system token values
final category taxonomy
final connector grammar
final semantic zoom behavior
```

Those remain subject to later design and implementation evidence.
