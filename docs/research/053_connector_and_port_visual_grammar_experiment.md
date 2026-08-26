# Research 053: Connector and Port Visual Grammar Experiment

**Date:** 2026-08-26  
**Status:** Active Phase-C product-design evidence  
**Scope:** Opens the next browser-rendered Cockpit slice after work-unit appearance convergence: generic project-relationship routing and endpoint/port treatment.  
**Authority:** Research/design evidence only. No final connector semantics or production graph architecture is promoted.

## 1. Why this slice is next

Work-unit appearance now has a stronger boundary:

```text
semantic category marker mapping   stable
Reduced in-box light               preferred baseline
approved box/surface appearance    user-configurable
```

The remaining project-scene relation lines therefore become one of the most salient unresolved visual systems.

Claude concept C4 Port Grammar was deliberately deferred until connector semantics became the active dependency. This is now the correct moment to evaluate it.

## 2. Current bounded question

> How should generic project relationships visually attach to work units and communicate structure while remaining quiet enough for large analytical project maps?

This first connector slice intentionally does **not** freeze final relation types such as dependency, evidence support, lineage, recommendation, runtime flow, or approval.

Those semantic relation classes require separate evidence.

The present experiment isolates:

```text
line routing
edge attachment
endpoint visibility
port integration
directional cue strength
hover revelation
```

## 3. Held controls

To preserve causal interpretability, the connector experiment holds:

```text
G4 Adaptive Hybrid world
scientific work-unit markers
Reduced in-box resting light
accepted H4 hover/world response
Subtle shapes
Micro material
same five-node churn-project fixture
same four generic relationships
```

The appearance profile is merely a representative held visual control. Foundation 023 now allows the end user to choose other approved appearance combinations later.

## 4. Geometry invariant

The relation geometry must derive from the rendered work-unit surfaces rather than hardcoded nominal card positions.

Current routing:

```text
Question -> Investigation
Investigation -> Validation
Validation -> Model
Model -> Evaluation
```

Dynamic endpoints:

```text
right -> left
right -> left
right -> left
bottom -> top
```

The Investigation notch receives a silhouette-aware right-edge anchor.

This routing substrate is held across all connector-style candidates.

## 5. Layering invariant

Human review identified an important distinction between the connector curve and the endpoint marker.

Preferred visual hierarchy:

```text
world / grid
    ↓
connector curve
    ↓
work-unit body
    ↓
endpoint dot / socket / port
```

Interpretation:

```text
connector curve
    remains behind the work-unit surface
    terminates cleanly at the rendered perimeter

endpoint marker
    sits visibly above the work-unit perimeter
    reads as a physical attachment point rather than a hidden decoration
```

This matters particularly for:

```text
K1 Micro Dots
K2 Frame Sockets
K4 Hover Ports
```

K3 Target Cue is also rendered in the endpoint overlay because it is a destination-side directional marker rather than part of the underlying curve.

Implementation uses two coordinated SVG layers:

```text
connector-relations
    under-node curve layer

connector-port-overlay
    above-node endpoint layer
```

The existing geometry engine remains authoritative. Endpoint geometry and hover state are mirrored into the overlay so resize-safe anchoring and relation emphasis remain synchronized.

## 6. Candidate family

### K0 Clean Curve

```text
edge-to-edge curve
no visible endpoint port
lowest resting visual noise
```

Question:

```text
Is the cleanest possible attachment already sufficient?
```

### K1 Micro Dots

```text
small source and target endpoint dots
ports visible at rest
markers centered on and above the work-unit perimeter
```

Question:

```text
Do explicit attachment points improve legibility enough to justify added visual density?
```

### K2 Frame Sockets

```text
small square endpoint sockets
more structural / instrument-like integration
sockets centered on and above the work-unit perimeter
```

Question:

```text
Should relationships feel physically docked into the work-unit frame?
```

### K3 Target Cue

```text
clean curve
restrained target-side chevron
source remains unmarked
target cue rendered above the destination edge
```

Question:

```text
Is persistent direction useful without resorting to a large generic arrowhead?
```

### K4 Hover Ports

```text
clean rest state
endpoint dots appear only when a connected work unit is hovered
hover ports render above the work-unit perimeter
```

Question:

```text
Can progressive disclosure preserve a calm world while still revealing attachment structure on demand?
```

## 7. Browser implementation

Route:

```text
frontend/design-lab/connector-grammar.html
frontend/design-lab/connector-grammar.css
frontend/design-lab/connector-grammar.js
frontend/design-lab/connector-port-layering.css
frontend/design-lab/connector-port-layering.js
```

Local URL:

```text
http://localhost:5173/design-lab/connector-grammar.html
```

The page provides one stable project scene and lets the human switch K0-K4 directly so unrelated geometry does not change between comparisons.

Current endpoint-layer refinement target:

```text
08a33868b1c1d2cd90f11431e3f6b730603f28eb
```

This target includes the separate above-node endpoint overlay and keeps relation curves below the nodes.

## 8. Evaluation questions

Human review should judge:

```text
resting visual noise
attachment clarity
large-project scalability
product identity
whether ports feel useful or ornamental
whether target direction should be persistent
whether hover-only revelation is sufficient
whether line attachment looks physically correct on all silhouettes
whether ports read as attached to the frame rather than hidden behind it
```

A candidate may also be combined later. For example, a clean K0 resting state could coexist with K4 hover ports and a later semantic direction cue only for relation classes that actually require direction.

## 9. Non-decisions

This experiment does not yet decide:

```text
final semantic connector vocabulary
relation colors
dashed/solid meaning
runtime-flow animation
evidence-support relation styling
lineage relation styling
blocked/approval relation styling
multi-edge routing at large scale
edge bundling
auto-layout
port placement under semantic zoom
production graph/canvas technology
```

Those remain open and should be addressed only when their dependency context is active.
