# Checkpoint 229: Relation-Class Hue + Tag Selected, Tag Refinement Review Opened

**Date:** 2026-08-27  
**Status:** Current product-design checkpoint  
**Checkpoint class:** CONTINUITY / PRODUCT_DESIGN / CONVERGENCE  
**Project stage:** V1 next-generation Project Cockpit browser-rendered design exploration  
**Scope:** Closes the broad E0-E6 relation-class encoding comparison, selects E5 Hue + Tag as the current relation-class visual carrier, preserves stroke rhythm as a future semantic resource, and opens a narrow human verification of slightly taller semantic tags.  
**Authority:** Current Phase-C routing boundary. The final ADS relation taxonomy remains unfrozen.

## 1. Human decision

The project owner selected:

```text
E5 Hue + Tag
    preferred
    clean
    current relation-class baseline
```

The project owner also liked E6 stroke rhythm but explicitly preferred not to use it redundantly for relation class.

Therefore:

```text
Hue + Tag
    selected for relation class

Stroke rhythm
    preserved for possible future meaning
    no semantic assignment yet
```

## 2. Small visual refinement

The tag labels appeared slightly too horizontally stretched.

Applied refinement:

```text
tag height       17 -> 20 SVG units
corner radius    5 -> 6
text size        7.0 -> 7.5 px
letter spacing   0.08em -> 0.05em
```

The width remains unchanged so the treatment becomes more naturally proportioned rather than simply larger.

## 3. Browser target

Browser route:

```text
frontend/design-lab/relation-class-grammar.html
frontend/design-lab/relation-class-grammar.css
frontend/design-lab/relation-class-grammar.js
```

Local URL:

```text
http://localhost:5173/design-lab/relation-class-grammar.html
```

Exact refined browser implementation target:

```text
b3d23b10be611f41a4e55fc40a28ba83089b7196
```

The page now opens in E5 by default while retaining E0-E6 as inspectable historical experiment controls.

## 4. Preserved evidence

Primary research:

```text
docs/research/057_semantic_relation_class_visual_grammar_experiment.md
docs/research/058_relation_class_hue_tag_selection_and_stroke_channel_reservation.md
```

Directionality remains sufficiently settled from the preceding slice:

```text
undirected      no arrow
forward         arrow at target
reverse         arrow at source
bidirectional   arrows at both endpoints
```

Connector terminal treatment and hover behavior remain separate mechanisms under Foundation 024.

## 5. Current human gate

```text
refresh relation-class-grammar.html
verify E5 opens by default
verify the taller tags feel more naturally proportioned
verify Hue + Tag remains clean
```

If accepted, relation-class visual encoding is sufficiently converged for the current design phase.

## 6. Important non-decisions

Still open:

```text
final ADS relation taxonomy
final relation-class codes / labels
production relation colors
semantic zoom behavior for relation tags
large-project label-density management
semantic assignment of stroke rhythm
runtime-flow connector semantics
production settings persistence
```

No production `/cockpit` file changed.

The permanent source-vault bootstrap remains paused and the Course 2 gate remains unchanged.
