# Research 066: Conditional Runtime State and Project-Disposition Semantic Correction

**Date:** 2026-08-27  
**Status:** Active Phase-C semantic refinement evidence  
**Scope:** Refines the work-unit runtime-state experiment after human review exposed that runtime should not be represented as a universally present peer state on every work unit.  
**Authority:** Research evidence for the current runtime browser slice. This memo does not freeze the final ADS project-disposition, runtime, blockage, or execution ontology.

## 1. Trigger

The first runtime-state browser opened with a provisional visual-test vocabulary:

```text
Idle
Queued
Running
Waiting
Waiting for Human
Failed
```

The project owner then asked a semantic question before judging the visual carriers:

> If something is Deferred, Future, or otherwise not currently part of active work, why would it have a runtime/status at all?

This exposed a real modeling problem rather than a cosmetic issue.

The original experiment implicitly suggested that every work unit always carries both:

```text
project disposition
+
runtime state
```

That is too strong.

## 2. Corrected semantic model

The refined distinction is:

```text
PROJECT DISPOSITION
    Where does this work stand in the project?

RUNTIME STATE
    If this work currently has a meaningful execution/work episode,
    what is happening in that episode?
```

Runtime is therefore conditional.

A work unit may exist, have a project disposition, belong or not belong to the current focus, and still have no current runtime episode at all.

## 3. No runtime is absence, not Idle

A crucial distinction is:

```text
No runtime
    there is no current execution/work episode to describe

Idle runtime
    a runtime episode exists but is currently doing nothing
```

The first case is common and must not be visually represented as though an idle process exists.

For the current browser refinement, `Idle` is therefore removed from the provisional controlled state set and replaced with:

```text
NONE / No runtime
```

The NONE example intentionally renders no runtime carrier in R1-R6.

## 4. Expected compatibility with project disposition

The current working interpretation is:

```text
Current
    may have no runtime
    may be Queued
    may be Running
    may be Waiting
    may be Waiting for Human
    may have a Failed current attempt

Recommended / Next
    usually has no runtime
    may be Queued if an execution has already been explicitly scheduled

Deferred
    normally no current runtime

Completed
    normally no current runtime

Future
    normally no current runtime
```

This is a conceptual guide for the visual experiment, not a frozen compatibility matrix.

## 5. Historical runtime remains possible

A work unit without a current runtime episode may still have execution history.

For example:

```text
Calibration review
    current disposition: Deferred

historical execution record
    Failed
    timestamp / attempt / evidence
```

That historical `Failed` result is provenance/history, not the work unit's present runtime state.

The Cockpit should not collapse historical execution evidence into current runtime presentation.

## 6. Active is retired from this slice in favor of Current

The earlier disposition fixture sometimes used:

```text
Active / Current
```

`Active` is semantically dangerous because it can be read as active execution.

The cleaner distinction is:

```text
Current
    belongs to the project's present working frontier

Running
    a current execution episode is progressing now
```

This allows combinations such as:

```text
Current + no runtime
Current + Queued
Current + Running
Current + Waiting
Current + Failed attempt
```

without overloading the word `Active`.

## 7. Blocked is now explicitly unresolved

The question also exposed that `Blocked` may not belong on exactly the same axis as:

```text
Current
Next
Deferred
Completed
Future
```

For example:

```text
Current + Blocked
Next + Blocked
```

are intuitively coherent combinations.

A plausible later architecture is:

```text
PROJECT DISPOSITION / LIFECYCLE
    Current
    Next
    Deferred
    Completed
    Future

PROGRESS CONSTRAINT
    Unblocked
    Blocked

RUNTIME
    absent
    Queued
    Running
    Waiting
    Waiting for Human
    Failed current attempt
```

This is deliberately not promoted or frozen yet. The important current result is only that `Blocked` must not be silently assumed to be a peer lifecycle value if later evidence shows it is orthogonal.

## 8. Corrected runtime browser fixture

The visual-carrier families remain unchanged:

```text
R0  Neutral Control
R1  Status Lamp
R2  Activity Rail
R3  Runtime Tag
R4  Instrument Cell
R5  Motion Signal
R6  Restrained Hybrid
```

The controlled comparison now holds:

```text
category       Investigation
project state  Current
focus          current
```

and varies:

```text
NONE    No runtime
QUEUE   Queued
RUN     Running
WAIT    Waiting
HUMAN   Waiting for Human
FAIL    Failed current attempt
```

The NONE row remains free of runtime instrumentation regardless of R1-R6.

## 9. Corrected practical coexistence scene

The practical scene now intentionally includes both live runtime and absent runtime:

```text
Question        CURRENT + HUMAN
Investigation   CURRENT + RUN
Validation      NEXT + QUEUE
Model Work      CURRENT + FAIL
Evaluation      DEFER + NONE
Investigation   FUTURE + NONE
```

This directly tests whether runtime remains legible when it genuinely exists without making Deferred/Future boxes look as though dormant processes are running behind them.

## 10. Semantic motion rule remains

Runtime motion, where used, remains semantic motion rather than ambient decoration.

Therefore:

```text
motion may reinforce a live runtime state
motion may not be the sole carrier of meaning
Reduced motion must preserve static interpretability
No runtime must not animate
```

## 11. Exact browser implementation

Local route:

```text
http://localhost:5173/design-lab/work-unit-runtime-grammar.html
```

Corrected exact browser implementation target:

```text
dfcb89c15a23486d3fb9b4947b6a1d7cf3ac8b95
```

Changed design-lab files:

```text
frontend/design-lab/work-unit-runtime-grammar.html
frontend/design-lab/work-unit-runtime-grammar.js
frontend/design-lab/work-unit-runtime-grammar.css
```

Production `/cockpit` remains untouched.

## 12. Current human review gate

The visual question can now be judged against the corrected semantics:

```text
1. Does NONE correctly look like an ordinary Current work unit with no runtime instrumentation?
2. Which R1-R6 carrier best distinguishes Queued / Running / Waiting / Waiting for Human / Failed?
3. Does runtime remain secondary to category identity and compatible with P7 disposition?
4. Does Runtime Tag become too dense next to the existing disposition tag?
5. Does semantic motion add useful execution information without looking decorative?
6. Does Reduced motion preserve the same state meaning?
7. In the practical scene, do Deferred/Future remain clean while genuine runtime remains obvious?
```

## 13. Promotion audit

Promote now:

```text
runtime is conditional / episode-scoped
No runtime is absence rather than Idle
current runtime must remain distinct from historical execution provenance
```

only as active design evidence for this Phase-C slice.

Do not yet promote a final ontology for:

```text
project disposition
runtime states
Blocked / progress constraints
runtime-flow connectors
execution history UI
```

Those require further product and implementation evidence.
