# Checkpoint 231: Disposition Hybrid Refined, Mixed-Category Comparison Opened

**Date:** 2026-08-27  
**Branch:** `v1-cockpit-design-exploration`  
**Status:** Phase-C human browser review open

## Preserved human decision

The project owner reviewed the first project-disposition browser and requested:

```text
remove rhythm from P6 Hybrid
add a colored-tag + tone candidate without disposition perimeter hue
show both candidates in a practical mixed-category scene
```

This is a convergence refinement, not a restart of the disposition slice.

## Refined active comparison

```text
P6  Hue + Colored Tag + Tone
    disposition perimeter hue
    colored state tag
    selective tone
    no rhythm

P7  Colored Tag + Tone
    no disposition perimeter hue
    colored state tag
    selective tone
    no rhythm
```

P4 State Rhythm remains preserved as standalone experiment evidence.

## Practical mixed-category gate

The same small project scene is rendered twice with:

```text
Question / Blocker
Investigation
Validation / Analysis
Model Work
Evaluation
```

across representative Blocked, Active, Recommended, Completed, Deferred and Future dispositions.

The goal is to determine whether P6 becomes semantically or visually confusing when category hue and disposition hue coexist, and whether P7 is cleaner without losing enough disposition clarity to matter.

## Browser route

```text
http://localhost:5173/design-lab/work-unit-disposition-grammar.html
```

Exact browser implementation target:

```text
2056bb31d7cb90766e112bc26aaf7339fb568242
```

Research:

```text
docs/research/060_disposition_hybrid_refinement_and_mixed_category_practical_comparison.md
```

## Current human gate

```text
compare P6 vs P7 in controlled rows
+
compare P6 vs P7 in practical mixed-category scenes
-> prefer / reject / combine / refine
```

No final disposition ontology is frozen.

No production `/cockpit` file changed.
