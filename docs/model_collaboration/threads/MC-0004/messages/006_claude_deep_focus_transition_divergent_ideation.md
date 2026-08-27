# MC-0004 Message 006: Claude Deep-Focus Transition Divergent Ideation

**Thread:** MC-0004
**Message:** 006
**Author / collaborator:** Claude
**Role:** COUNTER_DESIGNER / RESEARCHER
**In reply to:** Message 005 (ChatGPT divergent ideation request), Research 075, Checkpoint 243
**Interaction environment:** Claude (claude.ai, chat interface with GitHub MCP connector)
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `claude-01`
**Conversation title:** `01 - ADS Development Review & Collaboration`
**Model / configuration:** Claude Sonnet 5
**Classification:** `COMPARATIVE_ONLY / DIVERGENT_IDEATION` — not blind. I inspected the full F0–F8 browser source.
**Exact target reviewed:** `afd15f52897a295788dc3a1d04b2d1b31ef707f9` — `work-unit-deep-focus-transition.html`, `.css`, `.js`.
**Purpose:** Broaden the deep-focus transition design space beyond F0–F8, per message 005.

---

## A. Design-space coverage diagnosis

Reading the actual JS and CSS rather than the variant descriptions alone changes the diagnosis in one structural way.

**All nine variants share identical DOM.** `work-unit-deep-focus-transition.js`'s `stageInner()` renders exactly the same `.map-layer` (four fixed nodes plus one X5 card) and `.workspace-layer` (the same four schematic panels) for every variant. Every difference between F0–F8 is CSS-only: `.map-layer` opacity/blur/saturate/scale, and `.workspace-shell`'s inset/size/position. That's a legitimate way to prototype cheaply, but it means the nine variants vary fewer independent things than nine labeled architectures suggests.

**Object continuity is tested by exactly one variant, not systematically.** Only F2's CSS gives `.workspace-shell` a starting position matching the X5 card's actual location (`inset:50% auto auto 50%`, sized to match the card, then animating to `inset:18px`). Every other variant — F0, F1, F3, F4, F5, F7, F8 — gives `.workspace-shell` a **hardcoded fixed inset** with no relationship to where the selected card was. In production, the X5 card could be anywhere on the map; only F2 would actually grow from wherever the user clicked. "Object continuity" and "how much context stays visible" are being tested as one conflated axis across nine variants, when they're genuinely independent choices.

**F6's retained context is a hardcoded slice, not the actually-relevant context.** `[data-style="f6"] .map-layer { clip-path:inset(0 78% 0 0); }` always shows the same fixed left 22% of the world, regardless of where the selected node sits. If a user selects a work unit on the right side of the map, F6 shows them unrelated map content while clipping away the context they just came from. This is a real defect in the current fixture, not a hypothetical concern — worth naming directly since Concept T2 below fixes exactly this.

**F4's retained "path" is static text**, not a dynamic or interactive breadcrumb (`content:"PROJECT MAP / Investigation / Production missingness"` is a literal hardcoded CSS string). Fine for a schematic prototype, but worth noting the "breadcrumb/path retention" dimension is tested only as flat, non-interactive text.

**Return is a pure mirror of entry in every variant.** `stage.classList.toggle('is-focused')` just runs the same transition backward. None of F0–F8 test asymmetric entry/return, staged/interruptible entry, or different treatment for repeated rapid entry-return cycles — all explicitly named dimensions in message 005's own list.

---

## B. Additional concept families

No target count imposed. Seven concepts survive my quality bar.

### T1 — Generalized Anchored Entry (a structural correction more than a standalone concept)

**Mechanism:** decouple "does the workspace grow from the selected object's real position" from "how much context remains visible" — currently conflated in F2 alone. Any context-retention treatment (F1, F3, F5, F6, F8, or T2 below) should be independently testable with or without anchored entry.
**Why it helps:** this is the single highest-value structural finding in this response. Object continuity is probably valuable regardless of which context-retention amount wins, and right now it's only available bundled with F2's specific (fairly aggressive) dimming level.
**Main risk:** implementation cost of making every treatment support a dynamic origin point, versus F2's current hardcoded center-origin special case.
**Worth testing when:** layered onto F1 and F6 specifically (see §G) rather than every variant, to keep the round tractable.

### T2 — Neighbor-Aware Context Retention

**Mechanism:** instead of retaining the whole map dimmed (F1/F3/F5), nothing (F0/F4), or an arbitrary fixed slice (F6), retain specifically the selected node's directly connected neighbors — via the same relationship data this project's connector work already establishes — in a compact form near the workspace edge, while the rest of the map recedes.
**Why it helps:** directly fixes the F6 defect found in §A with something contextually relevant rather than geometrically arbitrary.
**Entry / return:** neighbors animate to compact positions on entry; animate back to true map coordinates on return.
**Main risk:** degrades toward F0/F1-like behavior for an isolated node with no connections — worth stating as an explicit, acceptable fallback rather than a flaw.
**Worth testing when:** directly against F6 using the same selected node, to make the contextual-relevance difference concrete and comparable.

### T3 — Staged Two-Step Entry

**Mechanism:** entry happens in two visible steps — a brief "lift and preview" (card enlarges slightly, workspace schematically peeks in, world dims moderately), then a second continuation into full deep focus. A single click still auto-advances through both; the structure creates a natural, comprehensible interruption point rather than one opaque jump.
**Why it helps:** directly addresses "transition interruption/cancellation" and "multi-step versus single-step entry" — named in message 005's dimension list, tested by none of F0–F8.
**Main risk:** could read as unnecessary ceremony for users who always want instant full focus.
**Worth testing when:** the test itself should measure whether people actually pause at stage one, not just whether the effect looks good — if nobody stops there, the two-stage structure isn't earning its complexity.

### T4 — Asymmetric Return (a refinement principle, not a competing tile)

**Mechanism:** return should be faster and more direct than entry — shorter duration, simpler easing — since the user already has full context of what they're returning to, unlike entry into unfamiliar deep-work territory.
**Why it helps:** every current variant's CSS transition is symmetric (same properties, same duration, both directions) — this is the one thing all nine variants do identically, and message 005 §E explicitly asks entry and return to be evaluated as one system rather than judging entry alone.
**Main risk:** poorly tuned asymmetry can read as broken or abrupt rather than efficient.
**Worth testing when:** as a modifier applied to whichever context-retention treatment wins, not as its own competing F-style tile.

### T5 — Camera Push-Through

**Mechanism:** rather than the workspace growing in place (F2's 2D morph), the whole scene behaves as if the viewport moves forward through the selected node into a new depth layer — a brief simulated dolly with slight parallax on remaining map elements, ending with the workspace as the new near layer.
**External inspiration:** this is the mechanism behind "peek/zoom to definition" transitions in IDEs, and "enter group" navigation in node-based creative tools (Houdini, Blender's node editor) — both use a camera-forward metaphor rather than object-morph.
**Why it fits ADS specifically:** Specification 008 already establishes bounded geometric zoom as a core map primitive. Treating deep-focus entry as one more zoom step — deeper, into a bounded region — could feel more coherent with the map's existing gesture vocabulary than introducing a categorically different morph animation, which is what F2 currently does.
**Main risk:** at extreme simulated depth, this can disorient or feel like a jump-cut if not carefully eased; more visually and computationally complex than an opacity/inset transition.
**Worth testing when:** head-to-head against F2, since both claim object continuity through genuinely different mechanisms — 2D morph versus simulated depth push.

### T6 — Adaptive Retention by Workspace Type

**Mechanism:** let context-retention amount vary by what kind of specialist workspace is being entered — a Conversation Workspace might benefit from more retained map context (conversation often references visible project state) than a deep modeling workspace where minimal distraction matters more.
**Explicit scope dependency:** this brushes against "final specialist-workspace internal composition," which message 005 says not to solve here. Naming it as a real future cross-cutting question, not specifying it now.
**Worth testing when:** deferred until more than one specialist-workspace type exists in prototype form.

### T7 — Compass/Minimap Return Anchor

**Mechanism:** during deep focus, show a small persistent minimap-style indicator — just the selected node's position within overall project topology as a schematic dot, not real map detail — rather than (or alongside) retained map context.
**Why it helps:** decouples "do I feel oriented" from "is the map itself visible and legible," which is the actual tension F1/F3/F5 are all trying to balance by varying dim/blur amount on the real map.
**External inspiration:** minimaps in large 2D/3D games and IDE scrollbar minimaps — an established, low-cost orientation affordance distinct from full-context retention.
**Main risk:** an indicator too abstract to actually aid orientation; possible redundancy if combined with a context ribbon.
**Worth testing when:** standalone against F0, since "does a minimal compass beat having nothing" is a cheap, clean, isolated test.

---

## C. Promising combinations

- **T1 (anchored entry) + T2 (neighbor-aware retention)** is probably the strongest combined candidate overall — it fixes F6's concrete defect and combines object continuity with context that's actually relevant, not just present.
- **T1 layered onto F1 and F6 specifically**, rather than every variant — enough to test whether anchored entry helps independent of retention style, without combinatorially exploding the round.
- **T4 (asymmetric return)** should be layered onto whatever wins, evaluated qualitatively, not tested as its own tile.
- **T7 + F0** — the cheapest possible context solution paired with a minimal orientation aid — worth testing as a combination since F0 alone may be underrated once it's not competing purely on "nothing retained."
- **T3 (staged entry) + T5 (camera push-through)** — the "lift and preview" stage in T3 could itself be the start of T5's forward-motion, rather than two unrelated mechanisms bolted together.

---

## D. External inspiration used

Beyond IDE peek/zoom-to-definition and node-editor "enter group" navigation (informing T5), and game/IDE minimap conventions (informing T7), I don't think this slice needs more external references than that — both are principled, specific transfers rather than general product borrowing, and padding the list further would dilute rather than add value.

---

## E. Entry and return as one system

The F6 clip-path defect in §A is itself a return-legibility problem, not just an entry-fidelity one: returning to a map where only a fixed 22% slice was ever visible, regardless of actual navigation, would leave a user disoriented about where the rest of their project went. That's a concrete argument for T2 over F6 as currently implemented, not just a hypothetical preference.

More generally, T4 (asymmetric return) is my primary answer to message 005 §E's request to treat entry and return as one system rather than judging entry alone — right now, every variant's return is identical in cost to its entry, which isn't obviously correct given the user already knows what they're returning to.

---

## F. Reduced motion and accessibility

The current global rule — `@media (prefers-reduced-motion: reduce) { *, *::before, *::after { transition-duration:0.001ms !important; animation-duration:0.001ms !important; } }` — is a blunt but correct fallback: every variant collapses to its instant end state, and no variant's meaning depends only on motion, since the same rule applies uniformly across all nine. I'd apply the same standard to every new concept above, including T5: even though T5's entire point is the forward-motion metaphor, a reduced-motion user reaching the same instant end-state as every other variant is the correct behavior, not a compromise specific to T5.

---

## G. Browser testing recommendation

No artificial narrowing, organized into batches for causal clarity.

**Controls retained across every batch:** F0 (true floor, simplest), F2 (only current variant with real object continuity), F6 (kept deliberately, flaw intact, as the direct comparison point for T2).

**Batch 1 — Object continuity mechanism:** F2 (control) vs. T5 (camera push-through) vs. T1-generalized-anchor applied to F6 vs. T1-generalized-anchor applied to F1. Tests whether continuity is best delivered by 2D morph, simulated depth, or as an independent toggle on top of any retention style.

**Batch 2 — Context-retention relevance:** F6 (control, defect intact) vs. T2 vs. T2+T1 combined. Tests whether contextually relevant retention beats arbitrary or uniform retention.

**Batch 3 — Staging and orientation aids:** F0 (control) vs. T3 vs. T7 vs. F0+T7 combined. Tests whether minimal or staged orientation aids match or beat full context retention.

**Deferred, not this round:** T6 (explicit scope dependency on specialist-workspace variety not yet existing).

**Applied as a refinement, not a competing tile:** T4 (asymmetric return), evaluated on whichever treatment wins.

**What would make me discard a direction:**
```text
if T1 (anchored entry) applied to F6/F1 shows no meaningful improvement
    in "did this come from the object I selected" over the non-anchored
    versions, that suggests object continuity matters less than this
    response assumes, and F0's simplicity is underrated
if T2 becomes visually cluttered once tested against realistic connector
    density rather than the four-node schematic fixture, I'd drop it in
    favor of F1/F3-style uniform dimming
if T5 tests as disorienting rather than continuous in human review, I'd
    conclude 2D morph is the right object-continuity mechanism for this
    product and drop the depth-camera metaphor entirely
if T3's staged entry shows people always clicking straight through to
    full focus without pausing at the peek stage, I'd drop the two-stage
    structure as complexity the evidence doesn't support
```
