# Research 040: G4 Grid/World Selection, Dark-First Baseline, and Ambient Dynamics Exploration

**Date:** 2026-08-26  
**Status:** Active human-reviewed product-design evidence, not a final visual specification  
**Scope:** Records the first Phase-C human grid/world review, selects G4 Adaptive Hybrid as the surviving substrate direction, defers light-mode optimization, and opens a bounded experiment on subtle decorative grid dynamics that remain visually subordinate to semantic project activity.  
**Authority:** Product-design evidence only. Specification 008 remains the promoted V1 Cockpit interaction architecture.  
**Interaction environment:** ChatGPT  
**Project / workspace:** Autonomous Data Science System  
**Interaction session:** chatgpt-07  
**Conversation title:** 07 - Project Cockpit Design Exploration  
**Companion collaboration thread:** MC-0004

---

## 1. Human review result for Slice 01

The project owner reviewed the browser-rendered G1-G4 grid/world experiment in the real Vite/Chromium environment.

Disposition:

```text
G1 Precision Lines
    REJECT as primary direction
    technically clear but less visually compelling than G4

G2 Dot Matrix
    REJECT as primary direction
    clean but weaker than G4 as the ADS world identity

G3 Cross Lattice
    REJECT as primary direction
    visually distinctive but not preferred over G4

G4 Adaptive Hybrid
    SELECT as the surviving grid/world substrate direction
```

The human judgment was strong rather than marginal: there was no identified reason to prefer G1-G3 over G4 after direct comparison.

The specific positive reaction to G4 included:

```text
best-looking overall substrate
strong grid/world visual character
localized light treatment is attractive
additional decorative visual life is acceptable when restrained
```

This does not freeze every G4 implementation detail. It selects the design direction and creates a better baseline for refinement.

---

## 2. Dark-first product direction

The light-mode rendering was judged unattractive, consistent with the earlier promoted Cockpit light-mode weakness.

The resulting product-direction rule for the current exploration is:

```text
DARK MODE
    primary design baseline
    all near-term visual decisions optimized and reviewed here

LIGHT MODE
    deferred
    must not constrain or dilute current dark-mode design choices
    may be designed as a dedicated later pass after the core Cockpit visual system is settled
```

This is not a permanent rejection of light mode.

It is a sequencing decision:

```text
first build one excellent coherent Cockpit visual system
then derive a deliberate light counterpart
```

The current design phase should therefore stop requiring every small visual experiment to prove itself in both themes.

Accessibility remains binding. Dark-first does not authorize insufficient contrast or meaning encoded only by brightness/color.

---

## 3. Decorative motion is explicitly allowed

Earlier synthesis correctly warned against making every edge, node, and grid element continuously animate merely to appear advanced.

The human review adds an important refinement:

> Decorative visual behavior is not inherently wrong. The Cockpit may contain subtle ambient motion purely because it makes the environment feel more polished, dynamic, and alive.

Therefore the motion model should distinguish at least two layers:

```text
SEMANTIC MOTION
    communicates real changing project/runtime state
    must remain interpretable
    may carry higher salience

AMBIENT MOTION
    decorative / atmospheric
    does not claim project-state meaning
    intentionally low salience
    sparse, slow, and visually subordinate
```

The rule from Research 037 remains binding for semantic relations:

> If a relation is moving, the user should be able to explain what is currently moving in the project.

But that rule should not be incorrectly generalized into:

```text
nothing may move unless it encodes project state
```

A more accurate rule is:

```text
ambient decorative motion is allowed
    IF
it is visibly lower-salience than semantic motion
it cannot be mistaken for a blocker/run/dependency signal
it stays calm enough for long analytical sessions
it degrades cleanly under reduced-motion preferences
```

---

## 4. Next bounded question

With G4 selected, the next design question is not whether to replace the substrate.

It is:

> What kind and amount of subtle ambient dynamics make the G4 world feel premium and alive without becoming noisy, gimmicky, or semantically confusing?

The project owner explicitly suggested possibilities such as:

```text
occasional light lines travelling through parts of the grid
subtle dynamic behavior distributed through the world
small decorative effects that create life without rapid/random activity
```

This is now the target of Slice 02.

---

## 5. Slice 02 experimental variants

The experiment should hold the G4 substrate and project fixture constant while varying only the ambient motion treatment.

### D1 Quiet Current

Sparse neutral light segments move slowly along selected major grid lines.

Intent:

```text
make the world feel electrically alive
without creating continuous global movement
```

Important characteristics:

```text
one or two visible traces at a time
long travel durations
long quiet gaps
neutral/cool light distinct from semantic teal/orange state colors
```

### D2 Intersection Glints

Rare grid intersections briefly brighten and decay.

Intent:

```text
add micro-detail and visual richness
without directional movement across the whole canvas
```

Important characteristics:

```text
small area
short pulse
low frequency
non-synchronized timing
```

### D3 Ambient Drift

A very broad, low-opacity light field moves slowly underneath the grid.

Intent:

```text
create depth and atmosphere rather than visible event-like animation
```

Important characteristics:

```text
very slow
soft edges
low contrast
never obscures text or relations
```

### D4 Restrained Hybrid

Combines one sparse current trace, occasional glints, and a very soft drifting field.

Intent:

```text
find whether several individually subtle mechanisms produce the strongest premium result
or whether their combination crosses the line into visual noise
```

The hybrid should be intentionally restrained rather than simply summing the maximum intensity of D1-D3.

---

## 6. Semantic versus ambient comparison controls

The browser design lab should make the distinction inspectable.

Useful controls:

```text
Ambient motion ON / OFF
Semantic activity ON / OFF
Reduced motion ON / OFF
```

This allows the project owner to answer separate questions:

```text
Does the decorative layer improve the world on its own?
Can semantic activity still clearly dominate when both are present?
Does reduced motion preserve hierarchy without looking broken?
```

---

## 7. Visual hierarchy rule

The current hypothesis is:

```text
semantic activity
    strongest and clearest motion channel

selected/focused work
    strongest static emphasis

ambient dynamics
    lower contrast and slower than both

resting grid
    quietest layer
```

Ambient effects should normally use neutral cool-white / blue-white light rather than reusing state colors.

This reduces the risk that decorative light is interpreted as an active dependency or runtime event.

---

## 8. Evaluation questions

Human review should focus on direct visual judgment rather than theoretical preference.

```text
Which variant simply looks best?
Which feels most premium and advanced?
Which remains comfortable after watching it for several minutes?
Does any motion feel random or distracting?
Can you still instantly identify real semantic activity?
Would a combination of two variants be better than any single one?
Should ambient behavior become even subtler or slightly more visible?
```

Aesthetic value is explicitly legitimate evidence for this slice because the target mechanism is partly decorative by definition.

---

## 9. What remains unchanged

This selection does not alter:

```text
Specification 008 promoted interaction architecture
semantic-zoom requirement
semantic connector work still pending
work-unit visual grammar still pending
Conversation Workspace requirement
large-project stress-test requirement
source-vault pause
Course 2 gate
```

No production Cockpit component is replaced by this experiment.

---

## 10. Next action

```text
1. preserve G4 as the selected grid/world baseline
2. use dark mode only for the current dynamics evaluation
3. build D1-D4 as isolated browser-rendered variants
4. preserve explicit separation between semantic and ambient motion
5. let the project owner inspect the motion live in the browser
6. record preferred/rejected/combine/refine disposition
7. refine G4 ambient behavior if needed
8. only then open the next major visual slice, likely work-unit grammar or connector language
```
