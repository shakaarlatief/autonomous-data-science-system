# Checkpoint 220: Work-Unit Grammar H4 Control Corrected, Claude Ideation Ready

**Date:** 2026-08-26  
**Status:** Current product-design checkpoint  
**Checkpoint class:** CONTINUITY / PRODUCT_DESIGN / COLLABORATION  
**Project stage:** V1 next-generation Project Cockpit browser-rendered design exploration  
**Scope:** Records correction of accidental H4 in-box-light drift in the work-unit grammar browser experiment, signature-edge-and-position-aware resting lighting, and an explicit H4-baseline versus reduced in-box-light comparison before Claude divergent ideation.  
**Authority:** Current Phase-C routing/evidence boundary only. Specification 008 remains the promoted Cockpit interaction architecture.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** chatgpt-08  
**Conversation title:** 08 - Project Cockpit Design Exploration  
**Primary collaborator:** ChatGPT

## 1. Human review result

After the Project Scene switching defect was corrected, the project owner identified two additional issues:

```text
1. in-box resting light was materially weaker than the accepted H4 appearance
2. resting light/spill stayed left-biased even when the category signature bar moved to another edge
```

The project owner correctly noted that the first issue was not an intentional experiment despite H4 being described as a held control.

The project owner also requested that the quieter in-box appearance be retained intentionally as an explicit comparison candidate rather than simply removed.

After the first side-aware correction was reviewed positively, the project owner identified one more structural refinement before Claude should inspect the experiment:

```text
light must follow not only the signature edge
but also the signature's position along that edge
```

For example, a top signature that occupies the left portion of the top edge should produce a top-left-biased resting light rather than a top-centered light.

## 2. H4 control correction

Research 047 preserves the cause and correction.

The grammar DOM introduced a separate `.node-surface` above the copied H4 rest-light layer, suppressing much of the color previously visible inside the box.

The corrected rule is:

```text
accepted rendered H4 behavior is the control
not merely copied CSS numeric values
```

The browser experiment now includes a dedicated surface-local resting-light layer so `H4 baseline` restores visible node-colored illumination inside the work unit.

## 3. Intentional reduced in-box-light comparison

The lab exposes:

```text
In-box light
    H4 baseline   DEFAULT
    Reduced       INTENTIONAL ALTERNATIVE
```

This comparison changes only in-box resting-light intensity.

It does not intentionally change:

```text
outward resting world spill
hover halo
pointer hotspot
hover world light
connector hover emphasis
perimeter sweep
hover timing
```

Therefore the lower-light idea is a real controlled candidate instead of accidental implementation drift.

## 4. Signature-edge-and-position-aware light

For variants with an explicit category signature bar, resting light now follows both:

```text
1. which edge contains the signature
2. where the signature is located along that edge
```

Current edge mapping remains:

```text
W1
    all left

W2 / W4
    Question        left
    Investigation   left
    Validation      top
    Model           bottom
    Evaluation      right

W3
    no explicit signature bar
    retain accepted left-biased H4 baseline
```

The refinement is especially visible for W2/W4 Validation and Model signatures. Their top/bottom bars are left-biased rather than centered, so the light anchor now uses the actual center of those authored bar geometries.

Current exact anchor expressions are derived from the corresponding frame-signature CSS:

```text
W2 Validation   top     calc(14px + 23%)
W2 Model        bottom  calc(14px + 25%)
W4 Validation   top     calc(12px + 21%)
W4 Model        bottom  calc(12px + 23%)
```

Full/centered left/right signatures retain a `50%` along-edge anchor.

The implementation moves all three resting layers together:

```text
in-box surface light
near-node rest light
outward resting spill
```

so the light remains structurally attached to the actual frame signature rather than only its broad side.

## 5. Browser implementation

Current design-lab route:

```text
frontend/design-lab/work-unit-grammar.html
frontend/design-lab/work-unit-grammar.css
frontend/design-lab/work-unit-grammar-lighting-controls.css
frontend/design-lab/work-unit-grammar.js
```

Local URL:

```text
http://localhost:5173/design-lab/work-unit-grammar.html
```

The existing Project Scene explicit display suppression remains in place.

The in-box-light control query remains scoped to the two control buttons.

No production Cockpit file changed.

## 6. Corrected Claude review target

Claude has not yet been triggered for Message 003.

The previous corrected target is now superseded by the signature-position refinement because that refinement changes the rendered design Claude should inspect.

The current exact browser-design target is:

```text
304db34d6482320b317db97277148bc129d07372
```

Relative to the previous branch head `3228f7570c3c54d1d4348c7c77df0a9addc11c7a`, this refinement changed only:

```text
frontend/design-lab/work-unit-grammar.js
frontend/design-lab/work-unit-grammar-lighting-controls.css
```

The two commits are 2 ahead / 0 behind and do not touch production Cockpit files.

## 7. Claude task remains divergent ideation

The purpose of Claude's next contribution remains:

```text
broaden the work-unit category-grammar design space
challenge premature convergence
preserve all genuinely worthwhile candidates
use external inspiration where useful
```

Claude may additionally comment on:

```text
H4 baseline vs Reduced in-box resting light
signature-edge-and-position / light-source coupling
```

but should not allow those secondary questions to replace the main category-grammar ideation task.

## 8. Exact continuation

```text
1. pull v1-cockpit-design-exploration
2. refresh http://localhost:5173/design-lab/work-unit-grammar.html
3. verify Project Scene still switches cleanly
4. compare H4 baseline vs Reduced in-box light
5. inspect W2/W4 Validation and Model especially
6. verify their top/bottom light is biased toward the actual left-biased signature bar rather than centered
7. verify right/left signatures still behave correctly
8. if browser rendering is correct, trigger Claude using REVIEW_INBOX.md
9. Claude reviews exact visual target 304db34d6482320b317db97277148bc129d07372
10. Claude writes only the next MC-0004 numbered message
11. ChatGPT synthesizes all worthwhile candidates and builds as many browser variants as evidence justifies
12. production /cockpit remains untouched
```
