# Checkpoint 236: Runtime State Made Conditional, Human Review Reopened

**Date:** 2026-08-27  
**Status:** Current product-design checkpoint  
**Checkpoint class:** CONTINUITY / PRODUCT_DESIGN / SEMANTIC_REFINEMENT  
**Project stage:** V1 next-generation Project Cockpit browser-rendered design exploration  
**Scope:** Refines the active runtime-state browser after human review exposed that live runtime is conditional on a current execution/work episode rather than universally present on every project work unit, updates the browser fixtures accordingly, and reopens visual-carrier review against the corrected semantics.  
**Authority:** Current Phase-C routing/evidence boundary only. Runtime conditionality is accepted for this slice; the final project-disposition ontology, runtime ontology, Blocked semantics, historical execution presentation, and runtime-flow connector grammar remain unfrozen.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** chatgpt-08  
**Conversation title:** 08 - Project Cockpit Design Exploration  
**Primary collaborator:** ChatGPT

## 1. Human semantic challenge

Before judging R0-R6 visually, the project owner questioned why Deferred or Future work would carry a runtime/status at all.

This correctly exposed an implicit conflation in the first runtime fixture.

The refined model is:

```text
PROJECT DISPOSITION
    where does this work stand in the project?

RUNTIME
    if a current execution/work episode exists,
    what is happening in that episode?
```

Therefore runtime is conditional rather than universally populated.

## 2. No runtime is not Idle

The active controlled vocabulary now begins with:

```text
NONE / No runtime
```

This means no current execution/work episode exists.

It must not be represented as an idle runtime process.

The browser therefore hides all R1-R6 runtime instrumentation for NONE.

## 3. Current compatibility interpretation

For the current visual experiment:

```text
Current
    may have no runtime
    may be Queued / Running / Waiting / Waiting for Human / Failed current attempt

Recommended / Next
    normally no runtime
    may be Queued if explicitly scheduled

Deferred
    normally no current runtime

Completed
    normally no current runtime

Future
    normally no current runtime
```

This is not a frozen ADS state matrix.

## 4. Historical execution remains separate

A Deferred, Future or Completed work unit may still have historical execution evidence.

That history belongs to provenance/attempt history, not the current runtime carrier.

This distinction prevents stale execution results from masquerading as current process state.

## 5. Active wording corrected

`Active / Current` is no longer used as a single project-disposition label in this slice.

Current interpretation:

```text
Current
    part of the present working frontier

Running
    executing now
```

This keeps project disposition separate from runtime behavior.

## 6. Blocked remains open

The semantic challenge also revealed that Blocked may ultimately be an orthogonal progress constraint rather than a peer of Current / Next / Deferred / Completed / Future.

Examples such as:

```text
Current + Blocked
Next + Blocked
```

appear coherent.

No new Blocked ontology is frozen at this checkpoint. The issue is preserved for later modeling.

## 7. Corrected browser fixture

Controlled rows now hold a Current Investigation constant and vary:

```text
NONE
QUEUE
RUN
WAIT
HUMAN
FAIL
```

The practical scene now contains:

```text
Question        CURRENT + HUMAN
Investigation   CURRENT + RUN
Validation      NEXT + QUEUE
Model Work      CURRENT + FAIL
Evaluation      DEFER + NONE
Investigation   FUTURE + NONE
```

The visual-carrier families remain:

```text
R0  Neutral Control
R1  Status Lamp
R2  Activity Rail
R3  Runtime Tag
R4  Instrument Cell
R5  Motion Signal
R6  Restrained Hybrid
```

## 8. Exact implementation target

Browser route:

```text
http://localhost:5173/design-lab/work-unit-runtime-grammar.html
```

Exact corrected browser implementation target:

```text
dfcb89c15a23486d3fb9b4947b6a1d7cf3ac8b95
```

Research:

```text
docs/research/066_conditional_runtime_state_and_project_disposition_semantic_correction.md
```

Production `/cockpit` remains untouched.

## 9. Promotion audit

Accepted for the active design model:

```text
runtime is optional / episode-scoped
No runtime is absence, not Idle
historical execution evidence is not current runtime
Current is preferred over Active when referring to project disposition
```

Not promoted/frozen:

```text
final project-disposition ontology
final runtime ontology
final Blocked semantics
final compatibility matrix between all axes
execution-history interface
runtime-flow connector grammar
final runtime visual carrier
```

## 10. Current human gate

The next actor is the human project owner.

Review:

```text
1. pull v1-cockpit-design-exploration
2. refresh work-unit-runtime-grammar.html
3. verify NONE shows no runtime instrumentation in R1-R6
4. compare R1-R6 on the five live runtime states
5. inspect the practical scene, especially DEFER + NONE and FUTURE + NONE
6. compare normal and Reduced motion
7. judge which runtime carriers survive the corrected semantic model
8. prefer / reject / combine / refine
9. do not freeze the final runtime/disposition/Blocked ontology from this visual gate alone
10. keep production Cockpit untouched
```
