# Checkpoint 230: Relation-Class Encoding Settled, Project-Disposition Grammar Review Opened

**Date:** 2026-08-27  
**Active branch:** `v1-cockpit-design-exploration`  
**Active PR:** none  
**Thread:** MC-0004  
**Phase:** Phase C browser-rendered Project Cockpit design evaluation

## Why this checkpoint exists

The project owner accepted the final relation-class tag refinement and explicitly authorized progression:

```text
Perfect. Let's proceed.
```

That closes the narrow tag-refinement gate and makes E5 Hue + Tag sufficiently settled as the current relation-class visual carrier for this design phase.

The next natural unresolved work-unit question is project disposition.

## Preserved relation-class result

Current selected relation-class treatment:

```text
restrained relation-class hue
+
compact explicit semantic tag
+
existing edge-connected arrow when semantic direction requires it
```

Latest accepted browser implementation before opening the new slice:

```text
497e81f06ba1f9901511449237d1bb9f96b2d108
```

Stroke rhythm remains preserved as a future line-level semantic resource rather than being discarded or redundantly assigned to relation class.

The provisional relation fixtures remain unfrozen.

## New active slice

Research:

```text
docs/research/059_work_unit_project_disposition_visual_grammar_experiment.md
```

Browser:

```text
frontend/design-lab/work-unit-disposition-grammar.html
frontend/design-lab/work-unit-disposition-grammar.css
frontend/design-lab/work-unit-disposition-grammar.js
```

Local URL:

```text
http://localhost:5173/design-lab/work-unit-disposition-grammar.html
```

Exact browser implementation target:

```text
565fdeabc1ebaa29f993699a4c0673b29e972be3
```

## Semantic separation under test

The new slice explicitly preserves:

```text
WHAT IS THIS?
    category / kind

WHAT IS ITS PROJECT DISPOSITION?
    current slice

WHAT IS HAPPENING NOW?
    runtime, held out

HOW IMPORTANT IS IT NOW?
    priority / relevance, held out
```

This prevents visual state from becoming an ambiguous mixture of lifecycle, execution and importance.

## Representative disposition fixtures

```text
S0  Active / Current
S1  Recommended / Next
S2  Deferred
S3  Completed
S4  Blocked
S5  Future / Not yet active
```

These are browser fixtures only and do not freeze the final ADS state ontology.

## Encoding families

```text
P0  Neutral Control
P1  Disposition Hue
P2  Explicit Tag
P3  Tonal Hierarchy
P4  State Rhythm
P5  Hue + Tag
P6  Restrained Hybrid
```

Held controls include the selected scientific category marker, Subtle shape, M1 material, Reduced in-box light and H4 hover response.

## Current human gate

The next actor is the human project owner.

Review should focus on:

```text
state clarity
category-color interference
label density
tonality vs unintended priority implication
rhythm usefulness
combined-channel noise
```

No final state taxonomy must be selected in this gate.

## Production boundary

Only `frontend/design-lab/**` was changed for the executable experiment.

Production `/cockpit` remains untouched.

Specification 008 remains the promoted Project Cockpit interaction architecture.

Foundation 023 and Foundation 024 remain in force.

The source-vault bootstrap remains paused and Course 2 remains gated.
