# Research 058: Relation-Class Hue + Tag Selection and Stroke-Channel Reservation

**Date:** 2026-08-27  
**Status:** Active Phase-C product-design evidence  
**Scope:** Preserves the human selection of E5 Hue + Tag for relation-class meaning, retains E6 stroke rhythm as a promising future semantic channel rather than discarding it, and records the iterative tag-proportion and spacing refinements.  
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

## 4. Tag-proportion and spacing refinement

Human review identified that the all-caps relation tag initially appeared too horizontally stretched / vertically compressed.

The refinement sequence intentionally preserved the selected E5 mechanism while improving proportion:

```text
initial tag
    width       48 SVG units
    height      17 SVG units
    radius      5
    font size   7.0 px
    tracking    0.08em

first refinement
    width       48, unchanged
    height      20
    radius      6
    font size   7.5 px
    tracking    0.05em

second refinement
    width       48, unchanged
    height      22
    radius      7

latest refinement
    font size   8.2 px
    tracking    0.05em
    tag center  raised farther above the connector line
```

The latest vertical-placement rule restores the small clean gap above the line that the project owner preferred in the original treatment, while keeping the newer taller tag body.

## 5. Browser behavior

The relation-class page opens directly in E5 rather than the neutral E0 control.

Historical E0-E6 controls remain inspectable because they are useful experiment evidence, but E5 is the current selected baseline.

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

Exact latest refined browser implementation target:

```text
497e81f06ba1f9901511449237d1bb9f96b2d108
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

Human verification remains narrow:

```text
refresh relation-class-grammar.html
verify E5 opens by default
verify the 22-unit tag body remains clean
verify the tag again sits clearly above, rather than on, the connector line
verify the slightly taller 8.2 px tag lettering looks more natural
```

After that verification, relation-class visual encoding is sufficiently converged to move to the next Cockpit design question.

No production `/cockpit` file changed.
