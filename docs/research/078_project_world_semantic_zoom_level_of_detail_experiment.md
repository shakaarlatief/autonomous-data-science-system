# Research 078: Project-World Semantic Zoom Level-of-Detail Experiment

**Date:** 2026-08-27  
**Status:** Phase-C interaction-design evidence, deferred with S0 working default  
**Scope:** Explored how work-unit information could simplify, persist, aggregate or become richer as the navigable project world changes scale.  
**Authority:** Research evidence only. The project owner has explicitly deferred semantic-zoom information changes and directed S0 Geometric Control to remain the current working behavior. This is not a final rejection of semantic zoom.

## 1. Predecessor closure

Research 077 records:

```text
Z7 Pull-Back Then Dive
    selected deep-focus entry direction

end state
    fullscreen specialist workspace
    no project grid / surrounding map
    compact topology compass retained
```

Selected/fixed spatial-browser target:

```text
04616a52df5cceff6c59223bbd6f07448d027510
```

## 2. Question explored

Specification 008 promotes bounded geometric zoom and a finite navigable project world, while Research 037 identified semantic-scale information architecture as unresolved.

The experiment separated:

```text
GEOMETRIC ZOOM
    physical scale / camera distance

SEMANTIC ZOOM
    information architecture at that scale
```

and asked:

```text
As the project world zooms out and in,
what information should survive,
aggregate,
disappear,
or become richer?
```

## 3. Browser

Local route:

```text
http://localhost:5173/design-lab/work-unit-semantic-zoom.html
```

Files:

```text
frontend/design-lab/work-unit-semantic-zoom.html
frontend/design-lab/work-unit-semantic-zoom.css
frontend/design-lab/work-unit-semantic-zoom.js
```

Exact implementation target:

```text
65ac02326a75b1c9f056676819d2d1b7b23b74c5
```

Production `/cockpit` remains untouched.

## 4. Controlled candidates

```text
S0  Geometric Control
    same information largely survives at every scale

S1  Progressive Detail
S2  Stage Clusters
S3  Topology First
S4  Focus Preserving
S5  Status First
S6  Glyph Field
S7  Hybrid Contextual
S8  Local Detail Lens
```

Every candidate was shown at provisional Overview, Work and Inspection levels.

## 5. Human disposition

The project owner explicitly deprioritized semantic information changes by zoom for now:

```text
For now, lets not change information etc dependent on the zoom,
so I think that is S0.
We will save this for later.
Proceed.
```

Current interpretation:

```text
S0 Geometric Control
    provisional working default
    keep information behavior stable across zoom for now
    sufficient to continue Phase C

S1-S8
    preserved for later
    not rejected

semantic zoom as a capability
    DEFERRED
    not cancelled
    not rejected
    not superseded
```

This is intentionally analogous to the earlier L0 internal-layout disposition: use the simplest stable behavior while the project explores more important unresolved Cockpit questions.

## 6. Why this is not a final semantic-zoom rejection

Large-project operation may eventually create stronger evidence for semantic-level adaptation. The following remain open and preserved:

```text
exact zoom thresholds
continuous versus discrete semantic transitions
cluster construction and interaction
stage taxonomy / grouping semantics
label collision strategy
large-project virtualization
relation simplification / bundling
selected-node detail persistence
focus-set interaction with scale
priority/status visibility by scale
semantic zoom animation
production graph/canvas library
performance implementation
```

The project should reopen semantic zoom when real large-project density, rendering, navigation or comprehension evidence makes the complexity earn its place.

## 7. Checkpoint disposition

The human choice is strong enough to close the active semantic-zoom review without promoting a semantic-scale system.

A new checkpoint should preserve:

```text
S0 working default
semantic zoom deferred for later
S1-S8 preserved
```

and route Phase C to the next first-class unresolved product problem.
