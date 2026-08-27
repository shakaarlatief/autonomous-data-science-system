# Checkpoint 239: Shared BLOCKED Carrier Accepted, Attention Priority Review Opened

**Date:** 2026-08-27  
**Status:** Current product-design checkpoint  
**Checkpoint class:** CONTINUITY / PRODUCT_DESIGN / SEMANTIC_VISUAL_GRAMMAR  
**Project stage:** V1 next-generation Project Cockpit browser-rendered design exploration  
**Scope:** Closes the Checkpoint 238 BLOCKED/progress-constraint visual gate after human acceptance of the shared operational-status carrier, explicit blocker-to-blocked relationship model and final BLOCKED/FAIL compact-ring swap, then opens a distinct experiment for elevated work-unit attention priority.  
**Authority:** Current Phase-C routing/evidence boundary only. Final priority ontology, relevance model, scheduling policy, progress-constraint ontology, runtime ontology and production visual system remain unfrozen.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** chatgpt-08  
**Conversation title:** 08 - Project Cockpit Design Exploration  
**Primary collaborator:** ChatGPT

## 1. Human acceptance closing Checkpoint 238

Checkpoint 238 began by testing `Blocked` as an orthogonal progress constraint rather than a peer of project disposition or runtime.

Human review refined the design substantially.

The accepted current Phase-C semantic distinction is:

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

A Question / Blocker work unit may therefore be the visible cause-resolution work without itself being Blocked.

Example:

```text
[Resolve data contract]
Question / Blocker
CURRENT + HUMAN

        BLOCKS
           ↓

[Production missingness]
Investigation
CURRENT + BLOCKED
```

The visual hypothesis also converged from dedicated blocked-only ornaments to a shared bottom-right operational-status slot.

Current accepted appearance direction:

```text
Dot mode
    compact colored core + dynamic ring

Tag mode
    T7 Soft Shade explicit status tag

BLOCKED
    red family
    sharper non-circular compact ring
    tag text = BLOCKED

FAIL
    red family
    smoother circular compact ring
    tag text = FAIL
```

The final requested refinement was to swap the compact red ring shapes so the sharper geometry belongs to `BLOCKED` and the smoother circular geometry belongs to `FAIL`.

After that implementation the project owner responded:

```text
Perfect. Proceed.
```

Exact accepted shared BLOCKED/status browser visual target:

```text
88fd3c3cfe7a1eff4664afde06341b7b654c97f4
```

Research evidence:

```text
docs/research/069_blocked_as_orthogonal_progress_constraint_visual_grammar_experiment.md
docs/research/070_shared_operational_status_carrier_blocker_relationship_and_work_unit_detail_deferment.md
```

The final ontology and state-transition rules remain unfrozen.

## 2. Work-unit expansion idea remains preserved but deferred

During the same review the project owner proposed:

```text
click compact work-unit box
    -> expand it elegantly
    -> reveal more information
```

This is compatible with Specification 008's promoted deep-work architecture, but the intermediate expanded-card level has not yet been designed or promoted.

It remains preserved for a future interaction-density slice with:

```text
semantic zoom
C5 Internal Layout Grammar
information-density lenses
selected/focused persistent treatment
work-unit detail/provenance presentation
```

It is not mixed into the next visual experiment.

## 3. Why attention priority is the next boundary

The Cockpit now has relatively mature Phase-C evidence for several distinct node-level dimensions:

```text
category
project disposition
current-process focus membership
operational status presentation
blocker cause -> BLOCKS -> blocked effect
```

The remaining node-level question is:

```text
Which visible work deserves more attention now?
```

This checkpoint deliberately names the new bounded concept:

```text
ATTENTION PRIORITY
```

rather than freezing the broader earlier shorthand `importance / priority / relevance` as one semantic axis.

The experiment does not assume priority equals relevance, scheduling order, runtime urgency or current-focus membership.

## 4. New browser target

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

Research:

```text
docs/research/071_work_unit_attention_priority_visual_grammar_experiment.md
```

Production `/cockpit` remains untouched.

## 5. Controlled priority fixture

Every controlled row holds:

```text
category       Investigation
disposition    Current
status         RUN
priority       HIGH
```

`HIGH` is only a provisional binary test fixture. No final scale is frozen.

## 6. Candidate priority treatments

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

The practical scene applies the selected treatment only to work units marked HIGH.

## 7. Practical coexistence fixture

```text
Question / Blocker    CURRENT + HUMAN      HIGH
Investigation         CURRENT + BLOCKED    HIGH
Validation            NEXT + NONE          normal
Model Work            CURRENT + FAIL       HIGH
Investigation         CURRENT + RUN        normal
Evaluation            DEFER + NONE         normal
```

This tests priority beside category color, disposition and accepted operational-status carriers.

The yellow Question / Blocker example is deliberately included to test whether the provisional warm priority tone remains distinguishable from category color.

## 8. Current human gate

The next actor is the human project owner.

Review:

```text
1. pull v1-cockpit-design-exploration
2. open work-unit-attention-priority.html
3. compare A1-A8 against A0
4. judge structural priority cues versus explicit HIGH text
5. reject treatments that resemble status, connector ports, focus or hover
6. inspect mixed categories and especially the yellow Question / Blocker node
7. prefer / reject / combine / refine
8. do not freeze a priority/relevance ontology from this visual gate alone
9. keep work-unit expansion deferred to its own later slice
10. keep production Cockpit untouched
```
