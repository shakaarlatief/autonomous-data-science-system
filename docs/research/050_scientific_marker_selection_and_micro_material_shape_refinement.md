# Research 050: Scientific Marker Selection and Micro-Material / Validation-Shape Refinement

**Date:** 2026-08-26  
**Status:** Active Phase-C product-design evidence  
**Scope:** Preserves the next human review of the focused work-unit grammar round and records the corresponding browser refinement.  
**Authority:** Research/design evidence only. No production Cockpit grammar is promoted.

## Human decisions

The project owner selected the simple scientific marker family as the work-unit category-mark direction for the current slice:

```text
Question        circle
Investigation   square
Validation      triangle
Model           diamond
Evaluation      plus
```

This supersedes continued active comparison against the G1 instrument-glyph family in the focused browser round. Historical G1 evidence remains preserved.

Reduced in-box resting light remains the preferred working control.

## Micro-material refinement

The M1 material family remains positively reviewed, but visibility was uneven.

Human observation:

```text
Question / yellow diagonal treatment      clearly visible / good
Investigation / green dots                too quiet
Validation / blue line treatment          too quiet
Model / red grid/stripe treatment         too quiet
Evaluation / luminous diagonal treatment  good
```

The refinement therefore selectively increases only the quieter Investigation, Validation and Model treatments rather than globally increasing the whole material layer.

Implementation:

```text
Investigation
    stronger dot contrast
    slightly denser 6 px lattice

Validation
    stronger horizontal line contrast
    slightly denser 7 px spacing

Model
    stronger red grid lines
    slightly denser 11 px lattice

Question / Evaluation
    retained as-is
```

The objective is better parity of category visibility while remaining subtle and premium.

## Validation true-shape refinement

The project owner liked the true-shape direction overall but judged the Validation silhouette too aggressive because it removed material from two areas of the top edge, including the upper-left reading corner.

Human requirement:

```text
keep the Validation shape subtle
preserve the upper-left corner
preserve the left reading edge
retain only a right-side structural change
```

The Validation silhouette is therefore changed from a centered raised-tab form to a restrained right-side top step:

```text
full top-left entry edge
flat top through 72% width
small 7 px downward step on the right portion only
```

This keeps category-specific shape identity while respecting the emerging evidence that upper-left disruption is visually awkward.

## Browser implementation

Active route:

```text
frontend/design-lab/work-unit-grammar-focused.html
frontend/design-lab/work-unit-grammar-focused.css
frontend/design-lab/work-unit-grammar-focused-refinement.css
frontend/design-lab/work-unit-grammar-focused.js
```

Local URL:

```text
http://localhost:5173/design-lab/work-unit-grammar-focused.html
```

Exact browser implementation target after this refinement:

```text
6f27ae22dd47c3a395c6c8462ba325e1ebb19a2a
```

The new refinement stylesheet intentionally overrides only the reviewed dimensions and retires F7 from active presentation while preserving its historical implementation in the underlying experiment code.

## Current interpretation

```text
scientific markers          SELECTED for current grammar direction
Reduced in-box light        SELECTED preferred working control
M1 micro-material           KEEP / refine
true-shape family           KEEP / refine
Validation original shape   REJECTED as too aggressive
Validation right-step       OPEN for human verification
G1 instrument comparator    RETIRED from active focused review
```

No production `/cockpit` file is changed.
