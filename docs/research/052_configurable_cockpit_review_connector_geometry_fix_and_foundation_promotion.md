# Research 052: Configurable Cockpit Review, Connector Geometry Fix, and Foundation Promotion

**Date:** 2026-08-26  
**Status:** Phase-C product-design evidence  
**Scope:** Records human approval of the user-configurable Cockpit appearance model, diagnoses and fixes the remaining project-scene connector attachment defect, and justifies promotion of the semantic/presentation separation into Foundation 023.  
**Authority:** Product-design evidence. Does not freeze production settings persistence or final connector semantics.

## 1. Human review result

The user-configurable visual-grammar prototype received a strongly positive human review:

```text
Very good
```

The only reported defect was that the project-scene relation lines did not correctly connect the work-unit boxes.

The product concept itself was accepted:

```text
normal and subtle box shapes may coexist
micro design may be on or off
approved visual mechanisms may coexist as user preferences
the user should be able to personalize the Cockpit for their own data projects
```

This moves configurability beyond a speculative design-lab idea.

## 2. Connector defect diagnosis

The customizable preview inherited static SVG path coordinates from an earlier fixed fixture.

That was fragile because the current page uses:

```text
different node widths
different percentage positions
a different world height
configurable clipped silhouettes
responsive browser geometry
```

Therefore the line endpoints could visually float away from the actual rendered node boundaries.

The underlying problem was:

```text
connector geometry authored against assumed coordinates
instead of derived from rendered geometry
```

## 3. Geometry correction

The customizable preview now derives every connector from the actual rendered `.node-surface` bounding boxes.

Current fixture relations:

```text
Question -> Investigation
Investigation -> Validation
Validation -> Model
Model -> Evaluation
```

Anchoring rules:

```text
first three relations
    source right edge -> target left edge

Model -> Evaluation
    source bottom edge -> target top edge
```

For the Investigation right-edge notch under Subtle shapes, the connector anchors to the actual visible inset rather than the rectangular wrapper boundary.

The paths are regenerated:

```text
after initial render
after view changes
after shape changes
after resize / observed scene geometry changes
```

Thus relation lines remain attached when the user switches between Normal and Subtle shapes or when the viewport changes.

Exact defect-fix commit:

```text
c1f996f6500672641de8e00780d5a4949c5dcb28
```

## 4. Product-architecture conclusion

The remaining line defect was an implementation geometry issue, not evidence against configurable appearance.

The human review plus executable prototype justify promotion of the durable principle:

```text
ADS owns semantic meaning
+
user controls approved non-semantic appearance dimensions
```

Promoted foundation:

```text
docs/foundations/023_user_configurable_cockpit_appearance_and_semantic_invariants.md
```

Foundation 023 promotes the principle while explicitly leaving final settings persistence, collaboration behavior, profile migration, and the complete option inventory unfrozen.

## 5. Next design implication

The connector defect also exposes the next natural Phase-C slice.

Now that meaningful work-unit appearance has a stable semantic/configurable boundary, the next high-value visual question is:

> How should project relationships attach to work units and remain legible without turning the Cockpit into graph noise?

This also reopens Claude concept C4 Port Grammar at the dependency-aligned moment originally reserved for it.
