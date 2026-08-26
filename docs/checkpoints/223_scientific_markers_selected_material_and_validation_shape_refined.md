# Checkpoint 223: Scientific Markers Selected, Material and Validation Shape Refined

**Date:** 2026-08-26  
**Status:** Current product-design checkpoint  
**Checkpoint class:** CONTINUITY / PRODUCT_DESIGN  
**Project stage:** V1 next-generation Project Cockpit browser-rendered design exploration  
**Scope:** Records selection of the scientific marker vocabulary, retention/refinement of the M1 micro-material direction, refinement of the Validation true-shape silhouette, and opening of the next human verification gate.  
**Authority:** Current Phase-C routing/evidence boundary only. No production work-unit grammar is promoted. Specification 008 remains the promoted Cockpit interaction architecture.

## Human review

Selected:

```text
Scientific marker family
    Question        circle
    Investigation   square
    Validation      triangle
    Model           diamond
    Evaluation      plus
```

Retained:

```text
Reduced in-box light
M1 micro-material direction
true-shape family
Evaluation-like micro character
```

Retired from active focused comparison:

```text
G1 instrument glyph comparator
```

Historical evidence remains preserved.

## Micro-material correction

The project owner judged Question/yellow already clearly visible and attractive, but found the following too quiet:

```text
Investigation / green dots
Validation / blue lines
Model / red grid
```

These three treatments are now selectively strengthened. Question and Evaluation material treatments are intentionally unchanged.

## Validation shape correction

The previous Validation true-shape treatment removed too much of the upper edge and again disturbed the upper-left corner.

The revised shape now:

```text
preserves the complete left reading edge
preserves the upper-left corner
keeps the top edge intact through most of the card
uses only a subtle right-side 7 px top step
```

This directly follows the human requirement that all box shapes remain nice and subtle.

## Browser route

```text
http://localhost:5173/design-lab/work-unit-grammar-focused.html
```

Refinement stylesheet:

```text
frontend/design-lab/work-unit-grammar-focused-refinement.css
```

Exact browser implementation target:

```text
6f27ae22dd47c3a395c6c8462ba325e1ebb19a2a
```

## Current verification questions

```text
1. Are the green dots now clearly visible without becoming noisy?
2. Are the Validation lines now clearly visible without becoming heavy?
3. Is the red Model grid now comparable in salience to the yellow Question treatment?
4. Does the Evaluation treatment remain attractive after the parity changes?
5. Is the revised Validation silhouette now subtle and balanced?
6. Do the other true-shape silhouettes remain acceptable?
7. Do these judgments survive Project scene composition?
```

## Promotion audit

No production promotion.

The work-unit grammar remains under focused browser review. Final taxonomy, semantic colors, runtime/status axes, connector semantics and semantic zoom remain unresolved.

Production `/cockpit` remains untouched.

## Exact continuation

```text
1. pull v1-cockpit-design-exploration
2. refresh http://localhost:5173/design-lab/work-unit-grammar-focused.html
3. inspect F2 and F5 first for the refined M1 material visibility
4. inspect F4/F5/F6 Validation shape for the right-only top step
5. compare Category strip and Project scene
6. record whether material parity and Validation subtlety are now correct
7. continue convergence only from surviving mechanisms
```
