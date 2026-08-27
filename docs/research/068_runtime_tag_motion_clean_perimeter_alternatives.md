# Research 068: Runtime Tag Motion Clean Perimeter Alternatives

**Date:** 2026-08-27  
**Status:** Active Phase-C visual refinement evidence inside Checkpoint 237  
**Scope:** Explores cleaner runtime-tag motion mechanisms after the project owner accepted the switchable runtime-carrier architecture but found both the original rotating-gradient tag and the later short-tracer refinement visually imperfect.  
**Authority:** Design evidence only. This memo does not freeze the final runtime carrier, final animation treatment, runtime ontology, project-disposition ontology, or production preference-persistence architecture.

## 1. Human evidence leading to this refinement

The project owner accepted the overall runtime-carrier architecture:

```text
exactly one runtime carrier per live-runtime work unit

Dot + dynamic ring
or
Runtime tag

Global switch
+
Per-box override
```

The remaining concern is specifically the runtime-tag animation.

Two prior mechanisms produced useful but incomplete evidence.

### Original rotating conic-gradient treatment

Positive:

```text
lively
continuous
visually richer than a tiny tracer
```

Negative:

```text
the gradient/box appeared to rotate inside the tag
parts were clipped as the rotating geometry moved beyond the tag bounds
therefore the effect did not read as fully clean or premium
```

### First fixed-perimeter tracer treatment

Positive:

```text
tag geometry stayed stationary
text stayed stationary
a bright segment followed the real rounded-rectangle perimeter
no clipping artifact
```

Negative:

```text
the animated element became one relatively small travelling line
conceptually correct, but potentially too sparse / literal to feel maximally polished
```

The new bounded question is therefore:

> What runtime-tag motion feels alive, premium and clearly dynamic while keeping the tag itself completely stationary and constraining all motion to the real perimeter?

## 2. Held constraints

The following are held:

```text
runtime remains conditional
No runtime means no runtime carrier
one runtime carrier per live-runtime work unit
Dot + ring remains the alternate carrier
runtime-tag text does not move
runtime-tag box does not rotate
runtime-tag geometry does not leave its own bounds
motion is semantic and must degrade under Reduced motion
category and P7 disposition remain separate semantic channels
```

## 3. New browser

Local route:

```text
http://localhost:5173/design-lab/work-unit-runtime-tag-motion.html
```

Files:

```text
frontend/design-lab/work-unit-runtime-tag-motion.html
frontend/design-lab/work-unit-runtime-tag-motion.css
frontend/design-lab/work-unit-runtime-tag-motion.js
```

Exact browser implementation target:

```text
6be6eddefc5bd54914d64199ef59911c3d0aec9b
```

Production `/cockpit` remains untouched.

## 4. Candidate motion families

The browser compares seven treatments while holding the same `Current + RUN` Investigation work unit constant.

### T0 Static Control

```text
no runtime-tag animation
```

Purpose: test whether motion improves the tag enough to justify itself.

### T1 Short Tracer

```text
one small luminous segment
travels around the real rounded-rectangle perimeter
```

This preserves the latest pre-existing refinement as a control rather than silently replacing it.

### T2 Comet Flow

```text
bright head
+
longer lower-opacity wake
+
continuous perimeter travel
```

The intention is to keep the geometric cleanliness of the real SVG perimeter while giving the motion more visual body than the short tracer.

### T3 Perimeter Current

```text
restrained repeated dash pattern
moves through the full outline
```

This tests the project owner's intuitive description that the line itself could appear to move around itself. Rather than one object travelling around a static border, the whole perimeter reads as carrying current.

### T4 Twin Orbit

```text
two opposite luminous accents
circulate together
```

This reduces the long empty interval produced by a single tracer while keeping the treatment symmetric and bounded.

### T5 Long Glide

```text
one longer highlighted band
moves calmly around the perimeter
```

This is intentionally quieter than T3 and fuller than T1.

### T6 Soft Pulse

```text
no directional travel
whole perimeter gently brightens and relaxes
```

This tests whether a premium dynamic tag needs directional circulation at all.

## 5. Practical coexistence check

The page includes the same mixed-category runtime fixture used in the switchable-carrier work:

```text
Question        CURRENT + HUMAN
Investigation   CURRENT + RUN
Validation      NEXT + QUEUE
Model Work      CURRENT + FAIL
Evaluation      DEFER + NONE
Investigation   FUTURE + NONE
```

A segmented control applies T0-T6 to all live runtime tags in this scene.

This is important because an effect that looks attractive on one isolated tag may become noisy when four different runtime states animate simultaneously.

## 6. Reduced motion

Reduced motion disables all semantic animation while preserving:

```text
runtime code
runtime state color
static rounded-rectangle perimeter
```

No runtime meaning depends on motion alone.

## 7. Current review questions

```text
1. Which treatment looks cleanest and most premium at actual tag scale?
2. Does T2 Comet Flow preserve cleanliness while feeling richer than T1?
3. Does T3 make the line itself feel alive in a good way, or become too technical?
4. Is T4 balanced and elegant, or unnecessarily busy?
5. Does T5 provide the right amount of continuous motion?
6. Is T6 aesthetically superior despite lacking directional circulation?
7. Which variants remain calm when several tags coexist in the practical scene?
8. Should more than one tag-motion appearance survive as a user option, or should this converge to one preferred tag motion?
```

## 8. Checkpoint hygiene

No new checkpoint is created for this refinement.

Reason:

```text
Checkpoint 237 already owns the switchable runtime-carrier convergence gate
+
this experiment changes only the visual motion mechanism inside the runtime-tag carrier
+
no semantic ontology, promotion status, routing boundary or production authorization changes
```

The refinement is therefore preserved in Git plus this research record, consistent with the rapid-iteration checkpoint-hygiene rule established in Research 064.

## 9. Still unfrozen

```text
preferred runtime-tag motion
whether multiple runtime-tag motion styles survive
final runtime carrier default
production runtime-carrier persistence scope
final runtime ontology
final Blocked semantics
final project-disposition ontology
runtime-flow connector semantics
```
