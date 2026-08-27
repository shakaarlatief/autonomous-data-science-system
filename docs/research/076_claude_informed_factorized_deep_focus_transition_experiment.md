# Research 076: Claude-Informed Factorized Deep-Focus Transition Experiment

**Date:** 2026-08-27  
**Status:** Active Phase-C interaction-design evidence  
**Scope:** Synthesizes MC-0004 Message 006 into an executable browser comparison that separates deep-focus transition mechanisms which the original F0-F8 browser partially bundled together.  
**Authority:** Research evidence only. No final deep-focus transition, workspace composition, motion timing, return behavior, minimap behavior, neighbor-retention semantics, or production component architecture is frozen by this memo.

## 1. Trigger

The project owner requested additional Claude ideas and explicitly removed any artificial limit on how much transition design could be tested.

ChatGPT issued MC-0004 Message 005. Claude responded in Message 006 after directly inspecting exact browser target:

```text
afd15f52897a295788dc3a1d04b2d1b31ef707f9
```

Claude's response is preserved at:

```text
docs/model_collaboration/threads/MC-0004/messages/006_claude_deep_focus_transition_divergent_ideation.md
```

## 2. Central synthesis

The most important contribution from Message 006 is not one visual candidate. It is the diagnosis that the transition problem contains several independent dimensions that should not automatically be bundled into monolithic F-variants.

Working decomposition:

```text
DEEP-FOCUS TRANSITION

object continuity
    where does the workspace visibly originate?

context retention
    what project context remains visible?

context relevance
    is retained context geometrically arbitrary or semantically relevant?

entry choreography
    one-step, staged, morph, camera push, etc.

orientation aid
    full map, rail, neighbor set, breadcrumb, compass, none

return choreography
    symmetric with entry or faster / more direct
```

This decomposition is now the organizing principle of the follow-up browser.

## 3. Concrete findings from Claude inspection

Message 006 identified several useful implementation facts in the original F0-F8 browser:

```text
all F0-F8 share the same DOM
    differences are primarily CSS composition

F2
    only current variant explicitly tries to preserve object continuity

F6
    retains a hardcoded left 22% map slice
    not the actually relevant context around the selected node

F4
    breadcrumb/path is schematic static text

entry / return
    every current variant simply reverses the same transition
    no asymmetric return treatment is tested
```

These findings are treated as design evidence, not as reasons to discard the original browser. F0, F2 and F6 remain useful controls.

## 4. Claude concepts carried forward

Message 006 proposed:

```text
T1  Generalized Anchored Entry
T2  Neighbor-Aware Context Retention
T3  Staged Two-Step Entry
T4  Asymmetric Return
T5  Camera Push-Through
T6  Adaptive Retention by Workspace Type
T7  Compass / Minimap Return Anchor
```

Disposition for this executable round:

```text
T1  TEST NOW
T2  TEST NOW
T3  TEST NOW
T4  TEST NOW AS MODIFIER
T5  TEST NOW
T6  DEFER, depends on real specialist-workspace diversity
T7  TEST NOW
```

T6 is preserved and not rejected.

## 5. New factorized browser

Local route:

```text
http://localhost:5173/design-lab/work-unit-deep-focus-factorized.html
```

Files:

```text
frontend/design-lab/work-unit-deep-focus-factorized.html
frontend/design-lab/work-unit-deep-focus-factorized.css
frontend/design-lab/work-unit-deep-focus-factorized-refinement.css
frontend/design-lab/work-unit-deep-focus-factorized.js
```

Exact latest implementation target:

```text
0390d8fef9d6647ae17ecd7c948159d0a5b603e5
```

Production `/cockpit` remains untouched.

## 6. Browser structure

### Batch A: object continuity

```text
A0  F2 Anchored Morph Control
A1  Anchored Center Stage
A2  Anchored Context Rail
A3  Camera Push-Through
```

The selected X5 card is intentionally rendered off-center.

For anchored candidates, JavaScript measures the actual rendered X5 rectangle and writes its position and dimensions into CSS custom properties. This removes the prior assumption that the selected node sits at the viewport center and makes the browser test the structural idea of a dynamic origin rather than a special-case coordinate.

The refinement stylesheet keeps final workspace dimensions numerically interpolable so the browser can animate from the measured card rectangle instead of relying on a `width/height -> auto` transition.

### Batch B: context relevance

```text
B0  F6 Fixed Rail Control
B1  Neighbor-Aware Context
B2  Neighbor-Aware + Anchor
```

B0 deliberately preserves F6's flawed geometric rail as a control.

B1/B2 replace arbitrary retained map area with compact representations of directly connected work. The neighbor content remains schematic and does not freeze final relation filtering, relation ranking, or semantic-neighborhood rules.

### Batch C: staging and orientation

```text
C0  Hard Replace Control
C1  Staged Two-Step Entry
C2  Compass + Soft World
C3  Hard Replace + Compass
```

C1 performs a brief visible preview phase before automatically advancing to full focus.

C2/C3 test whether a compact topology indicator can preserve orientation with much less map context than F1/F3/F5-style retained-world treatments.

The compass is schematic. It does not promote a production minimap.

## 7. T4 asymmetric return as a modifier

Claude correctly classified T4 as a cross-cutting refinement rather than another monolithic transition architecture.

The large interaction studio therefore exposes:

```text
Return timing
    Symmetric
    Fast return
```

Fast return changes only the return leg. Entry behavior remains unchanged.

This keeps the comparison aligned with the factorized model:

```text
transition architecture
    independent from
return timing policy
```

## 8. Fixture fidelity correction

The original F0-F8 fixture incorrectly showed only two diagonal SEL2 brackets even though the accepted persistent-selection treatment is four outside corner brackets.

The project owner explicitly said the old fixture did not need to be repaired as long as production fidelity is audited later.

Because this is a new browser rather than a repair to the old one, the new fixture restores the accepted four-corner SEL2 presentation so the known regression is not propagated into new evidence.

This does not reopen the SEL2 decision.

## 9. Reduced motion

All new motion remains optional presentation.

```text
prefers-reduced-motion
    transition and animation duration collapse to effectively instant
    final semantic state remains readable
    no transition meaning depends solely on motion
```

T5 therefore degrades to the same final workspace state without requiring a depth-motion metaphor.

## 10. Human review gate

Review the mechanisms separately:

```text
Object continuity
    A0 vs A1 vs A2 vs A3

Context relevance
    B0 vs B1 vs B2

Staging / minimal orientation
    C0 vs C1 vs C2 vs C3

Return timing
    Symmetric vs Fast return in the large interaction studio
```

Questions:

```text
does dynamic anchored entry materially improve source-object continuity?
does neighbor-aware context help or become cluttered?
does camera push-through feel coherent with Cockpit zoom or disorienting?
does staged entry add comprehension or ceremony?
can a topology compass replace visible world context?
does faster return feel efficient without feeling broken?
```

Human preference may select mechanisms from different batches and combine them later. The browser is intentionally not asking for one winner across all eleven tiles.

## 11. Still unfrozen

```text
final deep-focus transition composition
whether anchored entry is universal or optional
actual neighbor selection / graph-query semantics
neighbor count / ranking / overflow behavior
whether a compass/minimap exists in production
exact transition duration / easing
asymmetric return timing
interruptibility / cancellation
workspace mounting mechanics
URL and browser-history semantics
multiple deep-focus workspaces / tabs
specialist-workspace composition
adaptive treatment by workspace type
production performance implementation
```

No new checkpoint is created because this is a broadened executable comparison inside the existing Checkpoint 243 deep-focus-transition review gate.
