# Checkpoint 225: Configurable Appearance Promoted, Connector Grammar Review Opened

**Date:** 2026-08-26  
**Status:** Current product-design checkpoint  
**Checkpoint class:** CONTINUITY / PRODUCT_DESIGN / PROMOTION  
**Project stage:** V1 next-generation Project Cockpit browser-rendered design exploration  
**Scope:** Closes the user-configurable appearance prototype gate after positive human review, fixes the remaining scene-connector attachment defect, promotes the semantic/presentation separation into Foundation 023, and opens the next connector/port visual-grammar browser experiment.  
**Authority:** Current Phase-C routing boundary. Foundation 023 is promoted as durable product-interface direction. Final production settings persistence and connector semantics remain unfrozen. Specification 008 remains the promoted Cockpit interaction architecture.

## 1. Human configurator review

The configurable Cockpit prototype was judged:

```text
Very good
```

The only reported issue was a small implementation defect in the relation lines connecting project-scene boxes.

The underlying product direction is accepted:

```text
normal boxes and subtle shapes can coexist
micro design may be enabled or disabled
approved visual mechanisms may coexist as user configuration
users should be able to personalize the Cockpit for their own data projects
```

## 2. Connector attachment defect fixed

Root cause:

```text
static SVG connector coordinates
    !=
actual rendered node geometry
```

The customizable preview now computes connector endpoints from the rendered `.node-surface` bounds and regenerates them when layout-relevant state changes.

It also respects the Investigation right-edge notch when Subtle shapes are active.

Exact connector-fix commit:

```text
c1f996f6500672641de8e00780d5a4949c5dcb28
```

Local configurator route remains:

```text
http://localhost:5173/design-lab/work-unit-grammar-customizable.html
```

## 3. Promotion audit

The configurable-appearance principle now has:

```text
multiple browser-rendered visual mechanisms
repeated human evaluation
explicit product-owner approval
an executable configurator proof
clear semantic-safety boundary
```

The line defect was unrelated to the product principle and has been corrected.

Promotion is therefore justified for the principle:

```text
ADS owns semantic meaning
user controls approved non-semantic appearance dimensions
```

Promoted artifact:

```text
docs/foundations/023_user_configurable_cockpit_appearance_and_semantic_invariants.md
```

Not promoted:

```text
localStorage as production persistence
final settings UI
account synchronization
project override precedence
team/shared appearance behavior
complete appearance-option inventory
```

## 4. Current appearance architecture

Stable semantic layer:

```text
Question / Blocker        circle
Investigation             square
Validation / Analysis     triangle
Model Work                diamond
Evaluation                plus

Reduced in-box light      preferred baseline
category/status/runtime/importance meaning system-owned
```

Current proven configurable presentation dimensions:

```text
Box shape
    Normal
    Subtle shapes

Micro design
    None
    Micro material
    Micro light
```

## 5. Work-unit grammar disposition

The work-unit appearance slice is now sufficiently converged to stop searching for one universal visual winner.

The design objective becomes:

```text
stable semantic grammar
+
curated configurable appearance profile
```

Earlier rejected experiments remain historical evidence, not active appearance choices.

## 6. Next slice opened: connector / port grammar

Natural next question:

> How should project relationships meet work units and remain legible without turning the Cockpit into graph noise?

This is also the correct dependency-aligned moment to reopen Claude C4 Port Grammar.

Research:

```text
docs/research/053_connector_and_port_visual_grammar_experiment.md
```

Browser route:

```text
frontend/design-lab/connector-grammar.html
frontend/design-lab/connector-grammar.css
frontend/design-lab/connector-grammar.js
```

Local URL:

```text
http://localhost:5173/design-lab/connector-grammar.html
```

## 7. Connector candidate matrix

```text
K0  Clean Curve
K1  Micro Dots
K2  Frame Sockets
K3  Target Cue
K4  Hover Ports
```

Held controls:

```text
G4 world
scientific category markers
Reduced in-box light
accepted H4 hover response
Subtle shapes
Micro material
same node geometry
same relation fixture
```

The experiment isolates only connector/port treatment.

## 8. Production boundary

No production `/cockpit` file changes.

No graph/canvas dependency is selected.

No final connector semantic vocabulary is frozen.

## 9. Exact continuation

```text
1. pull v1-cockpit-design-exploration
2. optionally refresh http://localhost:5173/design-lab/work-unit-grammar-customizable.html to verify the connector attachment fix
3. open http://localhost:5173/design-lab/connector-grammar.html
4. compare K0 through K4
5. hover each work unit and inspect relation emphasis / hover-port behavior
6. judge resting noise, attachment clarity, direction usefulness and scale plausibility
7. human may prefer, reject or combine connector mechanisms
8. preserve the generic connector baseline before adding semantic relation classes
9. keep production Cockpit untouched
```
