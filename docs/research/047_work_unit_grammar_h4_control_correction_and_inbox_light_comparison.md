# Research 047: Work-Unit Grammar H4 Control Correction and In-Box Light Comparison

**Date:** 2026-08-26  
**Status:** Active Phase-C product-design evidence  
**Scope:** Corrects accidental H4 control drift in the work-unit grammar experiment, binds resting light to both the active category-signature edge and its position along that edge, and opens an explicit optional comparison between the accepted H4 in-box resting light and an intentionally reduced in-box-light treatment.  
**Authority:** Research/design evidence only. Specification 008 remains the promoted V1 Cockpit interaction architecture.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** chatgpt-08  
**Conversation title:** 08 - Project Cockpit Design Exploration

---

## 1. Human review trigger

The project owner reviewed the corrected Project Scene and identified two additional issues before Claude divergent ideation should begin.

First, the work-unit grammar implementation visually contained much less node-colored light inside the box than the previously accepted H4 treatment. This was not an intentional experiment, even though the page described H4 as a held control.

Second, the resting light remained left-biased even when a work-unit category signature moved to another edge, for example a top, bottom or right signature bar.

The project owner requested both defects be corrected and also requested that the lower-light appearance be preserved deliberately as an optional comparison rather than discarded as accidental implementation drift.

After the side-aware correction was reviewed positively, the project owner identified a further structural refinement: if the signature occupies only part of an edge, the light should follow that position too. A top-left signature should therefore produce top-left-biased light rather than light centered on the top edge.

---

## 2. Cause of the accidental in-box-light drift

The earlier H4 experiment used one work-unit element whose resting light and surface/background participated in the same visual stack.

The grammar experiment introduced an additional opaque-ish internal wrapper:

```text
.grammar-node
    -> external rest light / spill
    -> .node-surface
        -> content / frame signature / hover effects
```

The accepted H4 `rest-light` values were copied numerically, but the new `.node-surface` sat above that light and visually suppressed most of the colored illumination that had previously been visible inside the work-unit box.

Therefore:

```text
same nominal rest-light values
!=
same rendered H4 appearance
```

The implementation had preserved CSS numbers rather than the actual accepted visual control.

That is a design-experiment integrity defect.

---

## 3. Correct control rule

When a browser experiment declares an accepted mechanism as a control, later DOM or frame changes must preserve the accepted rendered behavior unless the control itself is explicitly reopened.

For this slice:

```text
DEFAULT
    accepted H4 in-box resting illumination
    accepted H4 outward resting spill
    accepted H4 hover response

NOT ALLOWED
    silent reduction of in-box light caused by new frame DOM
```

The grammar experiment restores a surface-local in-box light layer so the default treatment again visibly contains node-colored illumination inside the work unit.

---

## 4. Explicit reduced-light comparison

The accidentally quieter rendering is not automatically worthless. The project owner explicitly wants it available for comparison, but only as an intentional candidate.

The browser lab therefore exposes:

```text
IN-BOX LIGHT
    H4 baseline
        restored accepted in-box resting illumination

    Reduced
        intentionally near-dark / low-colour in-box resting treatment
```

Important experimental discipline:

```text
this control changes the in-box resting-light intensity only
```

The accepted outward resting spill remains present in both modes so the comparison does not silently reopen the already-settled world-spill amount at the same time.

The user may therefore compare whether the work-unit grammar looks better with:

```text
more visibly illuminated internal surfaces
vs
quieter almost-unlit internal surfaces
```

without confusing that question with category silhouette or outward-world spill.

No preference is recorded yet.

---

## 5. Signature edge and position lighting rule

The project owner established the structural visual rule:

> Signature-anchored resting light should follow not only the edge containing the category color/signature bar, but also the bar's position along that edge.

Therefore the light source is not globally hard-coded to the left edge or to the center of whichever edge is active.

For grammar variants that expose a category signature:

```text
left signature
    light exits through the left edge
    vertical light position follows the signature position

right signature
    light exits through the right edge
    vertical light position follows the signature position

top signature
    light exits through the top edge
    horizontal light position follows the signature position

bottom signature
    light exits through the bottom edge
    horizontal light position follows the signature position
```

This makes the light feel emitted by or structurally anchored to the actual category signature rather than pasted onto every work unit independently of its frame grammar.

Current first-round edge mapping:

```text
W1
    all categories left

W2
    Question        left
    Investigation   left
    Validation      top
    Model           bottom
    Evaluation      right

W3
    no explicit signature bar
    retain accepted left-biased H4 baseline for now

W4
    Question        left
    Investigation   left
    Validation      top
    Model           bottom
    Evaluation      right
```

The authored W2/W4 top and bottom signatures are intentionally left-biased. Their light anchor therefore uses the actual center of the bar geometry rather than `50%`:

```text
W2 Validation
    signature: left 14px; width 46%
    light anchor: calc(14px + 23%)

W2 Model
    signature: left 14px; width 50%
    light anchor: calc(14px + 25%)

W4 Validation
    signature: left 12px; width 42%
    light anchor: calc(12px + 21%)

W4 Model
    signature: left 12px; width 46%
    light anchor: calc(12px + 23%)
```

Full or centered vertical signatures retain a 50% along-edge anchor.

W3 may later gain a different structural-light anchor only if the silhouette design itself justifies one. This correction does not invent an additional W3 category signal.

---

## 6. Implementation evidence

Updated browser-design surface:

```text
frontend/design-lab/work-unit-grammar.html
frontend/design-lab/work-unit-grammar.js
frontend/design-lab/work-unit-grammar-lighting-controls.css
```

The lighting stylesheet is deliberately isolated because this is still a Phase-C design experiment and the correction/comparison should remain inspectable and rewrite-friendly.

Implementation changes now include:

```text
1. add a surface-local resting-light layer inside `.node-surface`
2. H4 baseline is the default in-box-light mode
3. add explicit H4 baseline / Reduced segmented control
4. assign each node a structural light side
5. assign each node an along-edge light anchor derived from frame-signature geometry
6. mirror/rotate near-node rest light and outward spill for right/top/bottom signatures
7. translate those resting layers along the active edge to the exact signature anchor
8. preserve accepted H4 hover timing and effects
9. preserve G4 world and production boundary
```

The exact browser commit containing the latest signature-position refinement is:

```text
304db34d6482320b317db97277148bc129d07372
```

Relative to the immediately preceding branch head `3228f7570c3c54d1d4348c7c77df0a9addc11c7a`, only the grammar JavaScript and lighting-control stylesheet changed.

No production `/cockpit` file changed.

---

## 7. Claude divergent-ideation implication

Claude should not review an earlier target that contains either the accidental-lighting drift or the side-only signature coupling as if those were the intended final controls.

The current corrected browser target should be used for MC-0004 divergent ideation:

```text
304db34d6482320b317db97277148bc129d07372
```

Claude is invited to comment on the explicit in-box-light comparison if it has useful design reasoning, but the main Claude task remains broad work-unit category-grammar ideation.

Claude should also preserve the structural rule that if a proposed category grammar relocates a visible signature/accent, signature-anchored resting light should relocate coherently with both its edge and position unless Claude explicitly argues for a different relationship.

---

## 8. Human evaluation questions

Before freezing either in-box-light treatment:

```text
Does restored H4 baseline feel richer and more integrated?
Does Reduced feel cleaner or merely underlit?
Does either intensity interfere with category recognition?
Does light correctly follow left/right/top/bottom signature placement?
For partial top/bottom signatures, does the light now sit under the actual bar rather than the edge center?
Does the outward spill still feel like the accepted H4 world integration?
Does hover remain clearly richer than rest in both in-box modes?
```

The answer may later vary by broader integrated visual grammar, but no per-category light-intensity semantics are implied by this comparison.

---

## 9. Current interpretation

The work-unit grammar slice now has two explicit dimensions:

```text
PRIMARY
    category / silhouette / frame grammar

SECONDARY CONTROLLED COMPARISON
    accepted H4 in-box resting light vs intentionally reduced in-box light
```

The signature-light rule is a structural consistency constraint within the primary grammar experiment, not a separate semantic axis:

```text
signature location
    -> resting light source location
```

This does not reopen generic H4 hover or outward-world spill tuning.

The corrected browser target is ready for human inspection and then Claude divergent ideation.
