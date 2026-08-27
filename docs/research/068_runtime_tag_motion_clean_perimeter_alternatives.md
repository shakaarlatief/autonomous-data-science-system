# Research 068: Runtime Tag Motion Clean Perimeter Alternatives

**Date:** 2026-08-27  
**Status:** Closed Phase-C visual refinement evidence inside Checkpoint 237; T7 Soft Shade Flow accepted for the runtime-tag carrier  
**Scope:** Explores cleaner runtime-tag motion mechanisms after the project owner accepted the switchable runtime-carrier architecture but found the original rotating-gradient tag, the fixed-perimeter tracer, and several line-led alternatives visually imperfect. The final refinement incorporates a user-supplied motion reference whose useful property is a broad, soft color/shade concentration flowing around a border rather than a crisp small line travelling around it.  
**Authority:** Accepted Phase-C design evidence for the runtime-tag motion mechanism. This memo does not freeze the final runtime ontology, production default carrier, project-disposition ontology, or production preference-persistence architecture.

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

The remaining concern was specifically the runtime-tag animation.

Five observations mattered.

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

The project owner supplied a short visual reference and clarified that the desired quality was not necessarily its color palette. The useful motion characteristic was:

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

### Second T7 implementation defect

The second T7 replaced the travelling dash with a masked conic shade field, but human review found that the rendered result was completely static.

Direct inspection identified the implementation defect:

```text
--t7-shade-angle
    was registered with inherits: false

animation
    ran on .motion-runtime-tag

paint field
    lived on ::before and ::after pseudo-elements
```

Because the registered custom property did not inherit, the pseudo-elements kept the property's initial `0deg` value even while the parent animated. The animation was therefore real on the parent but invisible in the painted pseudo-elements.

The correction changed the property to:

```css
@property --t7-shade-angle {
  syntax: "<angle>";
  inherits: true;
  initial-value: 0deg;
}
```

This was an implementation repair, not a new visual hypothesis.

## 2. Held constraints

The following remained held throughout:

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

## 3. Browser evidence

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

Exact accepted T7 browser implementation target:

```text
08534f94c2f272f969159087de2797a23e36b330
```

Static second-T7 target remains preserved at:

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

Production `/cockpit` remained untouched.

## 4. Candidate motion families

The browser compared nine treatments while holding the same `Current + RUN` Investigation work unit constant.

### T0 Static Control

```text
no runtime-tag animation
```

### T1 Short Tracer

```text
one small luminous segment
travels around the real rounded-rectangle perimeter
```

### T2 Comet Flow

```text
bright head
+
longer lower-opacity wake
+
continuous perimeter travel
```

### T3 Perimeter Current

```text
restrained repeated dash pattern
moves through the full outline
```

### T4 Twin Orbit

```text
two opposite luminous accents
circulate together
```

### T5 Long Glide

```text
one longer highlighted band
moves calmly around the perimeter
```

### T6 Soft Pulse

```text
no directional travel
whole perimeter gently brightens and relaxes
```

### T7 Soft Shade Flow, masked-paint implementation

T7 is structurally different from T5 and the first T7 attempt.

```text
tag geometry        fixed
text                fixed
base border mask    fixed

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

The gradient angle changes while the element itself remains stationary. The custom angle property is inherited into the pseudo-elements so the moving paint field is actually visible.

The perceptual target is:

```text
not a line doing a lap
not a long dash doing a lap
not a second box rotating

instead
    a soft illuminated atmosphere
    shifting continuously through the border
```

### T8 Layered Wash

T8 preserved the more organic multi-stroke interpretation as a comparator:

```text
long diffuse perimeter wash
+
medium overlapping wash
+
shorter brighter concentration
+
slightly different travel rates / direction
```

## 5. Practical coexistence check

The page used the same mixed-category runtime fixture as the switchable-carrier work:

```text
Question        CURRENT + HUMAN
Investigation   CURRENT + RUN
Validation      NEXT + QUEUE
Model Work      CURRENT + FAIL
Evaluation      DEFER + NONE
Investigation   FUTURE + NONE
```

The practical scene opened on T7 Soft Shade Flow so the selected mechanism could be judged with multiple live runtime states present at once.

## 6. Runtime-sensitive pacing

Runtime state continues to influence motion cadence rather than carrier architecture.

For T7, the entire paint field remains coherent while only circulation speed changes by runtime state. These timings remain provisional visual evidence rather than a frozen semantic mapping.

## 7. Reduced motion

Reduced motion disables semantic animation while preserving:

```text
runtime code
runtime state color
static rounded-rectangle perimeter
```

For T7, the moving masked paint layers disappear under Reduced motion. No runtime meaning depends on motion alone.

## 8. Final human review and accepted result

After the inheritance repair, the project owner reviewed T7 again and responded:

```text
Perfect. Proceed.
```

That closes the runtime-tag motion refinement for the current Phase-C round.

Accepted visual result:

```text
T7 Soft Shade Flow
    SELECTED for the Animated runtime tag carrier

stationary tag geometry
stationary text
stationary border mask
broad soft shade field flows through the perimeter
no travelling dash as the dominant read
no rotating inner rectangle
no clipping artifact from rotating geometry
```

The switchable-carrier browser was then updated so the main runtime-tag carrier uses the accepted T7 mechanism rather than the temporary perimeter tracer.

Exact integrated switchable-runtime browser target:

```text
fb847bd65ff6e5e4203a89ee2d4f74b7187c8359
```

The broader runtime presentation direction retained for Phase C is therefore:

```text
runtime is conditional / episode-scoped
+
exactly one live-runtime carrier per work unit
+
Dot + dynamic ring
or
T7 Soft Shade runtime tag
+
global carrier switching
+
per-work-unit local overrides
+
No runtime -> no carrier
+
Reduced motion preserves static identity
```

## 9. Checkpoint hygiene

No additional checkpoint was created for the intermediate T7 refinements because Checkpoint 237 already owned the runtime-carrier convergence gate and the changes were visual/implementation refinements inside that same gate.

A new checkpoint becomes warranted only now that human acceptance closes the runtime-carrier review boundary and the project proceeds to a distinct semantic/design question.

## 10. Still unfrozen

```text
final runtime ontology
whether both carriers survive unchanged to production
production default runtime carrier
production runtime-carrier persistence scope
final runtime-sensitive motion pacing
final project-disposition ontology
runtime-flow connector semantics
historical execution-attempt presentation
```
