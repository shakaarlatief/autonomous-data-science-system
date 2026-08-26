# Research 041: Combined G4 Ambient Motion Intensity Tuning

**Date:** 2026-08-26  
**Status:** Active product-design experiment record, not a promoted visual specification  
**Interaction environment:** ChatGPT  
**Interaction session:** chatgpt-07  
**Conversation title:** 07 - Project Cockpit Design Exploration  
**Companion thread:** MC-0004

## 1. Human disposition from the first ambient-dynamics comparison

The project owner explicitly preferred keeping all of the tested ambient mechanisms rather than selecting one:

```text
travelling grid currents        KEEP
intersection glints             KEEP
slow ambient light drift        KEEP
localized semantic activity     KEEP
```

The first D1-D4 experiment was judged too subtle overall. The requested change is not a different visual language. It is greater frequency/presence while remaining restrained enough for a serious analytical workspace.

## 2. Design implication

The design question has narrowed from:

```text
Which ambient mechanism should survive?
```

to:

```text
How active should the combined G4 ambient layer be?
```

This is important because it avoids unnecessary mechanism churn. G4 remains the selected grid/world substrate and the dark-first decision remains unchanged.

## 3. Ambient and semantic motion remain distinct channels

The accepted exploration distinction remains:

```text
ambient motion
    decorative atmosphere
    allowed to exist because it improves visual life and product character
    lower semantic authority

semantic motion
    represents real project/runtime state
    higher semantic authority
    should remain more directly interpretable
```

Ambient decoration is not required to encode project truth, but it must not obscure or impersonate semantic state.

## 4. Combined browser experiment

New isolated design-lab artifact:

```text
frontend/design-lab/grid-dynamics-combined.html
frontend/design-lab/grid-dynamics-combined.css
frontend/design-lab/grid-dynamics-combined.js
```

Expected local URL:

```text
http://localhost:5173/design-lab/grid-dynamics-combined.html
```

The experiment keeps all four surviving mechanisms active together and exposes three intensity presets:

```text
Quiet
    all mechanisms retained
    longest gaps / softest presence

Balanced
    more frequent than the initial D1-D4 round
    retains visible quiet intervals

Lively
    noticeably more continuous ambient life
    still not intended to become constant or rapid motion
```

Balanced is the initial default because the user explicitly requested an increase from the first round but did not ask for an aggressively animated world.

## 5. Increased density versus increased salience

This experiment primarily raises **frequency/density**, not raw brightness.

That distinction matters:

```text
more frequent
    = world feels more alive more often

brighter / larger / faster
    = individual effects become more attention-seeking
```

The current hypothesis is that the user's feedback is better answered by the first change.

The browser review should therefore separately judge:

```text
frequency
brightness
trace length
trace speed
glint salience
drift opacity
```

rather than treating all of them as one generic animation-intensity control.

## 6. Current product direction

The strongest current grid/world direction is now:

```text
G4 Adaptive Hybrid
+
dark-first visual baseline
+
major/minor technical grid hierarchy
+
localized semantic activity fields
+
travelling decorative grid currents
+
sparse decorative intersection glints
+
slow ambient light drift
```

Exact intensity remains under human review.

## 7. What is not decided here

This experiment does not freeze:

```text
production animation implementation
final durations or easing
final number of simultaneous traces
final glow colors or brightness
final performance budget
final reduced-motion treatment
light-mode equivalent
work-unit grammar
connector system
semantic zoom architecture
```

## 8. Next evidence

The project owner should inspect the combined experiment in motion and choose among or refine:

```text
Quiet
Balanced
Lively
custom combination
```

After ambient intensity is sufficiently settled, the grid/world slice can be provisionally closed and the next bounded Cockpit design question can open.