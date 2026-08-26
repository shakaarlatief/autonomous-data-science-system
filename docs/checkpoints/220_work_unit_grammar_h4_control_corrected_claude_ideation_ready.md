# Checkpoint 220: Work-Unit Grammar H4 Control Corrected, Claude Ideation Ready

**Date:** 2026-08-26  
**Status:** Current product-design checkpoint  
**Checkpoint class:** CONTINUITY / PRODUCT_DESIGN / COLLABORATION  
**Project stage:** V1 next-generation Project Cockpit browser-rendered design exploration  
**Scope:** Records correction of accidental H4 in-box-light drift in the work-unit grammar browser experiment, signature-side-aware resting lighting, and an explicit H4-baseline versus reduced in-box-light comparison before Claude divergent ideation.  
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

The lab now exposes:

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

Therefore the lower-light idea is now a real controlled candidate instead of accidental implementation drift.

## 4. Signature-side-aware light

For variants with an explicit category signature bar, resting light now follows that edge.

Current mapping:

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

The implementation mirrors or rotates:

```text
in-box surface light
near-node rest light
outward resting spill
```

so the light remains structurally attached to the frame grammar.

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

A small follow-up hardening change scopes the in-box-light control query to the two buttons rather than the root `data-inbox-light` attribute. This does not change the intended visual behavior but removes an unnecessary root-element event listener before the Claude target is frozen.

No production Cockpit file changed.

## 6. Corrected Claude review target

Claude has not yet been triggered for Message 003.

The earlier exact targets are superseded because they either contained the accidental H4 control drift or preceded the final control-query hardening.

The corrected browser-design target is:

```text
7843bdd6c7a7fcb2f6136b491846c11cec094cf0
```

That commit contains the complete corrected browser state:

```text
Project Scene fix
restored H4 baseline in-box layer
explicit H4 baseline / Reduced control
signature-side-aware light mapping
lighting correction stylesheet
scoped in-box-light button controller
```

Later documentation/routing commits do not alter that exact browser target.

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
signature-edge / light-source coupling
```

but should not allow those secondary questions to replace the main category-grammar ideation task.

## 8. Exact continuation

```text
1. pull v1-cockpit-design-exploration
2. refresh http://localhost:5173/design-lab/work-unit-grammar.html
3. verify Project Scene still switches cleanly
4. compare H4 baseline vs Reduced in-box light
5. verify W2/W4 top/bottom/right signatures move their resting light accordingly
6. if browser rendering is correct, trigger Claude using REVIEW_INBOX.md
7. Claude reviews exact target 7843bdd6c7a7fcb2f6136b491846c11cec094cf0
8. Claude writes only the next MC-0004 numbered message
9. ChatGPT synthesizes all worthwhile candidates and builds as many browser variants as evidence justifies
10. production /cockpit remains untouched
```
