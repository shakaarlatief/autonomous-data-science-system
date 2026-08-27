# Research 060: Disposition Hybrid Refinement and Mixed-Category Practical Comparison

**Date:** 2026-08-27  
**Status:** Active Phase-C product-design evidence  
**Scope:** Refines the project-disposition candidates after first human review and adds a practical mixed-category comparison so category identity and disposition treatment can be judged together.  
**Authority:** Research/design evidence only. The disposition fixtures remain provisional and do not freeze the final ADS project-state ontology.

## 1. Human review input

The project owner requested three concrete changes to the first disposition browser:

```text
P6 Hybrid
    remove state rhythm

new candidate
    colored disposition tag + tonal hierarchy
    no disposition-colored outer perimeter

practical comparison
    show both refined candidates with multiple work-unit categories
    judge whether category and disposition become confusing together
```

The request explicitly preserves rhythm as experiment evidence while removing it from the integrated P6 candidate.

## 2. Refined candidates

The active convergence comparison is now:

```text
P6  Hue + Colored Tag + Tone
    disposition-colored outer perimeter
    colored disposition tag
    selective tonal reduction for Completed / Deferred / Future
    NO state rhythm

P7  Colored Tag + Tone
    category perimeter remains visually dominant
    colored disposition tag
    same selective tonal reduction
    NO disposition-colored outer perimeter
    NO state rhythm
```

P4 State Rhythm remains available in the controlled comparison as historical design evidence, but it is no longer part of P6.

## 3. Why the practical comparison matters

The first browser deliberately repeated one Investigation category across every state. That isolates disposition cleanly, but it cannot answer whether a second color system becomes confusing when real category variation returns.

The new practical comparison therefore renders the same small project fixture twice:

```text
left scene
    P6 Hue + Colored Tag + Tone

right scene
    P7 Colored Tag + Tone
```

Both scenes contain multiple category identities:

```text
Question / Blocker
Investigation
Validation / Analysis
Model Work
Evaluation
```

and multiple disposition states:

```text
Blocked
Active
Recommended
Completed
Deferred
Future
```

The fixture intentionally includes a repeated Investigation category in two different dispositions so the reviewer can see whether category identity remains stable while disposition changes.

## 4. Held controls

The practical comparison keeps constant:

```text
scientific category markers
category-specific category hues
subtle shape family
M1 micro-material treatment
Reduced in-box resting light
accepted H4 hover behavior
same project fixture and node placement
same connector topology
runtime state absent
importance held constant
```

The only deliberate difference between the two practical scenes is whether disposition hue also appears as an outer perimeter.

## 5. Connector implementation in practical scenes

The practical scenes use dynamically calculated connector geometry rather than fixed visual paths.

This preserves the already-established Cockpit rule:

```text
rendered work-unit geometry is authoritative
connector endpoints follow the rendered boxes
hover lift must not visually detach the relation
```

The practical connectors are neutral because relation class is not the variable under test in this slice.

## 6. Browser implementation

Files:

```text
frontend/design-lab/work-unit-disposition-grammar.html
frontend/design-lab/work-unit-disposition-grammar.css
frontend/design-lab/work-unit-disposition-grammar.js
```

Local URL:

```text
http://localhost:5173/design-lab/work-unit-disposition-grammar.html
```

Exact refined browser implementation target:

```text
2056bb31d7cb90766e112bc26aaf7339fb568242
```

## 7. Human review gate

The next review should answer:

```text
Does P6's second perimeter hue materially improve disposition recognition?
Does that perimeter hue compete with category hue once multiple categories coexist?
Does P7 preserve category identity more cleanly while the colored tag remains explicit enough?
Does selective tone communicate lifecycle position without implying low importance or disabled state?
Which of P6 vs P7 remains clearer and calmer in the practical mixed-category scene?
```

The human does not need to settle the final disposition ontology yet.

## 8. Production boundary

No production `/cockpit` file changed.

No final disposition ontology is promoted.

No runtime-state grammar is selected.

No priority/importance grammar is selected.

P4 rhythm remains preserved as design evidence rather than silently discarded.
