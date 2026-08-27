# Research 055: Connector Presentation Configurability and Directionality Browser Slice

**Date:** 2026-08-27  
**Status:** Active Phase-C product-design evidence  
**Scope:** Closes the generic connector-style winner question, preserves the human decision to retain approved connector treatments as user-configurable presentation dimensions, promotes the semantic/presentation separation for connectors, and opens a controlled directionality browser experiment.  
**Authority:** Research/design evidence only. Final semantic relation taxonomy and final direction-cue vocabulary remain open.

## 1. Human decision

After repeated browser refinement of K0-K4, the project owner decided:

```text
keep everything useful
make it adjustable by the user
stop forcing one connector-style winner
```

The decision follows the same product logic already promoted for work-unit appearance:

```text
multiple coherent visual mechanisms
    can coexist

user may choose presentation
    while ADS preserves meaning
```

## 2. Connector candidates reinterpreted as dimensions

The previous candidate matrix was:

```text
K0  Clean Curve
K1  Micro Dots
K2  Frame Sockets
K3  Target Cue
K4  Hover Ports
```

Human evidence now supports a compositional interpretation:

```text
REST ATTACHMENT PRESENTATION
    Clean
    Micro dots
    Frame sockets

PROGRESSIVE DISCLOSURE / HOVER ATTACHMENT EMPHASIS
    Off
    On

DIRECTION CUE
    required when the semantic relation is directed
    not merely a user on/off appearance choice
```

Therefore K0, K1, K2 and K4 are retained as compatible presentation mechanisms.

K3 is retained as the seed of the semantic directionality grammar rather than treated as an optional decoration that could erase relation meaning.

## 3. Latest connector refinements carried forward

The accepted implementation evidence includes:

```text
42ec63d17095753dc4ab97628cd859473cbdf5e8
    K1/K4 circular terminals moved mostly outside the work-unit perimeter

183264bdd07783eaa2354894592f2cf4a076b6ec
    K2 sockets keep dark interiors but adopt the active relation color and restrained glow when highlighted
```

Other held connector invariants remain:

```text
curve below node body
endpoint overlay above node where appropriate
rendered-edge geometry authority
hover-lift geometry synchronization
K2 structural socket treatment preserved
```

## 4. Promotion result

The connector semantic/presentation separation has enough repeated human evidence to justify a durable foundation:

```text
docs/foundations/024_composable_connector_presentation_and_semantic_directionality.md
```

Promoted principle:

```text
ADS owns relation meaning and directionality
+
user controls approved non-semantic connector presentation dimensions
```

This does not freeze the final relation taxonomy or final production settings implementation.

## 5. Next bounded question: directionality

The next experiment deliberately isolates direction state before relation-type semantics.

Question:

> How should a relationship communicate no direction, one-way direction in either orientation, or bidirectional direction while remaining visually restrained and compatible with configurable attachment presentation?

The four comparison states are:

```text
D0  Undirected      A — B
D1  Forward         A -> B
D2  Reverse         A <- B
D3  Bidirectional   A <-> B
```

These are direction states, not final relation classes.

Examples such as chronological, causal, dependency, evidence and lineage remain later semantic-vocabulary work.

## 6. Browser implementation

Route:

```text
frontend/design-lab/connector-directionality.html
frontend/design-lab/connector-directionality.css
frontend/design-lab/connector-directionality.js
```

Local URL:

```text
http://localhost:5173/design-lab/connector-directionality.html
```

Exact browser implementation target:

```text
41bbdb75f338388f02a34fdf7dbac3ea90f86300
```

The browser exposes already-approved presentation dimensions for compatibility checking:

```text
Rest attachment
    Clean
    Micro dots
    Frame sockets

Hover attachment emphasis
    On / Off

Reduced motion
    On / Off
```

Those controls do not alter the direction state of any comparison lane.

## 7. Direction-cue experiment design

All four lanes hold constant:

```text
same source and target work-unit geometry
same category-marker language
same Reduced resting light
same micro-material / subtle-shape visual system
same curve geometry
same H4 hover lift and relation emphasis
same rendered-edge synchronization
```

Only direction state changes.

Direction cues are placed outside the work-unit edge so they can coexist with:

```text
clean attachment
micro dots
frame sockets
hover attachment emphasis
```

A directed cue remains persistent at rest because direction carries semantic information.

## 8. Evaluation questions

Human review should judge:

```text
Is A -> B immediately readable?
Is A <- B equally readable?
Does A <-> B read as bidirectional rather than duplicated decoration?
Are restrained endpoint chevrons sufficient or is a different cue needed?
Do the direction cues remain legible with dots and sockets?
Does persistent direction at rest feel functionally justified and visually calm?
```

## 9. Current gate

```text
human reviews connector-directionality.html
-> keep / refine / replace direction-cue mechanism
-> preserve directionality grammar
-> then open semantic relation-class exploration
```

No production `/cockpit` files changed.
