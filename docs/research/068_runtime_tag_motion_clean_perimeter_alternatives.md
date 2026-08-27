# Research 068: Runtime Tag Motion Clean Perimeter Alternatives

**Date:** 2026-08-27  
**Status:** Active Phase-C visual refinement evidence inside Checkpoint 237  
**Scope:** Explores cleaner runtime-tag motion mechanisms after the project owner accepted the switchable runtime-carrier architecture but found the original rotating-gradient tag, the fixed-perimeter tracer, and several line-led alternatives visually imperfect. The latest refinement incorporates a user-supplied motion reference whose useful property is a broad, soft color/shade concentration flowing around a border rather than a crisp small line travelling around it.  
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

Four observations now matter.

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
conceptually correct, but too sparse / literal to feel maximally polished
```

### User-supplied motion reference

The project owner supplied a short visual reference and clarified that the desired quality is not necessarily its color palette. The useful motion characteristic is:

```text
not one crisp straight tracer
not a second rotating box

instead
    a broader soft illuminated shade
    with diffuse edges
    moving around the perimeter
    so the border feels like it carries flowing light / color
```

### First T7 review

The first T7 Soft Shade Flow implementation still used synchronized SVG dash segments. Human review found that it looked effectively like T5 Long Glide rather than like the supplied reference.

That is important negative evidence:

```text
making a dash thicker + blurrier
    does not fundamentally change the read

if the animation is still a moving dash footprint
    it still reads as a moving line / band
```

The bounded question is therefore:

> What runtime-tag motion feels alive, premium and clearly dynamic while keeping the tag itself completely stationary and making the moving element read as a soft perimeter shade rather than a travelling line or band?

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

## 3. Browser

Local route:

```text
http://localhost:5173/design-lab/work-unit-runtime-tag-motion.html
```

Files:

```text
frontend/design-lab/work-unit-runtime-tag-motion.html
frontend/design-lab/work-unit-runtime-tag-motion.css
frontend/design-lab/work-unit-runtime-tag-motion-shade.css
frontend/design-lab/work-unit-runtime-tag-motion.js
```

Exact latest browser implementation target:

```text
6ee5b434e44f3276c5e799ae11958783b50bedef
```

Earlier reference-inspired target remains preserved at:

```text
9a6ffa9b4adefa9d39e9eb97b65283a2a620392c
```

Previous seven-candidate target remains preserved at:

```text
6be6eddefc5bd54914d64199ef59911c3d0aec9b
```

Production `/cockpit` remains untouched.

## 4. Candidate motion families

The browser continues to compare nine treatments while holding the same `Current + RUN` Investigation work unit constant.

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

This preserves the first fixed-perimeter refinement as a control rather than silently replacing it.

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

This tests the intuitive description that the line itself could appear to move around itself. Rather than one object travelling around a static border, the whole perimeter reads as carrying current.

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

### T7 Soft Shade Flow, second implementation

T7 has now been reimplemented rather than merely retuned.

The first T7 used synchronized dash footprints and therefore remained structurally too close to T5.

The new T7 deliberately removes the travelling dash mechanism entirely.

```text
tag geometry        fixed
text                fixed
SVG base border     fixed

moving mechanism
    broad conic paint field
    clipped through the fixed rounded-rectangle border mask
    animated by changing gradient angle
    no moving rectangular element
    no stroke dash travelling around the path
```

Two stationary masked paint layers are used:

```text
outer layer
    very broad diffuse shade shoulder
    low opacity
    stronger blur / glow

inner layer
    broad softer concentration
    no crisp head
    less blur
```

The gradient angle changes while the element itself remains stationary. This is the critical implementation distinction from the original rotating-gradient prototype:

```text
original
    rotating geometry / pseudo-element
    clipping became visually apparent

new T7
    fixed geometry
    only the paint field changes orientation
    rounded-rectangle mask remains fixed
```

The intended perceptual result is:

```text
not a line doing a lap
not a long dash doing a lap
not a second box rotating

instead
    a soft illuminated atmosphere
    shifting continuously through the border
```

T7 remains the default practical-scene candidate for review.

### T8 Layered Wash

T8 preserves the prior more organic multi-stroke interpretation as a comparator.

```text
long diffuse perimeter wash
+
medium overlapping wash
+
shorter brighter concentration
+
slightly different travel rates / direction
```

The overlap changes continuously, so the brightest region evolves while everything remains constrained to the real rounded-rectangle perimeter.

The purpose is to test whether a more fluid, less mechanically uniform shade looks premium or instead becomes unnecessarily busy at Cockpit scale.

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

A segmented control applies T0-T8 to all live runtime tags in this scene.

The practical scene opens on:

```text
T7 Soft Shade Flow
```

This is important because an effect that looks attractive on one isolated tag may become noisy when four different runtime states animate simultaneously.

## 6. Runtime-sensitive pacing

The runtime state continues to influence motion cadence rather than changing the carrier architecture.

For the new T7, the entire paint field remains coherent while only its circulation speed changes by runtime state.

T8 keeps its layered motion but scales the three layer speeds by runtime state so `Running` remains more energetic than `Waiting`, for example.

These timings remain provisional visual evidence rather than a frozen semantic mapping.

## 7. Reduced motion

Reduced motion disables all semantic animation while preserving:

```text
runtime code
runtime state color
static rounded-rectangle perimeter
```

For T7, the moving masked paint layers disappear under Reduced motion. For T8, the moving wash strokes disappear. No runtime meaning depends on motion alone.

## 8. Current review questions

```text
1. Does the second T7 finally stop reading like T5 Long Glide?
2. Does T7 now read as a soft shade / illumination field moving through the border rather than as a line or band travelling around it?
3. Does the fixed mask eliminate the rotating-box / clipping artifact while retaining the continuous movement quality of the original reference?
4. Does T8 still offer anything preferable, or does its multi-stroke character now feel more technical than T7?
5. Which treatment looks cleanest and most premium at actual runtime-tag scale?
6. Which variants remain calm when several runtime tags coexist in the practical scene?
7. Does Reduced motion preserve a clean static runtime tag?
8. Should more than one tag-motion appearance survive as a user option, or should this converge to one preferred tag motion?
```

## 9. Checkpoint hygiene

No new checkpoint is created for this refinement.

Reason:

```text
Checkpoint 237 already owns the switchable runtime-carrier convergence gate
+
this experiment changes only the visual motion mechanism inside the runtime-tag carrier
+
no semantic ontology, promotion status, routing boundary or production authorization changes
```

The refinement is therefore preserved in Git plus this active research record, consistent with the rapid-iteration checkpoint-hygiene rule established in Research 064.

## 10. Still unfrozen

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
