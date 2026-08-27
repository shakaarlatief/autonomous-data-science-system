# Research 071: Work-Unit Attention Priority Visual Grammar Experiment

**Date:** 2026-08-27  
**Status:** Active Phase-C semantic/visual experiment  
**Scope:** Opens a bounded visual grammar experiment for elevated attention priority after the shared operational-status carrier and blocker-to-blocked relationship model received positive human review.  
**Authority:** Research evidence only. This memo does not freeze a priority ontology, relevance score, scheduling policy, ranking algorithm, production carrier, or final Cockpit design system.

## 1. Boundary transition from BLOCKED

Checkpoint 238 explored whether `Blocked` should be a separate progress-constraint concept and how it should coexist with runtime and project disposition.

Human review converged on the following current Phase-C interpretation:

```text
BLOCKER
    cause / unresolved work or dependency preventing progress

BLOCKS
    relationship from blocker cause to affected work

BLOCKED
    current progress constraint on the affected work unit

FAIL
    failed current execution attempt
```

The visual presentation was simplified to one bottom-right operational-status slot that may present either a live runtime state or BLOCKED without claiming those concepts are the same model field.

Accepted appearance direction:

```text
Dot mode
    compact status dot + dynamic ring

Tag mode
    T7 Soft Shade explicit status tag

BLOCKED dot
    sharper red non-circular constraint ring

FAIL dot
    smoother circular red operational ring
```

The project owner explicitly accepted the final ring swap and responded:

```text
Perfect. Proceed.
```

Exact accepted BLOCKED/status browser visual target:

```text
88fd3c3cfe7a1eff4664afde06341b7b654c97f4
```

Research evidence:

```text
docs/research/069_blocked_as_orthogonal_progress_constraint_visual_grammar_experiment.md
docs/research/070_shared_operational_status_carrier_blocker_relationship_and_work_unit_detail_deferment.md
```

The final progress-constraint ontology and state-transition rules remain unfrozen.

## 2. Why attention priority is the next bounded question

Several node-level semantic channels are now sufficiently separated to expose the remaining problem:

```text
CATEGORY
    what is this work unit?

PROJECT DISPOSITION
    where does it stand in the project?

PROGRESS CONSTRAINT
    can it proceed?

RUNTIME
    if a meaningful current episode exists, what is happening?

CURRENT-FOCUS MEMBERSHIP
    is it in the emphasized process set?
```

A different question remains:

```text
ATTENTION PRIORITY
    among visible work, which work deserves more attention now?
```

This is deliberately narrower than the earlier shorthand `importance / priority / relevance`.

The current slice does **not** assume that:

```text
priority == relevance
priority == scheduling order
priority == current-focus membership
priority == project disposition
priority == runtime urgency
```

Those relationships require later semantic evidence.

## 3. Controlled semantic fixture

The controlled rows hold constant:

```text
category       Investigation
disposition    Current
status         RUN
priority       HIGH
```

Only the priority carrier changes.

`HIGH` is a provisional binary test fixture, not a frozen priority scale.

The experiment intentionally avoids committing to values such as:

```text
low
medium
high
critical
P0/P1/P2
numeric score
```

until a visual carrier and product meaning have earned further work.

## 4. Held controls

The experiment preserves:

```text
G4 Adaptive Hybrid world
H4 hover/world response
Reduced in-box resting light
scientific category markers
P7 Neutral Tag + Tone disposition
accepted operational-status dot/ring grammar
BLOCKED sharper ring
FAIL smoother circular ring
category hue remains category-owned
```

The accepted soft-shade status-tag alternative remains preserved, but the practical priority scene holds operational status to compact dot mode so the priority comparison changes one major visual variable at a time.

## 5. Browser

Local route:

```text
http://localhost:5173/design-lab/work-unit-attention-priority.html
```

Files:

```text
frontend/design-lab/work-unit-attention-priority.html
frontend/design-lab/work-unit-attention-priority.css
frontend/design-lab/work-unit-attention-priority.js
```

Exact browser implementation target:

```text
767c66f76974d3c0a851de0dfa17c502817a4b12
```

Production `/cockpit` remains untouched.

## 6. Candidate priority carriers

Every candidate uses the same provisional champagne attention color so geometry/presentation can be compared without simultaneously changing hue.

### A0 Neutral Control

```text
no priority-specific cue
```

Purpose: baseline.

### A1 Twin Tick

```text
two tiny vertical ticks
centered just above the upper frame
```

Tests a compact learned structural marker.

### A2 Top Rail

```text
short restrained highlight rail
centered on the upper frame
```

Tests a clean structural emphasis channel spatially separated from disposition and operational status.

### A3 Signal Bars

```text
three ascending micro-bars
near the upper-right frame but separated from the disposition badge
```

Tests an instrument-like attention signal. The ascending geometry has possible future ordinal potential, but no priority scale is implied or frozen here.

### A4 Side Bracket

```text
slim bracket gripping the right-middle edge
```

Tests structural emphasis without text or broad recoloring.

### A5 HIGH Tag

```text
small explicit HIGH tag
bottom-left
```

Tests maximum semantic explicitness while deliberately increasing label density.

### A6 Beacon

```text
small hollow diamond above the frame
```

Tests a compact beacon. It may fail if it resembles a connector port or endpoint.

### A7 Luminance Lift

```text
slightly brighter surface / outline
no dedicated marker
```

This is an intentional falsification candidate because it may collapse into hover, focus, selection or resting-light language.

### A8 Rail + Tag

```text
A2 structural rail
+
A5 explicit HIGH tag
```

Tests whether restrained redundancy helps or simply duplicates meaning.

## 7. Practical coexistence fixture

The mixed scene contains:

```text
Question / Blocker    CURRENT + HUMAN      HIGH
Investigation         CURRENT + BLOCKED    HIGH
Validation            NEXT + NONE          normal
Model Work            CURRENT + FAIL       HIGH
Investigation         CURRENT + RUN        normal
Evaluation            DEFER + NONE         normal
```

This tests whether priority remains readable beside:

```text
category color
disposition tags
BLOCKED
FAIL
RUN
HUMAN
ordinary non-priority work
```

The yellow Question / Blocker category is particularly important because the provisional priority tone is warm. A good carrier must remain distinguishable by geometry and placement rather than relying on hue alone.

## 8. Priority versus current-focus membership

The accepted current-process focus lens answers:

```text
Is this work in the process set I am emphasizing?
```

Attention priority instead asks:

```text
Among work I can see, which work deserves more attention now?
```

Therefore a node can plausibly be:

```text
in current focus + normal priority
in current focus + high priority
outside current focus + high priority
```

The last combination may or may not be useful in the final product, but this experiment does not silently forbid it.

Priority should not be encoded by broad suppression because suppression already belongs to the current-process focus lens.

## 9. Current human gate

Review:

```text
1. compare A1-A8 against A0
2. judge which carrier makes HIGH attention visible without overpowering category/status
3. compare structural-only cues against explicit HIGH text
4. reject any treatment that resembles connector ports, hover, focus or status
5. inspect the yellow Question / Blocker example carefully
6. judge whether A8 redundancy is useful or cluttered
7. prefer / reject / combine / refine
```

## 10. Work-unit detail expansion remains deferred

The previously proposed interaction remains preserved:

```text
compact map work unit
    -> expanded contextual/detail card
    -> full specialist workspace / deep focus
```

It is not mixed into this priority slice because that would change information density, node geometry and interaction depth simultaneously.

It remains grouped with future semantic zoom, C5 Internal Layout Grammar, information-density and selected/focused-treatment work.

## 11. Still unfrozen

```text
final priority / attention ontology
whether attention priority is binary, ordinal or scored
relationship between priority and relevance
relationship between priority and scheduling
who owns priority: ADS, human, or both
priority provenance and override rules
priority persistence
production priority carrier
production attention color
semantic zoom behavior for priority
large-project priority density
final current-focus interaction with priority
final operational-status ontology
final progress-constraint ontology
final work-unit inline expansion behavior
```
