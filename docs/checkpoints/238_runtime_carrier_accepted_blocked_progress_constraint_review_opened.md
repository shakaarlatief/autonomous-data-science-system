# Checkpoint 238: Runtime Carrier Accepted, BLOCKED Progress Constraint Review Opened

**Date:** 2026-08-27  
**Status:** Current product-design checkpoint  
**Checkpoint class:** CONTINUITY / PRODUCT_DESIGN / SEMANTIC_VISUAL_GRAMMAR  
**Project stage:** V1 next-generation Project Cockpit browser-rendered design exploration  
**Scope:** Closes the Checkpoint 237 runtime-carrier convergence gate after human acceptance of the switchable one-carrier architecture and repaired T7 Soft Shade runtime-tag motion, then opens a distinct experiment for `BLOCKED` as a possible orthogonal progress constraint rather than a peer project-disposition/runtime state.  
**Authority:** Current Phase-C routing/evidence boundary only. Final runtime ontology, project-disposition ontology, progress-constraint ontology, compatibility matrix and production visual system remain unfrozen.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** chatgpt-08  
**Conversation title:** 08 - Project Cockpit Design Exploration  
**Primary collaborator:** ChatGPT

## 1. Human acceptance closing Checkpoint 237

The project owner had already accepted the switchable runtime-carrier architecture as:

```text
exactly one runtime carrier per live-runtime work unit

Dot + dynamic ring
or
Animated runtime tag

Global switch
+
Per-box override
```

The remaining open item was the runtime-tag motion language.

After several iterations, T7 Soft Shade Flow was repaired so the broad masked paint field actually animates around the stationary tag perimeter. The project owner reviewed the repaired result and responded:

```text
Perfect. Proceed.
```

Accepted Phase-C runtime presentation direction:

```text
runtime is conditional / episode-scoped

No runtime
    no runtime carrier

live runtime
    exactly one carrier

carrier A
    Dot + dynamic ring

carrier B
    T7 Soft Shade runtime tag

switching
    global across live-runtime work units
    local per-work-unit override

Reduced motion
    static state identity remains legible
```

Exact accepted T7 motion-browser target:

```text
08534f94c2f272f969159087de2797a23e36b330
```

Exact switchable-runtime browser with T7 integrated:

```text
fb847bd65ff6e5e4203a89ee2d4f74b7187c8359
```

Research evidence:

```text
docs/research/067_switchable_runtime_carrier_convergence_and_r1_r5_verification.md
docs/research/068_runtime_tag_motion_clean_perimeter_alternatives.md
```

The final runtime ontology, final production default carrier and preference-persistence architecture remain unfrozen.

## 2. Why the next boundary is BLOCKED

The runtime semantic correction exposed that `Blocked` does not behave like a simple peer of:

```text
Current
Next
Deferred
Completed
Future
```

The following combinations are coherent:

```text
Current + Blocked
Next + Blocked
```

This motivates the working separation:

```text
PROJECT DISPOSITION
    where does this work stand in the project?

PROGRESS CONSTRAINT
    can this work proceed?

RUNTIME
    if a meaningful current execution/work episode exists,
    what is happening in that episode?
```

No final ontology is promoted by this checkpoint.

## 3. Critical semantic contrasts

The new browser explicitly tests:

```text
Current + Blocked + No runtime
vs
Current + WAIT runtime + Unblocked
```

because waiting during a live execution episode is not necessarily the same thing as project-level inability to proceed.

It also distinguishes:

```text
Question / Blocker category
    what kind of work unit is this?

Blocked progress constraint
    can this affected work unit proceed?
```

A Question / Blocker work unit may therefore be unblocked itself while resolving the blocker for another node.

## 4. New browser target

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

Research:

```text
docs/research/069_blocked_as_orthogonal_progress_constraint_visual_grammar_experiment.md
```

Production `/cockpit` remains untouched.

## 5. Candidate BLOCKED treatments

```text
C0  Neutral Control
C1  Explicit Tag
C2  Edge Clamp
C3  Stop Rail
C4  Barrier Seal
C5  Constraint Veil
C6  Tag + Clamp
```

The practical scene applies the selected C0-C6 treatment only to nodes whose progress constraint is Blocked.

## 6. Practical semantic fixture

```text
Question / Blocker    CURRENT + HUMAN     unblocked
Investigation         CURRENT + BLOCKED   NONE
Validation            NEXT + BLOCKED      NONE
Model Work            CURRENT + RUN       unblocked
Investigation         CURRENT + WAIT      unblocked
Evaluation            DEFER + NONE        unblocked
Investigation         FUTURE + NONE       unblocked
```

The goal is to judge semantic coexistence as well as visual quality.

## 7. Current human gate

The next actor is the human project owner.

Review:

```text
1. pull v1-cockpit-design-exploration
2. open work-unit-progress-constraint.html
3. judge whether Blocked belongs on an orthogonal progress-constraint axis
4. verify Question / Blocker category remains distinct from Blocked state
5. verify Current + Blocked + NONE remains distinct from Current + WAIT
6. compare C1-C6 against C0 control
7. judge explicit tag vs structural cues vs hybrid
8. identify confusing treatments, especially any that resemble focus suppression or priority
9. prefer / reject / combine / refine
10. keep final ontology unfrozen until semantic evidence warrants promotion
11. keep production Cockpit untouched
```
