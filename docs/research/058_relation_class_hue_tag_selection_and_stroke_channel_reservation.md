# Research 058: Relation-Class Hue + Tag Selection and Stroke-Channel Reservation

**Date:** 2026-08-27  
**Status:** Active Phase-C product-design evidence  
**Scope:** Preserves the human selection of E5 Hue + Tag for relation-class meaning, retains E6 stroke rhythm as a promising future semantic channel rather than discarding it, and records a small tag-proportion refinement.  
**Authority:** Research/design evidence. The selected visual carrier is stronger evidence than the provisional relation-class fixture taxonomy, which remains unfrozen.

## 1. Human review result

The project owner reviewed the semantic relation-class browser and judged E5 positively:

```text
E5 Hue + Tag
    very clean
    selected for relation-class meaning
```

The project owner also judged the E6 stroke rhythms visually strong, but did not want stroke rhythm to redundantly encode the same relation-class meaning once E5 already communicates it cleanly.

Therefore:

```text
RELATION CLASS
    selected visual carrier = Hue + Tag

STROKE RHYTHM
    preserved
    not rejected
    not assigned to relation class
    reserved as a candidate channel for another future line-level semantic dimension
```

This is an information-design separation, not merely an aesthetic preference.

## 2. Selected relation-class grammar

The current relation-class treatment is:

```text
relation-specific restrained hue
+
compact explicit semantic tag
+
existing semantic direction arrow where direction requires it
```

The tag provides explicit semantic certainty while hue provides rapid visual grouping.

This avoids requiring users to memorize a dash vocabulary for relation class.

## 3. Stroke rhythm remains valuable

The stroke patterns tested in E2/E4/E6 remain preserved in the design lab and in Research 057.

Possible future uses may include a different semantic dimension such as:

```text
provisional vs confirmed relation
confidence / certainty family
runtime vs structural relationship
manual vs inferred relationship
other line-level semantics discovered later
```

These examples are hypotheses only. No meaning is assigned yet.

The important preservation rule is:

```text
stroke rhythm is a reusable visual resource
not dead design work
not currently relation-class semantics
```

Any later assignment must earn its meaning through a separate bounded experiment.

## 4. Small tag-proportion refinement

Human review identified one small visual issue: the all-caps tag words appeared slightly horizontally stretched / vertically compressed.

The refinement deliberately changes proportions without redesigning the selected E5 mechanism:

```text
tag background
    width       48 SVG units, unchanged
    height      17 -> 20 SVG units
    radius      5 -> 6

semantic tag text
    font size   7.0 -> 7.5 px
    tracking    0.08em -> 0.05em
```

The tag is therefore slightly taller while preserving almost the same horizontal footprint and overall compactness.

## 5. Browser behavior

The relation-class page now opens directly in E5 rather than the neutral E0 control.

Historical E0-E6 controls remain inspectable because they are useful experiment evidence, but the page labels E5 as the current selected baseline.

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

## 6. What is selected vs still open

Selected for the current design phase:

```text
relation-class visual carrier
    Hue + Tag

stroke rhythm
    retained as a future semantic-channel candidate
```

Still deliberately open:

```text
final ADS relation taxonomy
final relation-class names and codes
exact production relation colors
whether tags show at every semantic zoom level
whether tags can collapse under large-project density
what semantic dimension, if any, eventually uses stroke rhythm
runtime-flow connector grammar
production persistence / user settings
```

## 7. Current gate

Human verification is now narrow:

```text
refresh relation-class-grammar.html
verify E5 opens by default
verify tags feel better proportioned vertically
verify the selected hue + tag treatment remains clean
```

After that verification, relation-class visual encoding is sufficiently converged to move to the next Cockpit design question.

No production `/cockpit` file changed.
