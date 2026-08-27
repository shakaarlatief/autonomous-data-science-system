# Checkpoint 232: Disposition Neutral-Tag + Tone Refinement Review Opened

**Date:** 2026-08-27  
**Branch:** `v1-cockpit-design-exploration`  
**Status:** Phase-C human browser verification open

## Preserved human evidence

The project owner reviewed the mixed-category P6/P7 practical comparison and found both persistent-color variants somewhat confusing.

Selected refinement direction:

```text
project disposition
    tag + tone

resting tag
    neutral

hover
    tag reveals disposition color
```

Persistent disposition perimeter hue and persistent colored disposition tags are therefore not part of the current convergence candidate.

## Current convergence candidate

```text
P7  Neutral Tag + Tone

REST
    category color remains dominant
    neutral explicit disposition tag
    selective tone for Completed / Deferred / Future

HOVER
    disposition tag becomes state-colored
```

P4 rhythm and P6 colored hybrid remain preserved as comparison/history evidence.

## Browser route

```text
http://localhost:5173/design-lab/work-unit-disposition-grammar.html
```

Exact browser implementation target:

```text
fac1db37af4225927d6c799e37418a3ad9c42c13
```

Research:

```text
docs/research/061_project_disposition_neutral_tag_tone_convergence_refinement.md
```

## Current human gate

```text
verify P7 rests neutral
verify P7 tag reveals state hue on hover
verify mixed-category scene is less confusing
verify tone does not imply low importance / disabled state
-> if accepted, treat project-disposition visual carrier as sufficiently converged for current Phase C
```

No final project-disposition ontology is frozen.

No production `/cockpit` file changed.
