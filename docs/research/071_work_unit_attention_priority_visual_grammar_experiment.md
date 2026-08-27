# Research 071: Work-Unit Attention Priority Visual Grammar Experiment

**Date:** 2026-08-27  
**Status:** Human-selected current Phase-C direction  
**Scope:** Bounded visual grammar experiment for elevated attention priority after the shared operational-status carrier and blocker-to-blocked relationship model received positive human review.  
**Authority:** Research evidence only. A3 Signal Bars are selected as the current Phase-C visual treatment, but this memo does not freeze a priority ontology, relevance score, scheduling policy, ranking algorithm, ownership model, persistence model or final production carrier.

## 1. Boundary transition from BLOCKED

Checkpoint 238 converged the BLOCKED/progress-constraint presentation to:

```text
BLOCKER
    cause / unresolved work or dependency preventing progress

BLOCKS
    relationship from blocker cause to affected work

BLOCKED
    current progress constraint on affected work

FAIL
    failed current execution attempt
```

The visual presentation uses one bottom-right operational-status slot that may present either live runtime or BLOCKED without merging the underlying semantics.

Accepted compact red mapping:

```text
BLOCKED    sharper non-circular dynamic ring
FAIL       smoother circular dynamic ring
```

Exact accepted BLOCKED/status target:

```text
88fd3c3cfe7a1eff4664afde06341b7b654c97f4
```

## 2. Bounded attention-priority concept

The experiment isolated:

```text
ATTENTION PRIORITY
    among visible work, which work deserves more attention now?
```

This was deliberately separated from:

```text
category
project disposition
progress constraint
runtime / operational status
current-process focus membership
```

The experiment did not assume:

```text
priority == relevance
priority == scheduling order
priority == current-focus membership
priority == operational urgency
```

Those relationships remain future semantic questions.

## 3. Controlled fixture

Every controlled row held:

```text
category       Investigation
disposition    Current
status         RUN
priority       HIGH
```

`HIGH` was a provisional binary test fixture only.

## 4. Held controls

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

## 5. Browser evidence

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

Exact browser implementation reviewed by the project owner:

```text
767c66f76974d3c0a851de0dfa17c502817a4b12
```

Production `/cockpit` remained untouched.

## 6. Candidate priority carriers

```text
A0  Neutral Control
A1  Twin Tick
A2  Top Rail
A3  Signal Bars
A4  Side Bracket
A5  HIGH Tag
A6  Beacon
A7  Luminance Lift
A8  Rail + Tag
```

### A0 Neutral Control
No priority-specific cue. Baseline.

### A1 Twin Tick
Two tiny vertical ticks centered above the upper frame.

### A2 Top Rail
Short restrained highlight rail centered on the upper frame.

### A3 Signal Bars
Three ascending micro-bars near the upper-right frame but separated from the disposition badge. The ascending geometry has possible future ordinal potential, but no scale is implied or frozen.

### A4 Side Bracket
Slim bracket gripping the right-middle edge.

### A5 HIGH Tag
Small explicit HIGH tag at bottom-left, maximizing explicitness while increasing label density.

### A6 Beacon
Small hollow diamond above the frame, deliberately testing possible confusion with connector ports.

### A7 Luminance Lift
Slightly brighter surface / outline with no dedicated marker, deliberately testing possible collapse into hover/focus/resting-light language.

### A8 Rail + Tag
A2 structural rail plus A5 explicit HIGH tag, testing restrained redundancy.

## 7. Practical coexistence fixture

```text
Question / Blocker    CURRENT + HUMAN      HIGH
Investigation         CURRENT + BLOCKED    HIGH
Validation            NEXT + NONE          normal
Model Work            CURRENT + FAIL       HIGH
Investigation         CURRENT + RUN        normal
Evaluation            DEFER + NONE         normal
```

The yellow Question / Blocker category deliberately tested whether the provisional warm attention tone could remain distinguishable from category color through geometry and placement.

## 8. Human selection

The project owner reviewed the candidates and responded:

```text
I choose A3. Perfect. Proceed.
```

Selected current Phase-C visual direction:

```text
A3  Signal Bars

HIGH attention
    three ascending micro-bars
    near the upper-right frame
    structural rather than textual
    spatially separated from disposition and bottom-right operational status
```

This closes the visual carrier comparison for the current Phase-C round.

It does **not** establish that the final product should use a binary HIGH/normal model or that the number/height of bars should encode an ordinal scale. Those remain hypotheses requiring separate evidence.

## 9. Why A3 is useful evidence

The selection supports several design observations:

```text
structural micro-signals can carry persistent node-level meaning without another textual badge

attention priority can remain visually independent from category hue

upper-frame geometry can coexist with top-right disposition and bottom-right operational status

selection should not rely on broad luminance or suppression because those channels already have other jobs
```

The final production tone, exact dimensions and semantic scale remain unfrozen.

## 10. Work-unit detail expansion remains deferred

The preserved interaction hierarchy remains:

```text
compact map work unit
    -> expanded contextual/detail card
    -> full specialist workspace / deep focus
```

The next slice first tests persistent selection, because the Cockpit needs a stable selected-object state before an expanded detail interaction can be designed cleanly.

## 11. Still unfrozen

```text
final priority / attention ontology
whether attention priority is binary, ordinal or scored
relationship between priority and relevance
relationship between priority and scheduling
who owns priority: ADS, human, or both
priority provenance and override rules
priority persistence
production attention color
semantic zoom behavior for priority
large-project priority density
final current-focus interaction with priority
```
