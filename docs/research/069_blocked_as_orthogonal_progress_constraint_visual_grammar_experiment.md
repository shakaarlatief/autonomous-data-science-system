# Research 069: BLOCKED as Orthogonal Progress Constraint Visual Grammar Experiment

**Date:** 2026-08-27  
**Status:** Active Phase-C semantic/visual experiment  
**Scope:** Opens a bounded Project Cockpit experiment for `BLOCKED` after the runtime slice showed that lifecycle/disposition, progress constraints and runtime should not be collapsed into one state axis.  
**Authority:** Research evidence only. This memo does not freeze the final ADS lifecycle ontology, progress-constraint ontology, runtime ontology, compatibility matrix, or production visual treatment.

## 1. Boundary transition from runtime

Checkpoint 237 and Research 068 now provide accepted Phase-C evidence for runtime presentation:

```text
runtime is conditional / episode-scoped

live runtime carrier
    exactly one per live-runtime work unit

carrier A
    Dot + dynamic ring

carrier B
    T7 Soft Shade runtime tag

switching
    global across live-runtime work units
    local per-work-unit override

No runtime
    no runtime carrier
```

The final runtime ontology and production preference/persistence model remain unfrozen, but the current visual carrier question is sufficiently converged to move on.

## 2. Semantic issue exposed by the runtime correction

The earlier disposition fixture included `Blocked` next to values such as:

```text
Current
Next
Deferred
Completed
Future
```

Human review of runtime semantics exposed that this may be the wrong axis.

The following combinations are coherent:

```text
Current + Blocked
Next + Blocked
```

This suggests a three-way separation:

```text
PROJECT DISPOSITION
    where does this work stand in the project?

PROGRESS CONSTRAINT
    can this work proceed?

RUNTIME
    if a meaningful current execution/work episode exists,
    what is happening in that episode?
```

This is a working semantic hypothesis, not a frozen ontology.

## 3. Critical distinctions under test

### Blocked versus Waiting runtime

```text
Blocked
    the work cannot proceed until a constraint is resolved
    a live runtime episode need not exist

WAIT runtime
    a current execution/work episode exists
    that episode is presently waiting for an external condition
```

Therefore:

```text
Current + Blocked + No runtime
```

and:

```text
Current + WAIT + Unblocked
```

must remain visibly and conceptually distinct.

### Question / Blocker category versus Blocked constraint

The current scientific category vocabulary includes:

```text
Question / Blocker
```

That category denotes **what a work unit is**. It may represent an unresolved question, approval, decision, or other blocking object that another work unit depends on.

`Blocked` instead denotes **a constraint on an affected work unit**.

Therefore this is valid:

```text
Question / Blocker work unit
    Current + HUMAN
    not itself Blocked

Investigation work unit
    Current + Blocked
    No runtime
```

The browser deliberately includes this contrast.

## 4. Held visual controls

The experiment keeps the following existing Phase-C directions constant:

```text
G4 world
H4 hover/world response
Reduced resting light
scientific category markers
P7 Neutral Tag + Tone for disposition
conditional runtime semantics
category hue remains category-owned
```

Runtime is shown only where useful for semantic contrast and is not itself being redesigned in this browser.

## 5. Browser

Local route:

```text
http://localhost:5173/design-lab/work-unit-progress-constraint.html
```

Files:

```text
frontend/design-lab/work-unit-progress-constraint.html
frontend/design-lab/work-unit-progress-constraint.css
frontend/design-lab/work-unit-progress-constraint.js
```

Exact browser implementation target:

```text
efd0d36ee4ccf4c5494220df54eb3e7f50995658
```

Production `/cockpit` remains untouched.

## 6. Controlled visual candidates

Every controlled row uses the same semantic fixture:

```text
category       Investigation
disposition    Current
constraint     Blocked
runtime        None
```

Only the blocked presentation changes.

### C0 Neutral Control

```text
no blocked-specific cue
```

Purpose: establish how much meaning is lost if the constraint exists only in underlying state.

### C1 Explicit Tag

```text
small red BLOCKED tag
category perimeter remains category-owned
```

Tests maximum explicitness with minimal structural change.

### C2 Edge Clamp

```text
small red clamp grips the right edge
no text
```

Tests whether blockage can read as a structural inability to proceed rather than another status label.

### C3 Stop Rail

```text
short red stopper rail interrupts the lower frame
no text
```

Tests a compact learned instrument cue.

### C4 Barrier Seal

```text
small edge-mounted red barrier seal
no text
```

Tests a discrete symbol-like structural marker without recoloring the node.

### C5 Constraint Veil

```text
subtle red diagonal veil / hatch across the node surface
```

This candidate is intentionally included as a falsification test because broad tonal treatment may be confused with:

```text
focus suppression
low priority
future/deferred recession
```

### C6 Tag + Clamp

```text
C1 explicit BLOCKED tag
+
C2 structural edge clamp
```

Tests whether a critical progress constraint benefits from restrained redundant signaling or whether it becomes duplicative.

## 7. Practical coexistence fixture

The practical scene contains:

```text
Question / Blocker
    CURRENT + HUMAN
    unblocked

Investigation
    CURRENT + BLOCKED + NONE

Validation
    NEXT + BLOCKED + NONE

Model Work
    CURRENT + RUN
    unblocked

Investigation
    CURRENT + WAIT
    unblocked

Evaluation
    DEFER + NONE
    unblocked

Investigation
    FUTURE + NONE
    unblocked
```

This scene is designed to answer semantic-confusion questions, not merely aesthetic ones.

In particular it tests whether the viewer can distinguish:

```text
Question / Blocker category
vs
Blocked constraint

Current + Blocked + None
vs
Current + WAIT

Next + Blocked
vs
Deferred / Future
```

## 8. Current human gate

Review:

```text
1. decide whether Blocked reads correctly as an orthogonal progress constraint
2. verify Question / Blocker category does not collapse into Blocked state
3. verify Current + Blocked + None differs clearly from Current + WAIT
4. compare C1-C6
5. judge whether an explicit BLOCKED label is required
6. judge whether structural-only cues can become learned Cockpit grammar
7. judge whether C5 wrongly resembles suppression / low importance
8. judge whether C6 is usefully redundant or unnecessarily duplicated
9. prefer / reject / combine / refine
```

## 9. Non-decisions

Still unfrozen:

```text
final project-disposition ontology
final progress-constraint ontology
whether Blocked is binary or has multiple constraint classes
whether multiple simultaneous blockers are represented directly on the node
how blocking causes / dependencies are navigated
whether blocked cause is encoded on the relation as well as the node
final compatibility matrix between disposition / constraint / runtime
production blocked visual treatment
historical blocked-state provenance
priority / relevance grammar
```

The saved connector stroke-rhythm channel remains unassigned and is not consumed by this node-level constraint experiment.
